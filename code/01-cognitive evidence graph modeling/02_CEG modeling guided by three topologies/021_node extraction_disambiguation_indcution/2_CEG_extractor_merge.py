# -*- coding: utf-8 -*-
"""
Literature Knowledge Graph Merge Script v7_merge.py
========================================================================
Functions:
  Merge all per-paper JSON files across the batch directories produced by the v7 extraction process
  into a single, complete JSON structure per paper.

New feature (v2):
  For batch 5 (15-20 Algorithm Nodes), fuse the role-level information from
  node_type="20-Algorithm Node Role-Importance Calibration"'s node_description into the node_description
  of the corresponding paper's nodes 15-19, then remove node 20 from the final output.

  Fusion rules:
    1. Read node 20's calibration info (three supported formats: plain text string, nested dict, prompt-fixed rule)
    2. If plain text: split by "；" into segments, each "{node_id}（{description snippet}）→{role level}"
       Example: "168_16_N1（feature extraction→...）→highest importance"
    3. If nested dict (e.g. {"15": "highest importance", ...}): build the mapping directly from key-value pairs
    4. Extract node_id and role level from each segment
    5. Append "，{role level}" to the end of the corresponding node's (15-19) node_description,
       separated by a Chinese comma
    6. The final output does not include node 20

Input directories (v7_version/):
  - Source prompts (relative path: ./v5_version_prompts/):
    - 00 hyperparameters.md
    - 01-03,08-09 nodes.md
    - 04-07 nodes.md
    - 10-14 nodes.md
    - 15-20 nodes.md
  - Per-batch per-paper JSON directories (relative path: ./output/):
    - hyperparameters-json/                                -> {case_id}.json
    - 01-03_08-09_object_problem_nodes-json/               -> {case_id}.json
    - 04-07_fault_info_nodes-json/                         -> {case_id}.json
    - 10-14_data_resource_nodes-json/                      -> {case_id}.json
    - 15-20_algorithm_nodes-json/                          -> {case_id}.json

Output directories (v7_version/final_merged/A0-node_merged/):
  - [first_case_id][last_case_id]_merged_nodes.json  -> merged result of all papers
  - merged_by_paper/                                -> per-paper independent merged file
  - merge_stats.json                                -> merge statistics

Output JSON format:
  - case_id, paper_title, publish_year, publish_source, cite_count
  - algorithm_hyperparameters, training_config, performance_metrics
  - nodes: sorted by node_type prefix number, nodes 15-19 have fused calibration info, node 20 is removed
  - edges: []

Usage:
  python zotero_knowledge_graph_extractor_v7_merge.py
  python zotero_knowledge_graph_extractor_v7_merge.py --input "./v7_version"   <-- RELATIVE PATH placeholder
"""

import os
import re
import json
import argparse


from pathlib import Path
from typing import Optional


# ============================================================================
# Configuration
# ============================================================================

# Input root directory (RELATIVE PATH placeholder):
# ./output/   <-- RELATIVE PATH: folder containing the per-batch subdirectories
V7_ROOT_DIR = r"./output"

# Per-batch directory configuration (RELATIVE PATH placeholders):
#   ./output/hyperparameters-json/                       <-- RELATIVE PATH
#   ./output/01-03_08-09_object_problem_nodes-json/      <-- RELATIVE PATH (matches 01-03,08-09 nodes.md)
#   ./output/04-07_fault_info_nodes-json/                <-- RELATIVE PATH (matches 04-07 nodes.md)
#   ./output/10-14_data_resource_nodes-json/             <-- RELATIVE PATH (matches 10-14 nodes.md)
#   ./output/15-20_algorithm_nodes-json/                 <-- RELATIVE PATH (matches 15-20 nodes.md)
BATCH_DIRS = [
    {"id": "hyperparam", "name": "Hyperparameters", "subdir": "hyperparameters-json"},
    {"id": "batch1",     "name": "01-03,08-09 Object & Problem Nodes", "subdir": "01-03_08-09_object_problem_nodes-json"},
    {"id": "batch2",     "name": "04-07 Fault Information Nodes",        "subdir": "04-07_fault_info_nodes-json"},
    {"id": "batch3",     "name": "10-14 Data & Resource Nodes",       "subdir": "10-14_data_resource_nodes-json"},
    {"id": "batch4",     "name": "15-20 Algorithm Nodes",         "subdir": "15-20_algorithm_nodes-json"},
]

# case_id mapping: raw numeric ID -> standard number (used as node_id prefix)
# 168->C00168, 169->C00169, 172->C00172, ...
def normalize_case_id(raw_id: str) -> str:
    """Convert a pure-numeric case_id (e.g. 168) to a standard number (e.g. C00168)"""
    s = str(raw_id).strip()
    # Already starts with C; return as-is
    if s.upper().startswith("C"):
        return s
    # Pure numeric; pad to C + 5 digits (zero-pad if shorter)
    try:
        num = int(s)
        return f"C{num:05d}"
    except ValueError:
        return s


# ============================================================================
# Utility Functions
# ============================================================================

# node_id standard format: case_id_prefix + "_" + category number (2 digits) + "_N" + sequence (1-2 digits)
# Example: C00168_11_N5, C00171_15_N1, C00169_19_N3
# Anomalous format the LLM may produce (missing "_N" prefix): e.g. 171_11_5 -> C00171_11_5
_NODE_ID_PATTERN = re.compile(r"^[A-Z]\d{5}_\d{2}_N\d+$")
_NODE_ID_ANOMALY_PATTERN = re.compile(r"^([A-Z]\d{5}_\d{2})_(\d+)$")


def fix_node_id_format(node_id: str) -> str:
    """
    Auto-fix an abnormal node_id format.

    Anomaly: the LLM may produce "C00171_11_5" (missing "_N" prefix),
    which should be corrected to standard format "C00171_11_N5".

    Returns:
      - If the format is correct, returns the original value as-is
      - If an anomaly is detected (trailing number missing "_N"), inserts "_N" and returns the corrected value
    """
    if not node_id:
        return node_id
    if _NODE_ID_PATTERN.match(node_id):
        return node_id
    m = _NODE_ID_ANOMALY_PATTERN.match(node_id)
    if m:
        prefix, num = m.group(1), m.group(2)
        fixed = f"{prefix}_N{num}"
        return fixed
    return node_id


def validate_and_report_node_ids(
    nodes: list[dict],
    case_id: str,
    logger=None,
) -> list[dict]:
    """
    Check the node_id format in the node list and auto-fix abnormal node_ids.

    Rules:
      1. Format is correct (matches C####_##_N#): keep as-is
      2. Missing "_N" prefix (e.g. C00171_11_5): auto-fix to C00171_11_N5
         and append "[node_id auto-corrected]" to the end of node_description
      3. Other unknown abnormal formats: keep the original and emit a warning

    Parameters:
      nodes: list of nodes
      case_id: paper ID (for log output)
      logger: optional print function; defaults to print

    Returns:
      The checked and corrected node list (mutates the objects in-place)
    """
    if logger is None:
        def logger(msg):
            print(msg)

    fixed_count = 0
    for node in nodes:
        old_id = node.get("node_id", "")
        if not old_id:
            continue
        if _NODE_ID_PATTERN.match(old_id):
            continue
        fixed_id = fix_node_id_format(old_id)
        if fixed_id != old_id:
            node["node_id"] = fixed_id
            desc = node.get("node_description") or ""
            suffix = " [node_id auto-corrected]"
            if suffix not in desc:
                node["node_description"] = desc + suffix
            fixed_count += 1
            logger(f"  [node_id format fixed] {old_id} -> {fixed_id}  (paper: {case_id})")

    if fixed_count > 0:
        logger(f"  -> Fixed {fixed_count} abnormal node_ids in total")

    return nodes

def extract_node_order(node_type: str) -> tuple[int, int]:
    """
    Extract the sort order from node_type.
    Returns (category_order, intra_category_order).

    Example: "05-Fault Mode" -> (5, 0)
             "05-Fault Mode" Nth of the same category -> (5, N)
    If the node_type prefix does not exist (e.g. empty string), returns (99, 0)
    """
    if not node_type:
        return (99, 0)
    prefix = node_type.split("-")[0].strip()
    try:
        return (int(prefix), 0)
    except ValueError:
        return (99, 0)


def scan_batch_files(root_dir: str, batch_info: dict) -> dict[str, dict]:
    """
    Scan the specified batch directory and read all JSON files.
    Returns: {case_id: json_data}
    """
    batch_dir = os.path.join(root_dir, batch_info["subdir"])
    result = {}

    if not os.path.exists(batch_dir):
        print(f"  [WARN] Directory does not exist: {batch_dir}")
        return result

    for filename in os.listdir(batch_dir):
        if not filename.endswith(".json"):
            continue
        filepath = os.path.join(batch_dir, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            case_id = data.get("case_id", "")
            if case_id:
                result[case_id] = data
        except (json.JSONDecodeError, IOError) as e:
            print(f"  [WARN] Read failure: {filename} -> {e}")

    return result


def extract_hyperparam_fields(hp_data: dict) -> dict:
    """Extract three core fields from hyperparameter data.

    Two supported structures:
    - Direct fields: hp_data["algorithm_hyperparameters"] (raw extractor output)
    - Nested fields: hp_data["hyperparam"]["algorithm_hyperparameters"] (saved format)
    """
    # Prefer the nested hyperparam (saved format)
    inner = hp_data.get("hyperparam")
    if inner is not None:
        return {
            "algorithm_hyperparameters": inner.get("algorithm_hyperparameters"),
            "training_config": inner.get("training_config"),
            "performance_metrics": inner.get("performance_metrics"),
        }
    # Fallback: read directly from the top level (raw extractor output)
    return {
        "algorithm_hyperparameters": hp_data.get("algorithm_hyperparameters"),
        "training_config": hp_data.get("training_config"),
        "performance_metrics": hp_data.get("performance_metrics"),
    }


# ============================================================================
# Node-20 Calibration Information Fusion
# ============================================================================

def parse_calibration_description(calib_node: dict, case_id: str) -> dict[str, str]:
    """
    Parse the calibration information from node 20 ("20-Algorithm Node Role-Importance Calibration").

    Three supported sources (tried by priority):
      1. node_description text string (standard format): "15（...）→highest importance; ..."
      2. Node 20 itself is a nested dict (e.g. {"15": "highest importance", ...})
      3. The fixed rule specified in the prompt

    Returns: {original node_id: role level}
        Example: {"168_15_N1": "highest importance", "168_16_N1": "medium importance", ...}
    """
    if not calib_node or not isinstance(calib_node, dict):
        return {}

    # ---- Method 1: parse from node_description text string ----
    calib_desc = calib_node.get("node_description") or calib_node.get("Node_description")
    if isinstance(calib_desc, str) and calib_desc.strip():
        result = _parse_calibration_from_text(calib_desc)
        if result:
            return result

    # ---- Method 2: parse from node 20's nested structure ----
    # If node_description is a dict (e.g. {"15": "highest importance", ...})
    # build the mapping directly from key-value pairs using node_original_name's node_id prefix
    if isinstance(calib_desc, dict):
        result = {}
        for k, v in calib_desc.items():
            if not isinstance(k, str) or not isinstance(v, str):
                continue
            # k is the category number ("15" / "16" etc.), v is the role level
            valid_levels = {"highest importance", "medium importance", "not mentioned"}
            if v.strip() in valid_levels:
                result[f"{case_id}_{k}_N1"] = v.strip()
        if result:
            return result

    # ---- Method 3: fixed prompt rule (summary of calibration rules in Section 5) ----
    # When node 20 is entirely unavailable, return empty dict and fall back to prompt default rule
    return {}


def _parse_calibration_from_text(calib_desc: str) -> dict[str, str]:
    """
    Parse the {node_id: importance} mapping from node 20's node_description plain text.
    Supports both Chinese and English punctuation separators: semicolon (；), period (；)
    """
    if not calib_desc or not isinstance(calib_desc, str):
        return {}

    # Tolerance for {}-style: strip inner { and } (handles LLM outputs like "{xxx}")
    calib_desc = calib_desc.replace("{", "").replace("}", "")

    result: dict[str, str] = {}
    valid_levels = {"highest importance", "medium importance", "not mentioned"}

    # Normalize English semicolons to Chinese semicolons for unified processing
    calib_desc = calib_desc.replace(";", "；")
    segments = calib_desc.split("；")

    for seg in segments:
        seg = seg.strip()
        if not seg:
            continue

        # Tolerance for {}-style: strip { and } inside segments
        seg = seg.replace("{", "").replace("}", "")

        # Extract node_id: format is {case_id}_{num}_N{n}, e.g. "168_15_N1"
        m_id = re.match(r"^([A-Za-z0-9_]+)", seg)
        if not m_id:
            continue
        node_id = m_id.group(1).strip()

        # Extract role level: the part after "→" or "->"
        arrow_pos = max(seg.rfind("→"), seg.rfind("->"))
        if arrow_pos == -1:
            continue
        importance = seg[arrow_pos + 1:].strip()
        # Strip trailing punctuation
        importance = importance.rstrip("，。.;,，。！？…—–·～.,;:!?()[]{}（）【】""''\"\"")

        if node_id and importance in valid_levels:
            result[node_id] = importance

    return result


def apply_importance_to_nodes(nodes: list[dict], importance_map: dict[str, str]) -> list[dict]:
    """
    Fuse the role-level information into the node_description of nodes 15-19.

    For each node whose node_type starts with "15-" to "19-":
      - If the node's node_id has a corresponding entry in importance_map
      - Strip trailing punctuation/whitespace from the original description, then append "，{role level}"

    Other nodes (types outside 15-19) are left untouched.
    """
    # Fixed prefix for the role-level marker (used to prevent duplicate appending)
    LEVEL_MARKER_PREFIX = "，"

    updated_nodes = []
    for node in nodes:
        # Compatible with both snake_case and camelCase
        node_type_raw = node.get("node_type") or node.get("Node_type") or ""
        node_type = str(node_type_raw)
        # Only process nodes 15-19
        if not (node_type.startswith("15-") or node_type.startswith("16-")
                or node_type.startswith("17-") or node_type.startswith("18-")
                or node_type.startswith("19-")
                # Compatibility with numeric formats: 15 -> "15-..."
                or (node_type_raw in (15, 16, 17, 18, 19))):
            updated_nodes.append(node)
            continue

        # Compatible with both snake_case and camelCase
        node_id = str(node.get("node_id") or node.get("Node_id") or "")

        # Prefer exact match (e.g. "168_15_N1"); otherwise match by node-number suffix (e.g. "15")
        importance = importance_map.get(node_id, "")
        if not importance:
            # Extract the node-number portion ("15") from the node_id (e.g. "168_15_N1") and look it up
            parts = node_id.split("_")
            if len(parts) >= 2:
                importance = importance_map.get(parts[1], "")

        if not importance:
            updated_nodes.append(node)
            continue

        # Compatible with both snake_case and camelCase
        old_desc = str(node.get("node_description") or node.get("Node_description") or "").strip()
        # Tolerance for {}-style: strip inner { and } (handles LLM outputs like "{xxx}")
        old_desc = old_desc.replace("{", "").replace("}", "")
        # Skip cases where the original description is empty or only "not mentioned"
        if not old_desc or old_desc == "not mentioned":
            updated_nodes.append(node)
            continue

        # Check whether already appended (by detecting whether the importance is already in the description)
        if importance in old_desc:
            updated_nodes.append(node)
            continue

        # Before appending: clean trailing punctuation (to avoid "desc., importance" with consecutive punctuation)
        clean_desc = old_desc.rstrip("，。；、：！？…—–·～.,;:!?()[]{}（）【】""''\"\"")
        new_desc = f"{clean_desc}，{importance}"
        updated_node = {**node, "node_description": new_desc}
        updated_nodes.append(updated_node)

    return updated_nodes


def merge_importance_into_batch4(batch4_data: dict, case_id: str) -> list[dict]:
    """
    Read node 20's calibration info from batch 4 (15-20 Algorithm Nodes) JSON,
    fuse the role levels into nodes 15-19, and return the node list with node 20 removed.

    Steps:
      1. Distinguish node 20 (calibration node) from other nodes in batch4_data["nodes"]
      2. If node 20 exists, parse its node_description to obtain a {node_id: importance} dict
         (supports three formats: plain text string, nested dict, prompt-fixed rule)
      3. Append the role level to the node_description of nodes 15-19 (via apply_importance_to_nodes)
      4. Return the fused node list (node 20 removed)
    """
    all_nodes = batch4_data.get("nodes", [])
    if not isinstance(all_nodes, list):
        all_nodes = []

    calib_node = None
    node15_19_list = []
    for node in all_nodes:
        # Compatible with both snake_case and camelCase
        node_type = node.get("node_type") or node.get("Node_type", "")
        if node_type == "20-Algorithm Node Role-Importance Calibration":
            calib_node = node
        else:
            node15_19_list.append(node)

    if calib_node is None:
        return node15_19_list

    importance_map = parse_calibration_description(calib_node, case_id)
    if not importance_map:
        return node15_19_list

    return apply_importance_to_nodes(node15_19_list, importance_map)


# ============================================================================
# Node Construction
# ============================================================================

def build_nodes_from_source(
    all_batch_data: dict[str, dict[str, dict]],
    case_id: str,
    mapped_case_id: str,
) -> list[dict]:
    """
    Collect all nodes from the 4 node batches (batch1~batch4):

    1. For batch 4 (15-20 Algorithm Nodes), for nodes 15-19,
       fuse node 20's calibration info (role level) into node_description
    2. Filter out nodes whose node_type starts with "20-" (i.e. node 20 itself, removed after fusion)
    3. Update the node_id prefix (168_01_N1 -> C00168_01_N1)
    4. Sort by node_type prefix number; nodes with the same number keep their original order
    """
    raw_nodes = []

    # batch1, batch2, batch3: directly collect (no special handling)
    for batch_id in ["batch1", "batch2", "batch3"]:
        batch_map = all_batch_data.get(batch_id, {})
        paper_data = batch_map.get(case_id, {})
        nodes = paper_data.get("nodes", [])
        if isinstance(nodes, list):
            raw_nodes.extend(nodes)

    # batch4 (15-20 Algorithm Nodes): fuse node 20's calibration info, then remove node 20
    batch4_map = all_batch_data.get("batch4", {})
    batch4_paper = batch4_map.get(case_id, {})
    if batch4_paper:
        calibrated_nodes = merge_importance_into_batch4(batch4_paper, case_id)
        raw_nodes.extend(calibrated_nodes)

    # Update node_id prefix (168_01_N1 -> C00168_01_N1) + dedupe + remove unwanted fields
    ORDER_FIELDS = ("node_absolute_order",
                    "node_absolute_order_mean",
                    "node_absolute_order_variance")
    filtered_nodes = []
    seen_node_ids: set[str] = set()   # Prevent the same node_id appearing multiple times (keep the first)
    for node in raw_nodes:
        old_id = node.get("node_id", "")
        # Dedupe by node_id: keep only the first occurrence
        if old_id in seen_node_ids:
            continue
        seen_node_ids.add(old_id)
        if old_id:
            new_id = mapped_case_id + old_id[len(case_id):]
        else:
            new_id = old_id
        clean_node = {k: v for k, v in node.items() if k not in ORDER_FIELDS}
        clean_node["node_id"] = new_id
        filtered_nodes.append(clean_node)

    filtered_nodes.sort(key=lambda n: extract_node_order(n.get("node_type", "")))
    validate_and_report_node_ids(filtered_nodes, mapped_case_id)
    return filtered_nodes


def merge_paper_case(
    case_id: str,
    all_batch_data: dict[str, dict[str, dict]],
) -> Optional[dict]:
    """
    Merge all batch data for one paper into a single, complete JSON structure.
    The output format matches the example merged JSON exactly.
    """
    # --- Paper metadata: take from any batch (they are the same across batches) ---
    hp_batch = all_batch_data.get("hyperparam", {}).get(case_id, {})
    meta_batch = None
    for bid in ["batch1", "batch2", "batch3", "batch4"]:
        m = all_batch_data.get(bid, {}).get(case_id)
        if m:
            meta_batch = m
            break

    raw_case_id = case_id
    mapped_case_id = normalize_case_id(case_id)

    paper_title = (meta_batch or hp_batch).get("paper_title", "")
    publish_year = (meta_batch or hp_batch).get("publish_year")
    publish_source = (meta_batch or hp_batch).get("publish_source", "")
    cite_count = (meta_batch or hp_batch).get("cite_count", 0)

    # --- Hyperparameters: take top-level fields directly from hp_batch (same as input JSON) ---
    hyperparam = extract_hyperparam_fields(hp_batch)

    # --- Node list (sorted) ---
    nodes = build_nodes_from_source(all_batch_data, raw_case_id, mapped_case_id)

    # --- Build final structure ---
    merged = {
        "case_id": mapped_case_id,
        "paper_title": paper_title,
        "publish_year": publish_year,
        "publish_source": publish_source,
        "cite_count": cite_count,
        "algorithm_hyperparameters": hyperparam["algorithm_hyperparameters"],
        "training_config": hyperparam["training_config"],
        "performance_metrics": hyperparam["performance_metrics"],
        "nodes": nodes,
        "edges": [],
    }

    return merged


# ============================================================================
# Main Flow
# ============================================================================

def run_merge(input_root: str, output_root: str):
    """Execute the main merge flow"""
    print("=" * 70)
    print("v7 merge script")
    print("=" * 70)
    print(f"Input directory: {input_root}")
    print(f"Output directory: {output_root}")
    print("=" * 70)

    # Create the output directory (do not delete the old directory; overwrite any duplicates)
    final_dir = os.path.join(output_root, "final_merged", "A0-node_merged")
    by_paper_dir = os.path.join(final_dir, "merged_by_paper")
    os.makedirs(by_paper_dir, exist_ok=True)

    # Step 1: scan all batch files
    print("\n[Step 1] Scanning batch directories...")
    all_batch_data: dict[str, dict[str, dict]] = {}
    for batch_info in BATCH_DIRS:
        batch_id = batch_info["id"]
        data_map = scan_batch_files(input_root, batch_info)
        all_batch_data[batch_id] = data_map
        print(f"  {batch_info['name']:30s}: {len(data_map)} files")

    # Step 2: collect all case_ids
    print("\n[Step 2] Collecting all case_ids...")
    all_case_ids = set()
    for batch_data in all_batch_data.values():
        all_case_ids.update(batch_data.keys())
    print(f"  Total {len(all_case_ids)} case_ids")
    for cid in sorted(all_case_ids):
        print(f"    {cid} -> {normalize_case_id(cid)}")

    # Step 3: merge each paper one by one
    print("\n[Step 3] Merging each paper...")
    merged_list = []
    skipped = 0
    errors = 0

    for case_id in sorted(all_case_ids):
        try:
            merged = merge_paper_case(case_id, all_batch_data)
            if merged is None:
                skipped += 1
                continue

            merged_list.append(merged)

            # Save an individual file
            out_file = os.path.join(by_paper_dir, f"{merged['case_id']}.json")
            with open(out_file, "w", encoding="utf-8") as f:
                json.dump(merged, f, ensure_ascii=False, indent=2)

        except Exception as e:
            errors += 1
            print(f"  [ERROR] {case_id}: {e}")

    # Step 4: save the final merged file
    print("\n[Step 4] Saving final merged file...")
    if merged_list:
        sorted_ids = sorted([p["case_id"] for p in merged_list])
        first_id = sorted_ids[0]
        last_id = sorted_ids[-1]
    else:
        first_id = "unknown"
        last_id = "unknown"

    final_file = os.path.join(final_dir, f"[{first_id}][{last_id}]_merged_nodes.json")
    with open(final_file, "w", encoding="utf-8") as f:
        json.dump(merged_list, f, ensure_ascii=False, indent=2)

    # Statistics
    total_nodes = sum(len(p.get("nodes", [])) for p in merged_list)

    stats = {
        "total_papers": len(merged_list),
        "total_nodes": total_nodes,
        "input_root": input_root,
        "source_dirs": {b["id"]: b["subdir"] for b in BATCH_DIRS},
        "paper_summary": [
            {
                "case_id": p["case_id"],
                "paper_title": p.get("paper_title", ""),
                "node_count": len(p.get("nodes", [])),
                "has_hyperparameters": any([
                    p.get("algorithm_hyperparameters"),
                    p.get("training_config"),
                    p.get("performance_metrics"),
                ]),
            }
            for p in merged_list
        ],
    }

    stats_file = os.path.join(final_dir, "merge_stats.json")
    with open(stats_file, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    # Print summary
    print("\n" + "=" * 70)
    print("Merge complete")
    print("=" * 70)
    print(f"  Papers processed:  {len(merged_list)}")
    print(f"  Skipped:            {skipped}")
    print(f"  Errors:             {errors}")
    print(f"  Total nodes:        {total_nodes}")
    print(f"  Final file:         {final_file}")
    print(f"  Per-paper files:    {by_paper_dir}/")
    print(f"  Statistics file:    {stats_file}")
    print("=" * 70)

    # Print per-paper details
    print("\nPaper summary:")
    print(f"{'case_id':<10} {'Title (first 40 chars)':<42} {'Nodes':>6} {'Hyperparams':>6}")
    print("-" * 70)
    for p in merged_list:
        title = (p.get("paper_title", "") or "")[:40]
        has_hp = "Yes" if any([
            p.get("algorithm_hyperparameters"),
            p.get("training_config"),
            p.get("performance_metrics"),
        ]) else "No"
        print(f"{p['case_id']:<10} {title:<42} {len(p.get('nodes', [])):>6} {has_hp:>6}")

    return merged_list, stats


def main():
    global V7_ROOT_DIR

    parser = argparse.ArgumentParser(
        description="v7 merge script: merge all batch JSONs into the final result"
    )
    parser.add_argument("--input", type=str, default=V7_ROOT_DIR, help="v7 output root directory")
    parser.add_argument("--output", type=str, default=None, help="Output root directory (default: same as --input)")
    args = parser.parse_args()

    input_root = args.input
    output_root = args.output or input_root

    if not os.path.exists(input_root):
        print(f"Error: input directory does not exist: {input_root}")
        return

    run_merge(input_root, output_root)


if __name__ == "__main__":
    main()
