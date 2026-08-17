# -*- coding: utf-8 -*-
r"""
Edge-Relation Disambiguation Processing Program V5
========================================================================
Functions:
  1. Load the edge-relation JSON (edge JSON array v1)
  2. Add 3 attributes to each edge: edge_cite_score, edge_cite_count, edge_id_list
  3. Use the journal-impact-factor table to fill cite_score and cite_count for each case_id's edges
  4. Use the disambiguated-induction node JSON to fill node_name for source/target edges
  5. Fix the node names in edge_description
  6. Output the disambiguated edge JSON and HTML statistics report

Input files (specified by user at runtime):
  - edge-relation JSON
  - journal impact-factor table (.md)
  - disambiguated-induction node JSON
Output files (auto-suffixed, dynamically named):
  - disambiguated edge JSON -> {original-filename}_disambiguation.json
  - HTML statistics report  -> {original-filename}_disambiguation.html
"""

import os
import re
import json
import html
from pathlib import Path
from datetime import datetime


# ============================================================================
# User configuration (paths can be overridden via command-line arguments)
# ============================================================================

# RELATIVE PATH placeholders below — replace with the actual paths at runtime.
EDGE_JSON_PATH = (
    r"./data/03_induction/B1-edges_disambiguation/225KHNN8+KC8MEE2V+merged-edges_conformance_audit_merged_conformance_audit_secondary_processing_conformance_audit.json"
)

JOURNAL_TABLE_PATH = (
    r"./data/03_induction/A2-nodes_merge_disambiguation_induction/[2277EAKD][ZZZRPFBV]merged-nodes_conformance_audit_merged_conformance_audit_disambiguation_conformance_audit_induction_conformance_audit_journal_impact_factor_table.md"
)

NODE_JSON_PATH = (
    r"./data/03_induction/A2-nodes_merge_disambiguation_induction/[2277EAKD][ZZZRPFBV]merged-nodes_conformance_audit_merged_conformance_audit_disambiguation_conformance_audit_induction_conformance_audit.json"
)

OUTPUT_BASE_DIR = (
    r"./data/03_induction/B1-edges_disambiguation"
)


# ============================================================================
# Utility functions
# ============================================================================

def ensure_dir(path: str) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)


def build_journal_table(journal_md_path: str) -> dict:
    r"""Parse the journal-impact-factor table (.md) and return {publish_source_upper: (cite_score, cite_count)}"""
    journal_map = {}
    with open(journal_md_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Match table row: | index | journal name | score | source | cite_source_paper |
    pattern = re.compile(
        r'\|\s*(\d+)\s*\|\s*([^\|]+?)\s*\|\s*\*\*([\d.]+)\s*\*\*.*?\|',
        re.IGNORECASE
    )
    for m in pattern.finditer(content):
        source = m.group(2).strip().upper()
        score = float(m.group(3))
        journal_map[source] = score

    if not journal_map:
        # Fallback match: publish_source | score | source | ...
        pattern2 = re.compile(
            r'^\|\s*\d+\s*\|\s*([^\|]+?)\s*\|\s*\*\*?([\d.]+)\s*\*\*?\s*\|',
            re.MULTILINE
        )
        for m in pattern2.finditer(content):
            source = m.group(1).strip().upper()
            score = float(m.group(2))
            if source not in journal_map:
                journal_map[source] = score

    return journal_map


def build_node_lookup(node_json_path: str) -> dict:
    r"""Build node_id -> node_name mapping dict (traversing all cases' nodes)"""
    lookup = {}
    with open(node_json_path, "r", encoding="utf-8") as f:
        cases = json.load(f)
    for case in cases:
        for node in case.get("nodes", []):
            nid = node.get("node_id", "")
            name = node.get("node_name") or node.get("node_original_name", "")
            lookup[nid] = name
    return lookup



# ============================================================================
# Core processing
# ============================================================================

def disambiguate_edge_json(
    edge_json_path: str,
    journal_table_path: str,
    node_json_path: str,
    output_base_dir: str,
) -> tuple:
    r"""
    Main flow:
      edge-json array v1 -> edge-json array v2 -> edge-json array v3 -> edge-json array v4
    Returns (output JSON path, output HTML path, output MD path, statistics dict)
    """
    # ---- 1. Load journal lookup table ----------------------------------------
    journal_map = build_journal_table(journal_table_path)

    # ---- 2. Load node lookup table -------------------------------------------
    node_lookup = build_node_lookup(node_json_path)

    # ---- 3. Load edge JSON ---------------------------------------------------
    with open(edge_json_path, "r", encoding="utf-8") as f:
        edge_cases = json.load(f)

    # ---- Aggregate collection ------------------------------------------------
    stats = {
        "total_edges": 0,
        "total_edges_with_desc": 0,
        "journal_matched": 0,
        "journal_unmatched": 0,
        # non-03 edges (direct overwrite strategy)
        "non03_count": 0,
        "non03_changed": 0,
        "non03_unchanged": 0,
        # 03-evidence edges (string replace strategy)
        "ev03_count": 0,
        "ev03_changed": 0,
        "ev03_unchanged": 0,
        # overall description changes
        "desc_changed": 0,
        "desc_unchanged": 0,
        "case_details": [],
    }

    # =========================================================================
    # Step 2 -> Step 3: add fields & fill cite_score / cite_count (edge-json array v2)
    # =========================================================================
    for case in edge_cases:
        case_id = case.get("case_id", "?")
        publish_source = case.get("publish_source", "").strip().upper()
        cite_count = case.get("cite_count")

        # Lookup cite_score in journal table
        cite_score = journal_map.get(publish_source)

        case_edge_count = len(case.get("edges", []))
        stats["total_edges"] += case_edge_count

        case_detail = {
            "case_id": case_id,
            "publish_source": publish_source,
            "cite_score_found": cite_score,
            "cite_count": cite_count,
            "edge_count": case_edge_count,
            "edges_with_desc_count": 0,
            # non-03 edges
            "non03_count": 0,
            "non03_changed": 0,
            "non03_unchanged": 0,
            # 03-evidence edges
            "ev03_count": 0,
            "ev03_changed": 0,
            "ev03_unchanged": 0,
            # overall
            "desc_changed": 0,
            "desc_unchanged": 0,
            # full info for unchanged edges
            "unchanged_edges": [],
            "desc_replace_samples": [],
        }

        if cite_score is not None:
            stats["journal_matched"] += 1
        else:
            stats["journal_unmatched"] += 1

        for edge in case.get("edges", []):
            # ---- add 3 attributes ----------------------------------------
            edge["edge_cite_score"] = cite_score
            edge["edge_cite_count"] = cite_count
            edge["edge_id_list"] = None

            # --------------------------------------------------------
            # Step 4-2: fill source_node_name / target_node_name
            # --------------------------------------------------------
            edge_group = edge.get("edge_group", "")
            is_03_evidence = (edge_group == "03-证据边")

            src_nid = edge.get("source_node_id", "")
            src_name = node_lookup.get(src_nid, "")
            edge["source_node_name"] = src_name if src_name else edge.get("source_node_name")

            tgt_nid = edge.get("target_node_id", "")
            tgt_name = node_lookup.get(tgt_nid, "")
            edge["target_node_name"] = tgt_name if tgt_name else edge.get("target_node_name")

            if edge.get("edge_description"):
                stats["total_edges_with_desc"] += 1
                case_detail["edges_with_desc_count"] += 1

            src_disamb = edge.get("source_node_name", "") or ""
            tgt_disamb = edge.get("target_node_name", "") or ""
            edge_type = edge.get("edge_type", "") or ""
            desc_original = edge.get("edge_description", "") or ""
            desc_after = desc_original

            if is_03_evidence:
                # ---- 03-evidence edges: string-exact replace strategy ----
                stats["ev03_count"] += 1
                case_detail["ev03_count"] += 1

                src_orig = edge.get("source_node_original_name", "") or ""
                tgt_orig = edge.get("target_node_original_name", "") or ""

                changed = False
                if src_orig and src_disamb and src_orig != src_disamb and src_orig in desc_after:
                    desc_after = desc_after.replace(src_orig, src_disamb)
                    changed = True
                if tgt_orig and tgt_disamb and tgt_orig != tgt_disamb and tgt_orig in desc_after:
                    desc_after = desc_after.replace(tgt_orig, tgt_disamb)
                    changed = True

                if changed:
                    stats["ev03_changed"] += 1
                    case_detail["ev03_changed"] += 1
                    if len(case_detail["desc_replace_samples"]) < 3:
                        case_detail["desc_replace_samples"].append({
                            "edge_id": edge.get("edge_id"),
                            "edge_group": edge_group,
                            "old": desc_original,
                            "new": desc_after,
                        })
                else:
                    stats["ev03_unchanged"] += 1
                    case_detail["ev03_unchanged"] += 1
                    case_detail["unchanged_edges"].append({
                        "case_id": case_id,
                        "edge_id": edge.get("edge_id"),
                        "edge_group": edge_group,
                        "source_node_id": src_nid,
                        "source_node_type": edge.get("source_node_type", ""),
                        "source_node_name": src_disamb,
                        "target_node_id": tgt_nid,
                        "target_node_type": edge.get("target_node_type", ""),
                        "target_node_name": tgt_disamb,
                        "edge_type": edge_type,
                    })
            else:
                # ---- non-03 edges: direct overwrite strategy ----
                stats["non03_count"] += 1
                case_detail["non03_count"] += 1

                new_desc = src_disamb + " " + edge_type + " " + tgt_disamb
                desc_after = new_desc

                if desc_original != new_desc:
                    stats["non03_changed"] += 1
                    case_detail["non03_changed"] += 1
                    if len(case_detail["desc_replace_samples"]) < 3:
                        case_detail["desc_replace_samples"].append({
                            "edge_id": edge.get("edge_id"),
                            "edge_group": edge_group,
                            "old": desc_original,
                            "new": new_desc,
                        })
                else:
                    stats["non03_unchanged"] += 1
                    case_detail["non03_unchanged"] += 1
                    case_detail["unchanged_edges"].append({
                        "case_id": case_id,
                        "edge_id": edge.get("edge_id"),
                        "edge_group": edge_group,
                        "source_node_id": src_nid,
                        "source_node_type": edge.get("source_node_type", ""),
                        "source_node_name": src_disamb,
                        "target_node_id": tgt_nid,
                        "target_node_type": edge.get("target_node_type", ""),
                        "target_node_name": tgt_disamb,
                        "edge_type": edge_type,
                    })

            # ---- Unified write-back & aggregate overall change ----
            edge["edge_description"] = desc_after
            if desc_original != desc_after:
                stats["desc_changed"] += 1
                case_detail["desc_changed"] += 1
            else:
                stats["desc_unchanged"] += 1
                case_detail["desc_unchanged"] += 1

        stats["case_details"].append(case_detail)

    # =========================================================================
    # Step 5: output file (dynamically named)
    # =========================================================================
    ensure_dir(output_base_dir)

    input_name = Path(edge_json_path).stem
    output_json_name = input_name + "_disambiguation.json"
    output_html_name = input_name + "_disambiguation.html"
    output_md_name = input_name + "_disambiguation_unchanged.md"
    output_json_path = os.path.join(output_base_dir, output_json_name)
    output_html_path = os.path.join(output_base_dir, output_html_name)
    output_md_path = os.path.join(output_base_dir, output_md_name)

    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(edge_cases, f, ensure_ascii=False, indent=2)

    generate_html_report(
        edge_cases=edge_cases,
        stats=stats,
        journal_map=journal_map,
        output_html_path=output_html_path,
        input_edge_json=edge_json_path,
        journal_table_path=journal_table_path,
        node_json_path=node_json_path,
    )

    generate_unchanged_md(stats=stats, output_md_path=output_md_path, input_edge_json=edge_json_path)

    return output_json_path, output_html_path, output_md_path, stats


# ============================================================================
# HTML report generation
# ============================================================================

def generate_html_report(
    edge_cases, stats, journal_map, output_html_path,
    input_edge_json, journal_table_path, node_json_path,
):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # overall aggregate numbers
    total_edges = stats["total_edges"]
    total_edges_with_desc = stats.get("total_edges_with_desc", 0)
    journal_matched = stats["journal_matched"]
    journal_unmatched = stats["journal_unmatched"]
    non03_count = stats["non03_count"]
    non03_changed = stats["non03_changed"]
    non03_unchanged = stats["non03_unchanged"]
    ev03_count = stats["ev03_count"]
    ev03_changed = stats["ev03_changed"]
    ev03_unchanged = stats["ev03_unchanged"]
    desc_changed = stats["desc_changed"]
    desc_unchanged = stats["desc_unchanged"]

    # ---- Journal lookup table summary -------------------------------------
    journal_rows = ""
    for src, score in sorted(journal_map.items(), key=lambda x: -x[1]):
        journal_rows += "<tr><td>%s</td><td><strong>%s</strong></td></tr>\n" % (html.escape(src), score)

    # ---- per-case detail table -------------------------------------------
    case_rows = ""
    for cd in stats["case_details"]:
        cite = cd.get("cite_score_found")
        cite_html = cite if cite is not None else '<span style="color:#e74c3c">not matched</span>'
        unchanged_count = len(cd.get("unchanged_edges", []))
        case_rows += "<tr>" \
            "<td>%s</td>" \
            "<td>%s</td>" \
            "<td>%s</td>" \
            "<td>%s</td>" \
            "<td>%s</td>" \
            "<td>%s</td>" \
            "<td>%s</td>" \
            "<td>%s</td>" \
            "<td style=\"color:#27ae60\">%s</td>" \
            "<td style=\"color:#e67e22\">%s</td>" \
            "</tr>\n" % (
                html.escape(cd["case_id"]),
                html.escape(cd["publish_source"]),
                cite_html,
                cd["cite_count"],
                cd["edge_count"],
                cd["non03_count"],
                cd["ev03_count"],
                cd.get("edges_with_desc_count", 0),
                cd["desc_changed"],
                cd["desc_unchanged"],
            )

    # ---- Unchanged-edge details (grouped by case_id) --------------------
    unchanged_detail_rows = ""
    for cd in stats["case_details"]:
        edges = cd.get("unchanged_edges", [])
        if not edges:
            continue
        first = True
        for ue in edges:
            if first:
                unchanged_detail_rows += "<tr>"
                unchanged_detail_rows += "<td rowspan=\"%d\">%s</td>" % (len(edges), html.escape(cd["case_id"]))
                unchanged_detail_rows += "<td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>" % (
                    html.escape(ue["edge_id"]),
                    html.escape(ue["edge_group"]),
                    html.escape(ue["source_node_id"]),
                    html.escape(ue["source_node_type"]),
                    html.escape(ue["source_node_name"]),
                    html.escape(ue["target_node_id"]),
                    html.escape(ue["target_node_type"]),
                    html.escape(ue["target_node_name"]),
                    html.escape(ue["edge_type"]),
                )
                unchanged_detail_rows += "</tr>\n"
                first = False
            else:
                unchanged_detail_rows += "<tr>"
                unchanged_detail_rows += "<td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>" % (
                    html.escape(ue["edge_id"]),
                    html.escape(ue["edge_group"]),
                    html.escape(ue["source_node_id"]),
                    html.escape(ue["source_node_type"]),
                    html.escape(ue["source_node_name"]),
                    html.escape(ue["target_node_id"]),
                    html.escape(ue["target_node_type"]),
                    html.escape(ue["target_node_name"]),
                    html.escape(ue["edge_type"]),
                )
                unchanged_detail_rows += "</tr>\n"

    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Edge Relation Disambiguation Report</title>
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
  .explain-box { background: #fff9e6; border: 1px solid #f0d060; border-radius: 8px; padding: 14px 18px; margin: 16px 0; font-size: 0.9em; line-height: 1.7; }
  .explain-box strong { color: #d35400; }
  table { border-collapse: collapse; width: 100%; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 6px rgba(0,0,0,0.08); margin-top: 10px; }
  th { background: #3498db; color: white; padding: 10px 12px; text-align: left; }
  td { padding: 8px 12px; border-bottom: 1px solid #ecf0f1; }
  tr:last-child td { border-bottom: none; }
  tr:hover { background: #f8f9fa; }
  code { background: #ecf0f1; padding: 2px 6px; border-radius: 4px; font-size: 0.88em; }
  del { color: #e74c3c; background: #fdecea; padding: 1px 4px; border-radius: 3px; }
  ins { color: #27ae60; background: #eafaf1; padding: 1px 4px; border-radius: 3px; text-decoration: none; }
  .meta { color: #95a5a6; font-size: 0.85em; margin: 6px 0; }
</style>
</head>
<body>
<h1>Edge Relation Disambiguation Report</h1>
<p class="meta">Generation time: %s</p>

<h2>Input files</h2>
<ul>
  <li>Edge-relation JSON: <code>%s</code></li>
  <li>Journal table: <code>%s</code></li>
  <li>Node JSON: <code>%s</code></li>
</ul>

<h2>Overall statistics</h2>
<div class="summary-cards">
  <div class="card"><div class="num">%d</div><div class="label">Total edges</div></div>
  <div class="card"><div class="num">%d</div><div class="label">Edges with edge_description</div></div>
  <div class="card green"><div class="num">%d</div><div class="label">Journal matched</div></div>
  <div class="card red"><div class="num">%d</div><div class="label">Journal unmatched</div></div>
  <div class="card"><div class="num">%d</div><div class="label">Non-03 edge count</div></div>
  <div class="card orange"><div class="num">%d</div><div class="label">Non-03 edge description changed</div></div>
  <div class="card"><div class="num">%d</div><div class="label">03-evidence edge count</div></div>
  <div class="card green"><div class="num">%d</div><div class="label">03-evidence edge description changed</div></div>
  <div class="card green"><div class="num">%d</div><div class="label">Total description changed</div></div>
  <div class="card orange"><div class="num">%d</div><div class="label">Total description unchanged (manual review needed)</div></div>
</div>

<div class="explain-box">
  <strong>edge_description replacement strategy:</strong><br>
  &nbsp;&nbsp;① <strong>Non-03-evidence edges</strong> (total %d): directly overwrite with <code>&lt;source_node_name&gt; + &lt;edge_type&gt; + &lt;target_node_name&gt;</code>.<br>
  &nbsp;&nbsp;② <strong>03-evidence edges</strong> (total %d): exact-replace source_node_original_name and target_node_original_name in the original description with the disambiguated ones.
</div>

<h2>Journal impact-factor mapping</h2>
<table>
  <tr><th>Journal name</th><th>2yr_mean_citedness</th></tr>
  %s
</table>

<h2>Per-case disambiguation details</h2>
<table>
  <tr>
    <th>case_id</th><th>publish_source</th><th>cite_score</th><th>cite_count</th>
    <th>Edge count</th><th>Non-03 edges</th><th>03-evidence edges</th>
    <th>Has desc</th>
    <th>Description changed</th><th>Description unchanged</th>
  </tr>
  %s
</table>

<h2>Unchanged-description edge details (manual review needed)</h2>
<p style="color:#95a5a6;font-size:0.85em;margin-bottom:8px">
  The following edges' edge_description remained identical to the original after the replacement strategy; please confirm one by one whether manual editing is needed.
</p>
%s

<p class="meta" style="margin-top:40px">Edge-Relation Disambiguation Processing Program V5 &middot; %s</p>
</body>
</html>""" % (
        now,
        html.escape(input_edge_json),
        html.escape(journal_table_path),
        html.escape(node_json_path),
        total_edges,
        total_edges_with_desc,
        journal_matched,
        journal_unmatched,
        non03_count,
        non03_changed,
        ev03_count,
        ev03_changed,
        desc_changed,
        desc_unchanged,
        non03_count,
        ev03_count,
        journal_rows,
        case_rows,
        "All edge descriptions have been changed" if not unchanged_detail_rows else "<table><tr><th>case_id</th><th>edge_id</th><th>edge_group</th><th>source_node_id</th><th>source_node_type</th><th>source_node_name</th><th>target_node_id</th><th>target_node_type</th><th>target_node_name</th><th>edge_type</th></tr>%s</table>" % unchanged_detail_rows,
        now,
    )

    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)


# ============================================================================
# MD report generation (details of edges with unchanged description)
# ============================================================================

def generate_unchanged_md(stats, output_md_path, input_edge_json):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total_unchanged = stats["desc_unchanged"]

    lines = []
    lines.append("# Edge-relation disambiguation - edges with unchanged edge_description (manual review needed)")
    lines.append("")
    lines.append("**Input file**: `%s`" % input_edge_json)
    lines.append("**Generation time**: %s" % now)
    lines.append("")
    lines.append("## Aggregate summary")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|------|------|")
    lines.append("| Total edges | %d |" % stats["total_edges"])
    lines.append("| Description changed | %d |" % stats["desc_changed"])
    lines.append("| **Description unchanged (manual review needed)** | **%d** |" % total_unchanged)
    lines.append("| Non-03-evidence edges | %d (changed %d, unchanged %d) |" % (
        stats["non03_count"], stats["non03_changed"], stats["non03_unchanged"]))
    lines.append("| 03-evidence edges | %d (changed %d, unchanged %d) |" % (
        stats["ev03_count"], stats["ev03_changed"], stats["ev03_unchanged"]))
    lines.append("")
    lines.append("---")
    lines.append("")

    grand_total = 0
    for cd in stats["case_details"]:
        edges = cd.get("unchanged_edges", [])
        if not edges:
            continue
        grand_total += len(edges)
        lines.append("## %s (total %d unchanged edges)" % (cd["case_id"], len(edges)))
        lines.append("")
        lines.append("| # | case_id | edge_id | edge_group | source_node_id | source_node_type | source_node_name | target_node_id | target_node_type | target_node_name | edge_type |")
        lines.append("|---|---------|---------|------------|----------------|-----------------|----------------|----------------|-----------------|----------------|----------|")
        for i, ue in enumerate(edges, 1):
            lines.append("| %d | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
                i,
                ue.get("case_id", cd["case_id"]),
                ue["edge_id"],
                ue["edge_group"],
                ue["source_node_id"],
                ue["source_node_type"],
                ue["source_node_name"],
                ue["target_node_id"],
                ue["target_node_type"],
                ue["target_node_name"],
                ue["edge_type"],
            ))
        lines.append("")

    if grand_total == 0:
        lines.append("**All edge descriptions have been changed.**")

    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


# ============================================================================
# Command-line entry point
# ============================================================================

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Edge-Relation Disambiguation Processing Program V5")
    parser.add_argument("--edge",   default=EDGE_JSON_PATH,      help="Edge-relation JSON path")
    parser.add_argument("--journal",default=JOURNAL_TABLE_PATH,   help="Journal impact-factor table (.md) path")
    parser.add_argument("--nodes", default=NODE_JSON_PATH,       help="Disambiguation-induction node JSON path")
    parser.add_argument("--out",    default=OUTPUT_BASE_DIR,      help="Output directory")

    args = parser.parse_args()

    print(f"[Edge Disambiguation] Edge JSON        : {args.edge}")
    print(f"[Edge Disambiguation] Journal table    : {args.journal}")
    print(f"[Edge Disambiguation] Node JSON        : {args.nodes}")
    print(f"[Edge Disambiguation] Output directory : {args.out}")

    output_json, output_html, output_md_path, stats = disambiguate_edge_json(
        edge_json_path=args.edge,
        journal_table_path=args.journal,
        node_json_path=args.nodes,
        output_base_dir=args.out,
    )

    print(f"\n[Complete] Disambiguated edge JSON -> {output_json}")
    print(f"[Complete] HTML report             -> {output_html}")
    print(f"[Complete] MD no-change details     -> {output_md_path}")
    print(f"\nStatistics summary:")
    print(f"  Total edges                 : {stats['total_edges']}")
    print(f"  Edges with desc             : {stats.get('total_edges_with_desc', 0)}")
    print(f"  Journal matched             : {stats['journal_matched']}")
    print(f"  Non-03 edges                : {stats['non03_count']} (changed {stats['non03_changed']}, unchanged {stats['non03_unchanged']})")
    print(f"  03-evidence edges            : {stats['ev03_count']} (changed {stats['ev03_changed']}, unchanged {stats['ev03_unchanged']})")
    print(f"  Description changed total    : {stats['desc_changed']}")
    print(f"  Description unchanged total  : {stats['desc_unchanged']}")


if __name__ == "__main__":
    main()
