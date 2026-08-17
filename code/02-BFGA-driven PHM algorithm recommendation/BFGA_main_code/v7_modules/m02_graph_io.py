# -*- coding: utf-8 -*-
r"""
v7_modules/02_graph_io.py
==========================
Graph loading and normalization. Directly copied from v6_modules.m02_graph_io.
"""

import json
from typing import Any
from pathlib import Path


def load_graph(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def normalize_graph(raw_graph: dict) -> dict:
    nodes_out = []
    edges_out = []

    # Compatible with A2 node merge output list format (each element is a case's nodes/edges)
    if isinstance(raw_graph, list):
        for case_obj in raw_graph:
            if isinstance(case_obj, dict):
                nodes_out.extend(case_obj.get("nodes", []))
                edges_out.extend(case_obj.get("edges", []))
        return {
            "nodes": nodes_out,
            "edges": edges_out,
            "meta": {},
        }

    if "nodes" in raw_graph and isinstance(raw_graph["nodes"], list):
        nodes_out = raw_graph["nodes"]
    if "edges" in raw_graph and isinstance(raw_graph["edges"], list):
        edges_out = raw_graph["edges"]

    if "papers" in raw_graph and isinstance(raw_graph["papers"], list):
        for paper in raw_graph["papers"]:
            if "nodes" in paper and isinstance(paper["nodes"], list):
                nodes_out.extend(paper["nodes"])
            if "edges" in paper and isinstance(paper["edges"], list):
                edges_out.extend(paper["edges"])

    return {
        "nodes": nodes_out,
        "edges": edges_out,
        "meta": raw_graph.get("meta", {}),
    }


def build_node_index(graph: dict) -> dict[str, dict]:
    return {node["node_id"]: node for node in graph["nodes"]}


def build_edge_index(graph: dict) -> dict[str, dict]:
    return {edge["edge_id"]: edge for edge in graph["edges"]}


def build_adjacency(graph: dict) -> dict[str, dict]:
    adjacency = {}
    for edge in graph["edges"]:
        src = edge["source_node_id"]
        tgt = edge["target_node_id"]
        if src not in adjacency:
            adjacency[src] = {"out_edges": [], "in_edges": []}
        if tgt not in adjacency:
            adjacency[tgt] = {"out_edges": [], "in_edges": []}
        adjacency[src]["out_edges"].append(edge)
        adjacency[tgt]["in_edges"].append(edge)
    return adjacency
