# -*- coding: utf-8 -*-
r"""
Literature knowledge-graph edge-extraction program V8 (multi-agent concurrency + LLM prompt extraction + visualization)

========================================================================
Functions (main program flow):
  1. Read the merged-node JSON (containing the node arrays of multiple papers)
  2. Match each paper with its corresponding PDF (via metadata Excel + PDF_ROOT_DIR)
  3. Call potential_edge_generation.py to generate the "candidate edge-node json array full set"
  4. Call edge_02_split.py to filter candidate edges where edge_group="02-causal edge" and edge_description=null
     -> split into multiple 02-causal-edge JSON fragments
  5. Call edge_03_split.py to filter candidate edges where edge_group="03-evidence edge" and edge_description=null
     -> split into multiple 03-evidence-edge JSON fragments
  6. Call edge_02_prompt.py to convert 02-causal-edge fragments into LLM prompt Markdown
     Call edge_03_prompt.py to convert 03-evidence-edge fragments into LLM prompt Markdown
  7. Concurrently call the LLM (with retry-on-failure), iterate through papers' PDFs, extract 02-causal and 03-evidence edge descriptions
     -> output "02 causal-edge json collection" to edge_relations-by_group/02-causal edge/
     -> output "03 evidence-edge json collection" to edge_relations-by_group/03-evidence edge/
  8. Back-fill the extraction result into the "candidate edge-node json array full set" edge_description field
     -> count the edge_description=null edges and output a txt notes file
  9. Delete the edge_description=null edges from the candidate edge set and generate the "extracted edge json array"
     -> save to final_merge/merged_edges/
  10. Call potential_edge_plot to generate an HTML graph visualization of the extracted edges

Output directory structure:
  - v7_version/edge_relations-by_group/02-causal edge/       -> independent JSON per 02-causal batch
  - v7_version/edge_relations-by_group/03-evidence edge/    -> independent JSON per 03-evidence batch
  - v7_version/edge_relations-by_group/notes_file.txt       -> edge_description=null statistics
  - v7_version/edge_relations-by_group/*.html               -> token / time visualization report
  - v7_version/final_merge/B0-edge_merge/                   -> final extracted-edge merged file (with per-batch merged outputs)
  - v7_version/final_merge/B0-edge_merge/*.html             -> extracted-edge HTML graph
  - v7_version/batch_progress/[filename]_progress.json      -> per-batch execution progress (for resuming)
  - v7_version/edge_relations-by_group/batch_run_logs/      -> per-batch execution log

========================================================================
Batch execution strategy (handling 1000+ large-volume papers)

  Design goal:
    - When the literature volume is very large (e.g. 1000+), a single run can easily be interrupted by API token exhaustion
    - Interruption causes the consumed tokens to be wasted
    - Therefore, papers are automatically split into batches of BATCH_SIZE (default 500) per batch; each batch is completed and saved independently

  Progress tracking:
    - Progress file: v7_version/batch_progress/[input filename]_progress.json
    - Records each batch's done state, case_id range, call count, extracted-edge count, completion time
    - Auto-persisted at the end of every run

  Resuming from a checkpoint:
    - Re-running this program will automatically read the progress file
    - Only batches with done=false will run
    - If a batch is interrupted, it is NOT marked done; the next run will retry it
    - The Step 9 merged output file is named per batch, automatically merging existing batch data with new batch data

  Usage:
    1) First run (process the first 500 papers):
       python zotero_knowledge_graph_edge_extractor_v8.py
    2) Continue (starting from paper 501):
       python zotero_knowledge_graph_edge_extractor_v8.py
       (automatically skips completed batches and runs the remaining ones)
    3) Run a specific batch only (manual selection):
       python zotero_knowledge_graph_edge_extractor_v8.py --only-batch 1
    4) Show current progress (no processing):
       python zotero_knowledge_graph_edge_extractor_v8.py --show-progress
       # or shorthand:
       python zotero_knowledge_graph_edge_extractor_v8.py --status
    5) Reset progress (start over):
       python zotero_knowledge_graph_edge_extractor_v8.py --reset-progress
    6) Run only N batches this time (save tokens):
       python zotero_knowledge_graph_edge_extractor_v8.py --max-batches 1
    7) Custom batch size:
       python zotero_knowledge_graph_edge_extractor_v8.py --batch-size 200

  Recovery from exceptions:
    - Ctrl+C interruption: the current batch is not marked done; the next run will automatically retry it
    - API quota exhaustion: check the completed-batch progress in _progress.json
    - System crash: the progress file has been persisted, re-run to continue
========================================================================

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
from typing import Optional, Union
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock, Semaphore, Event

# Edge-extraction stats aggregation utility (used to output the JSON summary of token / call distribution after extraction completes)
# Must be imported before the program entry; importing inside a function would be affected by the running directory and may block cleanup when the module is missing.
try:
    from zotero_edge_extractor_plot_v5 import build_stats_data  # noqa: E402
except ImportError:
    # Fallback: allow the program to terminate cleanly even if the module is not found (the stats JSON is a by-product and does not affect the main flow)
    build_stats_data = None
    print("[Warning] zotero_edge_extractor_plot_v5 not found; the stats JSON will be skipped")

# ============================================================================
# User configuration
# ============================================================================

# Input metadata Excel path (RELATIVE PATH placeholder):
# ./input/metadata.xls   <-- RELATIVE PATH: Excel file with paper metadata (title, DOI, journal, year, citations)
METADATA_EXCEL_PATH = r"./input/metadata.xls"

# Input PDF root directory (RELATIVE PATH placeholder):
# ./input/pdfs/   <-- RELATIVE PATH: folder whose subfolders are case_ids; each subfolder contains the PDF for that paper
PDF_ROOT_DIR = r"./input/pdfs"

# v8 output root directory (RELATIVE PATH placeholder):
# ./output/   <-- RELATIVE PATH
V8_ROOT_DIR = r"./output"

# Input: merged-node JSON (RELATIVE PATH placeholder):
# ./output/final_merged/A0-node_merged/[...].json   <-- RELATIVE PATH
MERGED_NODES_INPUT = r"./output/final_merged/A0-node_merged/[2277EAKD][ZZ36KWCF]_merged_nodes_conformance_audit.json"

# Edge-output directory (Step 7)
EDGE_OUTPUT_ROOT = os.path.join(V8_ROOT_DIR, "edges-grouped")
EDGE_02_OUTPUT_DIR = os.path.join(EDGE_OUTPUT_ROOT, "02-causal-edges")
EDGE_03_OUTPUT_DIR = os.path.join(EDGE_OUTPUT_ROOT, "03-evidence-edges")

# Temp directories (Steps 3-6)
CANDIDATE_EDGE_DIR = os.path.join(V8_ROOT_DIR, "edge-node-pairs-tmp", "00-candidate-edges-json")
EDGE_02_SPLIT_DIR = os.path.join(V8_ROOT_DIR, "edge-node-pairs-tmp", "02-causal-edges-json")
EDGE_03_SPLIT_DIR = os.path.join(V8_ROOT_DIR, "edge-node-pairs-tmp", "03-evidence-edges-json")
EDGE_02_PROMPT_DIR = os.path.join(V8_ROOT_DIR, "edge-prompts-tmp", "02-causal-edge-prompts")
EDGE_03_PROMPT_DIR = os.path.join(V8_ROOT_DIR, "edge-prompts-tmp", "03-evidence-edge-prompts")

# Final-merged directory (Step 9)
FINAL_EDGE_DIR = os.path.join(V8_ROOT_DIR, "final_merged", "B0-edges_merged")

# ============================================================
# Batch-execution configuration (handles large-volume papers and prevents token waste from a single-run interruption)
# ============================================================
BATCH_SIZE = 500               # Papers per batch (auto-splits if exceeded)
PROGRESS_DIR = os.path.join(V8_ROOT_DIR, "batch_progress")  # Directory for progress files


# ============================================================
# Progress-tracking system (thread-safe)
# ============================================================

_progress_lock = Lock()
# In-memory progress state
_progress_state: dict = {
    "run_id": "",          # Unique ID for this run (timestamp)
    "total_papers": 0,     # Total paper count
    "batch_size": 0,      # Batch size
    "batches": {},        # {batch_index: {case_ids: [...], done: bool, llm_calls: int, ...}}
    "all_done": False,
    "created_at": "",
    "last_updated": "",
}


def _progress_file_path() -> str:
    """Generate the progress-file path from the input filename"""
    os.makedirs(PROGRESS_DIR, exist_ok=True)
    base = os.path.splitext(os.path.basename(MERGED_NODES_INPUT))[0]
    return os.path.join(PROGRESS_DIR, f"{base}_progress.json")


def load_progress() -> dict:
    """Load the progress file from disk (called when resuming from a checkpoint)"""
    pf = _progress_file_path()
    if os.path.exists(pf):
        try:
            with open(pf, "r", encoding="utf-8") as f:
                data = json.load(f)
            print(f"[Progress] Detected existing progress file: {pf}")
            _done_batches = [b for b in data.get("batches", {}).values() if b.get("done")]
            print(f"       Completed batches: {len(_done_batches)}, remaining: {len(data.get('batches', {})) - len(_done_batches)}")
            return data
        except Exception as e:
            print(f"[Progress] Failed to load progress file: {e}; starting over")
    return {}


def save_progress(state: dict) -> None:
    """Persist the progress state to disk (called after each batch completes)"""
    pf = _progress_file_path()
    state["last_updated"] = time.strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(pf, "w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"[Progress] Failed to save progress file: {e}")


def init_progress_state(total_papers: int) -> dict:
    """Initialize the progress state: split into batches"""
    state = {
        "run_id": time.strftime("%Y%m%d_%H%M%S"),
        "total_papers": total_papers,
        "batch_size": BATCH_SIZE,
        "batches": {},
        "all_done": False,
        "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "last_updated": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    # Split into batches of BATCH_SIZE
    for i in range(0, total_papers, BATCH_SIZE):
        batch_idx = i // BATCH_SIZE
        state["batches"][batch_idx] = {
            "batch_index": batch_idx,
            "case_ids": [],          # Filled during processing
            "done": False,
            "llm_calls": 0,
            "edges_extracted": 0,
            "completed_at": None,
        }
    return state


def get_pending_batch(state: dict) -> Optional[int]:
    """Get the index of the first not-yet-completed batch; returns None if all are done"""
    for idx in sorted(state["batches"].keys()):
        if not state["batches"][idx].get("done", False):
            return idx
    return None


def mark_batch_done(state: dict, batch_idx: int,
                    case_ids: list[str], llm_calls: int, edges_extracted: int) -> None:
    """Mark the given batch as completed and save progress"""
    with _progress_lock:
        state["batches"][batch_idx]["done"] = True
        state["batches"][batch_idx]["case_ids"] = case_ids
        state["batches"][batch_idx]["llm_calls"] = llm_calls
        state["batches"][batch_idx]["edges_extracted"] = edges_extracted
        state["batches"][batch_idx]["completed_at"] = time.strftime("%Y-%m-%d %H:%M:%S")
        # check whether all are done
        all_done = all(b.get("done", False) for b in state["batches"].values())
        state["all_done"] = all_done
    save_progress(state)
    done_count = sum(1 for b in state["batches"].values() if b.get("done"))
    print(f"[Progress] Batch {batch_idx} marked complete ({done_count}/{len(state['batches'])} batches)")


# ============================================================
# Progress log utilities
# ============================================================

def _save_batch_log(batch_idx: int, content: str, log_type: str = "log") -> None:
    """Save the batch run log to a standalone file"""
    batch_log_dir = os.path.join(EDGE_OUTPUT_ROOT, "batch_run_logs")
    os.makedirs(batch_log_dir, exist_ok=True)
    ts = time.strftime("%Y%m%d_%H%M%S")
    # find current run_id
    run_id = _progress_state.get("run_id", ts)
    fname = f"batch{batch_idx:03d}_{run_id}_{log_type}.txt"
    fpath = os.path.join(batch_log_dir, fname)
    try:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception:
        pass


# ============================================================
# Concurrency configuration
# ============================================================
# 10 Keys x 3 Concurrency = global cap of 30 (fully utilize all API keys)
# Scheduling strategy: All edge types (02-causal edges / 03-evidence edges) uniformly use gemini-3.5-flash
# ============================================================
PROMPT_PARALLEL = 10          # Global concurrency cap (number of prompt files processed simultaneously = number of keys)
PER_KEY_LIMIT = 1             # Max concurrent requests held by each API Key at the same time
                             #   Note: the original 3 made the 10 keys look "fake-added" -- multiple requests all hitting the same key
                             #   would trigger 429 / rate-limiting; in practice only 2~3 of the 10 keys really carried the load.
                             #   After changing to 1, each of the 10 keys truly runs 1 request at the same time = 10 real concurrent paths.
LLM_RETRIES = 3             # Max retries after an LLM call failure (initial 1 + up to 2 retries)
N_SPLIT = 20                 # Max number of edges per json fragment

# ============================================================
# Model configuration
# ============================================================
# All edge types (02-causal edges / 03-evidence edges) use the same model
# ============================================================
MODEL_EDGE_02   = "gemini-3.5-flash"      # Unified model for 02-causal edges / 03-evidence edges

LLM_CONFIG = {
    "provider": "gemini",
    "base_url": os.environ.get("BFGA_LLM_API_URL", "https://YOUR.LLM.ENDPOINT/"),
    "timeout": 300,
    "temperature": 0.0,
}

# IMPORTANT: Provide your own API keys before running. The list below should be filled with valid keys.
MULTI_API_KEYS: list[str] = []


class GlobalRateLimiter:
    """
    Global rate limiter: controls the maximum concurrent requests sent to the LLM server.
    When a connection error (e.g. WinError 10054) is detected, automatically triggers a global slowdown -
    pauses all concurrent requests, waits for recovery, and then continues, avoiding cascading
    collapse caused by "retry-on-failure storms".
    """

    def __init__(self, max_concurrent: int = 10):
        self._sem = Semaphore(max_concurrent)
        self._max = max_concurrent
        self._lock = Lock()
        self._retrying_count = 0
        self._retrying_lock = Lock()

    def acquire(self):
        self._sem.acquire()

    def release(self):
        self._sem.release()

    def report_error(self):
        """Report a connection error, trigger global slowdown (pause new requests)"""
        with self._retrying_lock:
            self._retrying_count += 1

    def is_degraded(self) -> bool:
        with self._retrying_lock:
            return self._retrying_count >= 2

    def clear_errors(self):
        with self._retrying_lock:
            self._retrying_count = 0

    def wait_if_degraded(self):
        """If in a degraded state, wait some time before continuing"""
        with self._retrying_lock:
            count = self._retrying_count
        if count >= 2:
            # Slow down: wait for the server to recover
            wait_time = min(count * 15, 120)
            print(f"  [RateLimiter] Detected {count} connection errors, entering slowdown wait {wait_time}s...")
            time.sleep(wait_time)
            with self._retrying_lock:
                self._retrying_count = 0


class RoundRobinKeyManager:
    """
    Thread-safe key manager that supports per-key rate limiting (max N concurrent requests per key).

    Key design (avoid "fake" concurrency):
        The old get_key() scanned all keys and broke on the first "full slot",
        causing all threads to pile tasks onto key[0] while the other 9 keys sat idle,
        producing "fake 10-key, but only 1 key in use" pseudo-parallelism.

        The new implementation uses a **true round-robin + slot-aware** hybrid scheduler:
          1) acquire() only selects the subset of keys with the most remaining slots
             (avoiding piling tasks into an already-full key).
          2) Within that subset, an atomic round-robin cursor _rr_cursor picks the next
             key, ensuring 10 keys are evenly distributed under high concurrency.
          3) Key selection + slot occupancy + usage accounting are all done under one
             lock, keeping external state consistent.
    """

    def __init__(self, keys: list[str], per_key_limit: int = 1):
        self._keys = keys
        self._lock = Lock()
        self._usage: dict[str, int] = {}
        self._sems: list[Semaphore] = [Semaphore(per_key_limit) for _ in keys]
        self._per_key_limit = per_key_limit
        # Round-robin cursor: evenly distribute within the "most remaining slots" key subset.
        self._rr_cursor = 0

    def acquire(self) -> tuple[str, int]:
        """
        Atomic operation: under the lock, complete "balanced key selection + occupy one concurrent slot for that key".

        Scheduling strategy (true concurrency):
          a) Scan all keys, pick the subset best_idxs with the most remaining slots;
          b) Within best_idxs, take the key by the round-robin cursor, cursor +1 (mod subset size),
             so the next call under the same situation automatically lands on the next key;
          c) When the subset is empty (all keys are full), fall back to acquiring the key with the largest _value.

        Returns:
            (key, key_idx) -- the caller must eventually call release(key_idx).
        """
        with self._lock:
            best_free = -1
            best_idxs: list[int] = []
            for i in range(len(self._keys)):
                free = self._sems[i]._value
                if free > best_free:
                    best_free = free
                    best_idxs = [i]
                elif free == best_free:
                    best_idxs.append(i)

            if best_idxs:
                m = len(best_idxs)
                pos = self._rr_cursor % m
                key_idx = best_idxs[pos]
                self._rr_cursor = (self._rr_cursor + 1) % 1_000_003
            else:
                # fallback: all keys are full, pick the key with the largest _value,
                # the acquire below will block the thread as expected.
                key_idx = max(range(len(self._keys)),
                              key=lambda i: self._sems[i]._value)

            key = self._keys[key_idx]
            self._usage[key] = self._usage.get(key, 0) + 1
            self._sems[key_idx].acquire()
            return key, key_idx

    def get_key_for_paper(self, paper_index: int) -> str:
        """
        Stable mapping from paper_index to a fixed key (the same paper always uses the same key),
        still preferring the candidate with the most remaining slots, ensuring we never over-block
        on a full specified key.
        """
        with self._lock:
            n = len(self._keys)
            start = paper_index % n
            best_idx = start
            best_free = self._sems[start]._value
            for offset in range(1, n):
                i = (start + offset) % n
                free = self._sems[i]._value
                if free > best_free:
                    best_free = free
                    best_idx = i
            key = self._keys[best_idx]
            self._usage[key] = self._usage.get(key, 0) + 1
            return key

    def release(self, key_idx: int):
        """Release one concurrent slot of the specified key index."""
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


# Global statistics (thread-safe)

_stats_lock = Lock()
_edge02_stats: dict = {}
_edge03_stats: dict = {}    
_prompt_stats: list[dict] = []


def _record_prompt_stat(paper_id: str, edge_type: str, success: bool,
                         input_tokens: int, output_tokens: int,
                         total_tokens: int, elapsed_ms: int,
                         edge_count: int, error: str = ""):
    with _stats_lock:
        _prompt_stats.append({
            "paper_id": paper_id,
            "edge_type": edge_type,
            "success": success,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "total_tokens": total_tokens,
            "elapsed_ms": elapsed_ms,
            "edge_count": edge_count,
            "error": error,
        })


# Utility functions

def _clean_dir(dir_path: str) -> None:
    """Remove all files in the directory (used to clean up old split/prompt files and avoid leftovers)"""
    if os.path.isdir(dir_path):
        for f in os.listdir(dir_path):
            fpath = os.path.join(dir_path, f)
            if os.path.isfile(fpath):
                os.remove(fpath)


def _estimate_tokens(text: str) -> int:
    chinese = sum(1 for c in text if '\u4e00' <= c <= '\u9fff' or '\u3000' <= c <= '\u303f')
    english = len(text) - chinese
    return int(chinese * 2 + english * 0.25)


def load_prompt_file(filepath: str) -> str:
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Prompt file does not exist: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


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


# PDF text extraction

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


# ============================================================
# Status display utility (based on the existing load_progress / save_progress system)
# ============================================================

def _print_progress_status_verbose(state: dict, input_file: str = "") -> None:
    """Print the current batch progress status in detail, used by the --status command"""
    print("=" * 70)
    print("[Edge-relation extraction progress status]")
    print("=" * 70)
    if input_file:
        print(f"Input file:    {input_file}")
    if not state or not state.get("batches"):
        print("Progress:      No batches initialized yet (please run at least once first)")
        print("=" * 70)
        return

    print(f"Run ID:        {state.get('run_id', 'N/A')}")
    print(f"Batch size:    {state.get('batch_size', 'N/A')}")
    print(f"Total papers:  {state.get('total_papers', 'N/A')}")
    print(f"Created at:    {state.get('created_at', 'N/A')}")
    print(f"Updated at:    {state.get('last_updated', 'N/A')}")
    print(f"All done:      {'yes' if state.get('all_done') else 'no'}")
    print()
    print("-" * 110)
    print(f"{'Batch':<8}{'Status':<10}{'Cases':<8}{'case_id range':<32}{'LLM calls':<12}{'Edges extracted':<14}{'Completed at':<22}")
    print("-" * 110)
    for idx in sorted(state["batches"].keys()):
        b = state["batches"][idx]
        cids = b.get("case_ids", [])
        cid_range = f"{cids[0]} ... {cids[-1]}" if cids else "(empty)"
        status = "DONE" if b.get("done") else "PENDING"
        print(f"{idx:<8}{status:<10}{len(cids):<8}{cid_range:<32}"
              f"{b.get('llm_calls', 0):<12}{b.get('edges_extracted', 0):<14}"
              f"{(b.get('completed_at') or '-'):<22}")
    print("-" * 110)

    done_batches = [b for b in state["batches"].values() if b.get("done")]
    pending_batches = [b for b in state["batches"].values() if not b.get("done")]
    total_calls = sum(b.get("llm_calls", 0) for b in state["batches"].values())
    total_edges = sum(b.get("edges_extracted", 0) for b in state["batches"].values())
    done_case_ids = set()
    for b in done_batches:
        for c in b.get("case_ids", []):
            done_case_ids.add(c)
    print(f"\nSummary: total batches {len(state['batches'])} | "
          f"completed {len(done_batches)} | pending {len(pending_batches)} | "
          f"total LLM calls {total_calls} | total edges extracted {total_edges}")
    print(f"      Globally completed case_id: {len(done_case_ids)} / {state.get('total_papers', '?')}")

    if pending_batches:
        print("\nPending batch indices (you can run a single one with --only-batch):")
        pending_idx = sorted([b['batch_index'] for b in pending_batches])
        for i in range(0, len(pending_idx), 10):
            chunk = pending_idx[i:i+10]
            print(f"  {', '.join(str(x) for x in chunk)}")
    print("=" * 70)
    print(f"Progress file:  {_progress_file_path()}")
    print(f"Log directory:  {os.path.join(EDGE_OUTPUT_ROOT, 'batch_run_logs')}")
    print(f"Final merge:    {FINAL_EDGE_DIR}")
    print("=" * 70)


# Metadata reading

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


# PDF scan and match

def scan_pdf_files(pdf_root: str) -> list[dict]:
    """
    Scan the PDF directory.

    v7 version: the subfolder name is the Zotero key (e.g. "225KHNN8"), not pure digits.
    - No longer requires folder names to be pure digits; now uses a generic scan.
    - Take the first PDF file in each subfolder as that paper's PDF.
    """
    pdf_root_path = Path(pdf_root)
    pdfs = []
    for folder in sorted(pdf_root_path.iterdir(), key=lambda p: p.name.lower()):
        if not folder.is_dir():
            continue
        case_id = folder.name            # subfolder name = case_id (e.g. "225KHNN8")
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


# LLM call

def call_llm(prompt: str, config: dict, api_key_config: Optional[dict] = None) -> dict:
    """
    Call the LLM, return a structured result dictionary.

    Returns:
        dict: {
            "text": str,          # Text response generated by the LLM
            "input_tokens": int,  # Exact input token count (returned by the API)
            "output_tokens": int, # Exact output token count (returned by the API)
            "total_tokens": int,  # Total token count
            "model": str,         # Actually used model name
            "error": str,         # Error info (empty string if no error)
        }
    """
    provider = config.get("provider", "gemini").lower()
    if provider == "gemini":
        return _call_gemini(prompt, config, api_key_config)
    else:
        raise ValueError(f"Unsupported provider: {provider}")


def _call_gemini(prompt: str, config: dict, api_key_config: Optional[dict] = None) -> dict:
    """Gemini API call, returning precise token counts"""
    try:
        import google.genai as genai
        from google.genai.types import HttpOptions
    except ImportError:
        raise ImportError("Please install: pip install google-genai")

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

    model_name = config.get("model", "gemini-3-flash-preview")
    response = client.models.generate_content(
        model=model_name,
        contents=[prompt],
        config={"temperature": config.get("temperature", 0.0), "max_output_tokens": 30000},
    )

    # Extract exact token counts from the API response
    input_tokens = 0
    output_tokens = 0
    total_tokens = 0
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
        "model": model_name,
        "error": "",
    }


# ────────────────────────────────────────────────────────
# LLM call (only Gemini supported, others removed)
# ────────────────────────────────────────────────────────

def _try_parse_json(text: str):
    try:
        return json.loads(text.strip())
    except (json.JSONDecodeError, TypeError):
        return None


def _extract_json_from_response(text: str) -> Optional[Union[list, dict]]:
    import re
    text = text.strip()
    if not text:
        return None

    # Strategy 1: bracket counting (most reliable, supports truncated responses)
    fence_pattern = re.compile(r'^```(?:\w*)', re.MULTILINE)
    fences = [(m.start(), m.group()) for m in fence_pattern.finditer(text)]
    if fences:
        start_fence_pos, start_fence_str = fences[0]
        start_content = text[start_fence_pos + len(start_fence_str):]
        if start_content.startswith("\n"):
            start_content = start_content[1:]

        opener = start_content[0] if start_content else ""
        if opener in ("[", "{"):
            depth = 0
            end_pos = -1
            for i, ch in enumerate(start_content):
                if ch in ("{", "["):
                    depth += 1
                elif ch in ("}", "]"):
                    depth -= 1
                    if depth == 0:
                        end_pos = i
                        break
            if end_pos > 0:
                candidate = start_content[:end_pos + 1]
                parsed = _try_parse_json(candidate)
                if parsed is not None:
                    return parsed
            # Truncated response: try the available content
            candidate = start_content
            parsed = _try_parse_json(candidate)
            if parsed is not None:
                return parsed

    # Strategy 2: try parsing the whole text directly
    parsed = _try_parse_json(text)
    if parsed is not None:
        return parsed

    # Strategy 3: find the first [ or {
    first_bracket = min((text.find(c) for c in "[{" if text.find(c) >= 0), default=-1)
    if first_bracket >= 0:
        parsed = _try_parse_json(text[first_bracket:])
        if parsed is not None:
            return parsed

    return None


def parse_edge_response(response_text: str) -> list[dict]:
    """Parse the edge-extraction response, returning a list of edge_description"""
    result = _extract_json_from_response(response_text)
    if result is None:
        return []
    if isinstance(result, list):
        return [item for item in result if isinstance(item, dict)]
    if isinstance(result, dict):
        return [result]
    return []


# Step 1: read merged node JSON and match PDF

def step1_load_and_match(merged_nodes_path: str) -> tuple[list[dict], list[dict]]:
    """Step 1: read merged nodes + match PDFs, returning (papers, pdf_map)"""
    # read merged nodes
    with open(merged_nodes_path, "r", encoding="utf-8") as f:
        nodes_json_array = json.load(f)

    print(f"[Step1] Read merged nodes: {len(nodes_json_array)} papers")

    # Read metadata Excel
    papers = load_metadata_from_excel(METADATA_EXCEL_PATH)
    print(f"[Step1] Metadata: {len(papers)} papers")

    # Scan PDF
    pdfs = scan_pdf_files(PDF_ROOT_DIR)
    print(f"[Step1] Scanned PDFs: {len(pdfs)} entries")

    # Match
    papers, match_results, unmatched = match_pdfs_to_metadata(papers, pdfs)
    matched = sum(1 for m in match_results if m["status"] == "matched")
    print(f"[Step1] PDF matching: {matched} succeeded, {len(unmatched)} unmatched")

    # Build case_id -> pdf_path mapping
    pdf_map = {}
    for p in papers:
        if p.get("case_id") and p.get("pdf_path"):
            pdf_map[p["case_id"]] = p["pdf_path"]

    # Inject PDF paths into nodes_json_array
    for paper in nodes_json_array:
        case_id = paper.get("case_id")
        paper["pdf_path"] = pdf_map.get(case_id, "")

    return nodes_json_array, pdf_map


# Step 2: generate candidate edge full set

def step2_generate_candidate_edges(nodes_json_array: list[dict]) -> list[dict]:
    """Step 2: call potential_edge_generation to generate the candidate-edge full set"""
    from potential_edge_generation import generate_potential_edges

    print(f"[Step2] Generating candidate-edge full set...")
    candidate_edges = generate_potential_edges(nodes_json_array)

    total_edges = sum(len(p.get("edges", [])) for p in candidate_edges)
    print(f"[Step2] Candidate-edge full set done: {len(candidate_edges)} papers, {total_edges} edges")

    # Save candidate-edge full set
    os.makedirs(CANDIDATE_EDGE_DIR, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(MERGED_NODES_INPUT))[0]
    out_path = os.path.join(CANDIDATE_EDGE_DIR, base_name.replace("merged_nodes", "candidate_edges") + ".json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(candidate_edges, f, ensure_ascii=False, indent=2)
    print(f"[Step2] Candidate-edge full set saved: {out_path}")

    return candidate_edges


# Step 3: split 02 causal edges

def step3_split_edge02(candidate_edges: list[dict]) -> list[Path]:
    """Step 3: split the 02 causal-edge fragments"""
    from edge_02_split import split_edge02_candidates

    # Clean up old split files to avoid leftovers that would desync the prompt file count
    _clean_dir(EDGE_02_SPLIT_DIR)

    print(f"[Step3] Splitting 02 causal edges...")
    result = split_edge02_candidates(
        candidate_edges,
        EDGE_02_SPLIT_DIR,
        N_split=N_SPLIT,
    )
    print(f"[Step3] 02 causal-edge fragments: {len(result)} files")

    # Return the file list generated directly by the split function (no need to glob again)
    return [Path(r.get("_file_path", "")) for r in result if r.get("_file_path")]


# Step 4: split 03 evidence edges

def step4_split_edge03(candidate_edges: list[dict]) -> list[Path]:
    """Step 4: split the 03 evidence-edge fragments"""
    from edge_03_split import split_edge03_candidates

    # Clean up old split files to avoid leftovers that would desync the prompt file count
    _clean_dir(EDGE_03_SPLIT_DIR)

    print(f"[Step4] Splitting 03 evidence edges...")
    result = split_edge03_candidates(
        candidate_edges,
        EDGE_03_SPLIT_DIR,
        N_split=N_SPLIT,
    )
    print(f"[Step4] 03 evidence-edge fragments: {len(result)} files")

    # Return the file list generated directly by the split function (no need to glob again)
    return [Path(r.get("_file_path", "")) for r in result if r.get("_file_path")]


# ── Shared utility: group by case_id ───────────────────────────────

def _group_split_files_by_case(
    split_files: list[Path],
) -> dict[str, list[Path]]:
    """Group split files by case_id"""
    from collections import defaultdict
    by_case: dict[str, list[Path]] = defaultdict(list)
    for f in split_files:
        m = re.match(r'\[?([A-Z]\d+)', f.name)
        if m:
            case_id = m.group(1)
        else:
            case_id = f.stem.split("+")[0]
        by_case[case_id].append(f)
    return by_case


# Step 5: generate 02 causal-edge prompts (grouped by case_id, ~10 edges/file)

def step5_generate_edge02_prompts(edge02_split_files: list[Path]) -> list[dict]:
    """Step 5: generate LLM prompt Markdown for the 02 causal edges.

    Strategy: split files of the same case_id are aggregated and prompts are
    generated in batches of ~10 edges, ensuring that the attached PDF source
    text is not wastefully duplicated for every batch.
    """
    from edge_02_prompt import generate_edge02_prompts

    _clean_dir(EDGE_02_PROMPT_DIR)

    by_case = _group_split_files_by_case(edge02_split_files)
    print(f"[Step5] Generating 02 causal-edge prompts ({len(by_case)} papers)...")

    all_results = []
    for case_id, files in sorted(by_case.items()):
        results = generate_edge02_prompts([str(f) for f in files], EDGE_02_PROMPT_DIR)
        all_results.extend(results)
        n_batches = len(results)
        n_edges = sum(r["edge_count"] for r in results)
        print(f"  [{case_id}] {len(files)} split file(s) -> {n_batches} prompt batch(es), {n_edges} edges")

    print(f"[Step5] 02 causal-edge prompts: {len(all_results)} files")
    return all_results


# Step 6: generate 03 evidence-edge prompts

def step6_generate_edge03_prompts(edge03_split_files: list[Path]) -> list[dict]:
    """Step 6: generate LLM prompt Markdown for the 03 evidence edges.

    Strategy: aggregate all split files of the same case_id and generate
    ~10 edges/file prompts in batches, avoiding the case where every
    fragment contains only 1 edge and forces re-sending the PDF source.
    """
    from edge_03_prompt import generate_edge03_prompts

    _clean_dir(EDGE_03_PROMPT_DIR)

    by_case = _group_split_files_by_case(edge03_split_files)
    print(f"[Step6] Generating 03 evidence-edge prompts ({len(by_case)} papers)...")

    all_results = []
    for case_id, files in sorted(by_case.items()):
        results = generate_edge03_prompts(files, EDGE_03_PROMPT_DIR)
        all_results.extend(results)
        n_batches = len(results)
        n_edges = sum(r["edge_count"] for r in results)
        print(f"  [{case_id}] {len(files)} split file(s) -> {n_batches} prompt batch(es), {n_edges} edges")

    print(f"[Step6] 03 evidence-edge prompts: {len(all_results)} files")
    return all_results


# Step 7: Concurrently call LLM to extract edge_description

def _call_llm_for_prompt(
    prompt_file: Path,
    case_id: str,
    pdf_map: dict[str, str],
    llm_config: dict,
    key_manager: RoundRobinKeyManager,
    idx: int,
    edge_type: str = "02",
    rate_limiter: Optional[GlobalRateLimiter] = None,
) -> dict:
    """
    Call LLM for a single prompt file (guarded by per-key concurrency cap) and return the extraction result.

    Model assignment strategy:
        All edge types ("02" / "03") uniformly use MODEL_EDGE_02 (gemini-3.5-flash).

    Improvements:
        - Global rate limiter: when a connection error is detected it slows down automatically to avoid retry storms
        - Exponential backoff retries: each retry waits exponentially longer (5s, 15s, 45s...)
        - Specific error handling: WinError 10054 (connection reset) is treated as retryable
        - Atomic acquire: select key + occupy slot are done under one lock, avoiding the old
          get_key/acquire split that caused multiple threads to choose the same key (fake concurrency)
    """
    # Pick the model based on edge_type (decide before occupying the key slot,
    # so we never block while holding a slot while choosing a model)
    # All edge types uniformly use MODEL_EDGE_02 (gemini-3.5-flash)
    model_name = MODEL_EDGE_02

    model_config = {
        "provider": llm_config.get("provider", "gemini"),
        "model": model_name,
        "base_url": llm_config.get("base_url", ""),
        "timeout": llm_config.get("timeout", 300),
    }

    # Read prompt content
    prompt_text = load_prompt_file(str(prompt_file))
    pdf_path = pdf_map.get(case_id, "")
    pdf_text = extract_pdf_text(pdf_path) if pdf_path else ""

    # Build the full prompt
    if pdf_text:
        full_prompt = (prompt_text + "\n\n"
                      + "=" * 60 + "\n"
                      + "[Full PDF content]\n"
                      + "=" * 60 + "\n"
                      + pdf_text)
    else:
        full_prompt = prompt_text + "\n\n[Warning: matching PDF source not found]"

    # Atomically "balanced key selection + concurrent slot occupation" -- pick key,
    # occupy slot, and account usage all in one step under the lock.
    # This avoids the "fake concurrency" pitfall: the old get_key() and acquire(key)
    # were two separate steps, during which other threads still saw the key semaphore
    # as 3 and kept piling tasks onto the same key, producing a "10 keys added, 1
    # key actually carrying the load" pseudo-parallel pattern.
    assigned_key, key_idx = key_manager.acquire()
    api_key_config = {
        "api_key": assigned_key,
        "base_url": llm_config.get("base_url", ""),
        "timeout": llm_config.get("timeout", 300),
    }
    try:
        last_error = ""
        consecutive_errors = 0
        for attempt in range(LLM_RETRIES):
            t0 = time.time()
            try:
                result = call_llm(full_prompt, model_config, api_key_config)
                elapsed_ms = int((time.time() - t0) * 1000)

                # Prefer the exact token counts returned by the API; fall back to estimation if the API returned 0
                input_tokens = result["input_tokens"] if result["input_tokens"] > 0 else _estimate_tokens(full_prompt)
                output_tokens = result["output_tokens"] if result["output_tokens"] > 0 else _estimate_tokens(result["text"])

                # Parse the response
                edges = parse_edge_response(result["text"])

                # Success: clear error counters
                if rate_limiter is not None:
                    rate_limiter.clear_errors()

                return {
                    "success": True,
                    "prompt_file": str(prompt_file),
                    "case_id": case_id,
                    "input_tokens": input_tokens,
                    "output_tokens": output_tokens,
                    "total_tokens": input_tokens + output_tokens,
                    "elapsed_ms": elapsed_ms,
                    "edges": edges,
                    "llm_response": result["text"],
                    "error": "",
                }
            except Exception as e:
                elapsed_ms = int((time.time() - t0) * 1000)
                last_error = str(e)
                error_str = str(e)

                # Determine whether this is a connection-reset-class error
                # (WinError 10054 / errno 54 / reset / broken pipe)
                is_connection_reset = any(x in error_str for x in [
                    "10054", "RemoteConnectionError", "reset", "broken pipe",
                    "ConnectionResetError", "ConnectionRefusedError",
                    "timed out", "timeout", "502", "503", "429", "rate limit",
                ])
                if is_connection_reset:
                    consecutive_errors += 1
                    if rate_limiter is not None:
                        rate_limiter.report_error()

                    # Global slowdown check
                    if rate_limiter is not None:
                        rate_limiter.wait_if_degraded()

                    # Exponential backoff: 5s, 15s, 45s, 135s (exponential growth)
                    wait_time = 5 * (3 ** attempt)
                    if attempt < LLM_RETRIES - 1:
                        print(f"  [Retry] {prompt_file.name}: connection error ({last_error[:60]}), "
                              f"waiting {wait_time}s before retry (attempt {attempt+1}/{LLM_RETRIES})...")
                        time.sleep(wait_time)
                    continue
                else:
                    # Non-connection error: do not retry
                    if attempt < LLM_RETRIES - 1:
                        time.sleep(2 ** attempt)
                    continue

        return {
            "success": False,
            "prompt_file": str(prompt_file),
            "case_id": case_id,
            "input_tokens": 0,
            "output_tokens": 0,
            "total_tokens": 0,
            "elapsed_ms": 0,
            "edges": [],
            "llm_response": "",
            "error": last_error,
        }
    finally:
        # Slot must be released; the finally block guarantees it even if an exception is raised
        key_manager.release(key_idx)


def _extract_case_id_from_prompt(prompt_file: Path) -> str:
    """
    Extract the case_id from the prompt filename.

    Filename format (v8):
      <case_id>+02-causal_edge+<idx>+prompt.md
      <case_id>+03-evidence_edge+<idx>+prompt.md
      <case_id>+02-causal_edge+2+prompt.md
      ...
    case_id is an 8-character alphanumeric random code (e.g. 225KHNN8, ZZZRPFBV);
    also compatible with legacy C-prefixed identifiers (e.g. C00168).
    """
    fname = prompt_file.stem  # strip the extension
    # Prefer the '+' separator and take the first chunk as case_id (most reliable)
    if "+" in fname:
        return fname.split("+", 1)[0].strip()
    # fallback: legacy format without '+' separator
    m = re.match(r'^([A-Za-z0-9]+)', fname)
    if m:
        return m.group(1)
    return fname[:10]


def edge_type_label_from_type(edge_type: str) -> str:
    """Convert an edge-type code into its output label"""
    if edge_type == "02":
        return "02-causal edge"
    else:
        return "03-evidence edge"


def step7_call_llm_parallel(
    edge02_prompts: list[dict],
    edge03_prompts: list[dict],
    pdf_map: dict[str, str],
    llm_config: dict,
    key_manager: RoundRobinKeyManager,
    logger,
    skip_existing: bool = False,
    max_concurrent: int = 8,
    batch_case_ids: Optional[list[str]] = None,
    batch_idx: int = 0,
    on_batch_done: Optional[callable] = None,
) -> tuple[list[dict], list[dict]]:
    """
    Step 7: concurrently call the LLM, processing 02 causal-edge and 03 evidence-edge prompts in parallel.
    Returns (edge02_results, edge03_results)

    Batch mode (batch_case_ids is non-empty):
        - Only process tasks whose case_id falls within batch_case_ids
        - Once processing completes, invoke the on_batch_done callback to trigger progress persistence
    """
    # Create the global rate limiter
    rate_limiter = GlobalRateLimiter(max_concurrent=max_concurrent)
    print(f"[Step7] Global rate limit: at most {max_concurrent} concurrent LLM requests")

    # Merge all prompt tasks
    all_tasks: list[tuple] = []
    for p in edge02_prompts:
        prompt_file = Path(p["output_path"])
        case_id = _extract_case_id_from_prompt(prompt_file)
        all_tasks.append((prompt_file, case_id, "02"))

    for p in edge03_prompts:
        prompt_file = Path(p["output_path"])
        case_id = _extract_case_id_from_prompt(prompt_file)
        all_tasks.append((prompt_file, case_id, "03"))

    print(f"[Step7] Total {len(all_tasks)} prompt tasks (02: {len(edge02_prompts)}, 03: {len(edge03_prompts)})")

    # Batch filter: only process case_ids in the current batch (supports resuming from checkpoint)
    if batch_case_ids is not None:
        batch_set = set(batch_case_ids)
        all_tasks = [t for t in all_tasks if t[1] in batch_set]
        print(f"[Step7-batch{batch_idx}] Batch {batch_idx} only handles {len(all_tasks)} prompt tasks")
        if not all_tasks:
            print(f"[Step7-batch{batch_idx}] Warning: this batch has no tasks (case_id extraction may have failed or data is missing)")
            print(f"[Step7-batch{batch_idx}] Skipping this batch and not marking it complete; user must inspect and handle manually")
            # Note: on_batch_done is intentionally not called here, to avoid marking an "empty batch" as done by mistake
            return [], []

    # Skip already processed: when --skip-existing is set, check whether the output dir already has the corresponding JSON
    if skip_existing:
        pending_tasks = []
        for task in all_tasks:
            prompt_file, case_id, edge_type = task
            # Infer the output path (consistent with _save_edge_results)
            fname = prompt_file.stem
            m = re.search(r'\+(\d+)\+prompt$', fname)
            if m:
                chunk_idx = m.group(1)
                out_name = f"{case_id}+{edge_type_label_from_type(edge_type)}+{chunk_idx}.json"
            else:
                out_name = f"{case_id}+{edge_type_label_from_type(edge_type)}.json"
            out_dir = EDGE_02_OUTPUT_DIR if edge_type == "02" else EDGE_03_OUTPUT_DIR
            out_path = os.path.join(out_dir, out_name)
            if os.path.exists(out_path):
                logger(f"  [SKIP] Already exists, skipping: {out_name}")
                continue
            pending_tasks.append(task)
        skipped = len(all_tasks) - len(pending_tasks)
        print(f"[Step7] Skipped {skipped} already processed files, {len(pending_tasks)} remaining to process")
        all_tasks = pending_tasks

    edge02_results: list[dict] = []
    edge03_results: list[dict] = []

    results_lock = Lock()

    def process_task(idx: int, task: tuple) -> dict:
        prompt_file, case_id, edge_type = task
        logger(f"  >> Processing [{edge_type}] {prompt_file.name} (case={case_id})...")
        result = _call_llm_for_prompt(
            prompt_file, case_id, pdf_map, llm_config, key_manager, idx,
            edge_type=edge_type,
            rate_limiter=rate_limiter,
        )
        result["edge_type"] = edge_type
        return result

    # The thread-pool cap must use the function parameter max_concurrent (= key_manager.total_keys * PER_KEY_LIMIT),
    # not the module-level PROMPT_PARALLEL global. The old implementation used
    # PROMPT_PARALLEL, so when the user passed --prompt-parallel on the CLI to lower the value,
    # leaving some keys without any calling thread -- producing "fake concurrency".
    with ThreadPoolExecutor(max_workers=max_concurrent) as executor:
        futures = {
            executor.submit(process_task, i, task): task
            for i, task in enumerate(all_tasks)
        }

        for future in as_completed(futures):
            task = futures[future]
            try:
                result = future.result()
                edge_type = result["edge_type"]

                # Record aggregation
                _record_prompt_stat(
                    result["case_id"], edge_type, result["success"],
                    result["input_tokens"], result["output_tokens"],
                    result.get("total_tokens", result["input_tokens"] + result["output_tokens"]),
                    result["elapsed_ms"], len(result["edges"]), result["error"]
                )

                if result["success"]:
                    logger(f"    [OK] {task[2]} {task[0].name}: "
                           f"{len(result['edges'])} edges "
                           f"(in={result['input_tokens']:,}, out={result['output_tokens']:,}, "
                           f"{result['elapsed_ms']/1000:.1f}s)")
                else:
                    logger(f"    [FAIL] {task[2]} {task[0].name}: {result['error']}")

                with results_lock:
                    if edge_type == "02":
                        edge02_results.append(result)
                    else:
                        edge03_results.append(result)

            except Exception as e:
                logger(f"    [EXC] {task[2]} {task[0].name}: {e}")

    print(f"[Step7] LLM calls done: 02={len(edge02_results)} entries, 03={len(edge03_results)} entries")

    # Print per-key usage, useful to confirm that the 10 keys are actually called evenly (fake-concurrency detection)
    usage = key_manager.usage_report()
    total_calls = sum(usage.values())
    if total_calls > 0:
        n_used = sum(1 for v in usage.values() if v > 0)
        print(f"[Step7] Per-key call distribution (total {len(usage)} keys, actually used {n_used}, total calls {total_calls}):")
        for i, k in enumerate(usage.keys()):
            cnt = usage.get(k, 0)
            pct = cnt / total_calls * 100
            flag = "" if cnt > 0 else "  <- idle!"
            print(f"      Key{i + 1:02d}: {cnt:>5d} calls  ({pct:5.1f}%)  {k[:10]}...{k[-4:]}{flag}")
        if n_used < len(usage):
            print(f"      Warning: only {n_used}/{len(usage)} keys were called, please check the concurrency settings!")
        else:
            print(f"      All {n_used} keys were called, no idle key.")

    # Batch complete callback: trigger progress persistence
    if on_batch_done:
        total_calls_cb = len(edge02_results) + len(edge03_results)
        total_edges = sum(len(r["edges"]) for r in edge02_results + edge03_results)
        on_batch_done(batch_idx, batch_case_ids or [], total_calls_cb, total_edges)

    return edge02_results, edge03_results


def _save_edge_results(
    results: list[dict],
    output_dir: str,
    edge_type_label: str,
):
    """Save the LLM extraction results to the output directory (one file per batch)"""
    os.makedirs(output_dir, exist_ok=True)

    for result in results:
        case_id = result["case_id"]
        prompt_file = Path(result["prompt_file"])
        # Infer the chunk index from the prompt filename
        # format: <case_id>+02causal edges+<idx>+prompt.md or <case_id>+03evidence edges+<idx>+prompt.md
        fname = prompt_file.stem
        m = re.search(r'\+(\d+)\+prompt$', fname)  # C00170+03evidence edges+1+prompt
        if m:
            chunk_idx = m.group(1)
            out_name = f"{case_id}+{edge_type_label}+{chunk_idx}.json"
        else:
            # fallback: when there is no chunk index, use case_id directly
            out_name = f"{case_id}+{edge_type_label}.json"

        out_path = os.path.join(output_dir, out_name)

        doc = {
            "case_id": case_id,
            "edge_type": edge_type_label,
            "prompt_file": result["prompt_file"],
            "input_tokens": result["input_tokens"],
            "output_tokens": result["output_tokens"],
            "total_tokens": result.get("total_tokens", result["input_tokens"] + result["output_tokens"]),
            "elapsed_ms": result["elapsed_ms"],
            "success": result["success"],
            "error": result.get("error", ""),
            "edges": result["edges"],
            "llm_response": (result.get("llm_response", "")[:5000]
                             if result.get("llm_response") else ""),
        }

        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=2)


def step7_save_results(
    edge02_results: list[dict],
    edge03_results: list[dict],
):
    """Step 7 save: write LLM results to the output directory"""
    print(f"[Step7-Save] Saving 02 causal-edge results to {EDGE_02_OUTPUT_DIR}...")
    _save_edge_results(edge02_results, EDGE_02_OUTPUT_DIR, "02-causal edge")
    print(f"[Step7-Save] Saving 03 evidence-edge results to {EDGE_03_OUTPUT_DIR}...")
    _save_edge_results(edge03_results, EDGE_03_OUTPUT_DIR, "03-evidence edge")

    total_02 = sum(len(r["edges"]) for r in edge02_results)
    total_03 = sum(len(r["edges"]) for r in edge03_results)
    print(f"[Step7-Save] 02 causal edges: {len(edge02_results)} files, {total_02} edges")
    print(f"[Step7-Save] 03 evidence edges: {len(edge03_results)} files, {total_03} edges")


# Step 8: back-fill edge_description + aggregate null

def step8_backfill_and_statistics(
    candidate_edges: list[dict],
    edge02_results: list[dict],
    edge03_results: list[dict],
) -> tuple[list[dict], list[tuple], int, int]:
    """
    Step 8: back-fill the extraction results into the edge_description field of the candidate-edge full set.
    - 02/03 edges: the LLM returns edge_description directly, and the program back-fills it
    Aggregate the edges where edge_description is null (case_id, edge_id).
    Returns (candidate-edge full set with back-filled fields, null list, null total, total edges)
    """
    print(f"[Step8] Back-filling edge_description into the candidate-edge full set...")

    # Build edge_id -> edge_description mapping (02 and 03 edges)
    edge_desc_map: dict[str, str] = {}
    for result in edge02_results + edge03_results:
        for edge in result.get("edges", []):
            edge_id = edge.get("edge_id", "")
            desc = edge.get("edge_description", "")
            if edge_id:
                edge_desc_map[edge_id] = desc

    print(f"[Step8] Edge description map: {len(edge_desc_map)} entries")

    # Main back-fill loop
    null_list: list[tuple] = []
    total_edges = 0
    null_count = 0

    for paper in candidate_edges:
        for edge in paper.get("edges", []):
            total_edges += 1
            edge_id = edge.get("edge_id", "")

            if edge_id in edge_desc_map:
                edge["edge_description"] = edge_desc_map[edge_id]
            else:
                null_count += 1
                null_list.append((paper.get("case_id", ""), edge_id))

    print(f"[Step8] Back-fill done: total edges={total_edges}, edge_description=null={null_count}")

    # Generate the aggregation notes file
    os.makedirs(EDGE_OUTPUT_ROOT, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(MERGED_NODES_INPUT))[0]
    stats_file = os.path.join(EDGE_OUTPUT_ROOT, base_name + "_edge_description_null_stats.txt")

    lines = []
    lines.append("=" * 60)
    lines.append("Edge-relation edge_description=null statistics notes")
    lines.append(f"Generated at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"Input file: {MERGED_NODES_INPUT}")
    lines.append(f"Total edges: {total_edges}")
    lines.append(f"edge_description=null count: {null_count}")
    lines.append(f"Filled count: {total_edges - null_count}")
    lines.append("=" * 60)
    lines.append("")

    if null_list:
        lines.append("Edges with edge_description=null:")
        lines.append(f"{'#':<6} {'case_id':<12} {'edge_id':<20}")
        lines.append("-" * 40)
        for idx, (case_id, edge_id) in enumerate(null_list, 1):
            lines.append(f"{idx:<6} {case_id:<12} {edge_id:<20}")
    else:
        lines.append("All edges have edge_description filled, no nulls.")

    with open(stats_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"[Step8] Statistics notes saved: {stats_file}")
    return candidate_edges, null_list, null_count, total_edges


# Step 9: remove null edges and save the final merged result

def step9_finalize_and_save(
    candidate_edges: list[dict],
    batch_case_ids: Optional[list[str]] = None,
    batch_idx: int = 0,
) -> list[dict]:
    """
    Step 9: remove edge_description=null edges from the candidate-edge full set,
    generate the "extracted edge-relation json array" and save it.

    Batch mode (batch_case_ids non-empty):
        - Only process the case_ids of the current batch
        - Output filename includes the batch index: {case_id_start}+{case_id_end}+batch{idx}+merged_edges.json
        - Multiple runs will app continue writing to different batch files, no overwrite
    """
    print(f"[Step9] Generating the extracted edge-relation json array...")

    final_edges: list[dict] = []
    total_removed = 0

    for paper in candidate_edges:
        case_id = paper.get("case_id")
        original_count = len(paper.get("edges", []))
        # Filter out edges where edge_description is null
        filtered_edges = [
            e for e in paper.get("edges", [])
            if e.get("edge_description") is not None
        ]
        removed = original_count - len(filtered_edges)
        total_removed += removed

        final_paper = {
            "case_id": case_id,
            "paper_title": paper.get("paper_title"),
            "publish_year": paper.get("publish_year"),
            "publish_source": paper.get("publish_source"),
            "cite_count": paper.get("cite_count"),
            "algorithm_hyperparameters": paper.get("algorithm_hyperparameters"),
            "training_config": paper.get("training_config"),
            "performance_metrics": paper.get("performance_metrics"),
            "nodes": [],          # Edge extraction does not involve nodes
            "edges": filtered_edges,
        }
        final_edges.append(final_paper)

    print(f"[Step9] Extracted edge-relations: {len(final_edges)} papers, "
          f"total {sum(len(p['edges']) for p in final_edges)} edges, "
          f"removed {total_removed} null edges")

    # Save the final merged file
    os.makedirs(FINAL_EDGE_DIR, exist_ok=True)

    # Batch mode: save each batch as a standalone file (for resume support)
    if batch_case_ids is not None and len(batch_case_ids) > 0:
        # Sort to determine the file-name range
        sorted_case_ids = sorted(batch_case_ids)
        case_part = f"{sorted_case_ids[0]}+...+{sorted_case_ids[-1]}"
        out_name = f"{case_part}+batch{batch_idx}+merged_edges.json"
    else:
        # Full mode: keep the original file-name rule
        base_name = os.path.splitext(os.path.basename(MERGED_NODES_INPUT))[0]
        case_ids = sorted(set(p.get("case_id", "") for p in final_edges))
        if len(case_ids) > 1:
            case_part = f"{case_ids[0]}+...+{case_ids[-1]}"
        else:
            case_part = case_ids[0] if case_ids else ""
        out_name = f"{case_part}+merged_edges.json"

    out_path = os.path.join(FINAL_EDGE_DIR, out_name)

    # Use "append-merge" in batch mode: keep existing batch merged data + this batch's data
    if batch_case_ids is not None and os.path.exists(out_path):
        try:
            with open(out_path, "r", encoding="utf-8") as f:
                existing_data = json.load(f)
            existing_case_ids = {p.get("case_id") for p in existing_data}
            # Only add case_ids not present in this batch
            new_data = [p for p in final_edges if p.get("case_id") not in existing_case_ids]
            final_edges = existing_data + new_data
            print(f"[Step9-resume] Merged existing data: original {len(existing_data)} papers + this batch {len(new_data)} papers = {len(final_edges)} papers")
        except Exception as e:
            print(f"[Step9-resume] Failed to read existing file ({e}), overwriting")

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(final_edges, f, ensure_ascii=False, indent=2)

    print(f"[Step9] Extracted edge-relations saved: {out_path}")
    return final_edges


# ============================================================
# Entry point: local test
# ============================================================

def main():
    global MERGED_NODES_INPUT, EDGE_OUTPUT_ROOT, EDGE_02_OUTPUT_DIR, EDGE_03_OUTPUT_DIR
    global EDGE_02_PROMPT_DIR, EDGE_03_PROMPT_DIR, FINAL_EDGE_DIR
    global PROMPT_PARALLEL, PER_KEY_LIMIT, LLM_RETRIES, LLM_CONFIG, BATCH_SIZE

    parser = argparse.ArgumentParser(
        description="Literature knowledge-graph edge-relation extraction program V8"
    )
    parser.add_argument("--input", type=str, default=MERGED_NODES_INPUT,
                        help="Path to the merged-node JSON")
    parser.add_argument("--output-root", type=str, default=EDGE_OUTPUT_ROOT,
                        help="Edge-relation output root directory")
    parser.add_argument("--metadata", type=str, default=METADATA_EXCEL_PATH,
                        help="Path to the metadata Excel")
    parser.add_argument("--pdf-root", type=str, default=PDF_ROOT_DIR,
                        help="PDF root directory")
    parser.add_argument("--prompt-parallel", type=int, default=PROMPT_PARALLEL,
                        help="Number of prompts processed concurrently (total concurrency cap)")
    parser.add_argument("--per-key-limit", type=int, default=PER_KEY_LIMIT,
                        help="Maximum concurrent requests held by each API key at the same time (default 3)")
    parser.add_argument("--n-split", type=int, default=N_SPLIT,
                        help="Maximum number of edges per json fragment")
    parser.add_argument("--llm-retries", type=int, default=LLM_RETRIES,
                        help="Max retries after LLM call failure (default 2, i.e. up to 2 retries)")
    parser.add_argument("--api-keys", type=str, default="",
                        help="Multiple LLM API keys, separated by |")
    parser.add_argument("--provider", type=str, default="gemini",
                        choices=["gemini"],
                        help="LLM provider (only gemini is supported)")
    parser.add_argument("--model", type=str, default=MODEL_EDGE_02,
                        help=f"Default model (used for 02-causal edge / 03-evidence edge), default: {MODEL_EDGE_02}")
    parser.add_argument("--base-url", type=str, default=None)
    parser.add_argument("--skip-existing", action="store_true",
                        help="Skip already processed prompt files")
    parser.add_argument("--batch-size", type=int, default=BATCH_SIZE,
                        help=f"Papers per batch (default {BATCH_SIZE}). Papers exceeding this count are auto-split by case_id")
    parser.add_argument("--only-batch", type=int, default=-1,
                        help="Run only the specified batch index (-1 = run all pending batches, indexed from 0)")
    parser.add_argument("--reset-progress", action="store_true",
                        help="Reset the progress file (delete existing batch progress and start over)")
    parser.add_argument("--show-progress", action="store_true",
                        help="Display current progress only, do not perform any processing")
    parser.add_argument("--status", action="store_true",
                        help="Alias for --show-progress: display current progress and exit")
    parser.add_argument("--max-batches", type=int, default=-1,
                        help="Maximum number of batches to process this run (-1 = process all pending batches)")
    args = parser.parse_args()

    # Update configuration
    MERGED_NODES_INPUT = args.input
    EDGE_OUTPUT_ROOT = args.output_root
    EDGE_02_OUTPUT_DIR = os.path.join(EDGE_OUTPUT_ROOT, "02-causal edge")
    EDGE_03_OUTPUT_DIR = os.path.join(EDGE_OUTPUT_ROOT, "03-evidence edge")
    EDGE_02_PROMPT_DIR = os.path.join(V8_ROOT_DIR, "edge_prompts-temp", "02-causal edge prompts")
    EDGE_03_PROMPT_DIR = os.path.join(V8_ROOT_DIR, "edge_prompts-temp", "03-evidence edge prompts")
    FINAL_EDGE_DIR = os.path.join(V8_ROOT_DIR, "final_merge", "B0-edge_merge")
    PROMPT_PARALLEL = args.prompt_parallel
    PER_KEY_LIMIT = args.per_key_limit
    LLM_RETRIES = args.llm_retries
    BATCH_SIZE = args.batch_size

    LLM_CONFIG["provider"] = "gemini"
    LLM_CONFIG["model"] = args.model
    LLM_CONFIG["temperature"] = 0.0
    if args.base_url:
        LLM_CONFIG["base_url"] = args.base_url
    if not LLM_CONFIG.get("base_url"):
        LLM_CONFIG["base_url"] = os.environ.get("BFGA_LLM_API_URL", "https://YOUR.LLM.ENDPOINT/")

    # Multi-key mode
    keys: list[str] = []
    if args.api_keys:
        keys = [k.strip() for k in args.api_keys.split("|") if k.strip()]
    elif MULTI_API_KEYS:
        keys = [k.strip() for k in MULTI_API_KEYS if k.strip()]

    if not keys:
        print("Error: LLM API Key not set! Please configure MULTI_API_KEYS in the code, or pass --api-keys.")
        return

    key_manager = RoundRobinKeyManager(keys, per_key_limit=PER_KEY_LIMIT)
    print(f"[Multi-key mode] Total {len(keys)} keys")
    for i, k in enumerate(keys):
        print(f"  Key {i+1}: {k[:10]}...{k[-4:]}")
    # True-concurrency hint: explicitly state the "10 keys each running 1 concurrently" strategy,
    # to avoid being mistaken for "fake 10 keys but only 1 actually running".
    print(f"[True concurrency] Global concurrency = {len(keys)} (number of keys), per-key concurrency = {PER_KEY_LIMIT}")
    print(f"[True concurrency] Each of the 10 keys strictly runs 1, eliminating 429 / rate-limit triggered by same-key multi-request -> idle.")

    # --status early exit: no input file check needed, can directly view existing progress
    if getattr(args, "status", False) or args.show_progress:
        existing = load_progress()
        if existing:
            _print_progress_status_verbose(existing, MERGED_NODES_INPUT)
        else:
            print("[--status] No progress file found yet. Please run the full pipeline once first to initialize batches.")
            print(f"  Expected progress file path: {_progress_file_path()}")
        return

    # Check input file
    if not os.path.exists(MERGED_NODES_INPUT):
        print(f"Error: input file does not exist: {MERGED_NODES_INPUT}")
        return

    # Create all output directories
    for d in [CANDIDATE_EDGE_DIR, EDGE_02_SPLIT_DIR, EDGE_03_SPLIT_DIR,
              EDGE_02_PROMPT_DIR, EDGE_03_PROMPT_DIR,
              EDGE_02_OUTPUT_DIR, EDGE_03_OUTPUT_DIR,
              FINAL_EDGE_DIR]:
        os.makedirs(d, exist_ok=True)

    print("=" * 70)
    print("Literature knowledge-graph edge-relation extraction program V8")
    print("=" * 70)
    print(f"Input node JSON:  {MERGED_NODES_INPUT}")
    print(f"Output root dir:  {EDGE_OUTPUT_ROOT}")
    print(f"Metadata Excel:   {METADATA_EXCEL_PATH}")
    print(f"PDF root dir:     {PDF_ROOT_DIR}")
    print(f"LLM:              {LLM_CONFIG['provider']}")
    print(f"  - Model (02/03 unified):     {MODEL_EDGE_02}")
    print(f"API Keys:         {len(keys)} (multi-key round-robin, per-key {PER_KEY_LIMIT} concurrent -> 10 true concurrent paths)")
    print(f"Prompt parallelism:   {PROMPT_PARALLEL} (global concurrency cap = num keys = {len(keys)})")
    print(f"Max edges per fragment: {N_SPLIT}")
    print("=" * 70)

    log_lock = Lock()
    ts = time.strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(EDGE_OUTPUT_ROOT, f"edge_extractor_run_{ts}.log")

    def logger(msg: str):
        ts2 = time.strftime("%H:%M:%S")
        line = f"[{ts2}] {msg}"
        print(line)
        with log_lock:
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(line + "\n")

    logger(f"Starting edge-relation extraction pipeline...")

    print("\n" + "=" * 60)
    print("Step 1: Read merged nodes + match PDFs")
    print("=" * 60)
    nodes_json_array, pdf_map = step1_load_and_match(MERGED_NODES_INPUT)
    logger(f"Step1 done: {len(nodes_json_array)} papers matched with PDFs")

    print("\n" + "=" * 60)
    print("Step 2: Generate candidate-edge full set")
    print("=" * 60)
    candidate_edges = step2_generate_candidate_edges(nodes_json_array)

    # Extract all case_ids (in the original order)
    all_case_ids: list[str] = []
    for paper in candidate_edges:
        cid = paper.get("case_id", "")
        if cid and cid not in all_case_ids:
            all_case_ids.append(cid)
    print(f"\n[Batch planning] Total {len(all_case_ids)} papers, {BATCH_SIZE} per batch")
    total_batches = (len(all_case_ids) + BATCH_SIZE - 1) // BATCH_SIZE
    print(f"[Batch planning] Will be split into {total_batches} batches")

    # ── Load / initialize progress status ──
    global _progress_state
    if args.reset_progress:
        pf = _progress_file_path()
        if os.path.exists(pf):
            os.remove(pf)
            print(f"[Progress] Old progress file deleted: {pf}")
        _progress_state = init_progress_state(len(all_case_ids))
    else:
        existing = load_progress()
        if existing and existing.get("total_papers") == len(all_case_ids):
            _progress_state = existing
            print(f"[Progress] Reusing existing progress, run_id={_progress_state.get('run_id')}")
        else:
            _progress_state = init_progress_state(len(all_case_ids))
    save_progress(_progress_state)

    # ── Compute the list of pending batches ──
    if args.only_batch >= 0:
        target_batches = [args.only_batch]
        print(f"[Batch] --only-batch={args.only_batch}: only running batch {args.only_batch}")
    else:
        target_batches = sorted([
            b["batch_index"] for b in _progress_state["batches"].values()
            if not b.get("done", False)
        ])
        print(f"[Batch] Pending batches: {target_batches}")
        if args.max_batches > 0 and len(target_batches) > args.max_batches:
            target_batches = target_batches[:args.max_batches]
            print(f"[Batch] --max-batches={args.max_batches}: only running the first {args.max_batches} pending batches this run")

    if not target_batches:
        print("\n[Batch] All batches are done, nothing to run. Use --reset-progress to start over.")
        # Still run a full merge once, to view the final result
        logger("All batches are done, reusing existing output")
    else:
        # ── Step 3-6: shared preparation (each batch regenerates prompts, but only within its own case_id range) ──
        # Prepare the "all case_id -> batch index" mapping for later filtering
        case_to_batch: dict[str, int] = {}
        for batch_idx_t, batch in _progress_state["batches"].items():
            batch_idx_int = int(batch_idx_t)
            start = batch_idx_int * BATCH_SIZE
            end = min(start + BATCH_SIZE, len(all_case_ids))
            for i in range(start, end):
                case_to_batch[all_case_ids[i]] = batch_idx_int

        # Generate the full split and prompt sets in one go (avoid regenerating for every batch)
        print("\n" + "=" * 60)
        print("Step 3-6 (shared): split + generate prompts (full)")
        print("=" * 60)
        print("\n" + "=" * 60)
        print("Step 3: Split 02 causal edges")
        print("=" * 60)
        edge02_split_files = step3_split_edge02(candidate_edges)

        print("\n" + "=" * 60)
        print("Step 4: Split 03 evidence edges")
        print("=" * 60)
        edge03_split_files = step4_split_edge03(candidate_edges)

        print("\n" + "=" * 60)
        print("Step 5: Generate 02 causal-edge prompts")
        print("=" * 60)
        edge02_prompts = step5_generate_edge02_prompts(edge02_split_files)

        print("\n" + "=" * 60)
        print("Step 6: Generate 03 evidence-edge prompts")
        print("=" * 60)
        edge03_prompts = step6_generate_edge03_prompts(edge03_split_files)

        # Collect each batch's case_id range
        def _get_batch_case_ids(idx: int) -> list[str]:
            start = idx * BATCH_SIZE
            end = min(start + BATCH_SIZE, len(all_case_ids))
            return all_case_ids[start:end]

        # ── Run Step 7-9 batch by batch ──
        for batch_idx_t in target_batches:
            batch_case_ids = _get_batch_case_ids(batch_idx_t)
            print("\n" + "#" * 70)
            print(f"# Batch {batch_idx_t}/{total_batches - 1}: process {len(batch_case_ids)} papers")
            print(f"#  case_id range: {batch_case_ids[0]} ~ {batch_case_ids[-1]}")
            print("#" * 70)

            # Callback: persist progress when batch is complete
            def on_batch_done(b_idx: int, c_ids: list[str], calls: int, edges_n: int):
                mark_batch_done(_progress_state, b_idx, c_ids, calls, edges_n)

            try:
                print("\n" + "=" * 60)
                print(f"[Batch {batch_idx_t}] Step 7: concurrently call LLM to extract edge descriptions (02 / 03)")
                print("=" * 60)
                edge02_results, edge03_results = step7_call_llm_parallel(
                    edge02_prompts, edge03_prompts, pdf_map, LLM_CONFIG, key_manager, logger,
                    skip_existing=args.skip_existing,
                    # max_concurrent strictly equals the number of keys, ensuring all 10 keys are called simultaneously.
                    # (The old implementation used total_keys * PER_KEY_LIMIT=30, which produced "same-key multi-request"
                    #  triggering server rate-limiting, causing some keys to actually idle -- "fake" concurrency.)
                    max_concurrent=key_manager.total_keys,
                    batch_case_ids=batch_case_ids,
                    batch_idx=batch_idx_t,
                    on_batch_done=on_batch_done,
                )
                step7_save_results(edge02_results, edge03_results)

                print("\n" + "=" * 60)
                print(f"[Batch {batch_idx_t}] Step 8: back-fill edge_description + null statistics")
                print("=" * 60)
                # Only back-fill on this batch's candidate edges
                batch_candidate_edges = [
                    p for p in candidate_edges
                    if p.get("case_id") in set(batch_case_ids)
                ]
                candidate_edges_batch, null_list, null_count, total_edges = step8_backfill_and_statistics(
                    batch_candidate_edges, edge02_results, edge03_results
                )

                print("\n" + "=" * 60)
                print(f"[Batch {batch_idx_t}] Step 9: generate extracted edge-relations and save")
                print("=" * 60)
                final_edges = step9_finalize_and_save(
                    candidate_edges_batch,
                    batch_case_ids=batch_case_ids,
                    batch_idx=batch_idx_t,
                )
            except KeyboardInterrupt:
                print(f"\n[Batch {batch_idx_t}] User interrupted (Ctrl+C). This batch is not marked complete; the next run will automatically resume from the next pending batch.")
                # Do not mark complete, exit directly
                return
            except Exception as e:
                print(f"\n[Batch {batch_idx_t}] Exception: {e}")
                import traceback
                traceback.print_exc()
                print(f"[Batch {batch_idx_t}] This batch is not marked complete; the next run will automatically retry this batch.")
                # Do not mark complete, exit directly, let the user decide whether to continue
                return

    # ── Save stats JSON (for the standalone plotting tool to read) ──
    ts = time.strftime("%Y%m%d_%H%M%S")
    if build_stats_data is not None:
        try:
            stats = build_stats_data(_prompt_stats)
            stats_json_path = os.path.join(EDGE_OUTPUT_ROOT, f"edge_stats_{ts}.json")
            with open(stats_json_path, "w", encoding="utf-8") as f:
                json.dump({"prompt_stats": _prompt_stats, "stats_summary": stats}, f, ensure_ascii=False, indent=2)
            print(f"[Stats] Token statistics JSON saved: {stats_json_path}")
        except Exception as e:
            print(f"[Stats] Warning: statistics JSON save failed (does not affect extraction result): {e}")
    else:
        print("[Stats] Skipped: zotero_edge_extractor_plot_v5 not available")

    print("\n" + "=" * 60)
    print("Edge-relation extraction pipeline done!")
    print("=" * 60)

    # Print batch execution summary
    print("\n[Batch execution summary]")
    done_batches = [b for b in _progress_state["batches"].values() if b.get("done")]
    pending_batches = [b for b in _progress_state["batches"].values() if not b.get("done")]
    print(f"  Total batches: {len(_progress_state['batches'])} | This run done: {len([b for b in done_batches if b.get('completed_at','').startswith(ts[:8])])} | Cumulative done: {len(done_batches)} | Remaining: {len(pending_batches)}")
    for b in done_batches:
        cids = b.get("case_ids", [])
        if cids:
            print(f"    Batch{b['batch_index']:03d}: {len(cids)} papers, {b.get('edges_extracted',0)} edges, completed at {b.get('completed_at','?')}")
    if pending_batches:
        print(f"\n  Tip: {len(pending_batches)} batches are still pending; you can rerun this program to continue.")
        print(f"  Progress file: {_progress_file_path()}")

    if key_manager:
        usage = key_manager.usage_report()
        total_assigned = sum(usage.values())
        print(f"\nAPI Key usage statistics (this run, total {total_assigned} calls):")
        for i, k in enumerate(keys):
            count = usage.get(k, 0)
            pct = (count / total_assigned * 100) if total_assigned > 0 else 0
            print(f"  Key {i+1} ({k[:10]}...{k[-4:]}): {count} calls ({pct:.0f}%)")
    print("=" * 70)


if __name__ == "__main__":
    main()
