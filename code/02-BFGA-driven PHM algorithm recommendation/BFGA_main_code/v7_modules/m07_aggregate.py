# -*- coding: utf-8 -*-
r"""
v7_modules/07_aggregate.py
==========================
Aggregation module (Vote).

v7 main changes from v6:
  - Fact sufficiency calculation changed to 19-point system (each node_type counts only 1 point, max 19 points)
  - Other logic (vote ratio calculation, Top-K, grouping, etc.) remains unchanged
  - Added compute_fact_sufficiency_v7 (19-point system) and compute_fact_sufficiency_v6 (compatible with old calculation)
"""

import math
from typing import Any

from . import m00_config as cfg


def collect_non_algorithm_nodes(state: Any, graph: dict, node_idx: dict | None = None) -> list[str]:
    """Collect non-algorithm node ID list from all explored Epochs.

    Optimization note (performance):
      - When caller passes node_idx, node type determination uses O(1) dict lookup,
        avoiding the original O(N×N) graph["nodes"] full table linear scan.
      - When node_idx is not passed, fall back to original behavior (backward compatible).
    """
    non_alg_ids = set()
    for epoch_key, epoch_data in state.N_Explore.items():
        for node_id in epoch_data.keys():
            if node_idx is not None:
                node = node_idx.get(node_id)
            else:
                node = None
                for n in graph["nodes"]:
                    if n.get("node_id", "") == node_id:
                        node = n
                        break
            if node is None:
                continue
            node_type = node.get("node_type", "")
            if cfg.is_non_algorithm_node(node_type):
                non_alg_ids.add(node_id)
    return list(non_alg_ids)


def collect_algorithm_candidates(
    state: Any,
    Non_alg_group: list[str],
    graph: dict,
    edge_idx: dict[str, dict],
    node_idx: dict | None = None,
) -> dict[str, list[str]]:
    """Collect concrete algorithm candidate nodes (Alg_group) connected from non-algorithm nodes.

    Optimization note (performance):
      - When caller passes node_idx, edge endpoint node type determination uses O(1) dict lookup,
        avoiding the original O(E×N) graph["nodes"] full table linear scan.
      - When node_idx is not passed, fall back to original behavior (backward compatible).
    """
    Alg_group: dict[str, list[str]] = {nid: [] for nid in Non_alg_group}

    for epoch_key, epoch_data in state.N_Explore.items():
        for node_id, node_info in epoch_data.items():
            if node_id not in Non_alg_group:
                continue
            candidate_edge_ids = node_info.get("candidate_edge_ids", [])
            for eid in candidate_edge_ids:
                edge = edge_idx.get(eid)
                if edge is None:
                    continue
                src = edge.get("source_node_id", "")
                tgt = edge.get("target_node_id", "")

                if node_idx is not None:
                    src_node = node_idx.get(src)
                    tgt_node = node_idx.get(tgt)
                    if src_node and cfg.is_concrete_algorithm_node(src_node.get("node_type", "")):
                        if node_id in Alg_group:
                            Alg_group[node_id].append(src)
                    if tgt_node and cfg.is_concrete_algorithm_node(tgt_node.get("node_type", "")):
                        if node_id in Alg_group:
                            Alg_group[node_id].append(tgt)
                else:
                    for n in graph["nodes"]:
                        nid = n.get("node_id", "")
                        if nid == src and cfg.is_concrete_algorithm_node(n.get("node_type", "")):
                            if node_id in Alg_group:
                                Alg_group[node_id].append(nid)
                        if nid == tgt and cfg.is_concrete_algorithm_node(n.get("node_type", "")):
                            if node_id in Alg_group:
                                Alg_group[node_id].append(nid)

    for nid in Alg_group:
        Alg_group[nid] = list(set(Alg_group[nid]))
    return Alg_group


def collect_algorithm_candidates_from_explore_result(
    explore_result: dict[str, dict],
    graph: dict,
    edge_idx: dict[str, dict],
    node_idx: dict[str, dict],
) -> dict[str, list[str]]:
    """Collect Alg_group from exploration result (used for concurrent pruning phase).

    Similar to collect_algorithm_candidates, but exploration result comes from
    explore_for_node_ids return value, not state.N_Explore.
    """
    Alg_group: dict[str, list[str]] = {}

    for node_id, info in explore_result.items():
        Alg_group[node_id] = []
        candidate_edge_ids = info.get("candidate_edge_ids", [])
        for eid in candidate_edge_ids:
            edge = edge_idx.get(eid)
            if edge is None:
                continue
            src = edge.get("source_node_id", "")
            tgt = edge.get("target_node_id", "")

            for nid in [src, tgt]:
                node = node_idx.get(nid)
                if node and cfg.is_concrete_algorithm_node(node.get("node_type", "")):
                    if node_id in Alg_group:
                        Alg_group[node_id].append(nid)

    for nid in Alg_group:
        Alg_group[nid] = list(set(Alg_group[nid]))
    return Alg_group


def compute_vote_ratios(
    Alg_group: dict[str, list[str]],
    Non_alg_group: list[str],
    config: dict | None = None,
    node_idx: dict[str, dict] | None = None,
) -> dict[str, float]:
    """Compute vote ratio for each concrete algorithm candidate node.

    vote_ratio_k = num_node_k / Num_node_alg
    where Num_node_alg is computed differentiated by algorithm class node_type (v8.x modification 4):
      Num_node_alg = (1-14 nodes count) + (-Induction nodes count with same code as algorithm class)
    Historical version (before v7): Num_node = max(1, len(Non_alg_group) - N_induction),
    but because of the 01-default edge connecting-by-code rule, unmatched code Induction nodes
    should not inflate the denominator.

    Optimization note (performance):
      - Multiple algorithms of same alg_node_type share the same denominator, avoiding each
        algorithm traversing Non_alg_group to compute denominator repeatedly (O(M*K) -> O(M+K)).
      - When node_idx is not passed, fall back to original behavior (backward compatible).
    """
    vote_ratios: dict[str, float] = {}

    if not Non_alg_group:
        return vote_ratios

    if node_idx is None:
        # Fallback path: denominator by old logic total length (backward compatible)
        Num_node = max(1, len(Non_alg_group))
        alg_counts: dict[str, int] = {}
        for nid, alg_list in Alg_group.items():
            for alg_id in alg_list:
                alg_counts[alg_id] = alg_counts.get(alg_id, 0) + 1
        for alg_id, count in alg_counts.items():
            vote_ratios[alg_id] = min(count / Num_node, 1.0)
        return vote_ratios

    # Compute denominator separately for each algorithm class node_type
    alg_counts: dict[str, int] = {}
    alg_node_types: dict[str, str] = {}
    for nid, alg_list in Alg_group.items():
        for alg_id in alg_list:
            alg_counts[alg_id] = alg_counts.get(alg_id, 0) + 1
            if alg_id not in alg_node_types:
                alg_node = node_idx.get(alg_id, {})
                alg_node_types[alg_id] = alg_node.get("node_type", "")

    # Optimization: group by alg_node_type, same type shares same denominator
    denom_cache: dict[str, int] = {}
    for alg_id, count in alg_counts.items():
        alg_node_type = alg_node_types[alg_id]
        if alg_node_type not in denom_cache:
            denom_cache[alg_node_type] = cfg.compute_vote_ratio_denominator(
                alg_node_type, Non_alg_group, node_idx
            )
        Num_node_alg = denom_cache[alg_node_type]
        vote_ratios[alg_id] = min(count / Num_node_alg, 1.0)

    return vote_ratios


def group_algorithms_by_type(
    vote_ratios: dict[str, float],
    graph: dict,
    node_idx: dict[str, dict],
    Top_K: int,
) -> dict[str, list[dict]]:
    """Group candidate algorithms by algorithm type and keep Top-K.

    Sort rules: vote_ratio desc -> node_weight desc -> node_id stable sort.
    """
    by_type: dict[str, list[dict]] = {}
    for alg_id, vote_ratio in vote_ratios.items():
        node = node_idx.get(alg_id)
        if node is None:
            continue
        node_type = node.get("node_type", "")
        alg_type_name = node_type

        if alg_type_name not in by_type:
            by_type[alg_type_name] = []
        by_type[alg_type_name].append({
            "node_id": alg_id,
            "node_name": node.get("node_name", ""),
            "vote_ratio": vote_ratio,
            "node_weight": _get_node_weight(node),
        })

    for alg_type, candidates in by_type.items():
        candidates.sort(
            key=lambda x: (-x["vote_ratio"], -x["node_weight"], x["node_id"])
        )
        by_type[alg_type] = candidates[:Top_K]

    return by_type


def _get_node_weight(node: dict) -> float:
    """Extract node_weight from node object (range 0-1)."""
    nw = node.get("node_weight", {})
    if isinstance(nw, dict):
        return nw.get("node_weight", 0.0)
    if isinstance(nw, (int, float)):
        return float(nw)
    return 0.0


def compute_fact_sufficiency_v7(
    Non_alg_group: list[str],
    graph: dict,
    node_idx: dict[str, dict],
    config: dict,
) -> tuple[float, dict]:
    """v7: Compute fact sufficiency coefficient A (19-point system).

    Each node_type counts only 1 point, max 19 points.
    A = x_N^2 / (x^2 + (1 - x)^2)
    x_N = min(coverage / 19, 1), coverage = number of distinct node_types
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

    # type_score_v7: each type counts only 1 point (used for logging)
    type_score = {t: 1.0 for t in covered_types}

    return fact_sufficiency, type_score


def compute_fact_sufficiency_v6(
    Non_alg_group: list[str],
    graph: dict,
    node_idx: dict[str, dict],
    config: dict,
) -> tuple[float, dict]:
    """v6 compatible: Compute fact sufficiency coefficient (each type max 3 points, total max 30)."""
    N_non_alg_type_count_max = config.get("N_non_alg_type_count_max", 19)
    type_score: dict[str, float] = {}

    for nid in Non_alg_group:
        node = node_idx.get(nid)
        if node is None:
            continue
        node_type = node.get("node_type", "")
        if node_type not in type_score:
            type_score[node_type] = 0.0
        type_score[node_type] = min(type_score[node_type] + 1.0, 3.0)

    coverage = sum(type_score.values())
    eps = config.get("epsilon", 1e-9)

    x_N = min(coverage / N_non_alg_type_count_max, 1.0)
    numerator = x_N * x_N
    denominator = x_N * x_N + (1 - x_N) * (1 - x_N) + eps
    A = numerator / denominator
    return A, type_score


def compute_vote_entropy(vote_ratios_list: list[float], config: dict) -> float:
    """Compute normalized vote entropy E_i for an algorithm type."""
    K_i = len(vote_ratios_list)
    if K_i <= 1:
        return 0.0

    total = sum(vote_ratios_list)
    if total == 0:
        return 1.0

    p = [vr / total for vr in vote_ratios_list]
    h = 0.0
    for pi in p:
        if pi > 0:
            h -= pi * math.log(pi)
    E_i = h / math.log(K_i)
    return E_i


def compute_category_belief(E_i: float, config: dict) -> float:
    """Compute category vote belief B_i."""
    theta_E = config.get("vote_entropy_threshold", 0.90)
    eps = config.get("epsilon", 1e-9)
    B_i = min(1.0, (1 - E_i) / (1 - theta_E + eps))
    return B_i


def compute_type_belief(A: float, R_i_max: float) -> float:
    """Compute category recommendation belief V_i. V_i = A * R_i_max"""
    return A * R_i_max


def aggregate_vote_for_epoch(
    state: Any,
    epoch_key: str,
    graph: dict,
    config: dict,
    edge_idx: dict[str, dict],
    node_idx: dict[str, dict],
) -> dict:
    """Execute complete aggregation flow for current Epoch (v7, fact sufficiency uses 19-point system).

    Returns:
        vote_result: contains Thinking_belief, fact_sufficiency_A, by_algorithm_type
    """
    eps = config.get("epsilon", 1e-9)
    Top_K = config.get("Top_K", 3)

    # Step 1: Collect non-algorithm nodes
    Non_alg_group = collect_non_algorithm_nodes(state, graph, node_idx=node_idx)

    # Step 2: Collect algorithm candidates
    Alg_group = collect_algorithm_candidates(state, Non_alg_group, graph, edge_idx, node_idx=node_idx)

    # Step 3: Compute vote ratios
    vote_ratios = compute_vote_ratios(Alg_group, Non_alg_group, config, node_idx)

    # Step 4: Group by type and keep Top-K
    by_algorithm_type_full = group_algorithms_by_type(
        vote_ratios, graph, node_idx, Top_K
    )

    # Step 5: Compute fact sufficiency (v7 19-point system)
    A, type_score = compute_fact_sufficiency_v7(Non_alg_group, graph, node_idx, config)

    # Step 6: Compute R_i_max, V_i for each algorithm class
    algorithm_type_metrics: dict[str, dict] = {}
    by_algorithm_type: dict[str, dict] = {}

    for alg_type, candidates in by_algorithm_type_full.items():
        if not candidates:
            continue

        vote_ratios_list = [c["vote_ratio"] for c in candidates]
        R_i_max = max(vote_ratios_list) if vote_ratios_list else 0.0
        E_i = compute_vote_entropy(vote_ratios_list, config)
        B_i = compute_category_belief(E_i, config)
        V_i = compute_type_belief(A, R_i_max)

        algorithm_type_metrics[alg_type] = {
            "E_i": round(E_i, 6),
            "B_i": round(B_i, 6),
            "R_i_max": round(R_i_max, 6),
            "V_i": round(V_i, 6),
        }

        Top_K_detail = []
        for c in candidates:
            supporting_ids = []
            for nid, algs in Alg_group.items():
                if c["node_id"] in algs:
                    supporting_ids.append(nid)
            Top_K_detail.append({
                "node_id": c["node_id"],
                "node_name": c["node_name"],
                "vote_ratio": round(c["vote_ratio"], 6),
                "supporting_non_alg_node_ids": supporting_ids,
            })

        by_algorithm_type[alg_type] = {
            "R_i_max": round(R_i_max, 6),
            "V_i": round(V_i, 6),
            "Top_K": Top_K_detail,
        }

    # Step 7: Compute overall recommendation belief Thinking_belief
    all_V = [metrics["V_i"] for metrics in algorithm_type_metrics.values()]
    if len(all_V) == 0:
        Thinking_belief = 0.0
    elif len(all_V) <= 3:
        Thinking_belief = sum(all_V) / len(all_V)
    else:
        all_V_sorted = sorted(all_V, reverse=True)
        Thinking_belief = sum(all_V_sorted[:3]) / 3

    # Write to N_vote
    vote_result = {
        "Thinking_belief": round(Thinking_belief, 6),
        "fact_sufficiency_A": round(A, 6),
        "fact_sufficiency_type_score": type_score,
        "by_algorithm_type": by_algorithm_type,
    }
    state.N_vote[epoch_key] = vote_result

    # Write to vote_log
    vote_log = {
        "step": "vote",
        "epoch_key": epoch_key,
        "Non_alg_group": Non_alg_group,
        "Alg_group": Alg_group,
        "vote_ratios": {k: round(v, 6) for k, v in vote_ratios.items()},
        "by_algorithm_type_full": by_algorithm_type_full,
        "algorithm_type_metrics": algorithm_type_metrics,
        "by_algorithm_type": by_algorithm_type,
        "Thinking_belief": round(Thinking_belief, 6),
        "fact_sufficiency_A": round(A, 6),
        "fact_sufficiency_type_score": type_score,
        "warnings": [],
    }

    if epoch_key not in state.N_log["epoch_logs"]:
        state.N_log["epoch_logs"][epoch_key] = {}
    state.N_log["epoch_logs"][epoch_key]["vote_log"] = vote_log

    return vote_result


def build_current_recommend_vote_list(
    by_algorithm_type: dict[str, dict],
    node_idx: dict[str, dict],
) -> dict[str, str]:
    """Build recommendation vote ratio list string from by_algorithm_type.

    Used to fill the current_recommend_vote_list field in N_pruning array.
    Return format like:
    {
        "15-DataPreprocessingAlgorithm": "<node_id> + <node_name> + <vote_ratio>",
        ...
    }
    """
    result = {}
    for alg_type, candidates_data in by_algorithm_type.items():
        top_k = candidates_data.get("Top_K", [])
        if not top_k:
            result[alg_type] = "null + null + 0.0"
            continue
        # Take max vote ratio
        best = max(top_k, key=lambda x: x["vote_ratio"])
        result[alg_type] = (
            f"{best['node_id']} + {best['node_name']} + {best['vote_ratio']:.4f}"
        )
    return result


def vote_from_explore_result(
    explore_result: dict[str, dict],
    graph: dict,
    edge_idx: dict[str, dict],
    node_idx: dict[str, dict],
    config: dict,
    source_node_ids: list[str],
) -> dict:
    """Execute aggregation calculation on exploration result from concurrent pruning phase (does not modify state).

    Used for the concurrent aggregation step in the "pruning-exploration-aggregation concurrent loop".

    Parameters:
        explore_result: return value of explore_for_node_ids
        graph: standardized graph
        edge_idx / node_idx: index dicts
        config: configuration object
        source_node_ids: source node ID list that executed exploration (i.e., "temporary update existing non-algorithm node set")

    Returns:
        vote_result: same return value structure as aggregate_vote_for_epoch
    """
    eps = config.get("epsilon", 1e-9)
    Top_K = config.get("Top_K", 3)

    # source_node_ids as Non_alg_group
    Non_alg_group = list(source_node_ids)

    # Collect algorithm candidates (from explore_result)
    Alg_group = collect_algorithm_candidates_from_explore_result(
        explore_result, graph, edge_idx, node_idx
    )

    # Compute vote ratios
    vote_ratios = compute_vote_ratios(Alg_group, Non_alg_group, config, node_idx)

    # Group by type
    by_algorithm_type_full = group_algorithms_by_type(
        vote_ratios, graph, node_idx, Top_K
    )

    # Compute fact sufficiency (v7 19-point system)
    A, type_score = compute_fact_sufficiency_v7(Non_alg_group, graph, node_idx, config)

    # Compute metrics for each category
    algorithm_type_metrics: dict[str, dict] = {}
    by_algorithm_type: dict[str, dict] = {}

    for alg_type, candidates in by_algorithm_type_full.items():
        if not candidates:
            continue

        vote_ratios_list = [c["vote_ratio"] for c in candidates]
        R_i_max = max(vote_ratios_list) if vote_ratios_list else 0.0
        E_i = compute_vote_entropy(vote_ratios_list, config)
        B_i = compute_category_belief(E_i, config)
        V_i = compute_type_belief(A, R_i_max)

        algorithm_type_metrics[alg_type] = {
            "E_i": round(E_i, 6),
            "B_i": round(B_i, 6),
            "R_i_max": round(R_i_max, 6),
            "V_i": round(V_i, 6),
        }

        Top_K_detail = []
        for c in candidates:
            supporting_ids = []
            for nid, algs in Alg_group.items():
                if c["node_id"] in algs:
                    supporting_ids.append(nid)
            Top_K_detail.append({
                "node_id": c["node_id"],
                "node_name": c["node_name"],
                "vote_ratio": round(c["vote_ratio"], 6),
                "supporting_non_alg_node_ids": supporting_ids,
            })

        by_algorithm_type[alg_type] = {
            "R_i_max": round(R_i_max, 6),
            "V_i": round(V_i, 6),
            "Top_K": Top_K_detail,
        }

    all_V = [metrics["V_i"] for metrics in algorithm_type_metrics.values()]
    if len(all_V) == 0:
        Thinking_belief = 0.0
    elif len(all_V) <= 3:
        Thinking_belief = sum(all_V) / len(all_V)
    else:
        all_V_sorted = sorted(all_V, reverse=True)
        Thinking_belief = sum(all_V_sorted[:3]) / 3

    vote_result = {
        "Thinking_belief": round(Thinking_belief, 6),
        "fact_sufficiency_A": round(A, 6),
        "fact_sufficiency_type_score": type_score,
        "by_algorithm_type": by_algorithm_type,
        "Alg_group": Alg_group,
        "vote_ratios": vote_ratios,
    }

    return vote_result
