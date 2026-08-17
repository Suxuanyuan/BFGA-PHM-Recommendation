# -*- coding: utf-8 -*-
r"""
Knowledge-graph edges attribute-merge resolution + edge_weight quantification - post-processing program V7
========================================================================
Functions:
  Load the "edge json" and run post-processing:

Processing steps:
  1. Load the "edge json".
  2. Iterate each edge{} and remove the following fields:
       edge_description_list
       edge_cite_score_list
       edge_cite_count_list
       edge_publish_year_list
     to form "edge json v1.0".
  3. Compute edge_weight and assign it to each edge:
       3-1. empirical_e   — empirical importance (evidence_level + edge_description)
       3-2. freq_e         — co-occurrence frequency (per-group percentile_rank of log1p(edge_nums))
       3-3. authority_e    — paper influence (0.3*if_e + 0.7*cite_e, then unified normalization)
       3-4. recency_e      — time trend (exp(-(max_year-year)/tau), tau=5)
       3-5. edge_weight    — combined weighted score
  4. Save the output json (filename gets "_secondary_processing" suffix).

Output path (RELATIVE PATH placeholder):
  ./data/04_final_graph/C2-attribute_merge/
"""

import os
import json
import math
from collections import defaultdict

# ============================================================================
# User configuration
# ============================================================================

INPUT_JSON_PATH = (
    r"./data/04_final_graph/C2-attribute_merge/[2277EAKD][ZZZRPFBV]+merged-edges_disambiguation_induction_edges_merged.json"
)

OUTPUT_DIR = (
    r"./data/04_final_graph"
    r"/C2-attribute_merge"
)

# edge_weight combined weighting parameters (default)
ALPHA = 0.20   # total co-occurrence frequency
BETA  = 0.25   # paper influence
GAMMA = 0.10   # time trend
DELTA = 0.45   # empirical importance

# recency_e time-decay parameter
TAU = 5        # years; the smaller tau is, the more it favors recent papers

# ============================================================================
# Constants
# ============================================================================

FIELDS_TO_REMOVE = [
    "edge_description_list",
    "edge_cite_score_list",
    "edge_cite_count_list",
    "edge_publish_year_list",
]

# ============================================================================
# Helper functions
# ============================================================================

def percentile_rank_avg(values):
    """
    Compute the average-rank tie-aware percentile_rank.

    For cases with many equal values, the average-rank method is used to avoid
    all ranks being 0.

    Formula: percentile = (avg_rank - 1) / (n - 1)
    where avg_rank = (r1 + r2 + ... + rk) / k, and ri is the original position
    in ascending order (starting at 1) of each element within a tied-value group.

    Returns: a percentile score per element, range [0.0, 1.0] (returns 0.5 when n=1).
    """
    n = len(values)
    if n == 0:
        return []
    if n == 1:
        return [0.5]

    # element -> original index list (treat None as 0.0 during sorting)
    val_to_indices = defaultdict(list)
    for idx, v in enumerate(values):
        val_to_indices[v if v is not None else 0.0].append(idx)

    # sort by value ascending; within equal values, sort by original index ascending (stable)
    sorted_items = sorted(val_to_indices.items(), key=lambda x: x[0])

    ranks = [0.0] * n
    current_rank = 1
    for val, indices in sorted_items:
        k = len(indices)
        # average rank: center position of this group in the sorted sequence
        avg_rank = (current_rank + current_rank + k - 1) / 2.0
        percentile = (avg_rank - 1) / (n - 1)
        for idx in indices:
            ranks[idx] = percentile
        current_rank += k

    return ranks


def compute_empirical_e(edge):
    """
    Compute empirical importance empirical_e.
    Rules:
      Low confidence                                                -> 0.10
      Normal confidence                                             -> 0.70
      High confidence + "explicit evidence relation stated"          -> 1.00
      High confidence + "not explicitly stated but inferable"        -> 0.85
    """
    ev = edge.get("evidence_level", "")
    desc = edge.get("edge_description", "") or ""

    if ev == "Low confidence":
        return 0.10
    elif ev == "Normal confidence":
        return 0.70
    elif ev == "High confidence":
        if "明确指出证据关系" in desc:
            return 1.00
        elif "未明确指出但推理可知证据关系" in desc:
            return 0.85
        # High confidence but cannot infer from desc -> default to second-highest
        return 0.85
    else:
        return 0.10


def compute_edge_weights(edges):
    """
    Compute and fill edge_weight back into edges.

    Normalization principle per component:
      freq_e       — normalized within (source_node_type, edge_type, edge_group) group
      authority_e  — normalized within source_node_type group
      recency_e    — normalized across all edges (year needs no grouping)
      empirical_e  — already within [0, 1], no normalization needed
    """
    # -------------------------------------------------------------------------
    # Step 1: empirical_e (no normalization needed)
    # -------------------------------------------------------------------------
    for edge in edges:
        edge["empirical_e"] = compute_empirical_e(edge)

    # -------------------------------------------------------------------------
    # Step 2: freq_e — per (source_node_type, edge_type, edge_group)
    # -------------------------------------------------------------------------
    # collect group data
    freq_groups = defaultdict(list)
    for edge in edges:
        key = (
            edge.get("source_node_type", ""),
            edge.get("edge_type", ""),
            edge.get("edge_group", ""),
        )
        freq_groups[key].append(edge)

    for key, group_edges in freq_groups.items():
        n = len(group_edges)
        log_values = [math.log1p(e.get("edge_nums", 0)) for e in group_edges]
        ranked = percentile_rank_avg(log_values)
        for edge, rank in zip(group_edges, ranked):
            edge["freq_e"] = rank

    # -------------------------------------------------------------------------
    # Step 3: authority_e — per source_node_type
    # -------------------------------------------------------------------------
    # 3-a: if_e per source_node_type
    if_groups = defaultdict(list)
    for edge in edges:
        src_type = edge.get("source_node_type", "")
        if_groups[src_type].append(edge)

    for src_type, group_edges in if_groups.items():
        n = len(group_edges)
        values = [e.get("edge_cite_score", 0.0) for e in group_edges]
        ranked = percentile_rank_avg(values)
        for edge, rank in zip(group_edges, ranked):
            edge["_if_e"] = rank

    # 3-b: cite_e per source_node_type
    cite_groups = defaultdict(list)
    for edge in edges:
        src_type = edge.get("source_node_type", "")
        cite_groups[src_type].append(edge)

    for src_type, group_edges in cite_groups.items():
        n = len(group_edges)
        log_values = [math.log1p(e.get("edge_cite_count", 0.0)) for e in group_edges]
        ranked = percentile_rank_avg(log_values)
        for edge, rank in zip(group_edges, ranked):
            edge["_cite_e"] = rank

    # 3-c: compute authority_e and normalize per source_node_type
    for edge in edges:
        if_e = edge.get("_if_e", 0.0)
        cite_e = edge.get("_cite_e", 0.0)
        edge["authority_e_raw"] = 0.3 * if_e + 0.7 * cite_e

    # normalize authority_e_raw by source_node_type
    auth_groups = defaultdict(list)
    for edge in edges:
        src_type = edge.get("source_node_type", "")
        auth_groups[src_type].append(edge)

    for src_type, group_edges in auth_groups.items():
        n = len(group_edges)
        values = [e.get("authority_e_raw", 0.0) for e in group_edges]
        ranked = percentile_rank_avg(values)
        for edge, rank in zip(group_edges, ranked):
            edge["authority_e"] = rank

    # -------------------------------------------------------------------------
    # Step 4: recency_e — normalized across all edges
    # -------------------------------------------------------------------------
    max_year = max((e.get("edge_publish_year", 2000) for e in edges), default=2026)
    recency_raws = [
        math.exp(-(max_year - e.get("edge_publish_year", max_year)) / TAU)
        for e in edges
    ]

    ranked_recency = percentile_rank_avg(recency_raws)
    for edge, rank in zip(edges, ranked_recency):
        edge["recency_e"] = rank

    # -------------------------------------------------------------------------
    # Step 5: combined edge_weight (with weighted components, 2 decimals)
    # -------------------------------------------------------------------------
    for edge in edges:
        freq_e       = edge.get("freq_e", 0.0)
        authority_e  = edge.get("authority_e", 0.0)
        recency_e    = edge.get("recency_e", 0.0)
        empirical_e  = edge.get("empirical_e", 0.0)

        alpha_freq       = round(ALPHA * freq_e, 2)
        beta_authority   = round(BETA  * authority_e, 2)
        gamma_recency    = round(GAMMA * recency_e, 2)
        delta_empirical  = round(DELTA * empirical_e, 2)
        total_weight     = round(
            ALPHA * freq_e
            + BETA  * authority_e
            + GAMMA * recency_e
            + DELTA * empirical_e,
            2,
        )

        edge["edge_weight"] = {
            "edge_weight":           total_weight,
            "alpha * freq_e":        alpha_freq,
            "beta * authority_e":    beta_authority,
            "gamma * recency_e":     gamma_recency,
            "delta * empirical_e":   delta_empirical,
        }

        # clean up temporary fields (component scores are not exported in edge{})
        for tmp_key in ("_if_e", "_cite_e", "authority_e_raw",
                        "empirical_e", "freq_e", "authority_e", "recency_e"):
            edge.pop(tmp_key, None)

    return edges


def remove_list_fields(edge):
    """Remove list-type fields from edge and return a new edge."""
    return {k: v for k, v in edge.items() if k not in FIELDS_TO_REMOVE}


def main():
    print(f"Reading input file: {INPUT_JSON_PATH}")
    with open(INPUT_JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    input_filename = os.path.basename(INPUT_JSON_PATH)
    name_without_ext = os.path.splitext(input_filename)[0]

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # -------------------------------------------------------------------------
    # Step 1: remove list fields
    # -------------------------------------------------------------------------
    edges = data.get("edges", [])
    print(f"Total {len(edges)} edges; removing list fields...")

    edges_v1 = [remove_list_fields(edge) for edge in edges]

    # -------------------------------------------------------------------------
    # Step 2: compute edge_weight
    # -------------------------------------------------------------------------
    print("Computing edge_weight ...")
    edges_v1 = compute_edge_weights(edges_v1)

    # -------------------------------------------------------------------------
    # Step 3: save
    # -------------------------------------------------------------------------
    data_v1 = dict(data)
    data_v1["edges"] = edges_v1

    json_filename = f"{name_without_ext}_secondary_processing.json"
    json_path = os.path.join(OUTPUT_DIR, json_filename)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data_v1, f, ensure_ascii=False, indent=2)

    print(f"Secondary-processing JSON saved: {json_path}")

    # -------------------------------------------------------------------------
    # Step 4: print aggregate summary
    # -------------------------------------------------------------------------
    weights = [e.get("edge_weight", {}).get("edge_weight", 0.0) for e in edges_v1]
    if weights:
        print("\n=== edge_weight statistics ===")
        print(f"  Sample count     : {len(weights)}")
        print(f"  Min              : {min(weights):.4f}")
        print(f"  Max              : {max(weights):.4f}")
        print(f"  Mean             : {sum(weights)/len(weights):.4f}")
        print(f"  Median           : {sorted(weights)[len(weights)//2]:.4f}")

    print("\nProcessing complete.")


if __name__ == "__main__":
    main()
