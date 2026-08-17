# -*- coding: utf-8 -*-
# ##############################################################################
# ⚠️ IMPORTANT NOTICE ⚠️
# ##############################################################################
# 2026-07-07: N_log saving to disk has been temporarily disabled in save_case_json()
# (commented out ("N_log", state.N_log) in the `for name, obj in [...]:` block below).
# Reason: reduce disk usage and speed up test iteration.
# To restore: uncomment the N_log line and all *-N_log.json files will be written again.
# ##############################################################################
r"""
Diagnostic_TestSet_AgentGraphReasoning_Shared_Module_v8.py
=====================================

Shared module for graph reasoning test scripts.

Import:
  from Diagnostic_TestSet_AgentGraphReasoning_Shared_Module_v8 import (
      load_test_data,          # load input JSON + algorithm JSON
      run_graph_reasoning,     # run graph reasoning on a single case
      compute_consistency,     # compute 4 types of consistency
      save_case_json,          # save case-level JSON output
      generate_md_report,      # generate 00-Overall_Statistics.md
      GRAPH_PATH,              # common graph path
      OUTPUT_DIR,              # output root directory
      DEFAULT_TOPK,            # default K for TopK consistency
  )

Graph reasoning modules:
  - v7_modules located at ../AgentGraphReasoning/v7_modules/
  - Each .py file is located in ../TestSetConstruction-NormalTest/, requires two levels up
"""

import os
import sys
import json
import copy
import time
from pathlib import Path
from datetime import datetime
from typing import Any

# ============================================================
# Dynamically add module path
# ============================================================
_CURRENT_FILE = Path(__file__).resolve()
# Shared module is located at IncompleteGraph_ReasoningTest/, v7_modules at IncompleteGraph_ReasoningTest/AgentGraphReasoning/v7_modules
_MODULE_DIR = _CURRENT_FILE.parent / "AgentGraphReasoning" / "v7_modules"
if str(_MODULE_DIR) not in sys.path:
    sys.path.insert(0, str(_MODULE_DIR.parent))

# ============================================================
# Import v7 modules
# ============================================================
import v7_modules  # noqa: F401
from v7_modules import m00_config as cfg
from v7_modules import m01_schemas as schemas
from v7_modules import m02_graph_io as graph_io
from v7_modules import m04_background_parser as bg_parser
from v7_modules import m05_node_matcher as node_matcher
from v7_modules import m06_explore as explore_mod
from v7_modules import m07_aggregate as aggregate_mod
from v7_modules import m08_prune as prune_mod
from v7_modules import m09_recommend as recommend_mod

# ============================================================
# Default constants
# ============================================================
DEFAULT_TOPK = 3  # Default K value for TopK consistency

import os as _os_algo
from pathlib import Path as _Path_algo

_ALGO_REPO_ROOT = _Path_algo(__file__).resolve().parents[2]


def _resolve_algo(env_var: str, default_relpath: str) -> str:
    override = _os_algo.environ.get(env_var)
    if override:
        return override
    return str(_ALGO_REPO_ROOT / default_relpath)


# Source-papers metadata file. The aggregated CEG (with nodes/edges) is produced
# by the CEG construction pipeline and is not bundled here.
GRAPH_PATH = _resolve_algo(
    "BFGA_GRAPH_PATH",
    "data/CEG data/CEG data for 2027cases.json",
)

OUTPUT_DIR = _resolve_algo(
    "BFGA_OUTPUT_DIR",
    "data/output",
)

# ============================================================
# Auxiliary utility functions
# ============================================================

def save_json(obj: Any, path: str) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2, default=str)


def _to_serializable(obj: Any) -> Any:
    if hasattr(obj, "__dict__"):
        return _to_serializable(obj.__dict__)
    if isinstance(obj, dict):
        return {k: _to_serializable(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_to_serializable(item) for item in obj]
    return obj


def should_terminate(
    epoch_idx: int,
    Thinking_belief: float,
    config: dict,
    pruning_result: dict = None,
) -> bool:
    if epoch_idx >= config.get("Epoch_max", 5):
        return True
    if Thinking_belief >= config.get("Thinking_belief_threshold", 0.99):
        return True
    if pruning_result is not None:
        if pruning_result.get("pruning_status") == "failure":
            return True
        if len(pruning_result.get("next_node_ids", [])) == 0:
            return True
    return False


def write_termination_log(
    state: schemas.ReasoningState,
    epoch_idx: int,
    Thinking_belief: float,
    termination_reason: str,
    config: dict,
) -> None:
    epoch_key = f"Epoch{epoch_idx}"
    state.N_log["termination_log"] = {
        "terminated": True,
        "epoch_key": epoch_key,
        "Thinking_belief": round(Thinking_belief, 6),
        "Thinking_belief_threshold": config.get("Thinking_belief_threshold", 0.99),
        "termination_reason": termination_reason,
        "storage_target": "N_log.termination_log",
    }


# ============================================================
# Data loading
# ============================================================

def load_test_data(input_json_path: str, alg_json_path: str) -> tuple[dict, list[dict]]:
    """Load input JSON and algorithm JSON.

    Input JSON format:
      { case_id: [ { constraint_id, node_id, node_type, node_name, ... }, ... ], ... }

    Algorithm JSON format:
      { case_id: [ { alg_id, node_type, node_name, node_description }, ... ], ... }

    Returns:
        input_data: dict[case_id -> list of input nodes]
        alg_data:   list of ground-truth algorithm nodes (aggregated from all cases)
    """
    with open(input_json_path, "r", encoding="utf-8") as f:
        input_data = json.load(f)

    with open(alg_json_path, "r", encoding="utf-8") as f:
        alg_raw = json.load(f)

    # Aggregate standard algorithm nodes from all cases
    alg_data: list[dict] = []
    for case_nodes in alg_raw.values():
        alg_data.extend(case_nodes)

    return input_data, alg_data


# ============================================================
# Graph reasoning core process
# ============================================================

def match_fact_nodes_to_graph(
    Background_json: list[dict],
    graph: dict,
    config: dict,
    node_idx: dict[str, dict],
    candidates_by_type: dict[str, list[dict]] | None = None,
) -> tuple[list[dict], dict]:
    """Match input fact nodes with the graph, return match results and log.

    Optimization note (performance):
      - Caller can pre-bucket nodes by node_type and pass candidates_by_type to avoid
        full table linear scan of graph["nodes"] for each constraint.
      - When not provided, fallback to original behavior (backward compatible).
    """
    results = []
    match_log = {
        "total_input": len(Background_json),
        "program_matched": 0,
        "llm_matched": 0,
        "not_matched": 0,
        "details": [],
    }

    for constraint in Background_json:
        result = node_matcher.program_match_node(
            constraint, graph, config, node_idx,
            candidates_by_type=candidates_by_type,
        )

        if result["match_status"] in (
            "need_llm_fallback_same_node_type",
            "need_llm_fallback_no_same_node_type",
        ):
            b_type = constraint.get("node_type", "")
            if candidates_by_type is not None:
                candidates = candidates_by_type.get(b_type, [])
            else:
                candidates = [n for n in graph["nodes"] if n.get("node_type", "") == b_type]
            fallback_result = node_matcher.llm_fallback_match_node(constraint, candidates)
            if fallback_result["matched_node_id"] is not None:
                result.update(fallback_result)

        results.append(result)

        if result["matched_node_id"]:
            if result["match_method"] == "program_matched":
                match_log["program_matched"] += 1
            else:
                match_log["llm_matched"] += 1
        else:
            match_log["not_matched"] += 1

        match_log["details"].append({
            "constraint_id": result.get("constraint_id", ""),
            "node_type": constraint.get("node_type", ""),
            "node_name": constraint.get("node_name", ""),
            "matched_node_id": result.get("matched_node_id"),
            "matched_node_name": result.get("matched_node_name"),
            "match_method": result.get("match_method", ""),
            "similarity": result.get("similarity", 0.0),
            "llm_reason": result.get("llm_reason"),
        })

    return results, match_log


def _populate_epoch_logs(state: schemas.ReasoningState, node_idx: dict[str, dict]) -> None:
    """Extract data from N_vote and N_pruning to populate state.N_log["epoch_logs"].

    Fields required by Region 3 table:
      - participating_node_count       : number of participating nodes
      - participating_node_type_count  : deduplicated number of participating node_types
      - Thinking_belief                : overall recommendation belief
      - pruning.fact_sufficiency_A     : fact sufficiency A
      - pruning.pruning_strategy       : pruning strategy
      - pruning.pruning_status         : status
      - pruning.feedback_time          : number of backtracking iterations
    """
    for epoch_key, vote_data in state.N_vote.items():
        if epoch_key not in state.N_log["epoch_logs"]:
            state.N_log["epoch_logs"][epoch_key] = {}

        log = state.N_log["epoch_logs"][epoch_key]

        # Overall recommendation belief
        log["Thinking_belief"] = vote_data.get("Thinking_belief", 0.0)

        # Participating node count and deduplicated node_type count
        # Get participating node list from N_Explore[epoch_key]
        explore_data = state.N_Explore.get(epoch_key, {})
        node_ids = list(explore_data.keys())
        log["participating_node_count"] = len(node_ids)

        covered_types = set()
        for nid in node_ids:
            node = node_idx.get(nid)
            if node:
                nt = node.get("node_type", "")
                if nt:
                    covered_types.add(nt)
        log["participating_node_type_count"] = len(covered_types)

        # Pruning info: find the corresponding epoch record from N_pruning
        for pruning_entry in state.N_pruning:
            if pruning_entry.get("Epoch") == epoch_key:
                log["pruning"] = {
                    "fact_sufficiency_A": pruning_entry.get("fact_sufficiency_A", ""),
                    "pruning_strategy": pruning_entry.get("pruning_strategy", ""),
                    "pruning_status": pruning_entry.get("pruning_status", ""),
                    "feedback_time": len(pruning_entry.get("feedback_details", [])),
                }
                break


def run_graph_reasoning(
    case_id: str,
    input_nodes: list[dict],
    graph: dict,
    config: dict,
    run_id: str,
    output_case_dir: str,
    scenario_label: str = "placeholder scenario",
) -> tuple[schemas.ReasoningState, list[dict], dict]:
    """Run one round of graph reasoning for a single case.

    Parameters:
        case_id:       case identifier
        input_nodes:   list of input fact nodes (from input JSON)
        graph:         common graph
        config:        inference hyperparameter configuration
        run_id:        unique identifier for this run
        output_case_dir: case output directory

    Returns:
        (state, match_results, match_log)
    """
    state = schemas.new_reasoning_state()
    state.Background_string = f"[TEST CASE {case_id}] {scenario_label}"
    state.Background_json = input_nodes
    state.N_log["meta"] = {
        "run_id": run_id,
        "case_id": case_id,
        "scenario": scenario_label,
        "timestamp_start": datetime.now().isoformat(),
        "input_mode": "pre_extracted_fact_nodes",
        "version": "v8",
    }

    node_idx = graph_io.build_node_index(graph)
    edge_idx = graph_io.build_edge_index(graph)

    # Optimization (performance): pre-build adjacency list and pre-bucketed node list by node_type.
    # These two structures are reused throughout the case reasoning process, avoiding repeated
    # full graph/table scans by downstream functions.
    adjacency = graph_io.build_adjacency(graph)
    candidates_by_type: dict[str, list[dict]] = {}
    for n in graph["nodes"]:
        nt = n.get("node_type", "")
        if nt:
            candidates_by_type.setdefault(nt, []).append(n)

    # Node matching
    match_results, match_log = match_fact_nodes_to_graph(
        input_nodes, graph, config, node_idx,
        candidates_by_type=candidates_by_type,
    )

    # Initialize Epoch1 exploration nodes
    state.N_Explore["Epoch1"] = {}
    for result in match_results:
        nid = result.get("matched_node_id")
        if nid:
            state.N_Explore["Epoch1"][nid] = {
                "candidate_edge_ids": [],
                "source": "background_match",
                "matched_from": result.get("constraint_id", ""),
            }

    for result in match_results:
        state.N_log["node_match_log"].append({
            "constraint_id": result.get("constraint_id", ""),
            "candidate_nodes": [],
            "matched_node_id": result.get("matched_node_id"),
            "matched_node_name": result.get("matched_node_name"),
            "match_method": result.get("match_method", ""),
            "similarity": result.get("similarity", 0.0),
            "llm_reason": result.get("llm_reason"),
            "warnings": result.get("warnings", []),
        })

    state.N_log["meta"]["match_summary"] = match_log

    # Epoch main loop
    Thinking_belief = config.get("Thinking_belief_init", 0.0)
    Epoch_max = config.get("Epoch_max", 5)

    for epoch_idx in range(1, Epoch_max + 1):
        epoch_key = f"Epoch{epoch_idx}"
        next_epoch_key = f"Epoch{epoch_idx + 1}"

        if epoch_key not in state.N_log["epoch_logs"]:
            state.N_log["epoch_logs"][epoch_key] = {}

        # Exploration
        explore_mod.explore_edges_for_epoch(state, epoch_key, graph, adjacency=adjacency)

        # Aggregation
        vote_result = aggregate_mod.aggregate_vote_for_epoch(
            state, epoch_key, graph, config, edge_idx, node_idx
        )
        Thinking_belief = vote_result.get("Thinking_belief", 0.0)

        # Pruning
        pruning_result = prune_mod.prune_for_next_epoch(
            state, epoch_key, next_epoch_key, graph, config,
            edge_idx, node_idx, epoch_idx,
            adjacency=adjacency,
        )
        selected_count = len(pruning_result.get("next_node_ids", []))

        if selected_count == 0:
            write_termination_log(
                state, epoch_idx, Thinking_belief, "no_next_nodes", config
            )
            break

        # Termination check
        if should_terminate(epoch_idx, Thinking_belief, config, pruning_result):
            if Thinking_belief >= config.get("Thinking_belief_threshold", 0.99):
                reason = "thinking_belief_reached_threshold"
            elif epoch_idx >= Epoch_max:
                reason = "max_epoch_reached"
            elif pruning_result.get("pruning_status") == "failure":
                reason = "pruning_feedback_failure"
            else:
                reason = "unknown"
            write_termination_log(state, epoch_idx, Thinking_belief, reason, config)
            break

        state.N_Explore[next_epoch_key] = {
            nid: {
                "candidate_edge_ids": [],
                "source": f"pruning_from_{epoch_key}",
            }
            for nid in pruning_result["next_node_ids"]
        }

    # Recommendation
    N_recommend = recommend_mod.generate_recommendation(
        state, graph, config, node_idx
    )

    # Populate epoch_logs (for MD report Region 3)
    _populate_epoch_logs(state, node_idx)

    # Save JSON
    state.N_log["meta"]["timestamp_end"] = datetime.now().isoformat()

    return state, match_results, match_log


# ============================================================
# Save case-level JSON output
# ============================================================

def save_case_json(
    case_id: str,
    state: schemas.ReasoningState,
    consistency_result: dict,
    output_case_dir: str,
) -> None:
    """Save case-level JSON output files."""
    os.makedirs(output_case_dir, exist_ok=True)
    prefix = f"{case_id}"

    # ⚠️ 2026-07-07: Temporarily commented out N_log saving to reduce disk usage
    # To restore, add N_log back to the list below.
    for name, obj in [
        ("N_Explore", state.N_Explore),
        ("N_vote", state.N_vote),
        ("N_pruning", state.N_pruning),
        ("N_recommend", state.N_recommend),
        # ("N_log", state.N_log),
    ]:
        try:
            path = os.path.join(output_case_dir, f"{prefix}-{name}.json")
            save_json(_to_serializable(obj), path)
        except Exception as e:
            print(f"    [ERROR] Failed to save {name}: {e}")

    try:
        path = os.path.join(output_case_dir, f"{prefix}_consistency_report.json")
        save_json(consistency_result, path)
    except Exception as e:
        print(f"    [ERROR] Failed to save consistency: {e}")


# ============================================================
# Consistency computation (4 types)
# ============================================================

def _is_invalid_ground_truth_name(name: Any) -> bool:
    if not isinstance(name, str):
        return True
    normalized = name.strip()
    if not normalized:
        return True
    return "not mentioned" in normalized


def _is_specific_recommendation(info: dict | None) -> bool:
    if not info:
        return False
    name = info.get("node_name", "")
    if isinstance(name, str) and name.strip():
        return True
    node_id = info.get("node_id")
    if isinstance(node_id, str) and node_id.strip():
        return True
    return False


def _compute_gt_by_type(
    ground_truth_algorithms: list[dict],
) -> dict[str, dict]:
    """Aggregate ground_truth_algorithms by node_type and take Top-1 of each node_type."""
    by_type: dict[str, dict] = {}
    for gt in ground_truth_algorithms:
        nt = gt["node_type"]
        if nt not in by_type:
            by_type[nt] = gt
    return by_type


def _compute_gt_topk_by_type(
    ground_truth_algorithms: list[dict],
    topk: int = 3,
) -> dict[str, list[dict]]:
    """Aggregate ground_truth_algorithms by node_type and take Top-K of each node_type (sorted by score)."""
    by_type: dict[str, list[dict]] = {}
    for gt in ground_truth_algorithms:
        nt = gt["node_type"]
        if nt not in by_type:
            by_type[nt] = []
        by_type[nt].append(gt)
    # Take top K of each type (sorted by node_name alphabetically for stable order)
    for nt in by_type:
        by_type[nt] = by_type[nt][:topk]
    return by_type


def _get_topk_candidates_from_vote(
    N_vote: dict,
    node_idx: dict[str, dict],
    topk: int = 3,
) -> dict[str, list[dict]]:
    """Extract Top-K candidates for each recommended node_type from N_vote.

    Returns:
        { node_type: [ {node_id, node_name, vote_ratio}, ... ] }
    """
    if not N_vote:
        return {}

    latest_key = max(N_vote.keys(), key=lambda k: int(k.replace("Epoch", "")))
    by_algorithm_type = N_vote[latest_key].get("by_algorithm_type", {})

    result: dict[str, list[dict]] = {}
    for alg_type, vote_data in by_algorithm_type.items():
        candidates = vote_data.get("Top_K", [])
        # Enrich with node_name
        enriched = []
        for c in candidates[:topk]:
            nid = c.get("node_id", "")
            node = node_idx.get(nid, {})
            enriched.append({
                "node_id": nid,
                "node_name": c.get("node_name", node.get("node_name", "")),
                "vote_ratio": c.get("vote_ratio", 0.0),
            })
        result[alg_type] = enriched

    return result


# ---- Consistency 1: Strict Consistency ----
def check_strict_consistency(
    N_recommend: dict,
    N_vote: dict,
    ground_truth_algorithms: list[dict],
    node_idx: dict[str, dict],
    topk: int = 3,
) -> dict:
    """
    Strict consistency:

    Decision rules:
      - GT category exists (not filtered out) AND Top1 exact match OR GT in TopK
        and GT.vote_ratio == Top1.vote_ratio (tied highest) → hit
      - GT category exists (not filtered out) AND Top1 is not GT and not tied highest in TopK → miss
      - GT category exists but is filtered out (gt and not rec) → miss
      - Recommended category exceeds GT categories (rec and not gt) → miss

    match_rate = hits / (effective_GT_categories + rec-only_categories)
    - Effective GT categories: invalid GT (name "not mentioned" etc.) not counted
    - gt-only: counted as missed (filtered category counts as wrong)
    - rec-only: counted as extra (extra category counts as wrong)
    """
    gt_by_type = _compute_gt_by_type(ground_truth_algorithms)
    rec_by_type: dict[str, dict] = {}
    for alg_type, info in N_recommend.items():
        rec_by_type[alg_type] = info

    # Extract TopK candidates and Top1 vote_ratio from N_vote for tied highest determination
    vote_topk = _get_topk_candidates_from_vote(N_vote, node_idx, topk)

    all_types = sorted(set(list(gt_by_type.keys()) + list(rec_by_type.keys())))

    by_type_result = {}
    matched = missed = extra = 0
    invalid_gt_excluded = 0
    effective_total_gt = 0  # Number of non-invalid GT categories

    for alg_type in all_types:
        gt = gt_by_type.get(alg_type)
        rec = rec_by_type.get(alg_type)
        rec_name = rec["node_name"].strip() if rec and rec.get("node_name") else ""
        gt_name = gt["node_name"].strip() if gt and gt.get("node_name") else ""

        if gt:
            gt_invalid = _is_invalid_ground_truth_name(gt_name)
            if gt_invalid:
                invalid_gt_excluded += 1
                # Invalid GT: recommended specific algorithm counts as extra, not recommended is not wrong
                if _is_specific_recommendation(rec):
                    extra += 1
                    by_type_result[alg_type] = {
                        "ground_truth": {
                            "node_type": gt["node_type"],
                            "node_name": gt_name,
                            "is_invalid_node": True,
                        },
                        "recommended": {
                            "node_id": rec.get("node_id", ""),
                            "node_name": rec_name,
                            "vote_ratio": rec.get("vote_ratio", 0.0),
                        } if rec else None,
                        "match_status": "invalid_gt_over_recommended",
                        "strict_match": False,
                    }
                else:
                    by_type_result[alg_type] = {
                        "ground_truth": {
                            "node_type": gt["node_type"],
                            "node_name": gt_name,
                            "is_invalid_node": True,
                        },
                        "recommended": None,
                        "match_status": "invalid_gt_not_recommended",
                        "strict_match": True,
                    }
                continue

            effective_total_gt += 1

        # Compute Top1 vote_ratio and whether GT is tied highest in TopK
        candidates = vote_topk.get(alg_type, [])
        top1_vote_ratio = rec.get("vote_ratio", 0.0) if rec else 0.0
        gt_in_topk = any(
            c.get("node_name", "").strip() == gt_name for c in candidates
        )
        gt_in_topk_top_ratio = False
        if gt_in_topk:
            for c in candidates:
                if c.get("node_name", "").strip() == gt_name:
                    if abs(float(c.get("vote_ratio", 0.0)) - float(top1_vote_ratio)) < 1e-9:
                        gt_in_topk_top_ratio = True
                    break

        if gt and rec:
            is_exact_match = (gt_name == rec_name)
            if is_exact_match:
                status = "exact_match"
                matched += 1
            elif gt_in_topk_top_ratio:
                status = "tied_top_ratio_in_topk"
                matched += 1
            else:
                status = "name_mismatch"
                missed += 1
            by_type_result[alg_type] = {
                "ground_truth": {
                    "node_type": gt["node_type"],
                    "node_name": gt_name,
                    "is_invalid_node": False,
                },
                "recommended": {
                    "node_id": rec["node_id"],
                    "node_name": rec_name,
                    "vote_ratio": rec["vote_ratio"],
                    "topk_candidates": candidates,
                },
                "match_status": status,
                "strict_match": (is_exact_match or gt_in_topk_top_ratio),
            }
        elif gt and not rec:
            # GT category exists but is filtered out → miss, counted as missed
            by_type_result[alg_type] = {
                "ground_truth": {
                    "node_type": gt["node_type"],
                    "node_name": gt_name,
                    "is_invalid_node": False,
                },
                "recommended": None,
                "topk_candidates": candidates,
                "match_status": "missed",
                "strict_match": False,
            }
            missed += 1
        elif rec and not gt:
            # Recommended category exceeds GT category → miss, counted as extra
            by_type_result[alg_type] = {
                "ground_truth": None,
                "recommended": {
                    "node_id": rec["node_id"],
                    "node_name": rec_name,
                    "vote_ratio": rec.get("vote_ratio", 0.0),
                },
                "match_status": "extra_recommended",
                "strict_match": False,
            }
            extra += 1

    total_gt = len(gt_by_type)
    total_rec = len(rec_by_type)
    # Strict denominator: effective GT categories + rec-only categories
    denominator = effective_total_gt + extra

    return {
        "type": "strict",
        "topk": 1,
        "total_ground_truth": total_gt,
        "effective_ground_truth": effective_total_gt,
        "invalid_ground_truth": invalid_gt_excluded,
        "total_recommended": total_rec,
        "exact_match": matched,
        "missed": missed,
        "extra_recommended": extra,
        "invalid_gt_excluded": invalid_gt_excluded,
        "match_rate": round(matched / max(denominator, 1), 4),
        "by_type": by_type_result,
    }


# ---- Consistency 2: TopK Strict Consistency ----
def check_topk_strict_consistency(
    N_recommend: dict,
    N_vote: dict,
    ground_truth_algorithms: list[dict],
    node_idx: dict[str, dict],
    topk: int = 3,
) -> dict:
    """
    TopK strict consistency:

    Decision rules:
      - GT category exists (not filtered out) AND GT in TopK candidates → hit
      - GT category exists (not filtered out) AND GT not in TopK candidates → miss
      - GT category exists but is filtered out (gt and not candidates) → miss
      - Recommended category exceeds GT categories (rec and not gt) → miss

    match_rate = hits / (effective_GT_categories + rec-only_categories)
    - Effective GT categories: invalid GT (name "not mentioned" etc.) not counted
    - gt-only: counted as missed (filtered category counts as wrong)
    - rec-only: counted as extra (extra category counts as wrong)
    """
    gt_by_type = _compute_gt_by_type(ground_truth_algorithms)
    # Get TopK candidates from N_vote
    vote_topk = _get_topk_candidates_from_vote(N_vote, node_idx, topk)

    rec_by_type: dict[str, dict] = {}
    for alg_type, info in N_recommend.items():
        rec_by_type[alg_type] = info

    all_types = sorted(set(list(gt_by_type.keys()) + list(rec_by_type.keys())))

    by_type_result = {}
    matched = missed = extra = 0
    invalid_gt_excluded = 0
    effective_total_gt = 0

    for alg_type in all_types:
        gt = gt_by_type.get(alg_type)
        rec = rec_by_type.get(alg_type)
        gt_name = gt["node_name"].strip() if gt and gt.get("node_name") else ""
        rec_name = rec["node_name"].strip() if rec and rec.get("node_name") else ""

        # TopK candidates list
        candidates = vote_topk.get(alg_type, [])
        candidate_names = {c.get("node_name", "").strip() for c in candidates}
        # Also add Top1's node_name to candidates
        if rec_name:
            candidate_names.add(rec_name)

        if gt:
            gt_invalid = _is_invalid_ground_truth_name(gt_name)
            if gt_invalid:
                invalid_gt_excluded += 1
                # Invalid GT: recommended specific algorithm counts as extra, not recommended is not wrong
                if _is_specific_recommendation(rec):
                    extra += 1
                    by_type_result[alg_type] = {
                        "ground_truth": {
                            "node_type": gt["node_type"],
                            "node_name": gt_name,
                            "is_invalid_node": True,
                        },
                        "recommended": {
                            "node_id": rec.get("node_id", ""),
                            "node_name": rec_name,
                            "vote_ratio": rec.get("vote_ratio", 0.0),
                            "topk_candidates": candidates,
                        } if rec else None,
                        "match_status": "invalid_gt_over_recommended",
                        "topk_strict_match": False,
                    }
                else:
                    by_type_result[alg_type] = {
                        "ground_truth": {
                            "node_type": gt["node_type"],
                            "node_name": gt_name,
                            "is_invalid_node": True,
                        },
                        "recommended": None,
                        "match_status": "invalid_gt_not_recommended",
                        "topk_strict_match": True,
                    }
                continue

            effective_total_gt += 1

        if gt and candidates:
            is_hit = gt_name in candidate_names
            if is_hit:
                status = "topk_hit"
                matched += 1
            else:
                status = "topk_miss"
                missed += 1
            by_type_result[alg_type] = {
                "ground_truth": {
                    "node_type": gt["node_type"],
                    "node_name": gt_name,
                    "is_invalid_node": False,
                },
                "recommended": {
                    "node_id": rec.get("node_id", ""),
                    "node_name": rec_name,
                    "vote_ratio": rec.get("vote_ratio", 0.0),
                    "topk_candidates": candidates,
                } if rec else None,
                "match_status": status,
                "topk_strict_match": is_hit,
            }
        elif gt and not candidates:
            # GT category exists but is filtered out (no candidates) → miss, counted as missed
            by_type_result[alg_type] = {
                "ground_truth": {
                    "node_type": gt["node_type"],
                    "node_name": gt_name,
                    "is_invalid_node": False,
                },
                "recommended": None,
                "match_status": "missed",
                "topk_strict_match": False,
            }
            missed += 1
        elif rec and not gt:
            # Recommended category exceeds GT category → miss, counted as extra
            # Use rec not candidates for judgment, because even if vote is empty but rec has
            # recommendation it counts as extra
            by_type_result[alg_type] = {
                "ground_truth": None,
                "recommended": {
                    "node_id": rec.get("node_id", "") if rec else "",
                    "node_name": rec_name,
                    "vote_ratio": rec.get("vote_ratio", 0.0) if rec else 0.0,
                    "topk_candidates": candidates,
                },
                "match_status": "extra_recommended",
                "topk_strict_match": False,
            }
            extra += 1

    total_gt = len(gt_by_type)
    total_rec = len(rec_by_type)
    # Strict denominator: effective GT categories + rec-only categories
    denominator = effective_total_gt + extra

    return {
        "type": "topk_strict",
        "topk": topk,
        "total_ground_truth": total_gt,
        "effective_ground_truth": effective_total_gt,
        "invalid_ground_truth": invalid_gt_excluded,
        "total_recommended": total_rec,
        "topk_hit": matched,
        "missed": missed,
        "extra_recommended": extra,
        "invalid_gt_excluded": invalid_gt_excluded,
        "match_rate": round(matched / max(denominator, 1), 4),
        "by_type": by_type_result,
    }


# ---- Consistency 3: Relaxed Consistency ----
def check_relaxed_consistency(
    N_recommend: dict,
    N_vote: dict,
    ground_truth_algorithms: list[dict],
    node_idx: dict[str, dict],
    topk: int = 3,
) -> dict:
    """
    Relaxed consistency:

    Decision rules:
      - GT category exists (not filtered out) AND Top1 exact match OR GT in TopK
        and GT.vote_ratio == Top1.vote_ratio (tied highest) → hit
      - GT category exists (not filtered out) AND Top1 is not GT and not tied highest in TopK → miss
      - GT category exists but is filtered out (gt and not rec) → ignored, not counted in percentage
      - Recommended category exceeds GT categories (rec and not gt) → ignored, not counted in percentage

    match_rate = hit intersection categories / intersection categories (only for categories
    where GT and rec both exist)
    - gt-only: ignored, not in denominator
    - rec-only: ignored, not in denominator
    - invalid GT: ignored (not in intersection)
    """
    gt_by_type = _compute_gt_by_type(ground_truth_algorithms)
    rec_by_type: dict[str, dict] = {}
    for alg_type, info in N_recommend.items():
        rec_by_type[alg_type] = info

    vote_topk = _get_topk_candidates_from_vote(N_vote, node_idx, topk)

    all_types = sorted(set(list(gt_by_type.keys()) + list(rec_by_type.keys())))

    by_type_result = {}
    matched = missed = 0
    gt_only_count = rec_only_count = invalid_gt_excluded = 0
    # Relaxed denominator: effective intersection of GT and rec (excluding invalid GT)
    effective_intersection = 0

    for alg_type in all_types:
        gt = gt_by_type.get(alg_type)
        rec = rec_by_type.get(alg_type)
        rec_name = rec["node_name"].strip() if rec and rec.get("node_name") else ""
        gt_name = gt["node_name"].strip() if gt and gt.get("node_name") else ""

        if gt:
            gt_invalid = _is_invalid_ground_truth_name(gt_name)
            if gt_invalid:
                invalid_gt_excluded += 1
                # Invalid GT: ignored regardless of recommendation
                if _is_specific_recommendation(rec):
                    rec_only_count += 1
                    by_type_result[alg_type] = {
                        "ground_truth": {
                            "node_type": gt["node_type"],
                            "node_name": gt_name,
                            "is_invalid_node": True,
                        },
                        "recommended": {
                            "node_id": rec.get("node_id", ""),
                            "node_name": rec_name,
                            "vote_ratio": rec.get("vote_ratio", 0.0),
                        } if rec else None,
                        "match_status": "invalid_gt_ignored",
                        "relaxed_match": None,
                    }
                else:
                    by_type_result[alg_type] = {
                        "ground_truth": {
                            "node_type": gt["node_type"],
                            "node_name": gt_name,
                            "is_invalid_node": True,
                        },
                        "recommended": None,
                        "match_status": "invalid_gt_ignored",
                        "relaxed_match": None,
                    }
                continue

        # Compute Top1 vote_ratio and whether GT is tied highest in TopK
        candidates = vote_topk.get(alg_type, [])
        top1_vote_ratio = rec.get("vote_ratio", 0.0) if rec else 0.0
        gt_in_topk = any(
            c.get("node_name", "").strip() == gt_name for c in candidates
        )
        gt_in_topk_top_ratio = False
        if gt_in_topk:
            for c in candidates:
                if c.get("node_name", "").strip() == gt_name:
                    if abs(float(c.get("vote_ratio", 0.0)) - float(top1_vote_ratio)) < 1e-9:
                        gt_in_topk_top_ratio = True
                    break

        if gt and rec:
            # Intersection category: counted in relaxed denominator
            effective_intersection += 1
            is_exact_match = (gt_name == rec_name)
            if is_exact_match:
                status = "exact_match"
                matched += 1
            elif gt_in_topk_top_ratio:
                status = "tied_top_ratio_in_topk"
                matched += 1
            else:
                status = "name_mismatch"
                missed += 1
            by_type_result[alg_type] = {
                "ground_truth": {
                    "node_type": gt["node_type"],
                    "node_name": gt_name,
                    "is_invalid_node": False,
                },
                "recommended": {
                    "node_id": rec["node_id"],
                    "node_name": rec_name,
                    "vote_ratio": rec["vote_ratio"],
                    "topk_candidates": candidates,
                },
                "match_status": status,
                "relaxed_match": (is_exact_match or gt_in_topk_top_ratio),
            }
        elif gt and not rec:
            # GT category not recommended → ignored, not in denominator
            gt_only_count += 1
            by_type_result[alg_type] = {
                "ground_truth": {
                    "node_type": gt["node_type"],
                    "node_name": gt_name,
                    "is_invalid_node": False,
                },
                "recommended": None,
                "topk_candidates": candidates,
                "match_status": "gt_only_ignored",
                "relaxed_match": None,
            }
        elif rec and not gt:
            # Recommended category exceeds GT → ignored, not in denominator
            rec_only_count += 1
            by_type_result[alg_type] = {
                "ground_truth": None,
                "recommended": {
                    "node_id": rec["node_id"],
                    "node_name": rec_name,
                    "vote_ratio": rec.get("vote_ratio", 0.0),
                },
                "match_status": "rec_only_ignored",
                "relaxed_match": None,
            }

    total_gt = len(gt_by_type)
    total_rec = len(rec_by_type)

    return {
        "type": "relaxed",
        "topk": 1,
        "total_ground_truth": total_gt,
        "effective_intersection": effective_intersection,
        "invalid_ground_truth": invalid_gt_excluded,
        "total_recommended": total_rec,
        "exact_match": matched,
        "missed": missed,
        "gt_only_ignored": gt_only_count,
        "rec_only_ignored": rec_only_count,
        "invalid_gt_ignored": invalid_gt_excluded,
        "match_rate": round(matched / max(effective_intersection, 1), 4),
        "by_type": by_type_result,
    }


# ---- Consistency 4: TopK Relaxed Consistency ----
def check_topk_relaxed_consistency(
    N_recommend: dict,
    N_vote: dict,
    ground_truth_algorithms: list[dict],
    node_idx: dict[str, dict],
    topk: int = 3,
) -> dict:
    """
    TopK relaxed consistency:

    Decision rules:
      - GT category exists (not filtered out) AND GT in TopK candidates → hit
      - GT category exists (not filtered out) AND GT not in TopK candidates → miss
      - GT category exists but is filtered out (gt and not candidates) → ignored, not in percentage
      - Recommended category exceeds GT categories (rec and not gt) → ignored, not in percentage

    match_rate = hit intersection categories / intersection categories (only for categories
    where GT and rec both exist)
    - gt-only: ignored, not in denominator
    - rec-only: ignored, not in denominator
    - invalid GT: ignored (not in intersection)
    """
    gt_by_type = _compute_gt_by_type(ground_truth_algorithms)
    vote_topk = _get_topk_candidates_from_vote(N_vote, node_idx, topk)

    rec_by_type: dict[str, dict] = {}
    for alg_type, info in N_recommend.items():
        rec_by_type[alg_type] = info

    all_types = sorted(set(list(gt_by_type.keys()) + list(rec_by_type.keys())))

    by_type_result = {}
    matched = missed = 0
    gt_only_count = rec_only_count = invalid_gt_excluded = 0
    # Relaxed denominator: effective intersection of GT and rec (excluding invalid GT)
    effective_intersection = 0

    for alg_type in all_types:
        gt = gt_by_type.get(alg_type)
        rec = rec_by_type.get(alg_type)
        gt_name = gt["node_name"].strip() if gt and gt.get("node_name") else ""
        rec_name = rec["node_name"].strip() if rec and rec.get("node_name") else ""

        candidates = vote_topk.get(alg_type, [])
        candidate_names = {c.get("node_name", "").strip() for c in candidates}
        if rec_name:
            candidate_names.add(rec_name)

        if gt:
            gt_invalid = _is_invalid_ground_truth_name(gt_name)
            if gt_invalid:
                invalid_gt_excluded += 1
                # Invalid GT: ignored regardless of recommendation
                if _is_specific_recommendation(rec):
                    rec_only_count += 1
                    by_type_result[alg_type] = {
                        "ground_truth": {
                            "node_type": gt["node_type"],
                            "node_name": gt_name,
                            "is_invalid_node": True,
                        },
                        "recommended": {
                            "node_id": rec.get("node_id", ""),
                            "node_name": rec_name,
                            "vote_ratio": rec.get("vote_ratio", 0.0),
                            "topk_candidates": candidates,
                        } if rec else None,
                        "match_status": "invalid_gt_ignored",
                        "topk_relaxed_match": None,
                    }
                else:
                    by_type_result[alg_type] = {
                        "ground_truth": {
                            "node_type": gt["node_type"],
                            "node_name": gt_name,
                            "is_invalid_node": True,
                        },
                        "recommended": None,
                        "match_status": "invalid_gt_ignored",
                        "topk_relaxed_match": None,
                    }
                continue

        if gt and candidates:
            # Intersection category: counted in relaxed denominator
            effective_intersection += 1
            is_hit = gt_name in candidate_names
            if is_hit:
                status = "topk_hit"
                matched += 1
            else:
                status = "topk_miss"
                missed += 1
            by_type_result[alg_type] = {
                "ground_truth": {
                    "node_type": gt["node_type"],
                    "node_name": gt_name,
                    "is_invalid_node": False,
                },
                "recommended": {
                    "node_id": rec.get("node_id", "") if rec else "",
                    "node_name": rec_name,
                    "vote_ratio": rec.get("vote_ratio", 0.0) if rec else 0.0,
                    "topk_candidates": candidates,
                } if rec else None,
                "match_status": status,
                "topk_relaxed_match": is_hit,
            }
        elif gt and not candidates:
            # GT category exists but is filtered out → ignored, not in denominator
            gt_only_count += 1
            by_type_result[alg_type] = {
                "ground_truth": {
                    "node_type": gt["node_type"],
                    "node_name": gt_name,
                    "is_invalid_node": False,
                },
                "recommended": None,
                "match_status": "gt_only_ignored",
                "topk_relaxed_match": None,
            }
        elif rec and not gt:
            # Recommended category exceeds GT → ignored, not in denominator
            rec_only_count += 1
            by_type_result[alg_type] = {
                "ground_truth": None,
                "recommended": {
                    "node_id": rec.get("node_id", "") if rec else "",
                    "node_name": rec_name,
                    "vote_ratio": rec.get("vote_ratio", 0.0) if rec else 0.0,
                    "topk_candidates": candidates,
                },
                "match_status": "rec_only_ignored",
                "topk_relaxed_match": None,
            }

    total_gt = len(gt_by_type)
    total_rec = len(rec_by_type)

    return {
        "type": "topk_relaxed",
        "topk": topk,
        "total_ground_truth": total_gt,
        "effective_intersection": effective_intersection,
        "invalid_ground_truth": invalid_gt_excluded,
        "total_recommended": total_rec,
        "topk_hit": matched,
        "missed": missed,
        "gt_only_ignored": gt_only_count,
        "rec_only_ignored": rec_only_count,
        "invalid_gt_ignored": invalid_gt_excluded,
        "match_rate": round(matched / max(effective_intersection, 1), 4),
        "by_type": by_type_result,
    }


def compute_consistency(
    N_recommend: dict,
    N_vote: dict,
    ground_truth_algorithms: list[dict],
    node_idx: dict[str, dict],
    topk: int = 3,
) -> dict:
    """Compute 4 types of consistency metrics, return summary dict."""
    strict = check_strict_consistency(
        N_recommend, N_vote, ground_truth_algorithms, node_idx, topk
    )
    topk_strict = check_topk_strict_consistency(
        N_recommend, N_vote, ground_truth_algorithms, node_idx, topk
    )
    relaxed = check_relaxed_consistency(
        N_recommend, N_vote, ground_truth_algorithms, node_idx, topk
    )
    topk_relaxed = check_topk_relaxed_consistency(
        N_recommend, N_vote, ground_truth_algorithms, node_idx, topk
    )
    return {
        "strict": strict,
        "topk_strict": topk_strict,
        "relaxed": relaxed,
        "topk_relaxed": topk_relaxed,
    }



# ============================================================
# MD report generation
# ============================================================

def _build_md_table_row(
    case_id: str,
    result: dict,
    node_idx: dict[str, dict],
    ground_truth_algorithms: list[dict],
    topk: int,
) -> list[str]:
    """Build row data for the recommendation result table.

    Each row: [case_id, node_type, standard_GT_node_id, standard_GT_node_name,
           recommended_Top1_node_id, recommended_Top1_node_name, ...TopK..., ...TopK_vote_ratios...]
    """
    gt_by_type = _compute_gt_by_type(ground_truth_algorithms)
    vote_topk = _get_topk_candidates_from_vote(
        result.get("state_N_vote", {}), node_idx, topk
    )

    all_types = sorted(set(list(gt_by_type.keys())))

    rows = []
    for i, alg_type in enumerate(all_types):
        gt = gt_by_type.get(alg_type)
        gt_name = gt["node_name"].strip() if gt and gt.get("node_name") else ""
        gt_node_id = gt.get("node_id", "")

        candidates = vote_topk.get(alg_type, [])
        rec_top1 = result.get("N_recommend", {}).get(alg_type, {})

        row = {
            "case_id": case_id,
            "node_type": alg_type,
            "gt_node_id": gt_node_id,
            "gt_node_name": gt_name,
            "rec_top1_node_id": rec_top1.get("node_id", ""),
            "rec_top1_node_name": rec_top1.get("node_name", ""),
            "rec_top1_vote_ratio": rec_top1.get("vote_ratio", 0.0),
        }
        # TopK candidates
        for k_idx in range(topk):
            if k_idx < len(candidates):
                c = candidates[k_idx]
                row[f"top{k_idx+1}_node_id"] = c.get("node_id", "")
                row[f"top{k_idx+1}_node_name"] = c.get("node_name", "")
                row[f"top{k_idx+1}_vote_ratio"] = c.get("vote_ratio", 0.0)
            else:
                row[f"top{k_idx+1}_node_id"] = ""
                row[f"top{k_idx+1}_node_name"] = ""
                row[f"top{k_idx+1}_vote_ratio"] = ""

        rows.append(row)

    return rows


def _build_epoch_table_rows(result: dict) -> list[dict]:
    """Build inference epoch key parameter table data."""
    epoch_logs = result.get("epoch_logs", {})
    rows = []
    for epoch_key in sorted(epoch_logs.keys(), key=lambda k: int(k.replace("Epoch", ""))):
        log = epoch_logs.get(epoch_key, {})
        pruning_info = log.get("pruning", {})

        row = {
            "epoch": epoch_key,
            "participating_node_count": log.get("participating_node_count", ""),
            "participating_node_type_count": log.get("participating_node_type_count", ""),
            "Thinking_belief": log.get("Thinking_belief", ""),
            "fact_sufficiency_A": pruning_info.get("fact_sufficiency_A", ""),
            "pruning_strategy": pruning_info.get("pruning_strategy", ""),
            "pruning_status": pruning_info.get("pruning_status", ""),
            "feedback_time": pruning_info.get("feedback_time", ""),
        }
        rows.append(row)
    return rows


def generate_md_report(
    all_results: list[dict],
    output_dir: str,
    run_params: dict,
    topk: int = 3,
    scenario_label: str = "placeholder scenario",
    epoch_max_values: list[int] | None = None,
) -> str:
    """Generate 00-Overall_Statistics.md.

    Report structure:
      1. Overview (summary grouped by Epoch_max)
      2. Details (sub-heading for each case_id + epoch_max)
    """
    os.makedirs(output_dir, exist_ok=True)

    case_ids = sorted(set(r["case_id"] for r in all_results))
    total_cases = len(case_ids)
    total_runs = len(all_results)
    epoch_max_values = epoch_max_values or []

    # Compute 4 types of consistency average (global)
    def avg_rate(results, key):
        rates = [r.get(key, 0.0) for r in results if r.get(key) is not None]
        return round(sum(rates) / len(rates), 4) if rates else 0.0

    strict_avg = avg_rate(all_results, "strict_match_rate")
    topk_strict_avg = avg_rate(all_results, "topk_strict_match_rate")
    relaxed_avg = avg_rate(all_results, "relaxed_match_rate")
    topk_relaxed_avg = avg_rate(all_results, "topk_relaxed_match_rate")

    lines: list[str] = []
    lines.append(f"# 00-Overall_Statistics\n")
    lines.append(f"> Scenario: {scenario_label} | Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    lines.append("")

    # ---- 1 Overview ----
    lines.append("## I. Overview\n")
    lines.append(f"| Item | Value |\n")
    lines.append(f"| --- | --- |\n")
    lines.append(f"| Current data scenario | {scenario_label} |\n")
    lines.append(f"| case_id total | {total_cases} |\n")
    lines.append(f"| Epoch_max iteration values | {epoch_max_values} |\n")
    lines.append(f"| Strict consistency average (global) | {strict_avg:.2%} |\n")
    lines.append(f"| TopK strict consistency average (global) | {topk_strict_avg:.2%} |\n")
    lines.append(f"| Relaxed consistency average (global) | {relaxed_avg:.2%} |\n")
    lines.append(f"| TopK relaxed consistency average (global) | {topk_relaxed_avg:.2%} |\n")
    lines.append("")

    # ---- Group by Epoch_max ----
    if epoch_max_values:
        lines.append("### Group Summary by Epoch_max\n")
        lines.append(
            f"| Epoch_max | case count | Strict consistency | TopK strict consistency | Relaxed consistency | TopK relaxed consistency |\n"
        )
        lines.append(
            f"| --- | --- | --- | --- | --- | --- |\n"
        )
        for em in epoch_max_values:
            epoch_results = [r for r in all_results if r.get("epoch_max") == em]
            if not epoch_results:
                continue
            s_avg = avg_rate(epoch_results, "strict_match_rate")
            tk_avg = avg_rate(epoch_results, "topk_strict_match_rate")
            r_avg = avg_rate(epoch_results, "relaxed_match_rate")
            tk_r_avg = avg_rate(epoch_results, "topk_relaxed_match_rate")
            lines.append(
                f"| {em} | {len(epoch_results)} | {s_avg:.2%} | {tk_avg:.2%} | {r_avg:.2%} | {tk_r_avg:.2%} |\n"
            )
        lines.append("")

    # ---- 2 Graph reasoning configuration ----
    lines.append("### Graph Reasoning Configuration\n")
    lines.append(f"| Parameter | Value |\n")
    lines.append(f"| --- | --- |\n")
    lines.append(f"| Epoch_max iteration values | {epoch_max_values} |\n")
    for param_key in ["Thinking_belief_threshold",
                      "pruning_dynamic_width_gamma", "pruning_dynamic_width_hard_cap",
                      "pruning_entropy_disable_threshold",
                      "N_non_alg_type_count_max"]:
        val = run_params.get(param_key, "")
        lines.append(f"| {param_key} | {val} |\n")
    lines.append("")

    # ---- 3 Details ----
    lines.append("## II. Details\n")

    for case_id in case_ids:
        case_results = [r for r in all_results if r["case_id"] == case_id]
        if not case_results:
            continue

        # Each case may have multiple entries (different epoch_max), output separately
        for result in case_results:
            em = result.get("epoch_max", "?")
            lines.append(f"### Case {case_id} (Epoch_max={em})\n")

            # Region 1: 4 types of consistency + termination reason
            lines.append("#### Region 1: Consistency Metrics\n")
            lines.append(f"| Consistency type | match_rate |\n")
            lines.append(f"| --- | --- |\n")
            lines.append(f"| Strict consistency | {result.get('strict_match_rate', 0.0):.2%} |\n")
            lines.append(f"| TopK strict consistency | {result.get('topk_strict_match_rate', 0.0):.2%} |\n")
            lines.append(f"| Relaxed consistency | {result.get('relaxed_match_rate', 0.0):.2%} |\n")
            lines.append(f"| TopK relaxed consistency | {result.get('topk_relaxed_match_rate', 0.0):.2%} |\n")
            lines.append("")

            term_reason = result.get("termination_reason", "N/A")
            lines.append(f"**Graph reasoning termination reason**: {term_reason}\n")
            lines.append("")

            # Region 2: Recommendation result table
            node_idx = result.get("node_idx", {})
            ground_truth = result.get("ground_truth_algorithms", [])
            N_recommend = result.get("N_recommend", {})
            state_N_vote = result.get("state_N_vote", {})
            vote_topk = _get_topk_candidates_from_vote(state_N_vote, node_idx, topk)
            gt_by_type = _compute_gt_by_type(ground_truth)

            lines.append("#### Region 2: Recommendation Result Table\n")

            header_cols = [
                "node_type",
                "standard_GT_node_id",
                "standard_GT_node_name",
                "recommended_Top1_node_id",
                "recommended_Top1_node_name",
                "recommended_Top1_vote_ratio",
            ]
            for k in range(topk):
                header_cols.append(f"recommended_Top{k+1}_node_id")
                header_cols.append(f"recommended_Top{k+1}_node_name")
                header_cols.append(f"recommended_Top{k+1}_vote_ratio")

            lines.append("| " + " | ".join(header_cols) + " |\n")
            lines.append("| " + " | ".join(["---"] * len(header_cols)) + " |\n")

            for alg_type in sorted(gt_by_type.keys()):
                gt = gt_by_type[alg_type]
                gt_node_id = gt.get("node_id", "")
                gt_node_name = (gt["node_name"] or "").strip()

                rec_top1 = N_recommend.get(alg_type, {})
                rec_top1_id = rec_top1.get("node_id", "")
                rec_top1_name = (rec_top1.get("node_name") or "").strip()
                rec_top1_vote = rec_top1.get("vote_ratio", "")

                row_cells = [
                    alg_type,
                    gt_node_id,
                    gt_node_name,
                    rec_top1_id,
                    rec_top1_name,
                    f"{rec_top1_vote:.4f}" if rec_top1_vote != "" else "",
                ]

                candidates = vote_topk.get(alg_type, [])
                for k_idx in range(topk):
                    if k_idx < len(candidates):
                        c = candidates[k_idx]
                        row_cells.extend([
                            c.get("node_id", ""),
                            (c.get("node_name") or "").strip(),
                            f"{c.get('vote_ratio', 0.0):.4f}",
                        ])
                    else:
                        row_cells.extend(["", "", ""])

                lines.append("| " + " | ".join(str(c) for c in row_cells) + " |\n")

            lines.append("")

            # Region 3: Inference epoch key parameters
            lines.append("#### Region 3: Inference Epoch Key Parameters\n")
            lines.append(
                f"| Epoch round | Participating node count | Participating node_type deduplicated count | "
                f"Overall recommendation belief thinking_belief | Fact sufficiency A | "
                f"Pruning strategy | Status | Backtracking times |\n"
            )
            lines.append(
                f"| --- | --- | --- | --- | --- | --- | --- | --- |\n"
            )

            epoch_logs = result.get("epoch_logs", {})
            for epoch_key in sorted(epoch_logs.keys(), key=lambda k: int(k.replace("Epoch", ""))):
                log = epoch_logs.get(epoch_key, {})
                pruning = log.get("pruning", {})

                lines.append(
                    f"| {epoch_key} | "
                    f"{log.get('participating_node_count', '')} | "
                    f"{log.get('participating_node_type_count', '')} | "
                    f"{log.get('Thinking_belief', '')} | "
                    f"{pruning.get('fact_sufficiency_A', '')} | "
                    f"{pruning.get('pruning_strategy', '')} | "
                    f"{pruning.get('pruning_status', '')} | "
                    f"{pruning.get('feedback_time', '')} |\n"
                )

            lines.append("")
            lines.append("---\n\n")

    out_path = os.path.join(output_dir, "00-Overall_Statistics.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("".join(lines))

    return out_path


# ============================================================
# Hyperparameter subfolder naming utility
# ============================================================

def _format_hyperparam_value(value: Any) -> str:
    """Format a single hyperparameter value: int stays int; float keeps 2 decimals; others convert to string."""
    if isinstance(value, bool):
        return str(value)
    if isinstance(value, int):
        return str(value)
    if isinstance(value, float):
        return f"{value:.2f}"
    return str(value)


def build_hyperparam_subfolder_name(run_params: dict) -> str:
    """Build subfolder name from hyperparameter dict.

    Naming rule (fixed order):
      Epoch_max=<...> + Belief_thred=<...> + TopK=<...> +
      pruning_gamma=<...> + pruning_hardcap=<...> + pruning_thred=<...>

    Values come dynamically from run_params dict.
    """
    parts = [
        f"Epoch_max={_format_hyperparam_value(run_params.get('Epoch_max', ''))}",
        f"Belief_thred={_format_hyperparam_value(run_params.get('Thinking_belief_threshold', ''))}",
        f"TopK={_format_hyperparam_value(run_params.get('Top_K', ''))}",
        f"pruning_gamma={_format_hyperparam_value(run_params.get('pruning_dynamic_width_gamma', ''))}",
        f"pruning_hardcap={_format_hyperparam_value(run_params.get('pruning_dynamic_width_hard_cap', ''))}",
        f"pruning_thred={_format_hyperparam_value(run_params.get('pruning_entropy_disable_threshold', ''))}",
    ]
    return "_".join(parts)
def generate_hyperparam_md_report(
    all_results: list[dict],
    output_dir: str,
    run_params: dict,
    topk: int = 3,
    scenario_label: str = "placeholder scenario",
    epoch_max_values: list[int] | None = None,
) -> str:
    """Generate 00-Overall_Statistics.md for a single hyperparameter subfolder (same format as generate_md_report).

    Difference from generate_md_report: only generates report for the passed all_results,
    used for saving independent statistics files in each Epoch_max hyperparameter subfolder.
    """
    os.makedirs(output_dir, exist_ok=True)

    case_ids = sorted(set(r["case_id"] for r in all_results))
    total_cases = len(case_ids)
    total_runs = len(all_results)
    epoch_max_values = epoch_max_values or []

    def avg_rate(results, key):
        rates = [r.get(key, 0.0) for r in results if r.get(key) is not None]
        return round(sum(rates) / len(rates), 4) if rates else 0.0

    strict_avg = avg_rate(all_results, "strict_match_rate")
    topk_strict_avg = avg_rate(all_results, "topk_strict_match_rate")
    relaxed_avg = avg_rate(all_results, "relaxed_match_rate")
    topk_relaxed_avg = avg_rate(all_results, "topk_relaxed_match_rate")

    lines: list[str] = []
    lines.append(f"# 00-Overall_Statistics\n")
    lines.append(f"> Scenario: {scenario_label} | Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    lines.append("")

    # ---- 1 Overview ----
    lines.append("## I. Overview\n")
    lines.append(f"| Item | Value |\n")
    lines.append(f"| --- | --- |\n")
    lines.append(f"| Current data scenario | {scenario_label} |\n")
    lines.append(f"| case_id total | {total_cases} |\n")
    lines.append(f"| Epoch_max iteration values | {epoch_max_values} |\n")
    lines.append(f"| Strict consistency average (global) | {strict_avg:.2%} |\n")
    lines.append(f"| TopK strict consistency average (global) | {topk_strict_avg:.2%} |\n")
    lines.append(f"| Relaxed consistency average (global) | {relaxed_avg:.2%} |\n")
    lines.append(f"| TopK relaxed consistency average (global) | {topk_relaxed_avg:.2%} |\n")
    lines.append("")

    # ---- 2 Graph reasoning configuration ----
    lines.append("### Graph Reasoning Configuration\n")
    lines.append(f"| Parameter | Value |\n")
    lines.append(f"| --- | --- |\n")
    for param_key in ["Thinking_belief_threshold",
                      "pruning_dynamic_width_gamma", "pruning_dynamic_width_hard_cap",
                      "pruning_entropy_disable_threshold",
                      "N_non_alg_type_count_max"]:
        val = run_params.get(param_key, "")
        lines.append(f"| {param_key} | {val} |\n")
    lines.append("")

    # ---- 3 Details ----
    lines.append("## II. Details\n")

    for case_id in case_ids:
        case_results = [r for r in all_results if r["case_id"] == case_id]
        if not case_results:
            continue

        for result in case_results:
            em = result.get("epoch_max", "?")
            lines.append(f"### Case {case_id} (Epoch_max={em})\n")

            lines.append("#### Region 1: Consistency Metrics\n")
            lines.append(f"| Consistency type | match_rate |\n")
            lines.append(f"| --- | --- |\n")
            lines.append(f"| Strict consistency | {result.get('strict_match_rate', 0.0):.2%} |\n")
            lines.append(f"| TopK strict consistency | {result.get('topk_strict_match_rate', 0.0):.2%} |\n")
            lines.append(f"| Relaxed consistency | {result.get('relaxed_match_rate', 0.0):.2%} |\n")
            lines.append(f"| TopK relaxed consistency | {result.get('topk_relaxed_match_rate', 0.0):.2%} |\n")
            lines.append("")

            term_reason = result.get("termination_reason", "N/A")
            lines.append(f"**Graph reasoning termination reason**: {term_reason}\n")
            lines.append("")

            # Region 2: Recommendation result table
            node_idx = result.get("node_idx", {})
            ground_truth = result.get("ground_truth_algorithms", [])
            N_recommend = result.get("N_recommend", {})
            state_N_vote = result.get("state_N_vote", {})
            vote_topk = _get_topk_candidates_from_vote(state_N_vote, node_idx, topk)
            gt_by_type = _compute_gt_by_type(ground_truth)

            lines.append("#### Region 2: Recommendation Result Table\n")

            header_cols = [
                "node_type",
                "standard_GT_node_id",
                "standard_GT_node_name",
                "recommended_Top1_node_id",
                "recommended_Top1_node_name",
                "recommended_Top1_vote_ratio",
            ]
            for k in range(topk):
                header_cols.append(f"recommended_Top{k+1}_node_id")
                header_cols.append(f"recommended_Top{k+1}_node_name")
                header_cols.append(f"recommended_Top{k+1}_vote_ratio")

            lines.append("| " + " | ".join(header_cols) + " |\n")
            lines.append("| " + " | ".join(["---"] * len(header_cols)) + " |\n")

            for alg_type in sorted(gt_by_type.keys()):
                gt = gt_by_type[alg_type]
                gt_node_id = gt.get("node_id", "")
                gt_node_name = (gt["node_name"] or "").strip()

                rec_top1 = N_recommend.get(alg_type, {})
                rec_top1_id = rec_top1.get("node_id", "")
                rec_top1_name = (rec_top1.get("node_name") or "").strip()
                rec_top1_vote = rec_top1.get("vote_ratio", "")

                row_cells = [
                    alg_type,
                    gt_node_id,
                    gt_node_name,
                    rec_top1_id,
                    rec_top1_name,
                    f"{rec_top1_vote:.4f}" if rec_top1_vote != "" else "",
                ]

                candidates = vote_topk.get(alg_type, [])
                for k_idx in range(topk):
                    if k_idx < len(candidates):
                        c = candidates[k_idx]
                        row_cells.extend([
                            c.get("node_id", ""),
                            (c.get("node_name") or "").strip(),
                            f"{c.get('vote_ratio', 0.0):.4f}",
                        ])
                    else:
                        row_cells.extend(["", "", ""])

                lines.append("| " + " | ".join(str(c) for c in row_cells) + " |\n")

            lines.append("")

            # Region 3: Inference epoch key parameters
            lines.append("#### Region 3: Inference Epoch Key Parameters\n")
            lines.append(
                f"| Epoch round | Participating node count | Participating node_type deduplicated count | "
                f"Overall recommendation belief thinking_belief | Fact sufficiency A | "
                f"Pruning strategy | Status | Backtracking times |\n"
            )
            lines.append(
                f"| --- | --- | --- | --- | --- | --- | --- | --- |\n"
            )

            epoch_logs = result.get("epoch_logs", {})
            for epoch_key in sorted(epoch_logs.keys(), key=lambda k: int(k.replace("Epoch", ""))):
                log = epoch_logs.get(epoch_key, {})
                pruning = log.get("pruning", {})

                lines.append(
                    f"| {epoch_key} | "
                    f"{log.get('participating_node_count', '')} | "
                    f"{log.get('participating_node_type_count', '')} | "
                    f"{log.get('Thinking_belief', '')} | "
                    f"{pruning.get('fact_sufficiency_A', '')} | "
                    f"{pruning.get('pruning_strategy', '')} | "
                    f"{pruning.get('pruning_status', '')} | "
                    f"{pruning.get('feedback_time', '')} |\n"
                )

            lines.append("")
            lines.append("---\n\n")

    out_path = os.path.join(output_dir, "00-Overall_Statistics.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("".join(lines))

    return out_path


def generate_scenario_summary_md(
    all_results: list[dict],
    output_dir: str,
    run_params: dict,
    scenario_label: str = "placeholder scenario",
    epoch_max_values: list[int] | None = None,
) -> str:
    """Generate summary report in scenario-level folder (containing scenario info and averages per Epoch_max).

    Output file format matches terminal output, convenient for archiving comparison.
    """
    os.makedirs(output_dir, exist_ok=True)

    epoch_max_values = epoch_max_values or []

    def avg_rate(results, key):
        rates = [r.get(key, 0.0) for r in results if r.get(key) is not None]
        return round(sum(rates) / len(rates), 4) if rates else 0.0

    lines: list[str] = []
    lines.append(f"# {scenario_label} Test Summary Report\n")
    lines.append(f"> Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    lines.append("")

    # ---- Basic information ----
    case_ids = sorted(set(r["case_id"] for r in all_results))
    lines.append("## I. Basic Information\n")
    lines.append(f"| Item | Value |\n")
    lines.append(f"| --- | --- |\n")
    lines.append(f"| Current data scenario | {scenario_label} |\n")
    lines.append(f"| Test set case_id total | {len(case_ids)} |\n")
    lines.append(f"| Epoch_max iteration values | {epoch_max_values} |\n")
    lines.append("")

    # ---- Per Epoch_max averages ----
    lines.append("## II. Consistency Averages Grouped by Epoch_max\n")
    lines.append(
        f"| Epoch_max | case count | Strict consistency | TopK strict consistency | Relaxed consistency | TopK relaxed consistency |\n"
    )
    lines.append(
        f"| --- | --- | --- | --- | --- | --- |\n"
    )
    for em in epoch_max_values:
        epoch_results = [r for r in all_results if r.get("epoch_max") == em]
        if not epoch_results:
            continue
        s_avg = avg_rate(epoch_results, "strict_match_rate")
        tk_avg = avg_rate(epoch_results, "topk_strict_match_rate")
        r_avg = avg_rate(epoch_results, "relaxed_match_rate")
        tk_r_avg = avg_rate(epoch_results, "topk_relaxed_match_rate")
        lines.append(
            f"| {em} | {len(epoch_results)} | {s_avg:.2%} | {tk_avg:.2%} | {r_avg:.2%} | {tk_r_avg:.2%} |\n"
        )
    lines.append("")

    # ---- Graph reasoning configuration ----
    lines.append("## III. Graph Reasoning Hyperparameter Configuration\n")
    lines.append(f"| Parameter | Value |\n")
    lines.append(f"| --- | --- |\n")
    for param_key in ["Thinking_belief_threshold",
                      "pruning_dynamic_width_gamma", "pruning_dynamic_width_hard_cap",
                      "pruning_entropy_disable_threshold",
                      "N_non_alg_type_count_max"]:
        val = run_params.get(param_key, "")
        lines.append(f"| {param_key} | {val} |\n")
    lines.append("")

    out_path = os.path.join(output_dir, f"{scenario_label}_consistency_summary.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("".join(lines))

    return out_path
