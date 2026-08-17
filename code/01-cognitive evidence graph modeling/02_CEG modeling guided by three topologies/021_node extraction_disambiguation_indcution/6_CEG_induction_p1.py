# -*- coding: utf-8 -*-
"""
Algorithm-category induction summary-table generation program V4
========================================================================
Functions:
  1. Load the disambiguated node JSON array (node JSON array v1)
  2. Extract all node_names from node_type="09-Problem Scenario" to form the "problem-node inventory"
  3. Extract node_name and node_description for each node_type in {15,16,17,18,19} to form
     the "algorithm-node inventory" (including description information)
  4. Dynamic assembly of 5 node_type-specific prompts -> saved to the "induction summary-table prompts" directory (for human review)
  5. After human review and confirmation, run again -> LLM reads the prompt files -> outputs the induction tables
  6. 5 induction tables generated in parallel with all 9 API keys fully concurrent (round-robin)

V4 new prompt pre-generation + human-review workflow:
  - Dynamically assemble prompts -> saved as "{type_name}归纳提示词.md"
  - Prompt file path: PROMPT_BASE_DIR
  - The LLM directly reads the prompt file content to perform the output
  - Skip if the prompt file already exists; skip if the induction table file already exists

Outputs:
  - Induction prompts (for human review):
      {type_name}归纳提示词.md  x 5
  - Induction summary tables (LLM output):
      {input_filename}_归纳_{type_key}节点大表.md  x 5

Dependencies:
  pip install google-genai
"""

import os
import re
import json
import time
from pathlib import Path
from collections import defaultdict
from threading import Lock, Semaphore
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Optional

# ============================================================================
# User configuration
# ============================================================================

INPUT_JSON_PATH = r"./output/final_merged/A1-node_merged_disambiguated/[2277EAKD][ZZZRPFBV]_merged_nodes_conformance_audit_merged_conformance_audit_disambiguated_conformance_audit.json"

OUTPUT_BASE_DIR = r"./output/final_merged/A2-node_merged_disambiguated_induced/induction_inventory"

PROMPT_BASE_DIR = r"./output/final_merged/A2-node_merged_disambiguated_induced/induction_summary_table_prompts"

LLM_CONFIG = {
    "provider": "gemini",
    "model": "gemini-3.5-flash",
    "base_url": os.environ.get("BFGA_LLM_API_URL", "https://YOUR.LLM.ENDPOINT/"),
    "timeout": 300,
}

# IMPORTANT: Provide your own API keys before running. The list below should be filled with valid keys.
API_KEYS = []

# Per-Key concurrency limit: maximum concurrent requests each API Key can hold at the same time
# Design goal: 10 keys x 3 = 30 maximum concurrent LLM requests, kept consistent with edge_extractor_v8
# This way, all 10 keys can be called truly concurrently, rather than polling a single Key and queuing requests sequentially
PER_KEY_LIMIT = 3

# Global thread-pool ceiling: max_workers should be >= total_keys * PER_KEY_LIMIT so each Key's
# semaphore slots are fully utilized; here we take 10 x 3 = 30, leaving 1 buffer, using 32
MAX_WORKERS = 32

# Each algorithm type triggers one LLM call; lower temperature to keep results stable
LLM_TEMPERATURE = 0.05


# ============================================================================
# RoundRobinKeyManager: thread-safe API key round-robin manager
# ============================================================================

class RoundRobinKeyManager:
    """
    Thread-safe round-robin Key manager with per-Key rate limiting (max N concurrent requests per Key).

    1. Each Key has an independent Semaphore(per_key_limit) to prevent a single Key from
   being overwhelmed at the same moment and causing server-side disconnection / 10054 errors.
2. A main round-robin counter assigns Keys (ensuring all 10 Keys are used evenly without
   "false concurrency" -- i.e., situations where the pool nominally has 10 Keys but only
   a few are actually in use at the same time).
3. After obtaining a Key, the task must acquire an occupancy slot; the slot is released
   when the call finishes. When the Semaphore is full, subsequent requests block, which
   actually enforces true per-Key rate limiting.
    """

    def __init__(self, keys: list[str], per_key_limit: int = 3):
        self._keys = keys
        self._lock = Lock()
        self._idx = 0
        self._usage: dict[str, int] = {}
        self._sems: list[Semaphore] = [Semaphore(per_key_limit) for _ in keys]
        self._per_key_limit = per_key_limit

    def get_key(self) -> str:
        """Round-robin fetch of the next Key (thread-safe; ensures all 10 Keys are evenly distributed)"""
        with self._lock:
            key = self._keys[self._idx % len(self._keys)]
            self._idx += 1
            self._usage[key] = self._usage.get(key, 0) + 1
            return key

    def acquire(self, key: str) -> int:
        """
        Acquire one concurrency slot for the specified Key; returns the Key index.
        If the slot for that Key is full, blocks until a slot is released.
        """
        key_idx = self._keys.index(key)
        self._sems[key_idx].acquire()
        return key_idx

    def release(self, key_idx: int) -> None:
        """Release one concurrency slot for the specified Key index."""
        self._sems[key_idx].release()

    @property
    def total_keys(self) -> int:
        return len(self._keys)

    @property
    def per_key_limit(self) -> int:
        return self._per_key_limit

    def usage_report(self) -> dict[str, int]:
        with self._lock:
            return dict(self._usage)


# Global Key manager (lazily initialized)
_key_manager: Optional[RoundRobinKeyManager] = None


def get_key_manager() -> RoundRobinKeyManager:
    global _key_manager
    if _key_manager is None:
        _key_manager = RoundRobinKeyManager(API_KEYS, per_key_limit=PER_KEY_LIMIT)
    return _key_manager


# ============================================================================
# Part 1: LLM invocation utility
# ============================================================================

# Maximum retries (excluding the first call)
MAX_RETRIES = 3
# Seconds to wait before retry (exponential backoff)
RETRY_BASE_DELAY = 3


def _call_gemini_single_key(
    prompt: str, config: dict, api_key: str,
) -> dict:
    """
    Single Gemini API call (uses the specified api_key; no further distribution from key_manager).

    Concurrency model:
      The caller must obtain api_key from key_manager.get_key() before invoking this function,
      and occupy one slot for that Key via key_manager.acquire(api_key); after the call
      completes (whether successfully or not), the caller releases the slot. This function
      itself performs no Key allocation, avoiding "double allocation" and "false concurrency".
    """
    try:
        import google.genai as genai
        from google.genai.types import HttpOptions
    except ImportError:
        raise ImportError("Please install: pip install google-genai")

    base = config.get("base_url", "https://generativelanguage.googleapis.com/").strip()
    if not base.endswith("/"):
        base += "/"
    timeout_ms = max(1, int(float(config.get("timeout", 300)) * 1000))

    extra_headers = {}
    if api_key.startswith("sk-"):
        extra_headers["Authorization"] = f"Bearer {api_key}"

    http_opts = HttpOptions(base_url=base, timeout=timeout_ms,
                            headers=extra_headers or None)
    client = genai.Client(api_key=api_key, http_options=http_opts)

    model_name = config.get("model", "gemini-3.1-pro-preview")
    response = client.models.generate_content(
        model=model_name,
        contents=[prompt],
        config={"temperature": config.get("temperature", LLM_TEMPERATURE),
                "max_output_tokens": 30000},
    )

    input_tokens = output_tokens = total_tokens = 0
    try:
        usage = response.usage_metadata
        if usage:
            input_tokens = getattr(usage, "prompt_token_count", 0) or 0
            output_tokens = getattr(usage, "candidates_token_count", 0) or 0
            total_tokens = getattr(usage, "total_token_count", 0) or 0
    except Exception:
        pass

    try:
        parts = response.candidates[0].content.parts
        text = "".join(part.text for part in parts
                       if hasattr(part, "text") and part.text)
    except Exception:
        text = response.text

    return {
        "text": text,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": total_tokens,
    }


def call_llm_with_retry(
    prompt: str, config: dict, key_manager: RoundRobinKeyManager,
) -> str:
    """
    Call the LLM via the Key manager's round-robin + exponential-backoff retry logic.

    Concurrency model (key points, aligned with zotero_knowledge_graph_edge_extractor_v8):
      1. First call key_manager.get_key() to obtain a Key (round-robin assignment, ensuring
         all 10 Keys are distributed evenly without "false concurrency").
      2. Then call key_manager.acquire(api_key) to occupy one concurrency slot for that Key
         (max PER_KEY_LIMIT concurrent requests per Key).
      3. Retry up to MAX_RETRIES times on this Key; in any branch (success/exception),
         the slot is released via finally so the per-Key concurrency count returns to normal.
      4. This yields 10 Keys x PER_KEY_LIMIT = 30 truly concurrent LLM requests, matching
         the MAX_WORKERS thread-pool capacity.
    """
    # 1) Round-robin assign a Key; 2) occupy one concurrency slot for that Key
    assigned_key = key_manager.get_key()
    key_idx = key_manager.acquire(assigned_key)

    last_error: Optional[Exception] = None
    try:
        for attempt in range(MAX_RETRIES + 1):
            try:
                result = _call_gemini_single_key(
                    prompt, config, assigned_key,
                )
                return result["text"]
            except Exception as e:
                last_error = e
                err_msg = str(e).lower()
                if any(kw in err_msg for kw in [
                    "quota", "rate", "limit", "429",
                    "resource_exhausted", "internal error",
                    "timeout", "connection", "10054", "reset",
                ]):
                    delay = RETRY_BASE_DELAY * (2 ** attempt)
                    print(f"      [Key {key_idx + 1}] request failed ({type(e).__name__}): {e}, "
                          f"retry after {delay}s (attempt {attempt + 1}/{MAX_RETRIES + 1})...")
                    time.sleep(delay)
                    continue
                else:
                    # Non-rate-limit / connection-class errors: do not retry; raise directly
                    raise
        # All retries on this Key exhausted
        raise RuntimeError(
            f"Key {key_idx + 1} failed {MAX_RETRIES + 1} consecutive calls. Last error: {last_error}"
        )
    finally:
        # In any branch (success / exception) release the Key's slot
        key_manager.release(key_idx)


# ============================================================================
# Part 2: data extraction utilities
# ============================================================================

def load_json(path: str) -> list:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def collect_node_info(data: list, target_types: list[str]) -> list[dict]:
    """
    Collect information for all nodes of the specified node_types from the papers data.
    Each record contains {case_id, node_id, node_name, node_description}.
    Each (case_id + node_name) combination appears only once.
    """
    seen = set()
    nodes = []
    for paper in data:
        case_id = paper.get("case_id", "")
        for node in paper.get("nodes", []):
            if node.get("node_type") in target_types:
                name = node.get("node_name")
                if name and isinstance(name, str):
                    key = (case_id, name.strip())
                    if key not in seen:
                        seen.add(key)
                        nodes.append({
                            "case_id": case_id,
                            "node_id": node.get("node_id", ""),
                            "node_name": name.strip(),
                            "node_description": node.get("node_description") or "",
                        })
    return nodes


# ============================================================================
# Part 3: prompt construction
# ============================================================================

# ============================================================================
# Part 3: 5 node_type-specific prompts
# ============================================================================
#
# Design principles:
#   - Each node_type has its own prompt; the core task is "induction of main categories of subordinate algorithm nodes"
#   - Prompt structure (preserving existing strengths):
#       Step 1: induce the main algorithm-category list (with three induction criteria)
#       Step 2: write an entry for each main algorithm category
#       Output format requirements
#       Important notes (extended)
#   - Three-factor reference system:
#       Factor 1: node_type semantics and boundary constraints (PHM general knowledge + type definition)
#       Factor 2: node_name + node_description of subordinate algorithm nodes (factual evidence)
#       Factor 3: three induction criteria -- representativeness, distinctiveness, completeness
#   - Absolutely forbidden: inducing the LLM to perform node_type classification on input nodes
# ============================================================================


def _build_header(type_name: str, problem_names_str: str, algo_names_str: str) -> str:
    """Build the header shared by the five prompts (role + task background + problem inventory + algorithm-node inventory)."""
    return f"""## 角色设定
你是一位 PHM（Prognostics and Health Management，预测与健康管理）领域的资深学术顾问，拥有 20 年以上的故障诊断、寿命预测、智能算法研究经验，精通传统信号处理、机器学习、深度学习、迁移学习、数据生成等各类算法体系。

---

## 任务背景

我正在对 PHM 领域近年（截至 2026 年）学术文献中的知识图谱节点进行系统归纳。现有从文献中抽取的节点清单如下：

**本数据集涉及的问题场景清单（node_type="09-Problem Scenario"）：**
{problem_names_str}

**本数据集涉及的 [{type_name}] 节点清单（直接抽取自文献）：**
{algo_names_str}
"""


def _step1_block(type_name: str, algo_names_mention: str,
                 other_definitions_str: str) -> str:
    """Step 1: induce the main algorithm-category list + three induction criteria."""
    return f"""---

### 第一步：归纳主流算法类别清单

请结合 PHM 领域通识，归纳 **"{type_name}"** 下属主流算法类别（算法族 / 算法范式），而非具体模型实现名称。

**目标类型内涵定义：**

{other_definitions_str}

**归纳时必须同时满足以下三条原则：**

1. **代表性**：只选取在 PHM 及近似领域（机械故障诊断、旋转机械、化工过程、医学诊断等）具有广泛影响力的主流算法类别。应以 **本数据集涉及的 [{type_name}] 节点清单** 中的具体算法为首要锚点，结合领域通识判断每一项的类别归属。数据集中未出现的算法，原则上不作为归纳算法类别的参考。

2. **区分性**：各主流算法类别之间应有清晰区分，每个类别都有各自鲜明的技术原理和适用特征。即，针对**本数据集涉及的 [{type_name}] 节点清单**，被某种算法类别归纳的算法节点，应该和其他算法节点具有一定区分性。

3. **完备性**：选取的算法类别应能覆盖上方"问题场景清单"所代表的问题类型的技术解决路径，且能容纳 **本数据集涉及的 [{type_name}] 节点清单** 中所有具体算法的归纳归属。
"""


def _step2_block(type_name: str) -> str:
    """Step 2: write an entry for each main algorithm category (shared by all 5 types; type_name fills the table-header placeholder)."""
    return f"""---

### 第二步：为每个主流算法类别撰写条目

对每个归纳出的主流算法类别，请撰写以下四个维度的说明：

| 维度 | 填写要求 |
|------|---------|
| **类别名称** | 使用业内标准的算法类别名称（中文为主，关键术语可附英文）。**禁止**在类别名称中嵌入具体算法实例的名称（如禁止"元学习与双层优化"，应改为"元学习"；禁止"CNN与ResNet"，应改为"卷积神经网络"）。类别名称应具有标准性、规范性和可泛化性，能容纳同类算法的未来变体。 |
| **类别内涵** | 清晰阐述该类别的核心原理、技术路线、主要代表算法（2-4 个代表性具体模型名称）。已在 **"本数据集涉及的 [{type_name}] 节点清单"** 中出现的算法实例优先列入。 |
| **归纳标准** | 解释为什么将某些具体算法归入该类别，归类的关键依据是什么（原理相似 / 优化目标一致 / 应用场景重叠等）。 |
| **适用性分析** | 该类别算法的主要优势。简洁描述即可。**不需填写**适用场景和局限性（这两项已在问题场景清单中体现，读者可自行对应）。 |
"""


def _output_format_block(type_name: str) -> str:
    """Output-format-requirements section (shared by all 5 types)."""
    return f"""---

## output格式要求

请严格按以下 Markdown 表格格式输出，每行对应一个主流算法类别，共输出**一张完整的表格**：

```markdown
### {type_name} 主流算法类别归纳表

| 序号 | 类别名称 | 类别内涵 | 归纳标准 | 适用性分析 |
|------|---------|---------|---------|-----------|
| 1 | （类别名称） | （类别内涵） | （归纳标准） | （适用性分析） |
| 2 | ... | ... | ... | ... |
```
"""


# --------------------------------------------------------------------------
# Type-15 node-specific prompt
# --------------------------------------------------------------------------

def build_prompt_type15(
    algo_node_info: list[dict],
    problem_names: list[str],
) -> str:
    """
    [15-Data Preprocessing Algorithm] (Data-Preprocessing Algorithm Class) specific prompt

    Core task: induce main categories of algorithm nodes under this type (e.g., denoising,
    filtering, normalization) and produce the "Data-Preprocessing Algorithm Categories
    Induction Table". The task is NOT node_type classification of input nodes.
    """
    type_name = "15-Data Preprocessing Algorithm"
    type_definition = (
        "在准确信号进入特征提取或判别模型之前，对信号执行清洗、增强、规范化的算法。"
        "判别：去噪/滤波/重采样/归一化/分帧/滑窗分割/异常值剔除。"
        "注意：简单加噪/裁剪作为数据增强也归入此类。"
    )

    # 节点清单
    if algo_node_info:
        node_lines = []
        for n in sorted(algo_node_info, key=lambda x: x["node_name"]):
            desc = n["node_description"].strip()
            if desc:
                node_lines.append(f"- **{n['node_name']}**：{desc}")
            else:
                node_lines.append(f"- **{n['node_name']}**")
        algo_names_str = "\n".join(node_lines)
    else:
        algo_names_str = "（本数据集中未出现该类型节点）"

    problem_names_str = "\n".join(f"- {n}" for n in sorted(set(problem_names))) if problem_names else "（无）"

    unique_names = sorted(set(n["node_name"] for n in algo_node_info if n["node_name"]))
    algo_names_mention = "、".join(f"`{n}`" for n in unique_names) if unique_names else "无"

    header = _build_header(type_name, problem_names_str, algo_names_str)

    target_block = f"> **{type_name}**：{type_definition}"

    step1 = _step1_block(type_name, algo_names_mention, target_block)
    step2 = _step2_block(type_name)
    output_fmt = _output_format_block(type_name)

    important_notes = """**重要提示：**
- **本任务的核心是类别归纳，而非节点归类**：你的任务是对**本数据集涉及的 [15-Data Preprocessing Algorithm] 节点清单**，归纳出它们各自隶属的主流算法类别（即对这些算法进行分类）。任务绝不是判断某个算法是否属于[15-Data Preprocessing Algorithm]——这一点在数据抽取阶段已经完成。
- **必须使用数据集**：你的归纳结果必须以 **本数据集涉及的 [15-Data Preprocessing Algorithm] 节点清单** 中的具体算法实例为核心依据，不可脱离该清单凭空归纳。若清单中某算法无法归入任何已归纳的类别，应将其单独说明。
- **仅输出上述标题和表格**，不要输出任何额外说明文字。
- 表格中每个单元格的文字应简洁、明确、专业，适合直接用于学术文档。
- 类别名称必须使用业内通用标准名称，不要包含具体算法实例的专有名称。
- 每个单元格内容如果较长可使用 `<br>` 换行，但不要使用表格以外的 Markdown 语法。
- **不要进行 node_type 归类**：输入中已明确标注为[15-Data Preprocessing Algorithm]的算法节点，无需再次判断其是否属于[15-Data Preprocessing Algorithm]，直接对它们进行类别归纳即可。
"""

    return f"""{header}

## 你的任务（核心）

请结合 PHM 领域通识，归纳**本数据集涉及的 [15-Data Preprocessing Algorithm] 节点清单**。

本任务的核心是：对本数据集中已经明确属于[15-Data Preprocessing Algorithm]的算法节点（详见**本数据集涉及的 [15-Data Preprocessing Algorithm] 节点清单**），基于其技术原理和功能目的，归纳出它们各自隶属于哪个主流算法类别，生成"数据预处理算法类别归纳表"。

{step1}
{step2}
{output_fmt}
{important_notes}

请开始输出：
"""


# --------------------------------------------------------------------------
# 16类节点专属Prompt
# --------------------------------------------------------------------------

def build_prompt_type16(
    algo_node_info: list[dict],
    problem_names: list[str],
) -> str:
    """
    [16-Feature Extraction Algorithm] (Feature-Extraction Algorithm Class) specific prompt

    Core task: induce main categories of algorithm nodes under this type (e.g., CNN backbone,
    autoencoder, EMD) and produce the "Feature-Extraction Algorithm Categories Induction Table".
    """
    type_name = "16-Feature Extraction Algorithm"
    type_definition = (
        "从信号/数据中提取可表征设备状态的特征向量或表示。"
        "判别：信号→特征向量/嵌入表示（非最终分类/回归结果）。"
        "包括：CNN/ResNet backbone、自编码器Encoder输出、EMD/VMD模态分量作特征、Attention特征加权。"
    )

    if algo_node_info:
        node_lines = []
        for n in sorted(algo_node_info, key=lambda x: x["node_name"]):
            desc = n["node_description"].strip()
            if desc:
                node_lines.append(f"- **{n['node_name']}**：{desc}")
            else:
                node_lines.append(f"- **{n['node_name']}**")
        algo_names_str = "\n".join(node_lines)
    else:
        algo_names_str = "（本数据集中未出现该类型节点）"

    problem_names_str = "\n".join(f"- {n}" for n in sorted(set(problem_names))) if problem_names else "（无）"

    unique_names = sorted(set(n["node_name"] for n in algo_node_info if n["node_name"]))
    algo_names_mention = "、".join(f"`{n}`" for n in unique_names) if unique_names else "无"

    header = _build_header(type_name, problem_names_str, algo_names_str)

    target_block = f"> **{type_name}**：{type_definition}"

    step1 = _step1_block(type_name, algo_names_mention, target_block)
    step2 = _step2_block(type_name)
    output_fmt = _output_format_block(type_name)

    important_notes = """**重要提示：**
- **本任务的核心是类别归纳，而非节点归类**：你的任务是对**本数据集涉及的 [16-Feature Extraction Algorithm] 节点清单**，归纳出它们各自隶属的主流算法类别（即对这些算法进行分类）。任务绝不是判断某个算法是否属于[16-Feature Extraction Algorithm]——这一点在数据抽取阶段已经完成。
- **必须使用数据集**：你的归纳结果必须以 **本数据集涉及的 [16-Feature Extraction Algorithm] 节点清单** 中的具体算法实例为核心依据，不可脱离该清单凭空归纳。若清单中某算法无法归入任何已归纳的类别，应将其单独说明。
- **仅输出上述标题和表格**，不要输出任何额外说明文字。
- 表格中每个单元格的文字应简洁、明确、专业，适合直接用于学术文档。
- 类别名称必须使用业内通用标准名称，不要包含具体算法实例的专有名称。
- 每个单元格内容如果较长可使用 `<br>` 换行，但不要使用表格以外的 Markdown 语法。
- **不要进行 node_type 归类**：输入中已明确标注为[16-Feature Extraction Algorithm]的算法节点，无需再次判断其是否属于[16-Feature Extraction Algorithm]，直接对它们进行类别归纳即可。
"""

    return f"""{header}

## 你的任务（核心）

请结合 PHM 领域通识，归纳**本数据集涉及的 [16-Feature Extraction Algorithm] 节点清单**。

本任务的核心是：对本数据集中已经明确属于[16-Feature Extraction Algorithm]的算法节点（如**本数据集涉及的 [16-Feature Extraction Algorithm] 节点清单**），基于其技术原理和功能目的，归纳出它们各自隶属于哪个主流算法类别，生成"特征提取算法类别归纳表"。

{step1}
{step2}
{output_fmt}
{important_notes}

请开始输出：
"""


# --------------------------------------------------------------------------
# Type-17 node-specific prompt
# --------------------------------------------------------------------------

def build_prompt_type17(
    algo_node_info: list[dict],
    problem_names: list[str],
) -> str:
    """
    [17-Core Classifier Algorithm] (Core-Discriminator Algorithm Class) specific prompt

    Core task: induce main categories of algorithm nodes under this type (e.g., CNN classifier
    head, XGBoost, SVM) and produce the "Core-Discriminator Algorithm Categories Induction Table".
    """
    type_name = "17-Core Classifier Algorithm"
    type_definition = (
        "直接输出故障诊断/异常检测/寿命预测结果的决策模型，是PHM算法链条的终端决策环节。"
        "判别：论文算法流程最下游的决策模块。"
        "包括：端到端深度模型、集成模型（RF/XGBoost/AdaBoost）、SVM/KNN/Softmax、backbone+分类头的分类头部分。"
    )

    if algo_node_info:
        node_lines = []
        for n in sorted(algo_node_info, key=lambda x: x["node_name"]):
            desc = n["node_description"].strip()
            if desc:
                node_lines.append(f"- **{n['node_name']}**：{desc}")
            else:
                node_lines.append(f"- **{n['node_name']}**")
        algo_names_str = "\n".join(node_lines)
    else:
        algo_names_str = "（本数据集中未出现该类型节点）"

    problem_names_str = "\n".join(f"- {n}" for n in sorted(set(problem_names))) if problem_names else "（无）"

    unique_names = sorted(set(n["node_name"] for n in algo_node_info if n["node_name"]))
    algo_names_mention = "、".join(f"`{n}`" for n in unique_names) if unique_names else "无"

    header = _build_header(type_name, problem_names_str, algo_names_str)

    target_block = f"> **{type_name}**：{type_definition}"

    step1 = _step1_block(type_name, algo_names_mention, target_block)
    step2 = _step2_block(type_name)
    output_fmt = _output_format_block(type_name)

    important_notes = """**重要提示：**
- **本任务的核心是类别归纳，而非节点归类**：你的任务是对**本数据集涉及的 [17-Core Classifier Algorithm] 节点清单**，归纳出它们各自隶属的主流算法类别（即对这些算法进行分类）。任务绝不是判断某个算法是否属于[17-Core Classifier Algorithm]——这一点在数据抽取阶段已经完成。
- **必须使用数据集**：你的归纳结果必须以 **本数据集涉及的 [17-Core Classifier Algorithm] 节点清单** 中的具体算法实例为核心依据，不可脱离该清单凭空归纳。若清单中某算法无法归入任何已归纳的类别，应将其单独说明。
- **仅输出上述标题和表格**，不要输出任何额外说明文字。
- 表格中每个单元格的文字应简洁、明确、专业，适合直接用于学术文档。
- 类别名称必须使用业内通用标准名称，不要包含具体算法实例的专有名称。
- 每个单元格内容如果较长可使用 `<br>` 换行，但不要使用表格以外的 Markdown 语法。
- **不要进行 node_type 归类**：输入中已明确标注为 [17-Core Classifier Algorithm] 的算法节点，无需再次判断其是否属于[17-Core Classifier Algorithm]，直接对它们进行类别归纳即可。
"""

    return f"""{header}

## 你的任务（核心）

请结合 PHM 领域通识，归纳**本数据集涉及的 [17-Core Classifier Algorithm] 节点清单**。

本任务的核心是：对本数据集中已经明确属于[17-Core Classifier Algorithm]的算法节点（详见**本数据集涉及的 [17-Core Classifier Algorithm] 节点清单**），基于其技术原理和功能目的，归纳出它们各自隶属于哪个主流算法类别，生成"核心判别器算法类别归纳表"。

{step1}
{step2}
{output_fmt}
{important_notes}

请开始输出：
"""


# --------------------------------------------------------------------------
# Type-18 node-specific prompt
# --------------------------------------------------------------------------

def build_prompt_type18(
    algo_node_info: list[dict],
    problem_names: list[str],
) -> str:
    """
    [18-Data Generation Algorithm] (Data-Generation Algorithm Class) specific prompt

    Core task: induce main categories of algorithm nodes under this type (e.g., GAN, VAE, SMOTE)
    and produce the "Data-Generation Algorithm Categories Induction Table".
    """
    type_name = "18-Data Generation Algorithm"
    type_definition = (
        "产出新的训练样本/仿真数据（样本扩充/少样本补充/虚拟数据构造）。"
        "判别：算法目的是生成新样本。"
        "包括：GAN/VAE/扩散模型用于生成、SMOTE/过采样/插值生成、数字孪生仿真。"
    )

    if algo_node_info:
        node_lines = []
        for n in sorted(algo_node_info, key=lambda x: x["node_name"]):
            desc = n["node_description"].strip()
            if desc:
                node_lines.append(f"- **{n['node_name']}**：{desc}")
            else:
                node_lines.append(f"- **{n['node_name']}**")
        algo_names_str = "\n".join(node_lines)
    else:
        algo_names_str = "（本数据集中未出现该类型节点）"

    problem_names_str = "\n".join(f"- {n}" for n in sorted(set(problem_names))) if problem_names else "（无）"

    unique_names = sorted(set(n["node_name"] for n in algo_node_info if n["node_name"]))
    algo_names_mention = "、".join(f"`{n}`" for n in unique_names) if unique_names else "无"

    header = _build_header(type_name, problem_names_str, algo_names_str)

    target_block = f"> **{type_name}**：{type_definition}"

    step1 = _step1_block(type_name, algo_names_mention, target_block)
    step2 = _step2_block(type_name)
    output_fmt = _output_format_block(type_name)

    important_notes = """**重要提示：**
- **本任务的核心是类别归纳，而非节点归类**：你的任务是对**本数据集涉及的 [18-Data Generation Algorithm] 节点清单**，归纳出它们各自隶属的主流算法类别（即对这些算法进行分类）。任务绝不是判断某个算法是否属于[18-Data Generation Algorithm]——这一点在数据抽取阶段已经完成。
- **必须使用数据集**：你的归纳结果必须以 **本数据集涉及的 [18-Data Generation Algorithm] 节点清单** 中的具体算法实例为核心依据，不可脱离该清单凭空归纳。若清单中某算法无法归入任何已归纳的类别，应将其单独说明。
- **仅输出上述标题和表格**，不要输出任何额外说明文字。
- 表格中每个单元格的文字应简洁、明确、专业，适合直接用于学术文档。
- 类别名称必须使用业内通用标准名称，不要包含具体算法实例的专有名称。
- 每个单元格内容如果较长可使用 `<br>` 换行，但不要使用表格以外的 Markdown 语法。
- **不要进行 node_type 归类**：输入中已明确标注为[18-Data Generation Algorithm]的算法节点，无需再次判断其是否属于[18-Data Generation Algorithm]，直接对它们进行类别归纳即可。
"""

    return f"""{header}

## 你的任务（核心）

请结合 PHM 领域通识，归纳**本数据集涉及的 [18-Data Generation Algorithm] 节点清单**。

本任务的核心是：对本数据集中已经明确属于[18-Data Generation Algorithm]的算法节点（详见**本数据集涉及的 [18-Data Generation Algorithm] 节点清单**），基于其技术原理和功能目的，归纳出它们各自隶属于哪个主流算法类别，生成"数据生成算法类别归纳表"。

{step1}
{step2}
{output_fmt}
{important_notes}

请开始输出：
"""


# --------------------------------------------------------------------------
# Type-19 node-specific prompt
# --------------------------------------------------------------------------

def build_prompt_type19(
    algo_node_info: list[dict],
    problem_names: list[str],
) -> str:
    """
    [19-Training Optimization Algorithm] (Training-Optimization Algorithm Class) specific prompt

    Core task: induce main categories of algorithm nodes under this type (e.g., transfer
    learning, meta-learning, multi-task learning) and produce the "Training-Optimization
    Algorithm Categories Induction Table".
    """
    type_name = "19-Training Optimization Algorithm"
    type_definition = (
        "论文用于优化模型参数或解决多任务/多目标问题的高级学习策略，是作者方法论层面的核心研究关注点。"
        "不包括：Adam/SGD/RMSprop等通用优化器、CrossEntropyLoss等通用损失函数、BatchNormalization等正则化技术。"
        "包括：迁移学习/域适应（预训练-微调、元学习MAML）、多任务学习（MTL、GradNorm）、"
        "损失函数设计（自定义复合损失）、课程学习/对抗训练、知识蒸馏（跨域迁移）、领域自适应（DANN/CDAN/CORAL）。"
    )

    if algo_node_info:
        node_lines = []
        for n in sorted(algo_node_info, key=lambda x: x["node_name"]):
            desc = n["node_description"].strip()
            if desc:
                node_lines.append(f"- **{n['node_name']}**：{desc}")
            else:
                node_lines.append(f"- **{n['node_name']}**")
        algo_names_str = "\n".join(node_lines)
    else:
        algo_names_str = "（本数据集中未出现该类型节点）"

    problem_names_str = "\n".join(f"- {n}" for n in sorted(set(problem_names))) if problem_names else "（无）"

    unique_names = sorted(set(n["node_name"] for n in algo_node_info if n["node_name"]))
    algo_names_mention = "、".join(f"`{n}`" for n in unique_names) if unique_names else "无"

    header = _build_header(type_name, problem_names_str, algo_names_str)

    target_block = f"> **{type_name}**：{type_definition}"

    step1 = _step1_block(type_name, algo_names_mention, target_block)
    step2 = _step2_block(type_name)
    output_fmt = _output_format_block(type_name)

    important_notes = """**重要提示：**
- **本任务的核心是类别归纳，而非节点归类**：你的任务是对**本数据集涉及的 [19-Training Optimization Algorithm] 节点清单**，归纳出它们各自隶属的主流算法类别（即对这些算法进行分类）。任务绝不是判断某个算法是否属于[19-Training Optimization Algorithm]——这一点在数据抽取阶段已经完成。
- **必须使用数据集**：你的归纳结果必须以 **本数据集涉及的 [19-Training Optimization Algorithm] 节点清单** 中的具体算法实例为核心依据，不可脱离该清单凭空归纳。若清单中某算法无法归入任何已归纳的类别，应将其单独说明。
- **仅输出上述标题和表格**，不要输出任何额外说明文字。
- 表格中每个单元格的文字应简洁、明确、专业，适合直接用于学术文档。
- 类别名称必须使用业内通用标准名称，不要包含具体算法实例的专有名称。
- 每个单元格内容如果较长可使用 `<br>` 换行，但不要使用表格以外的 Markdown 语法。
- **不要进行 node_type 归类**：输入中已明确标注为[19-Training Optimization Algorithm]的算法节点，无需再次判断其是否属于[19-Training Optimization Algorithm]，直接对它们进行类别归纳即可。
"""

    return f"""{header}

## 你的任务（核心）

请结合 PHM 领域通识，归纳**本数据集涉及的 [19-Training Optimization Algorithm] 节点清单**。

本任务的核心是：对本数据集中已经明确属于[19-Training Optimization Algorithm]的算法节点（详见**本数据集涉及的 [19-Training Optimization Algorithm] 节点清单**），基于其技术原理和功能目的，归纳出它们各自隶属于哪个主流算法类别，生成"训练优化算法类别归纳表"。

{step1}
{step2}
{output_fmt}
{important_notes}

请开始输出：
"""


# --------------------------------------------------------------------------
# Unified prompt-routing function (keeps backward compatibility)
# --------------------------------------------------------------------------

ALGO_TYPE_CONFIG = {
    "15": {"type_name": "15-Data Preprocessing Algorithm"},
    "16": {"type_name": "16-Feature Extraction Algorithm"},
    "17": {"type_name": "17-Core Classifier Algorithm"},
    "18": {"type_name": "18-Data Generation Algorithm"},
    "19": {"type_name": "19-Training Optimization Algorithm"},
}

PROMPT_BUILDERS = {
    "15": build_prompt_type15,
    "16": build_prompt_type16,
    "17": build_prompt_type17,
    "18": build_prompt_type18,
    "19": build_prompt_type19,
}


def build_prompt(
    algo_type_key: str,
    problem_node_names: list[str],
    algo_node_info: list[dict],
) -> str:
    """
    Backward-compatible interface: route to the corresponding algorithm-type-specific prompt.
    (Existing callers need no changes)
    """
    return PROMPT_BUILDERS[algo_type_key](algo_node_info, problem_node_names)


# ============================================================================
# Part 4: parallel task functions (prompt pre-generation -> manual review -> LLM call -> induction-table saving)
# ============================================================================

def generate_single_table(
    algo_type_key: str,
    problem_names: list[str],
    algo_node_info: list[dict],
    config: dict,
    key_manager: RoundRobinKeyManager,
    output_path: str,
) -> dict:
    """
    Generate one induction table for a single algorithm type.
    Executed in parallel in a thread pool, with API Keys assigned by key_manager.

    Flow:
      1. Dynamically assemble the prompt -> save to PROMPT_BASE_DIR / "{type_name}归纳提示词.md"
         (if the prompt file exists, skip generation and read the existing content)
      2. Read the prompt file -> pass it to the LLM
      3. LLM output -> save to OUTPUT_BASE_DIR (if the induction-table file exists, skip)

    Returns a result dict: {success, type_key, output_path, text, elapsed_s, error}
    """
    cfg = ALGO_TYPE_CONFIG[algo_type_key]
    type_name = cfg["type_name"]

    # Step A: generate and save (or read directly) the prompt file
    prompt_path = os.path.join(
        PROMPT_BASE_DIR,
        f"{type_name}归纳提示词.md",
    )

    if os.path.exists(prompt_path):
        print(f"  [Thread-{algo_type_key}] prompt file exists, reading directly: {os.path.basename(prompt_path)}")
        with open(prompt_path, "r", encoding="utf-8") as f:
            prompt = f.read()
    else:
        print(f"  [Thread-{algo_type_key}] generating prompt -> {os.path.basename(prompt_path)}")
        prompt = build_prompt(
            algo_type_key, problem_names, algo_node_info,
        )
        os.makedirs(PROMPT_BASE_DIR, exist_ok=True)
        with open(prompt_path, "w", encoding="utf-8") as f:
            f.write(prompt)
        print(f"  [Thread-{algo_type_key}] prompt saved. Please manually review before continuing with the LLM.")

    # Step B: LLM call (skip if the induction-table file already exists)
    if os.path.exists(output_path):
        return {
            "success": True,
            "type_key": algo_type_key,
            "type_name": type_name,
            "output_path": output_path,
            "text": None,
            "elapsed_s": 0.0,
            "error": "Induction-table file already exists; skipped",
        }

    print(f"  [Thread-{algo_type_key}] generating {type_name} induction table (prompt source: {os.path.basename(prompt_path)})...")
    t0 = time.time()

    try:
        result_text = call_llm_with_retry(prompt, config, key_manager)
        elapsed = time.time() - t0

        _save_markdown(result_text, output_path, type_name)
        print(f"  [Thread-{algo_type_key}] done: {os.path.basename(output_path)} "
              f"({len(result_text)} chars, {elapsed:.1f}s)")

        return {
            "success": True,
            "type_key": algo_type_key,
            "type_name": type_name,
            "output_path": output_path,
            "text": result_text,
            "elapsed_s": elapsed,
            "error": None,
        }

    except Exception as e:
        elapsed = time.time() - t0
        print(f"  [Thread-{algo_type_key}] failed: {type(e).__name__}: {e}")
        return {
            "success": False,
            "type_key": algo_type_key,
            "type_name": type_name,
            "output_path": output_path,
            "text": None,
            "elapsed_s": elapsed,
            "error": str(e),
        }


def _save_markdown(content: str, output_path: str, type_name: str) -> None:
    """Save the content returned by the LLM as a .md file."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    if not content.strip().startswith("#"):
        header = f"# {type_name} 主流算法类别归纳表\n\n"
    else:
        header = ""
    full_content = header + content.strip() + "\n"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_content)


def build_output_filename(input_path: str, suffix: str) -> str:
    """
    Dynamically generate the output filename based on the input filename.
    Example:
      Input:  "[C00168][C00174]合并节点_消歧.json"
      Output: "[C00168][C00174]合并节点_消歧_归纳_15节点大表.md"
    """
    basename = os.path.basename(input_path)
    name_without_ext = os.path.splitext(basename)[0]
    return f"{name_without_ext}_{suffix}.md"


# ============================================================================
# Part 5: main flow (parallel)
# ============================================================================

def extract_name_lists(data: list) -> tuple[list[str], dict[str, list[dict]]]:
    """
    Extract the problem-node inventory (names only) and the full information for nodes of
    each algorithm type from the JSON.
    Returns:
      - problem_names: list of problem-node names
      - algo_node_info: {type_key: [node_dict, ...]}
    """
    problem_names_raw = collect_node_info(data, ["09-Problem Scenario"])
    problem_names = [n["node_name"] for n in problem_names_raw]

    algo_node_info = {}
    for type_key in ALGO_TYPE_CONFIG:
        full_type_name = ALGO_TYPE_CONFIG[type_key]["type_name"]
        algo_node_info[type_key] = collect_node_info(data, [full_type_name])

    return problem_names, algo_node_info


def main():
    print("=" * 70)
    print("Algorithm-Category Induction-Table Generator V4")
    print("=" * 70)

    # Initialize the Key manager
    key_manager = get_key_manager()
    # Compute max concurrency: 10 Keys x PER_KEY_LIMIT (=3) = 30, leave 1 buffer -> 32
    actual_max_workers = min(MAX_WORKERS,
                             key_manager.total_keys * key_manager.per_key_limit + 2)
    print(f"\n[Config] API Key count: {key_manager.total_keys}, "
          f"per-Key concurrency limit: {key_manager.per_key_limit}, "
          f"theoretical max concurrency: {key_manager.total_keys * key_manager.per_key_limit}, "
          f"thread-pool workers: {actual_max_workers} (5 tables in parallel)")

    # Step 1: load data
    print(f"\n[Step1] reading input JSON: {INPUT_JSON_PATH}")
    if not os.path.exists(INPUT_JSON_PATH):
        raise FileNotFoundError(f"Input file does not exist: {INPUT_JSON_PATH}")

    data = load_json(INPUT_JSON_PATH)
    print(f"  -> loaded {len(data)} papers")

    # Step 2: extract node inventories
    print(f"\n[Step2] extracting node inventories...")
    problem_names, algo_node_info = extract_name_lists(data)

    print(f"  -> problem-node inventory (Type 09) total {len(set(problem_names))}: "
          f"{sorted(set(problem_names))}")
    for type_key, nodes in sorted(algo_node_info.items()):
        unique_names = sorted(set(n["node_name"] for n in nodes))
        print(f"  -> {ALGO_TYPE_CONFIG[type_key]['type_name']} total {len(unique_names)}: "
              f"{unique_names}")
        for n in nodes:
            desc = n["node_description"].strip()
            if desc:
                print(f"      [{n['node_id']}] {n['node_name']}: {desc[:60]}...")
            else:
                print(f"      [{n['node_id']}] {n['node_name']}")

    # Step 3: ensure the output directory exists
    print(f"\n[Step3] confirming output directory: {OUTPUT_BASE_DIR}")
    os.makedirs(OUTPUT_BASE_DIR, exist_ok=True)

    # Prepare the task list
    tasks = []
    for type_key in sorted(ALGO_TYPE_CONFIG.keys()):
        cfg = ALGO_TYPE_CONFIG[type_key]
        suffix = f"归纳_{type_key}节点大表"
        output_filename = build_output_filename(INPUT_JSON_PATH, suffix)
        output_path = os.path.join(OUTPUT_BASE_DIR, output_filename)
        tasks.append({
            "type_key": type_key,
            "output_path": output_path,
        })

    # Count already-skipped tasks
    skipped = [t for t in tasks if os.path.exists(t["output_path"])]
    to_run = [t for t in tasks if not os.path.exists(t["output_path"])]
    if skipped:
        print(f"\n[Step4] {len(skipped)} files already exist and will be skipped: "
              f"{[os.path.basename(t['output_path']) for t in skipped]}")
    print(f"\n[Step4] generating {len(to_run)} induction tables in parallel "
          f"(workers={actual_max_workers}, "
          f"{key_manager.total_keys} API Keys x "
          f"max {key_manager.per_key_limit} concurrent per Key)...")

    if not to_run:
        print("  All files exist; no tasks to run.")
    else:
        results = []
        t0_total = time.time()

        with ThreadPoolExecutor(max_workers=actual_max_workers) as executor:
            futures = {}
            for task in to_run:
                type_key = task["type_key"]
                future = executor.submit(
                    generate_single_table,
                    type_key,
                    problem_names,
                    algo_node_info[type_key],
                    {**LLM_CONFIG, "temperature": LLM_TEMPERATURE},
                    key_manager,
                    task["output_path"],
                )
                futures[future] = task

            for future in as_completed(futures):
                task = futures[future]
                try:
                    result = future.result()
                    results.append(result)
                except Exception as e:
                    results.append({
                        "success": False,
                        "type_key": task["type_key"],
                        "type_name": ALGO_TYPE_CONFIG[task["type_key"]]["type_name"],
                        "output_path": task["output_path"],
                        "error": str(e),
                        "elapsed_s": 0.0,
                    })

        total_elapsed = time.time() - t0_total
        success_count = sum(1 for r in results if r["success"] and r["elapsed_s"] > 0)
        skip_count = len(skipped)
        fail_count = sum(1 for r in results if not r["success"])

        print(f"\n{'=' * 70}")
        print(f"Results of this run ({len(to_run)} tasks, {total_elapsed:.1f}s):")
        for r in sorted(results, key=lambda x: x["type_key"]):
            status = "OK" if (r["success"] and r["elapsed_s"] > 0) else (
                "SKIP" if r.get("error") == "文件已存在，跳过" else "FAIL"
            )
            elapsed_str = f"{r['elapsed_s']:.1f}s" if r["elapsed_s"] > 0 else "-"
            print(f"  [{status}] {r['type_name']} ({elapsed_str})")
        if skip_count:
            print(f"  [SKIP] {skip_count} files already existed (LLM not re-requested)")
        print(f"  Key usage stats: {key_manager.usage_report()}")

    print(f"\n{'=' * 70}")
    print("All done!")
    print(f"Output directory: {OUTPUT_BASE_DIR}")
    print("=" * 70)


if __name__ == "__main__":
    main()
