# -*- coding: utf-8 -*-
r"""
v7_modules/05_node_matcher.py
==============================
Node matching module. Directly copied from v6 (uses v7 llm_client).
"""

import difflib
import json
from typing import Any

from . import m00_config as config
from . import m03_llm_client as llm


def compute_node_similarity(b_name: str, node_name: str) -> float:
    if not b_name or not node_name:
        return 0.0
    return difflib.SequenceMatcher(None, b_name, node_name).ratio()


def program_match_node(
    constraint: dict,
    graph: dict,
    config: dict,
    node_idx: dict[str, dict],
    candidates_by_type: dict[str, list[dict]] | None = None,
) -> dict:
    b_type = constraint.get("node_type", "")
    b_name = constraint.get("node_name", "")
    constraint_id = constraint.get("constraint_id", "")
    warnings = []

    if candidates_by_type is not None:
        candidates = candidates_by_type.get(b_type, [])
    else:
        candidates = [n for n in graph["nodes"] if n.get("node_type", "") == b_type]

    if not candidates:
        return {
            "constraint_id": constraint_id,
            "matched_node_id": None,
            "matched_node_name": None,
            "match_method": "none",
            "similarity": 0.0,
            "match_status": "need_llm_fallback_no_same_node_type",
            "llm_reason": None,
            "warnings": ["No node with same node_type in graph"],
        }

    similarities = []
    for n in candidates:
        n_name = n.get("node_name", "")
        sim = compute_node_similarity(b_name, n_name)
        similarities.append((n, sim))

    best_node, max_sim = max(similarities, key=lambda x: x[1])

    if max_sim >= config.get("string_similarity_threshold", 0.80):
        return {
            "constraint_id": constraint_id,
            "matched_node_id": best_node["node_id"],
            "matched_node_name": best_node.get("node_name", ""),
            "match_method": "program_matched",
            "similarity": round(max_sim, 4),
            "match_status": "program_matched",
            "llm_reason": None,
            "warnings": [],
        }
    else:
        return {
            "constraint_id": constraint_id,
            "matched_node_id": None,
            "matched_node_name": None,
            "match_method": "llm_fallback",
            "similarity": round(max_sim, 4),
            "match_status": "need_llm_fallback_same_node_type",
            "llm_reason": None,
            "warnings": [f"Max similarity {max_sim:.4f} < threshold"],
        }


def llm_fallback_match_node(
    constraint: dict,
    candidate_nodes: list[dict],
) -> dict:
    if not candidate_nodes:
        return {
            "constraint_id": constraint.get("constraint_id", ""),
            "matched_node_id": None,
            "matched_node_name": None,
            "match_method": "none",
            "similarity": 0.0,
            "match_status": "no_candidate",
            "llm_reason": "No candidate nodes available",
            "warnings": [],
        }

    candidates_summary = []
    for i, n in enumerate(candidate_nodes[:10]):
        candidates_summary.append({
            "index": i,
            "node_id": n.get("node_id", ""),
            "node_name": n.get("node_name", ""),
            "node_type": n.get("node_type", ""),
            "node_description": n.get("node_description", "")[:200],
        })

    system_prompt = (
        "You are a graph node matching assistant. The user has a background constraint and needs to "
        "select the best matching one from candidate nodes.\n"
        "Your task is to select the most matching node from the candidate list based on the background "
        "constraint's node_type and node_name.\n"
        "If no candidate nodes look relevant, please return index=-1 to indicate no match.\n"
        "Output only JSON: {\"index\": <number>, \"reason\": \"<brief reason>\"}, no other text."
    )

    user_prompt = (
        f"Background constraint:\n"
        f"  node_type: {constraint.get('node_type', '')}\n"
        f"  node_name: {constraint.get('node_name', '')}\n"
        f"  raw_text: {constraint.get('raw_text', '')}\n\n"
        f"Candidate node list (max 10 displayed):\n"
        f"{json.dumps(candidates_summary, ensure_ascii=False, indent=2)}\n\n"
        f"Please select the most matching node index. If no relevant node is found, return index=-1."
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    try:
        raw_reply = llm.chat_llm(messages)
        parsed = llm.parse_json_response(raw_reply)
        idx = parsed.get("index", -1)
        reason = parsed.get("reason", "")
        if idx >= 0 and idx < len(candidate_nodes):
            chosen = candidate_nodes[idx]
            return {
                "constraint_id": constraint.get("constraint_id", ""),
                "matched_node_id": chosen.get("node_id"),
                "matched_node_name": chosen.get("node_name"),
                "match_method": "llm_fallback",
                "similarity": 1.0,
                "match_status": "llm_matched",
                "llm_reason": reason,
                "warnings": [],
            }
        else:
            return {
                "constraint_id": constraint.get("constraint_id", ""),
                "matched_node_id": None,
                "matched_node_name": None,
                "match_method": "llm_fallback",
                "similarity": 0.0,
                "match_status": "llm_rejected_all",
                "llm_reason": reason,
                "warnings": ["LLM rejected all candidates"],
            }
    except Exception as e:
        return {
            "constraint_id": constraint.get("constraint_id", ""),
            "matched_node_id": None,
            "matched_node_name": None,
            "match_method": "llm_fallback",
            "similarity": 0.0,
            "match_status": "llm_error",
            "llm_reason": str(e),
            "warnings": [f"LLM fallback error: {e}"],
        }


def match_background_nodes(
    Background_json: list[dict],
    graph: dict,
    config: dict,
    node_idx: dict[str, dict],
    candidates_by_type: dict[str, list[dict]] | None = None,
) -> list[dict]:
    results = []
    for constraint in Background_json:
        result = program_match_node(constraint, graph, config, node_idx, candidates_by_type=candidates_by_type)

        if result["match_status"] in (
            "need_llm_fallback_same_node_type",
            "need_llm_fallback_no_same_node_type",
        ):
            b_type = constraint.get("node_type", "")
            if candidates_by_type is not None:
                candidates = candidates_by_type.get(b_type, [])
            else:
                candidates = [n for n in graph["nodes"] if n.get("node_type", "") == b_type]
            fallback_result = llm_fallback_match_node(constraint, candidates)
            if fallback_result["matched_node_id"] is not None:
                result.update(fallback_result)

        results.append(result)

    return results
