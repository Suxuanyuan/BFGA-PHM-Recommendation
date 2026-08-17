# -*- coding: utf-8 -*-
r"""
v7_modules/01_schemas.py
==========================
v7 data structure definitions and ReasoningState state container.

Main differences from v6:
  - N_pruning changed from dict to list (array structure), each entry corresponds to complete
    pruning information for one Epoch
  - N_pruning array elements contain: Epoch, current_node_ids, current_recommend_vote_list,
    fact_sufficiency_A, pruning_strategy, pruning_time, pruning_status,
    best_pruning_node_ids, best_pruning_recommend_vote_list, next_node_ids,
    feedback_details (contains feedback_time, W_dynamic_n, Wsum_pruning_node_ids, etc.)
"""

from dataclasses import dataclass, field, asdict
from typing import Any


@dataclass
class ReasoningState:
    """v7 complete reasoning state container."""
    Background_string: str = ""
    Background_json: list = field(default_factory=list)
    N_Explore: dict = field(default_factory=dict)
    N_vote: dict = field(default_factory=dict)
    # v7: N_pruning changed to list, each entry corresponds to one Epoch
    N_pruning: list = field(default_factory=list)
    N_recommend: dict = field(default_factory=dict)
    N_log: dict = field(default_factory=lambda: {
        "meta": {},
        "background_parse_log": [],
        "node_match_log": [],
        "epoch_logs": {},
        "termination_log": {},
        "recommendation_log": {},
        "errors": [],
        "pruning_feedback_logs": {},  # v7 new: records feedback details per round
    })

    def to_dict(self) -> dict:
        return asdict(self)


def new_reasoning_state() -> ReasoningState:
    """Return an empty ReasoningState instance."""
    return ReasoningState()


def new_epoch_explore_node(node_id: str, matched_from: str = "") -> dict:
    """Return initialization structure for a single node in N_Explore."""
    node = {
        "candidate_edge_ids": [],
        "source": "background_match" if matched_from else "pruning_from",
    }
    if matched_from:
        node["matched_from"] = matched_from
    return node


def new_n_pruning_entry(
    epoch_key: str,
    current_node_ids: list,
    current_recommend_vote_list: dict,
    fact_sufficiency_A: float,
    pruning_strategy: str,
    pruning_time: int,
    pruning_status: str,
    best_pruning_node_ids: list | None,
    best_pruning_recommend_vote_list: dict,
    next_node_ids: list,
    feedback_details: list,
) -> dict:
    """Build a new N_pruning array element.

    Corresponds to the structure in the md document "N_pruning Array".
    """
    return {
        "Epoch": epoch_key,
        "current_node_ids": current_node_ids,
        "current_recommend_vote_list": current_recommend_vote_list,
        "fact_sufficiency_A": fact_sufficiency_A,
        "pruning_strategy": pruning_strategy,
        "pruning_time": pruning_time,
        "pruning_status": pruning_status,
        "best_pruning_node_ids": best_pruning_node_ids,
        "best_pruning_recommend_vote_list": best_pruning_recommend_vote_list,
        "next_node_ids": next_node_ids,
        "feedback_details": feedback_details,
    }


def new_feedback_detail(
    feedback_time: int,
    W_dynamic_n: int,
    Wsum_pruning_node_ids: dict,
    Wsum_num_increasing_max_vote: dict,
) -> dict:
    """Build a new feedback detail entry.

    Records W-sum group information for the f-th backtracking round.
    """
    return {
        "feedback_time": feedback_time,
        "W_dynamic_n": W_dynamic_n,
        "Wsum_pruning_node_ids": Wsum_pruning_node_ids,
        "Wsum_num_increasing_max_vote": Wsum_num_increasing_max_vote,
    }
