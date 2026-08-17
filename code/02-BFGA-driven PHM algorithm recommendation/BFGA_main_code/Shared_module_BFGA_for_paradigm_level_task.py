# -*- coding: utf-8 -*-
r"""
Diagnostic_TestSet_InductionConsistency_Shared_Module_v10.py
===========================================

Compute 4 types of consistency metrics (strict / TopK strict / relaxed / TopK relaxed)
for node_type indexes 15-19 with "-Induction" suffix only.

Input:
  1) Input data directory <SCENARIO_LABEL>_Induction.json
       { case_id: [ {node_id, node_type, node_name, ...}, ... ] }
     Where node_type looks like "16-FeatureExtractionAlgorithm-Induction", and
     node_name is the "category name" (e.g., "Unsupervised Reconstruction and
     Auto-Encoder Feature Learning Algorithm").

  2) Output data directory (OUTPUT_DIR/SCENARIO_LABEL) under each hyperparameter subfolder:
       - <case_id>-N_recommend.json  (recommended Top1)
       - <case_id>-N_vote.json        (TopK candidates, sorted by node vote_ratio)
     Where node_type looks like "16-FeatureExtractionAlgorithm" (without -Induction suffix),
     and node_name is the specific algorithm name (e.g., "Auto-Encoder").

  3) Node mapping table:
       ../data/literature_extraction_json/v8Version/FinalMerge/
       A2-NodeMerge_Disambiguation_Induction/InductionList/
         [2277EAKD][ZZZRPFBV]MergedNode_NormativeReview_Merged_NormativeReview_Disambiguation_NormativeReview_Induction_<NN>NodeMappingTable_SecondProcessing.md
     Where:
       - Column [1] = sequence number 1..K
       - Column [2] = category name (e.g., "Unsupervised Reconstruction and Auto-Encoder Feature Learning Algorithm")
       - Column [6] = node_names (per row: all specific algorithm names in this mapping table)
       - Column [7] = node_ids    (per row: all CASE_ID_<NN>_N1 form case numbers)

Output:
  1) Console prints 4 types of consistency scenario-level averages (grouped by Epoch_max).
  2) Appends <SCENARIO_LABEL>_consistency_summary.md
     (appends an "## Appendix: -Induction Category Consistency (Node Indexes 15-19)" section,
     does not overwrite the original report).
"""

import json
import os
import re
import os as _os_paradigm
from pathlib import Path
from typing import Any


# ============================================================
# Path constants (overridable via environment)
#
# These defaults point at the released data shipped with the repository.
# Set BFGA_GRAPH_PATH / BFGA_OUTPUT_DIR / BFGA_MAPPING_TABLE_DIR in your
# environment to point somewhere else (e.g. when running on a non-released
# intermediate dataset).
# ============================================================
_REPO_ROOT = Path(__file__).resolve().parents[2]


def _resolve(env_var: str, default_relpath: str) -> str:
    override = _os_paradigm.environ.get(env_var)
    if override:
        return override
    return str(_REPO_ROOT / default_relpath)


MAPPING_TABLE_DIR = _resolve(
    "BFGA_MAPPING_TABLE_DIR",
    "data/CEG data",
)

MAPPING_TABLE_PREFIX = (
    "[2277EAKD][ZZZRPFBV]MergedNode_NormativeReview_Merged_NormativeReview_Disambiguation_NormativeReview_Induction_"
)

OUTPUT_DIR = _resolve(
    "BFGA_OUTPUT_DIR",
    "data/output",
)

# Algorithm type indexes of interest
INDUCTION_NODE_TYPE_INDEXES = [15, 16, 17, 18, 19]
INDUCTION_SUFFIX = "-Induction"

# Internal TopK used for short-circuit comparison (must match Top_K in BASE_RUN_PARAMETERS)
DEFAULT_TOPK = 5


# ============================================================
# md mapping table parsing
# ============================================================

def _parse_md_table_row(line: str) -> dict | None:
    """Parse a single md table row.

    Input line format:
      `| 1 | category_name | ... | node_names | node_ids |`

    Returns dict {seq, category_name, node_names, node_ids} or None (not a data row).
    """
    s = line.strip()
    if not s.startswith("|"):
        return None
    # Filter header and separator lines
    if "node_names" in s and "node_ids" in s:
        return None
    if re.match(r"^\|\s*-+", s.replace("|", "|")):
        return None

    parts = [p.strip() for p in s.split("|")]
    # | a | b | c | d | e | f | g | -> split gives ['', 'a','b','c','d','e','f','g','']
    parts = [p for p in parts if p != ""]
    if len(parts) < 7:
        return None

    try:
        seq = int(parts[0])
    except Exception:
        return None

    category_name = parts[1]
    node_names_str = parts[5]  # node_names
    node_ids_str = parts[6]    # node_ids

    node_names = [x.strip() for x in node_names_str.split(",") if x.strip()]
    node_ids = [x.strip() for x in node_ids_str.split(",") if x.strip()]

    return {
        "seq": seq,
        "category_name": category_name,
        "node_names": node_names,
        "node_ids": node_ids,
    }


def load_mapping_table(node_type_index: int) -> list[dict]:
    """Load the md node mapping table (_SecondProcessing version) corresponding to node_type_index (15-19).

    Returns multiple rows of dict: {seq, category_name, node_names(list of algorithm_name),
    node_ids(list of CASE_ID_TYPE_N1)}.
    """
    md_path = os.path.join(
        MAPPING_TABLE_DIR,
        f"{MAPPING_TABLE_PREFIX}{node_type_index}NodeMappingTable_SecondProcessing.md",
    )
    if not os.path.exists(md_path):
        return []
    rows = []
    with open(md_path, "r", encoding="utf-8") as f:
        for line in f:
            row = _parse_md_table_row(line)
            if row is not None:
                rows.append(row)
    return rows


# ============================================================
# Reverse lookup mapping
# ============================================================

class InductionMapper:
    """Encapsulates (algorithm_name -> category_name) reverse lookup for 5 (15-19) node mapping tables.

    Build method:
      Build a {algorithm_name -> category_name} dict for each node_type_index (15~19) independently,
      and retain that algorithm's classification in this table. Even if the same-named algorithm
      is classified into different categories in different tables, the correct mapping can be
      selected based on the original base_node_type of the predicted algorithm.

    Interface:
      - build()
      - lookup(algorithm_name, node_type_index) -> str | None
      - categories_set() -> set[str]  (all categories set)
      - conflicts() -> list  (cross-category same name, kept as read-only list, for logs)
      - per_type_dict(idx) -> dict[str, str]
    """

    def __init__(self):
        self.per_type: dict[int, dict[str, str]] = {}  # idx -> {algo: cat}
        self.conflicts: list[tuple[str, int, str, str]] = []  # (algo, idx, cat1, cat2)
        self._built = False

    def build(self) -> "InductionMapper":
        if self._built:
            return self
        # 1) Build per table
        for idx in INDUCTION_NODE_TYPE_INDEXES:
            rows = load_mapping_table(idx)
            d: dict[str, str] = {}
            for row in rows:
                cat = row["category_name"]
                for algo in row["node_names"]:
                    a = algo.strip()
                    if not a:
                        continue
                    if a in d:
                        if d[a] != cat:
                            self.conflicts.append((a, idx, d[a], cat))
                        continue
                    d[a] = cat
            self.per_type[idx] = d
        # 2) Global conflict detection (between tables): algorithm name vs category conflict
        #    These are reasonable "cross-domain same names", not errors but we still note them
        seen_cat: dict[str, tuple[int, str]] = {}
        for idx, d in self.per_type.items():
            for algo, cat in d.items():
                if algo in seen_cat:
                    prev_idx, prev_cat = seen_cat[algo]
                    if prev_cat != cat and prev_idx != idx:
                        self.conflicts.append((algo, idx, prev_cat, cat))
                else:
                    seen_cat[algo] = (idx, cat)
        self._built = True
        return self

    def per_type_dict(self, idx: int) -> dict[str, str]:
        return self.per_type.get(idx, {})

    def lookup(self, algorithm_name: str, node_type_index: int) -> str | None:
        """Lookup table by node_type_index (15~19)."""
        if not algorithm_name or node_type_index not in self.per_type:
            return None
        a = algorithm_name.strip()
        d = self.per_type[node_type_index]
        cat = d.get(a)
        if cat is not None:
            return cat
        a_low = a.lower()
        for k, v in d.items():
            if k.lower() == a_low:
                return v
        return None

    def categories_set(self) -> set[str]:
        s: set[str] = set()
        for d in self.per_type.values():
            s.update(d.values())
        return s


# ============================================================
# Ground truth loading (_Induction.json)
# ============================================================

def load_ground_truth_induction(indu_json_path: str) -> dict[str, dict[str, str]]:
    """Read <SCENARIO_LABEL>_Induction.json, aggregate by (case_id, 'NN-XXX-Induction').

    Returns: { case_id: { node_type_suffix ("NN-XXXAlgorithm-Induction"): category_name } }
    """
    with open(indu_json_path, "r", encoding="utf-8") as f:
        raw = json.load(f)
    gt: dict[str, dict[str, str]] = {}
    for cid, items in raw.items():
        m: dict[str, str] = {}
        for it in items:
            nt = it.get("node_type", "")
            if not nt.startswith(tuple(f"{i}-" for i in INDUCTION_NODE_TYPE_INDEXES)):
                continue
            if INDUCTION_SUFFIX not in nt:
                continue
            nm = (it.get("node_name") or "").strip()
            if not nm:
                continue
            # Same category with multiple nodes, take the first occurrence name (consistent with _compute_gt_by_type behavior)
            m.setdefault(nt, nm)
        gt[cid] = m
    return gt


def _base_node_type(suffix: str) -> str:
    """Convert '16-FeatureExtractionAlgorithm-Induction' to '16-FeatureExtractionAlgorithm' (used for lookup in N_recommend)."""
    if suffix.endswith(INDUCTION_SUFFIX):
        return suffix[: -len(INDUCTION_SUFFIX)]
    return suffix


def _node_type_index(suffix: str) -> int:
    """Extract index 16 from '16-FeatureExtractionAlgorithm-Induction'."""
    try:
        return int(suffix.split("-", 1)[0])
    except Exception:
        return -1


# ============================================================
# N_recommend / N_vote reading and reverse lookup
# ============================================================

def _load_case_top1(hp_subdir: str, case_id: str) -> dict[str, dict]:
    """Read <case_id>-N_recommend.json.

    Returns { base_node_type: {"node_id":..., "node_name":..., "vote_ratio":...} }.
    """
    p = os.path.join(hp_subdir, f"{case_id}-N_recommend.json")
    if not os.path.exists(p):
        return {}
    try:
        with open(p, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return {}
    return data or {}


def _load_case_topk(hp_subdir: str, case_id: str) -> dict[str, list[dict]]:
    """Read <case_id>-N_vote.json, extract TopK candidates for each type (sorted by vote_ratio descending).

    Returns { base_node_type: [ {node_id, node_name, vote_ratio, ...}, ... ] }
    """
    p = os.path.join(hp_subdir, f"{case_id}-N_vote.json")
    if not os.path.exists(p):
        return {}
    with open(p, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict) or not data:
        return {}
    latest_key = max(data.keys(), key=lambda k: int(k.replace("Epoch", "")))
    by_type = data[latest_key].get("by_algorithm_type", {})
    out: dict[str, list[dict]] = {}
    for nt, sub in by_type.items():
        items = sub.get("Top_K", []) or []
        # Re-sort explicitly by vote_ratio descending if order is unreliable
        items = sorted(items, key=lambda x: float(x.get("vote_ratio", 0.0)), reverse=True)
        out[nt] = items
    return out


# ============================================================
# Consistency metrics computation
# ============================================================

def _calc_strict_for_case(
    case_id: str,
    ind_gt: dict[str, str],
    top1_map: dict[str, dict],
    top1_cats: dict[str, str | None],
) -> dict:
    """Strict consistency: compare top1 category_name vs GT for each Ind-node_type.

    Denominator: all Ind-node_types (those present in GT).
    """
    matched = missed = invalid_gt = 0
    by_type = {}
    for nt, gt_cat in ind_gt.items():
        base = _base_node_type(nt)
        pred_cat = top1_cats.get(nt)  # Filled by caller
        rec = top1_map.get(base, {}) or {}
        rec_name = (rec.get("node_name") or "").strip()
        gt_name = (gt_cat or "").strip()

        if pred_cat is None:
            # Algorithm name not found in mapping table → treat as miss
            status = "name_mismatch"
            hit = False
            missed += 1
        else:
            hit = (pred_cat == gt_name)
            if hit:
                status = "exact_match"
                matched += 1
            else:
                status = "name_mismatch"
                missed += 1

        by_type[nt] = {
            "ground_truth": gt_name,
            "recommended_algorithm": rec_name,
            "recommended_category": pred_cat,
            "match_status": status,
            "strict_match": hit,
        }

    denom = max(len(ind_gt), 1)
    return {
        "type": "strict",
        "total_gt": len(ind_gt),
        "exact_match": matched,
        "missed": missed,
        "match_rate": round(matched / denom, 4),
        "by_type": by_type,
    }


def _calc_topk_strict_for_case(
    case_id: str,
    ind_gt: dict[str, str],
    topk_map: dict[str, list[dict]],          # base_node_type -> [cand...]
    topk_cats_by_nt: dict[str, set[str]],     # ind-suffix -> {category_name in TopK}
) -> dict:
    """TopK strict consistency: hit if GT category is in TopK category set."""
    matched = missed = 0
    by_type = {}
    for nt, gt_cat in ind_gt.items():
        cand_cats = topk_cats_by_nt.get(nt, set())
        hit = gt_cat in cand_cats
        if hit:
            matched += 1
            status = "topk_hit"
        else:
            missed += 1
            status = "topk_miss"
        by_type[nt] = {
            "ground_truth": gt_cat,
            "topk_categories": sorted(cand_cats),
            "match_status": status,
            "topk_strict_match": hit,
        }

    denom = max(len(ind_gt), 1)
    return {
        "type": "topk_strict",
        "total_gt": len(ind_gt),
        "topk_hit": matched,
        "missed": missed,
        "match_rate": round(matched / denom, 4),
        "by_type": by_type,
    }


def _calc_relaxed_for_case(
    case_id: str,
    ind_gt: dict[str, str],
    top1_map: dict[str, dict],
    top1_cats: dict[str, str | None],
) -> dict:
    """Relaxed consistency: same as strict (per Ind-node_type comparing top1 category vs GT),

    Since GT and rec are aligned 1-to-1 by Ind-node_type, the denominator is also
    the total Ind-node_type count (same as strict).
    """
    return _calc_strict_for_case(case_id, ind_gt, top1_map, top1_cats)


def _calc_topk_relaxed_for_case(
    case_id: str,
    ind_gt: dict[str, str],
    topk_map: dict[str, list[dict]],
    topk_cats_by_nt: dict[str, set[str]],
) -> dict:
    """TopK relaxed consistency same as TopK strict: hit if GT category in TopK category set."""
    return _calc_topk_strict_for_case(case_id, ind_gt, topk_map, topk_cats_by_nt)


# ============================================================
# Single case × single epoch_max computation
# ============================================================

def compute_induction_consistency_for_case(
    case_id: str,
    hp_subdir: str,
    ind_gt: dict[str, str],
    mapper: InductionMapper,
    topk: int = DEFAULT_TOPK,
    require_outputs: bool = True,
) -> dict:
    """Read N_recommend and N_vote for this case in this epoch subdirectory and compute 4 types of consistency.

    If require_outputs=True and both N_recommend / N_vote are empty, returns None (caller should skip this case).
    """
    ind_gt = dict(ind_gt)  # Copy
    if not ind_gt:
        empty = {"match_rate": 0.0, "total_gt": 0, "by_type": {}}
        return {
            "strict": empty,
            "topk_strict": empty,
            "relaxed": empty,
            "topk_relaxed": empty,
        }

    top1_map = _load_case_top1(hp_subdir, case_id)
    topk_map = _load_case_topk(hp_subdir, case_id)

    if require_outputs and (not top1_map) and (not topk_map):
        # No output files, this case is not completed under this epoch_max
        return None

    # Reverse lookup Top1 categories (select corresponding md table by nt_index to avoid same-name cross-category conflicts)
    top1_cats: dict[str, str | None] = {}
    for nt in ind_gt:
        base = _base_node_type(nt)
        idx = _node_type_index(nt)
        rec = top1_map.get(base) or {}
        algo = (rec.get("node_name") or "").strip()
        top1_cats[nt] = mapper.lookup(algo, idx)

    # Reverse lookup TopK categories (take TopK candidates of each base_node_type's category set;
    # merge into ind-suffix)
    topk_cats_by_nt: dict[str, set[str]] = {nt: set() for nt in ind_gt}
    for nt in ind_gt:
        base = _base_node_type(nt)
        idx = _node_type_index(nt)
        cands = topk_map.get(base, [])[:topk]
        cats = set()
        for c in cands:
            algo = (c.get("node_name") or "").strip()
            cat = mapper.lookup(algo, idx)
            if cat:
                cats.add(cat)
        topk_cats_by_nt[nt] = cats

    strict_res = _calc_strict_for_case(case_id, ind_gt, top1_map, top1_cats)
    topk_strict_res = _calc_topk_strict_for_case(case_id, ind_gt, topk_map, topk_cats_by_nt)
    relaxed_res = _calc_relaxed_for_case(case_id, ind_gt, top1_map, top1_cats)
    topk_relaxed_res = _calc_topk_relaxed_for_case(case_id, ind_gt, topk_map, topk_cats_by_nt)

    return {
        "strict": strict_res,
        "topk_strict": topk_strict_res,
        "relaxed": relaxed_res,
        "topk_relaxed": topk_relaxed_res,
    }


# ============================================================
# Aggregate results for all cases under a single epoch subdirectory
# ============================================================

def aggregate_epoch_induction(
    hp_subdir: str,
    case_ids: list[str],
    gt_all: dict[str, dict[str, str]],
    mapper: InductionMapper,
    topk: int = DEFAULT_TOPK,
) -> dict:
    """Compute and aggregate Induction 4-type consistency for all cases in a single epoch_max subdirectory.

    Returns: {
      "case_results": { case_id: {strict,topk_strict,relaxed,topk_relaxed} },
      "epoch_summary": {
        "case_count": int,
        "strict_avg": float,
        "topk_strict_avg": float,
        "relaxed_avg": float,
        "topk_relaxed_avg": float,
      }
    }
    """
    case_results: dict[str, dict] = {}
    for cid in case_ids:
        ind_gt = gt_all.get(cid, {}) or {}
        if not ind_gt:
            continue
        per = compute_induction_consistency_for_case(
            case_id=cid,
            hp_subdir=hp_subdir,
            ind_gt=ind_gt,
            mapper=mapper,
            topk=topk,
        )
        if per is None:
            # This case has no N_recommend / N_vote under this epoch_max, skip
            continue
        case_results[cid] = per

    if not case_results:
        emp = {"case_count": 0,
               "strict_avg": 0.0,
               "topk_strict_avg": 0.0,
               "relaxed_avg": 0.0,
               "topk_relaxed_avg": 0.0}
        return {"case_results": {}, "epoch_summary": emp}

    strict_rates = [r["strict"]["match_rate"] for r in case_results.values()]
    topk_strict_rates = [r["topk_strict"]["match_rate"] for r in case_results.values()]
    relaxed_rates = [r["relaxed"]["match_rate"] for r in case_results.values()]
    topk_relaxed_rates = [r["topk_relaxed"]["match_rate"] for r in case_results.values()]

    def _avg(xs):
        return round(sum(xs) / len(xs), 4) if xs else 0.0

    summary = {
        "case_count": len(case_results),
        "strict_avg": _avg(strict_rates),
        "topk_strict_avg": _avg(topk_strict_rates),
        "relaxed_avg": _avg(relaxed_rates),
        "topk_relaxed_avg": _avg(topk_relaxed_rates),
    }
    return {"case_results": case_results, "epoch_summary": summary}


# ============================================================
# Markdown report: append to SCENARIO_LABEL_consistency_summary.md
# ============================================================

APPENDIX_TITLE_TEMPLATE = (
    "## Appendix: -Induction Category Consistency (Node Indexes 15-19)\n"
    "\n"
    "> Evaluation criteria:\n"
    ">> - GT comes from items with node_type like `'NN-XXXAlgorithm-Induction'` in "
    "`<SCENARIO_LABEL>_Induction.json`, the `node_name` field (already the \"category name\").\n"
    ">> - Predicted Top1 comes from `<case_id>-N_recommend.json`; Predicted TopK comes from `<case_id>-N_vote.json`.\n"
    ">> - The \"algorithm name\" in Top1/TopK is reverse-looked-up to \"category name\" via the "
    "[Induction List Node Mapping Table]({mapping_dir}), then compared with GT.\n"
    ">> - 4 types of consistency: strict / TopK strict / relaxed / TopK relaxed; "
    "denominator = total number of Induction categories present in the case.\n"
    "\n"
)


def build_appendix_md(
    scenario_label: str,
    epoch_max_values: list[int],
    epoch_results_map: dict[int, dict],
    mapping_dir: str = MAPPING_TABLE_DIR,
    topk: int = DEFAULT_TOPK,
) -> str:
    """Build the appendix section (plain text md) appended to the consistency summary md."""
    lines: list[str] = []
    title = (APPENDIX_TITLE_TEMPLATE
             .replace("<SCENARIO_LABEL>", scenario_label)
             .format(mapping_dir=mapping_dir))
    lines.append(title)
    lines.append(
        "### Summary per Epoch_max subdirectory\n\n"
    )
    lines.append("| Epoch_max | case count | Strict consistency | TopK strict consistency | Relaxed consistency | TopK relaxed consistency |\n")
    lines.append("| --- | --- | --- | --- | --- | --- |\n")
    for em in epoch_max_values:
        s = epoch_results_map.get(em, {}).get("epoch_summary")
        if not s:
            continue
        lines.append(
            f"| {em} | {s['case_count']} | {s['strict_avg']:.2%} | "
            f"{s['topk_strict_avg']:.2%} | {s['relaxed_avg']:.2%} | "
            f"{s['topk_relaxed_avg']:.2%} |\n"
        )
    lines.append("\n")

    # Details per Epoch_max: case × node_type
    lines.append("### Details (each case × each Induction category)\n\n")
    for em in epoch_max_values:
        per_epoch = epoch_results_map.get(em, {})
        case_res = per_epoch.get("case_results", {})
        if not case_res:
            continue
        lines.append(f"#### Epoch_max = {em}\n\n")
        lines.append(
            "| case_id | node_type | GT category | Top1 algorithm | Top1 reverse-looked category | Top1 match | TopK hit categories | TopK match |\n"
            "| --- | --- | --- | --- | --- | --- | --- | --- |\n"
        )
        for cid, res in case_res.items():
            ind_gt = list(res["strict"]["by_type"].items())
            for nt, info in ind_gt:
                gt_name = info["ground_truth"]
                top1_algo = info["recommended_algorithm"]
                top1_cat = info["recommended_category"] or ""
                top1_match = "Y" if info["strict_match"] else "N"
                topk_info = res["topk_strict"]["by_type"][nt]
                topk_cats = ", ".join(topk_info.get("topk_categories", []))
                topk_match = "Y" if topk_info["topk_strict_match"] else "N"
                lines.append(
                    f"| {cid} | {nt} | {gt_name} | "
                    f"{top1_algo} | {top1_cat} | {top1_match} | {topk_cats} | {topk_match} |\n"
                )
        lines.append("\n")
    return "".join(lines)


def append_md_file(path: str, content: str) -> None:
    """If the file already contains the same appendix title, replace the old appendix with new content;
    otherwise append to end of file."""
    appendix_marker = "## Appendix: -Induction Category Consistency"
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            existing = f.read()
        if appendix_marker in existing:
            head, _, _ = existing.partition(appendix_marker)
            with open(path, "w", encoding="utf-8") as f:
                f.write(head.rstrip() + "\n\n" + content)
            return
        with open(path, "a", encoding="utf-8") as f:
            f.write("\n\n" + content)
    else:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)


# ============================================================
# Main entry: reused by two Top0/Top1 test programs
# ============================================================

def run_induction_consistency(
    scenario_label: str,
    epoch_max_values: list[int],
    case_ids: list[str],
    gt_all: dict[str, dict[str, str]],
    scenario_output_dir: str,
    topk: int = DEFAULT_TOPK,
    log: Any = None,
) -> dict:
    """Run Induction 4-type consistency on a test scenario, append to md, return summary per epoch_max."""
    mapper = InductionMapper().build()

    if log is not None:
        total_size = sum(len(d) for d in mapper.per_type.values())
        log(f"  Inducer mapping table: loaded 5 (15-19) md tables, totaling {total_size} (algorithm → category) entries")
        if mapper.conflicts:
            log(f"  Inducer mapping table: {len(mapper.conflicts)} same-table/cross-table conflicts found, only keeping first occurrence category")
        else:
            log("  Inducer mapping table: no conflicts")

    epoch_results_map: dict[int, dict] = {}
    for em in epoch_max_values:
        hp_subdir = os.path.join(scenario_output_dir, _ind_hp_subfolder_name(em))
        if not os.path.isdir(hp_subdir):
            if log is not None:
                log(f"  [Skip] Subdirectory does not exist: {hp_subdir}")
            continue
        agg = aggregate_epoch_induction(
            hp_subdir=hp_subdir,
            case_ids=case_ids,
            gt_all=gt_all,
            mapper=mapper,
            topk=topk,
        )
        epoch_results_map[em] = agg
        s = agg["epoch_summary"]
        if log is not None:
            log(
                f"  Epoch_max={em}: case_count={s['case_count']} | "
                f"strict={s['strict_avg']:.2%} | TopK_strict={s['topk_strict_avg']:.2%} | "
                f"relaxed={s['relaxed_avg']:.2%} | TopK_relaxed={s['topk_relaxed_avg']:.2%}"
            )

    # Write md appendix
    md_path = os.path.join(scenario_output_dir, f"{scenario_label}_consistency_summary.md")
    md_appendix = build_appendix_md(
        scenario_label=scenario_label,
        epoch_max_values=epoch_max_values,
        epoch_results_map=epoch_results_map,
        topk=topk,
    )
    append_md_file(md_path, md_appendix)

    return {
        "epoch_results_map": epoch_results_map,
        "mapper_size": sum(len(d) for d in mapper.per_type.values()),
        "mapper_conflicts": len(mapper.conflicts),
    }


def _ind_hp_subfolder_name(epoch_max: int) -> str:
    """Build hyperparameter subfolder name consistent with BASE_RUN_PARAMETERS."""
    # Reuse build_hyperparam_subfolder_name from shared module to avoid string inconsistency
    from Diagnostic_TestSet_AgentGraphReasoning_Shared_Module_v10 import build_hyperparam_subfolder_name
    rp = {
        "Epoch_max": epoch_max,
        "Thinking_belief_threshold": 0.95,
        "Top_K": DEFAULT_TOPK,
        "pruning_dynamic_width_gamma": 2,
        "pruning_dynamic_width_hard_cap": 3,
        "pruning_entropy_disable_threshold": 1.10,
    }
    return build_hyperparam_subfolder_name(rp)
