# -*- coding: utf-8 -*-
r"""
v7_modules/06_explore.py
=========================
Exploration module.

v7 inherits v6's basic exploration logic, adds:
  - Function to execute exploration on given node set (used for concurrent pruning phase)
  - Utility function to collect candidate edges and candidate nodes

In v7 the exploration phase itself doesn't change (same flow as v6), the new exploration function
is used for the concurrent exploration step in the "pruning-exploration-aggregation concurrent loop".
"""

from typing import Any

from . import m00_config as cfg


def get_incident_edges(
    node_id: str,
    graph: dict,
    adjacency: dict | None = None,
) -> list[dict]:
    """Find all incoming and outgoing edges of a node, merge as candidate edge set.

    Optimization note (performance):
      - Caller can pre-build adjacency (m02_graph_io.build_adjacency) and pass to adjacency,
        avoiding O(E) full graph scan each time;
      - When adjacency is not provided, fall back to original behavior (fully backward compatible).
      - Measured at N=8424, E=115784: full graph scan ~12.35ms/time,
        adjacency query ~0.0001ms/time, approximately 140,000x speedup.
    """
    if adjacency is not None:
        info = adjacency.get(node_id)
        if info is None:
            return []
        in_edges = info.get("in_edges", [])
        out_edges = info.get("out_edges", [])
        return list(in_edges) + list(out_edges)

    candidates = []
    for edge in graph["edges"]:
        src = edge.get("source_node_id", "")
        tgt = edge.get("target_node_id", "")
        if src == node_id or tgt == node_id:
            candidates.append(edge)
    return candidates


def explore_edges_for_node(
    node_id: str,
    graph: dict,
    node_info: dict,
    adjacency: dict | None = None,
) -> dict:
    """Complete exploration of a single node, generate candidate edge records for the node in current Epoch.

    adjacency: optional adjacency list (performance optimization); falls back to O(E) full graph scan
    when not provided.
    """
    all_edges = get_incident_edges(node_id, graph, adjacency=adjacency)

    out_edges = [e for e in all_edges if e.get("source_node_id", "") == node_id]
    in_edges = [e for e in all_edges if e.get("target_node_id", "") == node_id]

    candidate_edges_detail = []
    for e in all_edges:
        direction = "out" if e.get("source_node_id", "") == node_id else "in"
        edge_weight = 0.0
        ew = e.get("edge_weight", {})
        if isinstance(ew, dict):
            edge_weight = ew.get("edge_weight", 0.0)
        elif isinstance(ew, (int, float)):
            edge_weight = ew

        candidate_edges_detail.append({
            "edge_id": e.get("edge_id", ""),
            "graph_source_node_id": e.get("source_node_id", ""),
            "graph_target_node_id": e.get("target_node_id", ""),
            "direction": direction,
            "edge_weight": edge_weight,
        })

    return {
        "candidate_edge_ids": [e.get("edge_id", "") for e in all_edges],
        "out_edge_count": len(out_edges),
        "in_edge_count": len(in_edges),
        "candidate_edges_detail": candidate_edges_detail,
    }


def explore_edges_for_epoch(
    state: Any,
    epoch_key: str,
    graph: dict,
    adjacency: dict | None = None,
) -> None:
    """Execute exploration for all nodes in current Epoch, write results to state.

    adjacency: optional adjacency list (performance optimization); falls back to O(E) full graph scan
    when not provided.
    """
    if epoch_key not in state.N_Explore:
        return

    explore_log_entries = []

    for node_id, node_info in state.N_Explore[epoch_key].items():
        result = explore_edges_for_node(node_id, graph, node_info, adjacency=adjacency)

        state.N_Explore[epoch_key][node_id]["candidate_edge_ids"] = result["candidate_edge_ids"]

        for detail in result["candidate_edges_detail"]:
            explore_log_entries.append({
                "step": "explore",
                "epoch_key": epoch_key,
                "current_node_id": node_id,
                "out_edge_count": result["out_edge_count"],
                "in_edge_count": result["in_edge_count"],
                "candidate_edge_ids": result["candidate_edge_ids"],
                "candidate_edges_detail": [detail],
                "warnings": [],
                "storage_target": f"N_log.epoch_logs.{epoch_key}.explore_log",
            })

    combined = {}
    for entry in explore_log_entries:
        nid = entry["current_node_id"]
        if nid not in combined:
            combined[nid] = {
                "step": "explore",
                "epoch_key": epoch_key,
                "current_node_id": nid,
                "out_edge_count": entry["out_edge_count"],
                "in_edge_count": entry["in_edge_count"],
                "candidate_edge_ids": entry["candidate_edge_ids"],
                "candidate_edges_detail": [],
                "warnings": [],
                "storage_target": f"N_log.epoch_logs.{epoch_key}.explore_log",
            }
        combined[nid]["candidate_edges_detail"].append(entry["candidate_edges_detail"][0])

    if epoch_key not in state.N_log["epoch_logs"]:
        state.N_log["epoch_logs"][epoch_key] = {}
    state.N_log["epoch_logs"][epoch_key]["explore_log"] = list(combined.values())


# ============================================================
# v7 new: exploration functions for concurrent pruning phase
# ============================================================

def explore_for_node_ids(
    node_ids: list[str],
    graph: dict,
    edge_idx: dict[str, dict],
    node_idx: dict[str, dict],
    adjacency: dict | None = None,
) -> dict[str, dict]:
    """Execute exploration for the specified node list, return each node's candidate edge and candidate node info.

    This is the core function for the concurrent exploration step in v7's
    "pruning-exploration-aggregation concurrent loop".
    Does not modify state, only returns exploration result dict.

    Parameters:
        node_ids: list of node IDs to explore (e.g., temporary node set of some W-sum group)
        graph: standardized graph
        edge_idx: edge_id -> edge dict
        node_idx: node_id -> node dict
        adjacency: optional adjacency list (performance optimization); falls back to O(E) full graph scan
        when not provided.

    Returns:
        explore_result: {
            "node_id": {
                "candidate_edge_ids": [...],
                "candidate_next_node_ids": [...],  # next-hop nodes reachable via edges
                "candidate_edges_detail": [...],
            }
        }
    """
    results = {}

    for node_id in node_ids:
        all_edges = get_incident_edges(node_id, graph, adjacency=adjacency)
        out_edges = [e for e in all_edges if e.get("source_node_id", "") == node_id]
        in_edges = [e for e in all_edges if e.get("target_node_id", "") == node_id]

        candidate_edges_detail = []
        candidate_next_node_ids = []

        for e in all_edges:
            direction = "out" if e.get("source_node_id", "") == node_id else "in"
            edge_weight = 0.0
            ew = e.get("edge_weight", {})
            if isinstance(ew, dict):
                edge_weight = ew.get("edge_weight", 0.0)
            elif isinstance(ew, (int, float)):
                edge_weight = ew

            if direction == "out":
                next_id = e.get("target_node_id", "")
            else:
                next_id = e.get("source_node_id", "")

            if next_id and next_id not in candidate_next_node_ids:
                candidate_next_node_ids.append(next_id)

            candidate_edges_detail.append({
                "edge_id": e.get("edge_id", ""),
                "graph_source_node_id": e.get("source_node_id", ""),
                "graph_target_node_id": e.get("target_node_id", ""),
                "direction": direction,
                "edge_weight": edge_weight,
                "next_node_id": next_id,
                "edge_group": e.get("edge_group", ""),
            })

        results[node_id] = {
            "candidate_edge_ids": [e.get("edge_id", "") for e in all_edges],
            "out_edge_count": len(out_edges),
            "in_edge_count": len(in_edges),
            "candidate_next_node_ids": candidate_next_node_ids,
            "candidate_edges_detail": candidate_edges_detail,
        }

    return results


def collect_candidate_edges_and_nodes_from_explore_result(
    explore_result: dict[str, dict],
    edge_idx: dict[str, dict],
    node_idx: dict[str, dict],
) -> tuple[list[dict], list[str]]:
    """Collect candidate edge details and candidate node ID list from exploration result.

    Used after the concurrent exploration step of the "pruning-exploration-aggregation
    concurrent loop", to collect explored edges and nodes for subsequent filtering and aggregation.

    Parameters:
        explore_result: return value of explore_for_node_ids
        edge_idx: edge_id -> edge dict
        node_idx: node_id -> node dict

    Returns:
        (candidate_edges, candidate_node_ids)
    """
    candidate_edges = []
    candidate_node_ids = []

    seen_edge_ids = set()
    seen_node_ids = set()

    for node_id, info in explore_result.items():
        # Collect edges
        for edge_id in info.get("candidate_edge_ids", []):
            if edge_id not in seen_edge_ids:
                edge = edge_idx.get(edge_id)
                if edge:
                    candidate_edges.append(edge)
                    seen_edge_ids.add(edge_id)

        # Collect nodes (nodes connected via edges)
        for detail in info.get("candidate_edges_detail", []):
            next_id = detail.get("next_node_id", "")
            if next_id and next_id not in seen_node_ids:
                candidate_node_ids.append(next_id)
                seen_node_ids.add(next_id)

    return candidate_edges, candidate_node_ids
