# -*- coding: utf-8 -*-
r"""
Algorithm-Node Induction-Completion Program V9
========================================================================
Functions:
  Read the disambiguated node JSON (disambiguation graph JSON); based on the 5
  algorithm-category mapping tables (15/16/17/18/19), perform induction and
  completion on the nodes, and produce a "disambiguation-induction graph JSON".

Processing steps:
  Step0 Print the explicit path configuration (verified at startup)
  Step1 Read input files (disambiguation graph JSON + 5 mapping-table md files)
        * The 5 mapping-table paths are defined as "explicit absolute paths" in
          MAPPING_TABLE_PATHS at the top of the file; there is no auto-search or
          suffix-stitching logic. To switch mapping tables, edit this dictionary.
  Step2 Parse 5 mapping-table md -> 5 mapping-table arrays
        Each array element: {alg_class_name, alg_class_description, node_ids: [...]}
  Step3 Iterate over the mapping-table arrays; add the node_algorithm_class property
        to each node and append new induction nodes
  Step4 "Disambiguation-induction graph JSON" mapping-completeness audit
  Step5 "Disambiguation-induction graph JSON" compliance cleanup
  Step6 Self-audit -- coverage check of node_algorithm_class for algorithm-type nodes
        in the output JSON + auto-fill
  Step7 Save the final disambiguation-induction graph JSON (the local JSON must be
        the latest graph)
  Step8 Generate an HTML report (based on the final saved JSON)

Input files (paths are explicitly defined in the user-config section at the top of
the file; no auto-search):
  - Disambiguation graph JSON: INPUT_JSON_PATH
  - 5 mapping-table md files: MAPPING_TABLE_PATHS["15"-"19"]  (each key is an algorithm-type number)

Output files (paths are explicitly defined in the user-config section at the top of the file):
  - Disambiguation-induction graph JSON (saved to OUTPUT_BASE_DIR; filename = input filename + "_归纳.json")
"""

import os
import re
import json
import time
import sys
from pathlib import Path

# Fix stdout encoding for Chinese Windows (GBK terminals)
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# =========================================================================
# User configuration
# ============================================================================

INPUT_JSON_PATH = r"./data/02_consensus_graph/[2277EAKD][ZZZRPFBV]合并节点_规范性审查_合并_规范性审查_消歧_规范性审查.json"

MAPPING_TABLE_PATHS = {
    "15": r"./data/03_induction/归纳清单表/[2277EAKD][ZZZRPFBV]合并节点_规范性审查_合并_规范性审查_消歧_规范性审查_归纳_15节点映射表_二次处理.md",
    "16": r"./data/03_induction/归纳清单表/[2277EAKD][ZZZRPFBV]合并节点_规范性审查_合并_规范性审查_消歧_规范性审查_归纳_16节点映射表_二次处理.md",
    "17": r"./data/03_induction/归纳清单表/[2277EAKD][ZZZRPFBV]合并节点_规范性审查_合并_规范性审查_消歧_规范性审查_归纳_17节点映射表_二次处理.md",
    "18": r"./data/03_induction/归纳清单表/[2277EAKD][ZZZRPFBV]合并节点_规范性审查_合并_规范性审查_消歧_规范性审查_归纳_18节点映射表_二次处理.md",
    "19": r"./data/03_induction/归纳清单表/[2277EAKD][ZZZRPFBV]合并节点_规范性审查_合并_规范性审查_消歧_规范性审查_归纳_19节点映射表_二次处理.md",
}

OUTPUT_BASE_DIR = r"./data/03_induction"


# ============================================================================
# Path-configuration overview (printed at startup for verification)
# ============================================================================
PATH_CONFIG = [
    ("Input JSON (disambiguation graph)", INPUT_JSON_PATH),
    ("Output directory (induction graph)", OUTPUT_BASE_DIR),
    ("Mapping-table 15 (Data-Preprocessing Algorithm Class)", MAPPING_TABLE_PATHS["15"]),
    ("Mapping-table 16 (Feature-Extraction Algorithm Class)", MAPPING_TABLE_PATHS["16"]),
    ("Mapping-table 17 (Core-Discriminator Algorithm Class)", MAPPING_TABLE_PATHS["17"]),
    ("Mapping-table 18 (Data-Generation Algorithm Class)",   MAPPING_TABLE_PATHS["18"]),
    ("Mapping-table 19 (Training-Optimization Algorithm Class)",   MAPPING_TABLE_PATHS["19"]),
]


# ============================================================================
# Utility functions
# ============================================================================

def load_json(path: str) -> list:
    """Load a JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(data: list, path: str) -> None:
    """Save a JSON file (creates the directory automatically)."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# ============================================================================
# Text-cleaning utilities (strip <br>, **, "代表算法：" and other distractors)
# ============================================================================

def _clean_description(text: str) -> str:
    """
    Clean description text extracted from mapping-table markdown cells; strip:
      - <br> newline tags  -> replaced by "；"
      - **  bold markers    -> removed
      - "代表算法：" and the content after it -> removed entirely
      - Extra whitespace   -> normalized to a single space, trimmed at both ends
    """
    if not text:
        return ""
    text = text.replace("<br>", "；")
    text = text.replace("**", "")
    marker = "代表算法："
    marker_idx = text.find(marker)
    if marker_idx != -1:
        text = text[:marker_idx]
        text = text.rstrip("。，,")
    text = re.sub(r"。[,，]", "。", text)
    text = re.sub(r"[,，]([，。])", r"\1", text)
    text = text.replace(",", "，")
    text = re.sub(r"\s+", " ", text).strip()
    text = text.strip("。，、；,")
    return text


def _fuzzy_name_match(name1: str, name2: str) -> float:
    """
    Compute a similarity score (0.0 ~ 1.0) between two algorithm names.
    Strategies:
      1. Exact equality: 1.0
      2. Substring containment ("Douglas-Rachford algorithm" subset of "Douglas-Rachford Splitting"): 0.95
      3. Algorithm-name variant matching: first extract the core algorithm name
         (e.g., "Douglas-Rachford"), then match core stems
      4. Word-level Jaccard similarity (with English suffix stripping)
    Final score is the maximum across strategies.
    """
    if not name1 or not name2:
        return 0.0
    if name1 == name2:
        return 1.0

    n1, n2 = name1.lower(), name2.lower()

    # Strategy 2: substring containment (core algorithm name identical)
    if n1 in n2 or n2 in n1:
        return 0.95

    def normalize_for_algo(s):
        """Extract the core stem from an algorithm name (remove common suffixes and added words)"""
        # Replace separators with spaces
        for ch in '/(),.-_':
            s = s.replace(ch, ' ')
        # Synonym replacement (algorithm naming variants)
        synonyms = {
            'algorithm': 'algo', 'method': 'algo', 'approach': 'algo',
            'technique': 'algo', 'scheme': 'algo', 'procedure': 'algo',
            'model': 'model', 'network': 'net', 'architecture': 'net',
            'splitting': 'split', 'split': 'split',
            'estimation': 'estim', 'estimate': 'estim',
            'classification': 'class', 'classifier': 'class',
            'detection': 'detect', 'detector': 'detect',
            'optimization': 'optim', 'optimizer': 'optim',
            'learning': 'learn', 'learner': 'learn',
            'representation': 'repr', 'feature': 'feat',
            'extraction': 'extract', 'extracting': 'extract',
        }
        for old, new in synonyms.items():
            s = s.replace(old, new)
        # Tokenize + strip common English suffixes
        words = s.split()
        stems = []
        for w in words:
            for suffix in ['ing', 'ed', 'tion', 'ness', 'ment', 'ive', 'er', 'est', 'al', 'ly', 'ic']:
                if w.endswith(suffix) and len(w) > len(suffix) + 1:
                    w = w[:-len(suffix)]
            if w and len(w) > 1:
                stems.append(w)
        return set(stems)

    # Strategy 3: core-algorithm-name match
    # Extract the core excluding (algorithm/method/splitting/model...)
    CORE_STRIP_RE = re.compile(
        r'\b(algorithm|method|approach|technique|scheme|procedure|model|network|'
        r'architecture|learning|classifier|classification|optimization|splitting|split|'
        r'estimation|detection|feature|representation|extraction)\b',
        re.IGNORECASE
    )

    def extract_core(s):
        """Extract the core algorithm name (strip common added words)"""
        s2 = CORE_STRIP_RE.sub(' ', s.lower())
        # Clean extra whitespace
        s2 = re.sub(r'\s+', ' ', s2).strip()
        # Strip leading/trailing punctuation
        s2 = s2.strip('()/,.-_ ')
        return s2

    core1, core2 = extract_core(name1), extract_core(name2)
    if core1 and core2:
        # If core names are exactly equal, score high
        if core1 == core2:
            return 0.9
        # If one core name contains the other
        if core1 in core2 or core2 in core1:
            return 0.85

    # Strategy 4: word-level Jaccard
    set1, set2 = normalize_for_algo(name1), normalize_for_algo(name2)
    if not set1 or not set2:
        return 0.0
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union > 0 else 0.0


# ============================================================================
# Step2: parse mapping-table md -> mapping-table array
# ============================================================================

def parse_mapping_table_to_array(md_path: str, node_type: str) -> list[dict]:
    """
    Parse a mapping-table markdown file; extract information for each row
    (each algorithm category); build the mapping-table array.

    Returned structure:
      [{
        "node_type": str,               # e.g. "16-Feature Extraction Algorithm"
        "alg_class_name": str,           # category name
        "alg_class_description": str,    # category connotation (after cleaning)
        "node_ids": [str, ...],          # list of node_ids
      }, ...]
    """
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    results = []
    content = content.strip()
    if content.startswith("```"):
        lines = content.split("\n")
        content = "\n".join(lines[1:-1] if lines[-1].strip() == "```" else lines[1:])

    md_lines = content.split("\n")
    data_rows = []
    in_table = False

    for line in md_lines:
        line_stripped = line.strip()
        if line_stripped.startswith("|") and "序号" in line_stripped and "node_ids" in line_stripped:
            in_table = True
            continue
        if in_table and line_stripped.startswith("|"):
            if re.match(r"^\|[\s\-:]+\|", line_stripped):
                continue
            cells = [c.strip() for c in line_stripped.strip("|").split("|")]
            data_rows.append(cells)

    for cells in data_rows:
        if len(cells) < 7:
            continue
        # cells[0] = seq
        # cells[1] = category name
        # cells[2] = category connotation
        # cells[3] = induction standard
        # cells[4] = applicability analysis
        # cells[5] = node_names
        # cells[6] = node_ids
        alg_class_name = cells[1].strip()
        alg_class_description_raw = cells[2].strip()
        alg_class_description = _clean_description(alg_class_description_raw)
        node_id_str = cells[6].strip() if len(cells) > 6 else ""

        if node_id_str and node_id_str not in ("（无）", ""):
            node_id_list = re.split(r"[，,、]", node_id_str)
            node_id_list = [nid.strip() for nid in node_id_list if nid.strip()]
        else:
            node_id_list = []

        results.append({
            "node_type": node_type,
            "alg_class_name": alg_class_name,
            "alg_class_description": alg_class_description,
            "node_ids": node_id_list,
        })

    return results


# ============================================================================
# Step3: iterate over the mapping-table array, set node_algorithm_class on each
#         node, and append new induction nodes
# ============================================================================

def process_papers(
    papers: list[dict],
    mapping_arrays: list[list[dict]],
    verbose: bool = True,
) -> tuple[list[dict], dict]:
    """
    Process the 5 mapping-table arrays sequentially; perform induction completion
    on papers.

    Returns: (processed papers, statistics dict)
    """
    # Build case_id -> paper dict index
    paper_index: dict[str, dict] = {}
    for paper in papers:
        case_id = paper.get("case_id", "")
        if case_id:
            paper_index[case_id] = paper

    stats = {
        "total_class_entries": 0,
        "total_node_ids": 0,
        "total_updated": 0,
        "total_new_induction_nodes": 0,
        "skip_no_case_id_in_node_id": 0,
        "skip_case_id_not_found": 0,
        "skip_node_id_not_found": 0,
    }

    for mapping_array in mapping_arrays:
        node_type_label = mapping_array[0]["node_type"] if mapping_array else "?"
        stats["total_class_entries"] += len(mapping_array)

        if verbose:
            print(f"\n{'=' * 60}")
            print(f"[{node_type_label}] {len(mapping_array)} algorithm-category entries in total")

        for entry in mapping_array:
            alg_class_name = entry["alg_class_name"]
            alg_class_description = entry["alg_class_description"]
            node_ids = entry["node_ids"]
            stats["total_node_ids"] += len(node_ids)

            if verbose:
                print(f"\n  Category: {alg_class_name}")
                print(f"    -> contains {len(node_ids)} node_ids")

            if not node_ids:
                if verbose:
                    print(f"    -> node_ids empty; skipping")
                continue

            for node_id in node_ids:
                node_id = str(node_id).strip()
                if not node_id:
                    continue

                # Extract case_id from node_id (prefix, before '_')
                if "_" not in node_id:
                    if verbose:
                        print(f"    -> WARNING: node_id='{node_id}' has no '_'; cannot extract case_id; skipping")
                    stats["skip_no_case_id_in_node_id"] += 1
                    continue

                case_id = node_id.split("_")[0]

                # Locate the corresponding paper
                paper = paper_index.get(case_id)
                if paper is None:
                    if verbose:
                        print(f"    -> WARNING: paper with case_id='{case_id}' not found; skipping node_id='{node_id}'")
                    stats["skip_case_id_not_found"] += 1
                    continue

                nodes_list = paper.get("nodes", [])

                # Locate the original node corresponding to node_id
                original_node = None
                for n in nodes_list:
                    if n.get("node_id") == node_id:
                        original_node = n
                        break

                if original_node is None:
                    if verbose:
                        print(f"    -> WARNING: node_id='{node_id}' not found under case_id='{case_id}'; skipping")
                    stats["skip_node_id_not_found"] += 1
                    continue

                original_node_type = original_node.get("node_type", "")

                # ---------- Step3-3-1: set node_algorithm_class on the original node ----------
                original_node["node_algorithm_class"] = alg_class_name
                stats["total_updated"] += 1

                # ---------- Step3-3-2: append a new induction node at the end of the nodes list ----------
                induction_node = {
                    "node_id": f"{node_id}-Induction",
                    "node_type": f"{original_node_type}-Induction",
                    "node_original_name": alg_class_name,
                    "node_name": alg_class_name,
                    "node_description": alg_class_description,
                    "node_num": None,
                    "node_cite_score": None,
                    "node_cite_count": None,
                    "node_weight": None,
                    "node_id_list": None,
                }
                nodes_list.append(induction_node)
                stats["total_new_induction_nodes"] += 1

                if verbose:
                    print(
                        f"    -> updated node_id='{node_id}' node_algorithm_class='{alg_class_name}', "
                        f"new induction node node_id='{induction_node['node_id']}'"
                    )

    return papers, stats


# ============================================================================
# Step4: mapping-generation completeness audit
# ============================================================================

def audit_completeness(
    papers: list[dict],
    mapping_arrays: list[list[dict]],
    verbose: bool = True,
) -> dict[str, dict]:
    """
    Iterate through the 5 mapping-table arrays in order; audit "disambiguation-induction
    graph JSON":
      N1: count of node_ids in the mapping table that have successfully received
          the node_algorithm_class property
      N2: count of node_ids in the mapping table that have successfully created
          "<node_id>-Induction" induction nodes

    Returns:
      {
        "node_type": {
          "mapping_node_id_count": int,   # total node_ids contained in the mapping table
          "n1_algorithm_class_set": int,   # nodes with node_algorithm_class set
          "n2_induction_node_added": int,  # nodes with induction nodes created
        },
        ...
      }
    """
    # Build all_nodes node_id -> node map (across all papers)
    all_node_map: dict[str, dict] = {}
    for paper in papers:
        for node in paper.get("nodes", []):
            nid = node.get("node_id", "")
            if nid:
                all_node_map[nid] = node

    results = {}
    node_type_labels = ["15-Data Preprocessing Algorithm", "16-Feature Extraction Algorithm",
                         "17-Core Classifier Algorithm", "18-Data Generation Algorithm",
                         "19-Training Optimization Algorithm"]

    print(f"\n{'=' * 70}")
    print("Step4: Mapping-generation completeness audit")
    print(f"{'=' * 70}")
    print(f"{'node_type':<30} {'Mapping-table node_id total':>15} {'N1 (algorithm-class flag)':>15} {'N2 (induction node)':>15}")
    print("-" * 80)

    for mapping_array, node_type_label in zip(mapping_arrays, node_type_labels):
        mapping_node_ids = set()
        for entry in mapping_array:
            for nid in entry["node_ids"]:
                mapping_node_ids.add(str(nid).strip())

        n1_count = 0  # has node_algorithm_class property
        n2_count = 0  # has "<node_id>-Induction" node

        for nid in mapping_node_ids:
            node = all_node_map.get(nid)
            if node is not None:
                if "node_algorithm_class" in node:
                    n1_count += 1
                if f"{nid}-Induction" in all_node_map:
                    n2_count += 1

        results[node_type_label] = {
            "mapping_node_id_count": len(mapping_node_ids),
            "n1_algorithm_class_set": n1_count,
            "n2_induction_node_added": n2_count,
        }

        print(
            f"{node_type_label:<30} {len(mapping_node_ids):>15} "
            f"{n1_count:>15} {n2_count:>15}"
        )

    print("-" * 80)
    total_map_ids = sum(v["mapping_node_id_count"] for v in results.values())
    total_n1 = sum(v["n1_algorithm_class_set"] for v in results.values())
    total_n2 = sum(v["n2_induction_node_added"] for v in results.values())
    print(
        f"{'合计':<30} {total_map_ids:>15} {total_n1:>15} {total_n2:>15}"
    )
    print(f"{'=' * 70}")

    return results


# ============================================================================
# Step5：合规性删减
# ============================================================================

def prune_invalid_nodes(papers: list[dict], verbose: bool = True) -> tuple[list[dict], dict]:
    """
    删除满足以下条件的无效节点：
      1. node_original_name == "Not Mentioned" 且 node_name is None
      2. node_original_name == ""     且 node_name == ""
      3. node_original_name is None  且 node_name is None

    返回：(删减后的 papers, 删除统计 dict)
    """
    stats = {
        "rule1_unmentioned_null": 0,
        "rule2_both_empty": 0,
        "rule3_both_none": 0,
        "total_removed": 0,
        "papers_affected": 0,
    }

    for paper in papers:
        nodes = paper.get("nodes", [])
        original_count = len(nodes)

        filtered = []
        for n in nodes:
            original_name = n.get("node_original_name")
            node_name = n.get("node_name")

            # Rule 1: "Not Mentioned" and null
            if original_name == "Not Mentioned" and node_name is None:
                stats["rule1_unmentioned_null"] += 1
                continue
            # Rule 2: "" and ""
            if original_name == "" and node_name == "":
                stats["rule2_both_empty"] += 1
                continue
            # Rule 3: null and null
            if original_name is None and node_name is None:
                stats["rule3_both_none"] += 1
                continue

            filtered.append(n)

        removed = original_count - len(filtered)
        if removed > 0:
            paper["nodes"] = filtered
            stats["total_removed"] += removed
            stats["papers_affected"] += 1

    if verbose:
        print(f"\n{'=' * 70}")
        print("Step 5: Conformance-based node removal")
        print(f"{'=' * 70}")
        print(f"  Rule 1 (node_original_name='Not Mentioned' and node_name=null): removed {stats['rule1_unmentioned_null']} nodes")
        print(f"  Rule 2 (node_original_name=''     and node_name=''):   removed {stats['rule2_both_empty']} nodes")
        print(f"  Rule 3 (node_original_name=null    and node_name=null):  removed {stats['rule3_both_none']} nodes")
        print(f"  Total removed: {stats['total_removed']} nodes, affecting {stats['papers_affected']} papers")
        print(f"{'=' * 70}")

    return papers, stats


# ============================================================================
# Step 6: build the output path
# ============================================================================

def build_output_path(input_json_path: str, output_base_dir: str) -> str:
    r"""
    Dynamically derive the output path from the input JSON filename.
    Input:  "[225KHNN8][ZZZRPFBV]合并节点_消歧.json"
    Output: r"{output_base_dir}\[225KHNN8][ZZZRPFBV]合并节点_消歧_归纳.json"
    (appends the "_归纳" suffix)
    """
    basename = os.path.basename(input_json_path)
    name_without_ext = os.path.splitext(basename)[0]
    output_name = f"{name_without_ext}_归纳.json"
    return os.path.join(output_base_dir, output_name)


# ============================================================================
# HTML report generation
# ============================================================================

def generate_html_report(
    mapping_arrays: list[list[dict]],
    nodes_json_v2: list[dict],
    output_json_path: str,
    output_base_dir: str,
    audit_results: dict[str, dict] | None = None,
) -> str:
    """
    Generate the HTML report for induction processing.
    """
    from collections import defaultdict

    all_node_map: dict[str, dict] = {}
    for paper in nodes_json_v2:
        for node in paper.get("nodes", []):
            nid = node.get("node_id", "")
            if nid:
                all_node_map[nid] = node

    node_type_labels = ["15-Data Preprocessing Algorithm", "16-Feature Extraction Algorithm",
                         "17-Core Classifier Algorithm", "18-Data Generation Algorithm",
                         "19-Training Optimization Algorithm"]

    # Statistics
    total_induction_nodes = sum(
        sum(len(e["node_ids"]) for e in arr) for arr in mapping_arrays
    )

    alg_type_detail_sections = ""
    stats_rows = ""
    for mapping_array, node_type_label in zip(mapping_arrays, node_type_labels):
        if not mapping_array:
            continue

        # Group by alg_class_name
        class_groups: dict[str, list[dict]] = defaultdict(list)
        for entry in mapping_array:
            for nid in entry["node_ids"]:
                class_groups[entry["alg_class_name"]].append({
                    "nid": nid,
                    "desc": entry["alg_class_description"],
                })

        rows_html = ""
        seq = 0
        for alg_class_name in sorted(class_groups.keys()):
            items = class_groups[alg_class_name]
            for item in items:
                seq += 1
                nid = item["nid"]
                node = all_node_map.get(nid, {})
                orig_name = node.get("node_name", "") or node.get("node_original_name", "")
                induction_nid = f"{nid}-Induction"
                has_induction = induction_nid in all_node_map

                rows_html += f"""
        <tr class="{'row-alt' if seq % 2 == 0 else ''}">
          <td>{seq}</td>
          <td class="alg-class">{alg_class_name}</td>
          <td class="node-id">{nid}</td>
          <td class="node-id">{induction_nid}</td>
          <td class="{'pass' if has_induction else 'fail'}">
            {'✓' if has_induction else '✗'}
          </td>
          <td>{orig_name or '（无）'}</td>
          <td class="alg-desc" title="{item['desc']}">
            {item['desc'][:60] + '…' if len(item['desc']) > 60 else item['desc'] or '（无）'}
          </td>
        </tr>"""

        alg_type_detail_sections += f"""
    <!-- ========== {node_type_label} ========== -->
    <div class="section">
      <h2 id="type{node_type_label[:2]}">🔹 {node_type_label}（{len(items) if mapping_array else 0} 条归纳节点）</h2>
      <table>
        <thead>
          <tr>
            <th>序号</th>
            <th>算法类别名称</th>
            <th>原始节点 ID</th>
            <th>归纳节点 ID</th>
            <th>归纳节点已生成</th>
            <th>原始节点名称</th>
            <th>类别内涵</th>
          </tr>
        </thead>
        <tbody>
          {rows_html}
        </tbody>
      </table>
    </div>"""

        class_count = len(class_groups)
        audit = (audit_results or {}).get(node_type_label, {})
        audit_row = ""
        if audit:
            audit_row = f"""
        <tr style="background:#e8f5e9">
          <td colspan="7">
            映射生成完备性审查: 映射表 node_id 总数={audit.get('mapping_node_id_count',0)} |
            N1(算法类标记)={audit.get('n1_algorithm_class_set',0)} |
            N2(归纳节点)={audit.get('n2_induction_node_added',0)}
          </td>
        </tr>"""
        stats_rows += f"""
        <tr>
          <td>{node_type_label}</td>
          <td>{class_count}</td>
          <td>{sum(len(v) for v in class_groups.values())}</td>
          <td>{audit.get('mapping_node_id_count','-')}</td>
          <td>{audit.get('n1_algorithm_class_set','-')}</td>
          <td>{audit.get('n2_induction_node_added','-')}</td>
        </tr>{audit_row}"""

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>归纳补全报告 V9</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: "Microsoft YaHei", "Segoe UI", Arial, sans-serif;
          font-size: 14px; background: #f5f7fa; color: #333;
          line-height: 1.6; }}
  .container {{ max-width: 1600px; margin: 0 auto; padding: 20px; }}
  h1 {{ text-align: center; color: #2c3e50; margin-bottom: 8px; font-size: 22px; }}
  .subtitle {{ text-align: center; color: #888; font-size: 12px; margin-bottom: 24px; }}
  .summary-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
                   gap: 16px; margin-bottom: 32px; }}
  .stat-card {{ background: #fff; border-radius: 10px; padding: 18px 22px;
                box-shadow: 0 2px 8px rgba(0,0,0,.07); }}
  .stat-card .label {{ color: #888; font-size: 12px; text-transform: uppercase;
                        letter-spacing: .5px; margin-bottom: 4px; }}
  .stat-card .value {{ font-size: 28px; font-weight: 700; color: #2c3e50; }}
  .stat-card.highlight .value {{ color: #e67e22; }}
  h2 {{ color: #34495e; font-size: 16px; border-left: 4px solid #3498db;
        padding-left: 10px; margin: 28px 0 14px; }}
  .section {{ background: #fff; border-radius: 10px; padding: 20px 24px;
              margin-bottom: 24px; box-shadow: 0 2px 8px rgba(0,0,0,.07); }}
  table {{ width: 100%; border-collapse: collapse; font-size: 13px;
           table-layout: auto; }}
  thead th {{ background: #34495e; color: #fff; padding: 10px 8px;
              text-align: left; font-weight: 600; white-space: nowrap; }}
  tbody td {{ padding: 9px 8px; border-bottom: 1px solid #eef0f3;
              vertical-align: top; word-break: break-all; }}
  tbody tr:last-child td {{ border-bottom: none; }}
  tbody tr:hover {{ background: #f8f9fb; }}
  .row-alt td {{ background: #fafbfc; }}
  .node-id {{ font-family: Consolas, monospace; font-size: 12px;
              color: #c0392b; white-space: nowrap; }}
  .alg-class {{ font-weight: 600; color: #2980b9; white-space: nowrap; }}
  .alg-desc {{ color: #555; font-size: 12px; }}
  .pass {{ color: #27ae60; font-weight: bold; }}
  .fail {{ color: #e74c3c; font-weight: bold; }}
  .nav {{ position: sticky; top: 0; background: #2c3e50; padding: 10px 20px;
           border-radius: 8px; margin-bottom: 24px; z-index: 100; }}
  .nav a {{ color: #ecf0f1; text-decoration: none; margin-right: 18px;
             font-size: 13px; }}
  .nav a:hover {{ color: #e67e22; }}
  .footer {{ text-align: center; color: #aaa; font-size: 12px;
              margin-top: 32px; padding-top: 16px; border-top: 1px solid #e0e0e0; }}
</style>
</head>
<body>
<div class="container">
  <h1>📊 归纳补全处理报告 V9</h1>
  <p class="subtitle">
    输入: {os.path.basename(output_json_path)}<br>
    生成时间: {time.strftime('%Y-%m-%d %H:%M:%S')}
  </p>

  <!-- 统计卡片 -->
  <div class="summary-grid">
    <div class="stat-card highlight">
      <div class="label">总归纳节点数</div>
      <div class="value">{total_induction_nodes}</div>
    </div>
    <div class="stat-card">
      <div class="label">算法类别数量</div>
      <div class="value">{sum(len(arr) for arr in mapping_arrays)}</div>
    </div>
    <div class="stat-card">
      <div class="label">涉及原始节点数</div>
      <div class="value">{sum(sum(len(e['node_ids']) for e in arr) for arr in mapping_arrays)}</div>
    </div>
    <div class="stat-card">
      <div class="label">文献数量</div>
      <div class="value">{len(nodes_json_v2)}</div>
    </div>
  </div>

  <!-- 分类统计表（含完备性审查结果） -->
  <div class="section">
    <h2>📋 各算法类别统计 &amp; 映射生成完备性审查</h2>
    <table>
      <thead>
        <tr><th>算法类别</th><th>类别条目数</th><th>node_id 总数</th>
            <th>映射表 node_id 总数</th><th>N1(算法类标记)</th><th>N2(归纳节点)</th></tr>
      </thead>
      <tbody>{stats_rows}
      </tbody>
    </table>
  </div>

  <!-- 快速导航 -->
  <div class="nav">
    <a href="#top">↑ 顶部</a>
    {"".join(f'<a href="#type{label[:2]}">{label[:2]}</a>' for label in node_type_labels)}
  </div>

  <!-- 详细表格 -->
  <div id="top"></div>
  {alg_type_detail_sections}

  <div class="footer">
    由 zotero_knowledge_graph_extractor_归纳生成_v9.py 自动生成
  </div>
</div>
</body>
</html>"""

    html_path = os.path.join(
        output_base_dir,
        os.path.basename(output_json_path).replace(".json", "_归纳报告.html")
    )
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  -> HTML 报告已生成: {html_path}")
    return html_path


# ============================================================================
# Main flow
# ============================================================================

def main():
    print("=" * 70)
    print("Algorithm-node induction completion script V9")
    print("=" * 70)

    # ========================================================================
    # Step 0: Print explicit path configuration (verified at startup)
    # ========================================================================
    print("\n[Step 0] Explicit path configuration (defined in the user-config section)")
    print("-" * 70)
    for name, path in PATH_CONFIG:
        exist_mark = "OK " if os.path.exists(path) else "MISS"
        print(f"  [{exist_mark}] {name}:")
        print(f"         {path}")
    print("-" * 70)
    print("  -> To modify, edit INPUT_JSON_PATH / MAPPING_TABLE_PATHS / OUTPUT_BASE_DIR at the top of the file\n")

    # ========================================================================
    # Step 1: read input files
    # ========================================================================
    print(f"[Step 1] Reading disambiguation graph JSON: {INPUT_JSON_PATH}")
    if not os.path.exists(INPUT_JSON_PATH):
        raise FileNotFoundError(f"Input file does not exist: {INPUT_JSON_PATH}")
    papers = load_json(INPUT_JSON_PATH)
    print(f"  -> Loaded {len(papers)} papers")
    total_original_nodes = sum(len(p.get("nodes", [])) for p in papers)
    print(f"  -> Total original nodes: {total_original_nodes}")

    # ========================================================================
    # Step 1b: mapping-table file check (using explicitly configured paths)
    # ========================================================================
    print(f"\n[Step 1b] Mapping-table file check:")
    for key, path in MAPPING_TABLE_PATHS.items():
        exist = "OK" if os.path.exists(path) else "MISSING"
        print(f"  [{key}] {exist}: {os.path.basename(path)}")

    # ========================================================================
    # Step 2: parse 5 mapping-table md files -> mapping-table arrays
    # ========================================================================
    print(f"\n{'=' * 70}")
    print("Step 2: Parse mapping-table md -> mapping arrays")
    print(f"{'=' * 70}")

    node_type_labels = {
        "15": "15-Data Preprocessing Algorithm",
        "16": "16-Feature Extraction Algorithm",
        "17": "17-Core Classifier Algorithm",
        "18": "18-Data Generation Algorithm",
        "19": "19-Training Optimization Algorithm",
    }

    mapping_arrays: list[list[dict]] = []
    for key in ["15", "16", "17", "18", "19"]:
        path = MAPPING_TABLE_PATHS[key]
        node_type = node_type_labels[key]
        if os.path.exists(path):
            arr = parse_mapping_table_to_array(path, node_type)
            mapping_arrays.append(arr)
            total_ids = sum(len(e["node_ids"]) for e in arr)
            print(f"  [{node_type}] -> {len(arr)} category entries, {total_ids} node_ids")
        else:
            print(f"  [{node_type}] -> file missing, skipping")
            mapping_arrays.append([])

    # ========================================================================
    # Step 3: iterate mapping arrays, add node attributes and append induction nodes
    # ========================================================================
    print(f"\n{'=' * 70}")
    print("Step 3: Iterate mapping arrays -> add node_algorithm_class + new induction nodes")
    print(f"{'=' * 70}")

    papers, process_stats = process_papers(papers, mapping_arrays, verbose=True)

    print(f"\n{'=' * 60}")
    print("Step 3 statistics:")
    print(f"  Total category entries: {process_stats['total_class_entries']}")
    print(f"  Total node_ids: {process_stats['total_node_ids']}")
    print(f"  Added node_algorithm_class attributes: {process_stats['total_updated']}")
    print(f"  Added new induction nodes: {process_stats['total_new_induction_nodes']}")
    print(f"  Skipped (no '_' in node_id): {process_stats['skip_no_case_id_in_node_id']}")
    print(f"  Skipped (case_id not found): {process_stats['skip_case_id_not_found']}")
    print(f"  Skipped (node_id not found): {process_stats['skip_node_id_not_found']}")

    # ========================================================================
    # Step 4: mapping-generation completeness audit
    # ========================================================================
    print(f"\n{'=' * 70}")
    print("Step 4: Mapping-generation completeness audit")
    print(f"{'=' * 70}")
    audit_results = audit_completeness(papers, mapping_arrays, verbose=True)

    # ========================================================================
    # Step 5: conformance-based node removal
    # ========================================================================
    papers, prune_stats = prune_invalid_nodes(papers, verbose=True)

    # ========================================================================
    # Step 6: self-audit + automatic gap filling
    # ========================================================================
    print(f"\n{'=' * 70}")
    print("Step 6: Self-audit -- check node_algorithm_class coverage for each algorithm type in the output JSON")
    print("(only counts non-Induction nodes, i.e. original algorithm nodes)")
    print(f"{'=' * 70}")

    # Build a node_id -> node index for the output JSON
    out_node_index: dict[str, dict] = {}
    for paper in papers:
        for node in paper.get("nodes", []):
            nid = node.get("node_id", "")
            if nid:
                out_node_index[nid] = node

    ALGO_TYPE_LABELS = [
        ("15", "15-Data Preprocessing Algorithm"),
        ("16", "16-Feature Extraction Algorithm"),
        ("17", "17-Core Classifier Algorithm"),
        ("18", "18-Data Generation Algorithm"),
        ("19", "19-Training Optimization Algorithm"),
    ]

    def run_audit(out_node_index, ALGO_TYPE_LABELS):
        """Audit the output JSON; returns (results list, failed types list)"""
        results = []
        failed_types = []
        for key, label in ALGO_TYPE_LABELS:
            total = 0
            with_class = 0
            without_class_ids = []
            for nid, node in out_node_index.items():
                if node.get("node_type") == label:
                    total += 1
                    if "node_algorithm_class" in node:
                        with_class += 1
                    else:
                        without_class_ids.append(nid)
            match_str = "OK" if total == with_class else "FAIL"
            results.append((label, total, with_class, without_class_ids, match_str))
            if match_str == "FAIL":
                failed_types.append((label, without_class_ids))
        return results, failed_types

    # ---- First audit round ----
    print()
    print(f"{'node_type':<30} {'original nodes':>12} {'with node_algorithm_class':>20}")
    print("-" * 65)

    first_results, failed_types = run_audit(out_node_index, ALGO_TYPE_LABELS)
    for label, total, with_class, without_class_ids, match_str in first_results:
        print(f"  {label:<28} {total:>12} {with_class:>20}  [{match_str}]")
        if match_str == "FAIL":
            for nid in without_class_ids[:10]:
                print(f"       - {nid}")
            if len(without_class_ids) > 10:
                print(f"       ... {len(without_class_ids) - 10} more")

    print("-" * 65)

    if not failed_types:
        print("  [PASS] All original algorithm nodes include the node_algorithm_class attribute")
    else:
        total_missing = sum(len(ids) for _, ids in failed_types)
        print(f"  [FAIL] {total_missing} nodes are missing node_algorithm_class; attempting automatic gap filling...")

        # ---- Automatic gap filling ----
        # Phase 1: build a case_id -> paper dict index
        paper_index: dict[str, dict] = {}
        for paper in papers:
            case_id = paper.get("case_id", "")
            if case_id:
                paper_index[case_id] = paper

        # Phase 2: extend the mapping-table index; also build a node_name -> category info index
        # To do this we need to load the disambiguation input JSON (for reading node_name)
        disambig_papers_for_fix = load_json(INPUT_JSON_PATH)

        mapping_nid_to_info: dict[str, tuple[str, str]] = {}
        mapping_name_to_info: dict[str, tuple[str, str]] = {}  # node_name -> (class, desc)
        for mapping_array in mapping_arrays:
            for entry in mapping_array:
                alg_class_name = entry["alg_class_name"]
                alg_class_description = entry["alg_class_description"]
                for nid in entry["node_ids"]:
                    nid = str(nid).strip()
                    if nid:
                        mapping_nid_to_info[nid] = (alg_class_name, alg_class_description)
                # Also index by node_name
                for nid in entry["node_ids"]:
                    nid = str(nid).strip()
                    if nid:
                        # Find the node_name corresponding to this nid in the disambiguation input JSON
                        for p in disambig_papers_for_fix:
                            for n in p.get("nodes", []):
                                if n.get("node_id") == nid:
                                    node_name = n.get("node_name", "")
                                    if node_name:
                                        mapping_name_to_info[node_name] = (alg_class_name, alg_class_description)
                                    break

        fixed_count = 0
        unfixable = []

        for label, missing_ids in failed_types:
            for nid in missing_ids:
                info = None
                reason = ""

                # Strategy A: direct lookup in the mapping-table node_id index
                if nid in mapping_nid_to_info:
                    info = mapping_nid_to_info[nid]
                    reason = "mapping-table node_id match"
                else:
                    # Strategy B: find node_name from the disambiguation input via node_id,
                    #             then look it up in the mapping table by node_name
                    for p in disambig_papers_for_fix:
                        for n in p.get("nodes", []):
                            if n.get("node_id") == nid:
                                node_name = n.get("node_name", "")
                                if node_name and node_name in mapping_name_to_info:
                                    info = mapping_name_to_info[node_name]
                                    reason = f"mapping-table node_name exact match ('{node_name}')"
                                else:
                                    # Strategy C: fuzzy match
                                    best_match = None
                                    best_score = 0
                                    for mapped_name, mapped_info in mapping_name_to_info.items():
                                        score = _fuzzy_name_match(node_name, mapped_name)
                                        if score > best_score and score >= 0.6:
                                            best_score = score
                                            best_match = mapped_info
                                    if best_match is not None:
                                        info = best_match
                                        reason = f"fuzzy match: '{node_name}' -> '{node_name}' ({best_score:.0%} similar)"
                                break
                        if info:
                            break

                if info is None:
                    unfixable.append((nid, label, f"not found in mapping table and cannot be matched by node_name"))
                    continue

                alg_class_name, alg_class_description = info

                # Locate the corresponding paper and node
                if "_" not in nid:
                    unfixable.append((nid, label, "node_id does not contain '_' so case_id cannot be extracted"))
                    continue
                case_id = nid.split("_")[0]
                paper = paper_index.get(case_id)
                if paper is None:
                    unfixable.append((nid, label, f"case_id='{case_id}' not found"))
                    continue

                nodes_list = paper.get("nodes", [])
                original_node = None
                for n in nodes_list:
                    if n.get("node_id") == nid:
                        original_node = n
                        break
                if original_node is None:
                    unfixable.append((nid, label, "node not found in the paper"))
                    continue

                # Add node_algorithm_class attribute
                original_node["node_algorithm_class"] = alg_class_name
                out_node_index[nid] = original_node  # Update index

                # Check whether the -Induction node already exists
                ind_nid = f"{nid}-Induction"
                if ind_nid not in out_node_index:
                    original_node_type = original_node.get("node_type", "")
                    induction_node = {
                        "node_id": ind_nid,
                        "node_type": f"{original_node_type}-Induction",
                        "node_original_name": alg_class_name,
                        "node_name": alg_class_name,
                        "node_description": alg_class_description,
                        "node_num": None,
                        "node_cite_score": None,
                        "node_cite_count": None,
                        "node_weight": None,
                        "node_id_list": None,
                    }
                    nodes_list.append(induction_node)
                    out_node_index[ind_nid] = induction_node  # Update index

                fixed_count += 1

        print()
        if fixed_count > 0:
            print(f"  Automatic gap-filling done: fixed {fixed_count} nodes")

        # ---- Second audit round ----
        print()
        print("=" * 65)
        print("Step 6b: Re-audit after automatic gap filling")
        print("-" * 65)

        second_results, second_failed = run_audit(out_node_index, ALGO_TYPE_LABELS)
        for label, total, with_class, without_class_ids, match_str in second_results:
            print(f"  {label:<28} {total:>12} {with_class:>20}  [{match_str}]")
            if match_str == "FAIL":
                for nid in without_class_ids[:10]:
                    print(f"       - {nid}")
                if len(without_class_ids) > 10:
                    print(f"       ... {len(without_class_ids) - 10} more")

        print("-" * 65)

        if not second_failed:
            print("  [RESOLVED] All issues resolved by automatic gap filling")
        else:
            print("  [UNRESOLVED] The following issues remain and require manual intervention:")
            for nid, label, reason in unfixable:
                print(f"    - {nid} ({label}): {reason}")

    # ========================================================================
    # Step 7: save the final disambiguated-induced graph JSON
    # ========================================================================
    output_path = build_output_path(INPUT_JSON_PATH, OUTPUT_BASE_DIR)
    print(f"\n{'=' * 70}")
    print(f"Step 7: Save the final disambiguated-induced graph JSON: {output_path}")
    save_json(papers, output_path)
    print(f"  -> Saved (all processing complete, graph is up to date)")

    # ========================================================================
    # Step 8: generate HTML report
    # ========================================================================
    print(f"\n{'=' * 70}")
    print("Step 8: Generate HTML induction report...")
    generate_html_report(mapping_arrays, papers, output_path, OUTPUT_BASE_DIR, audit_results)

    # ========================================================================
    # Statistics verification
    # ========================================================================
    total_nodes_v2 = sum(len(p.get("nodes", [])) for p in papers)
    print(f"\n{'=' * 70}")
    print("Statistics verification:")
    print(f"  Papers: {len(papers)} (unchanged)")
    print(f"  Total nodes before processing: {total_original_nodes}")
    print(f"  Step 5 (conformance removal) removed nodes: {prune_stats['total_removed']}")
    print(f"  Step 3 (induction nodes generated) added nodes: {process_stats['total_new_induction_nodes']}")
    print(f"  Final total nodes: {total_nodes_v2}")
    print(f"  Node-count change check: {total_original_nodes} + {process_stats['total_new_induction_nodes']} - {prune_stats['total_removed']} = {total_original_nodes + process_stats['total_new_induction_nodes'] - prune_stats['total_removed']} (actual: {total_nodes_v2})")
    print(f"\n{'=' * 70}")
    print(f"All complete! Output file: {output_path}")
    print("=" * 70)


if __name__ == "__main__":
    main()
