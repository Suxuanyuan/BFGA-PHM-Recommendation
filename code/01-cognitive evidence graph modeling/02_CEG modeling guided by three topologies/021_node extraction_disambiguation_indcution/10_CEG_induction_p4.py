# -*- coding: utf-8 -*-
"""
Literature knowledge-graph node-conformance audit script v9 - induction-generation compliance audit
========================================================================
Functions:
  1. Null-value audit: traverse each node{} of the graph JSON and delete the five categories of null-valued nodes
  2. node_name conformance audit: audit and correct node_types that have N-of-1 rules (uses LLM + programmatic fallback)
  3. Graph-structure conformance audit: group by node_type and check nested structure and attribute names
  4. Induction-generation consistency audit: base vs -Induction pairing audit for node_type 15-19

Input:
  - Graph JSON: A2-merged_nodes_disambiguation_induction/[...].json
  - Prompt md: v5-version prompts/*.md (4 files)

Output:
  - Graph JSON-v2: with the suffix "_conformance_audit", written to the same directory as the input file
"""

import os
import json
import requests
import copy
from typing import Optional


# ============================================================================
# Configuration
# ============================================================================

API_KEY = ""  # TODO: Provide your own API key before running
API_URL = os.environ.get("BFGA_LLM_API_URL", "https://YOUR.LLM.ENDPOINT/v1/chat/completions")
LLM_MODEL = "gemini-3.5-flash"
LLM_TIMEOUT = 300
LLM_TEMPERATURE = 0.0

INPUT_GRAPH_PATH = r"./data/03_induction/[2277EAKD][ZZZRPFBV]合并节点_规范性审查_合并_规范性审查_消歧_规范性审查_归纳.json"

OUTPUT_DIR = r"./data/03_induction"

# ============================================================================
# N-of-1 rules (extracted from the prompt md; embedded in code)
# ============================================================================

NODE_NAME_RULES: dict[str, set[str]] = {
    # 01-Object-Domain Class: 8-of-1
    "01-Object Domain": {
        "Aerospace", "Space", "Marine", "Industrial", "Nuclear", "Electronics", "Vehicle", "Other",
    },
    # 03-Operating-Condition Class: 3-of-1
    "03-Operating Conditions": {
        "Single Condition", "Multiple Conditions", "Variable Conditions",
    },
    # 06-Fault-Severity Class: 2-of-1
    "06-Fault Severity": {
        "Single Severity", "Multiple Severities",
    },
    # 07-Composite-Fault-Included Class: 3-of-1
    "07-Compound Fault": {
        "No Compound Fault", "Compound Fault Within Same Structure", "Compound Fault Across Structures",
    },
    # 08-PHM-Task Class: 5-of-1
    "08-PHM Task": {
        "Detection Task", "Diagnosis Task", "Prediction Task", "Assessment Task", "Other Task",
    },
    # 09-Problem-Scenario Class: 10-of-1
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
    # 12-Training Data Availability：3选1
    "12-Training Data Availability": {
        "Zero-Sample", "Scarce", "Sufficient",
    },
    # 13-Noise Level：2选1
    "13-Noise Level": {
        "High Noise", "Normal",
    },
    # 14-compute资源类：3选1
    "14-Computational Resource": {
        "Low Resource Consumption", "Not Mentioned", "High Resource Consumption",
    },
}

# Node types to audit (those with N-from-1 constraints)
AUDIT_NODE_TYPES = set(NODE_NAME_RULES.keys())

# ============================================================================
# LLM client
# ============================================================================

class LLMCallError(Exception):
    pass


def call_llm(messages: list[dict]) -> str:
    """Call LLM，返回纯文本内容"""
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
    """从LLM output中提取N选1的选项名称"""
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
    Iterate over all papers' nodes; delete the following five categories of null-value nodes:
      1) node_original_name == "Not Mentioned" and node_name == null
      2) node_original_name == ""   and node_name == ""
      3) node_original_name == null and node_name == null
      4) node_original_name == ""   and node_name == null
      5) node_original_name == null and node_name == ""
    Returns the updated papers list (mutated in place).
    """
    print("\n" + "=" * 70)
    print("[Step 1] Null-value audit")
    print("=" * 70)

    # Statistics per node_type
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
        print("  未发现空值节点。")
        return
    for node_type, counters in sorted(stats.items()):
        total = counters.get("total", 0)
        print(f"  {node_type}：经判定存在各类空值的node{{}}为{total}个，删除{total}个。经判定存在的数量和删除的数量相等。")
    print()


# ============================================================================
# node_name conformance audit
# ============================================================================

def audit_node_name(papers: list[dict]) -> list[dict]:
    """
    Run conformance audits for node_types with N-from-1 rules:
      - Compliant: pass through
      - Non-compliant: call LLM for a second assignment
      - LLM output is non-compliant: enforce N-from-1 programmatically
    Returns the updated papers list.
    """
    print("\n" + "=" * 70)
    print("[Step 2] node_name conformance audit")
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
                continue  # Compliant

            # Non-compliant
            stats[node_type]["non_compliant"] += 1

            # Step 1: call LLM
            llm_fixed = _llm_correct(node, node_type, options, case_id)

            if llm_fixed is not None:
                node["node_name"] = llm_fixed
                stats[node_type]["llm_fixed"] += 1
                print(f"    [LLM fix] {node_type} | {node_id}: '{node_name}' -> '{llm_fixed}'")
            else:
                # Step 2: enforce N-from-1 programmatically (judge by node_name similarity)
                program_fixed = _program_correct(node, node_type, options)
                if program_fixed is not None:
                    node["node_name"] = program_fixed
                    stats[node_type]["program_fixed"] += 1
                    print(f"    [Program fix] {node_type} | {node_id}: '{node_name}' -> '{program_fixed}' (LLM output invalid)")
                else:
                    # Fallback: take the first option
                    fallback = next(iter(options))
                    node["node_name"] = fallback
                    stats[node_type]["program_fixed"] += 1
                    print(f"    [Fallback fix] {node_type} | {node_id}: '{node_name}' -> '{fallback}' (all attempts failed)")

    # Print statistics
    _print_name_audit_stats(stats)

    return papers


def _build_llm_prompt(node: dict, node_type: str, options: set[str]) -> str:
    """Build the LLM reassignment prompt"""
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
    """Call LLM对不合规node_name进行N选1赋值"""
    prompt = _build_llm_prompt(node, node_type, options)
    messages = [
        {"role": "system", "content": "你是一个严格的知识图谱节点分类助手。"},
        {"role": "user", "content": prompt},
    ]
    try:
        response = call_llm(messages)
        # Strictly extract an option
        fixed = extract_n_from_llm_response(response, options)
        if fixed and fixed in options:
            return fixed
        # LLM output does not contain an option; treat as failure
        print(f"    [LLM invalid] {node.get('node_id','?')} LLM output does not match any option: {response[:100]}")
        return None
    except LLMCallError as e:
        print(f"    [LLM exception] {node.get('node_id','?')} {e}")
        return None
    except Exception as e:
        print(f"    [LLM exception] {node.get('node_id','?')} {e}")
        return None


def _program_correct(node: dict, node_type: str, options: set[str]) -> Optional[str]:
    """Programmatically enforce N-from-1 based on the similarity between node_name and node_original_name"""
    node_name = str(node.get("node_name", "")).strip()
    orig_name = str(node.get("node_original_name", "")).strip()

    if not node_name and not orig_name:
        return None

    text = node_name + " " + orig_name
    text = text.lower()

    KEYWORD_MAP = {
        # 01-Object Domain
        ("Aerospace", "aero", "aircraft", "uav", "unmanned"): "Aerospace",
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
        ("Variable Conditions", "time-varying", "non-stationary", "dynamic", "nonstationary"): "Variable Conditions",
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
    """print规范性auditaggregate"""
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
            f"{node_type}：node_name总数为{total}个，不合规node_name数量为{non}个，"
            f"合规node_name数量为{compliant}个，经LLM纠正后合规node_name数量为{llm}个，"
            f"经过LLM纠正后不合规node_name但经程序强行纠正合规数量为{prog}个。"
        )
    print()
    total_all = sum(s["total"] for s in stats.values())
    non_all = sum(s["non_compliant"] for s in stats.values())
    llm_all = sum(s["llm_fixed"] for s in stats.values())
    prog_all = sum(s["program_fixed"] for s in stats.values())
    compliant_all = total_all - non_all
    print(
        f"合计：node_name总数为{total_all}个，不合规node_name数量为{non_all}个，"
        f"合规node_name数量为{compliant_all}个，经LLM纠正后合规node_name数量为{llm_all}个，"
        f"经过LLM纠正后不合规node_name但经程序强行纠正合规数量为{prog_all}个。"
    )


# ============================================================================
# Graph-structure conformance audit
# ============================================================================

# node_type 01-14 (base): required fields (node_algorithm_class must be null)
STRUCT_BASE_FIELDS = {
    "node_id", "node_type", "node_original_name",
    "node_name", "node_description",
    "node_num", "node_cite_score", "node_cite_count",
    "node_weight", "node_algorithm_class", "node_id_list",
}

# node_type 15-19 (without -Induction suffix): required fields + node_importance
STRUCT_ALGO_FIELDS = {
    "node_id", "node_type", "node_original_name",
    "node_name", "node_description",
    "node_num", "node_cite_score", "node_cite_count",
    "node_weight", "node_algorithm_class", "node_id_list",
    "node_importance",
}

# node_type 15-19 (with -Induction suffix): required fields (no node_algorithm_class)
STRUCT_INDUCTION_FIELDS = {
    "node_id", "node_type", "node_original_name",
    "node_name", "node_description",
    "node_num", "node_cite_score", "node_cite_count",
    "node_weight", "node_id_list",
}

# Valid values for node_importance (5-2 rule)
_VALID_IMPORTANCE = {"最高重要性", "一般重要性", "Not Mentioned"}

# node_type prefix -> corresponding rule key (without -Induction)
_ALGO_PREFIXES = (
    "15-Data Preprocessing Algorithm",
    "16-Feature Extraction Algorithm",
    "17-Core Classifier Algorithm",
    "18-Data Generation Algorithm",
    "19-Training Optimization Algorithm",
)


def _classify_node(node_type: str) -> str:
    """
    Classify a node based on its node_type:
      - "base"    : 01-14 (base, no -Induction)
      - "algo"    : 15-19, without -Induction suffix (algorithm)
      - "induction": 15-19, with -Induction suffix (induction)
    """
    if node_type.endswith("-Induction"):
        return "induction"
    # Exact-match 15-19 prefixes (exclude base-style formats like "15-xxx")
    for prefix in _ALGO_PREFIXES:
        if node_type == prefix:
            return "algo"
    return "base"


def _get_structure_fields(node_type: str) -> set[str]:
    """Return the set of required fields for a given node_type"""
    cls = _classify_node(node_type)
    if cls == "induction":
        return STRUCT_INDUCTION_FIELDS
    if cls == "algo":
        return STRUCT_ALGO_FIELDS
    return STRUCT_BASE_FIELDS


def audit_graph_structure(papers: list[dict]) -> list[dict]:
    """
    Graph-structure conformance audit (rules 5-1 / 5-2 / 5-3).

    5-1: node_type 01-14 (base)
         - all required fields present
         - node_algorithm_class must be null

    5-2: node_type 15-19 (without -Induction suffix)
         - all required fields present
         - node_importance must be one of {"最高重要性", "一般重要性", "Not Mentioned"}
         - for each such node{}, use node_id + "-Induction" to find the corresponding
           induction node{}; require node_algorithm_class === induction node{}.node_name

    5-3: node_type 15-19 (with -Induction suffix)
         - all required fields present
         - node_algorithm_class field must not appear

    5-5 输出：
      图谱case_id{}总数、已检查数、结构合规数、结构不合规数，
      以及不合规 case_id / node_type / node_id 明细。
    """
    print("\n" + "=" * 70)
    print("【Step 3】图谱结构规范性审查")
    print("=" * 70)

    # ---------- 全局归纳节点索引（用于 5-2 配对check） ----------
    # { node_id: node }
    induction_index: dict[str, dict] = {}
    for paper in papers:
        for node in paper.get("nodes", []):
            nt = node.get("node_type", "")
            if nt.endswith("-Induction"):
                nid = node.get("node_id", "")
                if nid:
                    induction_index[nid] = node

    # ---------- 顶层必须字段 ----------
    PAPER_REQUIRED_FIELDS = {
        "case_id", "paper_title", "publish_year",
        "publish_source", "cite_count",
        "algorithm_hyperparameters", "training_config",
        "performance_metrics", "nodes",
    }

    # ---------- 汇总aggregate ----------
    total_papers = len(papers)
    compliant_papers: list[str] = []
    non_compliant_papers: list[dict] = []

    # node_importance 修复记录（用于复审）
    importance_fixes: list[dict] = []

    for paper in papers:
        case_id = str(paper.get("case_id", ""))
        issues: list[dict] = []   # {node_id, node_type, rule, detail}

        # ---- 1. 顶层类型check ----
        if not isinstance(paper, dict):
            issues.append({
                "node_id": case_id, "node_type": "顶层",
                "rule": "结构", "detail": "顶层元素不是 dict 对象"
            })
            non_compliant_papers.append({"case_id": case_id, "issues": issues})
            continue

        # ---- 2. 顶层字段check ----
        missing_top = PAPER_REQUIRED_FIELDS - {"nodes"} - set(paper.keys())
        if missing_top:
            issues.append({
                "node_id": case_id, "node_type": "顶层",
                "rule": "5-4",
                "detail": f"顶层缺少属性: {sorted(missing_top)}"
            })

        nodes = paper.get("nodes")
        if not isinstance(nodes, list):
            issues.append({
                "node_id": case_id, "node_type": "nodes",
                "rule": "5-4",
                "detail": f"nodes 属性类型错误，期望 list，实际为 {type(nodes).__name__}"
            })
            non_compliant_papers.append({"case_id": case_id, "issues": issues})
            continue

        # ---- 3. 每个 node{} 的结构check ----
        for idx, node in enumerate(nodes):
            node_id_val = str(node.get("node_id", f"第{idx}个节点"))
            node_type = str(node.get("node_type", ""))

            if not isinstance(node, dict):
                issues.append({
                    "node_id": node_id_val, "node_type": node_type,
                    "rule": "5-4",
                    "detail": f"nodes[{idx}] 不是 dict 对象，而是 {type(node).__name__}"
                })
                continue

            # 3.1 根据 node_type 确定规则分类
            cls = _classify_node(node_type)

            # 3.2 必须字段check（5-4 规则）
            required_fields = _get_structure_fields(node_type)
            if cls == "induction":
                # 5-3：归纳节点不得出现 node_algorithm_class
                extra_forbidden = {"node_algorithm_class"} & set(node.keys())
                if extra_forbidden:
                    issues.append({
                        "node_id": node_id_val, "node_type": node_type,
                        "rule": "5-3",
                        "detail": f"归纳类node{{}}不应出现属性: {sorted(extra_forbidden)}"
                    })
            if required_fields:
                missing = required_fields - set(node.keys())
                if missing:
                    issues.append({
                        "node_id": node_id_val, "node_type": node_type,
                        "rule": "5-4",
                        "detail": f"缺少属性: {sorted(missing)}"
                    })

            # 3.3 5-1：基础类 node_algorithm_class 必须为 null
            if cls == "base":
                alg_cls = node.get("node_algorithm_class")
                if alg_cls is not None:
                    issues.append({
                        "node_id": node_id_val, "node_type": node_type,
                        "rule": "5-1",
                        "detail": f"基础类node{{}}的node_algorithm_class必须为null，实际为: {repr(alg_cls)}"
                    })

            # 3.4 5-2：算法类额外规则
            if cls == "algo":
                # (a) node_importance 三选一；不合规时原地修正为"Not Mentioned"
                importance = node.get("node_importance")
                if importance not in _VALID_IMPORTANCE:
                    issues.append({
                        "node_id": node_id_val, "node_type": node_type,
                        "rule": "5-2",
                        "detail": (
                            f"node_importance必须为{{最高重要性/一般重要性/未提及}}之一，"
                            f"实际为: {repr(importance)}，已强制赋值为'未提及'"
                        )
                    })
                    node["node_importance"] = "Not Mentioned"
                    importance_fixes.append({
                        "case_id": case_id,
                        "node_id": node_id_val,
                        "node_type": node_type,
                        "old_value": importance,
                    })

                # (b) node_algorithm_class 必须与归纳 node{} 的 node_name 严格一致
                node_id_alg = node.get("node_id", "")
                if node_id_alg:
                    node_id_induction = node_id_alg + "-Induction"
                    matched_induction = induction_index.get(node_id_induction)
                    if matched_induction is None:
                        issues.append({
                            "node_id": node_id_val, "node_type": node_type,
                            "rule": "5-2",
                            "detail": (
                                f"未找到对应的归纳节点 (node_id={node_id_induction})，"
                                f"无法验证node_algorithm_class一致性"
                            )
                        })
                    else:
                        alg_cls_val = node.get("node_algorithm_class")
                        induction_name = matched_induction.get("node_name", "")
                        if alg_cls_val != induction_name:
                            issues.append({
                                "node_id": node_id_val, "node_type": node_type,
                                "rule": "5-2",
                                "detail": (
                                    f"node_algorithm_class(={repr(alg_cls_val)}) "
                                    f"必须等于对应归纳node{{}}的node_name(={repr(induction_name)})"
                                )
                            })

        if issues:
            non_compliant_papers.append({"case_id": case_id, "issues": issues})
        else:
            compliant_papers.append(case_id)

    # ---------- print结果（5-5 格式） ----------
    print(f"\n  【结构规范性检查详情】")
    print(f"  检查的图谱总数: {total_papers} 篇")

    if non_compliant_papers:
        print(f"\n  结构不合规的图谱 ({len(non_compliant_papers)} 篇)：")
        for item in non_compliant_papers:
            print(f"    case_id: {item['case_id']}")
            for iss in item["issues"]:
                print(f"      [rule={iss['rule']}] node_type={iss['node_type']}, node_id={iss['node_id']}")
                print(f"        {iss['detail']}")
    else:
        print(f"\n  所有 {total_papers} 篇图谱结构均合规。")

    print(f"\n  [Graph-structure conformance summary]")
    print(f"  Number of graph case_id{{}}: {total_papers}")
    print(f"  Number of graph case_id{{}} checked: {total_papers}")
    print(f"  Number of structurally-compliant case_id{{}}: {len(compliant_papers)}")
    print(f"  Number of structurally-non-compliant case_id{{}}: {len(non_compliant_papers)}")
    if non_compliant_papers:
        print(f"  List of non-compliant case_ids: {[item['case_id'] for item in non_compliant_papers]}")
        # Extra: summarize non-compliant node{} counts by node_type
        node_type_count: dict[str, int] = {}
        for item in non_compliant_papers:
            for iss in item["issues"]:
                nt = iss.get("node_type", "top-level")
                node_type_count[nt] = node_type_count.get(nt, 0) + 1
        print(f"  Non-compliant node_type statistics: {dict(sorted(node_type_count.items()))}")

    # ---------- Re-audit after repair (only node_importance) ----------
    if importance_fixes:
        print(f"\n  [node_importance repair log] total repairs: {len(importance_fixes)}")
        for fix in importance_fixes:
            print(
                f"    case_id={fix['case_id']}, node_id={fix['node_id']}, "
                f"node_type={fix['node_type']}, "
                f"old={repr(fix['old_value'])} -> new='Not Mentioned'"
            )

        # Re-audit all algo nodes' node_importance (after repair)
        print(f"\n  [Post-repair re-audit] node_importance compliance:")
        recheck_pass = 0
        recheck_fail = 0
        recheck_detail: list[dict] = []
        for paper in papers:
            case_id = str(paper.get("case_id", ""))
            for node in paper.get("nodes", []):
                nt = str(node.get("node_type", ""))
                if _classify_node(nt) == "algo":
                    imp = node.get("node_importance")
                    if imp in _VALID_IMPORTANCE:
                        recheck_pass += 1
                    else:
                        recheck_fail += 1
                        recheck_detail.append({
                            "case_id": case_id,
                            "node_id": str(node.get("node_id", "?")),
                            "node_type": nt,
                            "value": imp,
                        })
        print(f"    Compliant nodes: {recheck_pass}")
        print(f"    Still non-compliant nodes: {recheck_fail}")
        if recheck_detail:
            for d in recheck_detail:
                print(
                    f"      case_id={d['case_id']}, node_id={d['node_id']}, "
                    f"node_type={d['node_type']}, value={repr(d['value'])}"
                )
        print(f"\n  [node_importance re-audit conclusion]: {'all compliant' if recheck_fail == 0 else f'still {recheck_fail} non-compliant'}")

    return papers


# ============================================================================
# Induction-generation consistency audit
# ============================================================================

def audit_induction_consistency(papers: list[dict]) -> list[dict]:
    """
    Iterate the graph JSON-v2; perform consistency audit on node_types 15-19:

    For each node_type (e.g. 17-Core Classifier Algorithm),
    collect its node_id array (alg_xx_group) and the corresponding -Induction array
    (alg_xx_induction_group), then compare the element counts.

    If they differ, perform a string fix ("-Induction" suffix appended) for each node_id
    in alg_xx_group and check whether it exists in alg_xx_induction_group; if not, record
    it as wrong_node_id.
    """
    print("\n" + "=" * 70)
    print("[Step 4] Induction-generation consistency audit")
    print("=" * 70)

    # Base type -> Induction type mapping
    algo_pairs = [
        ("15-Data Preprocessing Algorithm",       "15-Data Preprocessing Algorithm-Induction"),
        ("16-Feature Extraction Algorithm",         "16-Feature Extraction Algorithm-Induction"),
        ("17-Core Classifier Algorithm",       "17-Core Classifier Algorithm-Induction"),
        ("18-Data Generation Algorithm",         "18-Data Generation Algorithm-Induction"),
        ("19-Training Optimization Algorithm",         "19-Training Optimization Algorithm-Induction"),
    ]

    # Aggregate statistics
    all_passed = True

    for base_type, induction_type in algo_pairs:
        alg_group: list[str] = []
        alg_induction_group: list[str] = []

        # Collect node_ids
        for paper in papers:
            for node in paper.get("nodes", []):
                if node.get("node_type") == base_type:
                    nid = node.get("node_id", "")
                    if nid:
                        alg_group.append(nid)
                elif node.get("node_type") == induction_type:
                    nid = node.get("node_id", "")
                    if nid:
                        alg_induction_group.append(nid)

        N1 = len(alg_group)
        N2 = len(alg_induction_group)

        if N1 == N2:
            result_str = "passed"
            wrong_ids: list[str] = []
        else:
            result_str = "failed"
            all_passed = False
            wrong_ids = []
            induction_set = set(alg_induction_group)
            for node_id1 in alg_group:
                node_id2 = node_id1 + "-Induction"
                if node_id2 not in induction_set:
                    wrong_ids.append(node_id1)

        # Print
        if wrong_ids:
            wrong_str = ", ".join(wrong_ids)
        else:
            wrong_str = "none"

        print(
            f"  node_type=\"{base_type}\", algorithm node count=<{N1}>, "
            f"induction node count=<{N2}>, <{result_str}>, "
            f"non-matching node_id details=<{wrong_str}>"
        )

    print()
    if all_passed:
        print("  [Induction-generation consistency audit] all passed")
    else:
        print("  [Induction-generation consistency audit] mismatches found; see above")

    return papers


# ============================================================================
# Main flow
# ============================================================================

def run():
    print("=" * 70)
    print("Literature knowledge-graph node conformance audit script v9")
    print("  -- Induction-generation compliance audit")
    print("=" * 70)

    # Step 0: read graph JSON
    print("\n[Step 0] Reading graph JSON...")
    if not os.path.exists(INPUT_GRAPH_PATH):
        print(f"  [Error] Input file does not exist: {INPUT_GRAPH_PATH}")
        return
    with open(INPUT_GRAPH_PATH, "r", encoding="utf-8") as f:
        papers = json.load(f)
    print(f"  Total papers: {len(papers)}, total nodes: {sum(len(p.get('nodes', [])) for p in papers)}")

    # Step 1: null-value audit -> papers-v1
    papers = audit_null_values(papers)
    nodes_after_null = sum(len(p.get("nodes", [])) for p in papers)
    print(f"  Total nodes after null-value audit: {nodes_after_null}")

    # Step 2: node_name conformance audit -> papers-v2
    papers = audit_node_name(papers)
    nodes_after_audit = sum(len(p.get("nodes", [])) for p in papers)
    print(f"  Total nodes after conformance audit: {nodes_after_audit}")

    # Step 3: graph-structure conformance audit
    papers = audit_graph_structure(papers)

    # Step 4: induction-generation consistency audit
    papers = audit_induction_consistency(papers)

    # Step 5: output
    print("\n[Step 5] Saving results...")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    input_filename = os.path.basename(INPUT_GRAPH_PATH)
    name_part, ext_part = os.path.splitext(input_filename)
    output_filename = f"{name_part}_conformance_audit.json"
    output_path = os.path.join(OUTPUT_DIR, output_filename)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(papers, f, ensure_ascii=False, indent=2)
    print(f"  Saved to: {output_path}")
    print(f"  Final: {len(papers)} papers, {nodes_after_audit} nodes")

    print("\n" + "=" * 70)
    print("Audit completed")
    print("=" * 70)


if __name__ == "__main__":
    run()
