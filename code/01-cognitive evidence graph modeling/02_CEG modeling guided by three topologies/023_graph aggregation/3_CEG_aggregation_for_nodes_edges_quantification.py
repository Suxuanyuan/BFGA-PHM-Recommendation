# -*- coding: utf-8 -*-
r"""
zotero_knowledge_graph_paper_node_edge_transform_v5.py
=====================================================
Merge secondary-processed JSON of nodes and edges, generate the knowledge-graph JSON, and output an HTML report on weight probability distributions.

Flow:
  1. Dynamically read edge JSON and node JSON; extract case_id tags (e.g. [C00168][C00174]) from the filenames.
  2. Merge papers, nodes, edges into one JSON, output as "[C00168][C00174]common-graph-merged.json".
  3. Aggregate the probability curves (4 metrics) of node_weight by node_type group,
     and probability curves (5 metrics) of edge_weight by edge_group group.
  4. Compute the normalized-entropy uncertainty (0=min, 1=max) for each probability curve, and annotate it on the chart.
  5. Output a single HTML file with embedded ECharts charts.

Dependencies: numpy, scipy, json, pathlib, math
"""

import json
import math
import re
import argparse
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Any, Tuple

import numpy as np
from scipy.stats import gaussian_kde


# ============================================================================
# Path configuration (default) — RELATIVE PATH placeholders
# ============================================================================
BASE_DIR = Path(r"./data/04_final_graph")

DEFAULT_EDGE_JSON_PATH = r"./data/04_final_graph/C2-edges_attribute_merge/[2277EAKD][ZZZRPFBV]+merged-edges_relations_disambiguation_induction_edges_merge_secondary_processing.json"

DEFAULT_NODE_JSON_PATH = r"./data/04_final_graph/C1-paper_nodes_attribute_merge/[2277EAKD][ZZZRPFBV]merged-nodes_conformance_audit_merged_conformance_audit_disambiguation_conformance_audit_induction_conformance_audit_hyperparameter_assignment_papers_nodes_merge_secondary_processing.json"

OUTPUT_DIR = BASE_DIR / r"C3-common_graph_merge_output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================================
# Utility functions
# ============================================================================

def extract_case_ids(filepath: Path) -> str:
    """
    Extract all case_ids from the file path.
    Supports three formats:
    1. With square brackets: [C00168][C00174]...
    2. Without square brackets: C00168+...+C00174+...
    3. With square brackets and alphanumeric mix: [225KHNN8][ZZZRPFBV]...
    Unifies the output as [C00168][C00174] form (if originally alphanumeric it is preserved as-is).
    """
    s = str(filepath)
    # prefer matching bracket format; compatible with 5-digit numbers and 8-digit alphanumeric mix
    bracketed = re.findall(r"\[([A-Z0-9]{5,8})\]", s)
    if bracketed:
        return "".join("[" + cid + "]" for cid in bracketed)
    # without brackets: match alphanumeric (5-8 digits)
    all_codes = re.findall(r"(?<![a-zA-Z0-9_])([A-Z0-9]{5,8})(?![a-zA-Z0-9_])", s)
    if all_codes:
        return "".join("[" + cid + "]" for cid in all_codes)
    return ""


def load_json(path: Path) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(data: Dict[str, Any], path: Path) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def compute_kde_curve(values: List[float], n_points: int = 200) -> Tuple[List[float], List[float]]:
    """Estimate the probability density curve with KDE."""
    if len(values) < 2:
        if values:
            return [min(values), max(values)], [1.0, 1.0]
        return [0.0, 1.0], [0.0, 0.0]
    try:
        kde = gaussian_kde(values, bw_method="scott")
        x = np.linspace(min(values) - 0.02, max(values) + 0.02, n_points)
        y = kde(x)
        area = np.trapezoid(y, x)
        if area > 0:
            y = y / area
        return x.tolist(), y.tolist()
    except Exception:
        if values:
            return [min(values), max(values)], [1.0, 1.0]
        return [0.0, 1.0], [0.0, 0.0]


def make_kde_curve_data(values: List[float], n_points: int = 300) -> Tuple[List[float], List[float]]:
    """Generate the continuous KDE probability-density curve data (used in ECharts line chart)."""
    x, y = compute_kde_curve(values, n_points)
    x = [round(v, 5) for v in x]
    y = [round(v, 5) for v in y]
    return x, y


def make_kde_bars(values: List[float], stride: int = 7, max_bars: int = 30) -> Tuple[List[float], List[float]]:
    """Generate discretized bar-chart data (for ECharts)."""
    x, y = compute_kde_curve(values, 200)
    x_bar = x[::stride][:max_bars]
    y_bar = y[::stride][:max_bars]
    x_bar = [round(v, 4) for v in x_bar]
    y_bar = [round(v, 4) for v in y_bar]
    return x_bar, y_bar


def normalized_entropy(values: List[float]) -> float:
    """
    Normalized entropy: first discretize values into a 50-bin histogram,
    compute Shannon entropy H = -sum(p_i * log(p_i + eps)),
    then divide by max entropy log(bins) to obtain a 0~1 normalized value.

    Physical meaning: H ≈ 0 means the distribution is highly concentrated (most certain);
    H ≈ 1 means the distribution is near-uniform (least certain).
    Normalized entropy = Shannon entropy / maximum possible entropy.
    """
    if len(values) < 2:
        return 0.0
    n_bins = 50
    hist, _ = np.histogram(values, bins=n_bins)
    hist = hist.astype(float)
    total = hist.sum()
    if total == 0:
        return 0.0
    p = hist / total
    eps = 1e-12
    # filter out all-zero bins to avoid NaN from 0 * log(0)
    p_nonzero = p[p > eps]
    if len(p_nonzero) <= 1:
        # only one bin has values: distribution is fully concentrated, uncertainty is 0
        return 0.0
    h = -np.sum(p_nonzero * np.log(p_nonzero))
    max_h = math.log(n_bins)
    if max_h == 0:
        return 0.0
    return float(min(max(h / max_h, 0.0), 1.0))


# ============================================================================
# Step 1: merge JSON
# ============================================================================

def merge_papers_nodes_edges(
    edge_path: Path,
    node_path: Path,
    output_dir: Path,
) -> Tuple[Path, Dict[str, Any]]:
    """Read edge and node JSON, merge into knowledge graph, save and return path."""
    edge_data = load_json(edge_path)
    node_data = load_json(node_path)
    case_tag = extract_case_ids(edge_path)
    merged = {
        "meta": {
            "description": "Common graph - papers, nodes, edges merged file",
            "case_ids": case_tag,
            "edge_source": str(edge_path),
            "node_source": str(node_path),
        },
        "papers": node_data.get("papers", []),
        "nodes": node_data.get("nodes", []),
        "edges": edge_data.get("edges", []),
    }
    output_name = case_tag + "common-graph-merged.json"
    output_path = output_dir / output_name
    save_json(merged, output_path)
    return output_path, merged


# ============================================================================
# Step 2: aggregate data preparation
# ============================================================================

NODE_SUB_KEYS = [
    "node_weight",
    "alpha * freq_n",
    "beta  * authority_n",
    "gamma * recency_n",
]

EDGE_SUB_KEYS = [
    "edge_weight",
    "alpha * freq_e",
    "beta * authority_e",
    "gamma * recency_e",
    "delta * empirical_e",
]


def collect_node_weight_stats(nodes: List[Dict[str, Any]]) -> Dict[str, Dict[str, List[float]]]:
    """Group by node_type and collect each component of node_weight."""
    by_type: Dict[str, Dict[str, List[float]]] = defaultdict(
        lambda: {
            "node_weight": [],
            "alpha * freq_n": [],
            "beta  * authority_n": [],
            "gamma * recency_n": [],
        }
    )
    for node in nodes:
        nt = node.get("node_type", "unknown")
        w = node.get("node_weight", {})
        if not isinstance(w, dict):
            continue
        by_type[nt]["node_weight"].append(w.get("node_weight"))
        by_type[nt]["alpha * freq_n"].append(w.get("alpha * freq_n"))
        by_type[nt]["beta  * authority_n"].append(w.get("beta  * authority_n"))
        by_type[nt]["gamma * recency_n"].append(w.get("gamma * recency_n"))

    for nt in by_type:
        for k in by_type[nt]:
            by_type[nt][k] = [float(v) for v in by_type[nt][k] if v is not None]
    return dict(by_type)


def collect_edge_weight_stats(edges: List[Dict[str, Any]]) -> Dict[str, Dict[str, List[float]]]:
    """Group by edge_group and collect each component of edge_weight."""
    by_group: Dict[str, Dict[str, List[float]]] = defaultdict(
        lambda: {
            "edge_weight": [],
            "alpha * freq_e": [],
            "beta * authority_e": [],
            "gamma * recency_e": [],
            "delta * empirical_e": [],
        }
    )
    for edge in edges:
        eg = edge.get("edge_group", "unknown")
        w = edge.get("edge_weight", {})
        if not isinstance(w, dict):
            continue
        by_group[eg]["edge_weight"].append(w.get("edge_weight"))
        by_group[eg]["alpha * freq_e"].append(w.get("alpha * freq_e"))
        by_group[eg]["beta * authority_e"].append(w.get("beta * authority_e"))
        by_group[eg]["gamma * recency_e"].append(w.get("gamma * recency_e"))
        by_group[eg]["delta * empirical_e"].append(w.get("delta * empirical_e"))

    for eg in by_group:
        for k in by_group[eg]:
            by_group[eg][k] = [float(v) for v in by_group[eg][k] if v is not None]
    return dict(by_group)


# ============================================================================
# Step 3: HTML generation
# ============================================================================

def _js_escape(s: str) -> str:
    """Simply escape special characters in JS strings."""
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\r", "")


NODE_SUB_LABELS = [
    ("1/4 node_weight", "node_weight"),
    ("2/4 alpha \u00d7 freq_n", "alpha * freq_n"),
    ("3/4 beta \u00d7 authority_n", "beta  * authority_n"),
    ("4/4 gamma \u00d7 recency_n", "gamma * recency_n"),
]

EDGE_SUB_LABELS = [
    ("1/5 edge_weight", "edge_weight"),
    ("2/5 alpha \u00d7 freq_e", "alpha * freq_e"),
    ("3/5 beta \u00d7 authority_e", "beta * authority_e"),
    ("4/5 gamma \u00d7 recency_e", "gamma * recency_e"),
    ("5/5 delta \u00d7 empirical_e", "delta * empirical_e"),
]


def build_node_charts(node_stats: Dict[str, Dict[str, List[float]]]) -> Tuple[str, str]:
    """
    Generate the HTML and corresponding JS for the node chart area.
    One row per node_type, with 4 smooth KDE curve charts per row (line + area).
    Each chart header shows an index (1/4 ~ 4/4) and the metric name,
    the normalized entropy is annotated at the top-right corner, and the curve color
    is a gradient on entropy value (low=blue, high=red).
    Returns (sections_html, init_js).
    """
    import time
    sections = []
    js_lines = []

    for node_type, sub_data in sorted(node_stats.items()):
        t_group = time.time()
        gid = "n" + hex(abs(hash(node_type)) % 0xFFFFFF).lstrip("0x").zfill(6)
        cols_html = ""
        for idx, (label_disp, label_key) in enumerate(NODE_SUB_LABELS):
            vals = sub_data.get(label_key, [])
            n = len(vals)
            x_curve, y_curve = make_kde_curve_data(vals, 300)
            entropy_val = normalized_entropy(vals)
            cid = "c-" + gid + "-" + str(idx)
            entropy_pct = entropy_val * 100
            bar_w = int(round(entropy_val * 100))
            bar_color_int = int(entropy_val * 255)
            r = bar_color_int
            g = 255 - bar_color_int
            b = 100
            bar_color = f"rgb({r},{g},{b})"

            parts = [
                '<div class="chart-cell" id="' + cid + '">',
                '<div class="chart-header">',
                '<div class="chart-index">[' + str(idx + 1) + '/4]</div>',
                '<div class="chart-title">' + label_disp + '</div>',
                '<div class="entropy-info">',
                'H=<span class="ent-val">' + ("%.3f" % entropy_val) + '</span> '
                '(<span class="ent-pct">' + ("%.1f" % entropy_pct) + '%</span>) '
                'n=' + str(n),
                '</div>',
                '</div>',
                '<div class="entropy-bar-wrap">',
                '<div class="entropy-bar" style="width:' + str(bar_w) + '%;background:' + bar_color + ';"></div>',
                '</div>',
                '</div>',
            ]
            cols_html += "\n".join(parts)

            area_color_top = "#00D4FF"
            area_color_bot = "#003366"
            line_color = "#00D4FF"

            legend_text = label_disp + "  H=" + ("%.3f" % entropy_val)
            js_lines.append(
                "(function(){"
                "var dom=document.getElementById('" + cid + "');"
                "var chart=echarts.init(dom);"
                "chart.setOption({"
                "tooltip:{trigger:'axis',axisPointer:{type:'line'},"
                "backgroundColor:'rgba(10,10,10,0.88)',"
                "borderColor:'#30363d',borderWidth:1,"
                "textStyle:{color:'#fff',fontWeight:'bold',fontSize:13},"
                "formatter:function(p){"
                "return '<div style=\"font-size:13px;font-weight:bold;color:#fff\">'"
                "+p[0].name+'<br/>'"
                "+'<span style=\"color:#00D4FF\">P(x):</span> '+p[0].value.toFixed(5);"
                "}},"
                "legend:{"
                "show:true,"
                "top:2,"
                "textStyle:{fontSize:10,color:'#555',fontWeight:'bold'},"
                "tooltip:{show:true,formatter:'{b}'},"
                "itemWidth:14,"
                "itemHeight:10"
                "},"
                "grid:{top:38,right:8,bottom:36,left:52,containLabel:false},"
                "xAxis:{type:'category',data:" + json.dumps(x_curve) + ","
                "axisLabel:{fontSize:11,color:'#333',interval:Math.floor(" + str(len(x_curve)) + "/5),"
                "rotate:30},"
                "axisLine:{lineStyle:{color:'#999'}},"
                "splitLine:{show:false}},"
                "yAxis:{type:'value',name:'P(x)',nameTextStyle:{fontSize:12,color:'#333',fontWeight:'bold'},"
                "axisLabel:{fontSize:11,color:'#333',fontWeight:'bold'},"
                "axisLine:{lineStyle:{color:'#999'}},"
                "splitLine:{lineStyle:{color:'#ccc',type:'dashed'}}},"
                "series:[{name:'" + legend_text + "',type:'line',data:" + json.dumps(y_curve) + ","
                "smooth:0.4,symbol:'none',"
                "lineStyle:{color:'" + line_color + "',width:2},"
                "areaStyle:{color:new echarts.graphic.LinearGradient(0,0,0,1,"
                "[{offset:0,color:'" + area_color_top + "aa'},{offset:1,color:'" + area_color_bot + "77'}]),"
                "opacity:0.85}}]});"
                "})();"
            )

        print(f"       [node] {node_type}: {time.time()-t_group:.2f}s")

        sections.append(
            '<div class="chart-group">'
            '<h3 class="group-title">NODE: ' + node_type + '</h3>'
            '<div class="charts-grid node-grid">' + cols_html + '</div>'
            '</div>'
        )

    return "\n".join(sections), "\n\n".join(js_lines)


def build_edge_charts(edge_stats: Dict[str, Dict[str, List[float]]]) -> Tuple[str, str]:
    """
    Generate the HTML and corresponding JS for the edge chart area.
    One row per edge_group, with 5 smooth KDE curve charts per row (line + area).
    Each chart header shows an index (1/5 ~ 5/5) and the metric name,
    the normalized entropy is annotated at the top-right corner, and the curve color
    is a gradient on entropy value (low=green, high=red).
    Returns (sections_html, init_js).
    """
    import time
    sections = []
    js_lines = []

    for edge_group, sub_data in sorted(edge_stats.items()):
        t_group = time.time()
        gid = "e" + hex(abs(hash(edge_group)) % 0xFFFFFF).lstrip("0x").zfill(6)
        cols_html = ""
        for idx, (label_disp, label_key) in enumerate(EDGE_SUB_LABELS):
            vals = sub_data.get(label_key, [])
            n = len(vals)
            x_curve, y_curve = make_kde_curve_data(vals, 300)
            entropy_val = normalized_entropy(vals)
            cid = "c-" + gid + "-" + str(idx)
            entropy_pct = entropy_val * 100
            bar_w = int(round(entropy_val * 100))
            bar_color_int = int(entropy_val * 255)
            r = bar_color_int
            g = 255 - bar_color_int
            b = 50
            bar_color = f"rgb({r},{g},{b})"

            parts = [
                '<div class="chart-cell" id="' + cid + '">',
                '<div class="chart-header">',
                '<div class="chart-index">[' + str(idx + 1) + '/5]</div>',
                '<div class="chart-title">' + label_disp + '</div>',
                '<div class="entropy-info">',
                'H=<span class="ent-val">' + ("%.3f" % entropy_val) + '</span> '
                '(<span class="ent-pct">' + ("%.1f" % entropy_pct) + '%</span>) '
                'n=' + str(n),
                '</div>',
                '</div>',
                '<div class="entropy-bar-wrap">',
                '<div class="entropy-bar" style="width:' + str(bar_w) + '%;background:' + bar_color + ';"></div>',
                '</div>',
                '</div>',
            ]
            cols_html += "\n".join(parts)

            area_color_top = "#39FF14"
            area_color_bot = "#1a4d00"
            line_color = "#39FF14"

            legend_text = label_disp + "  H=" + ("%.3f" % entropy_val)

            js_lines.append(
                "(function(){"
                "var dom=document.getElementById('" + cid + "');"
                "var chart=echarts.init(dom);"
                "chart.setOption({"
                "tooltip:{trigger:'axis',axisPointer:{type:'line'},"
                "backgroundColor:'rgba(10,10,10,0.88)',"
                "borderColor:'#30363d',borderWidth:1,"
                "textStyle:{color:'#fff',fontWeight:'bold',fontSize:13},"
                "formatter:function(p){"
                "return '<div style=\"font-size:13px;font-weight:bold;color:#fff\">'"
                "+p[0].name+'<br/>'"
                "+'<span style=\"color:#39FF14\">P(x):</span> '+p[0].value.toFixed(5);"
                "}},"
                "legend:{"
                "show:true,"
                "top:2,"
                "textStyle:{fontSize:10,color:'#555',fontWeight:'bold'},"
                "tooltip:{show:true,formatter:'{b}'},"
                "itemWidth:14,"
                "itemHeight:10"
                "},"
                "grid:{top:38,right:8,bottom:36,left:52,containLabel:false},"
                "xAxis:{type:'category',data:" + json.dumps(x_curve) + ","
                "axisLabel:{fontSize:11,color:'#333',interval:Math.floor(" + str(len(x_curve)) + "/5),"
                "rotate:30},"
                "axisLine:{lineStyle:{color:'#999'}},"
                "splitLine:{show:false}},"
                "yAxis:{type:'value',name:'P(x)',nameTextStyle:{fontSize:12,color:'#333',fontWeight:'bold'},"
                "axisLabel:{fontSize:11,color:'#333',fontWeight:'bold'},"
                "axisLine:{lineStyle:{color:'#999'}},"
                "splitLine:{lineStyle:{color:'#ccc',type:'dashed'}}},"
                "series:[{name:'" + legend_text + "',type:'line',data:" + json.dumps(y_curve) + ","
                "smooth:0.4,symbol:'none',"
                "lineStyle:{color:'" + line_color + "',width:2},"
                "areaStyle:{color:new echarts.graphic.LinearGradient(0,0,0,1,"
                "[{offset:0,color:'" + area_color_top + "aa'},{offset:1,color:'" + area_color_bot + "77'}]),"
                "opacity:0.85}}]});"
                "})();"
            )

        print(f"       [edge] {edge_group}: {time.time()-t_group:.2f}s")

        sections.append(
            '<div class="chart-group">'
            '<h3 class="group-title">EDGE: ' + edge_group + '</h3>'
            '<div class="charts-grid edge-grid">' + cols_html + '</div>'
            '</div>'
        )

    return "\n".join(sections), "\n\n".join(js_lines)


def build_summary_table(node_stats, edge_stats) -> str:
    """Build the summary aggregate table HTML."""
    EDGE_METRIC_LABELS = {
        "edge_weight": "edge_weight",
        "alpha * freq_e": "alpha * freq_e",
        "beta * authority_e": "beta * authority_e",
        "gamma * recency_e": "gamma * recency_e",
        "delta * empirical_e": "delta * empirical_e",
    }

    rows_node = []
    for nt, sd in sorted(node_stats.items()):
        for k in NODE_SUB_KEYS:
            vals = sd.get(k, [])
            if not vals:
                continue
            ent = normalized_entropy(vals)
            rows_node.append(
                "<tr>"
                "<td>" + nt + "</td>"
                "<td>" + k.strip() + "</td>"
                "<td>" + str(len(vals)) + "</td>"
                "<td>%.4f</td><td>%.4f</td><td>%.4f</td><td>%.4f</td>"
                "</tr>" % (min(vals), max(vals), sum(vals) / len(vals), ent)
            )

    rows_edge = []
    for eg, sd in sorted(edge_stats.items()):
        for k in EDGE_SUB_KEYS:
            vals = sd.get(k, [])
            if not vals:
                continue
            ent = normalized_entropy(vals)
            rows_edge.append(
                "<tr>"
                "<td>" + eg + "</td>"
                "<td>" + EDGE_METRIC_LABELS.get(k, k) + "</td>"
                "<td>" + str(len(vals)) + "</td>"
                "<td>%.4f</td><td>%.4f</td><td>%.4f</td><td>%.4f</td>"
                "</tr>" % (min(vals), max(vals), sum(vals) / len(vals), ent)
            )

    return (
        '<h2>Summary Statistics</h2>\n'
        '<h3>Node Weight (by Node_Type)</h3>\n'
        '<table class="stat-table">'
        '<thead><tr><th>Node_Type</th><th>Metric</th><th>N</th><th>Min</th><th>Max</th><th>Mean</th><th>Entropy</th></tr></thead>'
        '<tbody>' + "".join(rows_node) + '</tbody></table>\n'
        '<h3>Edge Weight (by Edge_Group)</h3>\n'
        '<table class="stat-table">'
        '<thead><tr><th>Edge_Group</th><th>Metric</th><th>N</th><th>Min</th><th>Max</th><th>Mean</th><th>Entropy</th></tr></thead>'
        '<tbody>' + "".join(rows_edge) + '</tbody></table>'
    )


def generate_html(
    merged_path: Path,
    node_stats: Dict[str, Dict[str, List[float]]],
    edge_stats: Dict[str, Dict[str, List[float]]],
    merged_data: Dict[str, Any],
    case_tag: str,
) -> Path:
    """Generate the complete HTML report file."""
    import time
    t0 = time.time()
    t_step = time.time()

    node_sections_html, node_init_js = build_node_charts(node_stats)
    print(f"       build_node_charts: {time.time()-t_step:.2f}s")

    t_step = time.time()
    edge_sections_html, edge_init_js = build_edge_charts(edge_stats)
    print(f"       build_edge_charts: {time.time()-t_step:.2f}s")

    summary_html = build_summary_table(node_stats, edge_stats)

    n_nodes = len(merged_data.get("nodes", []))
    n_edges = len(merged_data.get("edges", []))
    n_papers = len(merged_data.get("papers", []))

    html = (
        '<!DOCTYPE html>\n'
        '<html lang="en">\n'
        '<head>\n'
        '<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        '<title>Common Graph Weight Probability Distribution Report ' + case_tag + '</title>\n'
        '<script src="https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js"></script>\n'
        '<style>\n'
        '*{margin:0;padding:0;box-sizing:border-box;}\n'
        'body{background:#f5f6fa;color:#111;font-family:"Segoe UI","Microsoft YaHei",Arial,sans-serif;font-size:14px;padding:20px;}\n'
        'h1{text-align:center;color:#1a3a6b;margin-bottom:6px;font-size:22px;font-weight:bold;}\n'
        '.meta-banner{text-align:center;color:#555;margin-bottom:20px;font-size:12px;}\n'
        '.meta-banner span{margin:0 12px;display:inline-block;}\n'
        'h2{color:#1a3a6b;margin:28px 0 12px;font-size:16px;border-left:4px solid #1a3a6b;padding-left:10px;font-weight:bold;}\n'
        'h3{color:#2a4a8b;margin:16px 0 8px;font-size:13px;}\n'
        '.chart-group{background:#fff;border:1px solid #c0c8d8;border-radius:10px;padding:16px;margin-bottom:24px;box-shadow:0 1px 4px rgba(0,0,0,0.08);}\n'
        '.group-title{color:#111;font-size:14px;margin-bottom:14px;padding-bottom:8px;border-bottom:1px solid #ddd;font-weight:bold;}\n'
        '.charts-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;}\n'
        '.edge-grid{grid-template-columns:repeat(5,1fr);}\n'
        '.chart-cell{background:#fafbfc;border:1px solid #d0d8e8;border-radius:6px;height:300px;position:relative;padding:0;display:flex;flex-direction:column;overflow:hidden;}\n'
        '.chart-header{display:flex;flex-direction:column;align-items:center;padding:4px 4px 2px;flex-shrink:0;background:#fff;}\n'
        '.chart-index{font-size:10px;color:#888;font-weight:bold;}\n'
        '.chart-title{text-align:center;font-size:12px;color:#111;font-weight:bold;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:100%;}\n'
        '.entropy-info{font-size:10px;color:#555;}\n'
        '.chart-cell>div.entropy-bar-wrap{flex-shrink:0;}\n'
        '.entropy-bar-wrap{width:100%;height:4px;background:#e8ecf4;flex-shrink:0;}\n'
        '.entropy-bar{height:100%;min-width:2px;transition:width 0.3s;}\n'
        '.ent-val{font-weight:bold;color:#111;}\n'
        '.ent-pct{color:#666;}\n'
        '.stat-table{width:100%;border-collapse:collapse;margin-top:10px;font-size:12px;background:#fff;}\n'
        '.stat-table th{background:#1a3a6b;color:#fff;padding:8px 6px;text-align:center;border:1px solid #ccc;position:sticky;top:0;}\n'
        '.stat-table td{padding:6px;text-align:center;border:1px solid #ddd;color:#111;}\n'
        '.stat-table tr:hover td{background:#eef2ff;}\n'
        '.entropy-legend{background:#fff;border:1px solid #c0c8d8;border-radius:8px;padding:14px 18px;margin-bottom:20px;font-size:12px;color:#444;line-height:1.9;box-shadow:0 1px 4px rgba(0,0,0,0.06);}\n'
        '.entropy-legend strong{color:#1a3a6b;}\n'
        '.entropy-legend em{font-style:normal;color:#6a2dbb;}\n'
        '.tab-nav{display:flex;gap:4px;margin-bottom:20px;}\n'
        '.tab-btn{padding:8px 18px;background:#e8ecf4;border:1px solid #c0c8d8;border-radius:6px 6px 0 0;color:#555;cursor:pointer;font-size:13px;font-weight:bold;}\n'
        '.tab-btn.active{background:#1a3a6b;border-bottom:2px solid #1a3a6b;color:#fff;}\n'
        '.tab-content{display:block;visibility:hidden;position:absolute;top:0;left:0;width:100%;pointer-events:none;}\n'
        '.tab-content.active{visibility:visible;position:relative;pointer-events:auto;}\n'
        '.section-intro{color:#555;font-size:12px;margin-bottom:14px;}\n'
        '@media(max-width:900px){.charts-grid{grid-template-columns:repeat(2,1fr);}.edge-grid{grid-template-columns:repeat(2,1fr);}}\n'
        '</style>\n'
        '</head>\n'
        '<body>\n'
        '<h1>Common Graph Weight Probability Distribution Report</h1>\n'
        '<div class="meta-banner">\n'
        '<span>File: ' + case_tag + 'common-graph-merged.json</span>\n'
        '<span>Papers: ' + str(n_papers) + '</span>\n'
        '<span>Nodes: ' + str(n_nodes) + '</span>\n'
        '<span>Edges: ' + str(n_edges) + '</span>\n'
        '</div>\n'
        '\n'
        '<div class="tab-nav">\n'
        '<button class="tab-btn active" id="btn-node" onclick="showTab(\'node\')">Node Weight Distribution</button>\n'
        '<button class="tab-btn" id="btn-edge" onclick="showTab(\'edge\')">Edge Weight Distribution</button>\n'
        '<button class="tab-btn" id="btn-summary" onclick="showTab(\'summary\')">Summary Statistics</button>\n'
        '</div>\n'
        '\n'
        '<div class="entropy-legend">\n'
        '<strong>Normalized Entropy Description:</strong><br>\n'
        'Use Shannon entropy as the classical quantification metric of probability-curve uncertainty.<br>\n'
        'Computation: discretize the probability curve into 50 bins, compute<br>\n'
        '<em>H = -sum(p_i * log(p_i + eps))</em>,\n'
        'then divide by maximum entropy <em>log(50)</em> to obtain the normalized value <strong>Entropy in [0, 1]</strong>.<br>\n'
        '<span style="color:#6e7681">Entropy approx 0</span>: highly concentrated distribution, lowest uncertainty (most certain)&nbsp;|&nbsp;\n'
        '<span style="color:#6e7681">Entropy approx 1</span>: near-uniform distribution, highest uncertainty (least certain)\n'
        '</div>\n'
        '\n'
        '<div id="tab-node" class="tab-content active">\n'
        '<h2>Node Weight Probability Curves (by Node_Type group)</h2>\n'
        '<p class="section-intro">One row per node_type, with 4 charts per row: '
        'node_weight, alpha x freq_n, beta x authority_n, gamma x recency_n. '
        'Normalized entropy Entropy and sample count n are annotated in the top-right corner.</p>\n'
        + node_sections_html + '\n'
        '</div>\n'
        '\n'
        '<div id="tab-edge" class="tab-content">\n'
        '<h2>Edge Weight Probability Curves (by Edge_Group group)</h2>\n'
        '<p class="section-intro">One row per edge_group, with 5 charts per row: '
        'edge_weight, alpha x freq_e, beta x authority_e, gamma x recency_e, delta x empirical_e. '
        'Normalized entropy Entropy and sample count n are annotated in the top-right corner.</p>\n'
        + edge_sections_html + '\n'
        '</div>\n'
        '\n'
        '<div id="tab-summary" class="tab-content">\n'
        + summary_html + '\n'
        '</div>\n'
        '\n'
        '<script>\n'
        'var _nodeChartsDone=false,_edgeChartsDone=false;\n'
        'function showTab(name){\n'
        'document.querySelectorAll(".tab-content").forEach(function(el){el.classList.remove("active");});\n'
        'document.querySelectorAll(".tab-btn").forEach(function(el){el.classList.remove("active");});\n'
        'document.getElementById("tab-"+name).classList.add("active");\n'
        'document.getElementById("btn-"+name).classList.add("active");\n'
        '}\n'
        + node_init_js + '\n\n' + edge_init_js + '\n'
        'window.addEventListener("resize",function(){\n'
        'document.querySelectorAll(".chart-cell").forEach(function(el){\n'
        'var inst=echarts.getInstanceByDom(el);if(inst)inst.resize();});});\n'
        '</script>\n'
        '</body>\n'
        '</html>\n'
    )

    html_path = merged_path.parent / (merged_path.stem + "_weight_distribution_report.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    return html_path


# ============================================================================
# Main program
# ============================================================================

def main(
    edge_path: Path,
    node_path: Path,
    output_dir: Path,
) -> Tuple[Path, Path]:
    import time
    t0 = time.time()
    t_step = t0

    print("[1/4] Reading edge JSON: " + str(edge_path))
    print("[1/4] Reading node JSON: " + str(node_path))

    merged_path, merged_data = merge_papers_nodes_edges(edge_path, node_path, output_dir)
    print(f"[1/4] Merged JSON saved: {str(merged_path)} ({time.time()-t_step:.2f}s)")

    t_step = time.time()
    print("[2/4] Collecting node_weight stats (by node_type)...")
    nodes = merged_data.get("nodes", [])
    node_stats = collect_node_weight_stats(nodes)
    for nt, sd in sorted(node_stats.items()):
        print("       " + nt + ": " + str(len(sd["node_weight"])) + " nodes")
    print(f"       [2/4] done in {time.time()-t_step:.2f}s")

    t_step = time.time()
    print("[3/4] Collecting edge_weight stats (by edge_group)...")
    edges = merged_data.get("edges", [])
    edge_stats = collect_edge_weight_stats(edges)
    for eg, sd in sorted(edge_stats.items()):
        print("       " + eg + ": " + str(len(sd["edge_weight"])) + " edges")
    print(f"       [3/4] done in {time.time()-t_step:.2f}s")

    case_tag = extract_case_ids(edge_path)
    t_step = time.time()
    print("[4/4] Generating HTML report...")
    html_path = generate_html(merged_path, node_stats, edge_stats, merged_data, case_tag)
    print(f"[4/4] HTML report saved: {str(html_path)} ({time.time()-t_step:.2f}s)")

    print(f"\nTotal time: {time.time()-t0:.2f}s")
    print("\nDone!")
    print("  Merged JSON: " + str(merged_path))
    print("  HTML report: " + str(html_path))
    return merged_path, html_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Merge node and edge JSONs into a knowledge graph, "
                    "then generate a weight probability distribution HTML report."
    )
    parser.add_argument(
        "--edge", type=Path, default=DEFAULT_EDGE_JSON_PATH,
        help="Path to edge relationship JSON (secondary processing)"
    )
    parser.add_argument(
        "--node", type=Path, default=DEFAULT_NODE_JSON_PATH,
        help="Path to node JSON (secondary processing)"
    )
    parser.add_argument(
        "--output", type=Path, default=OUTPUT_DIR,
        help="Output directory"
    )
    args = parser.parse_args()
    main(args.edge, args.node, args.output)
