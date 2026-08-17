# -*- coding: utf-8 -*-
"""
Literature knowledge-graph induction-mapping conformance-audit script v9
========================================================================
Functions:
  1. Mapping-count audit: compare the node_id count of each algorithm-type node in the
     graph JSON against the total node_ids in the mapping-table md
  2. Mapping-category audit: compare the element counts of the "category name" column
     in the mapping-table md against the big-table md
  3. Generate the conformance-audit report md

Inputs:
  - Graph JSON: A1-节点合并_消歧/[...].json
  - Mapping-table md: A2-节点合并_消歧_归纳/归纳清单表/[...]*节点映射表.md
  - Big-table md:   A2-节点合并_消歧_归纳/归纳清单表/[...]*节点大表.md

Output:
  - Conformance-audit report md: A2-节点合并_消歧_归纳/[<case_id1>][<case_id2>]合并节点_归纳映射_合规性审查.md
"""

import os
import re
import json


# ============================================================================
# Configuration
# ============================================================================

# Input 1: graph JSON (after disambiguation + conformance audit)
INPUT_GRAPH_PATH = r"./data/02_consensus_graph/[2277EAKD][ZZZRPFBV]合并节点_规范性审查_合并_规范性审查_消歧_规范性审查.json"

# Input 2: 5 mapping-table md files
MAPPING_TABLE_PATHS = {
    "15": r"./data/03_induction/归纳清单表/[2277EAKD][ZZZRPFBV]合并节点_规范性审查_合并_规范性审查_消歧_规范性审查_归纳_15节点映射表_二次处理.md",
    "16": r"./data/03_induction/归纳清单表/[2277EAKD][ZZZRPFBV]合并节点_规范性审查_合并_规范性审查_消歧_规范性审查_归纳_16节点映射表_二次处理.md",
    "17": r"./data/03_induction/归纳清单表/[2277EAKD][ZZZRPFBV]合并节点_规范性审查_合并_规范性审查_消歧_规范性审查_归纳_17节点映射表_二次处理.md",
    "18": r"./data/03_induction/归纳清单表/[2277EAKD][ZZZRPFBV]合并节点_规范性审查_合并_规范性审查_消歧_规范性审查_归纳_18节点映射表_二次处理.md",
    "19": r"./data/03_induction/归纳清单表/[2277EAKD][ZZZRPFBV]合并节点_规范性审查_合并_规范性审查_消歧_规范性审查_归纳_19节点映射表_二次处理.md",
}

# Input 3: 5 big-table md files
BIG_TABLE_PATHS = {
    "15": r"./data/03_induction/归纳清单表/[2277EAKD][ZZZRPFBV]合并节点_规范性审查_合并_规范性审查_消歧_规范性审查_归纳_15节点大表.md",
    "16": r"./data/03_induction/归纳清单表/[2277EAKD][ZZZRPFBV]合并节点_规范性审查_合并_规范性审查_消歧_规范性审查_归纳_16节点大表.md",
    "17": r"./data/03_induction/归纳清单表/[2277EAKD][ZZZRPFBV]合并节点_规范性审查_合并_规范性审查_消歧_规范性审查_归纳_17节点大表.md",
    "18": r"./data/03_induction/归纳清单表/[2277EAKD][ZZZRPFBV]合并节点_规范性审查_合并_规范性审查_消歧_规范性审查_归纳_18节点大表.md",
    "19": r"./data/03_induction/归纳清单表/[2277EAKD][ZZZRPFBV]合并节点_规范性审查_合并_规范性审查_消歧_规范性审查_归纳_19节点大表.md",
}

# Output directory
OUTPUT_DIR = r"./data/03_induction"

# Algorithm-type node_type definitions
ALGO_NODE_TYPES = {
    "15": "15-Data Preprocessing Algorithm",
    "16": "16-Feature Extraction Algorithm",
    "17": "17-Core Classifier Algorithm",
    "18": "18-Data Generation Algorithm",
    "19": "19-Training Optimization Algorithm",
}


# ============================================================================
# Helper functions
# ============================================================================

def read_json(path: str) -> list[dict]:
    """Read a JSON file"""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def read_file(path: str) -> str:
    """Read a text file"""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def parse_mapping_table(content: str) -> tuple[list[str], list[str]]:
    """
    Parse the mapping-table md; extract the category-name list and all node_id lists.
    Returns: (category-name list, all-node_id list)
    """
    lines = content.split("\n")
    category_names = []
    all_node_ids = []

    for line in lines:
        line = line.strip()
        # Skip non-table rows
        if not line.startswith("|") or line.startswith("|---"):
            continue
        # Parse table columns
        parts = [p.strip() for p in line.split("|")]
        # Filter empty columns (leading/trailing empty columns)
        parts = [p for p in parts if p]
        if len(parts) < 3:
            continue
        # First column is sequence number (pure digits); second column is the category name
        # Determine whether the first column is a sequence number (pure digits)
        try:
            int(parts[0])
        except ValueError:
            continue  # Skip header rows, etc.
        category_name = parts[1]
        category_names.append(category_name)

        # node_ids are in the last column
        if len(parts) >= 7:
            ids_str = parts[-1]
            # Split by comma; strip whitespace
            ids = [i.strip() for i in ids_str.split(",") if i.strip()]
            all_node_ids.extend(ids)

    return category_names, all_node_ids


def parse_big_table(content: str) -> list[str]:
    """
    Parse the big-table md; extract all category names.
    Returns: category-name list
    """
    lines = content.split("\n")
    category_names = []

    for line in lines:
        line = line.strip()
        # Skip non-table rows
        if not line.startswith("|") or line.startswith("|---"):
            continue
        # Parse table columns
        parts = [p.strip() for p in line.split("|")]
        # Filter empty columns
        parts = [p for p in parts if p]
        if len(parts) < 3:
            continue
        # First column is sequence number (pure digits); second column is the category name
        try:
            int(parts[0])
        except ValueError:
            continue  # Skip header rows
        category_name = parts[1]
        category_names.append(category_name)

    return category_names


# ============================================================================
# Main audit logic
# ============================================================================

def audit_mapping_quantity(papers: list[dict]) -> dict:
    """
    1. Mapping-quantity audit
    Returned structure:
    {
        "15": {"N": int, "NM": int, "status": str, "non_map_ids": list},
        ...
    }
    """
    results = {}

    for idx in ["15", "16", "17", "18", "19"]:
        node_type = ALGO_NODE_TYPES[idx]

        # 1-1: count node_ids of the given node_type from the graph JSON
        node_ids_in_graph = []
        for paper in papers:
            for node in paper.get("nodes", []):
                if node.get("node_type") == node_type:
                    node_ids_in_graph.append(node["node_id"])

        # 1-2: read node_ids from the mapping table
        mapping_path = MAPPING_TABLE_PATHS[idx]
        content = read_file(mapping_path)
        _, node_ids_in_map = parse_mapping_table(content)
        # Deduplicate
        node_ids_in_map_unique = list(set(node_ids_in_map))

        N = len(node_ids_in_graph)
        NM = len(node_ids_in_map_unique)
        status = "fully covered" if N == NM else "not fully covered"

        # 1-5: find unmatched node_ids
        non_map_ids = []
        if status == "not fully covered":
            map_set = set(node_ids_in_map_unique)
            for nid in node_ids_in_graph:
                if nid not in map_set:
                    non_map_ids.append(nid)

        results[idx] = {
            "node_type": node_type,
            "N": N,
            "NM": NM,
            "status": status,
            "non_map_ids": non_map_ids,
            "graph_ids": node_ids_in_graph,
            "map_ids": node_ids_in_map_unique,
        }

    return results


def audit_mapping_category() -> dict:
    """
    2. Mapping-category audit
    Returned structure:
    {
        "15": {"A": int, "B": int, "status": str, "non_map_names": list},
        ...
    }
    """
    results = {}

    for idx in ["15", "16", "17", "18", "19"]:
        # 2-1: read category names from the mapping table
        mapping_path = MAPPING_TABLE_PATHS[idx]
        content_map = read_file(mapping_path)
        names_in_map, _ = parse_mapping_table(content_map)

        # 2-2: read category names from the big table
        big_path = BIG_TABLE_PATHS[idx]
        content_big = read_file(big_path)
        names_in_big = parse_big_table(content_big)

        A = len(names_in_map)
        B = len(names_in_big)
        status = "fully covered" if A == B else "not fully covered"

        # 2-5: find unmatched category names (in mapping table but not in big table)
        non_map_names = []
        if status == "not fully covered":
            big_set = set(names_in_big)
            for name in names_in_map:
                if name not in big_set:
                    non_map_names.append(name)

        results[idx] = {
            "node_type": ALGO_NODE_TYPES[idx],
            "A": A,
            "B": B,
            "status": status,
            "non_map_names": non_map_names,
            "map_names": names_in_map,
            "big_names": names_in_big,
        }

    return results


# ============================================================================
# Report generation
# ============================================================================

def extract_case_ids_from_path(json_path: str) -> tuple[str, str]:
    """Extract case_id1 and case_id2 from the graph JSON path."""
    # Filename format: [225KHNN8][ZZZRPFBV]merge节点_规范性audit_消歧_规范性audit.json
    basename = os.path.basename(json_path)
    # Remove extension
    name_without_ext = os.path.splitext(basename)[0]
    # Extract content inside []
    ids = re.findall(r'\[([A-Z0-9]+)\]', name_without_ext)
    if len(ids) >= 2:
        return ids[0], ids[1]
    return "unknown", "unknown"


def generate_report(
    qty_results: dict,
    cat_results: dict,
    case_id1: str,
    case_id2: str
) -> str:
    """Generate the conformance-audit report in MD format."""

    lines = []
    lines.append(f"# Induction Mapping Conformance-Audit Report")
    lines.append(f"")
    lines.append(f"**Audit Target**: {case_id1} + {case_id2}")
    lines.append(f"")
    lines.append(f"---")
    lines.append("")

    # ============================================================
    # 1. Mapping-quantity audit
    # ============================================================
    lines.append("## 1. Mapping-Quantity Audit")
    lines.append("")
    lines.append(
        "**Audit Logic**: compare the total node_id count of each algorithm-type node "
        "(node_type 15~19) in the graph JSON against the total element count in the "
        "corresponding mapping-table md's `node_ids` column."
    )
    lines.append("")

    for idx in ["15", "16", "17", "18", "19"]:
        r = qty_results[idx]
        node_type = r["node_type"]
        N = r["N"]
        NM = r["NM"]
        status = r["status"]

        # Simplified display: strip the node_type number prefix
        short_name = node_type.split("-", 1)[-1]

        lines.append(f"### {idx}-{short_name}")
        lines.append("")
        lines.append(f"- Total `node_id` count in graph JSON (`<N_{idx}>`): **{N}**")
        lines.append(f"- Total `node_ids` count in mapping-table md (`<NM_{idx}>`): **{NM}**")
        lines.append(f"- Coverage status: **{status}**")
        lines.append("")

        # Mismatch details
        if status == "not fully covered":
            non_map = r["non_map_ids"]
            lines.append(f"> [WARN] **Not fully covered** -- {len(non_map)} node_ids have no match in the mapping table:")
            for nid in non_map:
                lines.append(f"> - `{nid}`")
            lines.append("")

    lines.append("")
    lines.append("---")
    lines.append("")

    # ============================================================
    # 2. Mapping-category audit
    # ============================================================
    lines.append("## 2. Mapping-Category Audit")
    lines.append("")
    lines.append(
        "**Audit Logic**: compare the element counts of the `category-name` column in the "
        "mapping-table md against the big-table md."
    )
    lines.append("")

    for idx in ["15", "16", "17", "18", "19"]:
        r = cat_results[idx]
        node_type = r["node_type"]
        A = r["A"]
        B = r["B"]
        status = r["status"]

        short_name = node_type.split("-", 1)[-1]

        lines.append(f"### {idx}-{short_name}")
        lines.append("")
        lines.append(f"- Total `category-name` count in big table (`<B_{idx}>`): **{B}**")
        lines.append(f"- Total `category-name` count in mapping table (`<A_{idx}>`): **{A}**")
        lines.append(f"- Coverage status: **{status}**")
        lines.append("")

        # Mismatch details
        if status == "not fully covered":
            non_map = r["non_map_names"]
            lines.append(f"> [WARN] **Not fully covered** -- {len(non_map)} category names have no match in the mapping table:")
            for name in non_map:
                lines.append(f"> - `{name}`")
            lines.append("")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"*Report generation time: automatically generated by `zotero_knowledge_graph_extractor_归纳映射表_合规性审查_v9.py`*")

    return "\n".join(lines)


def build_summary_table(qty_results: dict, cat_results: dict) -> str:
    """Build the summary table (used in the report header)."""
    lines = []
    lines.append("### Audit-Result Summary")
    lines.append("")
    lines.append("| node_type | Graph-node total (N) | Mapping-table node_ids total (NM) | N=NM | Mapping-table category-name count (A) | Big-table category-name count (B) | A=B |")
    lines.append("|-----------|---------------|---------------------|------|-------------------|-----------------|-----|")
    for idx in ["15", "16", "17", "18", "19"]:
        r_q = qty_results[idx]
        r_c = cat_results[idx]
        short = r_q["node_type"].split("-", 1)[-1]
        status_q = "[OK]" if r_q["status"] == "fully covered" else "[FAIL]"
        status_c = "[OK]" if r_c["status"] == "fully covered" else "[FAIL]"
        lines.append(
            f"| {idx}-{short} | {r_q['N']} | {r_q['NM']} | {status_q} | "
            f"{r_c['A']} | {r_c['B']} | {status_c} |"
        )
    lines.append("")
    return "\n".join(lines)


# ============================================================================
# Main program
# ============================================================================

def main():
    print("=" * 60)
    print("  Induction-Mapping Conformance Audit Starting")
    print("=" * 60)

    # 0. Read the graph JSON
    print("\n[Step 0] reading graph JSON ...")
    papers = read_json(INPUT_GRAPH_PATH)
    print(f"  total {len(papers)} papers loaded")

    # Extract case_ids
    case_id1, case_id2 = extract_case_ids_from_path(INPUT_GRAPH_PATH)
    print(f"  case_id1={case_id1}, case_id2={case_id2}")

    # 1. Mapping-quantity audit
    print("\n[Step 1] mapping-quantity audit ...")
    qty_results = audit_mapping_quantity(papers)
    for idx in ["15", "16", "17", "18", "19"]:
        r = qty_results[idx]
        print(
            f"  {r['node_type']}: "
            f"graph N={r['N']}, mapping-table NM={r['NM']}, status={r['status']}"
            + (f", unmatched count={len(r['non_map_ids'])}" if r['status'] == 'not fully covered' else "")
        )

    # 2. Mapping-category audit
    print("\n[Step 2] mapping-category audit ...")
    cat_results = audit_mapping_category()
    for idx in ["15", "16", "17", "18", "19"]:
        r = cat_results[idx]
        print(
            f"  {r['node_type']}: "
            f"big-table B={r['B']}, mapping-table A={r['A']}, status={r['status']}"
            + (f", unmatched count={len(r['non_map_names'])}" if r['status'] == 'not fully covered' else "")
        )

    # 3. Generate the report
    print("\n[Step 3] generating conformance-audit report ...")
    report_parts = []
    report_parts.append("# Induction-Mapping Conformance-Audit Report")
    report_parts.append("")
    report_parts.append(f"**Audit Target**: {case_id1} + {case_id2}")
    report_parts.append(f"")
    report_parts.append("---")
    report_parts.append("")
    report_parts.append(build_summary_table(qty_results, cat_results))
    report_parts.append("")
    report_parts.append("---")
    report_parts.append("")

    # 1. Mapping-quantity audit (detailed)
    report_parts.append("## 1. Mapping-Quantity Audit")
    report_parts.append("")
    for idx in ["15", "16", "17", "18", "19"]:
        r = qty_results[idx]
        node_type = r["node_type"]
        N = r["N"]
        NM = r["NM"]
        status = r["status"]
        short_name = node_type.split("-", 1)[-1]
        report_parts.append(f"### {idx}-{short_name}")
        report_parts.append("")
        report_parts.append(f"- Total `node_id` count in graph JSON (`<N_{idx}>`): **{N}**")
        report_parts.append(f"- Total `node_ids` count in mapping-table md (`<NM_{idx}>`): **{NM}**")
        report_parts.append(f"- Coverage status: **{status}**")
        report_parts.append("")
        if status == "not fully covered":
            non_map = r["non_map_ids"]
            report_parts.append(f"> [WARN] **Not fully covered** -- {len(non_map)} node_ids have no match in the mapping table:")
            for nid in non_map:
                report_parts.append(f"> - `{nid}`")
            report_parts.append("")
    report_parts.append("")
    report_parts.append("---")
    report_parts.append("")

    # 2. Mapping-category audit (detailed)
    report_parts.append("## 2. Mapping-Category Audit")
    report_parts.append("")
    for idx in ["15", "16", "17", "18", "19"]:
        r = cat_results[idx]
        node_type = r["node_type"]
        A = r["A"]
        B = r["B"]
        status = r["status"]
        short_name = node_type.split("-", 1)[-1]
        report_parts.append(f"### {idx}-{short_name}")
        report_parts.append("")
        report_parts.append(f"- Total `category-name` count in big table (`<B_{idx}>`): **{B}**")
        report_parts.append(f"- Total `category-name` count in mapping table (`<A_{idx}>`): **{A}**")
        report_parts.append(f"- Coverage status: **{status}**")
        report_parts.append("")
        if status == "not fully covered":
            non_map = r["non_map_names"]
            report_parts.append(f"> [WARN] **Not fully covered** -- {len(non_map)} category names have no match in the mapping table:")
            for name in non_map:
                report_parts.append(f"> - `{name}`")
            report_parts.append("")
    report_parts.append("")
    report_parts.append("---")
    report_parts.append("")
    report_parts.append(
        f"*Report generation time: automatically generated by `zotero_knowledge_graph_extractor_归纳映射表_合规性审查_v9.py`*"
    )

    report_content = "\n".join(report_parts)

    # Save the report
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_filename = f"[{case_id1}][{case_id2}]合并节点_归纳映射_合规性审查.md"
    output_path = os.path.join(OUTPUT_DIR, output_filename)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report_content)

    print(f"\n[OK] 报告已保存至: {output_path}")
    print("\n" + "=" * 60)
    print("  归纳映射合规性审查 完成")
    print("=" * 60)

    # 控制台print汇总
    print("\n##############  1、映射数量audit  ############")
    for idx in ["15", "16", "17", "18", "19"]:
        r = qty_results[idx]
        print(
            f'"{r["node_type"]}"的映射数量审查：\n'
            f'图谱中node{{}}总数为{r["N"]}，映射表md中node_ids总数为{r["NM"]}，覆盖状态为{r["status"]}。'
        )

    print("\n##############  2、映射类别audit  ############")
    for idx in ["15", "16", "17", "18", "19"]:
        r = cat_results[idx]
        print(
            f'"{r["node_type"]}"的映射类别审查：\n'
            f'大表中类别名称总数为{r["B"]}，映射表中类别名称总数为{r["A"]}，覆盖状态为{r["status"]}。'
        )


if __name__ == "__main__":
    main()
