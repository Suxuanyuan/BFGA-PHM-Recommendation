# -*- coding: utf-8 -*-
"""
Knowledge Graph papers & nodes attribute merge/disambiguation program V5
========================================================================
Features:
  Read "node JSON" and construct a "graph JSON array", then summarize and merge node_description_list via LLM.

Processing steps:
  1. Read the node JSON and extract papers metadata and the nodes array.
  2. Traverse and merge papers: each case's metadata forms one paper object.
  3. Traverse and merge nodes:
     - Group by (node_type, node_name) and deduplicate/merge
     - Fields: node_description_list, node_id_list, cite_score_list, etc.
  4. Determine node_description_list:
     - If all descriptions are essentially identical (ignoring case/spaces), the program picks the shortest element directly, skipping LLM
     - For induction-type nodes (type contains -Induction) with inconsistent descriptions, invoke the dedicated deep-induction prompt
     - For other inconsistent cases, invoke the standard induction prompt

LLM configuration:
  - provider: gemini
  - model: gemini-3-flash-preview
  - base_url: https://YOUR.LLM.ENDPOINT/  (set BFGA_LLM_API_URL)
  - timeout: 300s
  - api_keys: 3 keys round-robin, max concurrency 6 (3 keys * 2)

Output:
  - Graph JSON array (papers + nodes)
  - Save path: C1-common-graph_paper&nodes_merge/[original_filename]_papers&nodes_merged.json
"""

import os
import re
import json
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock, Semaphore

# ============================================================================
# User configuration
# ============================================================================

INPUT_JSON_PATH = (
    # NOTE: relative path placeholder for code review / publication
    r"./data/03_induction/A2-merged_nodes_disambiguation_induction/[2277EAKD][ZZZRPFBV]_merged_nodes_normalized_disambiguated_induced_hyperparams.json"
)

OUTPUT_DIR = (
    # NOTE: relative path placeholder for code review / publication
    r"./data/03_induction/C1-common-graph_paper_and_nodes_merge"
)

# LLM API configuration (multi-key round-robin)
MULTI_API_KEYS = [
    # NOTE: provide your own API keys here
]

LLM_MODEL = "gemini-3.5-flash"
LLM_BASE_URL = os.environ.get("BFGA_LLM_API_URL", "https://YOUR.LLM.ENDPOINT/")
LLM_TIMEOUT = 300

# Maximum concurrent requests each API key can hold at the same time
# 10 keys * 3 concurrency = 30 global concurrent, matching the concurrency model of the v8 edge-relation extractor
PER_KEY_CONCURRENCY = 3
# Global max concurrency = key count * per-key concurrency
_MAX_CONCURRENT = len(MULTI_API_KEYS) * PER_KEY_CONCURRENCY


# ============================================================================
# Constants
# ============================================================================

NODE_TYPE_ORDER = {
    "01-Object Domain": 1,
    "02-Object Type": 2,
    "03-Operating Conditions": 3,
    "04-Fault Location": 4,
    "05-Fault Mode": 5,
    "06-Fault Severity": 6,
    "07-Compound Fault": 7,
    "08-PHM Task": 8,
    "09-Problem Scenario": 9,
    "10-Dataset": 10,
    "11-Sensor Information": 11,
    "12-Training Data Availability": 12,
    "13-Noise Level": 13,
    "14-Computational Resource": 14,
    "15-Data Preprocessing Algorithm": 15,
    "16-Feature Extraction Algorithm": 16,
    "17-Core Classifier Algorithm": 17,
    "18-Data Generation Algorithm": 18,
    "19-Training Optimization Algorithm": 19,
    "20-Algorithm Importance Classification": 20,
    "15-Data Preprocessing Algorithm-Induction": 21,
    "16-Feature Extraction Algorithm-Induction": 22,
    "17-Core Classifier Algorithm-Induction": 23,
    "18-Data Generation Algorithm-Induction": 24,
    "19-Training Optimization Algorithm-Induction": 25,
}

# Format constraint of node_description for each type (from v5 version prompt md file)
NODE_DESCRIPTION_FORMAT_RULES = {
    "01-Object Domain": "中文描述领域，1-3句，仅描述本文实验涉及的领域。",
    "02-Object Type": "中文描述具体设备，仅描述本文实验涉及的设备。",
    "03-Operating Conditions": "2段式——第1段数量及类型，第2段各工况参数及数值。",
    "04-Fault Location": "中文描述具体位置，仅描述本文实验涉及的部位。",
    "05-Fault Mode": "中文描述具体故障表现形式（物理机制或损伤类型）。",
    "06-Fault Severity": "2段式——第1段数量及类型，第2段各等级数值。",
    "07-Compound Fault": "2段式——第1段类型，第2段具体组合或原因。",
    "08-PHM Task": "中文描述具体PHM任务。",
    "09-Problem Scenario": "中文描述具体问题场景。",
    '10-Dataset': '格式为【类别】+【描述】，类别为"公开数据集"或"私有数据集（自采）"或"私有数据集（仿真）"。',
    "11-Sensor Information": "中文描述传感器类型、安装位置等，仅描述本文实验使用的传感器。",
    "12-Training Data Availability": "描述具体样本量及判定依据。",
    "13-Noise Level": "描述噪声水平信息。",
    "14-Computational Resource": "描述具体资源消耗情况。",
    "15-Data Preprocessing Algorithm": "中文描述该算法在本文中的作用；未提及则填'未提及'。",
    "16-Feature Extraction Algorithm": "中文描述该算法在本文中的作用；未提及则填'未提及'。",
    "17-Core Classifier Algorithm": "中文描述该算法在本文中的作用。",
    "18-Data Generation Algorithm": "中文描述该算法在本文中的作用；未提及则填'未提及'。",
    "19-Training Optimization Algorithm": "中文描述该算法在本文中的作用；未提及则填'未提及'。",
    "20-Algorithm Importance Classification": "格式为【node_id】(<一句话描述>)→<等级>，用分号分隔，例如：15(信号归一化)→一般重要性；16(1DCNN特征提取)→最高重要性。",
    "15-Data Preprocessing Algorithm-Induction": "归纳类别内涵：描述该类算法的通用原理；再描述本文具体应用及适应性。",
    "16-Feature Extraction Algorithm-Induction": "归纳类别内涵：描述该类算法的通用原理；再描述本文具体应用及适应性。",
    "17-Core Classifier Algorithm-Induction": "归纳类别内涵：描述该类算法的通用原理；再描述本文具体应用及适应性。",
    "18-Data Generation Algorithm-Induction": "归纳类别内涵：描述该类算法的通用原理；再描述本文具体应用及适应性。",
    "19-Training Optimization Algorithm-Induction": "归纳类别内涵：描述该类算法的通用原理；再描述本文具体应用及适应性。",
}


# ============================================================================
# LLM call module
# ============================================================================


class RoundRobinKeyManager:
    """
    Multi-API-Key round-robin manager (thread-safe).

    - Holds multiple keys; each acquire() returns the next key in round-robin order
      and records the usage count.
    - Each key has an independent Semaphore (capacity = per_key_limit);
      the caller calls acquire() to atomically complete "select key + occupy slot",
      and finally calls release() to free.
    - Blocking implementation: when all keys are full, the caller blocks automatically
      in the acquire() phase (no spin needed), avoiding busy-wait CPU waste.

    Key design (avoiding "fake" concurrency):
        The old get_key() implementation broke immediately on "full slot" while
        scanning all keys, causing all threads to pile tasks onto key[0] while
        leaving the other 9 keys idle.

        The new implementation adopts a **true round-robin + slot-aware** hybrid scheduler:
          1) acquire() only selects the subset of keys with the most remaining slots
             (avoiding piling tasks into already-full keys).
          2) Within that subset, the atomic round-robin cursor _rr_cursor picks the
             next key, ensuring 10 keys are evenly distributed under high concurrency
             without the "key[0] queued, key[9] idle" pseudo-concurrency.
          3) Selecting key + occupying slot + recording usage all happen under the
             same lock, keeping external state consistent.
    """

    def __init__(self, keys: list[str], per_key_limit: int = 3):
        self._keys = keys
        self._n = len(keys)
        self._lock = Lock()
        self._usage: dict[str, int] = {k: 0 for k in keys}  # cumulative usage count for each key
        self._sems: list[Semaphore] = [Semaphore(per_key_limit) for _ in keys]
        self._per_key_limit = per_key_limit
        # Round-robin cursor used to evenly distribute across the set of keys with the most remaining slots.
        # Must be read/written under lock; the initial value is randomized to avoid all threads grabbing the same key at startup.
        self._rr_cursor = 0

    @property
    def total_keys(self) -> int:
        return self._n

    @property
    def per_key_limit(self) -> int:
        return self._per_key_limit

    def acquire(self) -> tuple[str, int]:
        """
        Atomic operation: under the lock, complete "balanced key selection + occupying one concurrent slot of that key".

        Scheduling strategy (true concurrency):
          a) First scan all keys and pick the subset best_idxs with the most remaining slots;
          b) If the subset is non-empty: pick a key within best_idxs by the round-robin cursor,
             advance the cursor by 1 (mod subset size) after picking, so the next call falls to the next key.
          c) If the subset is empty (all keys full): fall back to picking the key with the largest
             _value among all keys (ensuring at least one can acquire successfully), acquire directly
             without advancing the cursor.

        Returns:
            (key, key_idx) — the caller must eventually call release(key_idx).
        """
        with self._lock:
            # 1) Find the set of keys with the most remaining slots
            best_free = -1
            best_idxs: list[int] = []
            for i in range(self._n):
                free = self._sems[i]._value
                if free > best_free:
                    best_free = free
                    best_idxs = [i]
                elif free == best_free:
                    best_idxs.append(i)

            if best_idxs:
                # 2) Within best_idxs, pick one key by round-robin
                m = len(best_idxs)
                pos = self._rr_cursor % m
                key_idx = best_idxs[pos]
                self._rr_cursor = (self._rr_cursor + 1) % 1_000_003
            else:
                # 3) Fallback: all keys are full, pick the key with the largest _value
                #    (indicates counter drift, still let it acquire, relying on Semaphore internal blocking as fallback)
                key_idx = max(range(self._n), key=lambda i: self._sems[i]._value)

            key = self._keys[key_idx]
            self._usage[key] = self._usage.get(key, 0) + 1
            # In-lock acquire always succeeds (if best_free>0), and stays consistent with get.
            # If the fallback branch is taken, best_free<=0, acquire will block — but this only happens when
            # all slots are full, which is the expected behavior.
            self._sems[key_idx].acquire()
            return key, key_idx

    def release(self, key_idx: int):
        """Release one concurrency slot of the key corresponding to key_idx."""
        if 0 <= key_idx < self._n:
            self._sems[key_idx].release()

    def usage_report(self) -> dict[str, int]:
        with self._lock:
            return dict(self._usage)


def _call_gemini(prompt: str, config: dict, api_key: str) -> dict:
    """Gemini API call."""
    try:
        import google.genai as genai
        from google.genai.types import HttpOptions
    except ImportError:
        raise ImportError("Please install first: pip install google-genai")

    base = config.get("base_url", "https://generativelanguage.googleapis.com/").strip()
    if not base.endswith("/"):
        base += "/"
    timeout_ms = max(1, int(float(config.get("timeout", 300)) * 1000))

    extra_headers = {}
    if api_key.startswith("sk-"):
        extra_headers["Authorization"] = f"Bearer {api_key}"

    http_opts = HttpOptions(base_url=base, timeout=timeout_ms, headers=extra_headers or None)
    client = genai.Client(api_key=api_key, http_options=http_opts)

    model_name = config.get("model", "gemini-3-flash-preview")
    response = client.models.generate_content(
        model=model_name,
        contents=[prompt],
        config={"temperature": 0, "max_output_tokens": 8000},
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
        text = "".join(part.text for part in parts if hasattr(part, "text") and part.text)
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


def _extract_json_from_response(text: str):
    """Extract JSON from the LLM response text."""
    text = text.strip()
    if not text:
        return None

    fence_pattern = re.compile(r'^```(?:\w*)', re.MULTILINE)
    fences = [(m.start(), m.group()) for m in fence_pattern.finditer(text)]
    if fences:
        start_pos, fence_str = fences[0]
        content = text[start_pos + len(fence_str):]
        if content.startswith("\n"):
            content = content[1:]
        end_fence_pos = content.find("```")
        if end_fence_pos != -1:
            content = content[:end_fence_pos]
        content = content.strip()
        if content.startswith("[") or content.startswith("{"):
            try:
                return json.loads(content)
            except json.JSONDecodeError:
                pass

    # Try direct JSON parse
    for start in (text.find("["), text.find("{")):
        if start == -1:
            continue
        sub = text[start:]
        try:
            return json.loads(sub)
        except json.JSONDecodeError:
            continue
    return None


# ============================================================================
# LLM merge node_description
# ============================================================================


def _normalize_description(desc: str) -> str:
    """
    Normalize a description: strip leading/trailing whitespace, lowercase, collapse spaces,
    used to determine whether two descriptions are "essentially identical".
    """
    if not desc:
        return ""
    desc = desc.strip()
    desc = re.sub(r"\s+", " ", desc)  # collapse internal whitespace
    return desc.lower()


def are_descriptions_essentially_identical(desc_list: list[str]) -> bool:
    """
    Determine whether all non-empty descriptions in desc_list are "essentially identical" (ignoring case and excess spaces).
    Return True if identical (no LLM needed); return False if not (LLM induction required).
    """
    non_empty = [_normalize_description(d) for d in desc_list if _normalize_description(d)]
    if not non_empty:
        return True
    return len(set(non_empty)) == 1


def _pick_one_element(desc_list: list[str]) -> str:
    """
    Pick one non-empty element string from desc_list and return it.
    Prefer the shortest (non-redundant) one to keep the result concise.
    """
    candidates = [d.strip() for d in desc_list if d.strip()]
    if not candidates:
        return ""
    candidates.sort(key=len)
    return candidates[0]


# Induction-type node_type (requires two-part format: general principle + specific application)
_INDUCTION_TYPES = {
    "15-Data Preprocessing Algorithm-Induction",
    "16-Feature Extraction Algorithm-Induction",
    "17-Core Classifier Algorithm-Induction",
    "18-Data Generation Algorithm-Induction",
    "19-Training Optimization Algorithm-Induction",
}


def _build_merge_prompt(node: dict) -> str:
    """
    Build a node_description merge prompt for a single node (output English).

    Output is two-part: <abstract generalization> | <2-3 representative examples>,
    applicable to "non-induction + inconsistent description" nodes.
    """
    nid = node.get("node_id", "")
    node_type = node.get("node_type", "")
    node_name = node.get("node_name", "") or "(empty)"
    desc_list = node.get("node_description_list", [])

    format_rule = NODE_DESCRIPTION_FORMAT_RULES.get(
        node_type,
        "English description, concise, 1-3 sentences."
    )

    desc_items = []
    for i, desc in enumerate(desc_list):
        desc_items.append(f"  Description {i + 1}: {desc}")

    if not desc_items:
        return None

    desc_text = "\n".join(desc_items)

    prompt = f"""You are a PHM (Prognostics and Health Management) domain knowledge graph construction expert.

## Task
Given the original descriptions of the same common node from multiple papers, synthesize them into ONE generalized description. Output must be in **English**.

## Node Info
- Node ID: {nid}
- Node Type: {node_type}
- Node Name: {node_name}
- Number of source descriptions: {len(desc_list)}

## Format Constraint
{format_rule}

## Source Descriptions (Chinese original)
{desc_text}

## Output Structure
The output MUST strictly follow this TWO-PART structure:

  <Abstract generalization> | <Refined summary of real instances from node_description_list, no more than 3>

Where:
  - Part 1 (Abstract generalization): Distill the SHARED, GENERALIZABLE pattern that underlies all source descriptions. Describe what is COMMON across papers — do NOT list individual instance details.
  - Part 2 (Examples): From the EXACT instances that appear in the source descriptions, select and briefly summarize no more than 3 representative ones to illustrate the generalization. Use semicolons to separate examples.

## Strict Output Requirements
1. Output MUST be a SINGLE LINE of text following the "<generalization> | <examples>" structure above.
2. Part 1 must be ABSTRACT and GENERAL — focus on the shared principle. Do NOT enumerate or list individual source details.
3. Part 2 must contain NO MORE THAN 3 concrete examples drawn EXACTLY from the source descriptions (use semicolons as separators). Summarize each example concisely.
4. The output must be DIRECTLY usable as a node_description value — no thinking steps, no reasoning process, no reasoning traces, no analysis, no preamble, no self-references, no markdown fences, no prefix text.
5. ABSOLUTELY FORBIDDEN in the output: any thinking/reasoning text (e.g., "I think", "Based on", "First", "Then", "In summary", "Okay", "Here's what", "I see", "Sure"), any markdown/special characters (e.g., **, ##, ===, >, -, _, `, #, [], <>, ||, ~~), and any self-referential phrases (e.g., "The description", "the node", "this node", "as shown").
6. No Chinese characters, no 【】, ##, ===, or any other markup symbols in the output.

Output the merged description directly:
"""
    return prompt


def _build_merge_prompt_for_induction(node: dict) -> str:
    """
    Build a more detailed induction prompt for induction-type nodes (type name contains -Induction).

    Output is two-part: <abstract generalization> | <2-3 representative examples>,
    guiding the LLM to abstract the commonality rather than accumulate a union.
    """
    nid = node.get("node_id", "")
    node_type = node.get("node_type", "")
    node_name = node.get("node_name", "") or "(empty)"
    desc_list = node.get("node_description_list", [])

    format_rule = NODE_DESCRIPTION_FORMAT_RULES.get(
        node_type,
"Induction category meaning: describe the general principle of this class of algorithms; then describe the specific application and adaptability in this paper."
    )

    desc_items = []
    for i, desc in enumerate(desc_list):
        desc_items.append(f"  Description {i + 1}: {desc}")

    if not desc_items:
        return None

    desc_text = "\n".join(desc_items)

    prompt = f"""You are a PHM (Prognostics and Health Management) domain knowledge graph construction expert.

## Task
Given the original descriptions of the same common Induction-type node from multiple papers, synthesize them into ONE generalized description. The output must be in **English**.

## Node Info
- Node ID: {nid}
- Node Type: {node_type}
- Node Name: {node_name}
- Number of source descriptions: {len(desc_list)}

## Format Constraint
{format_rule}

## Source Descriptions (Chinese original)
{desc_text}

## Output Structure
The output MUST strictly follow this TWO-PART structure:

  <Abstract generalization> | <Refined summary of real instances from node_description_list, no more than 3>

Where:
  - Part 1 (Abstract generalization): Distill the SHARED, GENERALIZABLE pattern that underlies all source descriptions. Focus on the COMMON principle — do NOT enumerate individual instance details.
  - Part 2 (Examples): From the EXACT instances that appear in the source descriptions, select and briefly summarize no more than 3 representative ones to illustrate the generalization. Use semicolons to separate examples.

## Strict Output Requirements
1. Output MUST be a SINGLE LINE of text following the "<generalization> | <examples>" structure above.
2. Part 1 must be ABSTRACT and GENERAL — focus on the shared principle. Do NOT enumerate or list individual source details.
3. Part 2 must contain NO MORE THAN 3 concrete examples drawn EXACTLY from the source descriptions (use semicolons as separators). Summarize each example concisely.
4. The output must be DIRECTLY usable as a node_description value — no thinking steps, no reasoning process, no reasoning traces, no analysis, no preamble, no self-references, no markdown fences, no prefix text.
5. ABSOLUTELY FORBIDDEN in the output: any thinking/reasoning text (e.g., "I think", "Based on", "First", "Then", "In summary", "Okay", "Here's what", "I see", "Sure"), any markdown/special characters (e.g., **, ##, ===, >, -, _, `, #, [], <>, ||, ~~), and any self-referential phrases (e.g., "The description", "the node", "this node", "as shown").
6. No Chinese characters, no 【】, ##, ===, or any other markup symbols in the output.

Output the merged description directly:
"""
    return prompt


def merge_node_descriptions_llm(
    nodes: list,
    llm_config: dict,
    api_keys: list,
    max_concurrent: int = _MAX_CONCURRENT,
) -> tuple[list, dict]:
    """
    Call the LLM in batch for all nodes that need to be merged (multi-key round-robin).

    Classification logic:
      - Identical nodes (desc essentially the same): the program picks the shortest element directly, skipping LLM
      - Non-induction inconsistent nodes: invoke the standard prompt _build_merge_prompt
      - Induction inconsistent nodes: invoke the dedicated prompt _build_merge_prompt_for_induction

    Returns:
        nodes: updated node list (node_description populated)
        stats: {"success": int, "failed": int, "total_tokens": int, "skip_llm": int, ...}
    """
    # Classify
    needs_llm_induction = []   # (idx, node)
    needs_llm_standard = []     # (idx, node)
    needs_skip = []             # (idx, node)

    for i, n in enumerate(nodes):
        desc_list = n.get("node_description_list", [])
        if len(desc_list) < 2:
            continue
        if are_descriptions_essentially_identical(desc_list):
            needs_skip.append((i, n))
        elif n.get("node_type", "") in _INDUCTION_TYPES:
            needs_llm_induction.append((i, n))
        else:
            needs_llm_standard.append((i, n))

    print(f"\n[LLM] Nodes to merge: {len(needs_llm_induction) + len(needs_llm_standard) + len(needs_skip)}")
    print(f"      - Skipped LLM (descriptions identical): {len(needs_skip)}")
    print(f"      - LLM needed (standard induction):   {len(needs_llm_standard)}")
    print(f"      - LLM needed (deep induction):   {len(needs_llm_induction)}")

    # Classify and process: skip-LLM nodes pick the shortest element directly
    for idx, node in needs_skip:
        nodes[idx]["node_description"] = _pick_one_element(node.get("node_description_list", []))

    all_to_call = needs_llm_induction + needs_llm_standard

    if not all_to_call:
        stats = {"success": 0, "failed": 0, "total_tokens": 0, "total_input": 0, "skip_llm": len(needs_skip)}
        return nodes, stats

    key_manager = RoundRobinKeyManager(api_keys, per_key_limit=PER_KEY_CONCURRENCY)
    results = {}  # idx -> merged_description
    stats = {"success": 0, "failed": 0, "total_tokens": 0, "total_input": 0, "skip_llm": len(needs_skip)}

    def _do_call(idx: int, node: dict, use_induction_prompt: bool) -> tuple:
        # Select prompt builder by node_type
        prompt_builder = _build_merge_prompt_for_induction if use_induction_prompt else _build_merge_prompt
        prompt = prompt_builder(node)
        if not prompt:
            return idx, node.get("node_description_list", [""])[0], 0, 0, ""

            # Atomically "balance-select key + occupy concurrency slot": avoid the old implementation where
        # get/acquire was separated, causing multiple threads to select the same key and block at the same time ("fake concurrency").
        key, key_idx = key_manager.acquire()
        try:
            resp = _call_gemini(prompt, llm_config, key)
            if resp.get("error"):
                raise RuntimeError(resp["error"])
            merged_text = resp.get("text", "").strip()
            if not merged_text:
                merged_text = node.get("node_description_list", [""])[0]
            return idx, merged_text, resp.get("input_tokens", 0), resp.get("output_tokens", 0), ""
        except Exception as ex:
            return idx, node.get("node_description_list", [""])[0], 0, 0, str(ex)
        finally:
            key_manager.release(key_idx)

    t0 = time.time()
    print(f"[LLM] Starting concurrent calls (global concurrency={max_concurrent}, "
          f"keys={len(api_keys)}, per-key concurrency={PER_KEY_CONCURRENCY})...")

    with ThreadPoolExecutor(max_workers=max_concurrent) as executor:
        futures = {}
        for idx, node in needs_llm_induction:
            futures[executor.submit(_do_call, idx, node, True)] = idx
        for idx, node in needs_llm_standard:
            futures[executor.submit(_do_call, idx, node, False)] = idx

        done_count = 0
        for future in as_completed(futures):
            done_count += 1
            idx, merged_text, inp, out, err = future.result()
            results[idx] = merged_text
            stats["total_tokens"] += inp + out
            stats["total_input"] += inp
            if err:
                stats["failed"] += 1
                print(f"      [{done_count}/{len(all_to_call)}] Failed [{nodes[idx]['node_id']}] {err[:60]}")
            else:
                stats["success"] += 1
                if done_count % 10 == 0 or done_count == len(all_to_call):
                    elapsed = time.time() - t0
                    rate = done_count / elapsed if elapsed > 0 else 0
                    print(f"      [{done_count}/{len(all_to_call)}] Success {stats['success']} / Failed {stats['failed']} | {rate:.1f} calls/sec")

    # Update node
    for idx, merged_text in results.items():
        nodes[idx]["node_description"] = merged_text

    elapsed = time.time() - t0
    print(f"[LLM] Done! Success: {stats['success']} / Failed: {stats['failed']} / Skipped: {stats['skip_llm']} | "
          f"Total tokens: {stats['total_tokens']} | Elapsed: {elapsed:.1f}s")

    # Print usage of each key to confirm the 10 keys are truly evenly called (fake-concurrency detection)
    usage = key_manager.usage_report()
    total_calls = sum(usage.values())
    if total_calls > 0:
        print(f"[LLM] Key call distribution (total {len(usage)} keys, total calls {total_calls}):")
        for i, k in enumerate(api_keys):
            cnt = usage.get(k, 0)
            pct = cnt / total_calls * 100
            print(f"      Key{i + 1:02d}: {cnt:>5d} times  ({pct:5.1f}%)  {k[:10]}...{k[-4:]}")

    return nodes, stats


# ============================================================================
# Utility functions
# ============================================================================


def get_type_order(node_type: str) -> int:
    return NODE_TYPE_ORDER.get(node_type, 99)


def safe_float(val, default: float = 0.0) -> float:
    try:
        return float(val) if val is not None else default
    except (ValueError, TypeError):
        return default


def safe_int(val, default: int = 0) -> int:
    try:
        return int(val) if val is not None else default
    except (ValueError, TypeError):
        return default


# ============================================================================
# Main processing functions
# ============================================================================


def load_node_json(path: str) -> list:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_papers(all_papers: list) -> list:
    papers = []
    for paper in all_papers:
        p = {
            "case_id": paper.get("case_id", ""),
            "paper_title": paper.get("paper_title", ""),
            "publish_year": paper.get("publish_year", ""),
            "publish_source": paper.get("publish_source", ""),
            "cite_count": paper.get("cite_count", 0),
            "algorithm_hyperparameters": paper.get("algorithm_hyperparameters", ""),
            "training_config": paper.get("training_config", ""),
            "performance_metrics": paper.get("performance_metrics", ""),
        }
        papers.append(p)
    return papers


def flatten_nodes(all_papers: list) -> list:
    flat = []
    for paper in all_papers:
        case_id = paper.get("case_id", "")
        paper_title = paper.get("paper_title", "")
        publish_year = paper.get("publish_year", "")
        for node in paper.get("nodes", []):
            n = dict(node)
            n["_source_case_id"] = case_id
            n["_source_paper_title"] = paper_title
            n["_source_publish_year"] = publish_year
            flat.append(n)
    return flat


# node_type order mapping (used to determine whether a node is an algorithm-type node 15-19)
def _type_num(node_type: str) -> int:
    m = re.match(r"(\d+)", node_type)
    return int(m.group(1)) if m else 99


# node_importance rank (used to pick the lowest rank on ties)
IMPORTANCE_RANK = {"Highest Importance": 1, "General Importance": 2, "Not Mentioned": 3}


def _compute_node_importance(importance_list: list) -> str | None:
    """
    Count node_importance_list and return the most frequent value.
    On ties, pick the lowest rank: Highest Importance > General Importance > Not Mentioned.
    If the list is empty or all empty strings, return null.
    """
    filtered = [v for v in importance_list if v]  # remove empty strings
    if not filtered:
        return None

    # aggregate frequency
    counts = {}
    for v in filtered:
        counts[v] = counts.get(v, 0) + 1

    max_count = max(counts.values())
    # candidates with the maximum count
    candidates = [v for v, c in counts.items() if c == max_count]
    if len(candidates) == 1:
        return candidates[0]

    # tie: pick the lowest rank
    candidates.sort(key=lambda v: IMPORTANCE_RANK.get(v, 99))
    return candidates[0]


def _migrate_importance_to_induction_nodes(merged: list):
    """
    Augmentation logic of node_importance_list for induction-type nodes.

    Traverse all induction-type nodes (node_type contains -Induction), and migrate node_importance
    from non-induction algorithm nodes (node_type is 15-19 without -Induction) merged in the same batch
    into the node_importance_list of induction-type nodes, by matching the node_id_list index relationship.

    Algorithm node_id extraction rule: split by "_", take the string before "_".
    Example: C00174_19_N1-Induction -> algorithm node_id = C00174_19
    """

    # 1. Build the precise algo_node_id -> importance mapping (one-to-one by index)
    #    Extracted from all non-induction algorithm nodes (15-19, without -Induction).
    #    Key: node_id_list[i] corresponds to node_importance_list[i], paired by index.
    algo_imp_map = {}  # algo_node_id -> importance string
    for n in merged:
        nt = n.get("node_type", "")
        if "Induction" in nt:
            continue
        tn = _type_num(nt)
        if 15 <= tn <= 19:
            nlist = n.get("node_id_list", [])
            imp_list = n.get("node_importance_list", [])
            for i, algo_id in enumerate(nlist):
                # algorithm node_id takes the string before "_"
                algo_node_id = algo_id.split("-")[0].rsplit("_", 1)[0]
                # take value precisely by index
                if i < len(imp_list):
                    algo_imp_map[algo_node_id] = imp_list[i]

    # 2. Traverse induction-type nodes, augment node_importance_list
    updated_count = 0
    for n in merged:
        nt = n.get("node_type", "")
        if nt not in _INDUCTION_TYPES:
            continue

        nlist = n.get("node_id_list", [])
        if not nlist:
            continue

        # Extract the algorithm importance value of each source from node_id_list (filter empty strings)
        migrated_imp = []
        for src_id in nlist:
            # Extract algorithm node_id (strip possible -Induction suffix, take part before "_")
            algo_node_id = src_id.split("-")[0].rsplit("_", 1)[0]
            imp_val = algo_imp_map.get(algo_node_id)
            if imp_val:  # filter empty/None
                migrated_imp.append(imp_val)

        if migrated_imp:
            existing = n.get("node_importance_list", [])
            # filter empty strings already in the array (may be filled under hot-start scenario)
            existing_clean = [v for v in existing if v]
            # avoid duplicate append
            new_values = [v for v in migrated_imp if v not in existing_clean]
            if new_values:
                n["node_importance_list"] = existing_clean + new_values
                updated_count += 1

    # 3. Compute node_importance for induction-type nodes (consistent with _compute_node_importance logic)
    for n in merged:
        nt = n.get("node_type", "")
        if nt not in _INDUCTION_TYPES:
            continue
        imp_list = n.get("node_importance_list", [])
        n["node_importance"] = _compute_node_importance(imp_list)

    print(f"    Induction node importance migration completed; updated {updated_count} nodes")


def merge_nodes(flat_nodes: list, paper_map: dict) -> list:
    groups = defaultdict(list)
    for n in flat_nodes:
        key = (n.get("node_type", ""), n.get("node_name", ""))
        groups[key].append(n)

    merged = []
    for (node_type, node_name), members in groups.items():
        is_algo_type = 15 <= _type_num(node_type) <= 19

        node_id_list = [m.get("node_id", "") for m in members]
        node_description_list = [m.get("node_description", "") or "" for m in members]
        node_cite_score_list = [safe_float(m.get("node_cite_score", 0)) for m in members]
        node_cite_count_list = [safe_int(m.get("node_cite_count", 0)) for m in members]
        node_num = len(members)

        node_cite_score = round(sum(node_cite_score_list) / len(node_cite_score_list), 4) \
            if node_cite_score_list else 0.0
        node_cite_count = round(sum(node_cite_count_list) / len(node_cite_count_list), 2) \
            if node_cite_count_list else 0.0

        # node_importance_list: only collect for algorithm-type nodes (15-19); other types use empty array
        if is_algo_type:
            node_importance_list = [m.get("node_importance", "") for m in members if m.get("node_importance")]
            node_importance = _compute_node_importance(node_importance_list)
        else:
            node_importance_list = []
            node_importance = None

        # node_publish_year_list: record publish_year per source paper (no dedup)
        node_publish_year_list = []
        for m in members:
            case_id = m.get("_source_case_id", "")
            year = paper_map.get(case_id, "") or m.get("_source_publish_year", "")
            if year:
                node_publish_year_list.append(year)
        node_publish_year_list.sort(key=lambda y: (y or "", str(y or "")))

        if node_publish_year_list:
            year_values = [safe_int(y, 0) for y in node_publish_year_list]
            year_values = [y for y in year_values if y > 0]
            node_publish_year = round(sum(year_values) / len(year_values)) if year_values else None
        else:
            node_publish_year = None

        # node_description: when num=1, use the unique description directly; when num>=2, wait for LLM merge
        if node_num == 1 and node_description_list:
            initial_desc = node_description_list[0]
        else:
            initial_desc = "[Pending LLM merge]"

        # Strictly follow the canonical structure, no extra fields added
        merged_node = {
            "node_id": "",  # placeholder, unified numbering at the end
            "node_type": node_type,
            "node_name": node_name,
            "node_description_list": node_description_list,
            "node_description": initial_desc,
            "node_num": node_num,
            "node_cite_score_list": node_cite_score_list,
            "node_cite_count_list": node_cite_count_list,
            "node_cite_score": node_cite_score,
            "node_cite_count": node_cite_count,
            "node_weight": None,
            "node_id_list": node_id_list,
            "node_importance_list": node_importance_list,
            "node_importance": node_importance,
            "node_publish_year_list": node_publish_year_list,
            "node_publish_year": node_publish_year,
        }
        merged.append(merged_node)

    # Sort by type order (replace null node_name with empty string)
    merged.sort(key=lambda n: (get_type_order(n.get("node_type", "")),
                              n.get("node_name", "") or ""))

    # ── Augment induction-type node node_importance_list ──────────────────────
    # At this point all non-induction-type nodes have completed merge and pre-numbering preparation,
    # so it is safe to reference them.
    _migrate_importance_to_induction_nodes(merged)

    # Unified numbering
    for i, n in enumerate(merged):
        n["node_id"] = f"N{i + 1:04d}"

    return merged


def validate_merged_nodes(nodes: list) -> list:
    warnings = []
    for n in nodes:
        nid = n.get("node_id", "")
        n_type = n.get("node_type", "")
        n_name = n.get("node_name", "")
        num = n.get("node_num", 0)
        type_num = _type_num(n_type)
        is_algo = 15 <= type_num <= 19

        check_items = [
            ("node_description_list", len(n.get("node_description_list", [])), num),
            ("node_id_list", len(n.get("node_id_list", [])), num),
            ("node_cite_score_list", len(n.get("node_cite_score_list", [])), num),
            ("node_cite_count_list", len(n.get("node_cite_count_list", [])), num),
            ("node_publish_year_list", len(n.get("node_publish_year_list", [])), num),
        ]
        if is_algo:
            check_items.append(
                ("node_importance_list", len(n.get("node_importance_list", [])), num)
            )

        for field, actual, expected in check_items:
            if actual != expected:
                warnings.append(
                    f"  [{nid}] {n_type} / {n_name}: "
                    f"{field} length ({actual}) != node_num ({expected})"
                )
    return warnings


# ============================================================================
# Main flow
# ============================================================================


def main():
    print("=" * 70)
    print("Knowledge Graph papers & nodes attribute merge/disambiguation program V5")
    print("=" * 70)

    llm_config = {
        "provider": "gemini",
        "model": LLM_MODEL,
        "base_url": LLM_BASE_URL,
        "timeout": LLM_TIMEOUT,
    }

    # ── 1. Load data ────────────────────────────────────────────────
    print("\n[1/5] Loading node JSON...")
    all_papers = load_node_json(INPUT_JSON_PATH)
    print(f"      Loaded; total {len(all_papers)} papers")
    total_raw_nodes = sum(len(p.get("nodes", [])) for p in all_papers)
    print(f"      Total raw nodes: {total_raw_nodes}")

    # ── 2. Build papers array ───────────────────────────────────────
    print("\n[2/5] Building papers array...")
    papers = build_papers(all_papers)
    print(f"      papers count: {len(papers)}")

    # Build case_id -> publish_year mapping (for filling node_publish_year_list)
    paper_map = {}
    for paper in all_papers:
        case_id = paper.get("case_id", "")
        if case_id:
            paper_map[case_id] = paper.get("publish_year", "")

    # ── 3. Flatten and merge nodes array ───────────────────────────────────────
    print("\n[3/5] Flattening and merging nodes array...")
    flat_nodes = flatten_nodes(all_papers)
    merged_nodes = merge_nodes(flat_nodes, paper_map)
    print(f"      Total flattened nodes: {len(flat_nodes)}")
    print(f"      Nodes after merging: {len(merged_nodes)}")

    # ── 4. Data consistency check ────────────────────────────────────────
    print("\n[4/5] Data consistency check...")
    warnings = validate_merged_nodes(merged_nodes)
    if warnings:
        print(f"      Check found {len(warnings)} issues:")
        for w in warnings:
            print(w)
    else:
        print(f"      All {len(merged_nodes)} nodes passed the consistency check!")

    # ── 5. LLM merge node_description ────────────────────────────
    # Hot-start: if the output file already exists, first load existing node_description
    # fill results to avoid repeated LLM calls
    output_filename_candidate = os.path.join(
        OUTPUT_DIR,
        os.path.splitext(os.path.basename(INPUT_JSON_PATH))[0] + "_papers&nodes_merged.json"
    )
    # Hot-start: skipped (force re-call LLM to generate English descriptions)
    USE_HOT_START = True
    if USE_HOT_START and os.path.exists(output_filename_candidate):
        print("\n[5/5] LLM merge node_description (hot-start: reusing existing results)...")
        try:
            with open(output_filename_candidate, "r", encoding="utf-8") as f:
                prev_output = json.load(f)
            prev_nodes = {n["node_id"]: n for n in prev_output.get("nodes", [])}
            merged_count = 0
            for node in merged_nodes:
                nid = node["node_id"]
                if nid in prev_nodes:
                    prev_desc = prev_nodes[nid].get("node_description", "")
                    if prev_desc and prev_desc != "[Pending LLM merge]" and "Pending LLM" not in prev_desc:
                        node["node_description"] = prev_desc
                        merged_count += 1
            print(f"      Reused merged descriptions for {merged_count} nodes from existing file")
            llm_stats = {"success": merged_count, "failed": 0, "total_tokens": 0, "total_input": 0, "skip_llm": 0}
        except Exception as ex:
            print(f"      Hot-start read failed: {ex}, re-call LLM")
            merged_nodes, llm_stats = merge_node_descriptions_llm(
                merged_nodes, llm_config, MULTI_API_KEYS, _MAX_CONCURRENT
            )
    else:
        print("\n[5/5] LLM merge node_description...")
        merged_nodes, llm_stats = merge_node_descriptions_llm(
            merged_nodes, llm_config, MULTI_API_KEYS, _MAX_CONCURRENT
        )

    # ── Save output ──────────────────────────────────────────────────
    output = {
        "papers": papers,
        "nodes": merged_nodes,
    }

    # Final safety check: remove all empty strings from node_importance_list
    sanitized_count = 0
    for node in output["nodes"]:
        imp_list = node.get("node_importance_list", [])
        if imp_list and "" in imp_list:
            node["node_importance_list"] = [v for v in imp_list if v]
            sanitized_count += 1
    if sanitized_count > 0:
        print(f"    [Safety check] cleaned empty strings from {sanitized_count} nodes")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    input_basename = os.path.splitext(os.path.basename(INPUT_JSON_PATH))[0]
    output_filename = input_basename + "_papers&nodes_merged.json"
    output_path = os.path.join(OUTPUT_DIR, output_filename)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    size_kb = os.path.getsize(output_path) / 1024
    print(f"\n{'=' * 70}")
    print(f"Graph JSON generation complete!")
    print(f"Output path: {output_path}")
    print(f"File size: {size_kb:.1f} KB")
    print(f"papers: {len(papers)} | nodes: {len(merged_nodes)}")
    print(f"LLM merge: success {llm_stats['success']} / failed {llm_stats['failed']} / skipped {llm_stats.get('skip_llm', 0)}")
    print(f"LLM tokens: {llm_stats['total_tokens']} (in: {llm_stats['total_input']})")
    print(f"{'=' * 70}")

    # ── Print merged result preview ────────────────────────────────────────
    print("\nMerged result preview (first 2 per type):")
    type_groups = defaultdict(list)
    for n in merged_nodes:
        type_groups[n.get("node_type", "")].append(n)

    for nt in sorted(type_groups.keys(), key=get_type_order):
        members = type_groups[nt]
        print(f"\n  [{nt}] total {len(members)} nodes:")
        for n in members[:3]:
            nid = n["node_id"]
            name = n["node_name"] or "(empty)"
            num = n["node_num"]
            desc_preview = (n["node_description"] or "")[:60]
            print(f"    [{nid}] {name} (num={num})")
            print(f"      -> {desc_preview}...")
        if len(members) > 3:
            print(f"    ... {len(members) - 3} more nodes")

    return output_path


if __name__ == "__main__":
    main()
