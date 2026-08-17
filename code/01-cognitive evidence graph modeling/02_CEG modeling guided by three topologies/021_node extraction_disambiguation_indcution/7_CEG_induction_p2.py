# -*- coding: utf-8 -*-
"""
Algorithm Node Induction Mapping-Table Generator V9 (batch version)
========================================================================
Functions:
  1. Read the 5 algorithm-type induction tables (15-19 node tables.md)
  2. Read the consensus-graph JSON; separate algorithm-node arrays by node_type
  3. Merge-and-classify the 5 algorithm-node arrays (aggregate same node_name)
  4. Load preset judgment-prompt templates; dynamically inject the induction-table content
     and the merged graph-node arrays
  5. Parallel API-key calls to perform LLM classification/mapping on the 5 algorithm types
     (with exponential-backoff retries)
  6. Parse LLM output; build a three-level mapping: node_name -> node_induce -> node_ids
  7. Back-fill the mapping results into the induction-table structure and generate a
     "节点映射表.md" (Node Mapping Table) file

V9 (batch version) core improvements:
  - Batch processing: when the number of node_name groups > BATCH_SIZE(200), automatically
    split into multiple LLM calls
  - P0 compliance audit: after loading the graph, delete non-compliant nodes per three
    classes of criteria (see sanitize_graph_nodes)
  - P1 capacity: max_output_tokens=50000, BATCH_SIZE=200, reduce LLM omissions
  - P2 strict constraints: the prompt forbids the LLM from inventing / abbreviating
    category names; parser adds case/whitespace normalization
  - P3 structured report: key monitoring data is written to
    "映射表生成报告_时间戳.json" (Mapping-Table Generation Report_<timestamp>.json)

Dependencies:
  pip install google-genai
"""

import os
import re
import json
import time
from threading import Lock, Semaphore
from concurrent.futures import ThreadPoolExecutor, as_completed

# ============================================================================
# User configuration
# ============================================================================

# Input: consensus graph JSON
INPUT_JSON_PATH = r"./data/02_consensus_graph/[2277EAKD][ZZZRPFBV]合并节点_规范性审查_合并_规范性审查_消歧_规范性审查.json"

# Directory holding the induction tables (5 node-table .md files)
INDUCTION_TABLE_DIR = r"./data/03_induction/归纳清单表"

# Judgment-prompt template directory (5 judgment-prompt .md files)
PROMPT_TEMPLATE_DIR = r"./data/03_induction/归纳映射提示词"

# Output directory
OUTPUT_DIR = INDUCTION_TABLE_DIR

# LLM configuration
LLM_CONFIG = {
    "provider": "gemini",
    "model": "gemini-3.5-flash",
    "base_url": os.environ.get("BFGA_LLM_API_URL", "https://YOUR.LLM.ENDPOINT/"),
    "timeout": 300,
}

# 5 API Keys (each key dedicated to one node_type)
# IMPORTANT: Provide your own API keys before running. The list below should be filled with valid keys.
MULTI_API_KEYS = []

# Concurrency control
PER_KEY_CONCURRENCY = 1  # each key is dedicated to one node_type; concurrency of 1 is sufficient

# Retry configuration
MAX_RETRIES = 5
INITIAL_BACKOFF = 1.0
MAX_BACKOFF = 60.0

LLM_TEMPERATURE = 0.0

# Maximum number of node_names per batch (split into multiple LLM calls if exceeded)
BATCH_SIZE = 120


# ============================================================================
# Algorithm-type configuration
# ============================================================================

ALGO_TYPE_CONFIG = {
    "15": {
        "type_name": "15-Data Preprocessing Algorithm",
        "type_key": "15",
        "induction_table_suffix": "归纳_15节点大表",
        "mapping_table_suffix": "归纳_15节点映射表",
        "prompt_template_name": "15判定提示词.md",
    },
    "16": {
        "type_name": "16-Feature Extraction Algorithm",
        "type_key": "16",
        "induction_table_suffix": "归纳_16节点大表",
        "mapping_table_suffix": "归纳_16节点映射表",
        "prompt_template_name": "16判定提示词.md",
    },
    "17": {
        "type_name": "17-Core Classifier Algorithm",
        "type_key": "17",
        "induction_table_suffix": "归纳_17节点大表",
        "mapping_table_suffix": "归纳_17节点映射表",
        "prompt_template_name": "17判定提示词.md",
    },
    "18": {
        "type_name": "18-Data Generation Algorithm",
        "type_key": "18",
        "induction_table_suffix": "归纳_18节点大表",
        "mapping_table_suffix": "归纳_18节点映射表",
        "prompt_template_name": "18判定提示词.md",
    },
    "19": {
        "type_name": "19-Training Optimization Algorithm",
        "type_key": "19",
        "induction_table_suffix": "归纳_19节点大表",
        "mapping_table_suffix": "归纳_19节点映射表",
        "prompt_template_name": "19判定提示词.md",
    },
}


# ============================================================================
# Part 1: file-path and basic utilities
# ============================================================================

def load_json(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def save_text(content: str, path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


# ============================================================================
# Part 2: consensus-graph parsing -> split 5 algorithm-type node arrays
# ============================================================================

def extract_graph_array_by_type(data: list, node_type: str) -> list[dict]:
    """
    Extract all nodes of the specified node_type from papers data.
    Returns a node list; each node contains node_id, node_name, node_original_name,
    node_description.
    """
    result = []
    for paper in data:
        for node in paper.get("nodes", []):
            if node.get("node_type") == node_type:
                nid = node.get("node_id", "")
                name = node.get("node_name", "") or ""
                orig_name = node.get("node_original_name", "") or ""
                desc = node.get("node_description", "") or ""
                result.append({
                    "node_id": nid,
                    "node_name": name.strip() if name else "",
                    "node_original_name": orig_name.strip() if orig_name else "",
                    "node_description": desc.strip(),
                })
    return result


# ============================================================================
# Part 2.5: P0 - Graph compliance audit (audit criteria see user rules)
# ============================================================================

def sanitize_graph_nodes(papers: list[dict]) -> tuple[list[dict], dict]:
    """
    Perform a compliance audit on the graph JSON; delete three classes of illegal nodes:

    Audit criteria (three cases where node_name is null):
      1. "node_original_name": "Not Mentioned" AND "node_name": null  -> delete that node
      2. "node_original_name": ""        AND "node_name": ""    -> delete that node
      3. "node_original_name": null       AND "node_name": null  -> delete that node

    Note: nodes with node_name=null but node_original_name carrying actual value (e.g., "CNN")
          are omissions from upstream disambiguation; they are kept and counted (not deleted
          in this function).
    """
    stats = {
        "papers_before": len(papers),
        "nodes_before": 0,
        "nodes_after": 0,
        "type1_removed": 0,   # node_original_name="Not Mentioned" AND node_name=null
        "type2_removed": 0,   # node_original_name=""        AND node_name=""
        "type3_removed": 0,   # node_original_name=null      AND node_name=null
        "type_detail": {},    # counts per node_type
    }

    def _is_illegal(node: dict) -> tuple[bool, int]:
        """Return (whether illegal, illegal-type code 1-3)."""
        orig = node.get("node_original_name")
        name = node.get("node_name")
        orig_str = _normalize_original_name(orig) if orig else ""

        # Type 1: node_original_name is "Not Mentioned", and node_name is null/empty
        if orig_str == "Not Mentioned" and not name:
            return True, 1
        # Type 2: node_original_name is empty string, and node_name is also empty
        if orig == "" and name == "":
            return True, 2
        # Type 3: both are None/null
        if orig is None and name is None:
            return True, 3
        return False, 0

    new_papers = []
    for paper in papers:
        new_nodes = []
        for node in paper.get("nodes", []):
            stats["nodes_before"] += 1
            illegal, typ = _is_illegal(node)
            if illegal:
                stats[f"type{typ}_removed"] += 1
                nt = node.get("node_type", "unknown")
                stats["type_detail"][nt] = stats["type_detail"].get(nt, 0) + 1
            else:
                new_nodes.append(node)
                stats["nodes_after"] += 1
        new_papers.append({**paper, "nodes": new_nodes})

    return new_papers, stats


def _print_sanitize_report(stats: dict) -> None:
    """Print the compliance-audit summary report."""
    print(f"\n  [P0-SANITIZE] ========== Graph Compliance Audit Report ==========")
    print(f"  [P0-SANITIZE] Papers: {stats['papers_before']}")
    print(f"  [P0-SANITIZE] Nodes: {stats['nodes_before']} -> {stats['nodes_after']}"
          f" (deleted {stats['nodes_before'] - stats['nodes_after']})")
    print(f"  [P0-SANITIZE] Deleted type-1 (node_original_name='Not Mentioned' AND node_name=null): "
          f"{stats['type1_removed']}")
    print(f"  [P0-SANITIZE] Deleted type-2 (node_original_name='' AND node_name=''): "
          f"{stats['type2_removed']}")
    print(f"  [P0-SANITIZE] Deleted type-3 (node_original_name=null AND node_name=null): "
          f"{stats['type3_removed']}")
    if stats["type_detail"]:
        for nt, cnt in sorted(stats["type_detail"].items()):
            print(f"  [P0-SANITIZE]   |_ {nt}: deleted {cnt}")
    print(f"  [P0-SANITIZE] =========================================\n")


# ============================================================================
# Part 3: node-array merge-and-group
# ============================================================================

def merge_graph_array(raw_nodes: list[dict]) -> list[dict]:
    """
    Merge and group the raw node array by node_name.
    Each node_name becomes one group, collecting all its node_id, node_original_name,
    and node_description (top 10).
    Note: nodes with node_name="" are also kept as a single group (key="") for
    upstream issue detection.

    Input:  raw_nodes = [{node_id, node_name, node_original_name, node_description}, ...]
    Output: node_group = [
        {
            'node_name': <name>,
            'node_ids': [id1, id2, ...],
            'node_original_names': [orig1, orig2, ...],   # keep original names
            'node_description_top10': [desc1, desc2, ..., desc10]
        },
        ...
    ]
    """
    groups: dict[str, dict] = {}
    for node in raw_nodes:
        name = node["node_name"]
        nid = node["node_id"]
        orig_name = node.get("node_original_name", "") or ""
        desc = node["node_description"]

        if name not in groups:
            groups[name] = {
                "node_name": name,
                "node_ids": [],
                "node_original_names": [],
                "node_description_top10": [],
            }
        groups[name]["node_ids"].append(nid)
        if orig_name and orig_name not in groups[name]["node_original_names"]:
            groups[name]["node_original_names"].append(orig_name)
        if desc and desc not in groups[name]["node_description_top10"]:
            groups[name]["node_description_top10"].append(desc)

    # Each node_description_top10 keeps only the first 10
    for name in groups:
        groups[name]["node_description_top10"] = groups[name]["node_description_top10"][:10]

    return list(groups.values())


def _normalize_original_name(s: str) -> str:
    """
    Normalize node_original_name, handling encoding issues.
    'δ�ἰ' (mojibake) is the GBK->UTF8 garbled form of 'Not Mentioned';
    they all normalize to the standard 'Not Mentioned'.
    """
    if not s:
        return ""
    # Detect garbled forms
    if "δ" in s or "�" in s or "ἰ" in s:
        return "Not Mentioned"
    return s


# ============================================================================
# Part 4: parse induction-table Markdown -> structured records
# ============================================================================

def _strip_html_tags(text: str) -> str:
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def _parse_table_format(md_content: str) -> list[dict]:
    """Parse standard Markdown-table format."""
    records = []
    rows = re.findall(
        r'^\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|',
        md_content,
        re.MULTILINE | re.DOTALL,
    )
    for row in rows:
        seq, type_name, connotation, standard, applicability = row
        records.append({
            "seq": seq.strip(),
            "type_name": _strip_html_tags(type_name.strip()),
            "connotation": _strip_html_tags(connotation.strip()),
            "standard": _strip_html_tags(standard.strip()),
            "applicability": _strip_html_tags(applicability.strip()),
        })
    return records


def _parse_narrative_format(md_content: str, type_key: str) -> list[dict]:
    """
    Parse narrative format (LLM-generated Markdown list/paragraph format).

    Strategy 1: parse from detailed blocks (the "细化" subsection with four content pieces),
    supporting 1-3 levels of * nesting/indentation.
    Strategy 2: supplement missing categories from the top-level numbered list (e.g.,
    type-16's table has 1-4 detailed blocks but the top list contains 1-7 categories).
    """
    records: list[dict] = []
    md_content = re.sub(r'^\s*#.*$', '', md_content, flags=re.MULTILINE)

    # ---- Strategy 1: detailed blocks (1-3 * indentation + "细化" subsection) ----
    block_pattern = (
        r'(?:^|\n)\s*\*[\s\*]*类别\s*(\d+)\s*[：:]\s*(.+?)\n'
        r'(.*?)'
        r'(?=(?:^|\n)\s*\*[\s\*]*类别\s*\d+\s*[：:]|\Z)'
    )
    for m in re.finditer(block_pattern, md_content, re.DOTALL | re.IGNORECASE):
        seq = m.group(1).strip()
        type_name = _strip_html_tags(m.group(2).strip())
        block = m.group(3)
        if not type_name:
            continue

        def ef(txt: str, pat: str) -> str:
            xm = re.search(pat, txt, re.DOTALL | re.IGNORECASE)
            return _strip_html_tags(xm.group(1).strip()) if xm else ""

        connotation = ef(block,
            r'(?:^|\n)\s*\*+\s*(?:内涵|核心原理)[：:]\s*(.+?)(?=(?:^|\n)\s*\*+\s*(?:归纳标准|适用性分析)|$)')
        standard = ef(block,
            r'(?:^|\n)\s*\*+\s*归纳标准[：:]\s*(.+?)(?=(?:^|\n)\s*\*+\s*(?:适用性分析|局限性)|$)')
        applicability = ef(block,
            r'(?:^|\n)\s*\*+\s*适用性[：:]\s*(.+?)(?=(?:^|\n)\s*\*+\s*(?:局限性|代表算法)|$)')

        records.append({
            "seq": seq,
            "type_name": type_name,
            "connotation": connotation,
            "standard": standard,
            "applicability": applicability,
        })

    # ---- Strategy 2: supplement categories from the top list (for missing categories 5-7) ----
    top_pattern = (
        r'(?:^|\n)\s*(?:[-*]\s+)?\s*(\d+)\.\s+\*\*(.+?)\*\*'
        r'(?=\s*[(（]|[^\s*]|$)'
    )
    existing_seqs = {r["seq"] for r in records}
    for m in re.finditer(top_pattern, md_content, re.MULTILINE):
        seq = m.group(1).strip()
        name = _strip_html_tags(m.group(2).strip())
        if name and len(name) >= 4 and "细化" not in name and "提炼" not in name:
            if seq not in existing_seqs:
                records.append({
                    "seq": seq,
                    "type_name": name,
                    "connotation": "",
                    "standard": "",
                    "applicability": "",
                })
                existing_seqs.add(seq)

    # Deduplicate and sort by sequence number
    seen: set[str] = set()
    unique: list[dict] = []
    for r in records:
        if r["seq"] not in seen:
            seen.add(r["seq"])
            unique.append(r)
    unique.sort(key=lambda x: int(x["seq"]))
    return unique


def parse_induction_table(md_content: str, type_key: str = "") -> list[dict]:
    """
    Parse the induction-table Markdown; return a list of structured records.
    Auto-detects two formats:
      1. Standard Markdown-table format
      2. Narrative/list format (LLM-generated Markdown paragraphs)
    Each record contains: seq, type_name, connotation, standard, applicability.
    """
    records = _parse_table_format(md_content)
    if records:
        return records

    records = _parse_narrative_format(md_content, type_key)
    if records:
        return records

    return []


# ============================================================================
# Part 5: load judgment-prompt templates and dynamically inject
# ============================================================================

def load_prompt_template(template_name: str) -> str:
    """Load a preset judgment-prompt template file."""
    template_path = os.path.join(PROMPT_TEMPLATE_DIR, template_name)
    if not os.path.exists(template_path):
        raise FileNotFoundError(
            f"Judgment-prompt template not found: {template_path}\n"
            f"Please create this file first. Prompt-template directory: {PROMPT_TEMPLATE_DIR}"
        )
    return read_text(template_path)


def build_llm_input(
    template: str,
    induction_table_md: str,
    merged_graph_array: list[dict],
    batch_no: int = 1,
    total_batches: int = 1,
) -> str:
    """
    Replace placeholders in the prompt template with actual content:
      {INDUCTION_TABLE}     -> induction-table Markdown content
      {MERGED_GRAPH_ARRAY}  -> merged-graph array (JSON string)
    When total_batches > 1, prepend a batch-description line before the array.
    """
    # Build batch-description header (only meaningful for multi-batch)
    batch_header = ""
    if total_batches > 1:
        batch_header = (
            f"【重要提示】本次共需处理 {total_batches} 个批次（每 {BATCH_SIZE} 个 node_name 为一批），"
            f"当前为第 {batch_no} / {total_batches} 批次。"
            f"请仅对以下 {len(merged_graph_array)} 个 node_name 进行归类，不要处理其他批次的节点。\n\n"
        )

    # Serialize the merged graph-array as a formatted JSON string
    graph_array_json = json.dumps(merged_graph_array, ensure_ascii=False, indent=2)

    prompt = template
    # Note: in the f-string {{INDUCTION_TABLE}} renders to {INDUCTION_TABLE} (single braces)
    prompt = prompt.replace("{INDUCTION_TABLE}", induction_table_md)
    prompt = prompt.replace(
        "{MERGED_GRAPH_ARRAY}",
        batch_header + graph_array_json,
    )
    return prompt


# ============================================================================
# Part 6: LLM invocation (shared Key pool with concurrency control and exponential backoff)
# ============================================================================

class SharedKeyManager:
    """
    Shared Key manager:
    All Keys form a shared pool; each Key has an independent semaphore for concurrency.
    Auto-degrades the concurrency cap on network failures; thread-safe.
    """

    DEFAULT_CONCURRENCY = 3
    FALLBACK_CONCURRENCY = 1

    def __init__(self, keys: list[str]):
        self._keys = keys
        self._lock = Lock()
        self._sems = [Semaphore(self.DEFAULT_CONCURRENCY) for _ in keys]
        self._idx = 0
        self._failed: set[int] = set()

    def acquire(self) -> tuple[str, int]:
        with self._lock:
            for _ in range(len(self._keys)):
                idx = self._idx % len(self._keys)
                self._idx += 1
                if self._sems[idx].acquire(blocking=False):
                    return self._keys[idx], idx
            idx = (self._idx - 1) % len(self._keys)
        self._sems[idx].acquire()
        return self._keys[idx], idx

    def release(self, key_idx: int):
        self._sems[key_idx].release()

    def on_error(self, key_idx: int):
        with self._lock:
            self._failed.add(key_idx)
            self._sems = [Semaphore(self.FALLBACK_CONCURRENCY) for _ in self._keys]

    def on_success(self, key_idx: int):
        with self._lock:
            if key_idx in self._failed and len(self._failed) == len(self._keys):
                self._sems = [Semaphore(self.DEFAULT_CONCURRENCY) for _ in self._keys]
                self._failed.clear()

    @property
    def total_keys(self) -> int:
        return len(self._keys)

    def usage_report(self) -> dict:
        return {"manager": "shared_pool"}


def _call_gemini(prompt: str, config: dict, api_key: str) -> dict:
    """Single Gemini API call."""
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

    http_opts = HttpOptions(base_url=base, timeout=timeout_ms, headers=extra_headers or None)
    client = genai.Client(api_key=api_key, http_options=http_opts)
    model_name = config.get("model", "gemini-3.5-flash")
    response = client.models.generate_content(
        model=model_name,
        contents=[prompt],
        config={"temperature": config.get("temperature", LLM_TEMPERATURE),
                "max_output_tokens": 50000},
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
        text = response.text if response.text else ""

    return {
        "text": text or "",
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": total_tokens,
    }


def call_llm_with_retry(
    prompt: str,
    config: dict,
    key_manager: SharedKeyManager,
    type_name: str,
    max_retries: int = MAX_RETRIES,
    initial_backoff: float = INITIAL_BACKOFF,
    max_backoff: float = MAX_BACKOFF,
) -> str:
    """
    LLM call with exponential-backoff retries.
    Acquires an available Key from SharedKeyManager; on failure switches Key and
    applies exponential backoff. Raises RuntimeError when all Keys have failed.
    """
    attempt = 0
    backoff = initial_backoff
    while True:
        api_key, key_idx = key_manager.acquire()
        try:
            result = _call_gemini(prompt, config, api_key)
            err = result.get("error", "") or ""
            if "401" in str(err) or "unauthorized" in str(err).lower():
                key_manager.on_error(key_idx)
                if attempt >= max_retries:
                    raise RuntimeError(f"Invalid API Key (401): {api_key[:12]}...")
                time.sleep(backoff)
                backoff = min(backoff * 2, max_backoff)
                attempt += 1
                continue
            if not result["text"]:
                if attempt >= max_retries:
                    raise RuntimeError(f"[{type_name}] LLM returned empty content (max retries {max_retries} reached)")
                print(f"      [{type_name}] LLM returned empty; exponential backoff {backoff:.1f}s then retry...")
                time.sleep(backoff)
                backoff = min(backoff * 2, max_backoff)
                attempt += 1
                continue
            key_manager.on_success(key_idx)
            return result["text"]
        except Exception as e:
            key_manager.on_error(key_idx)
            err_msg = str(e).lower()
            if any(kw in err_msg for kw in [
                "quota", "rate", "limit", "429",
                "resource_exhausted", "internal error",
                "timeout", "connection", "timed out",
                "invalid token", "unauthorized", "401",
            ]):
                if attempt >= max_retries:
                    raise RuntimeError(
                        f"[{type_name}] all API Keys failed (max retries {max_retries} reached), "
                        f"last error: {e}"
                    )
                print(f"      [{type_name}] request failed ({type(e).__name__}): {e}, "
                      f"exponential backoff {backoff:.1f}s then retry...")
                time.sleep(backoff)
                backoff = min(backoff * 2, max_backoff)
                attempt += 1
                continue
            else:
                raise
        finally:
            key_manager.release(key_idx)


# ============================================================================
# Part 7: parse LLM output -> node_name -> node_induce mapping
# ============================================================================

def parse_llm_output(llm_output: str, type_key: str) -> list[dict]:
    """
    Parse structured content returned by the LLM; supports multiple formats.

    Supported formats:
      1. Plain JSON: {"node_type":"...","node_group":[{"node_name":"...","node_induce":"..."}]}
      2. JSON in Markdown: ```json ... ```
      3. Markdown list: * **node_name** -> **category**
      4. Table row: | node_name | category |
      5. List paragraph: * **node_name** ... category: Category / belongs-to "Category"

    Returns: [{node_name, node_induce}, ...]
    """
    text = llm_output.strip()

    if not text:
        raise ValueError(f"[{type_key}] LLM returned empty content")

    # --- Attempt 1: standard JSON code block ---
    def _norm(s: str) -> str:
        s = s.lower()
        s = s.translate(str.maketrans(
            'ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ',
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        s = s.translate(str.maketrans(
            'ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ',
            'abcdefghijklmnopqrstuvwxyz'))
        s = s.translate(str.maketrans('（）【】', '()[]'))
        s = re.sub(r'[\s\u00a0\u3000]+', ' ', s)
        return s.strip()

    code_block_match = re.search(
        r'```(?:\w+)?\s*(\{.*?\})\s*```',
        text,
        re.DOTALL
    )
    if code_block_match:
        try:
            parsed = json.loads(code_block_match.group(1))
            node_groups = parsed.get("node_group", [])
            return [
                {"node_name": g["node_name"], "node_induce": g["node_induce"]}
                for g in node_groups
                if "node_name" in g and "node_induce" in g
            ]
        except (json.JSONDecodeError, TypeError):
            pass

    # --- Attempt 2: bare JSON (no wrapper); robust parse: truncate char-by-char to find valid JSON ---
    json_start = text.find('{')
    json_end = text.rfind('}')
    if json_start != -1 and json_end != -1 and json_end > json_start:
        raw = text[json_start:json_end + 1]
        for end_offset in range(len(raw), 0, -1):
            candidate = raw[:end_offset]
            try:
                parsed = json.loads(candidate)
                node_groups = parsed.get("node_group", [])
                if node_groups:
                    return [
                        {"node_name": g["node_name"], "node_induce": g["node_induce"]}
                        for g in node_groups
                        if "node_name" in g and "node_induce" in g
                    ]
            except json.JSONDecodeError:
                continue
        pairs = _extract_pairs_from_text(text)
        if pairs:
            return pairs

    # --- Fallback: directly regex-extract all node_name / node_induce pairs from raw text ---
    pairs = _extract_pairs_from_text(text)
    if pairs:
        return pairs

    raise ValueError(
        f"[{type_key}] cannot parse LLM output into a known format. "
        f"First 300 chars of content: {text[:300]}"
    )


def _extract_pairs_from_text(text: str) -> list[dict]:
    """
    Extract node_name -> node_induce pairs from LLM output text in any format.
    Supports: JSON arrays, Markdown bold + arrow, Markdown bold + quotes, narrative, etc.

    P2 enhancement: normalize all extracted node_induce values via case/whitespace
    folding to eliminate subtle formatting differences between LLM output and the
    induction table (initial capital, full-width vs half-width, etc.).
    """

    def _norm(s: str) -> str:
        """Case + whitespace normalization: lowercase, full-width -> half-width, fold whitespace."""
        s = s.lower()
        # Full-width English letters / symbols -> half-width
        s = s.translate(str.maketrans(
            'ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ',
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        s = s.translate(str.maketrans(
            'ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ',
            'abcdefghijklmnopqrstuvwxyz'))
        s = s.translate(str.maketrans('（）【】', '()[]'))
        # Fold whitespace (space, tab, NBSP, etc.)
        s = re.sub(r'[\s\u00a0\u3000]+', ' ', s)
        return s.strip()

    pairs = []
    seen_names: set[str] = set()
    seen_norm_induce: dict[str, str] = {}   # norm_induce -> original_induce (keep the first verbatim)

    # --- Strategy A: directly find {"node_name":..., "node_induce":...} objects in JSON arrays ---
    for m in re.finditer(
        r'"node_name"\s*:\s*"([^"]+)"[^}]*?"node_induce"\s*:\s*"([^"]+)"',
        text
    ):
        name = m.group(1).strip()
        induce = m.group(2).strip()
        induce_norm = _norm(induce)
        if name and induce_norm and name not in seen_names:
            seen_names.add(name)
            # Keep the original induce spelling (for debugging); use norm_induce as the mapping key
            pairs.append({"node_name": name, "node_induce": induce,
                           "_node_induce_norm": induce_norm})

    if pairs:
        return pairs

    # --- Strategy B: Markdown bold pair node_name -> node_induce ---
    arrow_pattern = re.compile(
        r'\*\*(.+?)\*\*\s*[-–—>→:：]\s*\*\*(.+?)\*\*',
        re.IGNORECASE
    )
    for m in arrow_pattern.finditer(text):
        name, induce = m.group(1).strip(), m.group(2).strip()
        induce_norm = _norm(induce)
        if name and induce_norm and name not in seen_names:
            seen_names.add(name)
            pairs.append({"node_name": name, "node_induce": induce,
                           "_node_induce_norm": induce_norm})

    if pairs:
        return pairs

    # --- Strategy C: node_name followed by Chinese "属于/归入/归为" quoted category ---
    belong_pattern = re.compile(
        r'\*\*(.+?)\*\*(?:[^"]*"([^"]+)"[^"]*["""]([^"""{}]+)["""]|'
        r'[^"""{}]*["""]([^"""{}]+)["""])',
        re.DOTALL
    )
    for m in belong_pattern.finditer(text):
        name = m.group(1).strip()
        induce = (m.group(2) or m.group(3) or m.group(4) or "").strip()
        induce_norm = _norm(induce)
        if name and induce_norm and name not in seen_names:
            seen_names.add(name)
            pairs.append({"node_name": name, "node_induce": induce,
                           "_node_induce_norm": induce_norm})

    if pairs:
        return pairs

    # --- Strategy D: line-by-line scan, bold word at line start is node_name, next line has quoted category ---
    lines = text.split('\n')
    pending_name = None
    for line in lines:
        bold_match = re.search(r'\*\*(.+?)\*\*', line)
        if bold_match:
            name_candidate = bold_match.group(1).strip()
            if len(name_candidate) < 60 and '属于' not in name_candidate:
                pending_name = name_candidate
        if pending_name:
            quote_match = re.search(r'["""]([^"""{}]{2,})["""]', line)
            if quote_match:
                induce = quote_match.group(1).strip()
                induce_norm = _norm(induce)
                if induce_norm and pending_name not in seen_names:
                    seen_names.add(pending_name)
                    pairs.append({"node_name": pending_name, "node_induce": induce,
                                   "_node_induce_norm": induce_norm})
                pending_name = None

    if pairs:
        return pairs

    # --- Strategy E: table row | node_name | Category | ---
    for m in re.finditer(r'\|\s*([^|]{2,60}?)\s*\|\s*([^|<]{2,60}?)\s*\|', text):
        name, induce = m.group(1).strip(), m.group(2).strip()
        induce_norm = _norm(induce)
        if name and induce_norm and name not in seen_names and induce_norm not in seen_norm_induce:
            seen_names.add(name)
            seen_norm_induce[induce_norm] = induce
            pairs.append({"node_name": name, "node_induce": induce,
                           "_node_induce_norm": induce_norm})

    if pairs:
        return pairs

    # --- Strategy F: narrative blocks (used when the LLM outputs an analysis report) ---
    narrative_patterns = [
        re.compile(
            r'`([^`]+?)`[^\n]*?\*[\s*]*归类[：:]\s*[`"\']*([^\n`"\'{}]{3,60}?)[`"\']*\s*(?:\n|$)',
            re.DOTALL
        ),
        re.compile(
            r'`([^`]+?)`[^\n]*?(?:属于|归入|归为)[^\n]*?[`"\']*([^\n`"\'{}]{3,60}?)[`"\']*\s*(?:\n|$)',
            re.DOTALL
        ),
        re.compile(
            r'\*\*(.+?)\*\*[^\n]*?\*[\s*]*归类[：:]\s*[`"\']*([^\n`"\'{}]{3,60}?)[`"\']*\s*(?:\n|$)',
            re.DOTALL
        ),
        re.compile(
            r'\*\*(.+?)\*\*[^\n:]*?：[^\n]*?["""]([^"""{}]{3,60}?)["""]',
            re.DOTALL
        ),
    ]
    for pat in narrative_patterns:
        for m in pat.finditer(text):
            name = m.group(1).strip()
            induce = m.group(2).strip()
            induce_norm = _norm(induce)
            if (name and induce_norm and len(name) >= 2 and len(induce_norm) >= 3
                    and name not in seen_names
                    and not induce.startswith("属于")
                    and not induce.startswith("归入")
                    and "分析" not in induce
                    and "描述" not in induce):
                seen_names.add(name)
                pairs.append({"node_name": name, "node_induce": induce,
                               "_node_induce_norm": induce_norm})

    if pairs:
        return pairs

    # --- Strategy G: extract all backtick-wrapped node_names, paired with subsequent quoted category ---
    code_name_pattern = re.compile(r'`([^`\n]{2,40}?)`')
    pending_code_name = None
    for m in code_name_pattern.finditer(text):
        name_candidate = m.group(1).strip()
        if (len(name_candidate) >= 2
                and '分析' not in name_candidate
                and '属于' not in name_candidate
                and '归类' not in name_candidate
                and '描述' not in name_candidate):
            pending_code_name = name_candidate
        elif pending_code_name:
            quote_m = re.search(r'["""]([^"""{}]{3,60}?)["""]', m.group(0))
            if quote_m:
                induce = quote_m.group(1).strip()
                induce_norm = _norm(induce)
                if induce_norm and pending_code_name not in seen_names:
                    seen_names.add(pending_code_name)
                    pairs.append({"node_name": pending_code_name, "node_induce": induce,
                                   "_node_induce_norm": induce_norm})
            pending_code_name = None

    if pairs:
        return pairs

    # --- Strategy H: backtick-wrapped `node_name` -> `Category` format ---
    backtick_arrow = re.compile(
        r'^[>\s]*[-*]?\s*`([^`]+?)`\s*[-–—>→:：]\s*`([^`]+?)`$',
        re.MULTILINE
    )
    for m in backtick_arrow.finditer(text):
        name = m.group(1).strip()
        induce = m.group(2).strip()
        induce_norm = _norm(induce)
        if name and induce_norm and name not in seen_names:
            seen_names.add(name)
            pairs.append({"node_name": name, "node_induce": induce,
                           "_node_induce_norm": induce_norm})

    if pairs:
        return pairs

    # --- Strategy I: backtick-wrapped node_name, next line has backtick-wrapped category ---
    lines = text.split('\n')
    pending_code_name = None
    for line in lines:
        line_stripped = line.strip()
        code_m = re.search(r'^[-*>\s]*`([^`\n]{2,50}?)`$', line_stripped)
        if code_m:
            candidate = code_m.group(1).strip()
            if (candidate and len(candidate) >= 2
                    and '属于' not in candidate
                    and '归类' not in candidate
                    and '分析' not in candidate
                    and '描述' not in candidate
                    and candidate not in seen_names):
                pending_code_name = candidate
        elif pending_code_name:
            next_code_m = re.search(r'`([^`\n]{3,50}?)`', line_stripped)
            if next_code_m:
                induce = next_code_m.group(1).strip()
                induce_norm = _norm(induce)
                if (induce_norm and '属于' not in induce
                        and '归类' not in induce
                        and '分析' not in induce):
                    seen_names.add(pending_code_name)
                    pairs.append({"node_name": pending_code_name, "node_induce": induce,
                                   "_node_induce_norm": induce_norm})
            pending_code_name = None

    return pairs


def _md_cell(s: str) -> str:
    return s.replace("\n", "<br>")


def generate_mapping_md(
    type_key: str,
    induction_records: list[dict],
    induce_mapping: dict[str, dict],
) -> str:
    """
    Fill the classification results into the induction-table structure; generate the
    node mapping-table Markdown.

    Header: seq | category name | category connotation | induction standard |
            applicability analysis | node_names | node_ids
    """
    cfg = ALGO_TYPE_CONFIG[type_key]
    type_name = cfg["type_name"]

    lines = []
    lines.append(f"### {type_name} 主流算法类别映射表\n")
    lines.append("| 序号 | 类别名称 | 类别内涵 | 归纳标准 | 适用性分析 | node_names | node_ids |")
    lines.append("|------|---------|---------|---------|-----------|-----------|----------|")

    for rec in induction_records:
        seq = rec["seq"]
        cat_name = rec["type_name"]
        cat_connotation = rec["connotation"]
        cat_standard = rec["standard"]
        cat_applicability = rec["applicability"]

        mapping = induce_mapping.get(cat_name)
        if mapping:
            node_names_str = ", ".join(mapping["node_names"])
            node_ids_str = ", ".join(mapping["node_ids"])
        else:
            node_names_str = "（无）"
            node_ids_str = "（无）"

        lines.append(
            f"| {seq} | {_md_cell(cat_name)} | {_md_cell(cat_connotation)} | "
            f"{_md_cell(cat_standard)} | {_md_cell(cat_applicability)} | "
            f"{node_names_str} | {node_ids_str} |"
        )

    return "\n".join(lines) + "\n"


# ============================================================================
# Part 9: parallel task function (called by ThreadPoolExecutor)
# ============================================================================

def _filter_and_classify_nodes(
    nodes: list[dict],
) -> tuple[list[dict], list[dict], list[dict]]:
    """
    Filter and classify nodes; returns three lists:
      - valid: node_name has a value; passed to LLM for classification
      - filtered: node_name is empty, and (node_original_name='Not Mentioned' or empty),
                  silently filtered
      - upstream_issue: node_name is empty, but node_original_name is non-empty and
                        not 'Not Mentioned'; console warning
    """
    valid = []
    filtered = []
    upstream_issue = []
    for g in nodes:
        name = g.get("node_name", "") or ""
        if name and name.strip():
            valid.append(g)
        else:
            orig = _normalize_original_name(
                (g.get("node_original_names") or [None])[0] or ""
            )
            # node_original_name empty -> silently filter (not mentioned and no original name)
            if orig == "Not Mentioned" or orig == "":
                filtered.append(g)
            else:
                # node_original_name non-empty and not 'Not Mentioned' -> upstream issue, warn
                upstream_issue.append(g)
    return valid, filtered, upstream_issue


def process_single_type(
    type_key: str,
    merged_graph_array: list[dict],
    induction_table_md: str,
    induction_records: list[dict],
    config: dict,
    key_manager: SharedKeyManager,
    output_path: str,
) -> dict:
    """
    Complete flow for a single algorithm type:
      1. Load the prompt template
      2. Filter nodes (valid / filtered / upstream_issue)
      3. Call LLM in batches (at most BATCH_SIZE node_names per batch)
      4. Merge LLM outputs across all batches
      5. Build the three-level mapping
      6. Generate and save the mapping-table Markdown

    Executed in parallel within a thread pool.
    """
    cfg = ALGO_TYPE_CONFIG[type_key]
    type_name = cfg["type_name"]

    if os.path.exists(output_path):
        return {
            "success": True,
            "type_key": type_key,
            "type_name": type_name,
            "output_path": output_path,
            "elapsed_s": 0.0,
            "error": "File already exists; skipped",
        }

    print(f"  [Thread-{type_key}] processing {type_name}...")
    t0 = time.time()

    # Debug-output directory: each run uses the same dir, separated by type_key
    debug_dir = os.path.join(
        os.path.dirname(output_path),
        "_LLM_output_debug",
    )
    os.makedirs(debug_dir, exist_ok=True)

    try:
        # Step 1: load the prompt template
        template = load_prompt_template(cfg["prompt_template_name"])
        print(f"  [Thread-{type_key}] judgment-prompt template loaded: {cfg['prompt_template_name']}")

        # Step 2: filter nodes
        valid_nodes, filtered_nodes, upstream_nodes = _filter_and_classify_nodes(merged_graph_array)
        if upstream_nodes:
            print(f"\n  !!!!! WARNING !!!!! [{type_name}] found {len(upstream_nodes)} upstream-issue nodes")
            print(f"  !!!!! WARNING !!!!! (node_name=null AND node_original_name != 'Not Mentioned')")
            for g in upstream_nodes:
                orig = _normalize_original_name(g["node_original_names"][0]) if g["node_original_names"] else "?"
                nid_list = g["node_ids"][:3]
                extra = "..." if len(g["node_ids"]) > 3 else ""
                print(f"  !!!!! WARNING !!!!!   node_id={nid_list}{extra}, "
                      f"node_type={type_key}, node_original_name={repr(orig)}, node_name=null")
            print(f"  !!!!! WARNING !!!!! These nodes will NOT be classified by the LLM.\n")

        if not valid_nodes:
            raise ValueError(f"[{type_name}] all nodes were filtered; nothing to classify")

        # Step 3: split into batches
        total_groups = len(valid_nodes)
        batches: list[list[dict]] = [
            valid_nodes[i:i + BATCH_SIZE]
            for i in range(0, total_groups, BATCH_SIZE)
        ]
        total_batches = len(batches)
        print(f"  [Thread-{type_key}] {total_groups} node_name groups in total, "
              f"split into {total_batches} batches (max {BATCH_SIZE} per batch)")

        # ========== Process monitor A: accurately record all node_names entering the LLM ==========
        # Build the to-be-sent node_name set (for precise comparison with LLM output)
        sent_names_set = set()
        for g in valid_nodes:
            if g["node_name"]:
                sent_names_set.add(g["node_name"])

        # ========== Step 4: call LLM batch by batch ==========
        all_llm_parsed: list[dict] = []
        batch_times: list[float] = []
        batch_llm_output_chars: list[int] = []
        batch_llm_input_chars: list[int] = []

        for batch_idx, batch_nodes in enumerate(batches, 1):
            batch_no = batch_idx
            prompt = build_llm_input(
                template, induction_table_md, batch_nodes,
                batch_no=batch_no, total_batches=total_batches,
            )
            prompt_chars = len(prompt)
            batch_llm_input_chars.append(prompt_chars)

            # ---- Monitor: node_name count in prompt ----
            batch_names_in_prompt = [g["node_name"] for g in batch_nodes if g["node_name"]]
            print(f"  [Thread-{type_key} Batch-{batch_no}/{total_batches}] "
                  f"prompt {len(prompt)} chars, contains {len(batch_names_in_prompt)} node_names, calling LLM...")

            t_batch = time.time()
            result_text = call_llm_with_retry(prompt, config, key_manager, type_name)
            batch_elapsed = time.time() - t_batch
            batch_times.append(batch_elapsed)
            output_chars = len(result_text)
            batch_llm_output_chars.append(output_chars)

            # ---- Detection: LLM refused processing (node_group:[]) -> backoff retry ----
            # Gemini may return an empty array instead of an error when input is too large
            # or context pressure is high. In that case, back off and retry (switch key / reduce load)
            empty_group_retries = 0
            while (output_chars > 0
                   and '"node_group": []' in result_text
                   and empty_group_retries < MAX_RETRIES):
                empty_group_retries += 1
                backoff = min(INITIAL_BACKOFF * (2 ** empty_group_retries), MAX_BACKOFF)
                print(f"  !!!!! EMPTY GROUP !!!!! [{type_name} Batch-{batch_no}] "
                      f"LLM returned empty node_group; retry {empty_group_retries}, "
                      f"exponential backoff {backoff:.1f}s...")
                time.sleep(backoff)
                result_text = call_llm_with_retry(prompt, config, key_manager, type_name)
                output_chars = len(result_text)
                batch_llm_output_chars[-1] = output_chars
                batch_times[-1] = time.time() - t_batch

            # ---- Monitor: save raw LLM output (per batch) ----
            timestamp_str = time.strftime("%Y%m%d_%H%M%S")
            raw_output_path = os.path.join(
                debug_dir,
                f"[{type_key}]batch{batch_no}_raw__{timestamp_str}.txt",
            )
            save_text(result_text, raw_output_path)

            # ---- Monitor: is the LLM output approaching the token cap (truncation detection)? ----
            max_tokens = 50000
            approx_output_tokens = output_chars // 4  # rough estimate (Chinese chars are heavier)
            if approx_output_tokens > max_tokens * 0.85:
                print(f"  !!!!! TRUNCATION WARNING !!!!! [{type_name} Batch-{batch_no}] "
                      f"output approx {approx_output_tokens} tokens (>{max_tokens*0.85}), "
                      f"may be truncated! Consider increasing max_output_tokens.")

            print(f"  [Thread-{type_key} Batch-{batch_no}/{total_batches}] "
                  f"LLM output {output_chars} chars (~{approx_output_tokens} tokens, {batch_elapsed:.1f}s)"
                  f" | raw output saved: {os.path.basename(raw_output_path)}")

            # ---- Parse ----
            try:
                parsed = parse_llm_output(result_text, type_key)
                parsed_count = len(parsed)
                print(f"  [Thread-{type_key} Batch-{batch_no}/{total_batches}] "
                      f"parsed {parsed_count} classification results")

                # ---- Monitor B: in-batch node_name omission detection ----
                batch_parsed_names = set(item["node_name"] for item in parsed)
                batch_sent_names = set(batch_names_in_prompt)
                batch_missed = batch_sent_names - batch_parsed_names
                if batch_missed:
                    print(f"  !!!!! BATCH LEAK !!!!! [{type_name} Batch-{batch_no}/{total_batches}] "
                          f"LLM missed {len(batch_missed)}/{len(batch_sent_names)} node_names: "
                          f" {sorted(batch_missed)[:10]}"
                          f"{'...' if len(batch_missed) > 10 else ''}")

                # Monitor C: LLM-invented node_names (not in input)
                invented_names = batch_parsed_names - batch_sent_names
                if invented_names:
                    print(f"  !!!!! INVENTED NAMES !!!!! [{type_name} Batch-{batch_no}/{total_batches}] "
                          f"LLM invented {len(invented_names)} node_names not in input: "
                          f" {sorted(invented_names)[:10]}")

                all_llm_parsed.extend(parsed)

                if not parsed:
                    print(f"  [Thread-{type_key} Batch-{batch_no}/{total_batches}] "
                          f"WARNING: this batch's parse result is empty!")
            except ValueError as parse_err:
                # ---- Detailed monitoring on parse failure ----
                err_str = str(parse_err)
                fail_output_path = os.path.join(
                    debug_dir,
                    f"[{type_key}]batch{batch_no}_parse_fail__{timestamp_str}.txt",
                )
                fail_report = (
                    f"========== Parse-Failure Report ==========\n"
                    f"Time: {timestamp_str}\n"
                    f"Batch: {batch_no}/{total_batches}\n"
                    f"node_type: {type_key}\n"
                    f"Error: {err_str}\n"
                    f"node_names in batch: {len(batch_names_in_prompt)}\n"
                    f"node_name list (first 50): {batch_names_in_prompt[:50]}\n"
                    f"\n========== Raw LLM Output ==========\n"
                    f"{result_text}\n"
                    f"\n========== LLM Output Length: {len(result_text)} chars ==========\n"
                )
                save_text(fail_report, fail_output_path)
                print(f"\n  !!!!! PARSE FAIL !!!!! [{type_name} Batch-{batch_no}]")
                print(f"  !!!!! PARSE FAIL !!!!! Error: {err_str[:200]}")
                print(f"  !!!!! PARSE FAIL !!!!! Full report saved: {os.path.basename(fail_output_path)}")
                print(f"  !!!!! PARSE FAIL !!!!! Raw output saved: {os.path.basename(raw_output_path)}\n")
                raise

        # ========== Process monitor D: overall LLM-classification completeness report ==========
        all_parsed_names = set(item["node_name"] for item in all_llm_parsed)
        total_sent = len(sent_names_set)
        total_parsed = len(all_parsed_names)
        leak_count = total_sent - total_parsed
        leak_pct = leak_count / total_sent * 100 if total_sent > 0 else 0

        print(f"\n  [MONITOR-{type_key}] ========== LLM-classification completeness monitor ==========")
        print(f"  [MONITOR-{type_key}] node_name groups entering LLM: {total_sent}")
        print(f"  [MONITOR-{type_key}] node_names actually returned by LLM: {total_parsed}")
        print(f"  [MONITOR-{type_key}] missed node_name groups: {leak_count} ({leak_pct:.1f}%)")
        if leak_count > 0:
            leaked_names = sent_names_set - all_parsed_names
            print(f"  [MONITOR-{type_key}] missed node_names: {sorted(leaked_names)}")
            # Save the missed list
            leak_report_path = os.path.join(debug_dir, f"[{type_key}]missed_node_name_list__{timestamp_str}.txt")
            leak_content = (
                f"========== LLM-classification Missed Report ==========\n"
                f"Time: {timestamp_str}\n"
                f"node_type: {type_key}\n"
                f"Total node_names entering LLM: {total_sent}\n"
                f"LLM-returned count: {total_parsed}\n"
                f"Missed count: {leak_count} ({leak_pct:.1f}%)\n"
                f"\n========== The {leak_count} missed node_names ==========\n"
            )
            for name in sorted(leaked_names):
                ids = name_to_ids.get(name, [])
                leak_content += f"  {name} -> {len(ids)} node_ids: {ids}\n"
            save_text(leak_content, leak_report_path)
            print(f"  [MONITOR-{type_key}] missed-list saved: {os.path.basename(leak_report_path)}")

        print(f"  [MONITOR-{type_key}] LLM-invented node_name count: {len(all_parsed_names - sent_names_set)}")
        print(f"  [MONITOR-{type_key}] Per-batch input/output char counts: {list(zip(batch_llm_input_chars, batch_llm_output_chars))}")
        print(f"  [MONITOR-{type_key}] =========================================\n")

        print(f"  [Thread-{type_key}] all {total_batches} batches done, "
              f"{len(all_llm_parsed)} node_name classification results in total, "
              f"cumulative {sum(batch_times):.1f}s")

        # ========== Step 5: build the three-level mapping ==========
        name_to_ids: dict[str, list[str]] = {}
        for g in valid_nodes:
            name_to_ids[g["node_name"]] = g["node_ids"]

        # ========== Process monitor E: final mapping-table completeness report ==========
        total_mapped_ids = sum(len(v["node_ids"]) for v in induce_mapping.values())
        upstream_filtered = len(filtered_nodes) + len(upstream_nodes)
        expected_mapped = sum(len(g["node_ids"]) for g in valid_nodes)
        actual_mapped = sum(len(v["node_ids"]) for v in induce_mapping.values())
        mapping_leak = expected_mapped - actual_mapped

        print(f"  [MONITOR-{type_key}] ========== Mapping-table completeness monitor ==========")
        print(f"  [MONITOR-{type_key}] Original node_id total (merged): {len(merged_graph_array)} groups")
        print(f"  [MONITOR-{type_key}] Upstream-filtered (empty name) node_id count: {upstream_filtered}")
        print(f"  [MONITOR-{type_key}] Expected-to-map (valid) node_id count: {expected_mapped}")
        print(f"  [MONITOR-{type_key}] Actually-mapped node_id count: {actual_mapped}")
        print(f"  [MONITOR-{type_key}] Mapping-table leak node_id count: {mapping_leak} ({mapping_leak/expected_mapped*100:.1f}% of valid)")
        print(f"  [MONITOR-{type_key}] =========================================\n")

        # ========== Step 6: generate mapping-table Markdown and save ==========
        mapping_md = generate_mapping_md(type_key, induction_records, induce_mapping)
        save_text(mapping_md, output_path)

        elapsed = time.time() - t0
        print(f"  [Thread-{type_key}] done: {os.path.basename(output_path)} "
              f"({len(mapping_md)} chars, {elapsed:.1f}s)")

        return {
            "success": True,
            "type_key": type_key,
            "type_name": type_name,
            "output_path": output_path,
            "elapsed_s": elapsed,
            "llm_parsed_count": len(all_llm_parsed),
            "total_batches": total_batches,
            "upstream_issue_count": len(upstream_nodes),
            "upstream_filtered_count": upstream_filtered,
            "mapping_leak_count": mapping_leak,
            "sent_names_count": total_sent,
            "llm_parsed_names_count": total_parsed,
            "error": None,
        }

    except Exception as e:
        elapsed = time.time() - t0
        print(f"  [Thread-{type_key}] failed: {type(e).__name__}: {e}")
        return {
            "success": False,
            "type_key": type_key,
            "type_name": type_name,
            "output_path": output_path,
            "elapsed_s": elapsed,
            "error": str(e),
        }


# ============================================================================
# Part 10.5: P3 - structured JSON report file writing
# ============================================================================

def _build_json_report(
    all_results: list[dict],
    sanitize_stats: dict,
    skipped_tasks: list[dict],
    total_elapsed_s: float,
    timestamp_str: str,
) -> dict:
    """
    Aggregate key run data into a structured JSON report for later analysis and
    automated monitoring.
    """
    report = {
        "timestamp": timestamp_str,
        "program": "zotero_knowledge_graph_extractor_归纳映射表_v9",
        "version": "v9-P0P1P2P3",
        "config": {
            "BATCH_SIZE": BATCH_SIZE,
            "max_output_tokens": 50000,
            "llm_model": LLM_CONFIG.get("model", "gemini-3.5-flash"),
            "num_api_keys": len(MULTI_API_KEYS),
        },
        "p0_sanitize": sanitize_stats,
        "tasks_summary": {
            "total": len(all_results) + len(skipped_tasks),
            "succeeded": sum(1 for r in all_results if r["success"]),
            "failed": sum(1 for r in all_results if not r["success"]),
            "skipped": len(skipped_tasks),
        },
        "per_type": [],
        "overall": {
            "total_elapsed_s": round(total_elapsed_s, 1),
            "total_sent_names": 0,
            "total_parsed_names": 0,
            "total_llm_leak": 0,
            "total_upstream_filtered": 0,
            "total_mapping_leak": 0,
        },
    }

    for r in all_results:
        entry = {
            "type_key": r.get("type_key"),
            "type_name": r.get("type_name"),
            "success": r.get("success"),
            "elapsed_s": round(r.get("elapsed_s", 0), 1),
            "error": r.get("error"),
            "sent_names": r.get("sent_names_count", 0),
            "parsed_names": r.get("llm_parsed_names_count", 0),
            "llm_leak": r.get("sent_names_count", 0) - r.get("llm_parsed_names_count", 0),
            "upstream_filtered": r.get("upstream_filtered_count", 0),
            "upstream_issue": r.get("upstream_issue_count", 0),
            "mapping_leak": r.get("mapping_leak_count", 0),
            "total_batches": r.get("total_batches", 1),
        }
        entry["llm_leak_pct"] = (
            round(entry["llm_leak"] / entry["sent_names"] * 100, 2)
            if entry["sent_names"] > 0 else 0.0
        )
        report["per_type"].append(entry)
        report["overall"]["total_sent_names"] += entry["sent_names"]
        report["overall"]["total_parsed_names"] += entry["parsed_names"]
        report["overall"]["total_llm_leak"] += entry["llm_leak"]
        report["overall"]["total_upstream_filtered"] += entry["upstream_filtered"]
        report["overall"]["total_mapping_leak"] += entry["mapping_leak"]

    o = report["overall"]
    o["total_llm_leak_pct"] = (
        round(o["total_llm_leak"] / o["total_sent_names"] * 100, 2)
        if o["total_sent_names"] > 0 else 0.0
    )

    return report


def _save_json_report(
    report: dict,
    output_dir: str,
    timestamp_str: str,
) -> str:
    """Write the structured report to a JSON file; return the file path."""
    report_filename = f"映射表生成报告_{timestamp_str}.json"
    report_path = os.path.join(output_dir, report_filename)
    os.makedirs(output_dir, exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    return report_path


# ============================================================================
# Part 11: main flow
# ============================================================================

def main():
    print("=" * 70)
    print("Algorithm-Node Induction Mapping-Table Generator V9 (batch version)")
    print("=" * 70)

    # Initialize the shared Key manager
    key_manager = SharedKeyManager(MULTI_API_KEYS)
    print(f"\n[Config] API Key count: {key_manager.total_keys}, "
          f"shared Key pool, concurrency cap: {SharedKeyManager.DEFAULT_CONCURRENCY} per Key, "
          f"batch size: {BATCH_SIZE} node_names/batch")

    # ========================================================================
    # Step 1: read consensus-graph JSON + P0 compliance audit
    # ========================================================================
    print(f"\n[Step1] reading consensus-graph JSON: {INPUT_JSON_PATH}")
    if not os.path.exists(INPUT_JSON_PATH):
        raise FileNotFoundError(f"Input file does not exist: {INPUT_JSON_PATH}")
    data = load_json(INPUT_JSON_PATH)
    print(f"  -> loaded {len(data)} papers")

    # P0: compliance audit (after auditing, data is cleaned; no longer contains three classes of illegal nodes)
    data, sanitize_stats = sanitize_graph_nodes(data)
    _print_sanitize_report(sanitize_stats)

    # ========================================================================
    # Step 2: separate 5 algorithm-type node arrays
    # ========================================================================
    print(f"\n[Step2] separating 5 algorithm-type node arrays...")
    graph_arrays: dict[str, list[dict]] = {}
    for type_key, cfg in sorted(ALGO_TYPE_CONFIG.items(), key=lambda x: x[0]):
        type_name = cfg["type_name"]
        nodes = extract_graph_array_by_type(data, type_name)
        graph_arrays[type_key] = nodes
        print(f"  -> {type_name}: {len(nodes)} nodes")

    # ========================================================================
    # Step 3b: upstream-issue diagnosis (print all upstream issues before parallel execution)
    # ========================================================================
    print(f"\n[Step3b] upstream-issue node diagnosis...")
    total_upstream = 0
    for type_key in ALGO_TYPE_CONFIG:
        raw = graph_arrays[type_key]
        upstream_count = 0
        for node in raw:
            name = (node.get("node_name") or "").strip()
            if not name:
                orig = _normalize_original_name(node.get("node_original_name", "") or "")
                # node_original_name non-empty and not 'Not Mentioned' qualifies as an upstream issue
                if orig and orig != "Not Mentioned":
                    upstream_count += 1
        if upstream_count > 0:
            print(f"  !!!!! WARNING !!!!! {ALGO_TYPE_CONFIG[type_key]['type_name']}: "
                  f"found {upstream_count} node_name=null AND node_original_name != 'Not Mentioned' nodes")
            for node in raw:
                name = (node.get("node_name") or "").strip()
                if not name:
                    orig = _normalize_original_name(node.get("node_original_name", "") or "")
                    if orig and orig != "Not Mentioned":
                        print(f"  !!!!! WARNING !!!!!   node_id={node['node_id']}, "
                              f"node_original_name={repr(orig)}, node_name=null")
            total_upstream += upstream_count
    if total_upstream == 0:
        print(f"  -> no upstream-issue nodes found "
              f"(all node_name=null nodes have node_original_name 'Not Mentioned')")
    else:
        print(f"\n  Note: the above {total_upstream} upstream-issue nodes will NOT be classified by the LLM")
        print(f"        Please check upstream disambiguation and confirm node_original_name is correct")

    # ========================================================================
    # Step 3: merge-and-group (aggregate same node_name)
    # ========================================================================
    print(f"\n[Step3] merge-and-group (aggregate by node_name)...")
    merged_arrays: dict[str, list[dict]] = {}
    for type_key in ALGO_TYPE_CONFIG:
        raw = graph_arrays[type_key]
        merged = merge_graph_array(raw)
        merged_arrays[type_key] = merged
        print(f"  -> after merge {ALGO_TYPE_CONFIG[type_key]['type_name']}: "
              f"{len(merged)} node_name groups")

    # ========================================================================
    # Step 4: read induction tables & parse structure
    # ========================================================================
    print(f"\n[Step4] reading and parsing induction tables...")
    json_basename = os.path.basename(INPUT_JSON_PATH)
    json_name_no_ext = os.path.splitext(json_basename)[0]

    # Read tables (parse first to get real category count, then generate/validate prompt templates)
    induction_tables: dict[str, str] = {}
    induction_records_map: dict[str, list[dict]] = {}
    for type_key, cfg in sorted(ALGO_TYPE_CONFIG.items(), key=lambda x: x[0]):
        table_path = os.path.join(INDUCTION_TABLE_DIR,
                                  f"{json_name_no_ext}_{cfg['induction_table_suffix']}.md")
        if not os.path.exists(table_path):
            print(f"  [WARN] induction table does not exist, skipping {cfg['type_name']}: {table_path}")
            continue
        md_content = read_text(table_path)
        records = parse_induction_table(md_content, type_key)
        if not records:
            print(f"  [WARN] {cfg['type_name']}: parse_induction_table returned 0 records! "
                  f"Table format may be incompatible; please check the table file.")
        induction_tables[type_key] = md_content
        induction_records_map[type_key] = records
        print(f"  -> {cfg['type_name']}: read table {len(md_content)} chars, "
              f"parsed {len(records)} categories")

    # ========================================================================
    # Step 4b: check / generate judgment-prompt templates (must come after table parsing, since it needs the real category list)
    # ========================================================================
    print(f"\n[Step4b] checking / generating judgment-prompt templates...")
    os.makedirs(PROMPT_TEMPLATE_DIR, exist_ok=True)

    for type_key, cfg in sorted(ALGO_TYPE_CONFIG.items(), key=lambda x: x[0]):
        template_path = os.path.join(PROMPT_TEMPLATE_DIR, cfg["prompt_template_name"])
        records = induction_records_map.get(type_key, [])
        should_regenerate = False

        if not os.path.exists(template_path):
            should_regenerate = True
            reason = "[new]"
        else:
            # File exists: check whether the category count matches the current table
            existing = read_text(template_path)
            # Extract the "total X" annotation from the existing template
            count_match = re.search(r'共(\d+)\s*个', existing)
            existing_count = int(count_match.group(1)) if count_match else -1
            if existing_count != len(records):
                should_regenerate = True
                reason = f"[category-count changed {existing_count} -> {len(records)}]"
            elif not records:
                should_regenerate = True
                reason = "[table-parse failed]"

        if should_regenerate or not records:
            placeholder = _create_placeholder_prompt(cfg, records)
            save_text(placeholder, template_path)
            print(f"  -> {reason} {template_path}")

    # Print template-check results (also report existing and matching files)
    for type_key, cfg in sorted(ALGO_TYPE_CONFIG.items(), key=lambda x: x[0]):
        template_path = os.path.join(PROMPT_TEMPLATE_DIR, cfg["prompt_template_name"])
        records = induction_records_map.get(type_key, [])
        if os.path.exists(template_path):
            print(f"  -> [loaded] {cfg['prompt_template_name']} ({len(records)} categories)")

    # ========================================================================
    # Step 5: prepare parallel tasks
    # ========================================================================
    print(f"\n[Step5] preparing parallel tasks...")

    tasks = []
    for type_key in sorted(ALGO_TYPE_CONFIG.keys()):
        cfg = ALGO_TYPE_CONFIG[type_key]
        if type_key not in induction_tables:
            print(f"  [SKIP] {cfg['type_name']} induction table missing; skipping")
            continue

        output_path = os.path.join(
            OUTPUT_DIR,
            f"{json_name_no_ext}_{cfg['mapping_table_suffix']}.md"
        )
        tasks.append({
            "type_key": type_key,
            "merged_graph_array": merged_arrays[type_key],
            "induction_table_md": induction_tables[type_key],
            "induction_records": induction_records_map[type_key],
            "output_path": output_path,
        })

    if not tasks:
        print("  No tasks to run (all induction tables missing).")
        return

    # Filter out files that already exist
    skipped = [t for t in tasks if os.path.exists(t["output_path"])]
    to_run = [t for t in tasks if not os.path.exists(t["output_path"])]

    if skipped:
        print(f"  {len(skipped)} files already exist; will be skipped: "
              f"{[os.path.basename(t['output_path']) for t in skipped]}")
    print(f"\n[Step6] generating {len(to_run)} mapping tables in parallel "
          f"(workers=5, 5 dedicated API keys, synchronous parallel)...")

    if not to_run:
        print("  All files already exist; no tasks to run.")
    else:
        results = []
        t0_total = time.time()

        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = {}
            for task in to_run:
                type_key = task["type_key"]

                future = executor.submit(
                    process_single_type,
                    type_key,
                    task["merged_graph_array"],
                    task["induction_table_md"],
                    task["induction_records"],
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
                        "elapsed_s": 0.0,
                        "error": str(e),
                    })

        total_elapsed = time.time() - t0_total
        skip_count = len(skipped)

        print(f"\n{'=' * 70}")
        print(f"Results of this run ({len(to_run)} tasks, {total_elapsed:.1f}s):")
        has_any_upstream = False

        # Global aggregation
        total_upstream = 0
        total_leak = 0
        total_sent = 0
        total_parsed = 0

        for r in sorted(results, key=lambda x: x["type_key"]):
            status = "OK" if (r["success"] and r["elapsed_s"] > 0) else (
                "SKIP" if r.get("error") == "文件已存在，跳过" else "FAIL"
            )
            elapsed_str = f"{r['elapsed_s']:.1f}s" if r["elapsed_s"] > 0 else "-"
            extra_parts = []
            if r["success"] and r["elapsed_s"] > 0:
                if "llm_parsed_count" in r:
                    extra_parts.append(f"classified {r['llm_parsed_count']} node_names")
                if "total_batches" in r and r["total_batches"] > 1:
                    extra_parts.append(f"split into {r['total_batches']} batches")
                if "upstream_issue_count" in r and r["upstream_issue_count"] > 0:
                    extra_parts.append(f"[WARN] upstream-issue {r['upstream_issue_count']}")
                    has_any_upstream = True
                # Monitoring data
                if "upstream_filtered_count" in r:
                    total_upstream += r["upstream_filtered_count"]
                if "mapping_leak_count" in r:
                    total_leak += r["mapping_leak_count"]
                if "sent_names_count" in r:
                    total_sent += r["sent_names_count"]
                if "llm_parsed_names_count" in r:
                    total_parsed += r["llm_parsed_names_count"]
                if r.get("mapping_leak_count", 0) > 0:
                    extra_parts.append(f"[WARN] LLM missed {r['mapping_leak_count']} node_ids")
            extra = f" ({', '.join(extra_parts)})" if extra_parts else ""
            print(f"  [{status}] {r['type_name']} ({elapsed_str}){extra}")

        if skip_count:
            print(f"  [SKIP] {skip_count} files already existed (LLM not re-requested)")

        # ========== P3: write the structured JSON report ==========
        ts = time.strftime("%Y%m%d_%H%M%S")
        json_report = _build_json_report(
            all_results=results,
            sanitize_stats=sanitize_stats,
            skipped_tasks=skipped,
            total_elapsed_s=total_elapsed,
            timestamp_str=ts,
        )
        json_report_path = _save_json_report(json_report, OUTPUT_DIR, ts)
        print(f"\n  [P3-REPORT] structured report written: {os.path.basename(json_report_path)}")

        # ========== Process-monitoring summary report (printed in terminal; complementary to JSON) ==========
        if total_sent > 0:
            llm_leak = total_sent - total_parsed
            llm_leak_pct = llm_leak / total_sent * 100
            print(f"\n  [MONITOR-ALL] ========== Cross-type LLM-classification summary ==========")
            print(f"  [MONITOR-ALL] Total node_names entering LLM: {total_sent}")
            print(f"  [MONITOR-ALL] Total node_names actually returned by LLM: {total_parsed}")
            print(f"  [MONITOR-ALL] Total node_names missed by LLM: {llm_leak} ({llm_leak_pct:.1f}%)")
            print(f"  [MONITOR-ALL] Total upstream-filtered node_ids: {total_upstream}")
            print(f"  [MONITOR-ALL] Total LLM-stage mapping_leak: {total_leak}")
            print(f"  [MONITOR-ALL] =========================================\n")

        if has_any_upstream:
            print(f"\n  Note: [WARN] upstream-issue nodes (node_name=null AND node_original_name != 'Not Mentioned') are NOT classified by the LLM")
            print(f"        Please check upstream disambiguation and confirm node_original_name is correct")
        print(f"  Key usage stats: {key_manager.usage_report()}")

    print(f"\n{'=' * 70}")
    print("All done!")
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Prompt directory: {PROMPT_TEMPLATE_DIR}")
    print(f"P3 JSON report directory: {OUTPUT_DIR}")
    print("=" * 70)


# ============================================================================
# Placeholder prompt-template generator (dynamically inject the real category list from the induction table)
# ============================================================================

def _build_category_list_section(records: list[dict], type_key: str) -> str:
    """
    Dynamically generate the "selectable category names" section from the parsed
    induction-table results. One category per line with sequence number, so the LLM
    strictly follows numbers when classifying.
    """
    if not records:
        return "> (Table parse failed; cannot provide category list. Please check the table format.)"
    lines = []
    for i, rec in enumerate(records, 1):
        name = rec.get("type_name", "").strip()
        if name:
            lines.append(f"> {i}. {name}")
    return "\n".join(lines)


def _create_placeholder_prompt(cfg: dict, records: list[dict]) -> str:
    """
    Dynamically generate the judgment-prompt template based on the parsed induction-table results.

    Key improvements:
      - The category list is dynamically injected from `records` (no longer hard-coded)
      - The category-count annotation stays in sync with `records` (template auto-updates
        when the table changes)
      - The format specification matches the first successful run (no code blocks,
        no narrative content, etc.)
    """
    type_key = cfg["type_key"]
    type_name = cfg["type_name"]
    num_categories = len(records)
    category_list_md = _build_category_list_section(records, type_key)

    # 从 records 提取第一个类别的 type_name 作为 JSON 示例
    first_cat = records[0]["type_name"] if records else "<类别名称>"
    first_example_induce = first_cat  # 简单示例：归入自己

    return f"""## 角色设定

你是 PHM（Prognostics and Health Management）领域的知识图谱工程助手，擅长将文献中抽取的算法实例节点准确归类到预定义的主流算法类别体系中。

---

## 任务

请根据下方"归纳大表"中定义的 **{type_name}** 主流算法类别，对"待映射节点数组"中的每一个算法节点进行分类映射。

---

### 归纳大表（{type_name}，来源：PHM 领域专家归纳）

{{INDUCTION_TABLE}}

### 待映射节点数组（来自消歧后的paperextract JSON，已按 node_name 归类merge）

{{MERGED_GRAPH_ARRAY}}

数组字段说明：
- `node_name`：算法实例的名称。
- `node_ids`：该 node_name 在文献中对应的所有 node_id 集合。
- `node_description_top10`：该 node_name 在文献中的 node_description 前10个（不足取所有）。

---

## 重要注意事项

**1. 必须仔细阅读归纳大表**
归纳大表中的"类别名称"、"类别内涵"、"归纳标准"是归类的核心原则，你必须严格遵循。你需要先完整阅读归纳大表，理解每一个"类别名称"的定义边界。

**2. node_induce 本质上是选择题，不是随意生成**
待映射节点数组中每个 node_name 的 `node_induce` 必须从归纳大表的"类别名称"列中**选择一个**，一字不差。以下是可选的类别名称列表（共{num_categories}个）：

{category_list_md}

**3. 每个 node_name 必须有 node_induce**
待映射节点数组中的每一个 `node_name` 都必须从上述{num_categories}个类别名称中选择1个填入 `node_induce`，不能遗漏，不能留空。

**4. 结合 node_name + node_description_top10 综合判断**
归类时必须同时结合每个节点的 `node_name`（算法名称）和 `node_description_top10`（描述信息），对照归纳大表中的"类别名称"、"类别内涵"、"归纳标准"，选择最匹配的一个类别。注意不要仅凭 node_name 的字面意思判断，还要结合其在文献中的具体用法（node_description_top10）。

**5. 【强制】严格遵循输出格式**
LLM 输出必须**严格**遵循以下 JSON 结构，**禁止输出任何思考过程、解释说明、分析报告或其他额外内容**。

输出规则：
- **禁止**使用 markdown 代码块包裹（不要输出 ```json ... ```）
- **禁止**输出任何带 *分析*、*描述*、*归类* 等文字的叙述性内容
- **禁止**输出表格、分隔线、标题等任何非 JSON 内容
- **禁止**使用反引号（` `）包裹 node_name 或 category，只允许使用双引号（`"`）
- 只输出一个纯净的 JSON 对象，其中 node_group 数组包含所有 node_name 的归类结果

```json
{{
  "node_type": "{type_name}",
  "node_group": [
    {{
      "node_name": "<node_name1>",
      "node_induce": "{first_example_induce}"
    }},
    {{
      "node_name": "<node_name2>",
      "node_induce": "<从上述{num_categories}个类别名称中选择>"
    }}
  ]
}}
```

请直接输出上述格式的 JSON，勿添加任何其他内容：
"""


if __name__ == "__main__":
    main()
