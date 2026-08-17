# -*- coding: utf-8 -*-
r"""
Edge-relation disambiguation and induction processing program V7
========================================================================
Functions:
  1. Read the "edge JSON array v1" (edges after disambiguation)
  2. Read the "node array" (nodes after disambiguation, induction and hyperparameter assignment)
  3. Iterate over algorithm-class nodes (node_type 15~19) and build the mapping
     from "instance nodes" to "category nodes" via node_algorithm_class,
     then redirect the related edges.
  4. For redirected edges, update target_node_id/type/name and edge_description.
  5. For each redirected edge's case_id, append a new "connects" edge
     (from the category node to the instance node) at the end of the edges array.
  6. Generate a comparison HTML report.
  7. Output the processed edge JSON.

Inputs (user-specified at runtime):
  - Edge relation JSON (edge JSON array v1)
  - Node JSON (node array, with hyperparameter assignment results)
Outputs (dynamically named):
  - Edge JSON -> {original_file_name}_induction.json
  - HTML comparison report -> {original_file_name}_induction_comparison.html
"""

import os
import json
import html
import re
from pathlib import Path
from datetime import datetime
from typing import Optional


# ============================================================================
# User configuration (paths can be overridden via CLI parameters)
# ============================================================================
# NOTE: relative-path placeholders. Replace with your own absolute paths before running.
EDGE_JSON_PATH = r"./data/edge_consensus_disambiguation_induction/edge_consensus_disambiguation_v1.json"

NODE_JSON_PATH = r"./data/node_consensus_disambiguation_induction/node_consensus_disambiguation_induction_hyperparameters.json"

OUTPUT_BASE_DIR = r"./data/edge_consensus_disambiguation_induction_induction"


# ============================================================================
# Utility functions
# ============================================================================

def ensure_dir(path: str) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)


NON_ALGO_NODE_TYPES = {
    "01-Object Domain",
    "02-Object Type",
    "03-Operating Conditions",
    "04-Fault Location",
    "05-Fault Mode",
    "06-Fault Severity",
    "07-Compound Fault",
    "08-PHM Task",
    "09-Problem Scenario",
    "10-Dataset",
    "11-Sensor Information",
    "12-Training Data Availability",
    "13-Noise Level",
    "14-Computational Resource",
}

ALGO_NODE_TYPES = {
    "15-Data Preprocessing Algorithm",
    "16-Feature Extraction Algorithm",
    "17-Core Classifier Algorithm",
    "18-Data Generation Algorithm",
    "19-Training Optimization Algorithm",
}


def build_node_lookup(node_cases: list) -> dict:
    """
    For each case_id build a node_id -> node dictionary,
    and collect the mapping for all algorithm-class nodes.
    Returns (case_node_map, algo_instance_map)
      - case_node_map[case_id] = {node_id: node}
      - algo_instance_map[(case_id, instance_node_id)] = class_node
    """
    case_node_map: dict[str, dict[str, dict]] = {}
    algo_instance_map: dict[tuple, dict] = {}

    for case in node_cases:
        case_id = case.get("case_id", "")
        case_node_map[case_id] = {}
        for node in case.get("nodes", []):
            nid = node.get("node_id", "")
            if nid:
                case_node_map[case_id][nid] = node

            # Collect algorithm-class instance node -> class-node mapping
            node_type = node.get("node_type", "")
            if node_type in ALGO_NODE_TYPES:
                algo_class = node.get("node_algorithm_class")
                if algo_class:
                    # induction node naming rule: <original node_id>-Induction
                    class_nid = f"{nid}-Induction"
                    class_node = None
                    for n2 in case.get("nodes", []):
                        if n2.get("node_id") == class_nid:
                            class_node = n2
                            break
                    if class_node:
                        algo_instance_map[(case_id, nid)] = class_node

    return case_node_map, algo_instance_map


def next_edge_id(case_edges: list, case_id: str) -> str:
    """Compute the next sequence number in the edges array for the given case_id."""
    if not case_edges:
        return f"{case_id}_E001"
    nums = []
    for e in case_edges:
        eid = e.get("edge_id", "")
        m = re.search(r"E(\d+)$", eid)
        if m:
            nums.append(int(m.group(1)))
    if nums:
        nxt = max(nums) + 1
    else:
        nxt = len(case_edges) + 1
    return f"{case_id}_E{nxt:03d}"


# ============================================================================
# Core processing
# ============================================================================

def process_edge_induction(
    edge_json_path: str,
    node_json_path: str,
    output_base_dir: str,
) -> tuple:
    """
    Main flow:
      edge JSON array v1 -> edge JSON array v2 -> edge JSON array v3
    Returns (output JSON path, output HTML path, statistics dict)
    """
    # ---- 1. Load node data -----------------------------------------------
    with open(node_json_path, "r", encoding="utf-8") as f:
        node_cases = json.load(f)

    # ---- 2. Build node lookup table --------------------------------------------
    case_node_map, algo_instance_map = build_node_lookup(node_cases)

    # ---- 3. Load edge JSON (edge JSON array v1) --------------------------------
    with open(edge_json_path, "r", encoding="utf-8") as f:
        edge_cases = json.load(f)

    # ---- Aggregate collection -------------------------------------------------------
    stats = {
        "total_edges_v1": 0,
        "total_edges_v3": 0,
        "edges_redirected": 0,       # number of redirected edges
        "edges_03_redirected": 0,    # of which 03-evidence edges
        "edges_non03_redirected": 0,  # of which non-03 edges
        "edges_new_added": 0,        # newly added edge count
        "cases_processed": 0,
        "algo_instance_count": 0,    # number of algorithm nodes with node_algorithm_class
        "case_details": [],
    }

    # =========================================================================
    # Step 2 -> Step 3: redirect edges (edge JSON array v1 -> edge JSON array v2)
    # =========================================================================
    for case in edge_cases:
        case_id = case.get("case_id", "?")
        edges = case.get("edges", [])

        stats["total_edges_v1"] += len(edges)

        case_node_dict = case_node_map.get(case_id, {})
        case_detail = {
            "case_id": case_id,
            "edge_count_v1": len(edges),
            "edges_redirected": 0,
            "edges_03_redirected": 0,
            "edges_non03_redirected": 0,
            "edges_new_added": 0,
            "redirected_edge_samples": [],
        }

        if case_id in case_node_map:
            stats["cases_processed"] += 1

        redirect_count = 0
        redirect_03 = 0
        redirect_non03 = 0

        redirected_new_edges = []
        for edge in edges:
            tgt_nid = edge.get("target_node_id", "")

            # Check whether this target_node_id is an algorithm instance node that needs redirect
            class_node = algo_instance_map.get((case_id, tgt_nid))
            if class_node is None:
                continue

            # Original edges between non-algorithm nodes (1-14) and algorithm nodes (15-19) are not processed
            src_type = edge.get("source_node_type", "")
            if src_type in NON_ALGO_NODE_TYPES:
                continue

            # Found the corresponding class node; copy a new edge and perform redirect while keeping the original
            class_nid = class_node.get("node_id", "")
            class_type = class_node.get("node_type", "")
            class_name = class_node.get("node_name", "")
            instance_node = case_node_dict.get(tgt_nid, {})
            instance_name = instance_node.get("node_name", "")

            src_nid = edge.get("source_node_id", "")
            src_name = edge.get("source_node_name", "")
            src_original_name = edge.get("source_node_original_name") or ""
            edge_type = edge.get("edge_type", "")
            edge_group = edge.get("edge_group", "")
            is_03 = (edge_group == "03-evidence edge")

            orig_tgt_name = edge.get("target_node_name", "")

            new_edge_id = next_edge_id(edges, case_id)

            if is_03:
                desc_orig = edge.get("edge_description", "")
                parts = desc_orig.split("|")
                new_first = f"{src_name} {edge_type} {class_name}({instance_name})"
                parts[0] = new_first
                new_desc = "|".join(parts)
                redirect_03 += 1
            else:
                new_desc = f"{src_name} {edge_type} {class_name}({instance_name})"
                redirect_non03 += 1

            redirected_edge = {
                "edge_id": new_edge_id,
                "source_node_id": src_nid,
                "source_node_type": src_type,
                "source_node_name": src_name,
                "source_node_original_name": src_original_name,
                "target_node_id": class_nid,
                "target_node_type": class_type,
                "target_node_name": class_name,
                "target_node_original_name": instance_node.get("node_original_name") or "",
                "edge_type": edge_type,
                "edge_group": edge_group,
                "evidence_level": edge.get("evidence_level"),
                "edge_description": new_desc,
                "edge_weight": edge.get("edge_weight"),
                "edge_nums": edge.get("edge_nums"),
                "edge_cite_score": edge.get("edge_cite_score"),
                "edge_cite_count": edge.get("edge_cite_count"),
                "edge_id_list": edge.get("edge_id_list"),
            }
            redirected_new_edges.append(redirected_edge)

            redirect_count += 1

            if len(case_detail["redirected_edge_samples"]) < 3:
                case_detail["redirected_edge_samples"].append({
                    "edge_id": new_edge_id,
                    "edge_group": edge_group,
                    "old_target": tgt_nid,
                    "new_target": class_nid,
                    "old_desc": f"{src_name} {edge_type} {orig_tgt_name}",
                    "new_desc": new_desc,
                })

        # Append all redirected new edges to the end of edges (keep the original edges unchanged)
        edges.extend(redirected_new_edges)

        case_detail["edges_redirected"] = redirect_count
        case_detail["edges_03_redirected"] = redirect_03
        case_detail["edges_non03_redirected"] = redirect_non03

        stats["edges_redirected"] += redirect_count
        stats["edges_03_redirected"] += redirect_03
        stats["edges_non03_redirected"] += redirect_non03

        # =========================================================================
        # Step 4: append new edges (edge JSON array v2 -> edge JSON array v3)
        # =========================================================================
        # Iterate again over nodes, find all algorithm class nodes (15~19), and append "connects" edges
        node_list = []
        if case_id in case_node_map:
            node_list = list(case_node_map[case_id].values())

        new_edges_added = 0
        case_detail["new_edge_samples"] = []

        for node in node_list:
            node_type = node.get("node_type", "")
            if node_type not in ALGO_NODE_TYPES:
                continue

            target_nid = node.get("node_id", "")
            target_algo_class = node.get("node_algorithm_class")
            target_original_name = node.get("node_original_name") or ""
            target_name = node.get("node_name") or ""

            if not target_algo_class:
                continue

            # find the corresponding class node
            # induction node naming rule: <original node_id>-Induction
            class_nid = f"{target_nid}-Induction"
            class_node = case_node_dict.get(class_nid)
            if class_node is None:
                continue

            source_nid = class_node.get("node_id", "")
            source_original_name = class_node.get("node_original_name") or ""
            source_name = class_node.get("node_name", "")
            source_type = class_node.get("node_type", "")

            # get cite_score / cite_count (take any one from current edges)
            edge_cite_score = None
            edge_cite_count = None
            for e in edges:
                edge_cite_score = e.get("edge_cite_score")
                edge_cite_count = e.get("edge_cite_count")
                break

            new_edge_id = next_edge_id(edges, case_id)

            # edge_description format depends on source_node_type
            INDUCTION_SOURCE_TYPES = {
                "15-Data Preprocessing Algorithm-Induction",
                "16-Feature Extraction Algorithm-Induction",
                "17-Core Classifier Algorithm-Induction",
                "18-Data Generation Algorithm-Induction",
                "19-Training Optimization Algorithm-Induction",
            }
            if source_type in INDUCTION_SOURCE_TYPES:
                edge_desc = f"{source_name} connects {target_name}"
            else:
                edge_desc = f"{source_type} connects {target_name}"

            new_edge = {
                "edge_id": new_edge_id,
                "source_node_id": source_nid,
                "source_node_type": source_type,
                "source_node_name": source_name,
                "source_node_original_name": source_original_name,
                "target_node_id": target_nid,
                "target_node_type": node_type,
                "target_node_name": target_name,
                "target_node_original_name": target_original_name,
                "edge_type": "connects",
                "edge_group": "01-default edge",
                "evidence_level": "Low confidence",
                "edge_description": edge_desc,
                "edge_weight": None,
                "edge_nums": None,
                "edge_cite_score": edge_cite_score,
                "edge_cite_count": edge_cite_count,
                "edge_id_list": None,
            }

            edges.append(new_edge)
            new_edges_added += 1

            if len(case_detail["new_edge_samples"]) < 3:
                case_detail["new_edge_samples"].append({
                    "edge_id": new_edge_id,
                    "source": f"{source_nid} ({source_type})",
                    "target": f"{target_nid} ({node_type})",
                })

        case_detail["edges_new_added"] = new_edges_added
        stats["edges_new_added"] += new_edges_added
        stats["total_edges_v3"] += len(edges)

        stats["case_details"].append(case_detail)

    # =========================================================================
    # Step 5: aggregate algo_instance_count
    # =========================================================================
    stats["algo_instance_count"] = len(algo_instance_map)

    # =========================================================================
    # Step 6: output files (dynamically named)
    # =========================================================================
    ensure_dir(output_base_dir)

    input_name = Path(edge_json_path).stem
    output_json_name = input_name + "_induction.json"
    output_html_name = input_name + "_induction_comparison.html"
    output_json_path = os.path.join(output_base_dir, output_json_name)
    output_html_path = os.path.join(output_base_dir, output_html_name)

    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(edge_cases, f, ensure_ascii=False, indent=2)

    generate_html_report(
        edge_cases=edge_cases,
        stats=stats,
        output_html_path=output_html_path,
        input_edge_json=edge_json_path,
        node_json_path=node_json_path,
    )

    return output_json_path, output_html_path, stats


# ============================================================================
# HTML report generation
# ============================================================================

def generate_html_report(
    edge_cases, stats, output_html_path,
    input_edge_json, node_json_path,
):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    total_v1 = stats["total_edges_v1"]
    total_v3 = stats["total_edges_v3"]
    redirected = stats["edges_redirected"]
    redirect_03 = stats["edges_03_redirected"]
    redirect_non03 = stats["edges_non03_redirected"]
    new_added = stats["edges_new_added"]
    algo_count = stats["algo_instance_count"]

    # ---- case details table ----------------------------------------------------
    case_rows = ""
    for cd in stats["case_details"]:
        case_rows += (
            "<tr>"
            f"<td>{html.escape(cd['case_id'])}</td>"
            f"<td>{cd['edge_count_v1']}</td>"
            f"<td>{cd['edges_redirected']}</td>"
            f"<td>{cd['edges_03_redirected']}</td>"
            f"<td>{cd['edges_non03_redirected']}</td>"
            f"<td>{cd['edges_new_added']}</td>"
            f"<td>{cd['edge_count_v1'] + cd['edges_new_added']}</td>"
            "</tr>\n"
        )

    # ---- redirected edge samples table --------------------------------------------------
    redirect_samples = ""
    for cd in stats["case_details"]:
        for sample in cd.get("redirected_edge_samples", []):
            redirect_samples += (
                "<tr>"
                f"<td>{html.escape(cd['case_id'])}</td>"
                f"<td>{html.escape(sample['edge_id'])}</td>"
                f"<td>{html.escape(sample['edge_group'])}</td>"
                f"<td>{html.escape(sample['old_target'])}</td>"
                f"<td>{html.escape(sample['new_target'])}</td>"
                f"<td><del>{html.escape(sample['old_desc'])}</del></td>"
                f"<td><ins>{html.escape(sample['new_desc'])}</ins></td>"
                "</tr>\n"
            )

    # ---- newly added edge samples table ---------------------------------------------------
    new_edge_samples = ""
    for cd in stats["case_details"]:
        for sample in cd.get("new_edge_samples", []):
            new_edge_samples += (
                "<tr>"
                f"<td>{html.escape(cd['case_id'])}</td>"
                f"<td>{html.escape(sample['edge_id'])}</td>"
                f"<td>{html.escape(sample['source'])}</td>"
                f"<td>{html.escape(sample['target'])}</td>"
                "</tr>\n"
            )

    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Edge-relation disambiguation and induction comparison report</title>
<style>
  body { font-family: "Segoe UI", "Microsoft YaHei", Arial, sans-serif; margin: 20px; background: #f5f7fa; color: #333; }
  h1 { color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 8px; }
  h2 { color: #34495e; margin-top: 30px; border-left: 4px solid #3498db; padding-left: 10px; }
  h3 { color: #7f8c8d; margin-top: 20px; font-size: 0.95em; }
  .summary-cards { display: flex; flex-wrap: wrap; gap: 16px; margin: 20px 0; }
  .card { background: white; border-radius: 10px; padding: 18px 24px; min-width: 160px; box-shadow: 0 2px 6px rgba(0,0,0,0.1); }
  .card .num { font-size: 2em; font-weight: bold; color: #3498db; }
  .card .label { color: #7f8c8d; font-size: 0.9em; margin-top: 4px; }
  .card.green .num { color: #27ae60; }
  .card.orange .num { color: #e67e22; }
  .card.red .num { color: #e74c3c; }
  .card.purple .num { color: #8e44ad; }
  .explain-box { background: #fff9e6; border: 1px solid #f0d060; border-radius: 8px; padding: 14px 18px; margin: 16px 0; font-size: 0.9em; line-height: 1.7; }
  .explain-box strong { color: #d35400; }
  table { border-collapse: collapse; width: 100%%; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 6px rgba(0,0,0,0.08); margin-top: 10px; }
  th { background: #34495e; color: white; padding: 10px 12px; text-align: left; }
  td { padding: 8px 12px; border-bottom: 1px solid #ecf0f1; }
  tr:last-child td { border-bottom: none; }
  tr:hover { background: #f8f9fa; }
  code { background: #ecf0f1; padding: 2px 6px; border-radius: 4px; font-size: 0.88em; }
  del { color: #e74c3c; background: #fdecea; padding: 1px 4px; border-radius: 3px; }
  ins { color: #27ae60; background: #eafaf1; padding: 1px 4px; border-radius: 3px; text-decoration: none; }
  .meta { color: #95a5a6; font-size: 0.85em; margin: 6px 0; }
  .empty-note { color: #95a5a6; font-style: italic; padding: 10px; }
</style>
</head>
<body>
<h1>Edge-relation disambiguation and induction comparison report</h1>
<p class="meta">Generation time: %s</p>

<h2>Input files</h2>
<ul>
  <li>Edge relation JSON: <code>%s</code></li>
  <li>Node JSON: <code>%s</code></li>
</ul>

<h2>Overall statistics</h2>
<div class="summary-cards">
  <div class="card">
    <div class="num">%d</div>
    <div class="label">Total edges (v1)</div>
  </div>
  <div class="card">
    <div class="num">%d</div>
    <div class="label">Total edges (v3)</div>
  </div>
  <div class="card green">
    <div class="num">+%d</div>
    <div class="label">Net edge increase</div>
  </div>
  <div class="card orange">
    <div class="num">%d</div>
    <div class="label">Redirected edges</div>
  </div>
  <div class="card">
    <div class="num">%d</div>
    <div class="label">　|- 03-evidence edges redirected</div>
  </div>
  <div class="card">
    <div class="num">%d</div>
    <div class="label">　|- Non-03 edges redirected</div>
  </div>
  <div class="card purple">
    <div class="num">%d</div>
    <div class="label">Newly added "connects" edges</div>
  </div>
  <div class="card">
    <div class="num">%d</div>
    <div class="label">Cases processed</div>
  </div>
  <div class="card">
    <div class="num">%d</div>
    <div class="label">Algorithm instance nodes total</div>
  </div>
</div>

<div class="explain-box">
  <strong>Processing logic:</strong><br>
  &nbsp;&nbsp;(1) <strong>Edge redirect</strong> (total %d edges): for edges pointing to "algorithm instance nodes",
  redirect them to the corresponding "algorithm category nodes" and update target_node_id/type/name.<br>
  &nbsp;&nbsp;&nbsp;&nbsp;- <strong>03-evidence edges</strong>: split edge_description by "|", and only replace the
  first segment with "<code>&lt;source_name&gt; &lt;edge_type&gt; &lt;class_name&gt;(&lt;instance_name&gt;)</code>".<br>
  &nbsp;&nbsp;&nbsp;&nbsp;- <strong>Non-03 edges</strong>: directly overwrite edge_description with
  "<code>&lt;source_name&gt; &lt;edge_type&gt; &lt;class_name&gt;(&lt;instance_name&gt;)</code>".<br>
  &nbsp;&nbsp;(2) <strong>New edges</strong> (total %d edges): at the end of each case's edges array,
  append a "connects" edge (category node -> instance node) for every pair.
</div>

<h2>Per-case edge-count change detail</h2>
<table>
  <tr>
    <th>case_id</th>
    <th>v1 edge count</th>
    <th>Redirected edges</th>
    <th>　|- 03-evidence</th>
    <th>　|- Non-03</th>
    <th>New edges</th>
    <th>v3 edge count</th>
  </tr>
  %s
</table>

<h2>Edge-redirect samples (before vs. after)</h2>
%s

<h2>Newly added "connects" edge samples</h2>
%s

<p class="meta" style="margin-top:40px">Edge-relation disambiguation and induction program V7 &middot; %s</p>
</body>
</html>""" % (
        now,
        html.escape(input_edge_json),
        html.escape(node_json_path),
        total_v1,
        total_v3,
        total_v3 - total_v1,
        redirected,
        redirect_03,
        redirect_non03,
        new_added,
        stats["cases_processed"],
        algo_count,
        redirected,
        new_added,
        case_rows,
        f"<table><tr><th>case_id</th><th>edge_id</th><th>edge_group</th><th>old target_node_id</th><th>new target_node_id</th><th>old edge_description</th><th>new edge_description</th></tr>{redirect_samples}</table>" if redirect_samples else "<p class='empty-note'>No redirected edges</p>",
        f"<table><tr><th>case_id</th><th>edge_id</th><th>source (category node)</th><th>target (instance node)</th></tr>{new_edge_samples}</table>" if new_edge_samples else "<p class='empty-note'>No new edges</p>",
        now,
    )

    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)


# ============================================================================
# Command-line entry point
# ============================================================================

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Edge-relation disambiguation and induction program V7")
    parser.add_argument("--edge",  default=EDGE_JSON_PATH, help="Path to edge-relation JSON (v1)")
    parser.add_argument("--nodes", default=NODE_JSON_PATH,  help="Path to node JSON array")
    parser.add_argument("--out",   default=OUTPUT_BASE_DIR, help="Output directory")

    args = parser.parse_args()

    print(f"[Edge induction] Edge JSON: {args.edge}")
    print(f"[Edge induction] Node JSON: {args.nodes}")
    print(f"[Edge induction] Output dir: {args.out}")

    output_json, output_html, stats = process_edge_induction(
        edge_json_path=args.edge,
        node_json_path=args.nodes,
        output_base_dir=args.out,
    )

    print(f"\n[Done] Inducted edge JSON -> {output_json}")
    print(f"[Done] Comparison HTML   -> {output_html}")
    print(f"\nStatistics summary:")
    print(f"  Total edges (v1)         : {stats['total_edges_v1']}")
    print(f"  Total edges (v3)         : {stats['total_edges_v3']}")
    print(f"  Net edge increase        : {stats['total_edges_v3'] - stats['total_edges_v1']}")
    print(f"  Redirected edges         : {stats['edges_redirected']}")
    print(f"    |- 03-evidence redirects: {stats['edges_03_redirected']}")
    print(f"    |- Non-03 redirects    : {stats['edges_non03_redirected']}")
    print(f"  Newly added connects     : {stats['edges_new_added']}")
    print(f"  Cases processed          : {stats['cases_processed']}")
    print(f"  Algorithm instance nodes : {stats['algo_instance_count']}")


if __name__ == "__main__":
    main()
