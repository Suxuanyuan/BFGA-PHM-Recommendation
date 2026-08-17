# -*- coding: utf-8 -*-
r"""
Knowledge-graph papers & nodes attribute-merge resolution - post-processing program V7
========================================================================
Functions:
  Load the "node JSON" and run post-processing:

Processing steps:
  1. Load the "node JSON".
  2. Iterate each node{} and build the mapping between node_id and node_id_list,
     and output to an md file (the node JSON filename gets the "_node_id_mapping" suffix).
  3. Iterate each node{} and remove the following fields:
       node_description_list
       node_cite_score_list
       node_cite_count_list
       node_importance_list
     to form "node JSON v1.0".
  4. Save the output json (filename gets the "_secondary_processing" suffix).

Output path (RELATIVE PATH placeholder):
  ./data/04_final_graph/C1-paper_nodes_attribute_merge/
"""

import os
import json
import math
from collections import defaultdict

# ============================================================================
# User configuration
# ============================================================================

INPUT_JSON_PATH = (
    r"./data/04_final_graph/C1-paper_nodes_attribute_merge/[2277EAKD][ZZZRPFBV]merged-nodes_conformance_audit_merged_conformance_audit_disambiguation_conformance_audit_induction_conformance_audit_hyperparameter_assignment_papers_nodes_merge.json"
)

OUTPUT_DIR = (
    r"./data/04_final_graph"
    r"/C1-paper_nodes_attribute_merge"
)

# ============================================================================
# Main logic
# ============================================================================

# Field descriptions, for JSON metadata
NODE_FIELD_DESCRIPTIONS = {
    "node_id": "Unique identifier of the merged node (single value), string",
    "node_id_list": "List of original node IDs aggregated by this merged node (multiple values), array of strings",
    "node_type": "Node-type classification",
    "node_name": "Node name",
    "node_description": "Node description after LLM merging",
    "node_num": "Number of original nodes aggregated",
    "node_cite_score": "Citation score (aggregated mean)",
    "node_cite_count": "Citation count (aggregated mean)",
    "node_weight": "Node weight (may be empty)",
    "node_importance": "Node importance (may be empty)",
}

# ============================================================================
# node_weight quantization parameters
# ============================================================================

ALPHA = 0.30
BETA  = 0.20
GAMMA = 0.20
DELTA = 0.30
TAU   = 5

IMPORTANCE_MAP = {
    "Highest importance": 1.00,
    "Average importance": 0.60,
    "Not mentioned": 0.25,
}


def percentile_rank(values):
    """
    Compute the percentile rank for each element in values (using average-rank
    tie handling).
    percentile_rank(x) = (count strictly less than x + count less than or equal to x) / 2 / n
    Returns floats in 0~1.
    Even if all values are equal, the result will not all be 0, but rather 0.5.
    """
    if not values:
        return 0.0
    n = len(values)
    sorted_vals = sorted(values)
    result = []
    for v in values:
        count_lt  = sum(1 for val in sorted_vals if val < v)
        count_lte = sum(1 for val in sorted_vals if val <= v)
        avg_rank  = (count_lt + count_lte) / 2.0
        result.append(avg_rank / n)
    return result


def compute_freq_norm(node_num, all_node_nums):
    """Co-occurrence frequency normalization: freq_n = percentile_rank(log1p(node_num))"""
    if not all_node_nums:
        return 0.0
    log_vals = [math.log1p(n) for n in all_node_nums]
    ranks = percentile_rank(log_vals)
    if node_num is None:
        return 0.0
    return ranks[all_node_nums.index(node_num)]


def compute_if_norm(node_cite_score, all_scores):
    """Impact-factor normalization: if_n = percentile_rank(node_cite_score)"""
    if not all_scores:
        return 0.0
    ranks = percentile_rank(all_scores)
    if node_cite_score is None:
        return 0.0
    return ranks[all_scores.index(node_cite_score)]


def compute_cite_norm(node_cite_count, all_counts):
    """Citation-count normalization: cite_n = percentile_rank(log1p(node_cite_count))"""
    if not all_counts:
        return 0.0
    log_vals = [math.log1p(c) for c in all_counts]
    ranks = percentile_rank(log_vals)
    if node_cite_count is None:
        return 0.0
    return ranks[all_counts.index(node_cite_count)]


def compute_recency_norm(node_publish_year, max_year):
    """Time-trend normalization: recency_n = exp(-(max_year - node_publish_year) / tau)"""
    if node_publish_year is None or max_year is None:
        return 0.0
    return math.exp(-(max_year - node_publish_year) / TAU)


def normalize_by_group(node, group_stats, max_year):
    """
    Normalize by the node_type group the node belongs to, returning normalized values per dimension.
    group_stats: dict[node_type] -> dict of lists
    """
    node_type = node.get("node_type", "unknown")
    stats = group_stats.get(node_type, {})

    node_num          = node.get("node_num")
    node_cite_score   = node.get("node_cite_score")
    node_cite_count   = node.get("node_cite_count")
    node_publish_year = node.get("node_publish_year")
    node_importance   = node.get("node_importance")

    all_nums    = stats.get("all_node_nums", [])
    all_scores  = stats.get("all_cite_scores", [])
    all_counts  = stats.get("all_cite_counts", [])

    freq_n    = compute_freq_norm(node_num, all_nums)
    if_n      = compute_if_norm(node_cite_score, all_scores)
    cite_n    = compute_cite_norm(node_cite_count, all_counts)
    recency_n = compute_recency_norm(node_publish_year, max_year)
    authority_n = 0.3 * if_n + 0.7 * cite_n

    return {
        "freq_n": freq_n,
        "if_n": if_n,
        "cite_n": cite_n,
        "recency_n": recency_n,
        "authority_n": authority_n,
        "is_algorithm_node": node_importance is not None,
        "empirical_n": IMPORTANCE_MAP.get(node_importance, IMPORTANCE_MAP["Not mentioned"])
                       if node_importance is not None else None,
    }


def build_id_mapping_table(nodes):
    """Iterate nodes, build a mapping between node_id and the members of node_id_list, return md content."""
    lines = []
    lines.append("# node ID mapping table\n\n")
    lines.append("**Field description**\n")
    lines.append("- `node_id`: unique identifier of the merged node (single value); corresponding attribute `node_id`\n")
    lines.append("- `node_id_list`: list of original node IDs aggregated by this merged node (multiple values); corresponding attribute `node_id_list`\n\n")
    lines.append("---\n\n")
    lines.append("| `node_id` (attribute) | `node_id_list` (attribute) |\n")
    lines.append("|------------------|-----------------------|\n")

    for node in nodes:
        node_id = node.get("node_id", "")
        node_name = node.get("node_name", "")
        node_type = node.get("node_type", "")
        node_id_list = node.get("node_id_list", [])

        header = f"**{node_id}** ({node_type}: {node_name})"
        lines.append(f"\n## {header}\n\n")

        if node_id_list:
            for src_id in node_id_list:
                lines.append(f"| `{node_id}` | `{src_id}` |\n")
        else:
            lines.append(f"| `{node_id}` | *(empty)* |\n")

    return "".join(lines)


def remove_list_fields(node):
    """Remove list-type fields from node and return a new node."""
    fields_to_remove = [
        "node_description_list",
        "node_cite_score_list",
        "node_cite_count_list",
        "node_importance_list",
        "node_publish_year_list",
    ]
    return {k: v for k, v in node.items() if k not in fields_to_remove}


def main():
    # read input JSON
    print(f"Reading input file: {INPUT_JSON_PATH}")
    with open(INPUT_JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    # extract filename (without extension) and base path
    input_filename = os.path.basename(INPUT_JSON_PATH)
    name_without_ext = os.path.splitext(input_filename)[0]

    # ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # -------------------------------------------------------------------------
    # Step 2: generate node_id mapping table (md)
    # -------------------------------------------------------------------------
    nodes = data.get("nodes", [])
    print(f"Total {len(nodes)} nodes; generating mapping table...")

    md_content = build_id_mapping_table(nodes)
    md_filename = f"{name_without_ext}_node_id_mapping.md"
    md_path = os.path.join(OUTPUT_DIR, md_filename)

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"Mapping table saved: {md_path}")

    # -------------------------------------------------------------------------
    # Step 2.5: remove nodes where node_name is null
    # -------------------------------------------------------------------------
    nodes_before = len(nodes)
    nodes = [n for n in nodes if n.get("node_name") is not None]
    nodes_after = len(nodes)
    print(f"Removed nodes with node_name = null: {nodes_before} -> {nodes_after} (deleted {nodes_before - nodes_after})")

    # -------------------------------------------------------------------------
    # Step 3: remove list fields, generate v1.0 data
    # -------------------------------------------------------------------------
    print("Removing list fields...")
    nodes_v1 = [remove_list_fields(node) for node in nodes]

    # -------------------------------------------------------------------------
    # Step 3.5: compute node_weight (grouped by node_type)
    # -------------------------------------------------------------------------
    print("Computing node_weight (grouped by node_type)...")

    # 3.5.1: collect global statistics per node_type
    group_stats = defaultdict(lambda: {
        "all_node_nums":   [],
        "all_cite_scores": [],
        "all_cite_counts": [],
    })
    for n in nodes_v1:
        nt = n.get("node_type", "unknown")
        if n.get("node_num") is not None:
            group_stats[nt]["all_node_nums"].append(n["node_num"])
        if n.get("node_cite_score") is not None:
            group_stats[nt]["all_cite_scores"].append(n["node_cite_score"])
        if n.get("node_cite_count") is not None:
            group_stats[nt]["all_cite_counts"].append(n["node_cite_count"])

    # 3.5.2: max_year uses the global maximum (across types is reasonable)
    all_years = []
    for n in nodes_v1:
        py = n.get("node_publish_year")
        if py is not None:
            all_years.append(py)
    max_year = max(all_years) if all_years else 2025

    # 3.5.3: compute node_weight per node
    for node in nodes_v1:
        norm_vals = normalize_by_group(node, group_stats, max_year)

        freq_n      = norm_vals["freq_n"]
        authority_n = norm_vals["authority_n"]
        recency_n   = norm_vals["recency_n"]
        is_algo     = norm_vals["is_algorithm_node"]
        empirical_n = norm_vals.get("empirical_n")

        alpha_times_freq = ALPHA * freq_n
        beta_times_auth  = BETA  * authority_n
        gamma_times_rec  = GAMMA * recency_n

        if is_algo:
            delta_times_emp = DELTA * empirical_n
            weight = alpha_times_freq + beta_times_auth + gamma_times_rec + delta_times_emp
            weight_detail = {
                "node_weight":           round(weight, 6),
                "alpha * freq_n":        round(alpha_times_freq, 6),
                "beta  * authority_n":   round(beta_times_auth, 6),
                "gamma * recency_n":     round(gamma_times_rec, 6),
                "delta * empirical_n":   round(delta_times_emp, 6),
            }
        else:
            denom = ALPHA + BETA + GAMMA
            weight = (alpha_times_freq + beta_times_auth + gamma_times_rec) / denom
            weight_detail = {
                "node_weight":           round(weight, 6),
                "alpha * freq_n":        round(alpha_times_freq, 6),
                "beta  * authority_n":   round(beta_times_auth, 6),
                "gamma * recency_n":     round(gamma_times_rec, 6),
            }

        node["node_weight"] = weight_detail

    data_v1 = dict(data)
    data_v1["nodes"] = nodes_v1

    # -------------------------------------------------------------------------
    # Step 4: output json
    # -------------------------------------------------------------------------
    json_filename = f"{name_without_ext}_secondary_processing.json"
    json_path = os.path.join(OUTPUT_DIR, json_filename)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data_v1, f, ensure_ascii=False, indent=2)

    print(f"Secondary-processing JSON saved: {json_path}")
    print("Processing complete.")


if __name__ == "__main__":
    main()
