# -*- coding: utf-8 -*-
r"""
Edge merge -> disambiguation -> induction -> conformance audit script v8
================================================================================
Functions:
  Perform 5 kinds of conformance audits on the JSON (in the B2-边合并_消歧_归纳 directory)
  produced by "edge merge -> disambiguation -> induction":
    1. Node null-value audit: delete edges whose source/target nodes are null
       ("Not Mentioned" / "" / null).
    2. Node node_name conformance audit (N-of-1 rules): strictly match node_name
       of source/target nodes against an N-of-1 set; non-compliant names are
       re-assigned by an LLM; if the LLM still fails, the program forcibly
       picks an N-of-1.
    3. Edge completeness audit: completeness checks for 01-default edge,
       02-causal edge, 02-causal edge supplement, 03-evidence edge; write
       invalid case_id to the audit log md file.
    4. Graph-structure conformance audit: check whether the nested structure and
       property names are compliant.
    5. Output the audited graph JSON to the same directory as the input,
       with the suffix "_audit" appended to the filename.

Inputs:
  1. Edge graph JSON:
     ./data/B2-边合并_消歧_归纳/edge_consensus_disambiguation_induction.json
2. Four node-prompt md files (for extracting N-of-1 rules), exactly matching the
   MD file names in the schema directory:
   - 01-03,08-09 nodes.md
   - 04-07 nodes.md
   - 10-14 nodes.md
   - 15-20 nodes.md

Outputs:
  - Audited graph JSON: <input_file_name>_audit.json (in the same directory as input)
  - Audit log MD: <input_file_name>_audit_log.md (in the same directory as input),
    recording:
      · Node null-value audit
      · Node node_name conformance audit
      · Edge completeness audit (01-default/02-causal/02-causal supplement/03-evidence)
      · Graph-structure conformance audit

LLM configuration:
  When calling the LLM, use the viviai relay (consistent with the
  zotero_knowledge_graph_extractor_v7_merge_compliance_audit.py script).
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

# --- input1: edge graph JSON ---
# NOTE: relative-path placeholder. Replace with your own absolute path before running.
INPUT_GRAPH_PATH = r"./data/B2-边合并_消歧_归纳/edge_consensus_disambiguation_induction.json"

# --- input2: 4 node-prompt md files (for extracting N-of-1 rules) ---
# File names exactly match the actual MD file names in the schema directory.
PROMPT_FILES = [
    r"./prompts/04-07 nodes.md",
    r"./prompts/10-14 nodes.md",
    r"./prompts/15-20 nodes.md",
    r"./prompts/01-03,08-09 nodes.md",
]

# Output directory (same as input directory)
OUTPUT_DIR = os.path.dirname(INPUT_GRAPH_PATH)

# --- LLM configuration (consistent with v7_merge_compliance_audit.py) ---
API_KEY = ""  # NOTE: provide your own API key here
API_URL = os.environ.get("BFGA_LLM_API_URL", "https://YOUR.LLM.ENDPOINT/v1/chat/completions")
LLM_MODEL = "gemini-3.5-flash"
LLM_TIMEOUT = 300
LLM_TEMPERATURE = 0.0


# ============================================================================
# N-of-1 rules (extracted from prompt md and written into the program)
# ============================================================================
# Strictly following the N-of-1 descriptions in the prompts:
#   01-object domain class: 8-of-1
#   03-operating condition class: 3-of-1
#   06-fault severity class: 2-of-1
#   07-composite fault included: 3-of-1
#   08-PHM task class: 5-of-1
#   09-problem scenario class: 10-of-1 (multi-select up to 3, single node picks one)
#   12-available training data: 3-of-1
#   13-noise level class: 2-of-1
#   14-compute resource class: 3-of-1
# The rest (02/04/05/10/11/15-19/20) follow the prompts rule node_name = null,
# and are NOT included in the N-of-1 audit.

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

# node types that need to be included in the node_name conformance audit and aggregation (have N-of-1 requirements)
AUDIT_NODE_TYPES: set[str] = set(NODE_NAME_RULES.keys())


# ============================================================================
# Edge completeness preset rules (from v5 version edge prompts / edge_rules.md + user requirements)
# ============================================================================

# Full set of (source_node_type, target_node_type) for 01-default edges
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
    # note: 原任务稿写is "14-compute资sourceclass | 19-training optimization algorithmclassclass", 其medium末尾多了一个"class"字；
    # 按prompt edge_rules.md medium的正确命名is "19-training optimization algorithmclass".
    ("14-Computational Resource", "19-Training Optimization Algorithm"),
    ("15-Data Preprocessing Algorithm-Induction", "15-Data Preprocessing Algorithm"),
    ("16-Feature Extraction Algorithm-Induction", "16-Feature Extraction Algorithm"),
    ("17-Core Classifier Algorithm-Induction", "17-Core Classifier Algorithm"),
    ("18-Data Generation Algorithm-Induction", "18-Data Generation Algorithm"),
    ("19-Training Optimization Algorithm-Induction", "19-Training Optimization Algorithm"),
]

# 02-causal edges (source_node_type, target_node_type, edge_type) 全集
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

# 02-causal edges补充 (source_node_type, target_node_type, edge_type) 全集
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
# note: according to edge_rules.md, the edge_type of 03-evidence edges is "motivates".
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
    ("09-Problem Scenario", "19-Training Optimization Algorithm-Induction"),
    ("12-Training Data Availability", "18-Data Generation Algorithm-Induction"),
    ("12-Training Data Availability", "19-Training Optimization Algorithm-Induction"),
    ("13-Noise Level", "15-Data Preprocessing Algorithm-Induction"),
    ("13-Noise Level", "16-Feature Extraction Algorithm-Induction"),
    ("09-Problem Scenario", "18-Data Generation Algorithm-Induction"),
    ("09-Problem Scenario", "15-Data Preprocessing Algorithm-Induction"),
    ("09-Problem Scenario", "16-Feature Extraction Algorithm-Induction"),
    ("09-Problem Scenario", "17-Core Classifier Algorithm-Induction"),
    ("07-Compound Fault", "16-Feature Extraction Algorithm-Induction"),
    ("07-Compound Fault", "17-Core Classifier Algorithm-Induction"),
    ("06-Fault Severity", "17-Core Classifier Algorithm-Induction"),
]

# edge_group mapping to English
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
    """Call LLM and return plain text content."""
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
    """Extract the N-of-1 option name from LLM output (strict match)."""
    text = text.strip()
    # 1) Prefer exact whole-segment match
    for opt in options:
        if text == opt:
            return opt
    # 2) Find the option completely contained in text
    for opt in options:
        if opt in text:
            return opt
    return None


# ============================================================================
# Utility functions
# ============================================================================

def load_json(path: str) -> list:
    """Load JSON whose outermost type is a list."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError(f"input JSON outermost type is not list, but {type(data).__name__}: {path}")
    return data


def save_json(path: str, data) -> None:
    """Save JSON with proper formatting."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def build_output_path(input_path: str, suffix: str = "_conformance audit") -> str:
    """根据input路径generateoutput路径(同Directory, File名加后缀)"""
    base_dir = os.path.dirname(input_path)
    basename = os.path.basename(input_path)
    name, ext = os.path.splitext(basename)
    return os.path.join(base_dir, f"{name}{suffix}{ext}")


def _build_case_line_map_from_text(json_text: str) -> dict[str, int]:
    """
    从format后的 JSON textmediumparse每个顶层 case_id object在filemedium的起始row号（1-based）。

    实现思路：
      1) 遍历整个 json_text，build (character偏移 -> row号) 的findtable；
      2) 通过 json.JSONDecoder().raw_decode 顺序parse每个顶层object，
         拿到其起始character偏移，再用findtable换算为row号。
    """
    # 1) character偏移 -> 1-based row号 findtable
    # line_starts[i] table示第 (i+1) row的起始character偏移
    line_starts: list[int] = [0]
    for i, ch in enumerate(json_text):
        if ch == '\n':
            line_starts.append(i + 1)

    def pos_to_line(p: int) -> int:
        # 二分find: 找max的 line_starts[i] <= p
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

    # 2) 顺序parse顶层每个object
    while idx < n:
        # skipempty白和逗号
        while idx < n and (json_text[idx].isspace() or json_text[idx] == ','):
            idx += 1
        if idx >= n:
            break
        if json_text[idx] == ']':
            break
        # parse一个object
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
    Iterate over each edge, check source_node_original_name/source_node_name and
    target_node_original_name/target_node_name, and delete edges with null values.

    Determination rules (per user requirements):
      1) source: "Not Mentioned" + null
      2) source: "" + ""
      3) source: null + null
      4) source: "Not Mentioned" + null  (exact duplicate of 1), kept as in user original)
      5) source: "" + ""         (exact duplicate of 2), kept as in user original)
      6) source: null + null     (exact duplicate of 3), kept as in user original)
      -- and the same rules applied to target.

    Returns:
      (updated papers, statistics dictionary)
      statistics dictionary: { edge_group: {"null_edges": N, "deleted_edges": N1, "status": str}, ... }
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
            f"removed: {s['deleted_edges']}, status: {s['status']}."
        )
    # Other edge_group (if any) are also printed
    for g, s in stats.items():
        if g not in ("01-default edge", "02-causal edge", "03-evidence edge"):
            print(
                f"edge_group: {g}. Edges with null values detected: {s['null_edges']}, "
                f"removed: {s['deleted_edges']}, status: {s['status']}."
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
    """constructor LLM N 选 1 prompt(针对 edge 的 source/target node)"""
    options_str = " | ".join(options)
    return (
        f"【任务】你是一位PHM（fault prediction与health management）domain的graphnodeclassification助手。\n"
        f"现在给定一个node的现有information，请你综合 node_name、node_original_name、"
        f"node_description 三者的information，"
        f"从给定的 N 个standard选项medium**strict选择 1 个**作为该node的最终 node_name output。\n\n"
        f"【node位置】{side} 端node\n"
        f"【node_id】{node_id}\n"
        f"【node_type】{node_type}\n"
        f"【当前 node_name】{node_name}\n"
        f"【node_original_name】{node_original_name}\n\n"
        f"【N 选 1 选项（必须且只能从以下选项medium选 1 个，禁止自造）】\n"
        f"{options_str}\n\n"
        f"【forceoutput要求】\n"
        f"1) **只output 1 row**：你选medium的选项名称（必须一字不差等于上述某个选项）。\n"
        f"2) 严禁output：解释、思考过程、JSON、引号、标点、前后缀、换row、Markdown 等任何附加内容。\n"
        f"3) 不允许output \"Not Mentioned\"、\"N/A\"、\"不知道\" 等模糊回答。\n"
        f"4) 严禁output多个选项或重复内容。\n\n"
        f"现在请直接output 1 row最终答案："
    )


def _llm_correct_edge(
    side: str,
    node_id: str,
    node_type: str,
    node_name: str,
    node_original_name: str,
    options: set[str],
) -> Optional[str]:
    """call LLM 对non-compliant node_name 进row N 选 1 re-assign"""
    prompt = _build_llm_prompt_edge(
        side, node_id, node_type, node_name, node_original_name, options
    )
    messages = [
        {"role": "system", "content": "你是一个strict的knowledge graphnodeclassification助手。"},
        {"role": "user", "content": prompt},
    ]
    try:
        response = call_llm(messages)
        fixed = extract_n_from_llm_response(response, options)
        if fixed and fixed in options:
            return fixed
        # force再次validate: 取 response firstrowfirst个 Match项
        first_line = response.strip().splitlines()[0].strip() if response.strip() else ""
        if first_line in options:
            return first_line
        return None
    except LLMCallError:
        return None
    except Exception:
        return None


# program fallback: 基于off键词做 N 选 1
KEYWORD_MAP_FOR_PROGRAM: list[tuple[tuple[str, ...], str]] = [
    # (keywords, option)
    (("Aerospace", "aero", "aircraft", "uav", "无人机", "飞row"), "Aerospace"),
    (("Space", "space", "satellite", "spacecraft"), "Space"),
    (("Marine", "ship", "vessel", "naval"), "Marine"),
    (("Industrial", "industrial", "manufacturing", "wind turbine"), "Industrial"),
    (("Nuclear", "nuclear", "reactor"), "Nuclear"),
    (("Electronics", "motor", "transformer", "electronics"), "Electronics"),
    (("Vehicle", "vehicle", "automotive", "railway", "car", "train"), "Vehicle"),
    (("Other",), "Other"),

    (("单一operating condition",), "单一operating condition"),
    (("多operating condition",), "多operating condition"),
    (("variable condition", "time-varying", "non-stationary", "dynamic", "时变", "非稳态"), "variable condition"),

    (("Single Severity",), "Single Severity"),
    (("Multiple Severities",), "Multiple Severities"),

    (("无compound fault",), "无compound fault"),
    (("同结构内compound fault",), "同结构内compound fault"),
    (("跨结构compound fault",), "跨结构compound fault"),

    (("检测", "detection", "detect", "monitor"), "检测class任务"),
    (("诊断", "diagnosis", "classif", "identif"), "诊断class任务"),
    (("预测", "prediction", "rul", "prognos", "remaining useful life"), "预测class任务"),
    (("评估", "assessment", "evaluat"), "评估class任务"),
    (("Other Task",), "Other Task"),

    (("小faultsample", "few-shot", "few shot", "scarc", "small-sample", "insufficient samples"), "小faultsample"),
    (("零faultsample", "zero-shot", "zero shot", "unseen fault", "zero-shot"), "零faultsample"),
    (("distribution discrepancy", "domain shift", "cross-domain", "transfer", "cross-domain", "分布偏移"), "distribution discrepancyissue"),
    (("uncertainty", "uncertainty", "noise robust", "robust"), "uncertaintyissue"),
    (("compound faultissue", "compound", "mixed fault"), "compound faultissue"),
    (("复杂system", "system-level", "complicated", "复杂"), "复杂systemissue"),
    (("incipient degradation", "incipient", "degradation", "degradation", "弱fault"), "incipient degradation预测issue"),
    (("多源", "multimodal", "multimodal", "heterogeneous", "sensor fusion", "异构"), "多源异构、multimodaldataissue"),
    (("trustworthy", "interpretable", "interpret", "physics-inform", "physics-consistent"), "trustworthy、interpretableissue"),
    (("Otherissue",), "Otherissue"),

    (("zero-shot", "zero-shot"), "zero-shot"),
    (("Scarce", "insufficient", "scarce", "不足"), "Scarce"),
    (("Sufficient", "充足", "丰富"), "Sufficient"),

    (("high noise", "noisy", "noise", "扰动"), "high noise"),
    (("Normal",), "Normal"),

    (("low resource consumption", "lightweight", "embedded", "flops", "轻量", "online"), "low resource consumption"),
    (("Not Mentioned",), "Not Mentioned"),
    (("high resource consumption", "computational", "复杂度", "消耗大"), "high resource consumption"),
]


def _program_correct_edge(node_name: str, node_original_name: str, options: set[str]) -> Optional[str]:
    """program layer基于off键词做fallback N 选 1(edge node版)"""
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
    对边graphmedium各 edge 的 source/target node进row node_name conformance audit（N 选 1）。

    note：edge node的命名是带前缀的："source_node_type"/"source_node_name"/
    "source_node_original_name" 和 "target_*"。

    返回：
      (update后的 papers, statisticsdictionary)
      统计字典：{ node_type: {"total": N2, "non_compliant": N3, "compliant": N4,
                               "llm_fixed": N5, "program_fixed": N6}, ... }
    """
    print("\n" + "=" * 70)
    print("【Step 2】node node_name conformance audit（N 选 1）")
    print("=" * 70)

    # aggregate: 按 node_type
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

                # compliantdetermine
                if node_name in options:
                    stats[node_type]["compliant"] += 1
                    continue

                # non-compliant
                stats[node_type]["non_compliant"] += 1

                # LLM re-assign
                llm_fixed = _llm_correct_edge(
                    side, node_id, node_type, node_name, node_original_name, options
                )
                if llm_fixed is not None:
                    edge[f"{side}_node_name"] = llm_fixed
                    stats[node_type]["llm_fixed"] += 1
                    print(
                        f"    [LLM纠正] case={case_id} edge={edge_id} "
                        f"{side} {node_type} ({node_id}): '{node_name}' → '{llm_fixed}'"
                    )
                else:
                    # program fallback N 选 1
                    prog_fixed = _program_correct_edge(node_name, node_original_name, options)
                    if prog_fixed is None:
                        # final fallback: 取 options mediumfirst个
                        prog_fixed = next(iter(options))
                    edge[f"{side}_node_name"] = prog_fixed
                    stats[node_type]["program_fixed"] += 1
                    print(
                        f"    [程序纠正] case={case_id} edge={edge_id} "
                        f"{side} {node_type} ({node_id}): '{node_name}' → '{prog_fixed}' (LLM无效)"
                    )

    # consoleoutput(按 node_type 划分, onlyaggregatehas N 选 1 要求的 node_type)
    for nt in sorted(stats.keys()):
        s = stats[nt]
        if s["total"] == 0:
            continue
        print(
            f"node_type：{nt}。node_name总数为{s['total']}个，"
            f"non-compliant node_namecount为{s['non_compliant']}个，"
            f"compliant node_namecount为{s['compliant']}个，"
            f"after LLM correctioncompliant node_namecount为{s['llm_fixed']}个，"
            f"经过LLM correction后non-compliant node_name但force-corrected to compliance by programcount为{s['program_fixed']}个。"
        )

    return papers, stats


# ============================================================================
# Step 3: edge completenessaudit
# ============================================================================

def _get_node_type_group(paper: dict) -> set[str]:
    """从 paper 的All edge medium收集 source/target node_type deduplicate并集"""
    node_type_group: set[str] = set()
    for edge in paper.get("edges", []):
        s_t = edge.get("source_node_type")
        t_t = edge.get("target_node_type")
        if isinstance(s_t, str) and s_t:
            node_type_group.add(s_t)
        if isinstance(t_t, str) and t_t:
            node_type_group.add(t_t)
    # synchronouscheck nodes[] field(虽然边graph的 nodes 多is [], 但保留fallback)
    for node in paper.get("nodes", []) or []:
        nt = node.get("node_type")
        if isinstance(nt, str) and nt:
            node_type_group.add(nt)
    return node_type_group


def _filter_full_by_node_type_group(
    full_list: list[tuple],
    node_type_group: set[str],
) -> list[tuple]:
    """对 (source, target) 或 (source, target, edge_type) 形式的预置rule, 
    用 node_type_group 进row筛查：候选元组medium"所有"string都必须出现在
    node_type_group medium，才视为有效候选；否则remove（description该 case 没有对应的
    node_type，该候选边对该 case 不适用）。

    注：edge_type 是English（如 'contains'），通常不在 node_type_group medium，
    此class非 node_type stringfield会被automaticskip。
    """
    # 已知的 edge_type collection(出现在预置rulemedium的), 它们不应参与 node_type_group 筛查
    EDGE_TYPES: set[str] = {
        "contains", "is collected on", "can obviously reflect", "can be used for",
        "has_fault_mode", "contains_phm_task", "induces_problem", "motivates",
        "connects",
    }
    valid: list[tuple] = []
    for tup in full_list:
        # extract node_type field(不yes edge_type)
        nt_parts = [p for p in tup if isinstance(p, str) and p not in EDGE_TYPES]
        # all nt_parts 都必须在 node_type_group medium
        if all(part in node_type_group for part in nt_parts):
            valid.append(tup)
    return valid


def _check_pairwise_symmetry(edges: list[dict]) -> tuple[bool, list[dict]]:
    """
    check 03-evidence edge是否两两对称：
    对于 03-evidence edge的有效边collection，一定存在这样的"对"：它们的 source_node_id 相同，
    一个 target_node_id 是另一个 target_node_id 加 "-Induction" 后缀。

    return：(是否满足对称, 不满足对称的具体边informationlist)
    """
    if not edges:
        return True, []

    # 按 source_node_id 分组
    groups: dict[str, list[dict]] = {}
    for e in edges:
        sid = e.get("source_node_id")
        if sid is None:
            continue
        groups.setdefault(sid, []).append(e)

    unmatched: list[dict] = []
    for sid, group in groups.items():
        if len(group) < 2:
            # 该 source_id 下没has成对的边
            for e in group:
                unmatched.append({
                    "source_node_id": sid,
                    "target_node_id": e.get("target_node_id"),
                    "target_node_type": e.get("target_node_type"),
                    "reason": "该 source_node_id 下没有任何与之配对的另一条边",
                })
            continue

        # 在该组内checkyesnoAll edges都能找到带 "-Induction" 配对的另一条
        # 用 target_node_id 作is key
        target_ids = [e.get("target_node_id") for e in group]
        # constructorindex: 对于 target_id, aggregateyesnoexists target_id 与 "X" 或 "X-Induction" 成对
        # 这里采用更宽松的两两对称check: 
        # 把All target_id 拆分is base_name 与后缀(-Induction)
        base_to_full: dict[str, list[str]] = {}
        for tid in target_ids:
            if tid is None:
                continue
            if tid.endswith("-Induction"):
                base = tid[:-len("-Induction")]
                base_to_full.setdefault(base, []).append(tid)
            else:
                base_to_full.setdefault(tid, []).append(tid)
        # 对每个 e, check其 target_id yesno能找到一个与之配对的target id
        for e in group:
            tid = e.get("target_node_id")
            if tid is None:
                unmatched.append({
                    "source_node_id": sid,
                    "target_node_id": None,
                    "target_node_type": e.get("target_node_type"),
                    "reason": "target_node_id 为空",
                })
                continue
            if tid.endswith("-Induction"):
                base = tid[:-len("-Induction")]
                # 需要has base(或 base-Induction) 之一
                pair_candidates = {base, base + "-Induction"}
            else:
                pair_candidates = {tid, tid + "-Induction"}
            # 至少要has一个 pair_candidates 在 target_ids medium(且不yes自己)
            has_pair = any(
                (c in target_ids) and (c != tid)
                for c in pair_candidates
            )
            if not has_pair:
                unmatched.append({
                    "source_node_id": sid,
                    "target_node_id": tid,
                    "target_node_type": e.get("target_node_type"),
                    "reason": f"target_node_id={tid} 在该 source_node_id 下找不到与之配对的另一条边",
                })

    if unmatched:
        return False, unmatched
    return True, []


def audit_edge_completeness(papers: list[dict]) -> tuple[list[dict], dict]:
    """
    edge completenessaudit：
      - 01-default edge：要求每个 case 的 01-default edgecollection == node_type_group 过滤后的"01-全集"
      - 02-causal edge：要求每个 case 的 02-causal edgecollection ⊇ node_type_group 过滤后的"02-全集"
      - 02-causal edge supplement：要求每个 case 的 02-causal edge supplementcollection ⊇ "02-全集-supplement"medium至少 1 条
      - 03-evidence edge：要求每个 case 的 03-evidence edgecollection ⊇ "03-全集"medium至少 1 条
        且满足两两对称原则
    """
    print("\n" + "=" * 70)
    print("【Step 3】edge completenessaudit")
    print("=" * 70)

    total_cases = len(papers)

    # --- 01-default边 ---
    n_01_case_ok = 0
    n_01_case_fail = 0
    invalid_01_cases: list[dict] = []

    # --- 02-causal edges ---
    n_02_case_ok = 0
    n_02_case_fail = 0
    invalid_02_cases: list[dict] = []

    # --- 02-causal edgessupplement ---
    n_02_case_ok_add = 0
    n_02_case_fail_add = 0
    invalid_02_cases_add: list[dict] = []

    # --- 03-evidence edges ---
    n_03_case_ok = 0
    n_03_case_fail_1 = 0
    n_03_case_fail_2 = 0
    invalid_03_cases: list[dict] = []

    for paper in papers:
        case_id = paper.get("case_id", "?")
        node_type_group = _get_node_type_group(paper)
        edges = paper.get("edges", []) or []

        # === 01-default边 ===
        full_01_valid = _filter_full_by_node_type_group(DEFAULT_EDGE_FULL, node_type_group)
        n7 = len(full_01_valid)
        full_01_valid_set = set(full_01_valid)
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

        # === 02-causal edgessupplement ===
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
                "note": "current case_id 无任何有效的 edge{} 在 02-causal edge supplementcollectionmedium",
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

        # filter出落在"03-全集临时copy-valid"medium的 03-evidence edges
        valid_evidence_edges = [e for e in evidence_edges
                                if (e.get("source_node_type"), e.get("target_node_type")) in set(full_03_valid)]

        if n10_real == 0:
            # none效情况 1: N10_real == 0
            n_03_case_fail_1 += 1
            invalid_03_cases.append({
                "case_id": case_id,
                "expected_N10": n10,
                "actual_N10_real": n10_real,
                "fail_type": 1,
                "note": "current case_id 无任何有效的 edge{} 在 03-evidence edgecollectionmedium（属于无效情况 1）",
            })
        else:
            # 进一步check两两对称
            sym_ok, unmatched = _check_pairwise_symmetry(valid_evidence_edges)
            if sym_ok:
                n_03_case_ok += 1
            else:
                # none效情况 2: N10_real >= 1, 但对称Failure
                n_03_case_fail_2 += 1
                invalid_03_cases.append({
                    "case_id": case_id,
                    "expected_N10": n10,
                    "actual_N10_real": n10_real,
                    "fail_type": 2,
                    "note": "evidence edge存在但未两两对称（属于无效情况 2）",
                    "unmatched": unmatched,
                })

    n_03_case_fail = n_03_case_fail_1 + n_03_case_fail_2

    # consoleprint
    print()
    print("egdecompletenessaudit")
    print(
        f"1、edge_group = 01-default edge，经audit，遍历case_id{{}}total{total_cases}个，\n"
        f"有效case_id{{}}total{n_01_case_ok}个，无效case_id{{}}total{n_01_case_fail}个，\n"
        f"无效case_id具体为{[c['case_id'] for c in invalid_01_cases]}，"
        f"details详见audit logmdfile的「egdecompletenessaudit-01default edgeaudit」chapter。"
    )
    print(
        f"\n2、edge_group = 02-causal edge，经audit，遍历case_id{{}}total{total_cases}个，\n"
        f"有效case_id{{}}total{n_02_case_ok}个，无效case_id{{}}total{n_02_case_fail}个，\n"
        f"无效case_id具体为{[c['case_id'] for c in invalid_02_cases]}，"
        f"details详见audit logmdfile的「egdecompletenessaudit-02causal edgeaudit」chapter。"
    )
    print(
        f"\n3、edge_group = 02-causal edge（supplement），经supplementaudit，遍历case_id{{}}total{total_cases}个，\n"
        f"有效case_id{{}}total{n_02_case_ok_add}个，无效case_id{{}}total{n_02_case_fail_add}个，\n"
        f"无效case_id具体为{[c['case_id'] for c in invalid_02_cases_add]}，"
        f"details详见audit logmdfile的「egdecompletenessaudit-02causal edge supplementaudit」chapter。"
    )
    print(
        f"\n4、edge_group = 03-evidence edge，经audit，遍历case_id{{}}total{total_cases}个，\n"
        f"有效case_id{{}}total{n_03_case_ok}个，无效case_id{{}}total{n_03_case_fail}个，\n"
        f"由于evidence edge不存在导致无效的case_id{{}}total{n_03_case_fail_1}个；\n"
        f"由于evidence edge存在但未两两对称导致无效的case_id{{}}total{n_03_case_fail_2}个；\n"
        f"无效case_id具体为{[c['case_id'] for c in invalid_03_cases]}，"
        f"details详见audit logmdfile的「egdecompletenessaudit-03evidence edgeaudit」chapter。"
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
            "fail_1": n_03_case_fail_1,
            "fail_2": n_03_case_fail_2,
            "invalid_cases": invalid_03_cases,
        },
    }

    return papers, completeness_stats


# ============================================================================
# Step 4: graph structureconformanceaudit
# ============================================================================

def audit_graph_structure(
    papers: list[dict],
    case_line_map: dict[str, int] | None = None,
) -> tuple[list[dict], dict]:
    """
    auditgraph json 的嵌套结构与property名称是否norm。
    return (update后的 papers, statistics)
    """
    print("\n" + "=" * 70)
    print("【Step 4】graph-structure conformance audit")
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
        "edge_nums", "edge_cite_score", "edge_cite_count", "edge_id_list",
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
            issues.append("顶层元素不是dictobject")
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
            issues.append(f"nodes propertyclass型error，expected list，actual为 {type(nodes).__name__}")
        if not isinstance(edges, list):
            issues.append(f"edges propertyclass型error，expected list，actual为 {type(edges).__name__}")

        # edge property齐全性
        if isinstance(edges, list):
            for i, edge in enumerate(edges):
                if not isinstance(edge, dict):
                    issues.append(f"edges[{i}] 不是 dict 对象")
                    continue
                missing = EDGE_REQUIRED_FIELDS - set(edge.keys())
                if missing:
                    issues.append(f"edges[{i}] 缺少属性: {sorted(missing)}")

        # 顶层propertymissing(除 nodes/edges 外)
        required_no_lists = PAPER_REQUIRED_FIELDS - {"nodes", "edges"}
        missing_top = required_no_lists - set(paper.keys())
        if missing_top:
            issues.append(f"顶层缺少property: {sorted(missing_top)}")

        if issues:
            non_compliant_papers.append({
                "case_id": case_id,
                "start_line": start_line,
                "issues": issues,
            })
        else:
            compliant_papers.append(case_id)

    print()
    print("graph-structure conformance audit")
    print(f"1、graphcase_id{{}}总数 {total_papers}")
    print(f"2、已check的graphcase_id{{}}总数 {total_papers}")
    print(
        f"3、结构compliance的graphcase_id{{}}总数 {len(compliant_papers)}，"
        f"结构non-compliant的graphcase_id{{}}总数 {len(non_compliant_papers)}，"
        f"以及结构non-compliant的case_id {[it['case_id'] for it in non_compliant_papers]}。"
    )
    if non_compliant_papers:
        print("4、结构non-compliant的case_id，其non-compliant原因与对应graphjsonrow数：")
        for it in non_compliant_papers:
            line_info = (
                f"第 {it['start_line']} 行起"
                if it.get("start_line") is not None
                else "行号未知"
            )
            print(
                f"   - case_id：`{it['case_id']}`，所在行：{line_info}，"
                f"non-compliant原因：{'；'.join(it['issues'])}"
            )
    else:
        print("4、结构non-compliant的case_id：（无）")

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
    """generatecompleteauditlog md 内容"""
    lines: list[str] = []
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    lines.append(f"# 边merge-disambiguation-induction-compliant性auditlog")
    lines.append("")
    lines.append(f"**审查对象**: `{os.path.basename(input_path)}`")
    lines.append(f"**生成时间**: {ts}")
    lines.append(f"**generatescript**: `zotero_knowledge_graph_edge_extractor_消歧_归纳_conformance audit_v8.py`")
    lines.append("")
    lines.append("---")
    lines.append("")

    # 1. nodeempty值audit
    lines.append("## 1、nodeempty值audit")
    lines.append("")
    lines.append(
        "**audit逻辑**：遍历边graphjsonmedium各edge{}，分别针对 source/target 的"
        "node_original_name 与 node_name，按 6 条null valuerule任一满足则remove该 edge，"
        "并按 edge_group classificationstatistics。"
    )
    lines.append("")
    for g in ("01-default edge", "02-causal edge", "03-evidence edge"):
        s = null_stats.get(g, {"null_edges": 0, "deleted_edges": 0, "status": "无需删减"})
        lines.append(
            f"- edge_group：`{g}`。as determined存在各classwith null valuesedge{{}}为"
            f"`{s['null_edges']}`个，删除`{s['deleted_edges']}`个，"
            f"status为`{s['status']}`。"
        )
    for g, s in null_stats.items():
        if g not in ("01-default edge", "02-causal edge", "03-evidence edge"):
            lines.append(
                f"- edge_group：`{g}`。as determined存在各classwith null valuesedge{{}}为"
                f"`{s['null_edges']}`个，删除`{s['deleted_edges']}`个，"
                f"status为`{s['status']}`。"
            )
    lines.append("")
    lines.append("---")
    lines.append("")

    # 2. node node_name conformanceaudit
    lines.append("## 2、node node_name 规范性audit(N 选 1)")
    lines.append("")
    lines.append(
        "**audit逻辑**：对边graphjsonmedium各edge{}的source/targetnode，"
        "针对有 N 选 1 要求的 node_type，"
        "对 source_node_name/target_node_name 进rowstrict match；"
        "non-compliant的call LLM 进row N 选 1 re-assign，"
        "LLM 仍non-compliant则由程序基于keywordsforce N 选 1。"
    )
    lines.append("")
    for nt in sorted(name_stats.keys()):
        s = name_stats[nt]
        if s["total"] == 0:
            continue
        lines.append(
            f"- node_type：`{nt}`。node_name总数为`{s['total']}`个，"
            f"non-compliant node_namecount为`{s['non_compliant']}`个，"
            f"compliant node_namecount为`{s['compliant']}`个，"
            f"after LLM correctioncompliant node_namecount为`{s['llm_fixed']}`个，"
            f"经过LLM correction后non-compliant node_name但force-corrected to compliance by programcount为`{s['program_fixed']}`个。"
        )
    lines.append("")
    lines.append("---")
    lines.append("")

    # 3. edge completenessaudit
    lines.append("## 3、edge 完备性audit")
    lines.append("")

    # 3-1 01-default边
    lines.append("### 3-1、egde完备性audit-01default边audit")
    lines.append("")
    lines.append(
        "**判定方法**：\n"
        "1) copy `01-全集` 为 `01-全集临时copy`，对其medium每条候选 (source_node_type, "
        "target_node_type) 用 node_type_group 进row筛查：候选元组medium任一string在 "
        "node_type_group medium完全不存在，则将该候选从 `01-全集临时copy` mediumremove。"
        "遍历done后得到 `01-全集临时copy-有效`，其package含的元组count记为 N7。\n"
        "2) statisticscurrent case{} medium edge_group = `01-default edge` 的 edge{} count时，"
        "**同一class别的 (source_node_type, target_node_type) 只记 1 次**，"
        "即累计不重复的 edge{} 总数记为 N7_real。\n"
        "3) 若 N7 == N7_real，则该 case_id{} 的 01-default edgeaudit为**有效**（N_01_case_ok_num+1）；"
        "若 N7 != N7_real，则为**无效**（N_01_case_fail_num+1）。"
    )
    lines.append("")
    s01 = completeness_stats["01-default edge"]
    lines.append(
        f"- 遍历case_id{{}}total：`{s01['total_cases']}`个，"
        f"有效case_id{{}}total（`N_01_case_ok_num`）：`{s01['ok']}`个，"
        f"无效case_id{{}}total（`N_01_case_fail_num`）：`{s01['fail']}`个。"
    )
    lines.append("")
    if s01["invalid_cases"]:
        lines.append("**无效 case_id details（续写）**：")
        lines.append("")
        for it in s01["invalid_cases"]:
            missing_str = "、".join(it["missing"]) if it.get("missing") else "（无）"
            extra_str = "、".join(it.get("extra", [])) if it.get("extra") else "（无）"
            lines.append(
                f"- case_id：`{it['case_id']}`，期望边数 N7=`{it['expected_N7']}`，"
                f"actual不重复边数 N7_real=`{it['actual_N7_real']}`。"
            )
            lines.append(
                f"  - 缺少的 (source_node_type, target_node_type) 组合：{missing_str}"
            )
            lines.append(
                f"  - 多出的 (source_node_type, target_node_type) 组合：{extra_str}"
            )
    else:
        lines.append("无无效 case_id。")
    lines.append("")

    # 3-2 02-causal edges
    lines.append("### 3-2、egde完备性audit-02causal edgesaudit")
    lines.append("")
    s02 = completeness_stats["02-因果边"]
    lines.append(
        f"- 遍历case_id{{}}total：`{s02['total_cases']}`个，"
        f"有效case_id{{}}total（`N_02_case_ok_num`）：`{s02['ok']}`个，"
        f"无效case_id{{}}total（`N_02_case_fail_num`）：`{s02['fail']}`个。"
    )
    lines.append("")
    if s02["invalid_cases"]:
        lines.append("**无效 case_id 明细**：")
        lines.append("")
        for it in s02["invalid_cases"]:
            missing_str = "、".join(it["missing"]) if it["missing"] else "（无）"
            lines.append(
                f"- case_id：`{it['case_id']}`，期望边数`{it['expected_N8']}`，"
                f"actual边数`{it['actual_N8_real']}`，缺少的(source, target, edge_type)：{missing_str}"
            )
    else:
        lines.append("无无效 case_id。")
    lines.append("")

    # 3-3 02-causal edgessupplement
    lines.append("### 3-3、egdecompletenessaudit-02causal edgessupplementaudit")
    lines.append("")
    s02a = completeness_stats["02-causal edge supplement"]
    lines.append(
        f"- 遍历case_id{{}}total：`{s02a['total_cases']}`个，"
        f"有效case_id{{}}total（`N_02_case_ok_num_add`）：`{s02a['ok']}`个，"
        f"无效case_id{{}}total（`N_02_case_fail_num_add`）：`{s02a['fail']}`个。"
    )
    lines.append("")
    if s02a["invalid_cases"]:
        lines.append("**无效 case_id 明细**：")
        lines.append("")
        for it in s02a["invalid_cases"]:
            lines.append(
                f"- case_id：`{it['case_id']}`，expectedsupplement边数`{it['expected_N9']}`，"
                f"actualsupplement边数`{it['actual_N9_real']}`，"
                f"备注：{it.get('note', '')}"
            )
    else:
        lines.append("无无效 case_id。")
    lines.append("")

    # 3-4 03-evidence edges
    lines.append("### 3-4、egde完备性audit-03evidence edgesaudit")
    lines.append("")
    s03 = completeness_stats["03-evidence edge"]
    lines.append(
        f"- 遍历case_id{{}}total：`{s03['total_cases']}`个，"
        f"有效case_id{{}}total（`N_03_case_ok_num`）：`{s03['ok']}`个，"
        f"无效case_id{{}}total（`N_03_case_fail_num`）：`{s03['fail']}`个，"
        f"其medium由于evidence edge不存在导致无效的case_id{{}}total（`N_03_case_fail_num_1`）：`{s03['fail_1']}`个，"
        f"由于evidence edge存在但未两两对称导致无效的case_id{{}}total（`N_03_case_fail_num_2`）：`{s03['fail_2']}`个。"
    )
    lines.append("")
    if s03["invalid_cases"]:
        lines.append("**无效 case_id 明细**：")
        lines.append("")
        for it in s03["invalid_cases"]:
            fail_type = it.get("fail_type", "?")
            extra = ""
            if fail_type == 2 and it.get("unmatched"):
                extra = "\n  - 不对称的边details：\n" + "\n".join(
                    f"    - source_node_id=`{u['source_node_id']}`，"
                    f"target_node_id=`{u['target_node_id']}`，"
                    f"target_node_type=`{u['target_node_type']}`，"
                    f"原因：{u['reason']}"
                    for u in it["unmatched"]
                )
            lines.append(
                f"- case_id：`{it['case_id']}`，期望边数`{it['expected_N10']}`，"
                f"实际边数`{it['actual_N10_real']}`，"
                f"无效情况class型：`{fail_type}`，"
                f"备注：{it.get('note', '')}{extra}"
            )
    else:
        lines.append("无无效 case_id。")
    lines.append("")

    lines.append("---")
    lines.append("")

    # 4. graph structureconformanceaudit
    lines.append("## 4、graph structureconformanceaudit")
    lines.append("")
    lines.append(
        "**audit逻辑**：以「边graphjson-v3」（即audit后graph json）为input，"
        "程序遍历其medium每partialarray，check结构性norm要求并statisticscount。\n"
        "结构性normmainaudit：\n"
        "1) 边graphjson-v3 是否遵循嵌套结构——各循环的array嵌套结构是否闭合、norm；\n"
        "2) 边graphjson-v3 对应array结构medium的property名称是否准确、是否齐全；\n"
        "3) 对于non-compliant的 case_id，给出non-compliant原因与其在「边graphjson-v3」medium的起始row号。"
    )
    lines.append("")
    lines.append(f"- 图谱case_id{{}}总数：`{structure_stats['total_papers']}`")
    lines.append(f"- 已check的graphcase_id{{}}总数：`{structure_stats['checked_papers']}`")
    lines.append(
        f"- 结构compliance的graphcase_id{{}}总数：`{len(structure_stats['compliant_papers'])}`"
    )
    lines.append(
        f"- 结构non-compliant的graphcase_id{{}}总数：`{len(structure_stats['non_compliant_papers'])}`"
    )
    if structure_stats["non_compliant_papers"]:
        lines.append("- 结构non-compliantcase_iddetails（含row号与原因）：")
        lines.append("")
        for it in structure_stats["non_compliant_papers"]:
            line_info = (
                f"第 {it['start_line']} 行起"
                if it.get("start_line") is not None
                else "行号未知"
            )
            lines.append(
                f"  - case_id：`{it['case_id']}`，所在行：{line_info}"
            )
            for iss in it["issues"]:
                lines.append(f"    - {iss}")
    else:
        lines.append("- 结构non-compliantcase_iddetails：（无）")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"*本报告由 `zotero_knowledge_graph_edge_extractor_消歧_归纳_conformance audit_v8.py` automaticgenerate*")

    return "\n".join(lines)


# ============================================================================
# Main flow
# ============================================================================

def run():
    print("=" * 70)
    print("边合并-消歧-归纳-conformance auditscript")
    print("=" * 70)
    print(f"input files: {INPUT_GRAPH_PATH}")
    print("=" * 70)

    # --- Step 0: loadinput ---
    print("\n[Step 0] 加载边graph JSON ...")
    papers = load_json(INPUT_GRAPH_PATH)
    total_edges_before = sum(len(p.get("edges", []) or []) for p in papers)
    print(f"  共 {len(papers)} 篇文献, 总 edge 数: {total_edges_before}")

    # --- Step 1: nodeempty值audit → 边graphjson-v2 ---
    papers, null_stats = audit_null_values(papers)
    total_edges_after_null = sum(len(p.get("edges", []) or []) for p in papers)
    print(f"  null-value audit后总 edge 数: {total_edges_after_null}（remove {total_edges_before - total_edges_after_null}）")

    # --- Step 2: node node_name conformanceaudit → 边graphjson-v3 ---
    papers, name_stats = audit_node_name_for_edges(papers)

    # --- Step 3: edge completenessaudit(不modify papers)---
    papers, completeness_stats = audit_edge_completeness(papers)

    # --- Step 4: outputaudit后graph JSON(v3) ---
    output_json_path = build_output_path(INPUT_GRAPH_PATH, "_conformance audit")
    save_json(output_json_path, papers)
    print(f"\n  audit后graph JSON（v3）：{output_json_path}")
    print(f"  最终：{len(papers)} 篇文献, "
          f"{sum(len(p.get('edges', []) or []) for p in papers)} 条 edge")

    # --- Step 4 续: graph structureconformanceaudit(针对"边graphjson-v3"= audit后graph) ---
    with open(output_json_path, "r", encoding="utf-8") as f:
        json_text_v3 = f.read()
    case_line_map_v3 = _build_case_line_map_from_text(json_text_v3)
    print(f"  已从「{os.path.basename(output_json_path)}」parse出 "
          f"{len(case_line_map_v3)} 个 case_id 的起始row号。")
    papers, structure_stats = audit_graph_structure(papers, case_line_map_v3)

    # --- Step 5: outputauditlog md ---
    print("\n[Step 5] 保存audit log MD ...")

    # auditlog md: 与input同Directory, File名加后缀 "_compliant性audit"
    log_md_path = build_output_path(INPUT_GRAPH_PATH, "_conformance audit").replace(".json", ".md")
    log_content = build_audit_log_md(
        null_stats, name_stats, completeness_stats, structure_stats, INPUT_GRAPH_PATH
    )
    os.makedirs(os.path.dirname(log_md_path), exist_ok=True)
    with open(log_md_path, "w", encoding="utf-8") as f:
        f.write(log_content)
    print(f"  audit log MD：{log_md_path}")

    print("\n" + "=" * 70)
    print("auditdone")
    print("=" * 70)


if __name__ == "__main__":
    run()
