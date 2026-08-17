# -*- coding: utf-8 -*-
r"""
v7_modules/09_recommend.py
==========================
Recommendation output module. Directly copied from v6 (uses v7's m00_config).
"""

import math
from typing import Any

from . import m00_config as cfg


def get_latest_vote_result(state: Any) -> tuple[str, dict]:
    """Find the latest Epoch's vote result from N_vote."""
    if not state.N_vote:
        return "", {}
    latest_key = max(state.N_vote.keys(), key=lambda k: int(k.replace("Epoch", "")))
    return latest_key, state.N_vote[latest_key]


def filter_valid_algorithm_types(
    vote_result: dict,
    config: dict,
) -> dict:
    """Filter algorithm types to recommend based on low-support significance coefficient."""
    eps = config.get("epsilon", 1e-9)
    z_threshold = config.get("node_type_low_support_z_threshold", 3.00)

    by_type = vote_result.get("by_algorithm_type", {})
    if not by_type:
        return {"valid": {}, "filtered": {}}

    V_support: dict[str, float] = {}
    for alg_type, data in by_type.items():
        top_k = data.get("Top_K", [])
        if not top_k:
            V_support[alg_type] = 0.0
        else:
            ratios = [c["vote_ratio"] for c in top_k]
            V_support[alg_type] = sum(ratios) / len(ratios)

    valid: dict[str, dict] = {}
    filtered: dict[str, dict] = {}

    for alg_type, v_support in V_support.items():
        others = {k: v for k, v in V_support.items() if k != alg_type}
        if len(others) < 1:
            valid[alg_type] = by_type[alg_type]
            continue

        mu = sum(others.values()) / len(others)
        variance = sum((v - mu) ** 2 for v in others.values()) / len(others)
        sigma = math.sqrt(variance + eps)

        L_i = (mu - v_support) / sigma
        entry = {
            "V_support_i": round(v_support, 6),
            "L_i": round(L_i, 6),
            "mu_-i": round(mu, 6),
            "sigma_-i": round(sigma, 6),
            "filtered_reason": "",
        }

        if L_i > z_threshold:
            entry["filtered_reason"] = f"L_i={L_i:.4f} > z_threshold={z_threshold}"
            filtered[alg_type] = entry
        else:
            valid[alg_type] = {**by_type[alg_type], **entry}

    return {"valid": valid, "filtered": filtered}


def select_final_algorithm_per_type(
    valid_candidates: dict,
    graph: dict,
    node_idx: dict[str, dict],
    source_epoch_key: str,
) -> dict:
    """Select the final recommended node for each valid algorithm type."""
    N_recommend: dict = {}

    for alg_type, data in valid_candidates.items():
        top_k = data.get("Top_K", [])
        if not top_k:
            continue

        top_k_sorted = sorted(
            top_k,
            key=lambda x: (-x["vote_ratio"], -x.get("node_weight", 0.0), x["node_id"])
        )
        best = top_k_sorted[0]
        node = node_idx.get(best["node_id"], {})

        why_selected = []
        if len(top_k_sorted) > 1:
            runner = top_k_sorted[1]
            if best["vote_ratio"] == runner["vote_ratio"]:
                why_selected.append(
                    f"Highest vote ratio in {alg_type} (tied with {best['node_name']}/{runner['node_name']}), highest node weight."
                )
            else:
                why_selected.append(f"Highest vote ratio in {alg_type} ({best['vote_ratio']:.4f}).")
        else:
            why_selected.append(f"The only candidate in {alg_type}.")

        N_recommend[alg_type] = {
            "node_id": best["node_id"],
            "node_name": best.get("node_name", ""),
            "vote_ratio": round(best["vote_ratio"], 6),
            "node_weight": best.get("node_weight", 0.0),
            "supporting_non_alg_node_ids": best.get("supporting_non_alg_node_ids", []),
            "why_selected": why_selected,
            "source_epoch_key": source_epoch_key,
        }

    return N_recommend


def generate_recommendation(
    state: Any,
    graph: dict,
    config: dict,
    node_idx: dict[str, dict],
) -> dict:
    """Execute the complete recommendation output flow."""
    source_epoch_key, vote_result = get_latest_vote_result(state)
    if not vote_result:
        return {}

    enable_node_type_filter = config.get("enable_node_type_filter", True)
    if enable_node_type_filter:
        filter_result = filter_valid_algorithm_types(vote_result, config)
        valid = filter_result["valid"]
        filtered = filter_result["filtered"]
        filter_mode = "enabled"
    else:
        valid = dict(vote_result.get("by_algorithm_type", {}))
        filtered = {}
        filter_mode = "disabled_keep_all_algorithm_types"

    N_recommend = select_final_algorithm_per_type(
        valid, graph, node_idx, source_epoch_key
    )

    state.N_recommend = N_recommend

    recommendation_log = {
        "step": "recommend",
        "source_epoch_key": source_epoch_key,
        "filter_mode": filter_mode,
        "candidate_by_type": vote_result.get("by_algorithm_type", {}),
        "valid_candidates": valid,
        "filtered_algorithm_types": filtered,
        "tie_break_details": {},
        "N_recommend_snapshot": N_recommend,
        "warnings": [],
    }
    state.N_log["recommendation_log"] = recommendation_log

    return N_recommend
