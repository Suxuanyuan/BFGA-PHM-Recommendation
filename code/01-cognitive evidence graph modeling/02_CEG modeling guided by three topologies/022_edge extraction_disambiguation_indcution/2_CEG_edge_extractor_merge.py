# -*- coding: utf-8 -*-
"""
Edge merge script zotero_knowledge_graph_edge_extractor_merge_v8.py
========================================================================
Functions:
  Merge the per-batch JSON files produced during the "edge" extraction stage into a single complete array.

Background:
  In v7, the "edge" extraction for each paper is split into multiple batches (batch0, batch1, batch2, batch3).
  After LLM extraction, each batch produces a JSON file with the form:
      <case_id_1>+...+<case_id_n>+batchN+merge-edges.json
  The outermost element is a JSON array; each element of the array is a dict for a single paper
  (containing case_id, paper_title, nodes, edges, etc.).

Merge goal:
  Merge the outermost arrays of multiple batch JSONs into a single array:
      [inner elements of batch0, inner elements of batch1, ..., inner elements of batch3]

Input directory (default):
  ./data/03_induction/B0-edges_merged/   <-- RELATIVE PATH placeholder

Output file (same directory as input; filename generated dynamically):
  <first_batch_case_id>+<last_batch_case_id>+merged-edges.json
  where:
    first_batch_case_id: case_id before the first "+" in the batch0 filename (e.g. "225KHNN8")
    last_batch_case_id: case_id before the first "+" in the last batch filename (e.g. "YPWGNCJD")

Usage:
  python zotero_knowledge_graph_edge_extractor_merge_v8.py
  python zotero_knowledge_graph_edge_extractor_merge_v8.py --input "F:\\...\\B0-edges_merged"
"""

import os
import re
import json
import argparse


# ============================================================================
# Configuration
# ============================================================================

DEFAULT_INPUT_DIR = r"./data/03_induction/B0-edges_merged"


# ============================================================================
# Utility functions
# ============================================================================

# Match the "batchN" tag: used to locate the batch number
# e.g.: "225KHNN8+...+C00174+batch0+merge-edges.json" -> batch number 0
_BATCH_TAG_PATTERN = re.compile(r"\+batch(\d+)\+")

def extract_first_case_id_from_filename(filename: str) -> str:
    """
    From the filename (e.g. '225KHNN8+...+C00174+batch0+merged-edges.json'),
    extract the part before the first '+' as the case_id.

    Per the user requirement: the merged output filename is
    <case_id_1>+<case_id_2>+merged-edges.json, where
    case_id_1 = case_id before the first '+' in the batch0 file,
          case_id_2 = case_id before the first '+' in the last batch file.
    Both are extracted the same way, so this function is used for both.
    """
    base = os.path.splitext(filename)[0]
    if "+" in base:
        return base.split("+", 1)[0].strip()
    return base.strip()


def extract_batch_index(filename: str) -> int:
    """
    Extract the batch number from the filename (N in "batchN"); returns -1 if not found.
    Used to sort multiple JSON files by batch order.
    """
    m = _BATCH_TAG_PATTERN.search(filename)
    if m:
        try:
            return int(m.group(1))
        except ValueError:
            return -1
    return -1


def load_json_list(filepath: str) -> list:
    """
    Load a JSON file and return its outermost list.
    Raises ValueError if the outermost element is not a list.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError(
            f"File {os.path.basename(filepath)} outermost is not a JSON array, "
            f"but {type(data).__name__}; cannot merge"
        )
    return data


# ============================================================================
# Main flow
# ============================================================================

def run_merge(input_dir: str):
    """
    Run the edge-merge main flow:
      1. Scan the input directory for all "*batchN+merged-edges.json" files
      2. Sort by ascending batch number
      3. Load each file's outermost array in turn
      4. Merge into a single complete array and save it
      5. Output filename: <first_case_id>+<last_case_id>+merged-edges.json
    """
    print("=" * 70)
    print("v8 edge-merge script")
    print("=" * 70)
    print(f"Input directory: {input_dir}")
    print("=" * 70)

    if not os.path.exists(input_dir):
        print(f"[ERROR] Input directory does not exist: {input_dir}")
        return None

    # ---- Step 1: scan candidate JSON files ----
    print("\n[Step 1] Scanning edge-merge JSON files in the directory...")
    candidate_files = []
    for filename in os.listdir(input_dir):
        if not filename.endswith(".json"):
            continue
        if "batch" not in filename or "merged-edges" not in filename:
            continue
        candidate_files.append(filename)

    if not candidate_files:
        print(f"[ERROR] No '*batchN+merged-edges.json' files found in {input_dir}")
        return None

    # ---- Step 2: sort by ascending batch number ----
    candidate_files.sort(key=extract_batch_index)
    print(f"  Found {len(candidate_files)} candidate files (sorted by ascending batch):")
    for fn in candidate_files:
        idx = extract_batch_index(fn)
        first_id = extract_first_case_id_from_filename(fn)
        print(f"    batch{idx}: {fn}  (start case_id={first_id})")

    # ---- Step 3: load and merge each batch's array ----
    print("\n[Step 2] Loading and merging each batch's JSON...")
    merged_list: list = []
    total_batches = len(candidate_files)
    errors = 0

    for i, filename in enumerate(candidate_files):
        filepath = os.path.join(input_dir, filename)
        try:
            batch_list = load_json_list(filepath)
            print(f"  [batch {extract_batch_index(filename)}] {filename} -> {len(batch_list)} entries")
            merged_list.extend(batch_list)
        except Exception as e:
            errors += 1
            print(f"  [ERROR] Read failed: {filename} -> {e}")

    print(f"\n  Total entries after merge: {len(merged_list)}")
    if errors > 0:
        print(f"  Failed batches: {errors}")

    # ---- Step 4: compute the output filename ----
    first_filename = candidate_files[0]
    last_filename = candidate_files[-1]
    first_case_id = extract_first_case_id_from_filename(first_filename)
    last_case_id = extract_first_case_id_from_filename(last_filename)

    if not first_case_id or not last_case_id:
        print("[ERROR] Cannot extract case_id from filename; please check the filename format")
        return None

    output_filename = f"{first_case_id}+{last_case_id}+merged-edges.json"
    output_filepath = os.path.join(input_dir, output_filename)

    # ---- Step 5: write the output file ----
    print("\n[Step 3] Writing merge result...")
    with open(output_filepath, "w", encoding="utf-8") as f:
        json.dump(merged_list, f, ensure_ascii=False, indent=2)

    # ---- aggregate / validate ----
    total_edges = 0
    papers_with_edges = 0
    for paper in merged_list:
        if not isinstance(paper, dict):
            continue
        edges = paper.get("edges", [])
        if isinstance(edges, list) and len(edges) > 0:
            total_edges += len(edges)
            papers_with_edges += 1

    print("\n" + "=" * 70)
    print("Merge complete")
    print("=" * 70)
    print(f"  Merged batches:        {total_batches - errors}/{total_batches}")
    print(f"  Merged papers:         {len(merged_list)}")
    print(f"  Papers with edges:     {papers_with_edges}")
    print(f"  Total edges:           {total_edges}")
    print(f"  Output file:           {output_filepath}")
    print("=" * 70)

    return merged_list, output_filepath


def main():
    parser = argparse.ArgumentParser(
        description="v8 edge-merge script: merge multiple batch edge-JSON arrays into one complete array"
    )
    parser.add_argument(
        "--input",
        type=str,
        default=DEFAULT_INPUT_DIR,
        help="Directory containing edge-merge JSON (default: B0-edges_merged)",
    )
    args = parser.parse_args()

    run_merge(args.input)


if __name__ == "__main__":
    main()
