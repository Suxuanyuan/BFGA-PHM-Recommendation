# -*- coding: utf-8 -*-
r"""
v7_modules/08_prune.py
=======================
Pruning module (v7 fully rewritten, v8.1 newly added strategy_3).

Core changes:
  1. Fact sufficiency changed to 19-point system (each node_type counts 1 point, max 19 points)
  2. Decide pruning strategy based on fact sufficiency normalization coefficient and node_type coverage status:
     - A < 1 AND 1-14 non-algorithm nodes not fully covered → strategy_1: prioritize completing missing 1-14 node_types
     - A < 1 AND 1-14 fully covered BUT 15-19-Induction not fully covered → strategy_3:
       prioritize completing missing 15-19-Induction node_types based on 01-default-edge + target=induction algorithm node
     - A >= 1 (fact constraints saturated: 1-14 fully covered AND 15-19-Induction fully covered)
       → strategy_2: supplement more potential facts
  3. Pruning-exploration-aggregation concurrent loop:
     - Pick TopW nodes from Top10 candidates
     - Generate W-sum group combinations (combinations without replacement)
     - Concurrently explore each W-sum group's temporary candidate edges/nodes
     - Concurrently aggregate to get each group's recommended algorithm vote ratios
     - Concurrently feedback: compare Epoch(i-1) with each W-sum group's vote ratio improvements
     - Select optimal group with n(i)[w] >= 3, or backtrack and retry
  4. Strategy_1 and strategy_3 share the "each pruning round prioritizes querying different node_types" diversity TopW selection logic

N_pruning output structure:
  N_pruning = [  # list, no longer dict
      {
          "Epoch": "Epoch1",
          "current_node_ids": [...],
          "current_recommend_vote_list": {...},
          "fact_sufficiency_A": 0.xxx,
          "pruning_strategy": "strategy_1" | "strategy_2" | "strategy_3",
          "pruning_time": f_last,
          "pruning_status": "success" | "failure",
          "best_pruning_node_ids": [...] | None,
          "best_pruning_recommend_vote_list": {...},
          "next_node_ids": [...],
          "coverage_status": {                    # v8.1 newly added: basis for strategy selection
              "non_alg_full": bool,
              "induction_full": bool,
              "missing_non_alg_codes": [...],
              "missing_induction_codes": [...],
              "covered_non_alg_count": int,
              "covered_induction_count": int,
          },
          "feedback_details": [
              {
                  "feedback_time": 1,
                  "W_dynamic_n": 2,
                  "Wsum_pruning_node_ids": {"id_1": [...], ...},
                  "Wsum_num_increasing_max_vote": {"id_1": 3, ...},
              },
              ...
          ],
      },
      ...
  ]

Key functions:
  collect_non_algorithm_candidates(...) -> dict    # Collect candidate edges and candidate nodes
  filter_valid_candidates(...) -> dict             # Filter by edge_group 02/03 (strategy_1/2)
  filter_valid_induction_candidates(...) -> dict   # Filter by edge_group 01-default-edge + target=Induction (strategy_3)
  filter_2nd_candidates(...) -> list               # Filter valid 2nd candidate nodes
  compute_type_coverage_status(...) -> dict        # v8.1 newly added: evaluate node_type coverage status
  compute_dynamic_width(...) -> int                # Dynamic pruning width (reuse v6 logic)
  generate_wsum_groups(...) -> list                # Generate W-sum groups
  concurrent_explore_wsum_groups(...) -> list      # Concurrent exploration
  concurrent_vote_wsum_groups(...) -> list         # Concurrent aggregation
  compute_feedback(...) -> dict                    # Concurrent feedback
  prune_for_next_epoch(...) -> dict                # Main entry
"""

import math
import itertools
from typing import Any

from . import m00_config as cfg
from . import m06_explore as explore_mod
from . import m07_aggregate as aggregate_mod


# ============================================================
# Candidate collection and filtering
# ============================================================

# Target induction algorithm node types corresponding to 01-default-edges (v8.1 newly added strategy_3 only)
INDUCTION_TARGET_NODE_TYPES = {
    "15-DataPreprocessingAlgorithmClass-Induction",
    "16-FeatureExtractionAlgorithmClass-Induction",
    "17-CoreDiscriminatorAlgorithmClass-Induction",
    "18-DataGenerationAlgorithmClass-Induction",
    "19-TrainingOptimizationAlgorithmClass-Induction",
}

DEFAULT_EDGE_GROUP = "01-DefaultEdge"


def collect_non_algorithm_candidates(
    state: Any,
    epoch_key: str,
    graph: dict,
    edge_idx: dict[str, dict],
    node_idx: dict[str, dict],
    Non_alg_group: list[str] | None = None,
) -> dict[str, list[dict]]:
    """Collect candidate next-hop non-algorithm nodes (valid candidate edges, valid 1st candidate nodes) for the current Epoch nodes.

    Returns:
        {
            "current_node_id": [
                {
                    "edge_id": str,
                    "next_node_id": str,
                    "direction": str,
                    "edge_weight": float,
                    "edge_group": str,
                    "graph_source_node_id": str,
                    "graph_target_node_id": str,
                },
                ...
            ]
        }
    """
    Non_alg_next_by_node: dict[str, list[dict]] = {}
    existing_set: set[str] = set(Non_alg_group) if Non_alg_group else set()

    if epoch_key not in state.N_Explore:
        return Non_alg_next_by_node

    for current_node_id, node_info in state.N_Explore[epoch_key].items():
        candidate_edge_ids = node_info.get("candidate_edge_ids", [])
        if not candidate_edge_ids:
            Non_alg_next_by_node[current_node_id] = []
            continue

        next_candidates = []
        for eid in candidate_edge_ids:
            edge = edge_idx.get(eid)
            if edge is None:
                continue
            src = edge.get("source_node_id", "")
            tgt = edge.get("target_node_id", "")

            if src == current_node_id:
                direction = "out"
                next_node_id = tgt
            elif tgt == current_node_id:
                direction = "in"
                next_node_id = src
            else:
                continue

            next_node = node_idx.get(next_node_id)
            if next_node is None:
                continue
            if not cfg.is_non_algorithm_node(next_node.get("node_type", "")):
                continue
            if next_node_id in existing_set:
                continue

            ew = edge.get("edge_weight", {})
            if isinstance(ew, dict):
                edge_weight = ew.get("edge_weight", 0.0)
            elif isinstance(ew, (int, float)):
                edge_weight = float(ew)
            else:
                edge_weight = 0.0

            next_candidates.append({
                "edge_id": eid,
                "next_node_id": next_node_id,
                "direction": direction,
                "edge_weight": edge_weight,
                "edge_group": edge.get("edge_group", ""),
                "graph_source_node_id": src,
                "graph_target_node_id": tgt,
            })

        Non_alg_next_by_node[current_node_id] = next_candidates

    return Non_alg_next_by_node


def filter_valid_candidates(
    Non_alg_next_by_node: dict[str, list[dict]],
) -> tuple[list[dict], list[str]]:
    """Filter by edge_group 02-CausalEdge / 03-EvidenceEdge, retain valid candidate edges and valid 1st candidate nodes.

    Corresponds to md 4-3-1-2/4-3-1-3 "screen out valid candidate edges and valid 1st candidate nodes".

    Returns:
        (valid_edges, valid_1st_node_ids)
    """
    valid_edge_groups = {"02-CausalEdge", "03-EvidenceEdge"}

    valid_edges = []
    valid_1st_node_ids = []
    seen_edges = set()
    seen_nodes = set()

    for current_node_id, candidates in Non_alg_next_by_node.items():
        for cand in candidates:
            edge_group = cand.get("edge_group", "")
            if edge_group not in valid_edge_groups:
                continue
            edge_id = cand["edge_id"]
            next_id = cand["next_node_id"]

            if edge_id not in seen_edges:
                valid_edges.append(cand)
                seen_edges.add(edge_id)
            if next_id not in seen_nodes:
                valid_1st_node_ids.append(next_id)
                seen_nodes.add(next_id)

    return valid_edges, valid_1st_node_ids


def filter_2nd_candidates(
    valid_1st_node_ids: list[str],
    Non_alg_group: list[str],
    node_idx: dict[str, dict],
    strategy: str,
    coverage_status: dict | None = None,
    excluded_node_types: set[str] | None = None,
) -> list[dict]:
    """Filter valid 2nd candidate nodes.

    Strategy_1 (A < 1 AND 1-14 not fully covered, fact constraints not saturated - complete 1-14):
      Strictly retain only valid 1st candidate nodes corresponding to "missing node_types":
        1. node's node_type code ∈ coverage_status["missing_non_alg_codes"]
        2. AND not in excluded_node_types (node_types selected in previous epochs of this case)
      → If filtered result is empty, return empty list (upper layer decides whether to terminate strategy_1)
    Strategy_3 (A < 1 AND 1-14 complete BUT 15-19-Induction not complete, fact constraints not saturated - complete induction):
      Also only retain valid 1st candidate nodes corresponding to "missing Induction node_types":
        1. node's node_type code ∈ coverage_status["missing_induction_codes"]
        2. AND not in excluded_node_types
    Strategy_2 (A = 1, fact constraints saturated):
      Retain all valid 1st nodes (maintain original behavior)

    Returns:
        list[dict]: each element contains node_id, node_name, node_type, vote_ratio, node_weight
                   If strategy_1/3 and no missing-type candidates, return empty list
    """
    non_alg_set = set(Non_alg_group)

    # Collect node_type distribution of existing non-algorithm nodes
    existing_types: set[str] = set()
    for nid in Non_alg_group:
        node = node_idx.get(nid)
        if node:
            existing_types.add(node.get("node_type", ""))

    # === Strategy_1 / Strategy_3: Strictly filter by "missing node_type" (modification 4+2 merged implementation) ===
    if strategy in ("strategy_1", "strategy_3"):
        # Get missing type code set
        if strategy == "strategy_1":
            allowed_codes = set((coverage_status or {}).get("missing_non_alg_codes", set()) or set())
        else:  # strategy_3
            allowed_codes = set((coverage_status or {}).get("missing_induction_codes", set()) or set())

        excluded = excluded_node_types or set()

        # Build complete name set of "missing node_types"
        allowed_type_names: set[str] = set()
        for code in allowed_codes:
            tn = cfg.NODE_TYPE_CODE_TO_NAME.get(code, "")
            if tn:
                allowed_type_names.add(tn)
        # Induction class node_types have special naming: with "-Induction" suffix
        if strategy == "strategy_3":
            allowed_type_names = {
                cfg.INDUCTION_TYPE_NAMES.get(str(code), "")
                for code in allowed_codes
            }
            allowed_type_names.discard("")

        filtered_ids: list[str] = []
        for nid in valid_1st_node_ids:
            node = node_idx.get(nid)
            if node is None:
                continue
            nt = node.get("node_type", "")
            if not nt:
                continue
            # Check whether node_type is in missing set
            if strategy == "strategy_3":
                # Induction nodes matched by name directly
                if nt not in allowed_type_names:
                    continue
            else:
                # 1-14 nodes matched by code
                code = cfg.get_type_code(nt)
                if code not in allowed_codes:
                    continue
            # Exclude already-selected node_types (prevent subsequent epochs from re-completing)
            if nt in excluded:
                continue
            # Exclude nodes already in Non_alg_group (fallback)
            if nid in non_alg_set:
                continue
            filtered_ids.append(nid)

        # Strict mode: return empty list when missing-type candidates are empty, no fallback to existing types
        if not filtered_ids:
            return []
        ordered_ids = filtered_ids
    else:
        # Strategy_2: all valid 1st nodes allowed
        ordered_ids = valid_1st_node_ids

    # Build node detail list
    node_candidates = []
    for nid in ordered_ids:
        node = node_idx.get(nid)
        if node is None:
            continue
        node_candidates.append({
            "node_id": nid,
            "node_name": node.get("node_name", ""),
            "node_type": node.get("node_type", ""),
            "vote_ratio": 0.0,  # Will be updated during sorting
            "node_weight": _get_node_weight(node),
        })

    # Deduplicate (preserve first-occurrence order)
    seen = set()
    unique_candidates = []
    for c in node_candidates:
        if c["node_id"] not in seen:
            unique_candidates.append(c)
            seen.add(c["node_id"])

    return unique_candidates


def _get_node_weight(node: dict) -> float:
    """Extract node_weight from node object (range 0-1)."""
    nw = node.get("node_weight", {})
    if isinstance(nw, dict):
        return nw.get("node_weight", 0.0)
    if isinstance(nw, (int, float)):
        return float(nw)
    return 0.0


def compute_type_coverage_status(
    Non_alg_group: list[str],
    node_idx: dict[str, dict],
) -> dict:
    """Evaluate node_type coverage status of existing non-algorithm nodes.

    Returns:
        {
            "covered_non_alg_types": set[str],      # node_type set with 1-14 codes
            "covered_induction_types": set[str],    # node_type set with 15-19 and -Induction suffix
            "non_alg_full": bool,                   # whether 1-14 is fully covered
            "induction_full": bool,                 # whether 15-19-Induction is fully covered
            "missing_non_alg_codes": set[int],      # missing codes in 1-14
            "missing_induction_codes": set[int],    # missing codes in 15-19-Induction
        }
    """
    covered_non_alg_types: set[str] = set()
    covered_induction_types: set[str] = set()
    covered_non_alg_codes: set[int] = set()
    covered_induction_codes: set[int] = set()

    # Optimization: single-pass traversal to compute both type set and code set simultaneously
    # Avoid second loop calling get_type_code (_cfg.get_type_code has regex matching internally)
    for nid in Non_alg_group:
        node = node_idx.get(nid)
        if node is None:
            continue
        nt = node.get("node_type", "")
        if not nt:
            continue
        # Determine via m00_config
        from . import m00_config as _cfg
        if _cfg.is_non_algorithm_node(nt):
            # Further subdivide: 1-14 vs 15-19-Induction
            if _cfg.is_induction_node(nt):
                covered_induction_types.add(nt)
            else:
                covered_non_alg_types.add(nt)

    # 1-14 completeness determination: directly through type_code numeric value
    for nt in covered_non_alg_types:
        code = cfg.get_type_code(nt)
        if 1 <= code <= 14:
            covered_non_alg_codes.add(code)

    for nt in covered_induction_types:
        code = cfg.get_type_code(nt)
        if 15 <= code <= 19:
            covered_induction_codes.add(code)

    missing_non_alg_codes = set(range(1, 15)) - covered_non_alg_codes
    missing_induction_codes = set(range(15, 20)) - covered_induction_codes

    return {
        "covered_non_alg_types": covered_non_alg_types,
        "covered_induction_types": covered_induction_types,
        "non_alg_full": len(missing_non_alg_codes) == 0,
        "induction_full": len(missing_induction_codes) == 0,
        "missing_non_alg_codes": missing_non_alg_codes,
        "missing_induction_codes": missing_induction_codes,
        "covered_non_alg_codes": covered_non_alg_codes,
        "covered_induction_codes": covered_induction_codes,
    }


def filter_valid_induction_candidates(
    Non_alg_next_by_node: dict[str, list[dict]],
    Non_alg_group: list[str],
    node_idx: dict[str, dict],
) -> tuple[list[dict], list[str]]:
    """Strategy_3 specific: Filter valid candidate edges and valid 1st candidate nodes by 01-default-edge + target=induction algorithm node.

    Determination conditions:
      - edge must be edge_group == "01-DefaultEdge"
      - target_node_type ∈ {15-Induction~19-Induction}
      - target_node_id not in Non_alg_group (i.e., exclude existing 1-14 nodes + existing Induction nodes)

    Returns:
        (valid_edges, valid_1st_node_ids)
    """
    valid_edges: list[dict] = []
    valid_1st_node_ids: list[str] = []
    seen_edges: set[str] = set()
    seen_nodes: set[str] = set()
    existing_set = set(Non_alg_group)

    for current_node_id, candidates in Non_alg_next_by_node.items():
        for cand in candidates:
            edge_group = cand.get("edge_group", "")
            if edge_group != DEFAULT_EDGE_GROUP:
                continue

            next_id = cand.get("next_node_id", "")
            next_node = node_idx.get(next_id)
            if next_node is None:
                continue

            # Verify target is an Induction node
            if not cfg.is_induction_node(next_node.get("node_type", "")):
                continue

            # target_node_id must not be in Non_alg_group
            if next_id in existing_set:
                continue

            edge_id = cand.get("edge_id", "")
            if edge_id not in seen_edges:
                valid_edges.append(cand)
                seen_edges.add(edge_id)
            if next_id not in seen_nodes:
                valid_1st_node_ids.append(next_id)
                seen_nodes.add(next_id)

    return valid_edges, valid_1st_node_ids


def compute_vote_ratios_for_2nd_candidates(
    candidates: list[dict],
    Non_alg_next_by_node: dict[str, list[dict]],
    Non_alg_group: list[str],
    strategy: str | None = None,
    node_idx: dict[str, dict] | None = None,
) -> dict[str, float]:
    """Compute population vote ratio for valid 2nd candidate nodes.

    Vote ratio = number of times pointed to / Num_node_alg
    where Num_node_alg is computed differentiated by candidate node's node_type (v8.x modification 4):
      Num_node_alg = (1-14 node count) + (-Induction node count with same code as candidate)
    Only count edges of the corresponding strategy:
      - strategy == "strategy_3"  → only count edge_group = "01-DefaultEdge"
      - others (strategy_1 / strategy_2 / None) → only count edges with edge_group 02/03
    """
    vote_ratios: dict[str, float] = {}
    if not Non_alg_group:
        return vote_ratios

    if strategy == "strategy_3":
        valid_edge_groups = {DEFAULT_EDGE_GROUP}
    else:
        valid_edge_groups = {"02-CausalEdge", "03-EvidenceEdge"}

    candidate_ids = {c["node_id"] for c in candidates}

    # Count how many current non-algorithm nodes point to each candidate node
    counts: dict[str, int] = {}
    for current_node_id, next_list in Non_alg_next_by_node.items():
        seen = set()
        for item in next_list:
            nid = item["next_node_id"]
            if nid not in candidate_ids:
                continue
            edge_group = item.get("edge_group", "")
            if edge_group not in valid_edge_groups:
                continue
            if nid not in seen:
                counts[nid] = counts.get(nid, 0) + 1
                seen.add(nid)

    # v8.x modification 4: compute denominator separately by candidate node's node_type
    if node_idx is not None:
        # Optimization: group by candidate node_type to share denominator, avoid each candidate repeatedly traversing Non_alg_group
        denom_cache: dict[str, int] = {}
        for nid, count in counts.items():
            cand_node = node_idx.get(nid, {})
            cand_node_type = cand_node.get("node_type", "")
            if cand_node_type not in denom_cache:
                denom_cache[cand_node_type] = cfg.compute_vote_ratio_denominator(
                    cand_node_type, Non_alg_group, node_idx
                )
            vote_ratios[nid] = count / denom_cache[cand_node_type]
    else:
        # Backward-compatible call: all candidates share same denominator
        num_node = max(1, len(Non_alg_group))
        for nid, count in counts.items():
            vote_ratios[nid] = count / num_node

    return vote_ratios


def sort_2nd_candidates(
    candidates: list[dict],
    vote_ratios: dict[str, float],
) -> list[dict]:
    """Sort valid 2nd candidate nodes by vote ratio descending.

    Sort rules: vote_ratio desc → node_weight desc → node_id stable sort.
    """
    sorted_candidates = sorted(
        candidates,
        key=lambda x: (
            -vote_ratios.get(x["node_id"], 0.0),
            -x["node_weight"],
            x["node_id"],
        )
    )
    # Update vote_ratio field
    for c in sorted_candidates:
        c["vote_ratio"] = vote_ratios.get(c["node_id"], 0.0)
    return sorted_candidates


# ============================================================
# strategy_1 / strategy_3 candidate filtering: retain only missing-type candidates
# (v8.x modification: per user design intent, restrict strategy_1/3 to only complete missing node_types)
# ============================================================

def _filter_candidates_by_missing_type(
    candidates: list[dict],
    coverage_status: dict,
    pruning_strategy: str,
    excluded_node_types: set[str] | None = None,
) -> list[dict]:
    """Filter strategy_1 / strategy_3 candidate nodes by "missing node_type".

    Rules:
      - strategy_1: retain candidates with node_type code ∈ coverage_status["missing_non_alg_codes"]
      - strategy_3: retain candidates with node_type code ∈ coverage_status["missing_induction_codes"]
      - Simultaneously exclude node_types already "selected in previous epochs of this case" in excluded_node_types
        (prevent subsequent epochs from re-completing already-completed node_types)

    Parameters:
        candidates: candidates to filter (already Top10 sorted list)
        coverage_status: compute_type_coverage_status return value
        pruning_strategy: "strategy_1" or "strategy_3"
        excluded_node_types: node_type set selected across epochs; no filtering when None

    Returns:
        Filtered candidate list (preserves original order)
    """
    if pruning_strategy not in ("strategy_1", "strategy_3"):
        return candidates

    if pruning_strategy == "strategy_1":
        allowed_codes = set(coverage_status.get("missing_non_alg_codes", set()) or set())
    else:
        allowed_codes = set(coverage_status.get("missing_induction_codes", set()) or set())

    if not allowed_codes:
        return []

    excluded = excluded_node_types or set()

    filtered: list[dict] = []
    for c in candidates:
        nt = c.get("node_type", "")
        if not nt:
            continue
        code = cfg.get_type_code(nt)
        if code not in allowed_codes:
            continue
        if nt in excluded:
            continue
        filtered.append(c)
    return filtered


def _record_epoch_selected_node_types(
    state: Any,
    best_pruning_node_ids: list[str] | None,
    node_idx: dict[str, dict],
    pruning_strategy: str,
) -> None:
    """Record node_types corresponding to this round's best_pruning_node_ids into state.N_log["pruning_history"].

    Only enabled for strategy_1 / strategy_3.
    This field is used by subsequent epochs to filter out "already-completed node_types".
    """
    if pruning_strategy not in ("strategy_1", "strategy_3"):
        return
    if not best_pruning_node_ids:
        return
    if "pruning_history" not in state.N_log:
        state.N_log["pruning_history"] = {"selected_node_types_by_case": {}}
    history = state.N_log["pruning_history"]
    if "selected_node_types_by_case" not in history:
        history["selected_node_types_by_case"] = {}
    # Isolate history of different cases by case_id dimension (state instance may be case-level)
    case_id = getattr(state, "case_id", "") or "__default__"
    selected_set = history["selected_node_types_by_case"].setdefault(case_id, set())
    for nid in best_pruning_node_ids:
        node = node_idx.get(nid)
        if not node:
            continue
        nt = node.get("node_type", "")
        if nt:
            selected_set.add(nt)


# ============================================================
# v8.x modification 2/3: per-case strategy_1 disable flag
# ============================================================

def _is_strategy_1_disabled(state: Any) -> bool:
    """Determine whether strategy_1 has been disabled for this case because "unable to complete missing types".

    Once disabled, subsequent epochs' pruning strategy determination should directly skip strategy_1
    and enter strategy_3/2.
    """
    if not hasattr(state, "N_log"):
        return False
    flag_map = state.N_log.get("disabled_strategies_by_case", {})
    if not isinstance(flag_map, dict):
        return False
    case_id = getattr(state, "case_id", "") or "__default__"
    return "strategy_1" in flag_map.get(case_id, set())


def _disable_strategy_1(state: Any, reason: str) -> None:
    """Set strategy_1 disable flag for this case.

    Call timing:
      - filter_2nd_candidates returns empty (i.e., missing-type candidates are empty)
      - filtered_top10 is empty without fallback
      - select_diverse_top_w cannot select nodes in strict mode
    """
    if "disabled_strategies_by_case" not in state.N_log:
        state.N_log["disabled_strategies_by_case"] = {}
    flag_map = state.N_log["disabled_strategies_by_case"]
    case_id = getattr(state, "case_id", "") or "__default__"
    if case_id not in flag_map:
        flag_map[case_id] = set()
    flag_map[case_id].add("strategy_1")
    # Also record disable reason for subsequent log analysis
    if "disabled_strategies_reasons" not in state.N_log:
        state.N_log["disabled_strategies_reasons"] = {}
    reason_map = state.N_log["disabled_strategies_reasons"]
    if case_id not in reason_map:
        reason_map[case_id] = []
    reason_map[case_id].append({
        "strategy": "strategy_1",
        "reason": reason,
    })


def _get_epoch_excluded_node_types(state: Any) -> set[str]:
    """Read the node_type set selected in this case from state.N_log["pruning_history"]."""
    history = state.N_log.get("pruning_history", {}) if hasattr(state, "N_log") else {}
    by_case = history.get("selected_node_types_by_case", {}) if isinstance(history, dict) else {}
    case_id = getattr(state, "case_id", "") or "__default__"
    selected = by_case.get(case_id, set())
    return set(selected) if isinstance(selected, set) else set(selected)


# ============================================================
# Diversity TopW selection (strategy_1 specific)
# ============================================================

def select_diverse_top_w(
    top10_candidates: list[dict],
    W: int,
    allowed_node_types: set[str] | None = None,
) -> tuple[list[dict], int]:
    """Select TopW nodes satisfying diversity constraints from Top10 candidate nodes.

    Parameters:
        top10_candidates: Top10 candidate nodes already sorted by vote ratio
        W: expected number of nodes to select
        allowed_node_types: allowed node_type set (newly added in modification 1);
            - None: allow all node_types (backward compatible with strategy_2)
            - non-empty set: only allow candidates whose node_type ∈ this set to participate in fallback supplement
            - empty set: no fallback allowed (strict mode)

    Logic (modification 1):
      1. Iterate Top10, prefer selecting higher-ranked nodes without duplicating the same node_type.
      2. If Top10 has N distinct node_types and N >= W: directly select first W nodes with mutually distinct node_types.
      3. If N < W: first select TopN nodes with mutually distinct node_types,
         then supplement from remaining after filtering by allowed_node_types (modification 1: no fallback allowed for non-missing types).

    Returns:
        (selected_candidates, N) — selected_candidates length <= W, N is distinct node_type count in Top10
    """
    if not top10_candidates or W <= 0:
        return [], 0

    # Count distinct node_type count N in Top10
    unique_types_in_top10: set[str] = set()
    for c in top10_candidates:
        nt = c.get("node_type", "")
        if nt:
            unique_types_in_top10.add(nt)
    N = len(unique_types_in_top10)

    selected: list[dict] = []
    used_types: set[str] = set()
    remaining: list[dict] = []

    for c in top10_candidates:
        nt = c.get("node_type", "")
        if nt not in used_types:
            selected.append(c)
            used_types.add(nt)
        else:
            remaining.append(c)

    if N < W:
        # Case 2-1: Top10 cannot cover W distinct node_types
        # Modification 1: fallback-supplemented nodes must satisfy allowed_node_types restriction;
        #                 if allowed_node_types is None (strategy_2) maintain original behavior
        #                 if allowed_node_types is empty set then don't supplement any fallback
        if allowed_node_types is None:
            # Strategy_2 backward-compatible path: original behavior
            need = W - N
            top_need = remaining[:need]
            return selected + top_need, N
        elif not allowed_node_types:
            # Strict mode: no fallback allowed, directly return selected
            return selected, N
        else:
            # Modification 1: only allow candidates within allowed_node_types to enter fallback
            need = W - N
            allowed_fallback: list[dict] = []
            for c in remaining:
                if c.get("node_type", "") in allowed_node_types:
                    allowed_fallback.append(c)
                if len(allowed_fallback) >= need:
                    break
            return selected + allowed_fallback, N
    else:
        # Case 2-2: Top10 sufficient to cover W distinct node_types
        # Modification 1: even when N >= W, when selecting first W fallbacks also filter by allowed_node_types,
        # to prevent unfiltered input (when filtered_top10 is empty and fallback) from mis-selecting non-missing types
        if allowed_node_types is None:
            # Strategy_2 backward-compatible path: original behavior
            return selected[:W], N
        else:
            # Modification 1 strict mode: only allow candidates within allowed_node_types to enter selection pool
            filtered_for_select: list[dict] = []
            seen_types: set[str] = set()
            for c in top10_candidates:
                nt = c.get("node_type", "")
                if nt in allowed_node_types and nt not in seen_types:
                    filtered_for_select.append(c)
                    seen_types.add(nt)
                    if len(filtered_for_select) >= W:
                        break
            # If filtered_for_select is less than W, supplement with remaining allowed_node_types nodes
            if len(filtered_for_select) < W:
                seen_ids: set = {c["node_id"] for c in filtered_for_select}
                for c in top10_candidates:
                    if c["node_id"] in seen_ids:
                        continue
                    if c.get("node_type", "") in allowed_node_types:
                        filtered_for_select.append(c)
                        if len(filtered_for_select) >= W:
                            break
            return filtered_for_select, N


# ============================================================
# Dynamic pruning width (reuse v6 logic)
# ============================================================

def compute_global_pruning_entropy(
    unique_candidates: list[tuple[str, float]],
    config: dict,
) -> float:
    """Take top TopN of candidate node full set by vote ratio desc to compute normalized pruning entropy."""
    TopN = config.get("pruning_entropy_top_n", 10)
    eps = config.get("epsilon", 1e-9)

    topN_candidates = unique_candidates[:TopN]
    n = len(topN_candidates)

    if n == 0:
        return 1.0
    if n == 1:
        return 0.0

    vote_ratios = [vote for _, vote in topN_candidates]
    total_vote = sum(vote_ratios)
    if total_vote == 0:
        return 1.0

    p = [v / total_vote for v in vote_ratios]
    h = 0.0
    for pi in p:
        if pi > 0:
            h -= pi * math.log(pi)

    norm_denom = math.log(min(n, TopN))
    if norm_denom == 0:
        return 0.0
    return h / norm_denom


def compute_fact_sufficiency_19pt(
    Non_alg_group: list[str],
    node_idx: dict[str, dict],
    config: dict,
) -> tuple[float, int]:
    """Compute 19-point fact sufficiency coefficient (v7).

    Returns:
        (A, coverage) where coverage = number of distinct node_types (0~19)
    """
    N_non_alg_type_count_max = config.get("N_non_alg_type_count_max", 19)
    covered_types: set[str] = set()

    for nid in Non_alg_group:
        node = node_idx.get(nid)
        if node is None:
            continue
        node_type = node.get("node_type", "")
        if node_type:
            covered_types.add(node_type)

    coverage = len(covered_types)
    fact_sufficiency = coverage / N_non_alg_type_count_max

    return fact_sufficiency, coverage


def compute_dynamic_width(
    fact_sufficiency_A: float,
    pruning_entropy: float,
    W_init: int,
    W_max: int,
    config: dict,
) -> int:
    """Compute dynamic pruning width (reuse v6 nonlinear enhancement logic)."""
    disable_dynamic_width_below_entropy = config.get(
        "disable_dynamic_width_below_entropy", None
    )
    if (
        disable_dynamic_width_below_entropy is not None
        and pruning_entropy < float(disable_dynamic_width_below_entropy)
    ):
        return min(W_init, W_max)

    W_expand_gamma = config.get("W_expand_gamma", 3)
    eps = config.get("epsilon", 1e-9)
    W_hard_cap = config.get("W_expand_hard_cap", 3)

    entropy_remainder = 1.0 - pruning_entropy
    coeff = fact_sufficiency_A * entropy_remainder

    if coeff <= 0.1:
        extra = math.floor(W_expand_gamma * (1 - coeff) ** 2 / (coeff + eps) + coeff * 5)
    elif coeff <= 0.3:
        extra = math.floor(W_expand_gamma * (1 - coeff) ** 2 / (coeff + eps))
    else:
        extra = math.floor(W_expand_gamma * (1 - coeff) / (coeff + eps))

    W_dynamic = W_init + extra
    return min(W_hard_cap, W_max, max(0, W_dynamic))


# ============================================================
# W-sum group generation
# ============================================================

def generate_wsum_groups(top_w_node_ids: list[str]) -> list[list[str]]:
    """Generate W-sum groups (combinations without replacement).

    Example with W=3, top_w_node_ids=[n1, n2, n3]:
    C(3,3): [n1, n2, n3]
    C(3,2): [n1, n2], [n1, n3], [n2, n3]
    C(3,1): [n1], [n2], [n3]

    Returns:
        list of node_id lists, sorted by combination size descending
    """
    groups = []
    W = len(top_w_node_ids)

    for k in range(W, 0, -1):
        for combo in itertools.combinations(top_w_node_ids, k):
            groups.append(list(combo))

    return groups


# ============================================================
# Concurrent exploration, aggregation, feedback
# ============================================================

def concurrent_explore_wsum_groups(
    wsum_groups: list[list[str]],
    current_node_ids: list[str],
    graph: dict,
    edge_idx: dict[str, dict],
    node_idx: dict[str, dict],
    adjacency: dict | None = None,
) -> list[dict]:
    """Concurrently explore W-sum groups.

    For each W-sum group:
      1. Merge with current_node_ids to get "temporarily updated existing non-algorithm node set"
      2. Execute exploration on this set (call explore_mod.explore_for_node_ids)

    adjacency: optional adjacency list (performance optimization); fallback to O(E) full-graph scan when not provided.

    Returns:
        list[dict]: each element corresponds to one W-sum group's exploration result
        [
            {
                "group_index": w,  # 1-indexed
                "group_node_ids": [...],  # this group's node IDs
                "temp_node_ids": [...],   # temporarily updated existing non-algorithm node set = current + group
                "explore_result": {...},  # explore_for_node_ids return value
            },
            ...
        ]
    """
    results = []

    for w, group_node_ids in enumerate(wsum_groups, start=1):
        # Temporarily update existing non-algorithm node set = current_node_ids ∪ group_node_ids
        temp_node_ids = list(set(current_node_ids) | set(group_node_ids))

        # Execute exploration on temporary node set
        explore_result = explore_mod.explore_for_node_ids(
            temp_node_ids, graph, edge_idx, node_idx, adjacency=adjacency
        )

        results.append({
            "group_index": w,
            "group_node_ids": group_node_ids,
            "temp_node_ids": temp_node_ids,
            "explore_result": explore_result,
        })

    return results


def concurrent_vote_wsum_groups(
    explore_results: list[dict],
    graph: dict,
    edge_idx: dict[str, dict],
    node_idx: dict[str, dict],
    config: dict,
) -> list[dict]:
    """Concurrently aggregate W-sum groups' exploration results.

    Execute aggregation computation for each W-sum group, get each node_type's TopK recommended algorithms and vote ratios.

    Returns:
        list[dict]: each element corresponds to one W-sum group's aggregation result
        [
            {
                "group_index": w,
                "group_node_ids": [...],
                "temp_node_ids": [...],
                "vote_result": {
                    "by_algorithm_type": {
                        "15-DataPreprocessingAlgorithmClass": {
                            "Top_K": [{"node_id": ..., "node_name": ..., "vote_ratio": ...}, ...],
                            "R_i_max": ...,
                            "V_i": ...,
                        },
                        ...
                    },
                    "fact_sufficiency_A": ...,
                    "Thinking_belief": ...,
                },
            },
            ...
        ]
    """
    vote_results = []

    for item in explore_results:
        explore_result = item["explore_result"]
        source_node_ids = item["temp_node_ids"]

        vote_result = aggregate_mod.vote_from_explore_result(
            explore_result,
            graph,
            edge_idx,
            node_idx,
            config,
            source_node_ids,
        )

        vote_results.append({
            "group_index": item["group_index"],
            "group_node_ids": item["group_node_ids"],
            "temp_node_ids": item["temp_node_ids"],
            "vote_result": vote_result,
        })

    return vote_results


def compute_feedback(
    wsum_vote_results: list[dict],
    prev_vote_result: dict,
    config: dict,
) -> dict[str, int]:
    """Concurrent feedback: compare Epoch(i-1) with each W-sum group's vote ratio improvements.

    For each W-sum group, compute its vote ratio gain count over Epoch(i-1) on node_type (15-19).

    Algorithm:
      For node_type j (15-19):
        max(V(i)[w]_j) = max_{k} vote_ratio of algorithm k in type j
        max(V(i-1)_j)  = max_{k} vote_ratio of algorithm k in type j (Epoch i-1)

      If max(V(i)[w]_j) >= max(V(i-1)_j), count as 1 gain
      n(i)[w] = sum_j [max(V(i)[w]_j) >= max(V(i-1)_j)] for j in [15..19]

    Returns:
        dict[str, int]: {group_index -> n(i)[w]}
    """
    gain_threshold = config.get("feedback_gain_threshold", 3)
    feedback_gains: dict[str, int] = {}

    # Extract Epoch(i-1)'s max vote ratio per category
    prev_max_by_type: dict[str, float] = {}
    prev_by_type = prev_vote_result.get("by_algorithm_type", {})
    for alg_type, data in prev_by_type.items():
        top_k = data.get("Top_K", [])
        if top_k:
            max_ratio = max(c["vote_ratio"] for c in top_k)
            prev_max_by_type[alg_type] = max_ratio
        else:
            prev_max_by_type[alg_type] = 0.0

    for item in wsum_vote_results:
        group_index = item["group_index"]
        vote_result = item["vote_result"]
        by_type = vote_result.get("by_algorithm_type", {})

        gain_count = 0
        for alg_type, data in by_type.items():
            top_k = data.get("Top_K", [])
            if not top_k:
                current_max = 0.0
            else:
                current_max = max(c["vote_ratio"] for c in top_k)

            prev_max = prev_max_by_type.get(alg_type, 0.0)
            if current_max >= prev_max:
                gain_count += 1

        feedback_gains[str(group_index)] = gain_count

    return feedback_gains


def select_best_wsum_group(
    wsum_vote_results: list[dict],
    feedback_gains: dict[str, int],
    config: dict,
) -> tuple[dict | None, str, int]:
    """Select the optimal candidate node set from W-sum groups.

    Selection rules:
      - Select group with highest n(i)[w]
      - If max n(i)[w] >= feedback_gain_threshold → "success"
      - Otherwise → "failure"

    Returns:
        (best_group, status, max_gain)
        best_group: optimal group's detail dict, or None (no available group)
        status: "success" | "failure"
        max_gain: max gain count
    """
    if not wsum_vote_results:
        return None, "failure", 0

    gain_threshold = config.get("feedback_gain_threshold", 3)

    # Find group with highest gain
    best_group = None
    max_gain = -1

    for item in wsum_vote_results:
        gidx = str(item["group_index"])
        gain = feedback_gains.get(gidx, 0)
        if gain > max_gain:
            max_gain = gain
            best_group = item

    if best_group is None:
        return None, "failure", 0

    status = "success" if max_gain >= gain_threshold else "failure"
    return best_group, status, max_gain


# ============================================================
# Main entry
# ============================================================

def prune_for_next_epoch(
    state: Any,
    epoch_key: str,
    next_epoch_key: str,
    graph: dict,
    config: dict,
    edge_idx: dict[str, dict],
    node_idx: dict[str, dict],
    epoch_idx: int = 0,
    adjacency: dict | None = None,
) -> dict:
    """Execute v7 complete pruning flow (including concurrent pruning-exploration-aggregation loop).

    Steps:
      1. Collect Non_alg_group (all non-algorithm nodes up to current Epoch)
      2. Compute fact sufficiency A (19-point)
      3. Decide pruning strategy based on A (strategy_1 or strategy_2)
      4. Collect candidate edges and nodes → filter valid candidate edges/valid 1st candidate nodes → filter valid 2nd candidate nodes
      5. Sort by vote ratio, take Top10
      6. Compute dynamic pruning width W, take TopW
      7. Generate W-sum groups
      8. Concurrent exploration + concurrent aggregation + concurrent feedback
      9. Select optimal group or backtrack and retry (max max_feedback_times times)
      10. Assemble N_pruning array entry and return

    Parameters:
        state: ReasoningState
        epoch_key: current Epoch key name
        next_epoch_key: reserved parameter (compatible with caller)
        graph: standardized graph
        config: configuration object
        edge_idx / node_idx: index dicts
        epoch_idx: Epoch index (starts from 1)

    Returns:
        pruning_result: {
            "current_node_ids": [...],
            "newly_selected_node_ids": [...],   # best_pruning_node_ids
            "next_node_ids": [...],
            "fact_sufficiency_A": ...,
            "pruning_strategy": "strategy_1" | "strategy_2",
            "pruning_status": "success" | "failure",
            "pruning_time": ...,
            "feedback_details": [...],
        }
    """
    # Step 1: Collect Non_alg_group (all non-algorithm nodes explored up to current Epoch)
    Non_alg_group: list[str] = []
    _seen: set[str] = set()
    for ek, edata in state.N_Explore.items():
        for nid in edata.keys():
            if nid not in _seen:
                Non_alg_group.append(nid)
                _seen.add(nid)

    # Step 2: Node set participating in exploration in current Epoch
    current_node_ids: list[str] = list(state.N_Explore.get(epoch_key, {}).keys())
    if not current_node_ids:
        pruning_result = {
            "current_node_ids": [],
            "newly_selected_node_ids": [],
            "next_node_ids": [],
            "fact_sufficiency_A": 0.0,
            "pruning_strategy": "none",
            "pruning_status": "failure",
            "pruning_time": 0,
            "feedback_details": [],
        }
        _write_pruning_log(state, epoch_key, pruning_result, "no_current_nodes", [])
        return pruning_result

    # Step 3: Collect candidate next-hop non-algorithm nodes
    Non_alg_next_by_node = collect_non_algorithm_candidates(
        state, epoch_key, graph, edge_idx, node_idx, Non_alg_group
    )

    # Step 3a: Early-stop determination (all current_node have no candidate next-hops)
    if all(len(cands) == 0 for cands in Non_alg_next_by_node.values()):
        all_next_ids = list(set(Non_alg_group))
        pruning_result = {
            "current_node_ids": current_node_ids,
            "newly_selected_node_ids": [],
            "next_node_ids": all_next_ids,
            "fact_sufficiency_A": 0.0,
            "pruning_strategy": "converged",
            "pruning_status": "success",
            "pruning_time": 0,
            "feedback_details": [],
        }
        _write_pruning_log(state, epoch_key, pruning_result,
                           "converged_no_non_alg_next_candidates",
                           ["All current nodes have zero non-algorithm next-hop candidates."])
        return pruning_result

    # Step 4: Compute fact sufficiency A (19-point)
    A, coverage = compute_fact_sufficiency_19pt(Non_alg_group, node_idx, config)
    N_max = config.get("N_non_alg_type_count_max", 19)

    # Step 4a: Evaluate node_type coverage status (used for strategy_1 vs strategy_3 determination)
    coverage_status = compute_type_coverage_status(Non_alg_group, node_idx)

    # Step 5: Determine pruning strategy (v8.1 newly added strategy_3)
    # Determination order:
    #   - A >= 1.0  → strategy_2 (fact sufficiency complete, supplement potential facts)
    #   - A < 1.0 AND 1-14 codes not fully covered → strategy_1 (prioritize completing 1-14)
    #   - A < 1.0 AND 1-14 fully covered BUT 15-19-Induction not fully covered → strategy_3 (complete induction algorithm nodes)
    #   - Other cases (A < 1.0 AND all complete theoretically impossible) → strategy_2 (fallback)
    #
    # v8.x modification 2 workaround: if this case has already disabled strategy_1 because "unable to complete missing types",
    #   then skip strategy_1 in this round and directly enter strategy_3/2, to avoid infinite loop
    #
    # v8.x modification 3 optimization: place "strategy_1 disabled branch" at the top of the if chain,
    #   so determination order corresponds one-to-one with strategy semantics:
    #     - A >= 1.0  → strategy_2 (fact sufficiency complete)
    #     - strategy_1 disabled  → skip strategy_1, check if Induction is complete
    #         - induction not complete → strategy_3
    #         - induction complete → strategy_2
    #     - 1-14 not fully covered  → strategy_1
    #     - 1-14 fully covered BUT Induction not covered  → strategy_3
    #     - Other → strategy_2 (fallback)
    if A >= 1.0:
        pruning_strategy = "strategy_2"
    elif _is_strategy_1_disabled(state):
        # Strategy_1 has been disabled (unable to complete missing types), skip strategy_1
        if not coverage_status["induction_full"]:
            pruning_strategy = "strategy_3"
        else:
            pruning_strategy = "strategy_2"
    elif not coverage_status["non_alg_full"]:
        pruning_strategy = "strategy_1"
    elif not coverage_status["induction_full"]:
        pruning_strategy = "strategy_3"
    else:
        # Theoretically unreachable (coverage_status all complete when A=1, already caught by first branch)
        pruning_strategy = "strategy_2"

    # Step 6: Filter valid candidate edges and valid 1st candidate nodes
    if pruning_strategy == "strategy_3":
        # Strategy_3: filter only by 01-default-edge + target=induction algorithm node
        valid_edges, valid_1st_node_ids = filter_valid_induction_candidates(
            Non_alg_next_by_node, Non_alg_group, node_idx
        )
    else:
        # Strategy_1 / Strategy_2: filter by edge_group 02-CausalEdge / 03-EvidenceEdge
        valid_edges, valid_1st_node_ids = filter_valid_candidates(Non_alg_next_by_node)

    if not valid_1st_node_ids:
        pruning_result = {
            "current_node_ids": current_node_ids,
            "newly_selected_node_ids": [],
            "next_node_ids": list(set(current_node_ids)),
            "fact_sufficiency_A": round(A, 6),
            "pruning_strategy": pruning_strategy,
            "pruning_status": "failure",
            "pruning_time": 0,
            "feedback_details": [],
        }
        _write_pruning_log(state, epoch_key, pruning_result, "no_valid_1st_candidates", [])
        return pruning_result

    # Step 7: Filter valid 2nd candidate nodes
    # v8.x modification 4: filter_2nd_candidates has internally applied strict "missing node_type" filter
    excluded_types_for_step7 = _get_epoch_excluded_node_types(state)
    candidates_2nd = filter_2nd_candidates(
        valid_1st_node_ids,
        Non_alg_group,
        node_idx,
        pruning_strategy,
        coverage_status=coverage_status,
        excluded_node_types=excluded_types_for_step7,
    )

    # v8.x modification 2 workaround: for strategy_1/3, if "missing-type candidates are empty"
    # it means the graph already has no valid candidate nodes of missing types, avoid trying strategy_1 next epoch
    if (
        not candidates_2nd
        and pruning_strategy in ("strategy_1", "strategy_3")
        and not coverage_status.get("non_alg_full", True)
        and pruning_strategy == "strategy_1"
    ):
        _disable_strategy_1(
            state,
            reason=(
                f"missing_node_type_no_candidates: "
                f"missing_codes={sorted(coverage_status.get('missing_non_alg_codes', []))}, "
                f"no valid 2nd candidates in current graph topology"
            ),
        )

    # Step 8: Compute vote ratios and sort, take Top10
    vote_ratios = compute_vote_ratios_for_2nd_candidates(
        candidates_2nd, Non_alg_next_by_node, Non_alg_group, pruning_strategy, node_idx
    )
    sorted_candidates = sort_2nd_candidates(candidates_2nd, vote_ratios)
    top_n = config.get("pruning_top_n_candidates", 10)
    top10_candidates = sorted_candidates[:top_n]

    if not top10_candidates:
        pruning_result = {
            "current_node_ids": current_node_ids,
            "newly_selected_node_ids": [],
            "next_node_ids": list(set(current_node_ids)),
            "fact_sufficiency_A": round(A, 6),
            "pruning_strategy": pruning_strategy,
            "pruning_status": "failure",
            "pruning_time": 0,
            "feedback_details": [],
        }
        # v8.x modification 2: disable strategy_1 when strategy_1 candidates are empty
        if pruning_strategy == "strategy_1" and not coverage_status.get("non_alg_full", True):
            _disable_strategy_1(
                state,
                reason="top10_candidates_empty_strategy_1_disabled",
            )
        _write_pruning_log(state, epoch_key, pruning_result, "no_valid_2nd_candidates", [])
        return pruning_result

    # Step 9: Compute dynamic pruning width W, diversity TopW selection
    unique_candidates_tuples = [
        (c["node_id"], vote_ratios.get(c["node_id"], 0.0))
        for c in top10_candidates
    ]
    global_entropy = compute_global_pruning_entropy(unique_candidates_tuples, config)
    W_init = config.get("W_init", 2)
    W_dynamic = compute_dynamic_width(A, global_entropy, W_init, len(top10_candidates), config)

    # Strategy_1 (A < 1) or Strategy_3 (induction not complete): enable diversity TopW selection
    # Strategy_3 same as strategy_1: each pruning round must prioritize querying different node_types
    if pruning_strategy in ("strategy_1", "strategy_3"):
        # v8.x modification: first filter Top10 candidates by "missing node_type",
        # simultaneously exclude node_types selected in previous epochs of this case,
        # then call select_diverse_top_w for diversity selection.
        excluded_types = _get_epoch_excluded_node_types(state)
        filtered_top10 = _filter_candidates_by_missing_type(
            top10_candidates, coverage_status, pruning_strategy, excluded_types
        )
        # v8.x modification 2: when filtered_top10 is empty, disable strategy_1 (only strategy_1 scenario)
        if not filtered_top10 and pruning_strategy == "strategy_1":
            _disable_strategy_1(
                state,
                reason=(
                    f"missing_node_type_no_top10_candidates: "
                    f"missing_codes={sorted(coverage_status.get('missing_non_alg_codes', []))}, "
                    f"filtered_top10 is empty"
                ),
            )
            pruning_result = {
                "current_node_ids": current_node_ids,
                "newly_selected_node_ids": [],
                "next_node_ids": list(set(current_node_ids)),
                "fact_sufficiency_A": round(A, 6),
                "pruning_strategy": pruning_strategy,
                "pruning_status": "failure",
                "pruning_time": 0,
                "feedback_details": [],
            }
            _write_pruning_log(
                state, epoch_key, pruning_result,
                "filtered_top10_empty_strategy_1_disabled", [],
                coverage=f"{coverage}/{N_max}",
            )
            return pruning_result

        # If filtered is empty (meaning missing types have no candidates in Top10), fall back to original Top10
        # to preserve backtrack logic usability; W_dynamic_zero will still be truncated below
        top10_for_select = filtered_top10 if filtered_top10 else top10_candidates
        # v8.x modification 1: select_diverse_top_w adds allowed_node_types parameter
        # Compute allowed fallback node_type set (= missing type node type name set)
        if pruning_strategy == "strategy_1":
            allowed_nt: set[str] = set()
            for code in coverage_status.get("missing_non_alg_codes", set()):
                tn = cfg.NODE_TYPE_CODE_TO_NAME.get(code, "")
                if tn:
                    allowed_nt.add(tn)
        else:  # strategy_3
            allowed_nt = {
                cfg.INDUCTION_TYPE_NAMES.get(str(code), "")
                for code in coverage_status.get("missing_induction_codes", set())
            }
            allowed_nt.discard("")
        top_w_candidates, diversity_N = select_diverse_top_w(
            top10_for_select, W_dynamic, allowed_node_types=allowed_nt
        )
    else:
        # Strategy_2: maintain original logic
        top_w_candidates = top10_candidates[:W_dynamic]
        diversity_N = len({c.get("node_type", "") for c in top_w_candidates})

    top_w_node_ids = [c["node_id"] for c in top_w_candidates]

    if not top_w_node_ids:
        pruning_result = {
            "current_node_ids": current_node_ids,
            "newly_selected_node_ids": [],
            "next_node_ids": list(set(current_node_ids)),
            "fact_sufficiency_A": round(A, 6),
            "pruning_strategy": pruning_strategy,
            "pruning_status": "failure",
            "pruning_time": 0,
            "feedback_details": [],
        }
        _write_pruning_log(state, epoch_key, pruning_result, "W_dynamic_zero", [])
        return pruning_result

    # Step 10: Generate W-sum groups
    wsum_groups = generate_wsum_groups(top_w_node_ids)

    # Step 11: Get Epoch(i-1)'s aggregation result (used for feedback comparison)
    prev_epoch_key = f"Epoch{epoch_idx - 1}" if epoch_idx > 1 else None
    prev_vote_result: dict = {}
    if prev_epoch_key and prev_epoch_key in state.N_vote:
        prev_vote_result = state.N_vote[prev_epoch_key]
    else:
        # Epoch1 has no previous round, take current round's result as baseline (all gains are 0)
        prev_vote_result = state.N_vote.get(epoch_key, {})

    # Step 12: Concurrent exploration + concurrent aggregation (direct computation if only one group)
    if len(wsum_groups) == 1:
        # Single group doesn't need concurrency, directly explore and aggregate
        explore_results = concurrent_explore_wsum_groups(
            wsum_groups, current_node_ids, graph, edge_idx, node_idx, adjacency=adjacency
        )
        vote_results = concurrent_vote_wsum_groups(
            explore_results, graph, edge_idx, node_idx, config
        )
    else:
        # Multiple groups: explore first then aggregate
        explore_results = concurrent_explore_wsum_groups(
            wsum_groups, current_node_ids, graph, edge_idx, node_idx, adjacency=adjacency
        )
        vote_results = concurrent_vote_wsum_groups(
            explore_results, graph, edge_idx, node_idx, config
        )

    # Step 13: Concurrent feedback
    feedback_gains = compute_feedback(vote_results, prev_vote_result, config)

    # Step 14: Select optimal group
    best_group, status, max_gain = select_best_wsum_group(
        vote_results, feedback_gains, config
    )

    # Step 15: Feedback loop (backtrack logic)
    max_feedback_times = config.get("max_feedback_times", 5)
    feedback_details = []
    remaining_candidates = list(top10_candidates)
    f = 0

    while f < max_feedback_times:
        f += 1

        # Build current round's W-sum group feedback info
        wsum_pruning_node_ids: dict[str, list] = {}
        wsum_num_increasing_max_vote: dict[str, int] = {}

        for item in vote_results:
            gidx = str(item["group_index"])
            wsum_pruning_node_ids[gidx] = item["group_node_ids"]
            wsum_num_increasing_max_vote[gidx] = feedback_gains.get(gidx, 0)

        feedback_details.append({
            "feedback_time": f,
            "W_dynamic_n": W_dynamic,
            "Wsum_pruning_node_ids": wsum_pruning_node_ids,
            "Wsum_num_increasing_max_vote": wsum_num_increasing_max_vote,
        })

        if status == "success":
            # Success: record optimal group and exit
            break

        # Failure: backtrack - remove highest-ranked node from Top10 candidates
        if len(remaining_candidates) <= 1:
            # No more nodes to backtrack
            break

        # Remove highest-ranked node
        removed_node = remaining_candidates.pop(0)

        if len(remaining_candidates) < W_dynamic:
            # Remaining nodes insufficient to fill TopW, skip
            break

        # Re-perform diversity TopW selection (both strategy_1 and strategy_3 enabled)
        # Strategy_1 (complete 1-14) and strategy_3 (complete 15-19-Induction) both need "each round prioritizes querying different node_types"
        if pruning_strategy in ("strategy_1", "strategy_3"):
            # v8.x modification 3: also filter remaining_candidates by "missing node_type" during backtrack,
            # to ensure only missing types are completed, avoid strategy_1/3 mis-selecting existing types;
            # if filtered is empty, directly end strategy_1 backtrack (Step 5's flag will skip strategy_1 next epoch)
            excluded_types_bt = _get_epoch_excluded_node_types(state)
            updated_top10 = _filter_candidates_by_missing_type(
                remaining_candidates, coverage_status, pruning_strategy, excluded_types_bt
            )
            # v8.x modification 3: no fallback to original remaining_candidates when filtered_top10 is empty
            if not updated_top10:
                # Only disable strategy_1 for strategy_1; for strategy_3 directly break
                if pruning_strategy == "strategy_1" and not coverage_status.get("non_alg_full", True):
                    _disable_strategy_1(
                        state,
                        reason=(
                            f"backtrack_filtered_top10_empty: "
                            f"missing_codes={sorted(coverage_status.get('missing_non_alg_codes', []))}"
                        ),
                    )
                break
            # remaining_candidates as new Top10 pool, re-execute select_diverse_top_w
            # Note: remaining_candidates may not have 10, but select_diverse_top_w internally uses
            # len(top10_candidates) to compute unique_types_in_top10, original top10 not appropriate here
            # should use updated_top10 = remaining_candidates to recompute
            updated_unique_types = len({c.get("node_type", "") for c in updated_top10 if c.get("node_type", "")})
            if updated_unique_types == 0:
                updated_top_w = updated_top10[:W_dynamic]
            elif updated_unique_types >= W_dynamic:
                used_types: set[str] = set()
                selected_new: list[dict] = []
                for c in updated_top10:
                    nt = c.get("node_type", "")
                    if nt not in used_types:
                        selected_new.append(c)
                        used_types.add(nt)
                        if len(selected_new) >= W_dynamic:
                            break
                updated_top_w = selected_new
            else:
                used_types2: set[str] = set()
                selected_unique: list[dict] = []
                remaining_new: list[dict] = []
                for c in updated_top10:
                    nt = c.get("node_type", "")
                    if nt not in used_types2:
                        selected_unique.append(c)
                        used_types2.add(nt)
                    else:
                        remaining_new.append(c)
                updated_top_w = selected_unique + remaining_new[:W_dynamic - len(selected_unique)]
            remaining_ids = [c["node_id"] for c in updated_top_w]
        else:
            remaining_ids = [c["node_id"] for c in remaining_candidates[:W_dynamic]]

        wsum_groups = generate_wsum_groups(remaining_ids)

        # Re-explore + re-aggregate
        explore_results = concurrent_explore_wsum_groups(
            wsum_groups, current_node_ids, graph, edge_idx, node_idx, adjacency=adjacency
        )
        vote_results = concurrent_vote_wsum_groups(
            explore_results, graph, edge_idx, node_idx, config
        )

        # Re-feedback
        feedback_gains = compute_feedback(vote_results, prev_vote_result, config)
        best_group, status, max_gain = select_best_wsum_group(
            vote_results, feedback_gains, config
        )

    # Step 16: Assemble result
    if status == "success" and best_group is not None:
        best_pruning_node_ids = best_group["group_node_ids"]
        next_node_ids = list(set(current_node_ids) | set(best_pruning_node_ids))
        newly_selected_node_ids = best_pruning_node_ids

        # v8.x modification: record this round's selected node_types into state, for subsequent epochs to filter "already-completed types"
        _record_epoch_selected_node_types(
            state, best_pruning_node_ids, node_idx, pruning_strategy
        )

        # Build best_pruning_recommend_vote_list
        best_vote = best_group["vote_result"]
        best_vote_list = _build_recommend_vote_list(best_vote.get("by_algorithm_type", {}))
    else:
        best_pruning_node_ids = None
        next_node_ids = list(set(current_node_ids))
        newly_selected_node_ids = []
        best_vote_list = {}

    # Step 16b (v8.x modification 3 fix):
    # Original coverage_status/A was computed using Non_alg_group at the time of entering pruning in Step 4a,
    # but best_pruning_node_ids is only determined now. Without correction,
    # this Epoch's coverage_status always lags 1 round, causing:
    #   (a) even if best completes missing 1-14 types, coverage_status still reports missing
    #   (b) next Epoch will see non_alg_full=True and enter strategy_3,
    #       but next Epoch's N_Explore may have no valid candidate edges -> pruning failure
    # Fix: recompute coverage_status and A with "Non_alg_group containing best_pruning_node_ids",
    #      overriding Step 4a's old values.
    if best_pruning_node_ids:
        Non_alg_group_with_best = list(set(Non_alg_group) | set(best_pruning_node_ids))
    else:
        Non_alg_group_with_best = Non_alg_group
    coverage_status_updated = compute_type_coverage_status(
        Non_alg_group_with_best, node_idx
    )
    A_updated, coverage_updated = compute_fact_sufficiency_19pt(
        Non_alg_group_with_best, node_idx, config
    )
    coverage_status = coverage_status_updated
    A = A_updated
    coverage = coverage_updated

    # Build current_recommend_vote_list (from current N_vote)
    current_vote = state.N_vote.get(epoch_key, {})
    current_vote_list = _build_recommend_vote_list(
        current_vote.get("by_algorithm_type", {})
    )

    # Step 17: Assemble N_pruning array entry (including diversity info)
    n_pruning_entry = {
        "Epoch": epoch_key,
        "current_node_ids": current_node_ids,
        "current_recommend_vote_list": current_vote_list,
        "fact_sufficiency_A": round(A, 6),
        "pruning_strategy": pruning_strategy,
        "pruning_time": f,
        "pruning_status": status,
        "best_pruning_node_ids": best_pruning_node_ids,
        "best_pruning_recommend_vote_list": best_vote_list,
        "next_node_ids": next_node_ids,
        "feedback_details": feedback_details,
        # Coverage status (v8.1 newly added strategy_3 specific), used to explain strategy selection basis
        "coverage_status": {
            "non_alg_full": coverage_status["non_alg_full"],
            "induction_full": coverage_status["induction_full"],
            "missing_non_alg_codes": sorted(coverage_status["missing_non_alg_codes"]),
            "missing_induction_codes": sorted(coverage_status["missing_induction_codes"]),
            "covered_non_alg_count": len(coverage_status["covered_non_alg_codes"]),
            "covered_induction_count": len(coverage_status["covered_induction_codes"]),
        },
        # Diversity info (shared by strategy_1 and strategy_3)
        "diversity_info": {
            "diversity_N": diversity_N,
            "W_dynamic": W_dynamic,
            "top10_candidates": [
                {"node_id": c["node_id"], "node_name": c["node_name"],
                 "node_type": c["node_type"], "vote_ratio": c["vote_ratio"]}
                for c in top10_candidates
            ],
            "top_w_candidates": [
                {"node_id": c["node_id"], "node_name": c["node_name"],
                 "node_type": c["node_type"], "vote_ratio": c["vote_ratio"]}
                for c in top_w_candidates
            ],
        },
    }

    # Append entry to N_pruning array
    state.N_pruning.append(n_pruning_entry)

    # Assemble return result (backward compatible with existing callers)
    pruning_result = {
        "current_node_ids": current_node_ids,
        "newly_selected_node_ids": newly_selected_node_ids,
        "next_node_ids": next_node_ids,
        "fact_sufficiency_A": round(A, 6),
        "pruning_strategy": pruning_strategy,
        "pruning_status": status,
        "pruning_time": f,
        "feedback_details": feedback_details,
    }

    # Log
    warnings = []
    if status == "failure":
        warnings.append(f"feedback_status=failure after {f} feedback iterations")
    _write_pruning_log(state, epoch_key, pruning_result,
                       f"{pruning_strategy}_{status}", warnings,
                       wsum_groups_count=len(wsum_groups),
                       feedback_gains=feedback_gains,
                       global_entropy=round(global_entropy, 6),
                       W_dynamic=W_dynamic,
                       coverage=f"{coverage}/{N_max}",
                       max_gain=max_gain,
                       diversity_N=diversity_N,
                       top_w_node_ids=top_w_node_ids,
                       coverage_status={
                           "non_alg_full": coverage_status["non_alg_full"],
                           "induction_full": coverage_status["induction_full"],
                           "missing_non_alg_codes": sorted(coverage_status["missing_non_alg_codes"]),
                           "missing_induction_codes": sorted(coverage_status["missing_induction_codes"]),
                           "covered_non_alg_count": len(coverage_status["covered_non_alg_codes"]),
                           "covered_induction_count": len(coverage_status["covered_induction_codes"]),
                       })

    return pruning_result


# ============================================================
# Helper functions
# ============================================================

def _build_recommend_vote_list(by_algorithm_type: dict) -> dict[str, str]:
    """Build recommended vote ratio list string (for N_pruning array)."""
    result = {}
    for alg_type, candidates_data in by_algorithm_type.items():
        top_k = candidates_data.get("Top_K", [])
        if not top_k:
            result[alg_type] = "null + null + 0.0"
            continue
        best = max(top_k, key=lambda x: x["vote_ratio"])
        result[alg_type] = (
            f"{best['node_id']} + {best['node_name']} + {best['vote_ratio']:.4f}"
        )
    return result


def _write_pruning_log(
    state: Any,
    epoch_key: str,
    pruning_result: dict,
    reason: str,
    warnings: list[str],
    wsum_groups_count: int = 0,
    feedback_gains: dict[str, int] | None = None,
    global_entropy: float = 0.0,
    W_dynamic: int = 0,
    coverage: str = "0/19",
    max_gain: int = 0,
    diversity_N: int = 0,
    top_w_node_ids: list[str] | None = None,
    coverage_status: dict | None = None,
) -> None:
    """Write pruning log into state.N_log["epoch_logs"]."""
    log = {
        "step": "prune",
        "epoch_key": epoch_key,
        "storage_target": f"N_log.epoch_logs.{epoch_key}.pruning_log",
        "main_state_target": "N_pruning (list, append)",
        "current_node_ids": pruning_result.get("current_node_ids", []),
        "newly_selected_node_ids": pruning_result.get("newly_selected_node_ids", []),
        "next_node_ids": pruning_result.get("next_node_ids", []),
        "fact_sufficiency_A": pruning_result.get("fact_sufficiency_A", 0.0),
        "pruning_strategy": pruning_result.get("pruning_strategy", ""),
        "pruning_status": pruning_result.get("pruning_status", ""),
        "pruning_time": pruning_result.get("pruning_time", 0),
        "feedback_details": pruning_result.get("feedback_details", []),
        "wsum_groups_count": wsum_groups_count,
        "feedback_gains": feedback_gains or {},
        "global_pruning_entropy": global_entropy,
        "W_dynamic": W_dynamic,
        "fact_coverage": coverage,
        "max_gain": max_gain,
        "diversity_N": diversity_N,
        "top_w_node_ids": top_w_node_ids or [],
        "coverage_status": coverage_status or {},
        "reason": reason,
        "warnings": warnings,
    }
    if epoch_key not in state.N_log["epoch_logs"]:
        state.N_log["epoch_logs"][epoch_key] = {}
    state.N_log["epoch_logs"][epoch_key]["pruning_log"] = log
