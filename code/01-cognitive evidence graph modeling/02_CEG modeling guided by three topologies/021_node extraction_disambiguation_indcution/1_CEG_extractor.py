# -*- coding: utf-8 -*-
r"""
Literature Knowledge Graph Information Extraction Program V5
(v5 merged prompts + parallel extraction + enhanced JSON parsing)
========================================================================
Functions:
  1. Read literature metadata from the Excel metadata file
  2. Scan the PDF folder and match PDFs to metadata rows by title similarity
  3. case_id is taken from the PDF subfolder name (e.g. "00114") and is an objective identifier
  4. Use v5 merged prompts, comprising 4 node-extraction batches + 1 hyperparameter batch:
     (a) 00 hyperparameters.md            -> Extract algorithm hyperparameters / training config / performance metrics
     (b) 01-03,08-09 nodes.md             -> 1 call extracts 5 node types (01, 02, 03, 08, 09)
     (c) 04-07 nodes.md                   -> 1 call extracts 4 node types (04, 05, 06, 07)
     (d) 10-14 nodes.md                   -> 1 call extracts 5 node types (10, 11, 12, 13, 14)
     (e) 15-20 nodes.md                   -> 1 call extracts 6 node types (15-19 + 20 calibration)
  5. Each paper and each batch are processed in parallel and saved as separate JSON files
  6. Each paper is finally merged into a complete JSON structure
  7. Detailed statistics of token consumption and runtime per batch
  8. The full LLM raw output is recorded to a log file for analyzing extraction quality
  9. Enhanced JSON parser: can automatically extract pure JSON from mixed chain-of-thought text
 10. Auto-fix common JSON formatting errors (truncation, duplicate blocks, extra brackets, etc.)

NOTE - Prompt source directory (RELATIVE PATH placeholder):
  ./v5_version_prompts/          <-- RELATIVE PATH: folder holding the v5 prompt .md files

Output directory structure (RELATIVE PATH placeholders):
  ./output/01-03_08-09_object_problem_nodes-json/      <-- RELATIVE PATH; one JSON per paper, filename = {case_id}.json
  ./output/04-07_fault_info_nodes-json/                <-- RELATIVE PATH; one JSON per paper, filename = {case_id}.json
  ./output/10-14_data_resource_nodes-json/             <-- RELATIVE PATH; one JSON per paper, filename = {case_id}.json
  ./output/15-20_algorithm_nodes-json/                 <-- RELATIVE PATH; one JSON per paper, filename = {case_id}.json
  ./output/hyperparameters-json/                       <-- RELATIVE PATH; one JSON per paper, filename = {case_id}.json
  ./output/final_merged/final_merged.json              <-- RELATIVE PATH; merged result of all papers
  ./output/v5_stats_report_*.txt                       <-- RELATIVE PATH; token / time analysis report
  ./output/v5_stats_data_*.json                        <-- RELATIVE PATH; raw statistics
  ./llm_logs/zotero_knowledge_graph_extractor_v4_LLM_raw_output/*.log  <-- RELATIVE PATH; LLM raw-output log

JSON file naming rule:
  - Filename format: {case_id}.json (e.g. 00114.json)
  - case_id = PDF subfolder name, NOT a program-generated sequence number
  - The 5 batch JSONs for the same case_id live in their respective subdirectories

Parallelism notes:
  - Multiple papers in parallel: ThreadPoolExecutor(max_workers=PAPER_PARALLEL)
  - 4 node batches within a single paper run in parallel: ThreadPoolExecutor(max_workers=4)

Dependencies:
  pip install pymupdf openai xlrd google-genai
"""

import os
import sys
import re
import json
import time
import shutil
import argparse
from pathlib import Path
from typing import Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

# ============================================================================
# User Configuration Section
# ============================================================================

METADATA_EXCEL_PATH = r"./input/metadata.xls"
PDF_ROOT_DIR = r"./input/pdfs"

V4_ROOT_DIR = r"./output"

PROMPTS_V4_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "v5_version_prompts"
)

# v4 batch configuration: each batch corresponds to a merged prompt file and an output subdirectory.
# Important: the hyperparam batch's node_types=[] means it is NOT a node-extraction batch.
# The prompt_file names below exactly match the actual MD file names in the schema directory.
BATCH_CONFIG = [
    {
        "id": "batch1",
        "name": "01-03,08-09 Object & Problem Nodes",
        "prompt_file": "01-03,08-09 nodes.md",
        "output_subdir": "01-03_08-09_object_problem_nodes-json",
        "is_node_batch": True,       # Whether this is a node-extraction batch
        "output_key": "batch1",
    },
    {
        "id": "batch2",
        "name": "04-07 Fault Information Nodes",
        "prompt_file": "04-07 nodes.md",
        "output_subdir": "04-07_fault_info_nodes-json",
        "is_node_batch": True,
        "output_key": "batch2",
    },
    {
        "id": "batch3",
        "name": "10-14 Data & Resource Nodes",
        "prompt_file": "10-14 nodes.md",
        "output_subdir": "10-14_data_resource_nodes-json",
        "is_node_batch": True,
        "output_key": "batch3",
    },
    {
        "id": "batch4",
        "name": "15-20 Algorithm Nodes",
        "prompt_file": "15-20 nodes.md",
        "output_subdir": "15-20_algorithm_nodes-json",
        "is_node_batch": True,
        "output_key": "batch4",
    },
    {
        "id": "hyperparam",
        "name": "Hyperparameter Extraction",
        "prompt_file": "00 hyperparameters.md",
        "output_subdir": "hyperparameters-json",
        "is_node_batch": False,      # Hyperparameters are not nodes; no node extraction
        "output_key": "hyperparam",
    },
]

# Parallelism configuration
PAPER_PARALLEL = 10         # Number of papers processed concurrently (recommend >= number of API Keys to fully utilize concurrency)
BATCH_PARALLEL = 4          # Number of batches run in parallel within a single paper (excluding hyperparam)
MAX_RETRIES = 3             # Maximum retry count for LLM calls (including the first attempt)
RETRY_BASE_DELAY = 5        # Base retry delay in seconds; uses exponential backoff: delay * (2 ** attempt)
NODE_ZERO_RETRY = 0         # Retry count when nodes are parsed to 0 (0 = no retry)

LLM_CONFIG = {
    "provider": "gemini",
    "model": "gemini-3.5-flash",
    "base_url": os.environ.get("BFGA_LLM_API_URL", "https://YOUR.LLM.ENDPOINT/"),
    "timeout": 300,
    "temperature": 0.0,        # 0.0 = near-deterministic; recommended for extraction tasks
}

# Multi API Key configuration (enabled by default; auto round-robin on program start)
# Each paper is assigned a key by index modulo; the same paper always uses the same key.
# 10 keys total, supporting 10-way concurrency.
# IMPORTANT: Provide your own API keys before running. The list below should be filled with valid keys.
MULTI_API_KEYS: list[str] = []


class RoundRobinKeyManager:
    """Thread-safe round-robin Key manager"""

    def __init__(self, keys: list[str]):
        self._keys = keys
        self._lock = Lock()
        self._idx = 0
        self._usage: dict[str, int] = {}

    def get_key(self) -> str:
        with self._lock:
            key = self._keys[self._idx % len(self._keys)]
            self._idx += 1
            self._usage[key] = self._usage.get(key, 0) + 1
            return key

    def get_key_for_paper(self, paper_index: int) -> str:
        """Assign by paper index modulo, ensuring the same paper always gets the same Key"""
        with self._lock:
            key = self._keys[paper_index % len(self._keys)]
            self._usage[key] = self._usage.get(key, 0) + 1
            return key

    @property
    def total_keys(self) -> int:
        return len(self._keys)

    def usage_report(self) -> dict[str, int]:
        with self._lock:
            return dict(self._usage)


_key_manager: RoundRobinKeyManager | None = None

# ============================================================================
# Global Statistics System (Thread-Safe)
# ============================================================================

_stats_lock = Lock()
# Global per-batch statistics: {batch_id: BatchStats}
_batch_stats: dict[str, "BatchStats"] = {}
# Global per-paper statistics: {case_id: PaperStats}
_paper_stats: dict[str, "PaperStats"] = {}
# Global per-call statistics: list of dicts
_per_call_stats: list[dict] = []


class BatchStats:
    """Statistics for a single batch"""
    def __init__(self, batch_id: str, name: str, prompt_file: str):
        self.batch_id = batch_id
        self.name = name
        self.prompt_file = prompt_file
        self.call_count = 0
        self.success_count = 0
        self.fail_count = 0
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.total_time_ms = 0
        self.total_nodes = 0

    def add(self, input_tokens: int, output_tokens: int, time_ms: int, success: bool, nodes: int = 0):
        self.call_count += 1
        self.total_input_tokens += input_tokens
        self.total_output_tokens += output_tokens
        self.total_time_ms += time_ms
        self.total_nodes += nodes
        if success:
            self.success_count += 1
        else:
            self.fail_count += 1

    def to_dict(self) -> dict:
        return {
            "batch_id": self.batch_id,
            "name": self.name,
            "prompt_file": self.prompt_file,
            "call_count": self.call_count,
            "success_count": self.success_count,
            "fail_count": self.fail_count,
            "total_input_tokens": self.total_input_tokens,
            "total_output_tokens": self.total_output_tokens,
            "total_tokens": self.total_input_tokens + self.total_output_tokens,
            "avg_input_tokens": round(self.total_input_tokens / self.call_count, 2) if self.call_count > 0 else 0,
            "avg_output_tokens": round(self.total_output_tokens / self.call_count, 2) if self.call_count > 0 else 0,
            "total_time_ms": self.total_time_ms,
            "avg_time_ms": round(self.total_time_ms / self.call_count, 2) if self.call_count > 0 else 0,
            "total_nodes": self.total_nodes,
        }


class PaperStats:
    """Statistics for a single paper"""
    def __init__(self, case_id: str, title: str):
        self.case_id = case_id
        self.title = title
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.total_time_ms = 0
        self.node_count = 0
        self.batch_details: dict[str, dict] = {}

    def add_batch(self, batch_id: str, input_tokens: int, output_tokens: int,
                  time_ms: int, success: bool, nodes: int = 0):
        self.total_input_tokens += input_tokens
        self.total_output_tokens += output_tokens
        self.total_time_ms += time_ms
        self.node_count += nodes
        self.batch_details[batch_id] = {
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "time_ms": time_ms,
            "success": success,
            "nodes": nodes,
        }

    def to_dict(self) -> dict:
        return {
            "case_id": self.case_id,
            "title": self.title,
            "total_input_tokens": self.total_input_tokens,
            "total_output_tokens": self.total_output_tokens,
            "total_tokens": self.total_input_tokens + self.total_output_tokens,
            "total_time_ms": self.total_time_ms,
            "node_count": self.node_count,
            "batch_details": self.batch_details,
        }


def _get_batch_stats(batch_id: str) -> BatchStats:
    with _stats_lock:
        if batch_id not in _batch_stats:
            cfg = next((b for b in BATCH_CONFIG if b["id"] == batch_id), None)
            name = cfg["name"] if cfg else batch_id
            prompt_file = cfg["prompt_file"] if cfg else ""
            _batch_stats[batch_id] = BatchStats(batch_id, name, prompt_file)
        return _batch_stats[batch_id]


def _get_paper_stats(case_id: str, title: str = "") -> PaperStats:
    with _stats_lock:
        if case_id not in _paper_stats:
            _paper_stats[case_id] = PaperStats(case_id, title)
        elif title and not _paper_stats[case_id].title:
            _paper_stats[case_id].title = title
        return _paper_stats[case_id]


def _record_per_call(batch_id: str, case_id: str, inp: int, out: int, ms: int, ok: bool, nodes: int):
    with _stats_lock:
        _per_call_stats.append({
            "batch_id": batch_id,
            "case_id": case_id,
            "input_tokens": inp,
            "output_tokens": out,
            "time_ms": ms,
            "success": ok,
            "nodes": nodes,
        })


# ============================================================================
# LLM Raw-Output Log (for analyzing extraction quality issues)
# ============================================================================

# LLM raw-output log directory
LLM_LOG_DIR = os.path.join(
    r"./llm_logs",
    "zotero_knowledge_graph_extractor_v4_LLM_raw_output"
)
_llm_log_lock = Lock()
# Log file path for this run (initialized in main() after computing min/max case_id)
_llm_log_file_path: str = ""
# Records the last case_id written so we can insert an H2 section header when the case_id changes
_last_logged_case_id: str = ""
# Run sequence number for this invocation (incremented at program start)
_llm_run_seq: int = 0


def log_llm_raw_output(
    case_id: str,
    batch_id: str,
    batch_name: str,
    llm_response: str,
    input_tokens: int,
    output_tokens: int,
    elapsed_ms: int,
    success: bool,
    parsed_node_count: int,
):
    """
    Append the raw LLM output to a Markdown log file in human-readable form.

    The file path is determined by main() at run start (based on min/max case_id);
    one .md file is created/appended per run, with all batches of a case_id appended together.

    Markdown format:
      - Each run begins with an H1 header (run number, datetime, case_id range)
      - Hyperparameters + nodes of each case_id (5 batches) are separated by H2 sub-sections
      - Each batch has an H3 header with the batch name and success status
      - The raw LLM output is wrapped in a code block; JSON is auto-collapsible
    """
    global _llm_log_file_path, _last_logged_case_id

    if not _llm_log_file_path:
        return  # Skip if not initialized

    # Batch Chinese-name mapping (used as emoji labels in Markdown)
    batch_label_map = {
        "hyperparam": "Hyperparameters",
        "batch1": "batch1 Object & Problem Nodes",
        "batch2": "batch2 Fault Information Nodes",
        "batch3": "batch3 Data & Resource Nodes",
        "batch4": "batch4 Algorithm Nodes",
    }
    batch_icon = batch_label_map.get(batch_id, f"Batch {batch_id}")
    node_info = f"{parsed_node_count} nodes" if batch_id != "hyperparam" else "(hyperparameter batch)"

    # Truncate excessively long responses (over 500,000 characters)
    display_response = llm_response
    if len(display_response) > 500000:
        display_response = display_response[:500000] + "\n\n... [LLM response truncated, too long]"

    # Markdown record body
    record = (
        f"### {batch_icon} | [{node_info}] | {'Success' if success else 'Failed'} "
        f"| Time {elapsed_ms}ms | Tokens {input_tokens}/{output_tokens}\n\n"
        f"```json\n{display_response}\n```\n\n"
    )

    with _llm_log_lock:
        with open(_llm_log_file_path, "a", encoding="utf-8") as f:
            # Insert an H2 section header when the case_id changes
            if case_id != _last_logged_case_id:
                f.write(f"## case_id: `{case_id}`\n\n")
                _last_logged_case_id = case_id
            f.write(record)


# ============================================================================
# Utility Functions
# ============================================================================

def normalize_title_for_match(title: str) -> str:
    t = re.sub(r'[:\-–,."\'()（）\[\]·/]', ' ', str(title))
    t = re.sub(r'\s+', ' ', t).strip()
    return t.lower()


def title_similarity(t1: str, t2: str) -> float:
    words1 = set(t1.split())
    words2 = set(t2.split())
    if not words1 or not words2:
        return 0.0
    stopwords = {'a', 'an', 'and', 'or', 'the', 'of', 'for', 'in', 'on', 'with', 'to', 'by', 'based', 'using'}
    common = (words1 & words2) - stopwords
    return len(common) / max(len(words1), len(words2))


def extract_pdf_title_from_filename(filename: str) -> str:
    name = filename.replace('.pdf', '')
    m = re.match(r'^.*?\s*-\s*\d{4}\s*-\s*(.*)', name)
    return m.group(1).strip() if m else name


def load_prompt_file(filepath: str) -> str:
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Prompt file does not exist: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


_prompt_cache: dict[str, str] = {}

def _estimate_tokens(text: str) -> int:
    chinese = sum(1 for c in text if '\u4e00' <= c <= '\u9fff')
    return int(chinese * 2 + (len(text) - chinese) * 0.25)


# ============================================================================
# Metadata Reading
# ============================================================================

def load_metadata_from_excel(excel_path: str) -> list[dict]:
    import xlrd
    wb = xlrd.open_workbook(excel_path)
    ws = wb.sheet_by_index(0)
    headers = [ws.cell_value(0, j) for j in range(ws.ncols)]

    def get_col(name):
        try:
            return headers.index(name)
        except ValueError:
            return -1

    idx_title = get_col('Article Title')
    idx_doi = get_col('DOI')
    idx_journal = get_col('Source Title')
    idx_year = get_col('Publication Year')
    idx_times_cited = get_col('Times Cited, WoS Core')

    papers = []
    for i in range(1, ws.nrows):
        def val(j):
            if j < 0:
                return ''
            v = ws.cell_value(i, j)
            if isinstance(v, float):
                return str(int(v)) if v == int(v) else str(v)
            return str(v).strip() if v else ''

        year_raw = val(idx_year)
        try:
            year = int(float(year_raw)) if year_raw else None
        except (ValueError, TypeError):
            year = None

        tc_raw = val(idx_times_cited)
        try:
            times_cited = int(float(tc_raw)) if tc_raw else 0
        except (ValueError, TypeError):
            times_cited = 0

        papers.append({
            "row_index": i,
            "title": val(idx_title),
            "doi": val(idx_doi),
            "journal": val(idx_journal),
            "year": year,
            "times_cited": times_cited,
            "pdf_path": None,
            "case_id": None,
        })
    return papers


# ============================================================================
# PDF Scanning & Matching
# ============================================================================

def scan_pdf_files(pdf_root: str) -> list[dict]:
    """
    Scan the PDF folder.

    v7 version: subfolder names are Zotero keys (e.g. "225KHNN8"), not pure digits.
    - No longer requires folder names to be pure digits; uses a generic scan.
    - For each subfolder, the first PDF file is taken as the PDF for that paper.
    """
    pdf_root_path = Path(pdf_root)
    pdfs = []
    for folder in sorted(pdf_root_path.iterdir(), key=lambda p: p.name.lower()):
        if not folder.is_dir():
            continue
        case_id = folder.name            # Subfolder name = case_id (e.g. "225KHNN8")
        for pdf_file in folder.glob("*.pdf"):
            pdf_title = extract_pdf_title_from_filename(pdf_file.name)
            pdfs.append({
                "case_id": case_id,
                "pdf_path": str(pdf_file.resolve()),
                "pdf_filename": pdf_file.name,
                "pdf_title": pdf_title,
                "normalized_pdf_title": normalize_title_for_match(pdf_title),
            })
            break
    return pdfs


def match_pdfs_to_metadata(papers: list[dict], pdfs: list[dict]) -> tuple:
    matched_meta_indices = set()
    results = []
    unmatched_pdfs = []

    for pdf in pdfs:
        best_idx, best_score = -1, 0.0
        norm_pdf_title = pdf["normalized_pdf_title"]
        for i, paper in enumerate(papers):
            if i in matched_meta_indices:
                continue
            score = title_similarity(norm_pdf_title,
                                     normalize_title_for_match(paper["title"]))
            if score > best_score:
                best_score = score
                best_idx = i
        if best_score >= 0.3 and best_idx >= 0:
            papers[best_idx]["pdf_path"] = pdf["pdf_path"]
            papers[best_idx]["case_id"] = pdf["case_id"]
            matched_meta_indices.add(best_idx)
            results.append({"meta_idx": best_idx, "pdf": pdf,
                            "score": best_score, "status": "matched"})
        else:
            unmatched_pdfs.append({"pdf": pdf, "best_idx": best_idx,
                                    "best_score": best_score})
            results.append({"meta_idx": -1, "pdf": pdf,
                            "score": best_score, "status": "unmatched"})
    return papers, results, unmatched_pdfs


# ============================================================================
# PDF Text Extraction
# ============================================================================

def extract_pdf_text(pdf_path: str) -> str:
    if not pdf_path or not os.path.exists(pdf_path):
        return ""
    try:
        import pymupdf
        doc = pymupdf.open(pdf_path)
        text_parts = []
        for i in range(len(doc)):
            text = doc[i].get_text("text")
            if text.strip():
                text_parts.append(f"[Page {i+1}]\n{text.strip()}")
        doc.close()
        return "\n\n".join(text_parts)
    except Exception:
        return ""


# ============================================================================
# LLM Invocation
# ============================================================================

def call_llm(prompt: str, config: dict, api_key_config: dict | None = None) -> str:
    provider = config.get("provider", "gemini").lower()
    if provider == "gemini":
        return _call_gemini(prompt, config, api_key_config)
    elif provider == "openai":
        return _call_openai(prompt, config, api_key_config)
    elif provider == "deepseek":
        return _call_deepseek(prompt, config, api_key_config)
    elif provider == "zhipu":
        return _call_zhipu(prompt, config, api_key_config)
    else:
        raise ValueError(f"Unsupported provider: {provider}")


def _call_gemini(prompt: str, config: dict, api_key_config: dict | None = None) -> str:
    try:
        import google.genai as genai
        from google.genai.types import HttpOptions
    except ImportError:
        raise ImportError("Please install: pip install google-genai")

    # Multi-Key mode: the key in api_key_config overrides the global key in config
    if api_key_config:
        api_key = (api_key_config.get("api_key") or "").strip()
        base = (api_key_config.get("base_url") or "").strip()
    else:
        api_key = (config.get("api_key") or "").strip()
        base = (config.get("base_url") or "https://generativelanguage.googleapis.com/").strip()

    if not base.endswith("/"):
        base += "/"
    timeout_ms = max(1, int(float(config.get("timeout", 300)) * 1000))

    extra_headers = {}
    if api_key.startswith("sk-"):
        extra_headers["Authorization"] = f"Bearer {api_key}"

    http_opts = HttpOptions(base_url=base, timeout=timeout_ms,
                            headers=extra_headers or None)
    client = genai.Client(api_key=api_key, http_options=http_opts)

    response = client.models.generate_content(
        model=config.get("model", "gemini-3.5-flash"),
        contents=[prompt],
        config={"temperature": config.get("temperature", 0.0), "max_output_tokens": 30000},
    )
    try:
        parts = response.candidates[0].content.parts
        return "".join(part.text for part in parts
                       if hasattr(part, "text") and part.text)
    except Exception:
        return response.text


def _call_openai(prompt: str, config: dict, api_key_config: dict | None = None) -> str:
    import openai
    key = api_key_config.get("api_key") if api_key_config else config["api_key"]
    base = api_key_config.get("base_url") if api_key_config else config.get("base_url")
    client = openai.OpenAI(
        api_key=key,
        base_url=base,
        timeout=config.get("timeout", 120),
    )
    response = client.chat.completions.create(
        model=config["model"],
        messages=[{"role": "user", "content": prompt}],
        temperature=config.get("temperature", 0.0), max_tokens=30000,
    )
    return response.choices[0].message.content


def _call_deepseek(prompt: str, config: dict, api_key_config: dict | None = None) -> str:
    import openai
    key = api_key_config.get("api_key") if api_key_config else config["api_key"]
    base = api_key_config.get("base_url") if api_key_config else config.get("base_url")
    client = openai.OpenAI(
        api_key=key,
        base_url=base or "https://api.deepseek.com",
        timeout=config.get("timeout", 120),
    )
    response = client.chat.completions.create(
        model=config["model"],
        messages=[{"role": "user", "content": prompt}],
        temperature=config.get("temperature", 0.0), max_tokens=30000,
    )
    return response.choices[0].message.content


def _call_zhipu(prompt: str, config: dict, api_key_config: dict | None = None) -> str:
    import openai
    key = api_key_config.get("api_key") if api_key_config else config["api_key"]
    base = api_key_config.get("base_url") if api_key_config else config.get("base_url")
    client = openai.OpenAI(
        api_key=key,
        base_url=base or "https://open.bigmodel.cn/api/paas/v4",
        timeout=config.get("timeout", 120),
    )
    response = client.chat.completions.create(
        model=config["model"],
        messages=[{"role": "user", "content": prompt}],
        temperature=config.get("temperature", 0.0), max_tokens=30000,
    )
    return response.choices[0].message.content


# ============================================================================
# JSON Parsing
# ============================================================================

# ============================================================================
# JSON Parsing - Helper Functions
# ============================================================================

def _strip_llm_thinking_prefix(text: str) -> str:
    """
    Enhanced chain-of-thought removal: covers all known thinking-chain patterns.

    Known patterns (by priority):
      1. Markdown ```json ... ``` block -> extract content inside the block (take the last fence)
      2. Markdown ``` ... ``` block (no language tag) -> extract content (take the last fence)
      3. Plain-text chain-of-thought (starting with ** headers + body) -> truncate at the first [
      4. Raw text without JSON markers -> truncate at the first [ or {
    """
    text = text.strip()
    if not text:
        return text

    # ---- Strategy 1: extract blocks wrapped in ```...``` (take the last one, usually the final answer) ----
    fence_pattern = re.compile(r'```(\w*)\n(.*?)```', re.DOTALL)
    fence_matches = list(fence_pattern.finditer(text))

    if fence_matches:
        last_match = fence_matches[-1]
        fence_content = last_match.group(2).strip()
        if fence_content and fence_content[0] in '[{':
            # Keep only the portion starting from the first [ or {
            first_json_pos = min(
                (fence_content.find(c) for c in '[{' if fence_content.find(c) >= 0),
                default=-1
            )
            if first_json_pos >= 0:
                return fence_content[first_json_pos:]
            return fence_content

    # ---- Strategy 2: no fence or no JSON inside the fence -> find the first [ or { ----
    candidates: list[tuple[int, str]] = []
    for ch in "[{":
        pos = text.find(ch)
        if pos >= 0:
            candidates.append((pos, ch))

    if not candidates:
        return text

    first_pos, first_ch = min(candidates, key=lambda x: x[0])
    prefix = text[:first_pos]
    last_newline = prefix.rfind('\n')
    return text[last_newline + 1:]


def _find_all_complete_json_blocks(text: str) -> list[str]:
    """
    Greedily search all complete (non-truncated) JSON blocks from the text.

    Algorithm: for each candidate start position, use bracket counting to find
    the matching closing bracket, and verify that the next non-whitespace
    character after the close is one of ] } , newline or EOF.
    Returns the list of all successfully parsed JSON strings (in appearance order).
    """
    results: list[str] = []

    for start_idx in range(len(text)):
        ch = text[start_idx]
        if ch not in ("[", "{"):
            continue

        opener = ch
        depth = 0
        in_string = False
        string_char = ""

        for i in range(start_idx, len(text)):
            c = text[i]
            if in_string:
                if c == string_char and (i == 0 or text[i - 1] != '\\'):
                    in_string = False
                    string_char = ""
            else:
                if c in ('"', "'"):
                    in_string = True
                    string_char = c
                elif c in ("{", "["):
                    depth += 1
                elif c in ("}", "]"):
                    depth -= 1
                    if depth == 0:
                        candidate = text[start_idx:i + 1]
                        next_pos = i + 1
                        while next_pos < len(text) and text[next_pos] in " \t\r\n":
                            next_pos += 1
                        if next_pos >= len(text) or text[next_pos] in ",]\n}":
                            try:
                                json.loads(candidate)
                                results.append(candidate)
                            except Exception:
                                pass
                        break

    return results


def _try_parse_json(text: str):
    try:
        return json.loads(text.strip())
    except (json.JSONDecodeError, TypeError):
        return None


def _extract_bracketed_json(text: str, opener: str) -> Optional[str]:
    """
    Extract JSON from the text (bracket counting, skipping brackets inside strings).

    Core logic:
    - Use bracket counting to track the nesting depth of {} and []
    - Skip brackets inside strings (brackets inside single or double quotes do not count)
    - Stop when the matching closing bracket is encountered

    Parameters:
      text: the raw text
      opener: the starting character, '[' or '{'

    Returns:
      The extracted JSON string (unparsed), or None
    """
    depth = 0
    in_string = False
    string_char = ""

    for i, ch in enumerate(text):
        if in_string:
            if ch == string_char and (i == 0 or text[i - 1] != '\\'):
                in_string = False
                string_char = ""
        else:
            if ch in ('"', "'"):
                in_string = True
                string_char = ch
            elif ch == opener:
                depth += 1
            elif ch in ("]", "}"):
                depth -= 1
                if depth == 0:
                    return text[:i + 1]
            elif ch == "{" and opener == "[":
                depth += 1
            elif ch == "[" and opener == "{":
                pass

    return None


def _try_parse_truncated_json(text: str, opener: str) -> Optional[list | dict]:
    """
    Handle truncated JSON text and try to extract a complete JSON object.

    Enhanced strategy (two-level fallback):
      1. Greedily search backward from the end of the text for the last complete JSON block
      2. Use bracket counting to find the first matching ] or } and try to parse
    """
    # ---- Level 1: search backward from the end for the last complete JSON ----
    blocks = _find_all_complete_json_blocks(text)
    if blocks:
        # Take the last block (most likely the LLM's final answer)
        last = blocks[-1]
        parsed = _try_parse_json(last)
        if parsed is not None:
            return parsed

    # ---- Level 2: bracket counting to find the outer close ----
    first_char = min((text.find(c) for c in "[{" if text.find(c) >= 0), default=-1)
    if first_char < 0:
        return None

    opener_char = text[first_char]
    extracted = _extract_bracketed_json(text[first_char:], opener_char)
    if extracted:
        parsed = _try_parse_json(extracted)
        if parsed is not None:
            return parsed

    return None


def _repair_json_text(text: str) -> str:
    """
    Auto-fix common JSON formatting errors (preprocessing layer).

    Repair strategy:
      1. Remove leading Markdown fences (```json ```)
      2. Handle duplicate JSON blocks [[...]] or nesting
      3. Extract all fence blocks, take the last one (the final answer)
      4. Remove chain-of-thought text before the JSON block
    """
    text = text.strip()
    if not text:
        return text

    # ---- Repair 1: Remove Markdown code-block markers ----
    fence_pattern = re.compile(r'```(\w*)\n(.*?)```', re.DOTALL)
    fence_matches = list(fence_pattern.finditer(text))

    if fence_matches:
        # Take the content of the last fence block
        last_match = fence_matches[-1]
        content = last_match.group(2).strip()
        if content:
            text = content

    # ---- Repair 2: Remove leading ```json / ``` ----
    text = re.sub(r'^```json\s*\n?', '', text)
    text = re.sub(r'^```\s*\n?', '', text).strip()

    # ---- Repair 3: Handle [[...]] nested arrays ----
    if text.startswith('[['):
        inner = text.lstrip('[')
        while inner.startswith('['):
            try:
                parsed = json.loads(inner)
                if isinstance(parsed, list):
                    text = inner
                    break
            except Exception:
                pass
            # Try stripping one more level
            inner = inner[1:]

    # ---- Repair 4: Remove chain-of-thought text before the JSON ----
    first_pos = -1
    for ch in "[{":
        pos = text.find(ch)
        if pos >= 0 and (first_pos < 0 or pos < first_pos):
            first_pos = pos

    if first_pos > 0:
        prefix = text[:first_pos]
        # Check whether the prefix contains JSON-significant characters
        has_json_chars = any(c in prefix for c in '{}[]":')
        if not has_json_chars:
            text = text[first_pos:]
        else:
            # Mixed prefix -> truncate from the last newline
            last_nl = prefix.rfind('\n')
            if last_nl >= 0:
                text = text[last_nl + 1:]

    return text


def _extract_json_from_response(text: str) -> Optional[list | dict]:
    """Extract JSON from an LLM response (JSON repair + chain-of-thought cleanup + greedy multi-block + five-level fallback)

    Core strategy (five-level fallback):
      0. JSON repair preprocessing (remove fences, handle nesting, clean chain-of-thought prefix)
      1. Greedily search all complete JSON blocks -> try parsing each one
      2. Take the last complete JSON block (handle multiple blocks from the LLM)
      3. Bracket counting to find the outer closing ] or }
      4. Truncation recovery (search backward from the end for the last complete block)
      5. Return None on failure
    """
    text = text.strip()
    if not text:
        return None

    # ---- Level 0: JSON repair preprocessing ----
    repaired = _repair_json_text(text)

    # ---- Level 1: greedily search all complete JSON blocks ----
    for block in _find_all_complete_json_blocks(repaired):
        parsed = _try_parse_json(block)
        if parsed is not None:
            return parsed

    # ---- Level 2: take the last complete block ----
    blocks = _find_all_complete_json_blocks(repaired)
    if blocks:
        last = blocks[-1]
        parsed = _try_parse_json(last)
        if parsed is not None:
            return parsed

    # ---- Level 3: bracket counting ----
    first_char_pos = min(
        (repaired.find(c) for c in "[{" if repaired.find(c) >= 0),
        default=-1
    )
    if first_char_pos < 0:
        return None

    opener = repaired[first_char_pos]
    extracted = _extract_bracketed_json(repaired[first_char_pos:], opener)
    if extracted:
        parsed = _try_parse_json(extracted)
        if parsed is not None:
            return parsed

    # ---- Level 4: truncation recovery ----
    return _try_parse_truncated_json(repaired[first_char_pos:], opener)


def _normalize_node_keys(node: dict) -> dict:
    """
    Normalize non-standard field names from the LLM output to standard snake_case.

    Known non-standard mappings (common in Gemini/GPT responses):
      camelCase -> snake_case
      Node_id      -> node_id
      Node_type    -> node_type
      Node_original_name -> node_original_name
      Node_parameters    -> node_parameters
      Node_description   -> node_description
      Highest_importance -> highest_importance
      node_case_id_list  -> node_case_id_list (unchanged)

    Also cleans empty-string node_ids (to avoid downstream logic misjudging them).
    """
    FIELD_MAP = {
        "Node_id": "node_id",
        "Node_type": "node_type",
        "Node_original_name": "node_original_name",
        "Node_parameters": "node_parameters",
        "Node_description": "node_description",
        "Highest_importance": "highest_importance",
        "node_case_id_list": "node_case_id_list",
    }
    # Tolerance for {}-style: for text fields containing {}, strip inner { and }
    normalized = {}
    for k, v in node.items():
        new_key = FIELD_MAP.get(k, k)
        if new_key == "node_id":
            if v == "":
                v = None
            else:
                # Fix abnormal node_id formats (e.g. "171_11_5" missing the "_N")
                nid_str = str(v).strip()
                fixed_nid, status = check_and_fix_node_id_format(nid_str)
                if status == "fixed":
                    sys.stderr.write(
                        f"[WARN] node_id format abnormal: \"{nid_str}\" -> fixed to \"{fixed_nid}\"\n"
                    )
                    v = fixed_nid
        elif isinstance(v, str):
            # Strip { and } inside strings (handles cases like LLM outputting "{xxx}")
            v = v.replace("{", "").replace("}", "")
        normalized[new_key] = v
    return normalized


def _strip_order_fields(node: dict) -> dict:
    """Remove unwanted absolute-order attribute fields from a node"""
    return {k: v for k, v in node.items()
            if k not in ("node_absolute_order",
                         "node_absolute_order_mean",
                         "node_absolute_order_variance")}


def validate_batch4_structure(nodes: list[dict]) -> tuple[bool, str]:
    """
    Validate that the batch4 (15-20 Algorithm Nodes) output structure is correct.

    Pass criteria (all must hold):
      1. Number of nodes >= 6 (must include 15-19 + 20 calibration)
      2. Node 20 exists ("20-Algorithm Node Role-Importance Calibration")
      3. node_type for nodes 15-19 must be a string (not a number)
      4. node_description for node 20 must be a string (not a nested object)

    Returns: (is_valid, reason)
    """
    if not isinstance(nodes, list):
        return False, f"Result is not an array, but {type(nodes).__name__}"

    # 1. Node count check
    if len(nodes) < 6:
        return False, f"Number of nodes = {len(nodes)} < 6 (nodes missing)"

    # 2. Find node 20
    calib_node = None
    for n in nodes:
        ntype = str(n.get("node_type") or n.get("Node_type") or "")
        if ntype == "20-Algorithm Node Role-Importance Calibration":
            calib_node = n
            break

    if calib_node is None:
        return False, "Missing node 20 (calibration node)"

    # 3. Check that node_type for nodes 15-19 is a string
    expected_types = {"15-Data Preprocessing Algorithm", "16-Feature Extraction Algorithm",
                      "17-Core Classifier Algorithm", "18-Data Generation Algorithm",
                      "19-Training Optimization Algorithm"}
    found_types = set()
    for n in nodes:
        ntype_raw = n.get("node_type") or n.get("Node_type") or ""
        ntype_str = str(ntype_raw)
        found_types.add(ntype_str)

        # Check that node_type is not a number (incorrect format)
        if isinstance(ntype_raw, (int, float)):
            return False, f"node_type is a number {ntype_raw}; should be a string"

        # Check that it is not an empty string
        if ntype_str == "":
            return False, f"node_id={n.get('node_id','?')} has an empty node_type"

    # Check that all 15-19 are present (20 not counted here; only advisory)
    for expected in expected_types:
        if expected not in found_types:
            return False, f"Missing node type: {expected}"

    # 4. Check that node 20's node_description is plain text
    calib_desc = calib_node.get("node_description") or calib_node.get("Node_description")
    if calib_desc is None:
        return False, "node 20's node_description is null"

    # If it is a dict or list (nested format), the LLM output an object instead of text
    if isinstance(calib_desc, (dict, list)):
        return False, f"node 20's node_description is {type(calib_desc).__name__}, not a string"

    if not isinstance(calib_desc, str):
        return False, f"node 20's node_description is {type(calib_desc).__name__}, not a string"

    return True, "Pass"


# node_id standard format: case_id_prefix + "_" + category number (2 digits) + "_N" + sequence (1-2 digits)
# Example: C00168_11_N5, C00171_15_N1, C00169_19_N3
# Anomalous format the LLM may produce (missing "_N" prefix): e.g. 171_11_5 -> C00171_11_5
_NODE_ID_PATTERN = re.compile(r"^[A-Z]?\d{5}_\d{2}_N\d+$")
_NODE_ID_ANOMALY_PATTERN = re.compile(r"^([A-Z]?\d{5}_\d{2})_(\d+)$")


def check_and_fix_node_id_format(node_id: str) -> tuple[str, str]:
    """
    Check the node_id format and auto-fix anomalies.

    Parameters:
        node_id: the node_id string to check

    Returns:
        (fixed_node_id, status_message)
        - Format OK: returns (original, "ok")
        - Missing "_N" prefix: returns (fixed value, "fixed")
        - Cannot determine: returns (original, "unknown")
    """
    if not node_id:
        return node_id, "empty"
    if _NODE_ID_PATTERN.match(node_id):
        return node_id, "ok"
    m = _NODE_ID_ANOMALY_PATTERN.match(node_id)
    if m:
        prefix, num = m.group(1), m.group(2)
        fixed = f"{prefix}_N{num}"
        return fixed, "fixed"
    return node_id, "unknown"


def _is_valid_node_object(obj: dict) -> bool:
    """
    Determine whether a dict is a valid node object.
    Must contain all 6 core fields, and node_id must not be empty.
    """
    REQUIRED_FIELDS = [
        "node_id",
        "node_type",
        "node_original_name",
        "node_name",
        "node_description",
        "node_case_id_list",
    ]
    if not isinstance(obj, dict):
        return False
    for field in REQUIRED_FIELDS:
        if field not in obj:
            return False
    # Empty-string node_id is also considered invalid
    node_id = obj.get("node_id")
    if node_id is None or str(node_id).strip() == "":
        return False
    return True


def _extract_all_node_objects(text: str) -> list[dict]:
    """
    Extract all valid node objects from the raw LLM text.

    Core strategy (four-level fallback):
      0. JSON repair preprocessing (remove fences, handle nesting, clean chain-of-thought prefix)
      1. Greedily search all complete JSON blocks -> parse each one
      2. Take the last complete JSON block (handle duplicate blocks)
      3. Bracket counting + truncation recovery (final fallback)

    From the parsed result, extract all valid nodes that contain the 6 core
    fields and have a non-empty node_id.
    """
    text = text.strip()
    if not text:
        return []

    # ---- Level 0: JSON repair preprocessing ----
    repaired = _repair_json_text(text)

    # ---- Level 1: greedily search all complete JSON blocks ----
    results: list[dict] = []
    for block in _find_all_complete_json_blocks(repaired):
        parsed = _try_parse_json(block)
        if parsed is None:
            continue
        if isinstance(parsed, list):
            for item in parsed:
                if isinstance(item, dict):
                    norm = _normalize_node_keys(item)
                    if _is_valid_node_object(norm):
                        results.append(norm)
        elif isinstance(parsed, dict):
            norm = _normalize_node_keys(parsed)
            if _is_valid_node_object(norm):
                results.append(norm)

    if results:
        return results

    # ---- Level 2: take the last complete block ----
    blocks = _find_all_complete_json_blocks(repaired)
    if blocks:
        last = blocks[-1]
        parsed = _try_parse_json(last)
        if parsed is not None:
            if isinstance(parsed, list):
                for item in parsed:
                    if isinstance(item, dict):
                        norm = _normalize_node_keys(item)
                        if _is_valid_node_object(norm):
                            results.append(norm)
            elif isinstance(parsed, dict):
                norm = _normalize_node_keys(parsed)
                if _is_valid_node_object(norm):
                    results.append(norm)
        if results:
            return results

    # ---- Level 3: bracket counting + truncation recovery ----
    first_char = min((repaired.find(c) for c in "[{" if repaired.find(c) >= 0), default=-1)
    if first_char < 0:
        return []

    opener = repaired[first_char]
    extracted = _extract_bracketed_json(repaired[first_char:], opener)
    if not extracted:
        return []

    parsed = _try_parse_json(extracted)
    if parsed is None:
        parsed = _try_parse_truncated_json(extracted, opener)

    if parsed is None:
        return []

    if isinstance(parsed, list):
        for item in parsed:
            if isinstance(item, dict):
                norm = _normalize_node_keys(item)
                if _is_valid_node_object(norm):
                    results.append(norm)
    elif isinstance(parsed, dict):
        norm = _normalize_node_keys(parsed)
        if _is_valid_node_object(norm):
            results.append(norm)

    return results


def _is_valid_hyperparam_object(obj: dict) -> bool:
    """
    Determine whether a dict is a valid hyperparameter object.
    Must contain all 5 core fields, and node_id must not be empty.
    """
    REQUIRED_FIELDS = [
        "node_id",
        "node_type",
        "algorithm_hyperparameters",
        "training_config",
        "performance_metrics",
    ]
    if not isinstance(obj, dict):
        return False
    for field in REQUIRED_FIELDS:
        if field not in obj:
            return False
    node_id = obj.get("node_id")
    if node_id is None or str(node_id).strip() == "":
        return False
    return True


def _extract_all_hyperparam_objects(text: str) -> list[dict]:
    """
    Extract all valid hyperparameter objects from the raw LLM text.

    Core strategy (three-level fallback):
      0. JSON repair preprocessing (remove fences, handle nesting, clean chain-of-thought prefix)
      1. Greedily search all complete JSON blocks -> parse each one
      2. Take the last complete JSON block (handle duplicate blocks)
      3. Bracket counting + truncation recovery (final fallback)
    """
    text = text.strip()
    if not text:
        return []

    # ---- Level 0: JSON repair preprocessing ----
    repaired = _repair_json_text(text)

    # ---- Level 1: greedily search all complete JSON blocks ----
    results: list[dict] = []
    for block in _find_all_complete_json_blocks(repaired):
        parsed = _try_parse_json(block)
        if parsed is None:
            continue
        if isinstance(parsed, list):
            for item in parsed:
                if isinstance(item, dict) and _is_valid_hyperparam_object(item):
                    results.append(item)
        elif isinstance(parsed, dict) and _is_valid_hyperparam_object(parsed):
            results.append(parsed)

    if results:
        return results

    # ---- Level 2: take the last complete block ----
    blocks = _find_all_complete_json_blocks(repaired)
    if blocks:
        last = blocks[-1]
        parsed = _try_parse_json(last)
        if parsed is not None:
            if isinstance(parsed, list):
                for item in parsed:
                    if isinstance(item, dict) and _is_valid_hyperparam_object(item):
                        results.append(item)
            elif isinstance(parsed, dict) and _is_valid_hyperparam_object(parsed):
                results.append(parsed)
        if results:
            return results

    # ---- Level 3: bracket counting + truncation recovery ----
    first_char = min((repaired.find(c) for c in "[{" if repaired.find(c) >= 0), default=-1)
    if first_char < 0:
        return []

    opener = repaired[first_char]
    extracted = _extract_bracketed_json(repaired[first_char:], opener)
    if not extracted:
        return []

    parsed = _try_parse_json(extracted)
    if parsed is None:
        parsed = _try_parse_truncated_json(extracted, opener)

    if parsed is None:
        return []

    if isinstance(parsed, list):
        for item in parsed:
            if isinstance(item, dict) and _is_valid_hyperparam_object(item):
                results.append(item)
    elif isinstance(parsed, dict) and _is_valid_hyperparam_object(parsed):
        results.append(parsed)

    return results


def parse_hyperparam_response(response_text: str) -> dict:
    """Parse the hyperparameter-extraction response, returning {algorithm_hyperparameters, training_config, performance_metrics}

    Strategy:
      1. Use bracket counting to extract all complete {} JSON objects from the text
      2. Keep only valid hyperparameter objects that contain all 5 core fields and have a non-empty node_id
      3. Take the first valid object and extract its three business fields
    """
    raw_objects = _extract_all_hyperparam_objects(response_text)

    if not raw_objects:
        return {
            "algorithm_hyperparameters": None,
            "training_config": None,
            "performance_metrics": None,
        }

    # Take the first valid object
    item = raw_objects[0]
    return {
        "algorithm_hyperparameters": item.get("algorithm_hyperparameters"),
        "training_config": item.get("training_config"),
        "performance_metrics": item.get("performance_metrics"),
    }


def _deduplicate_nodes(nodes: list[dict]) -> list[dict]:
    """
    Deduplicate the node list by node_id + node_type + node_original_name + node_description + node_case_id_list,
    keeping the first occurrence of each unique node.
    """
    seen: set[str] = set()
    unique: list[dict] = []

    for n in nodes:
        # Use 5 core fields to compose the dedup key (excluding node_name)
        key_parts = [
            str(n.get("node_id") or ""),
            str(n.get("node_type") or ""),
            str(n.get("node_original_name") or ""),
            str(n.get("node_description") or ""),
            str(n.get("node_case_id_list") or ""),
        ]
        key = "|||".join(key_parts)
        if key not in seen:
            seen.add(key)
            unique.append(n)

    return unique


def parse_batch_node_response(response_text: str) -> list[dict]:
    """Parse the merged-node-extraction response and return the node list

    Strategy:
      1. Use bracket counting to extract all complete {} JSON objects from the text
      2. Keep only valid nodes that contain all 6 core fields and have a non-empty node_id
      3. Normalize field names; remove order-attribute fields
      4. Deduplicate by the 5 core fields
    """
    raw_nodes = _extract_all_node_objects(response_text)

    if not raw_nodes:
        return []

    # Remove order-attribute fields
    nodes = [_strip_order_fields(n) for n in raw_nodes]

    # Deduplicate
    nodes = _deduplicate_nodes(nodes)

    return nodes
    return {k: v for k, v in node.items()
            if k not in ("node_absolute_order",
                         "node_absolute_order_mean",
                         "node_absolute_order_variance")}


# Prompt Construction
# ============================================================================

def build_hyperparam_prompt(md_content: str, paper_title: str,
                            pdf_text: str) -> str:
    return f"""You are an academic literature analysis expert in the PHM (Prognostics and Health Management) field.
Your task is to extract information from the following academic paper in the specified JSON format.

{'='*60}
[Prompt Details]
{'='*60}
{md_content.strip()}

{'='*60}
[Paper to Extract]
{'='*60}
Title: {paper_title}

{'='*60}
[PDF Text Content (Full Paper)]
{'='*60}
{pdf_text if pdf_text else '[PDF text extraction failed; please extract information as best you can from the title and abstract]'}

{'='*60}
[Operating Instructions]
{'='*60}
Please strictly follow the [Extraction Prompt Details] and [Mandatory Constraints] sections
of the [Prompt Details] above, extract hyperparameter information from [PDF Text Content],
and output JSON directly without any explanatory text.

Output JSON:
"""


def build_batch_prompt(md_content: str, paper_title: str,
                       pdf_text: str, case_id: str) -> str:
    """Build the prompt for merged node extraction"""
    return f"""You are an academic literature analysis expert in the PHM (Prognostics and Health Management) field.
Your task is to extract multiple types of node information from the following academic paper in a single shot, in the specified JSON format.

{'='*60}
[Prompt Details]
{'='*60}
{md_content.strip()}

{'='*60}
[Paper Metadata to Extract]
{'='*60}
Paper ID (case_id): {case_id}
Title: {paper_title}

{'='*60}
[PDF Text Content (Full Paper)]
{'='*60}
{pdf_text if pdf_text else '[PDF text extraction failed; please extract information as best you can from the title and abstract]'}

{'='*60}
[Operating Instructions]
{'='*60}
Please strictly follow all sections of the [Prompt Details] above,
extract all nodes in one shot from [PDF Text Content], and output the complete JSON array.

Notes:
- Replace <case_id> in the output with: {case_id}
- Output JSON directly, without any explanatory text

Output JSON:
"""


# ============================================================================
# Single-Batch Node Extraction (with retry and statistics)
# ============================================================================

def extract_single_batch(
    batch_config: dict,
    paper: dict,
    case_id: str,
    pdf_text: str,
    llm_config: dict,
    api_key_config: dict | None = None,
    logger: callable | None = None,
) -> dict:
    """
    Extract a single batch of nodes / hyperparameters.
    Returns a result dictionary:
      {
        "batch_id": str,
        "success": bool,
        "error": str,
        "input_tokens": int,
        "output_tokens": int,
        "elapsed_ms": int,
        "nodes": list[dict],          # node-extraction batch
        "hyperparam": dict,           # hyperparameter batch
        "llm_response": str,
        "llm_response_for_save": str,  # for saving (may be truncated)
      }
    """
    prompt_file = batch_config["prompt_file"]
    prompt_path = os.path.join(PROMPTS_V4_DIR, prompt_file)
    batch_id = batch_config["id"]
    is_node_batch = batch_config["is_node_batch"]

    result = {
        "batch_id": batch_id,
        "success": False,
        "error": "",
        "input_tokens": 0,
        "output_tokens": 0,
        "elapsed_ms": 0,
        "nodes": [],
        "hyperparam": None,
        "llm_response": "",
        "llm_response_for_save": "",
    }

    try:
        if prompt_file in _prompt_cache:
            md_content = _prompt_cache[prompt_file]
        else:
            md_content = load_prompt_file(prompt_path)
            _prompt_cache[prompt_file] = md_content
    except FileNotFoundError as e:
        result["error"] = str(e)
        return result

    # Build prompt
    if batch_id == "hyperparam":
        prompt = build_hyperparam_prompt(md_content,
                                          paper.get("title", ""), pdf_text)
    else:
        prompt = build_batch_prompt(md_content,
                                    paper.get("title", ""), pdf_text, case_id)

    input_tokens = _estimate_tokens(prompt)

    # LLM call with retry (batch4 adds extra retries for structure validation)
    last_error = ""
    last_response = ""
    last_nodes: list[dict] = []
    BATCH4_STRUCT_RETRY = 1  # extra retry count for structure validation failure

    for attempt in range(MAX_RETRIES + BATCH4_STRUCT_RETRY):
        t0 = time.time()
        try:
            response = call_llm(prompt, llm_config, api_key_config)
            elapsed_ms = int((time.time() - t0) * 1000)
            output_tokens = _estimate_tokens(response)

            # Parse response
            if batch_id == "hyperparam":
                hyperparam = parse_hyperparam_response(response)
                nodes = []
                result["hyperparam"] = hyperparam
                result["success"] = True
                result["input_tokens"] = input_tokens
                result["output_tokens"] = output_tokens
                result["elapsed_ms"] = elapsed_ms
                result["llm_response"] = response
                if len(response) > 100000:
                    result["llm_response_for_save"] = response[:100000] + "\n... [response truncated, too long]"
                else:
                    result["llm_response_for_save"] = response
                bs = _get_batch_stats(batch_id)
                bs.add(input_tokens, output_tokens, elapsed_ms, True, 0)
                ps = _get_paper_stats(case_id, paper.get("title", ""))
                ps.add_batch(batch_id, input_tokens, output_tokens, elapsed_ms, True, 0)
                _record_per_call(batch_id, case_id, input_tokens, output_tokens, elapsed_ms, True, 0)
                # Save LLM raw output to the log
                log_llm_raw_output(
                    case_id=case_id,
                    batch_id=batch_id,
                    batch_name=batch_config["name"],
                    llm_response=response,
                    input_tokens=input_tokens,
                    output_tokens=output_tokens,
                    elapsed_ms=elapsed_ms,
                    success=True,
                    parsed_node_count=0,
                )
                return result
            else:
                nodes = parse_batch_node_response(response)
                result["nodes"] = nodes
                last_nodes = nodes
                last_response = response

                # ---- batch4-specific structure validation; trigger an extra retry on failure ----
                struct_valid = True
                should_struct_retry = False
                if batch_id == "batch4":
                    struct_valid, _ = validate_batch4_structure(nodes)
                    if not struct_valid:
                        struct_retry_count = result.get("struct_retry_count", 0)
                        if struct_retry_count < BATCH4_STRUCT_RETRY:
                            result["struct_retry_count"] = struct_retry_count + 1
                            should_struct_retry = True

                if not should_struct_retry:
                    result["success"] = True
                    result["input_tokens"] = input_tokens
                    result["output_tokens"] = output_tokens
                    result["elapsed_ms"] = elapsed_ms
                    result["llm_response"] = response
                    if len(response) > 100000:
                        result["llm_response_for_save"] = response[:100000] + "\n... [response truncated, too long]"
                    else:
                        result["llm_response_for_save"] = response
                    bs = _get_batch_stats(batch_id)
                    bs.add(input_tokens, output_tokens, elapsed_ms, True, len(nodes))
                    ps = _get_paper_stats(case_id, paper.get("title", ""))
                    ps.add_batch(batch_id, input_tokens, output_tokens, elapsed_ms, True, len(nodes))
                    _record_per_call(batch_id, case_id, input_tokens, output_tokens, elapsed_ms, True, len(nodes))
                    # Save LLM raw output to the log
                    log_llm_raw_output(
                        case_id=case_id,
                        batch_id=batch_id,
                        batch_name=batch_config["name"],
                        llm_response=response,
                        input_tokens=input_tokens,
                        output_tokens=output_tokens,
                        elapsed_ms=elapsed_ms,
                        success=True,
                        parsed_node_count=len(nodes),
                    )
                    return result
                # batch4 structure validation failed but retry count remains -> continue retrying
                # (do not set success; keep the parsed nodes as fallback)

        except Exception as e:
            elapsed_ms = int((time.time() - t0) * 1000)
            last_error = str(e)
            last_response = response if 'response' in dir() else ""
            result["input_tokens"] = input_tokens
            result["elapsed_ms"] = elapsed_ms
            log_llm_raw_output(
                case_id=case_id,
                batch_id=batch_id,
                batch_name=batch_config["name"],
                llm_response=last_response,
                input_tokens=input_tokens,
                output_tokens=0,
                elapsed_ms=elapsed_ms,
                success=False,
                parsed_node_count=0,
            )
            if attempt < MAX_RETRIES + BATCH4_STRUCT_RETRY - 1:
                delay = RETRY_BASE_DELAY * (2 ** attempt)
                if logger:
                    logger(f"    [RETRY] {batch_config['name']} retry {attempt+1}, waiting {delay:.0f}s...")
                time.sleep(delay)
            continue

    # All retries failed: try using the fallback result (keep it even if validation did not fully pass)
    if last_nodes and batch_id != "hyperparam":
        # When fallback nodes exist, mark as partial success (nodes may be incomplete)
        result["success"] = True
        result["nodes"] = last_nodes
        result["error"] = f"Structure validation did not fully pass; using fallback result ({len(last_nodes)} nodes)"
        bs = _get_batch_stats(batch_id)
        bs.add(input_tokens, _estimate_tokens(last_response), result["elapsed_ms"], True, len(last_nodes))
        ps = _get_paper_stats(case_id, paper.get("title", ""))
        ps.add_batch(batch_id, input_tokens, _estimate_tokens(last_response),
                     result["elapsed_ms"], True, len(last_nodes))
        _record_per_call(batch_id, case_id, input_tokens, _estimate_tokens(last_response),
                         result["elapsed_ms"], True, len(last_nodes))
        log_llm_raw_output(
            case_id=case_id, batch_id=batch_id, batch_name=batch_config["name"],
            llm_response=last_response, input_tokens=input_tokens,
            output_tokens=_estimate_tokens(last_response),
            elapsed_ms=result["elapsed_ms"], success=True,
            parsed_node_count=len(last_nodes),
        )
        return result

    result["error"] = last_error if last_error else "Maximum retries exhausted"
    result["success"] = False

    # Update failure statistics
    bs = _get_batch_stats(batch_id)
    bs.add(input_tokens, 0, result["elapsed_ms"], False, 0)
    ps = _get_paper_stats(case_id, paper.get("title", ""))
    ps.add_batch(batch_id, input_tokens, 0,
                  result["elapsed_ms"], False, 0)
    _record_per_call(batch_id, case_id, input_tokens,
                     0, result["elapsed_ms"], False, 0)

    return result


# ============================================================================
# Save Single-Batch JSON File
# ============================================================================

def save_batch_json(
    batch_config: dict,
    case_id: str,
    paper: dict,
    batch_result: dict,
):
    """Save the single-batch extraction result as an independent JSON file

    Output field rules:
      - All batches: case_id, paper_title, publish_year, publish_source, cite_count
      - Node batches: nodes (excluding hyperparam)
      - Hyperparameter batches: hyperparam (excluding nodes, batch_id, batch_name, is_node_batch,
                     extraction_stats, llm_raw_response)
    """
    subdir = batch_config["output_subdir"]
    batch_output_dir = os.path.join(V4_ROOT_DIR, subdir)
    os.makedirs(batch_output_dir, exist_ok=True)

    filename = f"{case_id}.json"
    filepath = os.path.join(batch_output_dir, filename)

    # Base fields: required in all batches
    doc = {
        "case_id": case_id,
        "paper_title": paper.get("title", ""),
        "publish_year": paper.get("year"),
        "publish_source": paper.get("journal", ""),
        "cite_count": paper.get("times_cited", 0),
    }

    is_node_batch = batch_config["is_node_batch"]

    # Node batches: include only nodes (excluding batch_id, batch_name, is_node_batch,
    #               extraction_stats, llm_raw_response, hyperparam)
    if is_node_batch:
        doc["prompt_file"] = batch_config["prompt_file"]
        doc["nodes"] = batch_result.get("nodes", [])

    # Hyperparameter batches: include only hyperparam (excluding nodes, batch_id, batch_name,
    #               is_node_batch, extraction_stats, llm_raw_response)
    else:
        doc["hyperparam"] = batch_result.get("hyperparam")

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)


# ============================================================================
# Single-Paper Processing (Internal Parallel: 4 Batches + Serial Hyperparameters)
# ============================================================================

def process_single_paper(
    paper: dict,
    llm_config: dict,
    logger,
    api_key_config: dict | None = None,
) -> dict | None:
    """
    Process a single paper:
    - Extract the PDF text (skip and return None if no PDF is found)
    - Extract hyperparameters (serial, run first)
    - Extract 4 node batches in parallel
    - Return the merged single-paper result

    case_id is taken from paper["case_id"] (i.e. the PDF subfolder name);
    it must be an objective identifier.
    """
    case_id = paper.get("case_id")
    if not case_id:
        raise ValueError("paper['case_id'] is empty; please check the PDF scan and metadata matching process.")

    title_short = (paper.get("title") or "Untitled")[:60]
    logger(f"  [Paper={case_id}] {title_short}...")

    # Extract PDF (skip the paper if no PDF is found)
    pdf_text = ""
    if paper.get("pdf_path") and os.path.exists(paper["pdf_path"]):
        pdf_text = extract_pdf_text(paper["pdf_path"])
        if pdf_text:
            logger(f"    PDF: {len(pdf_text)} characters")
        else:
            logger(f"    [WARN] PDF text extraction failed; skipping this paper")
            return None
    else:
        logger(f"    [SKIP] No PDF file found ({paper.get('title', '')[:40]}...); skipping this paper")
        return None

    # Prepare batch tasks
    node_batches = [b for b in BATCH_CONFIG if b["is_node_batch"]]
    hyperparam_batch = next((b for b in BATCH_CONFIG
                             if b["id"] == "hyperparam"), None)

    # Initialize paper result
    paper_result = {
        "case_id": case_id,
        "paper_title": paper.get("title", ""),
        "publish_year": paper.get("year"),
        "publish_source": paper.get("journal", ""),
        "cite_count": paper.get("times_cited", 0),
        "algorithm_hyperparameters": None,
        "training_config": None,
        "performance_metrics": None,
        "nodes": [],
        "edges": [],
    }

    # Step 1: Extract hyperparameters (serial, run first)
    if hyperparam_batch:
        logger(f"    >> Hyperparameter extraction...")
        hp_result = extract_single_batch(
            hyperparam_batch, paper, case_id, pdf_text, llm_config, api_key_config, logger)
        save_batch_json(hyperparam_batch, case_id, paper, hp_result)

        if hp_result["success"]:
            hp = hp_result["hyperparam"] or {}
            paper_result["algorithm_hyperparameters"] = hp.get(
                "algorithm_hyperparameters")
            paper_result["training_config"] = hp.get("training_config")
            paper_result["performance_metrics"] = hp.get("performance_metrics")
            logger(f"    [OK] Hyperparameters ({hp_result['elapsed_ms']/1000:.1f}s)")
        else:
            logger(f"    [FAIL] Hyperparameters: {hp_result['error']}")

    # Step 2: Extract 4 node batches in parallel
    with ThreadPoolExecutor(max_workers=BATCH_PARALLEL) as executor:
        futures = {
            executor.submit(
                extract_single_batch,
                batch_cfg, paper, case_id, pdf_text, llm_config, api_key_config, logger
            ): batch_cfg
            for batch_cfg in node_batches
        }

        for future in as_completed(futures):
            batch_cfg = futures[future]
            try:
                batch_result = future.result()

                save_batch_json(batch_cfg, case_id, paper, batch_result)

                if batch_result["success"]:
                    for n in batch_result["nodes"]:
                        paper_result["nodes"].append(n)
                    logger(f"    [OK] {batch_cfg['name']}: "
                           f"{len(batch_result['nodes'])} nodes "
                           f"({batch_result['elapsed_ms']/1000:.1f}s)")
                else:
                    logger(f"    [FAIL] {batch_cfg['name']}: "
                           f"{batch_result['error']}")

            except Exception as e:
                logger(f"    [EXC] {batch_cfg['name']}: {e}")
                save_batch_json(batch_cfg, case_id, paper, {
                    "success": False,
                    "error": str(e),
                    "input_tokens": 0,
                    "output_tokens": 0,
                    "elapsed_ms": 0,
                    "nodes": [],
                    "hyperparam": None,
                    "llm_response": "",
                    "llm_response_for_save": "",
                })

    logger(f"    Done: {case_id} total {len(paper_result['nodes'])} nodes")
    return paper_result


# ============================================================================
# Multi-Paper Parallel Processing (External Scheduler)
# ============================================================================

_global_results_lock = Lock()
_all_results: list[dict] = []


def run_papers_parallel(
    papers: list[dict],
    llm_config: dict,
    skip_existing: bool,
    logger,
    key_manager: RoundRobinKeyManager | None = None,
):
    """Process multiple papers in parallel; when key_manager is provided, the API Key is assigned by round-robin per paper"""
    total = len(papers)

    def process_one(idx: int, paper: dict) -> dict | None:
        case_id = paper.get("case_id")
        if not case_id:
            logger(f"[{idx+1}/{total}] [ERROR] case_id is empty, skipping: {paper.get('title','')[:40]}")
            return None

        # Assign API Key by paper index (ensuring the same paper always uses the same Key)
        api_key_config: dict | None = None
        if key_manager:
            assigned_key = key_manager.get_key_for_paper(idx)
            api_key_config = {
                "api_key": assigned_key,
                "base_url": llm_config.get("base_url", ""),
                "timeout": llm_config.get("timeout", 300),
            }
            logger(f"  [Key=Key{(idx % key_manager.total_keys) + 1}] {case_id}")

        # Skip already processed: check whether a JSON file for this case_id exists (any batch is enough)
        if skip_existing:
            # Check the first batch directory
            first_batch_dir = os.path.join(
                V4_ROOT_DIR,
                next(b["output_subdir"] for b in BATCH_CONFIG)
            )
            if os.path.exists(os.path.join(first_batch_dir, f"{case_id}.json")):
                logger(f"[{idx+1}/{total}] Skipping already-processed: {case_id}")
                return None

        try:
            result = process_single_paper(paper, llm_config, logger, api_key_config)
            # process_single_paper returns None when the PDF is missing or extraction failed;
            # the paper is already logged internally
            if result is None:
                logger(f"[{idx+1}/{total}] [SKIP] {case_id} "
                       f"{paper.get('title','')[:40]}: PDF missing or extraction failed")
                return None
            with _global_results_lock:
                _all_results.append(result)
            return result
        except Exception as e:
            logger(f"[{idx+1}/{total}] [ERROR] {case_id} "
                   f"{paper.get('title','')[:40]}: {e}")
            import traceback
            traceback.print_exc()
            return None

    with ThreadPoolExecutor(max_workers=PAPER_PARALLEL) as executor:
        futures = {executor.submit(process_one, i, p): (i, p)
                   for i, p in enumerate(papers)}
        for future in as_completed(futures):
            idx, paper = futures[future]
            try:
                result = future.result()
                if result is not None:
                    case_id = paper.get("case_id", "?")
                    title = (paper.get("title") or "")[:40]
                    logger(f"[{idx+1}/{total}] Done: {case_id} {title}")
                    # Save a checkpoint every 5 papers
                    if len(_all_results) % 5 == 0:
                        _save_checkpoint()
            except Exception as e:
                logger(f"[{idx+1}/{total}] [EXC] "
                       f"{paper.get('title','')[:40]}: {e}")


def _save_checkpoint():
    """Save a checkpoint"""
    ckpt_dir = os.path.join(V4_ROOT_DIR, "checkpoint")
    os.makedirs(ckpt_dir, exist_ok=True)
    ts = time.strftime("%Y%m%d_%H%M%S")
    ckpt_file = os.path.join(ckpt_dir, f"checkpoint_{ts}.json")
    with open(ckpt_file, "w", encoding="utf-8") as f:
        json.dump(_all_results, f, ensure_ascii=False, indent=2)


# ============================================================================
# Statistics Report Generation (same format as v3 for easy comparison)
# ============================================================================

def generate_stats_report() -> str:
    """Generate the Token / time analysis report (aligned with the v3 format)"""
    lines = []
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    lines.append("=" * 80)
    lines.append(f"V5 Token Consumption and Runtime Analysis Report")
    lines.append(f"Generated: {ts}")
    lines.append(f"LLM: {LLM_CONFIG.get('model','?')} @ {LLM_CONFIG.get('base_url','?')}")
    lines.append("=" * 80)

    # Global summary
    total_input = sum(s.total_input_tokens for s in _batch_stats.values())
    total_output = sum(s.total_output_tokens for s in _batch_stats.values())
    total_time = sum(s.total_time_ms for s in _batch_stats.values())
    total_calls = sum(s.call_count for s in _batch_stats.values())
    total_nodes = sum(s.total_nodes for s in _batch_stats.values())
    total_papers = len(_paper_stats)

    lines.append(f"\n[Global Summary]")
    lines.append(f"  Papers processed: {total_papers}")
    lines.append(f"  Total calls: {total_calls}")
    lines.append(f"  Total nodes extracted: {total_nodes}")
    lines.append(f"  Total input tokens: {total_input:,}")
    lines.append(f"  Total output tokens: {total_output:,}")
    lines.append(f"  Total token consumption: {total_input + total_output:,}")
    lines.append(f"  Total runtime: {total_time / 1000:.2f} seconds")
    if total_calls > 0:
        lines.append(f"  Average input tokens per call: {total_input / total_calls:.2f}")
        lines.append(f"  Average output tokens per call: {total_output / total_calls:.2f}")
        lines.append(f"  Average runtime per call: {total_time / total_calls / 1000:.2f} seconds")
    if total_papers > 0:
        lines.append(f"  Average tokens per paper: {(total_input+total_output)/total_papers:.2f}")
        lines.append(f"  Average runtime per paper: {total_time/total_papers/1000:.2f} seconds")

    # Sort by tokens (descending)
    sorted_by_tokens = sorted(_batch_stats.values(),
                              key=lambda s: s.total_input_tokens + s.total_output_tokens,
                              reverse=True)
    sorted_by_time = sorted(_batch_stats.values(),
                            key=lambda s: s.total_time_ms, reverse=True)

    # TOP - by tokens
    lines.append(f"\n{'=' * 80}")
    lines.append("[Batches - sorted by token consumption (descending)]")
    lines.append(f"{'Rank':<4} {'Batch':<35} {'Calls':>6} {'Success':>6} {'Failed':>6} "
                 f"{'InputTokens':>12} {'OutputTokens':>12} {'TotalTokens':>12} {'Time(s)':>10}")
    lines.append("-" * 110)
    for rank, s in enumerate(sorted_by_tokens, 1):
        rate = f"{s.success_count*100/s.call_count:.0f}%" if s.call_count > 0 else "N/A"
        lines.append(
            f"{rank:<4} {s.name:<35} {s.call_count:>6} {s.success_count:>6} "
            f"{s.fail_count:>6} {s.total_input_tokens:>12,} "
            f"{s.total_output_tokens:>12,} "
            f"{s.total_input_tokens + s.total_output_tokens:>12,} "
            f"{s.total_time_ms / 1000:>10.2f}"
        )

    # TOP - by runtime
    lines.append(f"\n{'=' * 80}")
    lines.append("[Batches - sorted by runtime (descending)]")
    lines.append(f"{'Rank':<4} {'Batch':<35} {'Calls':>6} {'Total time(s)':>12} "
                 f"{'Avg time(ms)':>14} {'InputTokens':>12} {'OutputTokens':>12} {'Nodes':>8}")
    lines.append("-" * 110)
    for rank, s in enumerate(sorted_by_time, 1):
        lines.append(
            f"{rank:<4} {s.name:<35} {s.call_count:>6} "
            f"{s.total_time_ms / 1000:>12.2f} {s.total_time_ms / s.call_count if s.call_count > 0 else 0:>14.1f} "
            f"{s.total_input_tokens:>12,} {s.total_output_tokens:>12,} "
            f"{s.total_nodes:>8}"
        )

    # Per-paper statistics
    if _paper_stats:
        sorted_papers = sorted(_paper_stats.values(),
                               key=lambda p: p.total_input_tokens + p.total_output_tokens,
                               reverse=True)
        lines.append(f"\n{'=' * 80}")
        lines.append("[Per-Paper Statistics - sorted by total tokens (descending)]")
        lines.append(f"{'case_id':<10} {'Title (first 40 chars)':<42} {'Nodes':>6} "
                     f"{'InputTokens':>12} {'OutputTokens':>12} {'TotalTokens':>12} {'Time(s)':>10}")
        lines.append("-" * 110)
        for p in sorted_papers:
            title = (p.title or "")[:40]
            lines.append(
                f"{p.case_id:<10} {title:<42} {p.node_count:>6} "
                f"{p.total_input_tokens:>12,} {p.total_output_tokens:>12,} "
                f"{p.total_input_tokens + p.total_output_tokens:>12,} "
                f"{p.total_time_ms / 1000:>10.2f}"
            )
        avg_tokens = sum(p.total_input_tokens + p.total_output_tokens
                         for p in sorted_papers) / len(sorted_papers)
        avg_time = sum(p.total_time_ms for p in sorted_papers) / len(sorted_papers)
        lines.append("-" * 110)
        lines.append(f"{'Average':<10} {'':<42} {'':<6} {'':<12} {'':<12} "
                     f"{avg_tokens:>12.2f} {avg_time / 1000:>10.2f}")

    return "\n".join(lines)


def save_stats_and_report():
    """Save statistics JSON and text report"""
    ts = time.strftime("%Y%m%d_%H%M%S")

    # Statistics JSON
    total_input = sum(s.total_input_tokens for s in _batch_stats.values())
    total_output = sum(s.total_output_tokens for s in _batch_stats.values())
    total_time = sum(s.total_time_ms for s in _batch_stats.values())

    stats_data = {
        "generated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total_papers": len(_paper_stats),
        "total_calls": sum(s.call_count for s in _batch_stats.values()),
        "total_input_tokens": total_input,
        "total_output_tokens": total_output,
        "total_tokens": total_input + total_output,
        "total_time_ms": total_time,
        "batch_stats": [s.to_dict() for s in _batch_stats.values()],
        "paper_stats": [p.to_dict() for p in _paper_stats.values()],
        "per_call_stats": _per_call_stats,
    }

    stats_file = os.path.join(V4_ROOT_DIR, f"v5_stats_data_{ts}.json")
    with open(stats_file, "w", encoding="utf-8") as f:
        json.dump(stats_data, f, ensure_ascii=False, indent=2)

    # Text report
    report = generate_stats_report()
    report_file = os.path.join(V4_ROOT_DIR, f"v5_stats_report_{ts}.txt")
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(report)

    return stats_file, report_file


# ============================================================================
# Main Program
# ============================================================================

def main():
    global V4_ROOT_DIR, LLM_CONFIG, PROMPTS_V4_DIR, PAPER_PARALLEL, BATCH_PARALLEL, NODE_ZERO_RETRY, RETRY_BASE_DELAY

    parser = argparse.ArgumentParser(
        description="Literature Knowledge Graph Information Extraction Program V5 (v5 merged prompts + parallel extraction + enhanced JSON parsing)"
    )
    parser.add_argument("--metadata", type=str, default=METADATA_EXCEL_PATH,
                        help="Metadata Excel file")
    parser.add_argument("--pdf-root", type=str, default=PDF_ROOT_DIR,
                        help="PDF root directory")
    parser.add_argument("--output-root", type=str, default=V4_ROOT_DIR,
                        help="Output root directory")
    parser.add_argument("--prompts-dir", type=str, default=PROMPTS_V4_DIR,
                        help="v4 prompt directory")
    parser.add_argument("--max-papers", type=int, default=0,
                        help="Maximum number of papers to process (0 = all)")
    parser.add_argument("--paper-parallel", type=int, default=PAPER_PARALLEL,
                        help="Paper parallelism (default 10; recommend >= API Key count)")
    parser.add_argument("--batch-parallel", type=int, default=BATCH_PARALLEL,
                        help="Node-batch parallelism")
    parser.add_argument("--retry-base-delay", type=float, default=RETRY_BASE_DELAY,
                        help=f"Base retry delay in seconds (default {RETRY_BASE_DELAY}; uses exponential backoff)")
    parser.add_argument("--node-zero-retry", type=int, default=NODE_ZERO_RETRY,
                        help="Retry count when nodes are parsed to 0 (default 0; 0 = disabled)")
    parser.add_argument("--api-key", type=str, default="",
                        help="LLM API Key (single-key mode)")
    parser.add_argument("--api-keys", type=str, default="",
                        help="Multiple LLM API Keys, separated by | (e.g. k1|k2|k3); round-robin per paper")
    parser.add_argument("--provider", type=str, default="gemini",
                        choices=["openai", "deepseek", "zhipu", "gemini"])
    parser.add_argument("--model", type=str,
                        default="gemini-3.5-flash")
    parser.add_argument("--base-url", type=str, default=None)
    parser.add_argument("--temperature", type=float, default=None,
                        help="LLM temperature (0 = deterministic, 0.7 = creative; default 0.0)")
    parser.add_argument("--skip-existing", action="store_true",
                        help="Skip already-extracted papers")
    args = parser.parse_args()

    V4_ROOT_DIR = args.output_root
    PROMPTS_V4_DIR = args.prompts_dir
    PAPER_PARALLEL = args.paper_parallel
    BATCH_PARALLEL = args.batch_parallel
    NODE_ZERO_RETRY = args.node_zero_retry
    RETRY_BASE_DELAY = args.retry_base_delay

    os.makedirs(V4_ROOT_DIR, exist_ok=True)

    LLM_CONFIG["provider"] = args.provider
    LLM_CONFIG["model"] = args.model
    if args.base_url:
        LLM_CONFIG["base_url"] = args.base_url
    if args.temperature is not None:
        LLM_CONFIG["temperature"] = args.temperature
    if LLM_CONFIG["provider"] == "gemini" and not LLM_CONFIG.get("base_url"):
        LLM_CONFIG["base_url"] = os.environ.get("BFGA_LLM_API_URL", "https://YOUR.LLM.ENDPOINT/")

    # Multi-key mode initialization (defaults from MULTI_API_KEYS; --api-keys overrides)
    key_manager: RoundRobinKeyManager | None = None
    keys: list[str] = []
    if args.api_keys:
        keys = [k.strip() for k in args.api_keys.split("|") if k.strip()]
    elif MULTI_API_KEYS:
        keys = [k.strip() for k in MULTI_API_KEYS if k.strip()]

    if not keys:
        print("Error: No LLM API Key configured! Please configure MULTI_API_KEYS in code or pass --api-keys.")
        return
    key_manager = RoundRobinKeyManager(keys)
    print(f"[Multi-key mode] {len(keys)} keys total; round-robin per paper")
    for i, k in enumerate(keys):
        print(f"  Key {i+1}: {k[:10]}...{k[-4:]}")

    if not os.path.exists(PROMPTS_V4_DIR):
        print(f"Error: v5 prompt directory does not exist: {PROMPTS_V4_DIR}")
        return

    # Create each batch's output subdirectory
    for batch in BATCH_CONFIG:
        subdir = os.path.join(V4_ROOT_DIR, batch["output_subdir"])
        os.makedirs(subdir, exist_ok=True)

    # Create final-merge directory (RELATIVE PATH): ./output/final_merged/   <-- RELATIVE PATH
    final_dir = os.path.join(V4_ROOT_DIR, "final_merged")
    os.makedirs(final_dir, exist_ok=True)

    # Create LLM raw-output log directory
    os.makedirs(LLM_LOG_DIR, exist_ok=True)
    print(f"LLM log directory:  {LLM_LOG_DIR}")

    # ========== Print configuration ==========
    print("=" * 70)
    print("Literature Knowledge Graph Information Extraction Program V5 (v5 merged prompts + parallel extraction + enhanced JSON parsing)")
    print("=" * 70)
    print(f"Metadata file:   {METADATA_EXCEL_PATH}")
    print(f"PDF root dir:    {PDF_ROOT_DIR}")
    print(f"Output root dir: {V4_ROOT_DIR}")
    print(f"Prompt dir:      {PROMPTS_V4_DIR}")
    print(f"LLM:             {LLM_CONFIG['provider']} / {LLM_CONFIG['model']} / temperature={LLM_CONFIG.get('temperature', 0.0)}")
    print(f"API Keys:        {key_manager.total_keys} keys (multi-key round-robin mode)")
    print(f"Paper parallel:  {PAPER_PARALLEL}")
    print(f"Retry delay:     Exponential backoff, base={RETRY_BASE_DELAY}s (Nth retry delay = {RETRY_BASE_DELAY}*2^N seconds)")
    print(f"Max retries:     {MAX_RETRIES}")
    print(f"Batch parallel:  {BATCH_PARALLEL}")
    print(f"Node-zero retry: {NODE_ZERO_RETRY} times")
    print(f"Number of batches: {len(BATCH_CONFIG)}")
    print("=" * 70)

    print("\nBatch configuration:")
    for batch in BATCH_CONFIG:
        prompt_path = os.path.join(PROMPTS_V4_DIR, batch["prompt_file"])
        exists = os.path.exists(prompt_path)
        status = "OK" if exists else "MISSING"
        node_tag = "[node]" if batch["is_node_batch"] else "[hyperparameter]"
        print(f"  [{status}] {node_tag} {batch['id']:12s} | {batch['name']:30s} "
              f"| -> {batch['output_subdir']}")

    # ========== Read metadata ==========
    print("\n[Step 1] Reading metadata...")
    papers = load_metadata_from_excel(METADATA_EXCEL_PATH)
    print(f"  Total {len(papers)} papers (with title: {sum(1 for p in papers if p['title'])})")

    # ========== Scan PDFs ==========
    print("\n[Step 2] Scanning PDFs...")
    pdfs = scan_pdf_files(PDF_ROOT_DIR)
    print(f"  Total {len(pdfs)} PDFs scanned")

    # ========== Match PDFs ==========
    print("\n[Step 3] Matching PDFs to metadata...")
    papers, match_results, unmatched = match_pdfs_to_metadata(papers, pdfs)
    matched = sum(1 for m in match_results if m["status"] == "matched")
    print(f"  Matched: {matched} | Unmatched: {len(unmatched)}")

    # Filter out papers with no PDF (avoid idle processing)
    papers_with_pdf = [p for p in papers if p.get("pdf_path") and p.get("case_id")]
    skipped_no_pdf = len(papers) - len(papers_with_pdf)
    if skipped_no_pdf > 0:
        print(f"  [INFO] Skipping papers without PDF: {skipped_no_pdf} papers (will skip processing)")
    papers = papers_with_pdf

    if unmatched:
        for up in unmatched[:5]:
            print(f"    Unmatched: {up['pdf']['pdf_title'][:50]} "
                  f"best score={up['best_score']:.2f}")

    if args.max_papers > 0:
        papers = papers[:args.max_papers]
        print(f"  Limit processing: {args.max_papers} papers")

    # ========== LLM raw-output log initialization ==========
    # After all papers are matched, compute the case_id range (min/max) and generate a unique log filename
    os.makedirs(LLM_LOG_DIR, exist_ok=True)

    matched_papers = [p for p in papers if p.get("case_id")]
    if matched_papers:
        all_case_ids = sorted([p["case_id"] for p in matched_papers],
                              key=lambda x: x.lower())
        case_id_min = all_case_ids[0]
        case_id_max = all_case_ids[-1]
    else:
        case_id_min = case_id_max = "unknown"

    log_base_name = f"{case_id_min}+{case_id_max}+LLM_raw_output.md"
    global_log_path = os.path.join(LLM_LOG_DIR, log_base_name)

    # Determine whether to create new or append: append if file exists, create otherwise
    file_mode = "a" if os.path.exists(global_log_path) else "w"

    # Compute the run sequence number for this invocation: count existing H1 headers +1
    run_seq = 1
    if file_mode == "a":
        try:
            with open(global_log_path, "r", encoding="utf-8") as _f:
                lines = _f.readlines()
            # Count H1 headers (lines starting with "# Run")
            run_seq = sum(1 for line in lines if line.startswith("# Run"))
            run_seq += 1
        except Exception:
            run_seq = 1

    # Write the H1 header for this run
    run_ts = time.strftime("%Y-%m-%d %H:%M:%S")
    header = (
        f"# Run {run_seq} | {run_ts}\n\n"
        f"**case_id range:** `{case_id_min}` ~ `{case_id_max}` | "
        f"**Papers:** {len(matched_papers)}\n\n"
        f"---\n\n"
    )
    with open(global_log_path, "a", encoding="utf-8") as _f:
        _f.write(header)

    # Set global variables for use by log_llm_raw_output()
    global _llm_log_file_path, _llm_run_seq
    _llm_log_file_path = global_log_path
    _llm_run_seq = run_seq
    print(f"LLM log: {global_log_path}  ({'append' if file_mode == 'a' else 'new'}, run #{run_seq})")

    # ========== Run log ==========
    log_lock = Lock()
    ts = time.strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(V4_ROOT_DIR, f"v4_run_{ts}.log")

    def logger(msg: str):
        ts2 = time.strftime("%H:%M:%S")
        line = f"[{ts2}] {msg}"
        print(line)
        with log_lock:
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(line + "\n")

    logger(f"Starting to process {len(papers)} papers...")

    # ========== Parallel processing ==========
    run_papers_parallel(
        papers=papers,
        llm_config=LLM_CONFIG,
        skip_existing=args.skip_existing,
        logger=logger,
        key_manager=key_manager,
    )

    # Save merged JSON (same output format as v3)
    final_file = os.path.join(final_dir, "final_merged.json")
    with open(final_file, "w", encoding="utf-8") as f:
        json.dump(_all_results, f, ensure_ascii=False, indent=2)

    # Save statistics
    stats_file, report_file = save_stats_and_report()
    report = generate_stats_report()

    # ========== Print summary ==========
    print("\n" + "=" * 70)
    print(report)
    print("=" * 70)
    print(f"\nProcessing complete!")
    print(f"  This run:        {len(_all_results)} papers")
    print(f"  Final merged:    {final_file}")
    print(f"  Stats JSON:     {stats_file}")
    print(f"  Stats report:   {report_file}")
    print(f"  Run log:        {log_file}")
    if _llm_log_file_path:
        print(f"  LLM raw log:    {_llm_log_file_path}")
    print(f"\nPer-batch independent JSON files are saved in their respective subdirectories.")
    if key_manager:
        usage = key_manager.usage_report()
        total_assigned = sum(usage.values())
        print(f"\nAPI Key usage statistics (by paper assignment, total {total_assigned} papers):")
        if total_assigned > 0:
            for i, k in enumerate(keys):
                count = usage.get(k, 0)
                print(f"  Key {i+1} ({k[:10]}...{k[-4:]}): {count} papers ({count/total_assigned*100:.0f}%)")
        else:
            print("  (No papers assigned)")
    print(f"To re-merge, please run: python zotero_knowledge_graph_extractor_v4_merge.py")
    print("=" * 70)


if __name__ == "__main__":
    main()
