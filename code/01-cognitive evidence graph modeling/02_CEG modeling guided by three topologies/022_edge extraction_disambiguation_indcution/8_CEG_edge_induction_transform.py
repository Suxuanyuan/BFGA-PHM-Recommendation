"""
zotero_knowledge_graph_edge_transform_v5.py

Merge "edge JSON" into the "graph JSON array" format `edges` attribute based on the "node merge JSON".

Process:
  1. Read the edge JSON, iterate over each case's edges, collect and clean them.
  2. Node-replacement stage (preprocessing): first do exact match on source_node_id / target_node_id
     in the mapping table; entries without exact match are removed directly from raw_edges,
     so every edge entering the merge step has a valid mapping.
  3. Node-replacement stage (dual strategy): exact match + prefix-fallback, replace
     source_node_id / target_node_id with the merged node IDs.
  4. Merge stage: edges with the same (edge_group, edge_type, source_node_type, source_node_name,
     target_node_type, target_node_name, evidence_level) are merged into one, regenerating
     edge_id, edge_description, etc.
  5. Output the JSON and the HTML comparison report.

v1.1 changes:
  - Fix parse_node_id_map_md: regex now supports -Induction and other suffix variants.
  - Fix replace_node_ids: add prefix-stripping fallback strategy to generalize handling of all variant suffixes.
  - Add HTML report: display the edge-count change before vs. after merge and the property-detail differences.

v8.1 changes:
  - Process refactor: move the node_id mapping stage (Step 4-5) before the merge stage (Step 3)
    to avoid backtracking issues when node_id is missing from the mapping table after the merge.
  - Add filter_edges_by_exact_match: both source_node_id and target_node_id must match exactly in the
    mapping table; otherwise the edge is discarded, so every edge entering the merge step has a valid mapping.
  - Move the merge stage to Step 6, based on the replaced node_id.
"""

import json
import re
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Any, Tuple


# ============================================================================
# Path configuration
# ============================================================================
# NOTE: relative-path placeholders. Replace with your own absolute paths before running.
BASE_DIR = Path(r"./data/02_consensus_graph")

EDGE_JSON_PATH = r"./data/02_consensus_graph/B2-edge_consensus_disambiguation_induction/edge_consensus_disambiguation_induction_audit.json"
NODE_MERGE_JSON_PATH = r"./data/02_consensus_graph/C1-consensus_graph_paper_nodes_merge/nodes_audit_induction_hyperparameters_papers_nodes_merge_secondary.json"

NODE_ID_MAP_MD_PATH = r"./data/02_consensus_graph/C1-consensus_graph_paper_nodes_merge/nodes_audit_induction_hyperparameters_papers_nodes_merge_node_id_map.md"

OUTPUT_DIR = BASE_DIR / r"C2-consensus_graph_edges_merge"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_JSON_NAME = None   # dynamically generated, see run()
OUTPUT_JSON_PATH = None
OUTPUT_HTML_NAME = None
OUTPUT_HTML_PATH = None


# ============================================================================
# Helper functions
# ============================================================================
def extract_case_ids_from_filename(filename: str) -> Tuple[str, str]:
    """
    Extract the case_ids wrapped in square brackets from a filename.
    Prefer the first two [xxx] to construct the output filename.
    For example, input:
      "[225KHNN8][ZZZRPFBV]merge_nodes_audit_disambiguation_..."
    returns: ("225KHNN8", "ZZZRPFBV")
    """
    case_ids = re.findall(r"\[([A-Z0-9]+)\]", filename)
    if len(case_ids) >= 2:
        return case_ids[0], case_ids[1]
    return "unknown1", "unknown2"


# ============================================================================
# Step 0: read original data
# ============================================================================
def load_edge_json(path: Path) -> List[Dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def load_node_merge_json(path: Path) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# ============================================================================
# Step 1: read and parse node id mapping table (.md)
# ============================================================================
def _strip_suffix(node_id: str) -> str:
    """
    Strip the variant suffix at the end of node_id.
    For example: C00168_16_N1-Induction -> C00168_16_N1
                  C00171_11_5           -> C00171_11_5
    """
    if "-" in node_id:
        return node_id.split("-")[0]
    return node_id


def parse_node_id_map_md(path: Path) -> Dict[str, str]:
    """
    Parse the Markdown-format mapping table and return
        { original_node_id: merged_node_id }
    Example:
        | `N0001` | `C00169_01_N1` |
        | `N0090` | `C00168_16_N1-Induction` |
        | `N0042` | `C00171_11_5` |
    Output:
        { "C00169_01_N1": "N0001",
          "C00168_16_N1-Induction": "N0090",
          "C00171_11_5": "N0042", ... }
    """
    mapping: Dict[str, str] = {}
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    merged_pattern = re.compile(r"`(N\d{4})`")
    # Use `_` split to take the first part as case_id, format: | `N####` | `CASEID_...` |
    original_pattern = re.compile(r"`([A-Z0-9]+_\d{2}_[^`]+)`")

    for raw_line in content.splitlines():
        line = raw_line.strip()
        if not line or "|" not in line:
            continue

        merged_matches = merged_pattern.findall(line)
        original_matches = original_pattern.findall(line)

        if merged_matches and original_matches:
            merged_id = merged_matches[0]
            for orig_id in original_matches:
                mapping[orig_id] = merged_id

    return mapping


# ============================================================================
# Step 2: build the initial edges list (original collection before merge stage)
# ============================================================================
def collect_raw_edges(edge_json_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Iterate over the edges array of each case in the edge JSON and append them in order.
    Remove source_node_original_name / target_node_original_name.
    Also extract publish_year from the parent case and attach it to each raw edge.
    """
    raw_edges: List[Dict[str, Any]] = []
    for case in edge_json_data:
        publish_year = case.get("publish_year")
        for edge in case.get("edges", []):
            e = dict(edge)
            e.pop("source_node_original_name", None)
            e.pop("target_node_original_name", None)
            e["publish_year"] = publish_year
            raw_edges.append(e)
    return raw_edges


# ============================================================================
# Step 3: merge identical edges
# ============================================================================
def build_edge_key(e: Dict[str, Any]) -> tuple:
    """Key for determining whether two edges are completely identical."""
    return (
        e.get("edge_group", ""),
        e.get("edge_type", ""),
        e.get("source_node_type", ""),
        e.get("source_node_name", ""),
        e.get("target_node_type", ""),
        e.get("target_node_name", ""),
        e.get("evidence_level", ""),
    )


def build_edge_description_from_list(
    edge_group: str,
    edge_type: str,
    source_node_name: str,
    target_node_name: str,
    descriptions: List[str],
) -> str:
    """
    Generate a unified edge_description based on edge_group.
    """
    if edge_group == "01-default edge":
        return f"{source_node_name} connects {target_node_name}"

    if edge_group == "02-causal edge":
        return f"{source_node_name} {edge_type} {target_node_name}"

    if edge_group == "03-evidence edge":
        front = f"{source_node_name} motivates {target_node_name}"
        front_counter = 0
        back_counter = 0
        back_pattern = re.compile(r"\|(.*?)$")

        for desc in descriptions:
            m = back_pattern.search(desc)
            if not m:
                continue
            back_part = m.group(1).strip()
            if "明确指出证据关系" in back_part:
                front_counter += 1
            elif "未明确指出但推理可知证据关系" in back_part:
                back_counter += 1

        if front_counter > back_counter:
            suffix = "明确指出证据关系"
        else:
            suffix = "未明确指出但推理可知证据关系"

        return f"{front} | {suffix}"

    return f"{source_node_name} {edge_type} {target_node_name}"


def merge_edges(raw_edges: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    """
    Merge completely identical edges into one.
    Returns (merged_edges, diff_detail); diff_detail records the source information
    for each merged edge.
    """
    groups: Dict[tuple, List[Dict[str, Any]]] = defaultdict(list)
    for e in raw_edges:
        key = build_edge_key(e)
        groups[key].append(e)

    merged: List[Dict[str, Any]] = []
    diff_detail: Dict[str, Any] = {}

    for key, group in groups.items():
        edge_id = f"E{len(merged) + 1:04d}"

        first = group[0]
        source_node_id = first.get("source_node_id", "")
        target_node_id = first.get("target_node_id", "")
        source_node_type = first.get("source_node_type", "")
        source_node_name = first.get("source_node_name", "")
        target_node_type = first.get("target_node_type", "")
        target_node_name = first.get("target_node_name", "")
        edge_type = first.get("edge_type", "")
        edge_group = first.get("edge_group", "")
        evidence_level = first.get("evidence_level", "")

        desc_list = [e.get("edge_description", "") for e in group]

        edge_description = build_edge_description_from_list(
            edge_group, edge_type,
            source_node_name, target_node_name,
            desc_list,
        )

        edge_id_list = [e.get("edge_id", "") for e in group]

        edge_nums = len(group)

        publish_year_list = [e.get("publish_year") for e in group
                             if e.get("publish_year") is not None]
        if publish_year_list:
            edge_publish_year = round(sum(publish_year_list) / len(publish_year_list))
        else:
            edge_publish_year = None

        cite_score_list = [e.get("edge_cite_score") for e in group
                           if e.get("edge_cite_score") is not None]
        cite_count_list = [e.get("edge_cite_count") for e in group
                           if e.get("edge_cite_count") is not None]

        if cite_score_list:
            edge_cite_score = round(sum(cite_score_list) / len(cite_score_list), 4)
        else:
            edge_cite_score = None

        if cite_count_list:
            edge_cite_count = round(sum(cite_count_list) / len(cite_count_list), 4)
        else:
            edge_cite_count = None

        merged_edge = {
            "edge_id": edge_id,
            "source_node_id": source_node_id,
            "source_node_type": source_node_type,
            "source_node_name": source_node_name,
            "target_node_id": target_node_id,
            "target_node_type": target_node_type,
            "target_node_name": target_node_name,
            "edge_type": edge_type,
            "edge_group": edge_group,
            "evidence_level": evidence_level,
            "edge_description": edge_description,
            "edge_description_list": desc_list,
            "edge_weight": None,
            "edge_nums": edge_nums,
            "edge_cite_score": edge_cite_score,
            "edge_cite_count": edge_cite_count,
            "edge_cite_score_list": cite_score_list,
            "edge_cite_count_list": cite_count_list,
            "edge_id_list": edge_id_list,
            "edge_publish_year": edge_publish_year,
            "edge_publish_year_list": publish_year_list,
        }
        merged.append(merged_edge)

        diff_detail[edge_id] = {
            "source_edge_ids": edge_id_list,
            "source_node_id_before_merge": source_node_id,
            "target_node_id_before_merge": target_node_id,
            "merged_count": edge_nums,
        }

    return merged, diff_detail


# ============================================================================
# Step 4: node_id replacement (v1.0 -> v2.0)
# Dual strategy: exact match + prefix-stripping fallback
# ============================================================================
def _build_prefix_map(node_id_mapping: Dict[str, str]) -> Dict[str, str]:
    """
    Extract the prefix mapping { "CASEID_##_N#" : "N####" } from the complete mapping.
    Used as the fallback strategy: strip the variant suffix (e.g. -Induction) before matching.
    Note: variants without the trailing N prefix are also supported (e.g. C00171_11_5),
    where stripping still leaves the full ID.
    """
    prefix_map: Dict[str, str] = {}
    for orig_id, merged_id in node_id_mapping.items():
        stripped = _strip_suffix(orig_id)
        if stripped not in prefix_map:
            prefix_map[stripped] = merged_id
    return prefix_map


def filter_edges_by_exact_match(
    raw_edges: List[Dict[str, Any]],
    node_id_mapping: Dict[str, str],
) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    """
    Filter raw_edges using only the exact-match strategy.
    For source_node_id and target_node_id, both must be found in node_id_mapping,
    otherwise the edge is discarded and does not participate in subsequent processing.

    Returns (filtered edges, filter statistics).
    """
    src_unmatched_edges: List[Dict[str, Any]] = []
    tgt_unmatched_edges: List[Dict[str, Any]] = []
    both_unmatched_edges: List[Dict[str, Any]] = []
    passed_edges: List[Dict[str, Any]] = []

    for e in raw_edges:
        src_id = e.get("source_node_id", "")
        tgt_id = e.get("target_node_id", "")
        src_ok = src_id in node_id_mapping
        tgt_ok = tgt_id in node_id_mapping

        if src_ok and tgt_ok:
            passed_edges.append(e)
        elif not src_ok and not tgt_ok:
            both_unmatched_edges.append(e)
        elif not src_ok:
            src_unmatched_edges.append(e)
        else:
            tgt_unmatched_edges.append(e)

    stats = {
        "total_raw": len(raw_edges),
        "src_only_unmatched": len(src_unmatched_edges),
        "tgt_only_unmatched": len(tgt_unmatched_edges),
        "both_unmatched": len(both_unmatched_edges),
        "passed": len(passed_edges),
        "deleted": len(raw_edges) - len(passed_edges),
        "src_unmatched_detail": [
            {"edge_id": e.get("edge_id", "?"), "source_node_id": e.get("source_node_id", "")}
            for e in src_unmatched_edges
        ] + [
            {"edge_id": e.get("edge_id", "?"), "source_node_id": e.get("source_node_id", "")}
            for e in both_unmatched_edges
        ],
        "tgt_unmatched_detail": [
            {"edge_id": e.get("edge_id", "?"), "target_node_id": e.get("target_node_id", "")}
            for e in tgt_unmatched_edges
        ] + [
            {"edge_id": e.get("edge_id", "?"), "target_node_id": e.get("target_node_id", "")}
            for e in both_unmatched_edges
        ],
    }
    return passed_edges, stats


def replace_node_ids(
    edges: List[Dict[str, Any]],
    node_id_mapping: Dict[str, str],
    diff_detail: Dict[str, Any],
) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    """
    Iterate over edges, replacing source_node_id / target_node_id.

    Replacement strategy (dual safeguard):
      1. Exact match: directly look up in node_id_mapping.
      2. Prefix fallback: if exact match fails, try stripping the variant suffix part
         (-Induction etc., or a number without an N prefix), then look up prefix_map.
         Examples: C00168_16_N1-Induction -> C00168_16_N1 -> found -> N0090
                   C00171_11_5            -> C00171_11_5  -> found -> N0042
    Note: trailing numbers with or without the N prefix are both supported
    (e.g. C00171_11_5 and C00168_11_N5).

    Returns (replaced edges, replacement details); the replacement details record
    each edge's pre- and post-replacement source/target node_id.
    """
    prefix_map = _build_prefix_map(node_id_mapping)

    replace_log: Dict[str, Any] = {}
    total_src_replaced = 0
    total_tgt_replaced = 0
    total_src_fallback = 0
    total_tgt_fallback = 0
    total_src_unmatched = 0
    total_tgt_unmatched = 0

    for e in edges:
        edge_id = e.get("edge_id", "?")
        src_before = e.get("source_node_id", "")
        tgt_before = e.get("target_node_id", "")

        src_after = src_before
        tgt_after = tgt_before
        src_replaced = False
        tgt_replaced = False
        src_strategy = "exact"
        tgt_strategy = "exact"

        if src_before in node_id_mapping:
            src_after = node_id_mapping[src_before]
            src_replaced = True
        elif src_before in prefix_map:
            src_after = prefix_map[src_before]
            src_replaced = True
            src_strategy = "prefix_fallback"
        elif not src_before.startswith("N"):
            stripped = _strip_suffix(src_before)
            if stripped in prefix_map:
                src_after = prefix_map[stripped]
                src_replaced = True
                src_strategy = "prefix_fallback"

        if tgt_before in node_id_mapping:
            tgt_after = node_id_mapping[tgt_before]
            tgt_replaced = True
        elif tgt_before in prefix_map:
            tgt_after = prefix_map[tgt_before]
            tgt_replaced = True
            tgt_strategy = "prefix_fallback"
        elif not tgt_before.startswith("N"):
            stripped = _strip_suffix(tgt_before)
            if stripped in prefix_map:
                tgt_after = prefix_map[stripped]
                tgt_replaced = True
                tgt_strategy = "prefix_fallback"

        if src_replaced:
            e["source_node_id"] = src_after
            if src_strategy == "exact":
                total_src_replaced += 1
            else:
                total_src_fallback += 1
        else:
            if not src_before.startswith("N"):
                total_src_unmatched += 1

        if tgt_replaced:
            e["target_node_id"] = tgt_after
            if tgt_strategy == "exact":
                total_tgt_replaced += 1
            else:
                total_tgt_fallback += 1
        else:
            if not tgt_before.startswith("N"):
                total_tgt_unmatched += 1

        if src_replaced or tgt_replaced or not (src_before.startswith("N") and tgt_before.startswith("N")):
            replace_log[edge_id] = {
                "source": {
                    "before": src_before,
                    "after": src_after,
                    "replaced": src_replaced,
                    "strategy": src_strategy,
                },
                "target": {
                    "before": tgt_before,
                    "after": tgt_after,
                    "replaced": tgt_replaced,
                    "strategy": tgt_strategy,
                },
            }

    summary = {
        "src_exact_replaced": total_src_replaced,
        "src_fallback_replaced": total_src_fallback,
        "tgt_exact_replaced": total_tgt_replaced,
        "tgt_fallback_replaced": total_tgt_fallback,
        "src_unmatched": total_src_unmatched,
        "tgt_unmatched": total_tgt_unmatched,
    }

    return edges, {"summary": summary, "details": replace_log}


# ============================================================================
# Step 5: generate HTML comparison report
# ============================================================================
def generate_html_report(
    raw_edges_count: int,
    merged_edges_count: int,
    replaced_edges_count: int,
    diff_detail: Dict[str, Any],
    replace_log: Dict[str, Any],
    replace_summary: Dict[str, Any],
    output_path: Path,
    filter_stats: Dict[str, Any] = None,
):
    """
    Generate an HTML report showing:
      1. Edge-count statistics (original -> after merge -> after replacement)
      2. Replacement-strategy statistics (exact match / prefix fallback / unmatched)
      3. Detailed property-change table (showing pre- vs. post-replacement differences per edge_id)
    """
    src_exact = replace_summary.get("src_exact_replaced", 0)
    src_fallback = replace_summary.get("src_fallback_replaced", 0)
    tgt_exact = replace_summary.get("tgt_exact_replaced", 0)
    tgt_fallback = replace_summary.get("tgt_fallback_replaced", 0)
    src_unmatched = replace_summary.get("src_unmatched", 0)
    tgt_unmatched = replace_summary.get("tgt_unmatched", 0)

    changed_edges = []
    for edge_id, info in replace_log.items():
        src = info.get("source", {})
        tgt = info.get("target", {})
        if src.get("replaced") or tgt.get("replaced") or src.get("before") != src.get("after") or tgt.get("before") != tgt.get("after"):
            changed_edges.append({
                "edge_id": edge_id,
                "src_before": src.get("before", ""),
                "src_after": src.get("after", ""),
                "src_replaced": src.get("replaced", False),
                "src_strategy": src.get("strategy", ""),
                "tgt_before": tgt.get("before", ""),
                "tgt_after": tgt.get("after", ""),
                "tgt_replaced": tgt.get("replaced", False),
                "tgt_strategy": tgt.get("strategy", ""),
            })

    changed_edges.sort(key=lambda x: int(re.search(r"\d+", x["edge_id"]).group() if re.search(r"\d+", x["edge_id"]) else "0"))

    rows_src = ""
    rows_tgt = ""
    rows_unchanged = ""
    for ce in changed_edges:
        src_class = "replaced-exact" if ce["src_strategy"] == "exact" else ("replaced-fallback" if ce["src_strategy"] == "prefix_fallback" else "unmatched")
        tgt_class = "replaced-exact" if ce["tgt_strategy"] == "exact" else ("replaced-fallback" if ce["tgt_strategy"] == "prefix_fallback" else "unmatched")
        src_badge = ce["src_strategy"] if ce["src_replaced"] else ("unmatched" if src_unmatched > 0 else "—")
        tgt_badge = ce["tgt_strategy"] if ce["tgt_replaced"] else ("unmatched" if tgt_unmatched > 0 else "—")

        if ce["src_replaced"]:
            rows_src += f"""
        <tr>
          <td><code>{ce['edge_id']}</code></td>
          <td class="{src_class}"><code>{ce['src_before']}</code></td>
          <td class="{src_class}"><code>{ce['src_after']}</code></td>
          <td class="{src_class} badge-cell"><span class="badge badge-{src_class}">{src_badge}</span></td>
        </tr>"""
        if ce["tgt_replaced"]:
            rows_tgt += f"""
        <tr>
          <td><code>{ce['edge_id']}</code></td>
          <td class="{tgt_class}"><code>{ce['tgt_before']}</code></td>
          <td class="{tgt_class}"><code>{ce['tgt_after']}</code></td>
          <td class="{tgt_class} badge-cell"><span class="badge badge-{tgt_class}">{tgt_badge}</span></td>
        </tr>"""

    example_edge = changed_edges[0] if changed_edges else None
    example_rows = ""
    if example_edge:
        for key in ["edge_id", "src_before", "src_after", "tgt_before", "tgt_after"]:
            example_rows += f"<code>{example_edge.get(key, '')}</code><br>"

    unmatched_src_list = [eid for eid, info in replace_log.items()
                          if not info.get("source", {}).get("replaced", False)
                          and not info["source"]["before"].startswith("N")]
    unmatched_tgt_list = [eid for eid, info in replace_log.items()
                          if not info.get("target", {}).get("replaced", False)
                          and not info["target"]["before"].startswith("N")]

    unmatched_src_html = ""
    if unmatched_src_list:
        for eid in sorted(unmatched_src_list, key=lambda x: int(re.search(r"\d+", x).group() if re.search(r"\d+", x) else "0")):
            node_id = replace_log[eid]["source"]["before"]
            unmatched_src_html += f"<li><code>{eid}</code>: {node_id}</li>"
    else:
        unmatched_src_html = "<li class='text-success'>none</li>"

    unmatched_tgt_html = ""
    if unmatched_tgt_list:
        for eid in sorted(unmatched_tgt_list, key=lambda x: int(re.search(r"\d+", x).group() if re.search(r"\d+", x) else "0")):
            node_id = replace_log[eid]["target"]["before"]
            unmatched_tgt_html += f"<li><code>{eid}</code>: {node_id}</li>"
    else:
        unmatched_tgt_html = "<li class='text-success'>none</li>"

    unchanged_count = merged_edges_count - len(changed_edges)
    unchanged_html = f"<li>Edges with no node_id change: <strong>{unchanged_count}</strong></li>" if unchanged_count > 0 else ""

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Edges Transform Report — {OUTPUT_JSON_NAME}</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: "Segoe UI", "Microsoft YaHei", Arial, sans-serif; background: #f5f7fa; color: #333; padding: 24px; }}
  h1 {{ color: #1a1a2e; font-size: 1.5rem; margin-bottom: 6px; }}
  h2 {{ color: #16213e; font-size: 1.15rem; margin: 28px 0 12px; border-left: 4px solid #4361ee; padding-left: 10px; }}
  h3 {{ color: #2c3e50; font-size: 1rem; margin: 16px 0 8px; }}
  .subtitle {{ color: #666; font-size: 0.85rem; margin-bottom: 24px; }}
  .card {{ background: #fff; border-radius: 10px; padding: 20px; margin-bottom: 20px;
           box-shadow: 0 2px 8px rgba(0,0,0,0.08); }}
  .stats-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 14px; }}
  .stat-box {{ background: linear-gradient(135deg, #4361ee 0%, #3a0ca3 100%);
               color: #fff; border-radius: 8px; padding: 16px; text-align: center; }}
  .stat-box.green {{ background: linear-gradient(135deg, #06d6a0 0%, #028090 100%); }}
  .stat-box.orange {{ background: linear-gradient(135deg, #f77f00 0%, #d62828 100%); }}
  .stat-box.purple {{ background: linear-gradient(135deg, #7b2ff7 0%, #4361ee 100%); }}
  .stat-number {{ font-size: 2rem; font-weight: 700; }}
  .stat-label {{ font-size: 0.78rem; opacity: 0.9; margin-top: 4px; }}
  table {{ width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 0.85rem; }}
  th {{ background: #1a1a2e; color: #fff; padding: 9px 12px; text-align: left; }}
  td {{ padding: 7px 12px; border-bottom: 1px solid #e9ecef; vertical-align: middle; }}
  tr:hover {{ background: #f8f9fa; }}
  code {{ background: #e9ecef; padding: 1px 5px; border-radius: 3px; font-size: 0.82em;
          font-family: "Cascadia Code", "Consolas", monospace; }}
  .replaced-exact {{ background: #d4edda !important; }}
  .replaced-fallback {{ background: #fff3cd !important; }}
  .unmatched {{ background: #f8d7da !important; }}
  .badge-cell {{ text-align: center; }}
  .badge {{ padding: 2px 8px; border-radius: 12px; font-size: 0.75rem; color: #fff; }}
  .badge-replaced-exact {{ background: #28a745; }}
  .badge-replaced-fallback {{ background: #e67700; }}
  .badge-unmatched {{ background: #dc3545; }}
  .text-success {{ color: #28a745; }}
  .text-danger {{ color: #dc3545; }}
  .summary-row {{ display: flex; gap: 16px; flex-wrap: wrap; margin-top: 12px; }}
  .summary-item {{ background: #f8f9fa; border-radius: 6px; padding: 10px 14px; min-width: 160px; }}
  .summary-item .label {{ font-size: 0.75rem; color: #888; }}
  .summary-item .value {{ font-size: 1.1rem; font-weight: 600; color: #1a1a2e; }}
  ul {{ padding-left: 20px; }}
  li {{ margin-bottom: 4px; }}
  .footer {{ text-align: center; color: #aaa; font-size: 0.75rem; margin-top: 30px; }}
  .tab-bar {{ display: flex; gap: 4px; margin-bottom: 0; }}
  .tab-btn {{ padding: 8px 18px; border: none; border-radius: 6px 6px 0 0; cursor: pointer;
              font-size: 0.85rem; background: #dee2e6; color: #495057; }}
  .tab-btn.active {{ background: #1a1a2e; color: #fff; }}
  .tab-content {{ display: none; }}
  .tab-content.active {{ display: block; }}
  .section-note {{ font-size: 0.78rem; color: #888; margin-top: 6px; }}
</style>
</head>
<body>
<h1>Edges Transform Report</h1>
<p class="subtitle">File: {OUTPUT_JSON_NAME}</p>

<div class="card">
  <h2>1. Edge-count change statistics</h2>
  <div class="stats-grid">
    <div class="stat-box">
      <div class="stat-number">{raw_edges_count}</div>
      <div class="stat-label">Total raw edges (before merge)</div>
    </div>
    <div class="stat-box green">
      <div class="stat-number">{merged_edges_count}</div>
      <div class="stat-label">Edges after merge</div>
    </div>
    <div class="stat-box purple">
      <div class="stat-number">{replaced_edges_count}</div>
      <div class="stat-label">Edges after replacement</div>
    </div>
    <div class="stat-box orange">
      <div class="stat-number">{raw_edges_count - merged_edges_count}</div>
      <div class="stat-label">Edges reduced by duplicate-merge</div>
    </div>
  </div>
  <p class="section-note">Merge strategy: edges with the same (edge_group, edge_type, source_node_type, source_node_name, target_node_type, target_node_name, evidence_level) are merged.</p>
  {f"""
  <h3>Exact-match filter statistics</h3>
  <div class="summary-row">
    <div class="summary-item">
      <div class="label">Deleted by exact-match filter</div>
      <div class="value" style="color:#dc3545">{filter_stats.get('deleted', 0)}</div>
    </div>
    <div class="summary-item">
      <div class="label">Of which source unmatched</div>
      <div class="value">{filter_stats.get('src_only_unmatched', 0)}</div>
    </div>
    <div class="summary-item">
      <div class="label">Of which target unmatched</div>
      <div class="value">{filter_stats.get('tgt_only_unmatched', 0)}</div>
    </div>
    <div class="summary-item">
      <div class="label">Of which both source&target unmatched</div>
      <div class="value">{filter_stats.get('both_unmatched', 0)}</div>
    </div>
  </div>
  """ if filter_stats and filter_stats.get('deleted', 0) > 0 else ""}
</div>

<div class="card">
  <h2>2. Node-ID replacement strategy statistics</h2>
  <div class="summary-row">
    <div class="summary-item">
      <div class="label">source_node_id exact match</div>
      <div class="value">{src_exact}</div>
    </div>
    <div class="summary-item">
      <div class="label">source_node_id prefix fallback</div>
      <div class="value">{src_fallback}</div>
    </div>
    <div class="summary-item">
      <div class="label">source_node_id unmatched</div>
      <div class="value">{src_unmatched}</div>
    </div>
    <div class="summary-item">
      <div class="label">target_node_id exact match</div>
      <div class="value">{tgt_exact}</div>
    </div>
    <div class="summary-item">
      <div class="label">target_node_id prefix fallback</div>
      <div class="value">{tgt_fallback}</div>
    </div>
    <div class="summary-item">
      <div class="label">target_node_id unmatched</div>
      <div class="value">{tgt_unmatched}</div>
    </div>
  </div>
  <h3>Strategy explanation</h3>
  <ul>
    <li><strong>exact (exact match)</strong>: directly look up the complete original node_id (e.g. <code>C00168_16_N1-Induction</code>) in the mapping table.</li>
    <li><strong>prefix_fallback (prefix fallback)</strong>: when exact match fails, strip the suffix-variant part (e.g. <code>-Induction</code>), restore it to the <code>C####_##_N#</code> format, and look up again.</li>
    <li><strong>unmatched</strong>: no corresponding record is found in the mapping table; you need to check whether the node exists in the mapping table.</li>
  </ul>
</div>

<div class="card">
  <h2>3. source_node_id replacement details <span style="font-size:0.8rem;color:#888">({len([x for x in changed_edges if x['src_replaced']])} edges changed)</span></h2>
  <table>
    <thead>
      <tr>
        <th>edge_id</th>
        <th>Before replacement (source_node_id)</th>
        <th>After replacement</th>
        <th>Strategy</th>
      </tr>
    </thead>
    <tbody>
{rows_src if rows_src else "      <tr><td colspan='4' style='text-align:center;color:#888'>no source_node_id was replaced</td></tr>"}
    </tbody>
  </table>
</div>

<div class="card">
  <h2>4. target_node_id replacement details <span style="font-size:0.8rem;color:#888">({len([x for x in changed_edges if x['tgt_replaced']])} edges changed)</span></h2>
  <table>
    <thead>
      <tr>
        <th>edge_id</th>
        <th>Before replacement (target_node_id)</th>
        <th>After replacement</th>
        <th>Strategy</th>
      </tr>
    </thead>
    <tbody>
{rows_tgt if rows_tgt else "      <tr><td colspan='4' style='text-align:center;color:#888'>no target_node_id was replaced</td></tr>"}
    </tbody>
  </table>
</div>

<div class="card">
  <h2>5. Unmatched node IDs (need manual review)</h2>
  <div class="summary-row">
    <div class="summary-item">
      <div class="label">source_node_id unmatched</div>
      <ul style="list-style:none;padding:0">{unmatched_src_html}</ul>
    </div>
    <div class="summary-item">
      <div class="label">target_node_id unmatched</div>
      <ul style="list-style:none;padding:0">{unmatched_tgt_html}</ul>
    </div>
  </div>
  {unchanged_html}
</div>

<p class="footer">
  Automatically generated by zotero_knowledge_graph_edge_transform_v5.py &nbsp;|&nbsp; {output_path.name}
</p>
</body>
</html>"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"  -> HTML report saved: {output_path}")


# ============================================================================
# Main flow
# ============================================================================
def main():
    print("=" * 60)
    print("Edge Transform v8.1 — starting execution")
    print("=" * 60)

    # 0. Dynamically construct output path: extract [case_id1][case_id2] from NODE_MERGE_JSON_PATH filename
    # Note: the EDGE_JSON_PATH filename may contain the [unknown1][unknown2] placeholders;
    #       the real case_ids come from NODE_MERGE_JSON_PATH (e.g. [225KHNN8][ZZZRPFBV]).
    node_merge_filename = Path(NODE_MERGE_JSON_PATH).name
    case_id1, case_id2 = extract_case_ids_from_filename(node_merge_filename)
    OUTPUT_JSON_NAME = f"[{case_id1}][{case_id2}]+merged_edge_relations_disambiguation_induction_edges_merge.json"
    OUTPUT_JSON_PATH = OUTPUT_DIR / OUTPUT_JSON_NAME
    OUTPUT_HTML_NAME = OUTPUT_JSON_NAME.replace(".json", "_report.html")
    OUTPUT_HTML_PATH = OUTPUT_DIR / OUTPUT_HTML_NAME
    print(f"\n  [Path] Input filename (edge JSON): {Path(EDGE_JSON_PATH).name}")
    print(f"  [Path] Input filename (node-merge JSON): {node_merge_filename}")
    print(f"  [Path] Extracted case_id: [{case_id1}] + [{case_id2}]")
    print(f"  [Path] Output filename: {OUTPUT_JSON_NAME}")

    # 1. Read edge JSON
    print("\n[Step 1] Reading edge JSON...")
    edge_json_data = load_edge_json(EDGE_JSON_PATH)
    total_cases = len(edge_json_data)
    print(f"  -> Total {total_cases} cases")

    # 2. Collect raw edges
    print("\n[Step 2] Collecting raw edges (removing original_name attributes)...")
    raw_edges = collect_raw_edges(edge_json_data)
    raw_edges_count = len(raw_edges)
    print(f"  -> Total raw edges: {raw_edges_count}")

    # 3. Read and parse node-id mapping table
    print("\n[Step 3] Reading and parsing node-id mapping table...")
    node_id_map = parse_node_id_map_md(NODE_ID_MAP_MD_PATH)
    print(f"  -> Mapping entries: {len(node_id_map)}")

    # 4. Exact-match filter: entries without exact match are discarded
    print("\n[Step 4] Exact-match filter (both source_node_id & target_node_id must be in the mapping table)...")
    filtered_edges, filter_stats = filter_edges_by_exact_match(raw_edges, node_id_map)
    print(f"  -> Raw edge count: {filter_stats['total_raw']}")
    print(f"  -> Edge count after exact-match filter: {filter_stats['passed']}")
    print(f"  -> Edges deleted by exact-match filter: {filter_stats['deleted']}")
    if filter_stats['src_only_unmatched'] > 0:
        print(f"     Of which source_node_id unmatched: {filter_stats['src_only_unmatched']} edges")
    if filter_stats['tgt_only_unmatched'] > 0:
        print(f"     Of which target_node_id unmatched: {filter_stats['tgt_only_unmatched']} edges")
    if filter_stats['both_unmatched'] > 0:
        print(f"     Of which both source&target unmatched: {filter_stats['both_unmatched']} edges")

    # 5. Replace node_id (dual strategy)
    print("\n[Step 5] Replacing source_node_id / target_node_id (dual strategy)...")
    edges_replaced, replace_result = replace_node_ids(filtered_edges, node_id_map, diff_detail=None)
    replaced_edges_count = len(edges_replaced)
    replace_summary = replace_result["summary"]
    replace_log = replace_result["details"]

    print(f"  -> Edge count after replacement: {replaced_edges_count}")
    print(f"  -> source_node_id exact-match replacements: {replace_summary['src_exact_replaced']}")
    print(f"  -> source_node_id prefix-fallback replacements: {replace_summary['src_fallback_replaced']}")
    print(f"  -> source_node_id unmatched: {replace_summary['src_unmatched']}")
    print(f"  -> target_node_id exact-match replacements: {replace_summary['tgt_exact_replaced']}")
    print(f"  -> target_node_id prefix-fallback replacements: {replace_summary['tgt_fallback_replaced']}")
    print(f"  -> target_node_id unmatched: {replace_summary['tgt_unmatched']}")

    # 6. Merge stage (based on replaced node_id)
    print("\n[Step 6] Merging identical edges...")
    edges_v2, diff_detail = merge_edges(edges_replaced)
    merged_edges_count = len(edges_v2)
    print(f"  -> Edge count after merge: {merged_edges_count}")
    print(f"  -> Graph JSON array v2.0 built")

    # 7. Aggregate counts by edge_group
    group_counts: Dict[str, int] = defaultdict(int)
    for e in edges_v2:
        group_counts[e.get("edge_group", "unknown")] += 1
    print("\n  Edge-group statistics:")
    for g, cnt in sorted(group_counts.items()):
        print(f"    {g}: {cnt}")

    # 8. Generate HTML report
    print(f"\n[Step 7] Generating HTML comparison report...")
    generate_html_report(
        raw_edges_count=raw_edges_count,
        merged_edges_count=merged_edges_count,
        replaced_edges_count=replaced_edges_count,
        diff_detail=diff_detail,
        replace_log=replace_log,
        replace_summary=replace_summary,
        output_path=OUTPUT_HTML_PATH,
        filter_stats=filter_stats,
    )

    # 9. Save output
    print(f"\n[Step 8] Saving graph JSON...")
    output_obj = {"edges": edges_v2}
    with open(OUTPUT_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(output_obj, f, ensure_ascii=False, indent=2)

    print(f"  -> Output path: {OUTPUT_JSON_PATH}")
    print(f"  -> Wrote {len(edges_v2)} edges")
    print("\n" + "=" * 60)
    print("Execution complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
