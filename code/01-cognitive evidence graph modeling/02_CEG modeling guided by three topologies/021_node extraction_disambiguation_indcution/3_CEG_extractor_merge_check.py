# -*- coding: utf-8 -*-
"""
Literature Knowledge Graph Node Conformance Audit Script v7_merge_conformance_audit.py
========================================================================
Functions:
  1. Null-value audit: iterate through each node {} in the graph JSON and delete three categories of empty-value nodes
  2. node_name conformance audit: review and correct node_types that have N-from-1 rules
  3. Call the LLM to reassign non-compliant node_names
  4. Graph structure conformance audit: check whether nested structures and property names are compliant

Inputs:
  - Graph JSON: A0-node_merged/[...].json (relative path: ./output/final_merged/A0-node_merged/)
  - Prompt md: ./v5_version_prompts/*.md (4 files, matching the actual MD filenames in the schema directory):
      * 01-03,08-09 nodes.md
      * 04-07 nodes.md
      * 10-14 nodes.md
      * 15-20 nodes.md

Outputs:
  - Graph JSON-v2: appended with the suffix "_conformance_audit"
"""

import os
import json
import requests
from typing import Optional


# ============================================================================
# Configuration
# ============================================================================

API_KEY = ""  # TODO: Provide your own API key before running
API_URL = os.environ.get("BFGA_LLM_API_URL", "https://YOUR.LLM.ENDPOINT/v1/chat/completions")
LLM_MODEL = "gemini-3.5-flash"
LLM_TIMEOUT = 300
LLM_TEMPERATURE = 0

INPUT_GRAPH_PATH = r"./output/final_merged/A0-node_merged/[2277EAKD][ZZZRPFBV]_merged_nodes_conformance_audit_merged.json"

PROMPT_FILES = [
    r"./v5_version_prompts/04-07 nodes.md",
    r"./v5_version_prompts/10-14 nodes.md",
    r"./v5_version_prompts/15-20 nodes.md",
    r"./v5_version_prompts/01-03,08-09 nodes.md",
]

OUTPUT_DIR = r"./output/final_merged/A0-node_merged"


# ============================================================================
# N-from-1 Rules (extracted from the prompt .md files and embedded into the program)
# ============================================================================

# node_type -> set of N-from-1 options (exact match)
NODE_NAME_RULES: dict[str, set[str]] = {
    # 01-Object Domain: 8 from 1
    "01-Object Domain": {
        "Aerospace", "Space", "Marine", "Industrial", "Nuclear", "Electronics", "Vehicle", "Other",
    },
    # 03-Operating Conditions: 3 from 1
    "03-Operating Conditions": {
        "Single Condition", "Multiple Conditions", "Variable Conditions",
    },
    # 06-Fault Severity: 2 from 1
    "06-Fault Severity": {
        "Single Severity", "Multiple Severities",
    },
    # 07-Compound Fault: 3 from 1
    "07-Compound Fault": {
        "No Compound Fault", "Compound Fault Within Same Structure", "Compound Fault Across Structures",
    },
    # 08-PHM Task: 5 from 1
    "08-PHM Task": {
        "Detection Task", "Diagnosis Task", "Prediction Task", "Assessment Task", "Other Task",
    },
    # 09-Problem Scenario: 10 from 1
    "09-Problem Scenario": {
        "Small Fault Samples",
        "Zero Fault Samples",
        "Distribution Discrepancy",
        "Uncertainty",
        "Compound Faults",
        "Complex Systems",
        "Early Degradation Prediction",
        "Multi-Source Heterogeneous / Multimodal Data",
        "Trustworthiness / Interpretability",
        "Other",
    },
    # 12-Training Data Availability: 3 from 1
    "12-Training Data Availability": {
        "Zero-Sample", "Scarce", "Sufficient",
    },
    # 13-Noise Level: 2 from 1
    "13-Noise Level": {
        "High Noise", "Normal",
    },
    # 14-compute资源类: 3 from 1
    "14-Computational Resource": {
        "Low Resource Consumption", "Not Mentioned", "High Resource Consumption",
    },
}

# node_types that have N-from-1 rules (need auditing)
AUDIT_NODE_TYPES = set(NODE_NAME_RULES.keys())


# ============================================================================
# LLM Client
# ============================================================================

class LLMCallError(Exception):
    pass


def call_llm(messages: list[dict]) -> str:
    """Call the LLM and return the plain-text content."""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": LLM_MODEL,
        "messages": messages,
        "temperature": LLM_TEMPERATURE,
        "max_tokens": 4096,
    }
    try:
        resp = requests.post(API_URL, headers=headers, json=payload, timeout=LLM_TIMEOUT)
        resp.raise_for_status()
        data = resp.json()
        if "choices" not in data or not data["choices"]:
            raise LLMCallError(f"No choices in response: {data}")
        return data["choices"][0]["message"]["content"]
    except requests.exceptions.Timeout:
        raise LLMCallError("LLM request timeout")
    except requests.exceptions.RequestException as e:
        raise LLMCallError(f"LLM request failed: {e}")


def extract_n_from_llm_response(text: str, options: set[str]) -> Optional[str]:
    """Extract the chosen option name from the LLM output (N-from-1)."""
    text = text.strip()
    for opt in options:
        if opt in text:
            return opt
    return None


# ============================================================================
# Null-value audit
# ============================================================================

def audit_null_values(papers: list[dict]) -> list[dict]:
    """
    Iterate through each paper's nodes and delete three categories of empty-value nodes:
      1) node_original_name == "Not Mentioned" and node_name == null
      2) node_original_name == ""   and node_name == ""
      3) node_original_name == null and node_name == null
    Return the updated papers list (in-place modification).
    """
    print("\n" + "=" * 70)
    print("【Step 1】 Null-value audit")
    print("=" * 70)

    # Count deletions per node_type
    type_deleted: dict[str, dict[str, int]] = {}

    for paper in papers:
        case_id = paper.get("case_id", "?")
        new_nodes = []
        for node in paper.get("nodes", []):
            orig = node.get("node_original_name")
            name = node.get("node_name")

            # Case 1: "Not Mentioned" + null
            if orig == "Not Mentioned" and name is None:
                _record_deletion(node.get("node_type", ""), type_deleted, case_id)
                continue
            # Case 2: "" + ""
            if orig == "" and name == "":
                _record_deletion(node.get("node_type", ""), type_deleted, case_id)
                continue
            # Case 3: null + null
            if orig is None and name is None:
                _record_deletion(node.get("node_type", ""), type_deleted, case_id)
                continue
            # Case 4: "" + null
            if orig == "" and name is None:
                _record_deletion(node.get("node_type", ""), type_deleted, case_id)
                continue
            # Case 5: null + ""
            if orig is None and name == "":
                _record_deletion(node.get("node_type", ""), type_deleted, case_id)
                continue

            new_nodes.append(node)
        paper["nodes"] = new_nodes

    # Print statistics
    _print_null_audit_stats(type_deleted)

    return papers


def _record_deletion(node_type: str, stats: dict, case_id: str):
    if node_type not in stats:
        stats[node_type] = {"total": 0}
    stats[node_type]["total"] = stats[node_type].get("total", 0) + 1


def _print_null_audit_stats(stats: dict):
    if not stats:
        print("  No empty-value nodes were found.")
        return
    for node_type, counters in sorted(stats.items()):
        total = counters.get("total", 0)
        print(f"  {node_type}: {total} node(s) determined to have empty values were detected, and {total} were deleted. The detected and deleted counts match.")
    print()


# ============================================================================
# node_name conformance audit
# ============================================================================

def audit_node_name(papers: list[dict]) -> list[dict]:
    """
    Perform a conformance audit on node_types that have N-from-1 rules:
      - Compliant: pass through
      - Non-compliant: call the LLM to reassign
      - LLM output invalid: programmatically force N-from-1
    Return the updated papers list.
    """
    print("\n" + "=" * 70)
    print("【Step 2】 node_name conformance audit")
    print("=" * 70)

    # Statistics
    stats: dict[str, dict] = {
        nt: {"total": 0, "non_compliant": 0, "llm_fixed": 0, "program_fixed": 0}
        for nt in AUDIT_NODE_TYPES
    }

    for paper in papers:
        case_id = paper.get("case_id", "?")
        for node in paper.get("nodes", []):
            node_type = node.get("node_type", "")
            if node_type not in AUDIT_NODE_TYPES:
                continue

            options = NODE_NAME_RULES[node_type]
            node_name = node.get("node_name", "")
            node_id = node.get("node_id", "?")

            stats[node_type]["total"] += 1

            # Check compliance
            if node_name in options:
                continue  # compliant

            # Non-compliant
            stats[node_type]["non_compliant"] += 1

            # Step 1: call the LLM
            llm_fixed = _llm_correct(node, node_type, options, case_id)

            if llm_fixed is not None:
                node["node_name"] = llm_fixed
                stats[node_type]["llm_fixed"] += 1
                print(f"    [LLM corrected] {node_type} | {node_id}: '{node_name}' -> '{llm_fixed}'")
            else:
                # Step 2: programmatically force N-from-1 (based on node_name similarity)
                program_fixed = _program_correct(node, node_type, options)
                if program_fixed is not None:
                    node["node_name"] = program_fixed
                    stats[node_type]["program_fixed"] += 1
                    print(f"    [Program corrected] {node_type} | {node_id}: '{node_name}' -> '{program_fixed}' (LLM output invalid)")
                else:
                    # Fallback: take the first option
                    fallback = next(iter(options))
                    node["node_name"] = fallback
                    stats[node_type]["program_fixed"] += 1
                    print(f"    [Fallback corrected] {node_type} | {node_id}: '{node_name}' -> '{fallback}' (all attempts failed)")

    # Print statistics
    _print_name_audit_stats(stats)

    return papers


def _build_llm_prompt(node: dict, node_type: str, options: set[str]) -> str:
    """Build the LLM reassignment prompt (Chinese prompt sent to LLM; domain-specific)."""
    node_id = node.get("node_id", "?")
    node_name = node.get("node_name", "")
    orig_name = node.get("node_original_name", "")
    desc = node.get("node_description", "")
    options_str = " | ".join(options)

    prompt = (
        f"【任务】请根据以下信息，从给定的N个选项中，为节点的node_name选择一个最合适的值。\n\n"
        f"【node_id】{node_id}\n"
        f"【node_type】{node_type}\n"
        f"【当前node_name】{node_name}\n"
        f"【node_original_name】{orig_name}\n"
        f"【node_description】{desc}\n\n"
        f"【N选1选项（必须从以下选项中选择一个，禁止输出任何其他内容）】\n"
        f"{options_str}\n\n"
        f"【要求】\n"
        f"1. 只输出选项名称，不要输出任何解释、思考过程、JSON等额外内容。\n"
        f"2. 严格从上述N个选项中选择1个最符合节点信息的名称。\n"
        f"3. 输出必须精确等于选项中的某个值。\n"
    )
    return prompt


def _llm_correct(node: dict, node_type: str, options: set[str], case_id: str) -> Optional[str]:
    """Call the LLM to perform an N-from-1 reassignment for a non-compliant node_name."""
    prompt = _build_llm_prompt(node, node_type, options)
    messages = [
        {"role": "system", "content": "你是一个严格的知识图谱节点分类助手。"},
        {"role": "user", "content": prompt},
    ]
    try:
        response = call_llm(messages)
        # Strictly extract the option
        fixed = extract_n_from_llm_response(response, options)
        if fixed and fixed in options:
            return fixed
        # LLM output does not contain any option: treat as failure
        print(f"    [LLM invalid] {node.get('node_id','?')} LLM output did not match any option: {response[:100]}")
        return None
    except LLMCallError as e:
        print(f"    [LLM error] {node.get('node_id','?')} {e}")
        return None
    except Exception as e:
        print(f"    [LLM error] {node.get('node_id','?')} {e}")
        return None


def _program_correct(node: dict, node_type: str, options: set[str]) -> Optional[str]:
    """Programmatically fall back to an N-from-1 choice based on similarity between node_name and node_original_name."""
    node_name = str(node.get("node_name", "")).strip()
    orig_name = str(node.get("node_original_name", "")).strip()

    if not node_name and not orig_name:
        return None

    # Strategy: extract keywords from node_name and orig_name, then match against options
    text = node_name + " " + orig_name
    text = text.lower()

    # Simple keyword mapping
    KEYWORD_MAP = {
        # 01-Object Domain
        ("Aerospace", "aero", "aircraft", "uav", "无人机"): "Aerospace",
        ("Space", "space", "satellite", "spacecraft"): "Space",
        ("Marine", "ship", "vessel", "naval"): "Marine",
        ("Industrial", "industrial", "manufacturing", "wind turbine"): "Industrial",
        ("Nuclear", "nuclear", "reactor"): "Nuclear",
        ("Electronics", "motor", "transformer", "electronics"): "Electronics",
        ("Vehicle", "vehicle", "automotive", "railway", "car"): "Vehicle",
        ("Other", "other"): "Other",
        # 03-Operating Conditions
        ("Single Condition",): "Single Condition",
        ("Multiple Conditions",): "Multiple Conditions",
        ("Variable Conditions", "time-varying", "non-stationary", "dynamic"): "Variable Conditions",
        # 06-Fault Severity
        ("Single Severity",): "Single Severity",
        ("Multiple Severities",): "Multiple Severities",
        # 07-Compound Fault
        ("No Compound Fault",): "No Compound Fault",
        ("Compound Fault Within Same Structure",): "Compound Fault Within Same Structure",
        ("Compound Fault Across Structures",): "Compound Fault Across Structures",
        # 08-PHM Task
        ("检测", "detection", "detect"): "Detection Task",
        ("诊断", "diagnosis", "classif"): "Diagnosis Task",
        ("预测", "prediction", "rul", "prognos"): "Prediction Task",
        ("评估", "assessment", "evaluat"): "Assessment Task",
        ("Other Task",): "Other Task",
        # 09-Problem Scenario
        ("Small Fault Samples", "few-shot", "few shot", "scarc"): "Small Fault Samples",
        ("Zero Fault Samples", "zero-shot", "zero shot"): "Zero Fault Samples",
        ("分布差异", "domain shift", "cross-domain", "transfer"): "Distribution Discrepancy",
        ("不确定性", "uncertainty", "noise robust"): "Uncertainty",
        ("复合故障", "compound"): "Compound Faults",
        ("复杂系统", "system-level", "complicated"): "Complex Systems",
        ("早期退化", "incipient", "degradation", "rul"): "Early Degradation Prediction",
        ("多源", "多模态", "multimodal", "heterogeneous", "sensor fusion"): "Multi-Source Heterogeneous / Multimodal Data",
        ("可信", "可解释", "interpret", "physics-inform"): "Trustworthiness / Interpretability",
        ("Other",): "Other",
        # 12-Training Data Availability
        ("Zero-Sample", "zero-shot"): "Zero-Sample",
        ("Scarce", "insufficient", "scarce"): "Scarce",
        ("Sufficient",): "Sufficient",
        # 13-Noise Level
        ("High Noise", "noisy", "noise"): "High Noise",
        ("Normal",): "Normal",
        # 14-compute资源类
        ("Low Resource Consumption", "lightweight", "embedded", "flops"): "Low Resource Consumption",
        ("Not Mentioned",): "Not Mentioned",
        ("High Resource Consumption", "computational"): "High Resource Consumption",
    }

    best_match = None
    best_score = 0
    for keywords, option in KEYWORD_MAP.items():
        if option not in options:
            continue
        score = sum(1 for kw in keywords if kw.lower() in text)
        if score > best_score:
            best_score = score
            best_match = option

    return best_match


def _print_name_audit_stats(stats: dict):
    """Print the conformance audit statistics."""
    print()
    for node_type in sorted(stats.keys()):
        s = stats[node_type]
        total = s["total"]
        if total == 0:
            continue
        non = s["non_compliant"]
        llm = s["llm_fixed"]
        prog = s["program_fixed"]
        compliant = total - non
        print(
            f"{node_type}: total node_name count = {total}, non-compliant node_name count = {non}, "
            f"compliant node_name count = {compliant}, LLM-corrected compliant node_name count = {llm}, "
            f"program-corrected (LLM non-compliant) compliant count = {prog}."
        )
    print()
    total_all = sum(s["total"] for s in stats.values())
    non_all = sum(s["non_compliant"] for s in stats.values())
    llm_all = sum(s["llm_fixed"] for s in stats.values())
    prog_all = sum(s["program_fixed"] for s in stats.values())
    compliant_all = total_all - non_all
    print(
        f"Summary: total node_name count = {total_all}, non-compliant node_name count = {non_all}, "
        f"compliant node_name count = {compliant_all}, LLM-corrected compliant node_name count = {llm_all}, "
        f"program-corrected (LLM non-compliant) compliant count = {prog_all}."
    )


# ============================================================================
# Graph-structure conformance audit
# ============================================================================

def audit_graph_structure(papers: list[dict]) -> list[dict]:
    """
    Audit whether the graph JSON conforms to the following nested-structure spec:

    [
      {
        "case_id": <value>,
        "paper_title": <value>,
        "publish_year": <value>,
        "publish_source": <value>,
        "cite_count": <value>,
        "algorithm_hyperparameters": <value>,
        "training_config": <value>,
        "performance_metrics": <value>,
        "nodes": [
          {
            "node_id": <value>,
            "node_type": <value>,
            "node_original_name": <value>,
            "node_name": <value>,
            "node_description": <value>,
            "node_case_id_list": <value>,
          },
          ...
        ]
      },
      ...
    ]

    Audit contents:
      1) Whether the nested structure is closed and well-formed (correct array nesting)
      2) Whether property names at each level are complete and accurate

    Return the updated papers list.
    """
    print("\n" + "=" * 70)
    print("[Step 3] Graph-structure conformance audit")
    print("=" * 70)

    # Required top-level (paper-level) fields
    PAPER_REQUIRED_FIELDS = {
        "case_id",
        "paper_title",
        "publish_year",
        "publish_source",
        "cite_count",
        "algorithm_hyperparameters",
        "training_config",
        "performance_metrics",
        "nodes",
    }

    # Required second-level fields for each item in nodes[]
    NODE_REQUIRED_FIELDS = {
        "node_id",
        "node_type",
        "node_original_name",
        "node_name",
        "node_description",
        "node_case_id_list",
    }

    total_papers = len(papers)
    compliant_papers: list[str] = []
    non_compliant_papers: list[dict] = []

    for paper in papers:
        case_id = str(paper.get("case_id", ""))
        issues: list[str] = []

        # --- Check top-level fields ---
        # 1. Is it a dict?
        if not isinstance(paper, dict):
            issues.append("Top-level element is not a dict object")
            non_compliant_papers.append({"case_id": case_id, "issues": issues})
            continue

        # 2. Is nodes a list?
        nodes = paper.get("nodes")
        if not isinstance(nodes, list):
            issues.append(f"nodes has the wrong type; expected list, got {type(nodes).__name__}")
        else:
            # --- Check each node ---
            for idx, node in enumerate(nodes):
                node_id_val = node.get("node_id", "?") if isinstance(node, dict) else "?"
                # 1) Is it a dict?
                if not isinstance(node, dict):
                    issues.append(
                        f"nodes[{idx}] is not a dict object; it is {type(node).__name__}, node_id={node_id_val}"
                    )
                    continue

                # 2) Are the second-level fields complete?
                missing_node_fields = NODE_REQUIRED_FIELDS - set(node.keys())
                if missing_node_fields:
                    issues.append(
                        f"nodes[{idx}] (node_id={node_id_val}) is missing fields: {sorted(missing_node_fields)}"
                    )

                # 3) Extra second-level fields (informational only, not a compliance violation)
                extra_node_fields = set(node.keys()) - NODE_REQUIRED_FIELDS
                if extra_node_fields:
                    # Not treated as a non-compliant item; recorded in detail only
                    pass

        # 3. Top-level field-missing check (excluding nodes)
        missing_paper_fields = PAPER_REQUIRED_FIELDS - {"nodes"} - set(paper.keys())
        if missing_paper_fields:
            issues.append(f"Top-level is missing fields: {sorted(missing_paper_fields)}")

        # 4. Extra top-level field check (excluding nodes)
        extra_paper_fields = set(paper.keys()) - PAPER_REQUIRED_FIELDS
        if extra_paper_fields:
            # Not treated as a non-compliant item; recorded in detail only
            pass

        # --- Aggregate this paper's audit result ---
        if issues:
            non_compliant_papers.append({"case_id": case_id, "issues": issues})
        else:
            compliant_papers.append(case_id)

    # --- Print detailed results ---
    print(f"\n  【Structure-conformance details】")
    print(f"  Total graphs checked: {total_papers}")

    if non_compliant_papers:
        print(f"\n  Structure-non-compliant graphs ({len(non_compliant_papers)}):")
        for item in non_compliant_papers:
            print(f"    case_id: {item['case_id']}")
            for iss in item["issues"]:
                print(f"      - {iss}")
    else:
        print(f"\n  All {total_papers} graph(s) conform to the structure.")

    # --- Final summary output ---
    print(f"\n  【Structure-conformance summary】")
    print(f"  Total graph case_id count: {total_papers}")
    print(f"  Total graph case_id count checked: {total_papers}")
    print(f"  Structure-compliant graph case_id count: {len(compliant_papers)}")
    print(f"  Structure-non-compliant graph case_id count: {len(non_compliant_papers)}")
    if non_compliant_papers:
        print(f"  Structure-non-compliant case_id list: {[item['case_id'] for item in non_compliant_papers]}")

    return papers


# ============================================================================
# Main flow
# ============================================================================

def run():
    print("=" * 70)
    print("Literature knowledge-graph node conformance audit script")
    print("=" * 70)

    # Step 0: Load graph JSON
    print("\n[Step 0] Loading graph JSON...")
    if not os.path.exists(INPUT_GRAPH_PATH):
        print(f"  [Error] Input file does not exist: {INPUT_GRAPH_PATH}")
        return
    with open(INPUT_GRAPH_PATH, "r", encoding="utf-8") as f:
        papers = json.load(f)
    print(f"  Total papers: {len(papers)}; total nodes: {sum(len(p.get('nodes',[])) for p in papers)}")

    # Step 1: Null-value audit -> papers-v1
    papers = audit_null_values(papers)
    nodes_after_null = sum(len(p.get("nodes", [])) for p in papers)
    print(f"  Total nodes after null-value audit: {nodes_after_null}")

    # Step 2: node_name conformance audit -> papers-v2
    papers = audit_node_name(papers)
    nodes_after_audit = sum(len(p.get("nodes", [])) for p in papers)
    print(f"  Total nodes after conformance audit: {nodes_after_audit}")

    # Step 3: Graph structure conformance audit
    papers = audit_graph_structure(papers)

    # Step 4: Output
    print("\n[Step 4] Saving results...")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    input_filename = os.path.basename(INPUT_GRAPH_PATH)
    name_part, ext_part = os.path.splitext(input_filename)
    output_filename = f"{name_part}_conformance_audit.json"
    output_path = os.path.join(OUTPUT_DIR, output_filename)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(papers, f, ensure_ascii=False, indent=2)
    print(f"  Saved to: {output_path}")
    print(f"  Final: {len(papers)} paper(s), {nodes_after_audit} node(s)")

    print("\n" + "=" * 70)
    print("Audit complete")
    print("=" * 70)


if __name__ == "__main__":
    run()
