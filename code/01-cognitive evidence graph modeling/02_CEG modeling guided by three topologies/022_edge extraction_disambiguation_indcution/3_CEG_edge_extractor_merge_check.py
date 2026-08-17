# -*- coding: utf-8 -*-
r"""
Edge-merge graph conformance-audit script zotero_knowledge_graph_edge_extractor_merge_conformance_audit_v8.py
========================================================================
Functions:
  Perform 5 categories of conformance audits on the JSON produced by "edge merge":
    1. Node null-value audit: delete edges whose source/target nodes have null values ("not mentioned" / "" / null)
    2. Node node_name conformance audit (N-of-1 rule): strictly match the node_name
       of source/target nodes against N-of-1; non-compliant ones are reassigned via LLM;
       still non-compliant after LLM are forced to N-of-1 by program.
    3. Edge completeness audit: completeness audits for 01-default edges, 02-causal edges,
       02-causal edges supplement, 03-evidence edges; invalid case_ids are written to the audit log md.
    4. Graph-structure conformance audit: check whether the nested structure and property
       names are compliant.
    5. Output the audited graph JSON to the same directory as the input, with the suffix
       "_conformance_audit" appended to the filename.

Inputs:
  1. Edge-graph json:
     ./data/03_induction/B0-edges_merged/225KHNN8+YPWGNCJD+merged-edges.json   <-- RELATIVE PATH placeholder
  2. 4 node prompt md files (used to extract the N-of-1 rule), exactly matching the
     MD file names in the schema directory:
     - 01-03,08-09 nodes.md
     - 04-07 nodes.md
     - 10-14 nodes.md
     - 15-20 nodes.md

Outputs:
  - Audited graph json: <input-filename>_conformance_audit.json (same directory as input)
  - Audit log md: <input-filename>_conformance_audit.md (same directory as input), recording:
      · Node null-value audit
      · Node node_name conformance audit
      · Edge completeness audit (01-default / 02-causal / 02-causal-supplement / 03-evidence)
      · Graph-structure conformance audit

LLM configuration:
  When calling the LLM, use the viviai proxy (consistent with v7_merge_conformance_audit.py).
  Provide your own API key below.
"""

import os
import re
import json
import time
import requests
from typing import Optional


# ============================================================================
# Configuration
# ============================================================================

# --- input1: edge-graph json (RELATIVE PATH placeholder) ---
INPUT_GRAPH_PATH = (
    r"./data/03_induction/B0-edges_merged/225KHNN8+KC8MEE2V+merged-edges_conformance_audit_merged.json"
)

# --- input2: 4 nodes prompt md (used to extract N-of-1 rule) ---
# File names exactly match the actual MD file names in the schema directory.
PROMPT_FILES = [
    r"./data/02_consensus_graph/prompts/04-07 nodes.md",
    r"./data/02_consensus_graph/prompts/10-14 nodes.md",
    r"./data/02_consensus_graph/prompts/15-20 nodes.md",
    r"./data/02_consensus_graph/prompts/01-03,08-09 nodes.md",
]

# Output directory (same as input directory)
OUTPUT_DIR = os.path.dirname(INPUT_GRAPH_PATH)

# --- LLM configuration (consistent with v7_merge_compliant_audit.py) ---
API_KEY = ""  # TODO: replace with your own API key
API_URL = os.environ.get("BFGA_LLM_API_URL", "https://YOUR.LLM.ENDPOINT/v1/chat/completions")
LLM_MODEL = "gemini-3.5-flash"
LLM_TIMEOUT = 300
LLM_TEMPERATURE = 0.0


# ============================================================================
# N-of-1 rules (extracted from Prompt md and written into the program)
# ============================================================================
# Strictly follow the N-of-1 descriptions in the Prompt:
#   01-object-domain-class: 8 choose 1
#   03-operating-condition-class: 3 choose 1
#   06-fault-severity-class: 2 choose 1
#   07-composite-fault-included: 3 choose 1
#   08-PHM-task-class: 5 choose 1
#   09-problem-scenario-class: 10 choose 1 (multi-select up to 3; single-node picks one)
#   12-available-training-data: 3 choose 1
#   13-noise-level-class: 2 choose 1
#   14-compute-resource-class: 3 choose 1
# The remainder (02/04/05/10/11/15-19/20) per the Prompt specify node_name = null; they are not included in the N-of-1 audit.

NODE_NAME_RULES: dict[str, set[str]] = {
    "01-Object Domain": {
        "Aerospace", "Space", "Marine", "Industrial", "Nuclear", "Electronics", "Vehicle", "Other",
    },
    "03-Operating Conditions": {
        "Single Condition", "Multiple Conditions", "Variable Conditions",
    },
    "06-Fault Severity": {
        "Single Severity", "Multiple Severities",
    },
    "07-Compound Fault": {
        "No Compound Fault", "Compound Fault Within Same Structure", "Compound Fault Across Structures",
    },
    "08-PHM Task": {
        "Detection Task", "Diagnosis Task", "Prediction Task", "Assessment Task", "Other Task",
    },
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
    "12-Training Data Availability": {
        "Zero-Sample", "Scarce", "Sufficient",
    },
    "13-Noise Level": {
        "High Noise", "Normal",
    },
    "14-Computational Resource": {
        "Low Resource Consumption", "Not Mentioned", "High Resource Consumption",
    },
}

# Node types that need to be included in the node_name conformance audit and aggregation
# (those with N-of-1 requirements)
AUDIT_NODE_TYPES: set[str] = set(NODE_NAME_RULES.keys())


# ============================================================================
# Edge-completeness preset rules (from v5 edge Prompt/edge_rules.md + user requirements)
# ============================================================================

# 01-default edges (source_node_type, target_node_type) full set
DEFAULT_EDGE_FULL: list[tuple[str, str]] = [
    ("01-Object Domain", "15-Data Preprocessing Algorithm"),
    ("01-Object Domain", "16-Feature Extraction Algorithm"),
    ("01-Object Domain", "17-Core Classifier Algorithm"),
    ("01-Object Domain", "18-Data Generation Algorithm"),
    ("01-Object Domain", "19-Training Optimization Algorithm"),
    ("02-Object Type", "15-Data Preprocessing Algorithm"),
    ("02-Object Type", "16-Feature Extraction Algorithm"),
    ("02-Object Type", "17-Core Classifier Algorithm"),
    ("02-Object Type", "18-Data Generation Algorithm"),
    ("02-Object Type", "19-Training Optimization Algorithm"),
    ("03-Operating Conditions", "15-Data Preprocessing Algorithm"),
    ("03-Operating Conditions", "16-Feature Extraction Algorithm"),
    ("03-Operating Conditions", "17-Core Classifier Algorithm"),
    ("03-Operating Conditions", "18-Data Generation Algorithm"),
    ("03-Operating Conditions", "19-Training Optimization Algorithm"),
    ("04-Fault Location", "15-Data Preprocessing Algorithm"),
    ("04-Fault Location", "16-Feature Extraction Algorithm"),
    ("04-Fault Location", "17-Core Classifier Algorithm"),
    ("04-Fault Location", "18-Data Generation Algorithm"),
    ("04-Fault Location", "19-Training Optimization Algorithm"),
    ("05-Fault Mode", "15-Data Preprocessing Algorithm"),
    ("05-Fault Mode", "16-Feature Extraction Algorithm"),
    ("05-Fault Mode", "17-Core Classifier Algorithm"),
    ("05-Fault Mode", "18-Data Generation Algorithm"),
    ("05-Fault Mode", "19-Training Optimization Algorithm"),
    ("06-Fault Severity", "15-Data Preprocessing Algorithm"),
    ("06-Fault Severity", "16-Feature Extraction Algorithm"),
    ("06-Fault Severity", "17-Core Classifier Algorithm"),
    ("06-Fault Severity", "18-Data Generation Algorithm"),
    ("06-Fault Severity", "19-Training Optimization Algorithm"),
    ("07-Compound Fault", "15-Data Preprocessing Algorithm"),
    ("07-Compound Fault", "16-Feature Extraction Algorithm"),
    ("07-Compound Fault", "17-Core Classifier Algorithm"),
    ("07-Compound Fault", "18-Data Generation Algorithm"),
    ("07-Compound Fault", "19-Training Optimization Algorithm"),
    ("08-PHM Task", "15-Data Preprocessing Algorithm"),
    ("08-PHM Task", "16-Feature Extraction Algorithm"),
    ("08-PHM Task", "17-Core Classifier Algorithm"),
    ("08-PHM Task", "18-Data Generation Algorithm"),
    ("08-PHM Task", "19-Training Optimization Algorithm"),
    ("09-Problem Scenario", "15-Data Preprocessing Algorithm"),
    ("09-Problem Scenario", "16-Feature Extraction Algorithm"),
    ("09-Problem Scenario", "17-Core Classifier Algorithm"),
    ("09-Problem Scenario", "18-Data Generation Algorithm"),
    ("09-Problem Scenario", "19-Training Optimization Algorithm"),
    ("10-Dataset", "15-Data Preprocessing Algorithm"),
    ("10-Dataset", "16-Feature Extraction Algorithm"),
    ("10-Dataset", "17-Core Classifier Algorithm"),
    ("10-Dataset", "18-Data Generation Algorithm"),
    ("10-Dataset", "19-Training Optimization Algorithm"),
    ("11-Sensor Information", "15-Data Preprocessing Algorithm"),
    ("11-Sensor Information", "16-Feature Extraction Algorithm"),
    ("11-Sensor Information", "17-Core Classifier Algorithm"),
    ("11-Sensor Information", "18-Data Generation Algorithm"),
    ("11-Sensor Information", "19-Training Optimization Algorithm"),
    ("12-Training Data Availability", "15-Data Preprocessing Algorithm"),
    ("12-Training Data Availability", "16-Feature Extraction Algorithm"),
    ("12-Training Data Availability", "17-Core Classifier Algorithm"),
    ("12-Training Data Availability", "18-Data Generation Algorithm"),
    ("12-Training Data Availability", "19-Training Optimization Algorithm"),
    ("13-Noise Level", "15-Data Preprocessing Algorithm"),
    ("13-Noise Level", "16-Feature Extraction Algorithm"),
    ("13-Noise Level", "17-Core Classifier Algorithm"),
    ("13-Noise Level", "18-Data Generation Algorithm"),
    ("13-Noise Level", "19-Training Optimization Algorithm"),
    ("14-Computational Resource", "15-Data Preprocessing Algorithm"),
    ("14-Computational Resource", "16-Feature Extraction Algorithm"),
    ("14-Computational Resource", "17-Core Classifier Algorithm"),
    ("14-Computational Resource", "18-Data Generation Algorithm"),
    # NOTE: original draft wrote "14-compute-resource-class | 19-training-optimization-algorithm-classclass"
    # with an extra trailing "class"; the correct name in Prompt edge_rules.md is "19-training-optimization-algorithm-class".
    ("14-Computational Resource", "19-Training Optimization Algorithm"),
]

# 02-causal edges (source_node_type, target_node_type, edge_type) full set
CAUSAL_EDGE_FULL: list[tuple[str, str, str]] = [
    ("01-Object Domain", "02-Object Type", "contains"),
    ("02-Object Type", "04-Fault Location", "contains"),
    ("02-Object Type", "03-Operating Conditions", "contains"),
    ("05-Fault Mode", "07-Compound Fault", "contains"),
    ("11-Sensor Information", "04-Fault Location", "is collected on"),
    ("11-Sensor Information", "05-Fault Mode", "can obviously reflect"),
    ("10-Dataset", "08-PHM Task", "can be used for"),
    ("04-Fault Location", "05-Fault Mode", "has_fault_mode"),
    ("05-Fault Mode", "06-Fault Severity", "contains"),
    ("02-Object Type", "08-PHM Task", "contains_phm_task"),
    ("04-Fault Location", "08-PHM Task", "contains_phm_task"),
    ("05-Fault Mode", "08-PHM Task", "contains_phm_task"),
    ("06-Fault Severity", "08-PHM Task", "contains_phm_task"),
]

# 02-causal edges supplement (source_node_type, target_node_type, edge_type) full set
CAUSAL_EDGE_SUPPLEMENT: list[tuple[str, str, str]] = [
    ("02-Object Type", "09-Problem Scenario", "induces_problem"),
    ("03-Operating Conditions", "09-Problem Scenario", "induces_problem"),
    ("06-Fault Severity", "09-Problem Scenario", "induces_problem"),
    ("07-Compound Fault", "09-Problem Scenario", "induces_problem"),
    ("08-PHM Task", "09-Problem Scenario", "induces_problem"),
    ("12-Training Data Availability", "09-Problem Scenario", "induces_problem"),
    ("13-Noise Level", "09-Problem Scenario", "induces_problem"),
    ("14-Computational Resource", "09-Problem Scenario", "induces_problem"),
]

# 03-evidence edges (source_node_type, target_node_type) full set
# NOTE: the edge type for 03-evidence edges in edge_rules.md is "motivates".
EVIDENCE_EDGE_FULL: list[tuple[str, str]] = [
    ("09-Problem Scenario", "19-Training Optimization Algorithm"),
    ("12-Training Data Availability", "18-Data Generation Algorithm"),
    ("12-Training Data Availability", "19-Training Optimization Algorithm"),
    ("13-Noise Level", "15-Data Preprocessing Algorithm"),
    ("13-Noise Level", "16-Feature Extraction Algorithm"),
    ("09-Problem Scenario", "18-Data Generation Algorithm"),
    ("09-Problem Scenario", "15-Data Preprocessing Algorithm"),
    ("09-Problem Scenario", "16-Feature Extraction Algorithm"),
    ("09-Problem Scenario", "17-Core Classifier Algorithm"),
    ("07-Compound Fault", "16-Feature Extraction Algorithm"),
    ("07-Compound Fault", "17-Core Classifier Algorithm"),
    ("06-Fault Severity", "17-Core Classifier Algorithm"),
]

# Chinese-English mapping for edge_group
EDGE_GROUP_NAME: dict[str, str] = {
    "01-default edge": "01-default edge",
    "02-causal edge": "02-causal edge",
    "03-evidence edge": "03-evidence edge",
}


# ============================================================================
# LLM client
# ============================================================================

class LLMCallError(Exception):
    pass


def call_llm(messages: list[dict]) -> str:
    """Call the LLM and return the raw text content"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": LLM_MODEL,
        "messages": messages,
        "temperature": LLM_TEMPERATURE,
        "max_tokens": 256,
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
    """Strictly extract the N-of-1 option name from the LLM output (exact match)"""
    text = text.strip()
    # 1) 优先精确整段 Match
    for opt in options:
        if text == opt:
            return opt
    # 2) 在文本中find完整包含的选项
    for opt in options:
        if opt in text:
            return opt
    return None


# ============================================================================
# Utility functions
# ============================================================================

def load_json(path: str) -> list:
    """load最外层is list 的 JSON"""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError(f"输入 JSON 最外层不是 list，而是 {type(data).__name__}: {path}")
    return data


def save_json(path: str, data) -> None:
    """saveisformat化 JSON"""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def build_output_path(input_path: str, suffix: str = "_规范性审查") -> str:
    """根据input路径generateoutput路径(同Directory, File名加后缀)"""
    base_dir = os.path.dirname(input_path)
    basename = os.path.basename(input_path)
    name, ext = os.path.splitext(basename)
    return os.path.join(base_dir, f"{name}{suffix}{ext}")


def _build_case_line_map_from_text(json_text: str) -> dict[str, int]:
    """
    从格式化后的 JSON 文本中解析每个顶层 case_id 对象在文件中的起始行号（1-based）。

    实现思路：
      1) 遍历整个 json_text，构建 (字符偏移 -> 行号) 的查找表；
      2) 通过 json.JSONDecoder().raw_decode 顺序解析每个顶层对象，
         拿到其起始字符偏移，再用查找表换算为行号。
    """
    # 1) 字符偏移 -> 1-based 行号 find表
    # line_starts[i] 表示第 (i+1) 行的起始字符偏移
    line_starts: list[int] = [0]
    for i, ch in enumerate(json_text):
        if ch == '\n':
            line_starts.append(i + 1)

    def pos_to_line(p: int) -> int:
        # 二分find: 找最大的 line_starts[i] <= p
        lo, hi = 0, len(line_starts) - 1
        result = 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if line_starts[mid] <= p:
                result = mid + 1
                lo = mid + 1
            else:
                hi = mid - 1
        return result

    line_map: dict[str, int] = {}
    decoder = json.JSONDecoder()

    # skipon头的empty白
    idx = 0
    n = len(json_text)
    while idx < n and json_text[idx].isspace():
        idx += 1
    if idx >= n or json_text[idx] != '[':
        return line_map
    idx += 1  # skip '['

    # 2) 顺序parse顶层每个对象
    while idx < n:
        # skipempty白和逗号
        while idx < n and (json_text[idx].isspace() or json_text[idx] == ','):
            idx += 1
        if idx >= n:
            break
        if json_text[idx] == ']':
            break
        # parse一个对象
        try:
            obj, end_idx = decoder.raw_decode(json_text, idx)
        except json.JSONDecodeError:
            break
        if isinstance(obj, dict):
            start_line = pos_to_line(idx)
            case_id = str(obj.get("case_id", ""))
            line_map[case_id] = start_line
        idx = end_idx

    return line_map


# ============================================================================
# Step 1: node null-value audit
# ============================================================================

def audit_null_values(papers: list[dict]) -> tuple[list[dict], dict]:
    """
    遍历各 edge，分别针对 source_node_original_name/source_node_name、
    target_node_original_name/target_node_name，删除空值 edge。

    判定规则（按用户要求）：
      1) source: "Not Mentioned" + null
      2) source: "" + ""
      3) source: null + null
      4) source: "Not Mentioned" + null  （与 1) 完全重复，按用户原文保留）
      5) source: "" + ""         （与 2) 完全重复，按用户原文保留）
      6) source: null + null     （与 3) 完全重复，按用户原文保留）
      —— 以及同样的规则套用到 target。

    返回：
      (更新后的 papers, 统计字典)
      统计字典：{ edge_group: {"null_edges": N, "deleted_edges": N1, "status": str}, ... }
    """
    print("\n" + "=" * 70)
    print("[Step 1] Node null-value audit")
    print("=" * 70)

    # Aggregate N (number of edges with null values) and N1 (number of removed edges) by edge_group
    stats: dict[str, dict] = {}

    def _is_null_pair(orig, name) -> bool:
        """Determine whether (original_name, name) satisfies the null-value condition."""
        if orig == "Not Mentioned" and name is None:
            return True
        if orig == "" and name == "":
            return True
        if orig is None and name is None:
            return True
        return False

    def _is_null_edge(edge: dict) -> bool:
        """Check whether the edge's source or target has a null-value node."""
        for prefix in ("source", "target"):
            orig = edge.get(f"{prefix}_node_original_name")
            name = edge.get(f"{prefix}_node_name")
            if _is_null_pair(orig, name):
                return True
        return False

    for paper in papers:
        case_id = paper.get("case_id", "?")
        old_edges = paper.get("edges", []) or []
        new_edges = []
        for edge in old_edges:
            edge_group = edge.get("edge_group", "?")
            if edge_group not in stats:
                stats[edge_group] = {"null_edges": 0, "deleted_edges": 0, "status": "no deletion needed"}
            if _is_null_edge(edge):
                stats[edge_group]["null_edges"] += 1
                stats[edge_group]["deleted_edges"] += 1
                # remove the edge, do not add it to new_edges
                continue
            new_edges.append(edge)
        paper["edges"] = new_edges

    # Determine status
    for g, s in stats.items():
        n = s["null_edges"]
        n1 = s["deleted_edges"]
        if n1 == 0 and n == 0:
            s["status"] = "no deletion needed"
        elif n1 == n:
            s["status"] = "fully deleted"
        else:
            s["status"] = "partially deleted"

    # Console output
    for g in ("01-default edge", "02-causal edge", "03-evidence edge"):
        s = stats.get(g, {"null_edges": 0, "deleted_edges": 0, "status": "no deletion needed"})
        print(
            f"edge_group: {g}. Edges with null values detected: {s['null_edges']}, "
            f"deleted: {s['deleted_edges']}, status: {s['status']}."
        )
    # Other edge_group (if any) are also printed
    for g, s in stats.items():
        if g not in ("01-default edge", "02-causal edge", "03-evidence edge"):
            print(
                f"edge_group: {g}. Edges with null values detected: {s['null_edges']}, "
                f"deleted: {s['deleted_edges']}, status: {s['status']}."
            )

    return papers, stats


# ============================================================================
# Step 2: node node_name conformance audit (N-of-1)
# ============================================================================

def _build_llm_prompt_edge(
    side: str,            # "source" / "target"
    node_id: str,
    node_type: str,
    node_name: str,
    node_original_name: str,
    options: set[str],
) -> str:
    """Build the LLM N-of-1 prompt (for edge source/target node)."""
    options_str = " | ".join(options)
    return (
        f"【任务】你是一位PHM（故障预测与健康管理）领域的图谱节点分类助手。\n"
        f"现在给定一个节点的现有信息，请你综合 node_name、node_original_name、"
        f"node_description 三者的信息，"
        f"从给定的 N 个标准选项中**严格选择 1 个**作为该节点的最终 node_name 输出。\n\n"
        f"【节点位置】{side} 端节点\n"
        f"【node_id】{node_id}\n"
        f"【node_type】{node_type}\n"
        f"【当前 node_name】{node_name}\n"
        f"【node_original_name】{node_original_name}\n\n"
        f"【N 选 1 选项（必须且只能从以下选项中选 1 个，禁止自造）】\n"
        f"{options_str}\n\n"
        f"【强制输出要求】\n"
        f"1) **只输出 1 行**：你选中的选项名称（必须一字不差等于上述某个选项）。\n"
        f"2) 严禁输出：解释、思考过程、JSON、引号、标点、前后缀、换行、Markdown 等任何附加内容。\n"
        f"3) 不允许输出 \"Not Mentioned\"、\"N/A\"、\"不知道\" 等模糊回答。\n"
        f"4) 严禁输出多个选项或重复内容。\n\n"
        f"现在请直接输出 1 行最终答案："
    )


def _llm_correct_edge(
    side: str,
    node_id: str,
    node_type: str,
    node_name: str,
    node_original_name: str,
    options: set[str],
) -> Optional[str]:
    """Invoke LLM to perform N-of-1 secondary assignment for non-compliant node_name."""
    prompt = _build_llm_prompt_edge(
        side, node_id, node_type, node_name, node_original_name, options
    )
    messages = [
        {"role": "system", "content": "你是一个严格的知识图谱节点分类助手。"},
        {"role": "user", "content": prompt},
    ]
    try:
        response = call_llm(messages)
        fixed = extract_n_from_llm_response(response, options)
        if fixed and fixed in options:
            return fixed
        # Force re-validation: take the first matched item from the first line of response
        first_line = response.strip().splitlines()[0].strip() if response.strip() else ""
        if first_line in options:
            return first_line
        return None
    except LLMCallError:
        return None
    except Exception:
        return None


# Program fallback: N-of-1 based on keywords
KEYWORD_MAP_FOR_PROGRAM: list[tuple[tuple[str, ...], str]] = [
    # (keywords, option)
    (("Aerospace", "aero", "aircraft", "uav", "无人机", "飞行"), "Aerospace"),
    (("Space", "space", "satellite", "spacecraft"), "Space"),
    (("Marine", "ship", "vessel", "naval"), "Marine"),
    (("Industrial", "industrial", "manufacturing", "wind turbine"), "Industrial"),
    (("Nuclear", "nuclear", "reactor"), "Nuclear"),
    (("Electronics", "motor", "transformer", "electronics"), "Electronics"),
    (("Vehicle", "vehicle", "automotive", "railway", "car", "train"), "Vehicle"),
    (("Other",), "Other"),

    (("Single Condition",), "Single Condition"),
    (("Multiple Conditions",), "Multiple Conditions"),
    (("Variable Conditions", "time-varying", "non-stationary", "dynamic", "时变", "非稳态"), "Variable Conditions"),

    (("Single Severity",), "Single Severity"),
    (("Multiple Severities",), "Multiple Severities"),

    (("No Compound Fault",), "No Compound Fault"),
    (("Compound Fault Within Same Structure",), "Compound Fault Within Same Structure"),
    (("Compound Fault Across Structures",), "Compound Fault Across Structures"),

    (("检测", "detection", "detect", "monitor"), "Detection Task"),
    (("诊断", "diagnosis", "classif", "identif"), "Diagnosis Task"),
    (("预测", "prediction", "rul", "prognos", "remaining useful life"), "Prediction Task"),
    (("评估", "assessment", "evaluat"), "Assessment Task"),
    (("Other Task",), "Other Task"),

    (("Small Fault Samples", "few-shot", "few shot", "scarc", "小样本", "样本不足"), "Small Fault Samples"),
    (("Zero Fault Samples", "zero-shot", "zero shot", "未见故障", "Zero-Sample"), "Zero Fault Samples"),
    (("分布差异", "domain shift", "cross-domain", "transfer", "跨域", "分布偏移"), "Distribution Discrepancy"),
    (("不确定性", "uncertainty", "noise robust", "鲁棒"), "Uncertainty"),
    (("Compound Faults", "compound", "mixed fault"), "Compound Faults"),
    (("复杂系统", "system-level", "complicated", "复杂"), "Complex Systems"),
    (("早期退化", "incipient", "degradation", "退化", "弱故障"), "Early Degradation Prediction"),
    (("多源", "多模态", "multimodal", "heterogeneous", "sensor fusion", "异构"), "Multi-Source Heterogeneous / Multimodal Data"),
    (("可信", "可解释", "interpret", "physics-inform", "物理一致"), "Trustworthiness / Interpretability"),
    (("Other",), "Other"),

    (("Zero-Sample", "zero-shot"), "Zero-Sample"),
    (("Scarce", "insufficient", "scarce", "不足"), "Scarce"),
    (("Sufficient", "充足", "丰富"), "Sufficient"),

    (("High Noise", "noisy", "noise", "扰动"), "High Noise"),
    (("Normal",), "Normal"),

    (("Low Resource Consumption", "lightweight", "embedded", "flops", "轻量", "在线"), "Low Resource Consumption"),
    (("Not Mentioned",), "Not Mentioned"),
    (("High Resource Consumption", "computational", "复杂度", "消耗大"), "High Resource Consumption"),
]


def _program_correct_edge(node_name: str, node_original_name: str, options: set[str]) -> Optional[str]:
    """Program-level fallback N-of-1 based on keywords (edge-node version)."""
    text = (str(node_name or "") + " " + str(node_original_name or "")).lower()
    if not text.strip():
        return None
    best_match = None
    best_score = 0
    for keywords, option in KEYWORD_MAP_FOR_PROGRAM:
        if option not in options:
            continue
        score = sum(1 for kw in keywords if kw.lower() in text)
        if score > best_score:
            best_score = score
            best_match = option
    return best_match


def audit_node_name_for_edges(papers: list[dict]) -> tuple[list[dict], dict]:
    """
    Perform node_name conformance audit (N-of-1) on the source/target nodes of each edge in the edge graph.

    Note: edge nodes are prefixed with "source_node_type"/"source_node_name"/
    "source_node_original_name" and "target_*".

    Returns:
      (updated papers, statistics dict)
      statistics dict: { node_type: {"total": N2, "non_compliant": N3, "compliant": N4,
                                     "llm_fixed": N5, "program_fixed": N6}, ... }
    """
    print("\n" + "=" * 70)
    print("[Step 2] Node node_name conformance audit (N-of-1)")
    print("=" * 70)

    # Aggregate: by node_type
    stats: dict[str, dict] = {
        nt: {"total": 0, "non_compliant": 0, "compliant": 0,
             "llm_fixed": 0, "program_fixed": 0}
        for nt in AUDIT_NODE_TYPES
    }

    for paper in papers:
        case_id = paper.get("case_id", "?")
        for edge in paper.get("edges", []):
            edge_id = edge.get("edge_id", "?")
            for side in ("source", "target"):
                node_type = edge.get(f"{side}_node_type", "")
                if node_type not in AUDIT_NODE_TYPES:
                    continue
                options = NODE_NAME_RULES[node_type]
                node_name = edge.get(f"{side}_node_name", "")
                node_original_name = edge.get(f"{side}_node_original_name", "")
                node_id = edge.get(f"{side}_node_id", "?")

                stats[node_type]["total"] += 1

                # compliance check
                if node_name in options:
                    stats[node_type]["compliant"] += 1
                    continue

                # non-compliant
                stats[node_type]["non_compliant"] += 1

                # LLM secondary assignment
                llm_fixed = _llm_correct_edge(
                    side, node_id, node_type, node_name, node_original_name, options
                )
                if llm_fixed is not None:
                    edge[f"{side}_node_name"] = llm_fixed
                    stats[node_type]["llm_fixed"] += 1
                    print(
                        f"    [LLM correction] case={case_id} edge={edge_id} "
                        f"{side} {node_type} ({node_id}): '{node_name}' → '{llm_fixed}'"
                    )
                else:
                    # Program fallback N-of-1
                    prog_fixed = _program_correct_edge(node_name, node_original_name, options)
                    if prog_fixed is None:
                        # Final fallback: take the first element of options
                        prog_fixed = next(iter(options))
                    edge[f"{side}_node_name"] = prog_fixed
                    stats[node_type]["program_fixed"] += 1
                    print(
                        f"    [Program correction] case={case_id} edge={edge_id} "
                        f"{side} {node_type} ({node_id}): '{node_name}' → '{prog_fixed}' (LLM invalid)"
                    )

    # Console output (by node_type, only aggregate node_types with N-of-1 requirements)
    for nt in sorted(stats.keys()):
        s = stats[nt]
        if s["total"] == 0:
            continue
        print(
            f"node_type: {nt}. Total node_name: {s['total']}, "
            f"non-compliant node_name: {s['non_compliant']}, "
            f"compliant node_name: {s['compliant']}, "
            f"node_name made compliant after LLM correction: {s['llm_fixed']}, "
            f"node_name made compliant via program forcing (LLM failed): {s['program_fixed']}."
        )

    return papers, stats


# ============================================================================
# Step 3: edge completeness audit
# ============================================================================

def _get_node_type_group(paper: dict) -> set[str]:
    """Collect deduplicated union of source/target node_types from all edges of the paper."""
    node_type_group: set[str] = set()
    for edge in paper.get("edges", []):
        s_t = edge.get("source_node_type")
        t_t = edge.get("target_node_type")
        if isinstance(s_t, str) and s_t:
            node_type_group.add(s_t)
        if isinstance(t_t, str) and t_t:
            node_type_group.add(t_t)
    # Also check the nodes[] field (although edge graph nodes are mostly [], keep as fallback)
    for node in paper.get("nodes", []) or []:
        nt = node.get("node_type")
        if isinstance(nt, str) and nt:
            node_type_group.add(nt)
    return node_type_group


def _filter_full_by_node_type_group(
    full_list: list[tuple],
    node_type_group: set[str],
) -> list[tuple]:
    """For the preset rules in (source, target) or (source, target, edge_type) form,
    filter by node_type_group: only candidates whose strings all appear in node_type_group
    are considered valid; otherwise they are dropped (meaning the case lacks that node_type,
    so this candidate edge does not apply).

    Note: edge_type is English (e.g., 'contains') and is usually not in node_type_group,
    so such non-node_type string fields are automatically skipped.
    """
    # Known edge_type set (appearing in preset rules), which should not participate in node_type_group filtering
    EDGE_TYPES: set[str] = {
        "contains", "is collected on", "can obviously reflect", "can be used for",
        "has_fault_mode", "contains_phm_task", "induces_problem", "motivates",
        "connects",
    }
    valid: list[tuple] = []
    for tup in full_list:
        # Extract node_type fields (not edge_type)
        nt_parts = [p for p in tup if isinstance(p, str) and p not in EDGE_TYPES]
        # all nt_parts must be in node_type_group
        if all(part in node_type_group for part in nt_parts):
            valid.append(tup)
    return valid


def audit_edge_completeness(papers: list[dict]) -> tuple[list[dict], dict]:
    """
    Edge completeness audit:
      - 01-default edges: each case's 01-default edge set must equal the "01-full-set" filtered by node_type_group
      - 02-causal edges: each case's 02-causal edge set must be a superset of the "02-full-set" filtered by node_type_group
      - 02-causal edges supplement: each case's 02-causal-edge supplement set must be a superset of at least 1 of the "02-full-supplement"
      - 03-evidence edges: each case's 03-evidence edge set must be a superset of at least 1 of the "03-full-set"
    """
    print("\n" + "=" * 70)
    print("[Step 3] Edge completeness audit")
    print("=" * 70)

    total_cases = len(papers)

    # --- 01-default edges ---
    n_01_case_ok = 0
    n_01_case_fail = 0
    invalid_01_cases: list[dict] = []

    # --- 02-causal edges ---
    n_02_case_ok = 0
    n_02_case_fail = 0
    invalid_02_cases: list[dict] = []

    # --- 02-causal edges supplement ---
    n_02_case_ok_add = 0
    n_02_case_fail_add = 0
    invalid_02_cases_add: list[dict] = []

    # --- 03-evidence edges ---
    n_03_case_ok = 0
    n_03_case_fail = 0
    invalid_03_cases: list[dict] = []

    for paper in papers:
        case_id = paper.get("case_id", "?")
        node_type_group = _get_node_type_group(paper)
        edges = paper.get("edges", []) or []

        # === 01-default edges ===
        # Judgment method:
        #   1) Copy "01-full-set" into "01-full-temp-copy", filter by node_type_group:
        #      if any string in candidate (s, t) is not in node_type_group, the candidate
        #      is considered invalid. After filtering, the "01-full-temp-copy-valid" count is N7.
        #   2) In the current case's edges, aggregate distinct (source_node_type, target_node_type)
        #      pairs with edge_group == "01-default edge" and count them as N7_real.
        #   3) N7 == N7_real => valid; otherwise => invalid.
        # When invalid, record: missing (s, t) (in N7 but not in N7_real),
        #                      extra (s, t) (in N7_real but not in N7).
        full_01_valid = _filter_full_by_node_type_group(DEFAULT_EDGE_FULL, node_type_group)
        n7 = len(full_01_valid)
        full_01_valid_set = set(full_01_valid)
        # Real distinct (s, t) pairs that exist and whose (s, t) falls in the full set
        real_pairs_01: set[tuple] = {
            (e.get("source_node_type"), e.get("target_node_type"))
            for e in edges
            if e.get("edge_group") == "01-default edge"
            and (e.get("source_node_type"), e.get("target_node_type")) in full_01_valid_set
        }
        n7_real = len(real_pairs_01)
        if n7 == n7_real:
            n_01_case_ok += 1
        else:
            n_01_case_fail += 1
            missing_pairs = sorted(full_01_valid_set - real_pairs_01)
            extra_pairs = sorted(real_pairs_01 - full_01_valid_set)
            invalid_01_cases.append({
                "case_id": case_id,
                "expected_N7": n7,
                "actual_N7_real": n7_real,
                "missing": [f"{s}→{t}" for (s, t) in missing_pairs],
                "extra": [f"{s}→{t}" for (s, t) in extra_pairs],
            })

        # === 02-causal edges ===
        full_02_valid = _filter_full_by_node_type_group(CAUSAL_EDGE_FULL, node_type_group)
        n8 = len(full_02_valid)
        # 02-causal edges actually existing: edge_group=02-causal edge and (s,t,et) in full_02_valid
        causal_edges = [e for e in edges if e.get("edge_group") == "02-causal edge"]
        causal_real_keys = {
            (e.get("source_node_type"), e.get("target_node_type"), e.get("edge_type"))
            for e in causal_edges
        }
        n8_real = sum(1 for k in full_02_valid if k in causal_real_keys)
        if n8_real >= n8:
            n_02_case_ok += 1
        else:
            n_02_case_fail += 1
            missing = [f"{s}|{t}|{et}" for (s, t, et) in full_02_valid if (s, t, et) not in causal_real_keys]
            invalid_02_cases.append({
                "case_id": case_id,
                "expected_N8": n8,
                "actual_N8_real": n8_real,
                "missing": missing,
            })

        # === 02-causal edges supplement ===
        full_02_sup_valid = _filter_full_by_node_type_group(CAUSAL_EDGE_SUPPLEMENT, node_type_group)
        n9 = len(full_02_sup_valid)
        n9_real = sum(1 for k in full_02_sup_valid if k in causal_real_keys)
        if n9_real >= 1:
            n_02_case_ok_add += 1
        else:
            n_02_case_fail_add += 1
            invalid_02_cases_add.append({
                "case_id": case_id,
                "expected_N9": n9,
                "actual_N9_real": n9_real,
                "note": "Current case_id has no valid edge in the 02-causal edge supplement set",
            })

        # === 03-evidence edges ===
        full_03_valid = _filter_full_by_node_type_group(EVIDENCE_EDGE_FULL, node_type_group)
        n10 = len(full_03_valid)
        evidence_edges = [e for e in edges if e.get("edge_group") == "03-evidence edge"]
        evidence_real_keys = {
            (e.get("source_node_type"), e.get("target_node_type"))
            for e in evidence_edges
        }
        n10_real = sum(1 for k in full_03_valid if k in evidence_real_keys)
        if n10_real >= 1:
            n_03_case_ok += 1
        else:
            n_03_case_fail += 1
            invalid_03_cases.append({
                "case_id": case_id,
                "expected_N10": n10,
                "actual_N10_real": n10_real,
                "note": "Current case_id has no valid edge in the 03-evidence edge set",
            })

    # Console output
    print()
    print("Edge completeness audit")
    print(
        f"1. edge_group = 01-default edge, after audit, traversed case_id total {total_cases}, "
        f"valid case_id total {n_01_case_ok}, invalid case_id total {n_01_case_fail}, "
        f"invalid case_id specifically: {[c['case_id'] for c in invalid_01_cases]}; "
        f"details in the audit log md file under section \"edge completeness audit - 01 default edge audit\"."
    )
    print(
        f"\n2. edge_group = 02-causal edge, after audit, traversed case_id total {total_cases}, "
        f"valid case_id total {n_02_case_ok}, invalid case_id total {n_02_case_fail}, "
        f"invalid case_id specifically: {[c['case_id'] for c in invalid_02_cases]}; "
        f"details in the audit log md file under section \"edge completeness audit - 02 causal edge audit\"."
    )
    print(
        f"\n3. edge_group = 02-causal edge (supplement), after supplement audit, traversed case_id total {total_cases}, "
        f"valid case_id total {n_02_case_ok_add}, invalid case_id total {n_02_case_fail_add}, "
        f"invalid case_id specifically: {[c['case_id'] for c in invalid_02_cases_add]}; "
        f"details in the audit log md file under section \"edge completeness audit - 02 causal edge supplement audit\"."
    )
    print(
        f"\n4. edge_group = 03-evidence edge, after audit, traversed case_id total {total_cases}, "
        f"valid case_id total {n_03_case_ok}, invalid case_id total {n_03_case_fail}, "
        f"invalid case_id specifically: {[c['case_id'] for c in invalid_03_cases]}; "
        f"details in the audit log md file under section \"edge completeness audit - 03 evidence edge audit\"."
    )

    completeness_stats = {
        "01-default edge": {
            "total_cases": total_cases,
            "ok": n_01_case_ok,
            "fail": n_01_case_fail,
            "invalid_cases": invalid_01_cases,
        },
        "02-causal edge": {
            "total_cases": total_cases,
            "ok": n_02_case_ok,
            "fail": n_02_case_fail,
            "invalid_cases": invalid_02_cases,
        },
        "02-causal edge supplement": {
            "total_cases": total_cases,
            "ok": n_02_case_ok_add,
            "fail": n_02_case_fail_add,
            "invalid_cases": invalid_02_cases_add,
        },
        "03-evidence edge": {
            "total_cases": total_cases,
            "ok": n_03_case_ok,
            "fail": n_03_case_fail,
            "invalid_cases": invalid_03_cases,
        },
    }

    return papers, completeness_stats


# ============================================================================
# Step 4: graph-structure conformance audit
# ============================================================================

def audit_graph_structure(
    papers: list[dict],
    case_line_map: dict[str, int] | None = None,
) -> tuple[list[dict], dict]:
    """
    Audit whether the nested structure and property names of the graph JSON are compliant.
    Returns (updated papers, statistics)

    Statistics new fields:
      - case_line_map: dict[case_id, start_line] the start line number (1-based)
        of the corresponding case_id in the graph JSON, used to trace structure
        non-compliance back to the specific line in the JSON file.
    """
    print("\n" + "=" * 70)
    print("[Step 4] Graph-structure conformance audit")
    print("=" * 70)

    PAPER_REQUIRED_FIELDS = {
        "case_id", "paper_title", "publish_year", "publish_source",
        "cite_count", "algorithm_hyperparameters", "training_config",
        "performance_metrics", "nodes", "edges",
    }
    EDGE_REQUIRED_FIELDS = {
        "edge_id", "source_node_id", "source_node_type", "source_node_name",
        "source_node_original_name", "target_node_id", "target_node_type",
        "target_node_name", "target_node_original_name", "edge_type",
        "edge_group", "evidence_level", "edge_description", "edge_weight",
        "edge_nums",
    }

    total_papers = len(papers)
    compliant_papers: list[str] = []
    non_compliant_papers: list[dict] = []
    if case_line_map is None:
        case_line_map = {}

    for paper in papers:
        case_id = str(paper.get("case_id", ""))
        issues: list[str] = []
        start_line = case_line_map.get(case_id)

        if not isinstance(paper, dict):
            issues.append("Top-level element is not a dict object")
            non_compliant_papers.append({
                "case_id": case_id,
                "start_line": start_line,
                "issues": issues,
            })
            continue

        # nodes / edges type
        nodes = paper.get("nodes")
        edges = paper.get("edges")
        if not isinstance(nodes, list):
            issues.append(f"nodes property type error, expected list, actual {type(nodes).__name__}")
        if not isinstance(edges, list):
            issues.append(f"edges property type error, expected list, actual {type(edges).__name__}")

        # edge property completeness
        if isinstance(edges, list):
            for i, edge in enumerate(edges):
                if not isinstance(edge, dict):
                    issues.append(f"edges[{i}] is not a dict object")
                    continue
                missing = EDGE_REQUIRED_FIELDS - set(edge.keys())
                if missing:
                    issues.append(f"edges[{i}] missing properties: {sorted(missing)}")

        # Top-level properties missing (excluding nodes/edges)
        required_no_lists = PAPER_REQUIRED_FIELDS - {"nodes", "edges"}
        missing_top = required_no_lists - set(paper.keys())
        if missing_top:
            issues.append(f"Top-level missing properties: {sorted(missing_top)}")

        if issues:
            non_compliant_papers.append({
                "case_id": case_id,
                "start_line": start_line,
                "issues": issues,
            })
        else:
            compliant_papers.append(case_id)

    print()
    print("Graph-structure conformance audit")
    print(f"1. Total graph case_id: {total_papers}")
    print(f"2. Checked graph case_id total: {total_papers}")
    print(
        f"3. Structurally compliant graph case_id total: {len(compliant_papers)}, "
        f"structurally non-compliant graph case_id total: {len(non_compliant_papers)}, "
        f"and the non-compliant case_ids: {[it['case_id'] for it in non_compliant_papers]}."
    )
    # 4. Print each non-compliant case_id's reason and corresponding line number
    if non_compliant_papers:
        print("4. Non-compliant case_ids, their non-compliance reasons and corresponding graph JSON line numbers:")
        for it in non_compliant_papers:
            line_info = (
                f"starting from line {it['start_line']}"
                if it.get("start_line") is not None
                else "line number unknown"
            )
        print(
            f"   - case_id: `{it['case_id']}`, located at line: {line_info}, "
            f"non-compliance reasons: {'; '.join(it['issues'])}"
        )
    else:
        print("4. Non-compliant case_id: (none)")

    return papers, {
        "total_papers": total_papers,
        "checked_papers": total_papers,
        "compliant_papers": compliant_papers,
        "non_compliant_papers": non_compliant_papers,
        "case_line_map": case_line_map,
    }


# ============================================================================
# auditlog md generate
# ============================================================================

def build_audit_log_md(
    null_stats: dict,
    name_stats: dict,
    completeness_stats: dict,
    structure_stats: dict,
    input_path: str,
) -> str:
    """Generate the complete audit log md content."""
    lines: list[str] = []
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    lines.append(f"# Edge merge graph conformance audit log")
    lines.append("")
    lines.append(f"**Audit target**: `{os.path.basename(input_path)}`")
    lines.append(f"**Generation time**: {ts}")
    lines.append(f"**Generation script**: `zotero_knowledge_graph_edge_extractor_merge_conformance_audit_v8.py`")
    lines.append("")
    lines.append("---")
    lines.append("")

    # 1. node null-value audit
    lines.append("## 1. Node null-value audit")
    lines.append("")
    lines.append(
        "**Audit logic**: iterate each edge{} in the edge graph JSON, for source/target "
        "node_original_name and node_name; delete the edge if any of the 6 null-value "
        "rules is satisfied, and aggregate by edge_group."
    )
    lines.append("")
    for g in ("01-default edge", "02-causal edge", "03-evidence edge"):
        s = null_stats.get(g, {"null_edges": 0, "deleted_edges": 0, "status": "no deletion needed"})
        lines.append(
            f"- edge_group: `{g}`. Edges with null values detected: "
            f"`{s['null_edges']}`, deleted: `{s['deleted_edges']}`, "
            f"status: `{s['status']}`."
        )
    for g, s in null_stats.items():
        if g not in ("01-default edge", "02-causal edge", "03-evidence edge"):
            lines.append(
                f"- edge_group: `{g}`. Edges with null values detected: "
                f"`{s['null_edges']}`, deleted: `{s['deleted_edges']}`, "
                f"status: `{s['status']}`."
            )
    lines.append("")
    lines.append("---")
    lines.append("")

    # 2. node node_name conformance audit
    lines.append("## 2. Node node_name conformance audit (N-of-1)")
    lines.append("")
    lines.append(
        "**Audit logic**: for source/target nodes of each edge{} in the edge graph JSON, "
        "for node_types with N-of-1 requirements, "
        "strictly match source_node_name/target_node_name; "
        "non-compliant ones call LLM for N-of-1 secondary assignment, "
        "still non-compliant after LLM are forced to N-of-1 by program via keywords."
    )
    lines.append("")
    for nt in sorted(name_stats.keys()):
        s = name_stats[nt]
        if s["total"] == 0:
            continue
        lines.append(
            f"- node_type: `{nt}`. Total node_name: `{s['total']}`, "
            f"non-compliant node_name count: `{s['non_compliant']}`, "
            f"compliant node_name count: `{s['compliant']}`, "
            f"node_name made compliant after LLM correction: `{s['llm_fixed']}`, "
            f"node_name made compliant via program forcing (LLM failed): `{s['program_fixed']}`."
        )
    lines.append("")
    lines.append("---")
    lines.append("")

    # 3. edge completeness audit
    lines.append("## 3. Edge completeness audit")
    lines.append("")

    # 3-1 01-default edge
    lines.append("### 3-1. Edge completeness audit - 01 default edge audit")
    lines.append("")
    lines.append(
        "**Judgment method**:\n"
        "1) Copy `01-full-set` as `01-full-temp-copy`, and for each candidate "
        "(source_node_type, target_node_type) filter by node_type_group: if any "
        "string in the candidate tuple does not fully exist in node_type_group, "
        "remove that candidate from `01-full-temp-copy`. After filtering, the "
        "`01-full-temp-copy-valid` tuple count is N7.\n"
        "2) When counting the edges with edge_group = `01-default edge` in the "
        "current case{}, the **same (source_node_type, target_node_type) "
        "category is counted only once**, i.e., the cumulative distinct edge{} "
        "total is N7_real.\n"
        "3) If N7 == N7_real, the case_id's 01-default edge audit is **valid** "
        "(N_01_case_ok_num+1); if N7 != N7_real, it is **invalid** "
        "(N_01_case_fail_num+1)."
    )
    lines.append("")
    s01 = completeness_stats["01-default edge"]
    lines.append(
        f"- Traversed case_id total: `{s01['total_cases']}`, "
        f"valid case_id total (`N_01_case_ok_num`): `{s01['ok']}`, "
        f"invalid case_id total (`N_01_case_fail_num`): `{s01['fail']}`."
    )
    lines.append("")
    if s01["invalid_cases"]:
        lines.append("**Invalid case_id details (continued)**:")
        lines.append("")
        for it in s01["invalid_cases"]:
            missing_str = ", ".join(it["missing"]) if it.get("missing") else "(none)"
            extra_str = ", ".join(it.get("extra", [])) if it.get("extra") else "(none)"
            lines.append(
                f"- case_id: `{it['case_id']}`, expected edge count N7=`{it['expected_N7']}`, "
                f"actual distinct edge count N7_real=`{it['actual_N7_real']}`."
            )
            lines.append(
                f"  - Missing (source_node_type, target_node_type) combinations: {missing_str}"
            )
            lines.append(
                f"  - Extra (source_node_type, target_node_type) combinations: {extra_str}"
            )
    else:
        lines.append("No invalid case_id.")
    lines.append("")

    # 3-2 02-causal edges
    lines.append("### 3-2. Edge completeness audit - 02 causal edge audit")
    lines.append("")
    s02 = completeness_stats["02-causal edge"]
    lines.append(
        f"- Traversed case_id total: `{s02['total_cases']}`, "
        f"valid case_id total: `{s02['ok']}`, "
        f"invalid case_id total: `{s02['fail']}`."
    )
    lines.append("")
    if s02["invalid_cases"]:
        lines.append("**Invalid case_id details**:")
        lines.append("")
        for it in s02["invalid_cases"]:
            missing_str = ", ".join(it["missing"]) if it["missing"] else "(none)"
            lines.append(
                f"- case_id: `{it['case_id']}`, expected edge count `{it['expected_N8']}`, "
                f"actual edge count `{it['actual_N8_real']}`, missing (source, target, edge_type): {missing_str}"
            )
    else:
        lines.append("No invalid case_id.")
    lines.append("")

    # 3-3 02-causal edges supplement
    lines.append("### 3-3. Edge completeness audit - 02 causal edge supplement audit")
    lines.append("")
    s02a = completeness_stats["02-causal edge supplement"]
    lines.append(
        f"- Traversed case_id total: `{s02a['total_cases']}`, "
        f"valid case_id total: `{s02a['ok']}`, "
        f"invalid case_id total: `{s02a['fail']}`."
    )
    lines.append("")
    if s02a["invalid_cases"]:
        lines.append("**Invalid case_id details**:")
        lines.append("")
        for it in s02a["invalid_cases"]:
            lines.append(
                f"- case_id: `{it['case_id']}`, expected supplement edge count `{it['expected_N9']}`, "
                f"actual supplement edge count `{it['actual_N9_real']}`, "
                f"note: {it.get('note', '')}"
            )
    else:
        lines.append("No invalid case_id.")
    lines.append("")

    # 3-4 03-evidence edges
    lines.append("### 3-4. Edge completeness audit - 03 evidence edge audit")
    lines.append("")
    s03 = completeness_stats["03-evidence edge"]
    lines.append(
        f"- Traversed case_id total: `{s03['total_cases']}`, "
        f"valid case_id total: `{s03['ok']}`, "
        f"invalid case_id total: `{s03['fail']}`."
    )
    lines.append("")
    if s03["invalid_cases"]:
        lines.append("**Invalid case_id details**:")
        lines.append("")
        for it in s03["invalid_cases"]:
            lines.append(
                f"- case_id: `{it['case_id']}`, expected edge count `{it['expected_N10']}`, "
                f"actual edge count `{it['actual_N10_real']}`, "
                f"note: {it.get('note', '')}"
            )
    else:
        lines.append("No invalid case_id.")
    lines.append("")

    lines.append("---")
    lines.append("")

    # 4. graph-structure conformance audit
    lines.append("## 4. Graph-structure conformance audit")
    lines.append("")
    lines.append(
        "**Audit logic**: take \"edge graph JSON-v2\" (i.e., the audited graph JSON) as input, "
        "the program iterates each part of the array, checks structural conformance requirements "
        "and counts.\n"
        "Structural conformance mainly audits:\n"
        "1) Whether the edge graph JSON-v2 follows the nested structure — whether the nested "
        "structure of each loop's array is closed and canonical;\n"
        "2) Whether the property names in the corresponding arrays of the edge graph JSON-v2 are "
        "accurate and complete;\n"
        "3) For non-compliant case_ids, give the non-compliance reason and its start line number "
        "in the \"edge graph JSON-v2\"."
    )
    lines.append("")
    lines.append(f"- Graph case_id total: `{structure_stats['total_papers']}`")
    lines.append(f"- Checked graph case_id total: `{structure_stats['checked_papers']}`")
    lines.append(
        f"- Structurally compliant graph case_id total: `{len(structure_stats['compliant_papers'])}`"
    )
    lines.append(
        f"- Structurally non-compliant graph case_id total: `{len(structure_stats['non_compliant_papers'])}`"
    )
    if structure_stats["non_compliant_papers"]:
        lines.append("- Non-compliant case_id details (including line number and reason):")
        lines.append("")
        for it in structure_stats["non_compliant_papers"]:
            line_info = (
                f"starting from line {it['start_line']}"
                if it.get("start_line") is not None
                else "line number unknown"
            )
            lines.append(
                f"  - case_id: `{it['case_id']}`, located at line: {line_info}"
            )
            for iss in it["issues"]:
                lines.append(f"    - {iss}")
    else:
        lines.append("- Non-compliant case_id details: (none)")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"*This report is auto-generated by `zotero_knowledge_graph_edge_extractor_merge_conformance_audit_v8.py`*")

    return "\n".join(lines)


# ============================================================================
# Main flow
# ============================================================================

def run():
    print("=" * 70)
    print("Edge merge graph conformance audit script")
    print("=" * 70)
    print(f"Input file: {INPUT_GRAPH_PATH}")
    print("=" * 70)

    # --- Step 0: load input ---
    print("\n[Step 0] Loading edge graph JSON ...")
    papers = load_json(INPUT_GRAPH_PATH)
    total_edges_before = sum(len(p.get("edges", []) or []) for p in papers)
    print(f"  Total {len(papers)} papers, total edge count: {total_edges_before}")

    # --- Step 1: node null-value audit ---
    papers, null_stats = audit_null_values(papers)
    total_edges_after_null = sum(len(p.get("edges", []) or []) for p in papers)
    print(f"  Total edge count after null audit: {total_edges_after_null} (deleted {total_edges_before - total_edges_after_null})")

    # --- Step 2: node node_name conformance audit ---
    papers, name_stats = audit_node_name_for_edges(papers)

    # --- Step 3: edge completeness audit (does not modify papers) ---
    papers, completeness_stats = audit_edge_completeness(papers)

    # --- Step 4: graph-structure conformance audit ---
    # Since the structure audit needs case_id line-number info from the original
    # graph JSON file, here we first save the audited graph JSON, then use the
    # "edge graph JSON-v2" as input (i.e., the audited JSON) for line-number
    # parsing and structure audit.
    output_json_path = build_output_path(INPUT_GRAPH_PATH, "_conformance_audit")
    save_json(output_json_path, papers)
    print(f"  Audited graph JSON: {output_json_path}")
    print(f"  Final: {len(papers)} papers, "
          f"{sum(len(p.get('edges', []) or []) for p in papers)} edges")

    # --- Step 4 continued: graph-structure conformance audit (targeting the "edge graph JSON-v2" = audited graph) ---
    with open(output_json_path, "r", encoding="utf-8") as f:
        json_text_v2 = f.read()
    case_line_map_v2 = _build_case_line_map_from_text(json_text_v2)
    print(f"  Parsed start line numbers for {len(case_line_map_v2)} case_ids from \"{os.path.basename(output_json_path)}\".")
    papers, structure_stats = audit_graph_structure(papers, case_line_map_v2)

    # --- Step 5: output audit log md ---
    print("\n[Step 5] Saving audit log MD ...")

    # audit log md: same directory as input, file name with suffix "_conformance_audit"
    log_md_path = build_output_path(INPUT_GRAPH_PATH, "_conformance_audit").replace(".json", ".md")
    log_content = build_audit_log_md(
        null_stats, name_stats, completeness_stats, structure_stats, INPUT_GRAPH_PATH
    )
    os.makedirs(os.path.dirname(log_md_path), exist_ok=True)
    with open(log_md_path, "w", encoding="utf-8") as f:
        f.write(log_content)
    print(f"  Audit log MD: {log_md_path}")

    print("\n" + "=" * 70)
    print("Audit complete")
    print("=" * 70)


if __name__ == "__main__":
    run()
