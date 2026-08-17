# -*- coding: utf-8 -*-
"""
Node name disambiguation program V9 (LLM-assisted cross-ambiguity-group secondary disambiguation version)
=====================================================================
Functions:
  1. Load merged-node JSON (nested structure: 1571 papers x nodes arrays)
  2. Field adjustment: 6 existing fields + 6 new fields (null); rename node_case_id_list -> node_id_list
  3. Extract importance for algorithm-type nodes (15-19)
  4. Disambiguation eligibility check (node_name == null and node_original_name != "Not Mentioned")
  5. Disambiguation pipeline:
     5-2 String-normalization similarity > 0.9 -> directly merge
     5-3 Vector-semantic-embedding similarity > 0.85 -> merge / < 0.3 -> unambiguous
     5-4 Remaining nodes -> LLM disambiguation (single call per node_type)
  6. LLM-assisted cross-ambiguity-group secondary disambiguation check (NEW)
     For ambiguous groups produced by steps 5-2 and 5-3, check whether ambiguity still exists between different groups
  7. Save the disambiguation result JSON
  8. Generate 19-category disambiguation statistics tables by node_type (including Step 6 statistics)

Dependencies: pip install google-genai sentence-transformers
"""

import os
import re
import json
import time
import math
import html
import hashlib
from pathlib import Path
from typing import Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock, Semaphore
from collections import defaultdict

# ============================================================================
# Progress bar (no external dependency)
# ============================================================================

class ProgressBar:
    """Lightweight progress bar; displays real-time percentage and ETA (compatible with Windows GBK console)."""
    BAR_LEN = 30

    def __init__(self, total: int, desc: str = ""):
        self.total = total
        self.current = 0
        self.desc = desc
        self._last_pct = -1

    def update(self, n: int = 1):
        self.current += n
        pct = int(round(self.current / self.total * 100)) if self.total > 0 else 100
        if pct != self._last_pct:
            filled = int(round(self.BAR_LEN * self.current / max(self.total, 1)))
            bar = "=" * filled + "-" * (self.BAR_LEN - filled)
            print(f"\r  {self.desc} [{bar}] {pct:>3}% ({self.current}/{self.total})", end="", flush=True)
            self._last_pct = pct

    def finish(self):
        print(f"\r  {self.desc} [{'=' * self.BAR_LEN}] 100% ({self.current}/{self.total})", flush=True)

# ============================================================================
# User configuration
# ============================================================================

INPUT_JSON_PATH = r"./output/final_merged/A0-node_merged/[2277EAKD][ZZZRPFBV]_merged_nodes_conformance_audit_merged_conformance_audit.json"

OUTPUT_DIR = r"./output/final_merged/A1-node_merged_disambiguated"

PROMPT_DIR = r"./output/final_merged/A1-node_merged_disambiguated/disambiguation_prompts_md"

LLM_ASSIST_PROMPT_DIR = r"./output/final_merged/A1-node_merged_disambiguated/LLM_assisted_cross_group_disambiguation_prompts_md"

LLM_CONFIG = {
    "provider": "gemini",
    "model": "gemini-3.5-flash",
    "base_url": os.environ.get("BFGA_LLM_API_URL", "https://YOUR.LLM.ENDPOINT/"),
    "timeout": 300,
}

# IMPORTANT: Provide your own API keys before running. The list below should be filled with valid keys.
MULTI_API_KEYS = []

PER_KEY_CONCURRENCY = 3

# Disambiguation pipeline thresholds
STRING_SIM_THRESHOLD = 0.90
EMBED_SIM_HIGH = 0.85
EMBED_SIM_LOW = 0.30

# Retry configuration
MAX_RETRIES = 5
INITIAL_BACKOFF = 1.0
MAX_BACKOFF = 60.0

# ============================================================================
# Part 1: utility functions
# ============================================================================

def levenshtein_ratio(s1: str, s2: str) -> float:
    """Compute the Levenshtein edit-distance similarity (0~1) between two strings."""
    if s1 == s2:
        return 1.0
    if not s1 or not s2:
        return 0.0
    len1, len2 = len(s1), len(s2)
    if len1 > len2:
        s1, s2 = s2, s1
        len1, len2 = len2, len1
    prev_row = list(range(len1 + 1))
    curr_row = [0] * (len1 + 1)
    for i in range(1, len2 + 1):
        curr_row[0] = i
        for j in range(1, len1 + 1):
            cost = 0 if s2[i - 1] == s1[j - 1] else 1
            curr_row[j] = min(prev_row[j] + 1, curr_row[j - 1] + 1, prev_row[j - 1] + cost)
        prev_row, curr_row = curr_row, prev_row
    edit_dist = prev_row[len1]
    max_len = max(len(s1), len(s2))
    return 1.0 - edit_dist / max_len


def jaccard_similarity(s1: str, s2: str) -> float:
    """Compute the Jaccard word-set similarity (0~1) between two strings."""
    if not s1 or not s2:
        return 0.0
    words1 = set(re.findall(r'\w+', s1.lower()))
    words2 = set(re.findall(r'\w+', s2.lower()))
    if not words1 or not words2:
        return 0.0
    intersection = words1 & words2
    union = words1 | words2
    return len(intersection) / len(union)


def name_similarity(s1: str, s2: str) -> float:
    """Node-name similarity: Levenshtein Ratio * 0.6 + Jaccard * 0.4."""
    return levenshtein_ratio(s1, s2) * 0.6 + jaccard_similarity(s1, s2) * 0.4


def normalize_text_for_comparison(text: str) -> str:
    """String normalization: strip excess whitespace, lowercase, remove common leading/trailing punctuation."""
    if not text:
        return ""
    t = text.lower().strip()
    t = re.sub(r'\s+', ' ', t)
    t = re.sub(r'^[^\w]+|[^\w]+$', '', t)
    return t


def _build_tfidf_corpus(texts: list[str]) -> tuple[list[tuple[str, float]], list[float], list[list[float]]]:
    """Manual TF-IDF + cosine similarity (no sklearn required)."""
    docs: list[set] = []
    for t in texts:
        words = re.findall(r'\w+', t.lower())
        docs.append(set(words))
    vocab: dict = {}
    for words in docs:
        for w in words:
            if w not in vocab:
                vocab[w] = len(vocab)
    n_docs = len(texts)
    n_vocab = len(vocab)
    if n_vocab == 0:
        return [], [1.0] * n_docs, [[0.0] * n_vocab]
    df = [0] * n_vocab
    for words in docs:
        seen = set()
        for w in words:
            if w not in seen:
                seen.add(w)
                df[vocab[w]] += 1
    idfs = [(w, math.log((n_docs + 1) / (d + 1)) + 1) for w, d in zip(vocab.keys(), df)]
    tfidf_vectors: list[list[float]] = []
    doc_lengths: list[float] = []
    for words in docs:
        tf = [0.0] * n_vocab
        for w in words:
            if w in vocab:
                tf[vocab[w]] += 1
        if tf:
            max_tf = max(tf)
            if max_tf > 0:
                for i in range(n_vocab):
                    tf[i] = tf[i] / max_tf
        vec = []
        vec_sq_sum = 0.0
        for w, idf_val in idfs:
            w_idx = vocab.get(w, -1)
            if w_idx >= 0:
                tfidf = tf[w_idx] * idf_val
                vec.append(tfidf)
                vec_sq_sum += tfidf * tfidf
            else:
                vec.append(0.0)
        length = math.sqrt(vec_sq_sum) if vec_sq_sum > 0 else 1.0
        doc_lengths.append(length)
        tfidf_vectors.append([v / length for v in vec])
    return idfs, doc_lengths, tfidf_vectors


def description_similarity(s1: str, s2: str) -> float:
    """TF-IDF cosine similarity of node descriptions."""
    if not s1 or not s2:
        return 0.0
    if s1 == s2:
        return 1.0
    _, _, vectors = _build_tfidf_corpus([s1, s2])
    if len(vectors) < 2:
        return 0.0
    v1, v2 = vectors[0], vectors[1]
    return sum(a * b for a, b in zip(v1, v2))


# ============================================================================
# Part 2: embedding vector semantic similarity
# ============================================================================

class EmbeddingModel:
    """Sentence-Transformers embedding model (with lazy loading and caching)."""
    _instance: Optional['EmbeddingModel'] = None
    _lock_init = Lock()

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model_name = model_name
        self._model = None
        self._cache: dict[str, list[float]] = {}
        self._cache_lock = Lock()

    @classmethod
    def get_instance(cls) -> 'EmbeddingModel':
        if cls._instance is None:
            with cls._lock_init:
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance

    def _load_model(self):
        if self._model is None:
            try:
                from sentence_transformers import SentenceTransformer
            except ImportError:
                raise ImportError("Please install: pip install sentence-transformers")
            self._model = SentenceTransformer(self.model_name)

    def encode(self, texts: list[str], normalize: bool = True) -> list[list[float]]:
        """Return normalized vectors."""
        self._load_model()
        results: list[list[float]] = []
        uncached: list[tuple[int, str]] = []
        uncached_idx: list[int] = []

        for i, t in enumerate(texts):
            key = hashlib.md5((t or "").encode()).hexdigest()
            with self._cache_lock:
                if key in self._cache:
                    results.append(self._cache[key])
                else:
                    uncached_idx.append(i)
                    uncached.append((i, t))
                    results.append(None)

        if uncached:
            raw = self._model.encode([t for _, t in uncached], normalize_embeddings=normalize)
            for (i, t), vec in zip(uncached, raw):
                key = hashlib.md5((t or "").encode()).hexdigest()
                with self._cache_lock:
                    self._cache[key] = vec.tolist()
                results[i] = vec.tolist()
        return results

    @staticmethod
    def cosine_sim(v1: list[float], v2: list[float]) -> float:
        """Compute the cosine similarity between two vectors."""
        dot = sum(a * b for a, b in zip(v1, v2))
        norm1 = math.sqrt(sum(a * a for a in v1)) or 1.0
        norm2 = math.sqrt(sum(b * b for b in v2)) or 1.0
        return dot / (norm1 * norm2)


def compute_entity_similarity(n1: dict, n2: dict) -> float:
    """Compute the vector-semantic similarity between two nodes (entity_text = type + name + description)."""
    et1 = f"{n1.get('node_type', '')} {n1.get('node_original_name', '')} {n1.get('node_description', '')}"
    et2 = f"{n2.get('node_type', '')} {n2.get('node_original_name', '')} {n2.get('node_description', '')}"
    model = EmbeddingModel.get_instance()
    vecs = model.encode([et1, et2])
    return EmbeddingModel.cosine_sim(vecs[0], vecs[1])


# ============================================================================
# Part 3: LLM invocation and API key round-robin management (exponential backoff retries)
# ============================================================================

class AdaptiveKeyManager:
    """
    Thread-safe adaptive concurrency Key manager (with exponential-backoff retries).
    """
    DEFAULT_CONCURRENCY = 1
    FALLBACK_CONCURRENCY = 1

    def __init__(self, keys: list[str]):
        self._keys = keys
        self._lock = Lock()
        self._sems = [Semaphore(self.DEFAULT_CONCURRENCY) for _ in keys]
        self._idx = 0
        self._failed_keys: set[int] = set()

    def acquire(self) -> tuple[str, int]:
        key_idx = -1
        key = ""
        with self._lock:
            for _ in range(len(self._keys)):
                idx = self._idx % len(self._keys)
                self._idx += 1
                if self._sems[idx].acquire(blocking=False):
                    key_idx = idx
                    key = self._keys[idx]
                    return key, key_idx
        with self._lock:
            idx = (self._idx - 1) % len(self._keys)
            key = self._keys[idx]
            key_idx = idx
        self._sems[key_idx].acquire()
        return key, key_idx

    def release(self, key_idx: int):
        self._sems[key_idx].release()

    def on_network_error(self, key_idx: int) -> None:
        with self._lock:
            self._failed_keys.add(key_idx)
            self._sems = [Semaphore(self.FALLBACK_CONCURRENCY) for _ in self._keys]

    def reset_concurrency(self) -> None:
        with self._lock:
            self._sems = [Semaphore(self.DEFAULT_CONCURRENCY) for _ in self._keys]
            self._failed_keys.clear()

    @property
    def total_keys(self) -> int:
        return len(self._keys)


def _call_gemini(prompt: str, config: dict, api_key: str) -> dict:
    """Gemini API call."""
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
        config={"temperature": 0.1, "max_output_tokens": 30000},
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
        opener = content[0] if content else ""
        if opener in ("[", "{"):
            depth = 0
            end_pos = -1
            for i, ch in enumerate(content):
                if ch in ("{", "["):
                    depth += 1
                elif ch in ("}", "]"):
                    depth -= 1
                    if depth == 0:
                        end_pos = i
                        break
            if end_pos > 0:
                try:
                    return json.loads(content[:end_pos + 1])
                except (json.JSONDecodeError, TypeError):
                    pass
    try:
        return json.loads(text)
    except (json.JSONDecodeError, TypeError):
        first_bracket = min((text.find(c) for c in "[{" if text.find(c) >= 0), default=-1)
        if first_bracket >= 0:
            try:
                return json.loads(text[first_bracket:])
            except (json.JSONDecodeError, TypeError):
                pass
    return None


def call_llm_with_retry(
    prompt: str,
    config: dict,
    key_manager: AdaptiveKeyManager,
    max_retries: int = MAX_RETRIES,
    initial_backoff: float = INITIAL_BACKOFF,
    max_backoff: float = MAX_BACKOFF,
) -> dict:
    """LLM call with exponential-backoff retries."""
    attempt = 0
    backoff = initial_backoff
    while True:
        api_key, key_idx = key_manager.acquire()
        try:
            result = _call_gemini(prompt, config, api_key)
            if result.get("error") and "401" in str(result.get("error", "")):
                key_manager.on_network_error(key_idx)
                if attempt >= max_retries:
                    return result
                time.sleep(backoff)
                backoff = min(backoff * 2, max_backoff)
                attempt += 1
                continue
            return result
        except Exception as e:
            key_manager.on_network_error(key_idx)
            if attempt >= max_retries:
                return {"text": "", "error": str(e), "input_tokens": 0, "output_tokens": 0, "total_tokens": 0}
            time.sleep(backoff)
            backoff = min(backoff * 2, max_backoff)
            attempt += 1
        finally:
            key_manager.release(key_idx)


# ============================================================================
# Part 4: 19 node_type-specific configurations
# ============================================================================

NODE_TYPE_PROMPTS = {
    "01-Object Domain": {
        "type_key": "01-Object-Domain",
        "definition": "论文所属的研究领域或应用方向（如旋转机械、电力电子、航空航天、工业过程等）。每篇论文有且仅有一个该类节点。",
        "scope_note": "该 node_type 代表的是广义的研究领域，而非具体设备。例如：'rotating machinery' 是领域；'ball bearing' 不是领域，而是对象类型。",
        "merge_rules": [
            "MERGE: 同一领域的不同表达形式（如 'UAV' ↔ 'unmanned aerial vehicle'，'aerospace' ↔ 'aeronautical'）",
            "MERGE: 完全相同领域仅有微小格式差异",
            "DO NOT MERGE: 不同研究领域（如 'rotating machinery' vs 'power electronics'）",
            "DO NOT MERGE: 领域与其子领域（如 'electronics' vs 'analog circuits'）",
            "DO NOT MERGE: 多领域混合节点与单一领域节点",
        ],
        "desc_template": "一个简洁的英文句子（40-80词），描述该研究领域的范围和典型应用场景。",
    },
    "02-Object Type": {
        "type_key": "02-Object-Type",
        "definition": "论文所研究的具体物理设备、零部件或系统（如滚动轴承、涡扇发动机、PEMFC 堆等）。歧义来源：同一物理对象用不同名称或缩写指代。",
        "scope_note": "该 node_type 代表的是具体物理对象，而非广义领域。歧义来源于同一物理对象在不同语境下的不同命名或缩写形式。",
        "merge_rules": [
            "MERGE: 缩写 ↔ 全称（如 'SNN' ↔ 'Spiking Neural Network'）",
            "MERGE: 同一对象仅有微小名称差异（如 'three-tank system' ↔ 'Three-tank system'）",
            "MERGE: 指向同一物理对象的同义词（需结合 description 验证）",
            "DO NOT MERGE: 同一家族的不同对象（如 'ball bearing' vs 'roller bearing'）",
            "DO NOT MERGE: 对象与其子部件（如 'bearing' vs 'ball bearing'）",
            "DO NOT MERGE: 不同设备（如 'compressor' vs 'turbine'）",
        ],
        "desc_template": "一个简洁的英文句子（40-80词），描述该物理对象的类型、功能和典型应用上下文。",
    },
    "03-Operating Conditions": {
        "type_key": "03-Operating-Condition",
        "definition": "系统运行时的操作环境或工作条件（如恒定转速、变负载、电压波动等）。每篇论文有且仅有一个该类节点。",
        "scope_note": "歧义来源于同一运行条件以不同数值或参数组合描述。数值差异通常意味着不同的条件，不应合并。",
        "merge_rules": [
            "MERGE: 参数完全相同的条件描述",
            "MERGE: 同一条件的等价描述（如 'steady-state' ↔ 'constant condition'）",
            "DO NOT MERGE: 同类型但不同数值（如 '1000 rpm' vs '2000 rpm'）",
            "DO NOT MERGE: 笼统条件与具体条件（如 'operational conditions' vs '1000 rpm'）",
            "DO NOT MERGE: 不同条件类型（如 'varying load' vs 'varying speed'）",
            "DO NOT MERGE: 多条件混合节点与单条件节点",
        ],
        "desc_template": "一个简洁的英文句子（40-80词），描述运行条件特征，包括转速、负载、温度或其他相关操作参数。",
    },
    "04-Fault Location": {
        "type_key": "04-Fault-Location",
        "definition": "故障发生的具体物理位置或部件（如定子绕组、外圈、转子导条等）。歧义来源：同一位置但用不同术语描述。",
        "scope_note": "该 node_type 表示故障发生的位置。歧义来源于同义词的混用以及同一部件的解剖学子区域。",
        "merge_rules": [
            "MERGE: 同一位置的各种同义表达（如 'outer race' ↔ 'outer raceway' ↔ 'bearing outer raceway'）",
            "MERGE: 当指向相同故障部位时，部件与其子区域可合并（需结合 description 验证）",
            "MERGE: 同一解剖学术语的不同语言形式",
            "DO NOT MERGE: 不同物理位置（如 'stator' vs 'rotor' vs 'blade'）",
            "DO NOT MERGE: 如果 description 表明指向不同故障部位，则部件与其子区域不应合并",
            "DO NOT MERGE: 同一家族的不同类型部件（如 'ball bearing' vs 'roller bearing'）",
        ],
        "desc_template": "一个简洁的英文句子（40-80词），描述该物理位置、在设备中的位置以及在此处发生的典型故障类型。",
    },
    "05-Fault Mode": {
        "type_key": "05-Fault-Mode",
        "definition": "故障的类型或模式（如短路、断齿、点蚀、偏心等）。歧义来源：同一故障现象用不同描述术语或粒度级别描述。",
        "scope_note": "该 node_type 表示发生了何种故障。歧义来源于对同一故障的不同描述术语以及不同的严重程度级别。",
        "merge_rules": [
            "MERGE: 同一故障的同义词（如 'pitting' ↔ 'spalling' [均为表面磨损]，'broken tooth' ↔ 'missing tooth'）",
            "MERGE: 指向同一故障类型的不同粒度描述",
            "MERGE: 同一故障的单复数形式（需结合 description 验证）",
            "DO NOT MERGE: 不同故障类型（如 'short circuit' vs 'open circuit' vs 'broken tooth'）",
            "DO NOT MERGE: 静偏心与动偏心（不同的故障机理）",
            "DO NOT MERGE: 故障状态与正常/健康状态",
        ],
        "desc_template": "一个简洁的英文句子（40-80词），描述该故障模式的现象、物理机理和典型症状。",
    },
    "06-Fault Severity": {
        "type_key": "06-Fault-Severity",
        "definition": "故障的严重程度或规模，通常以具体数值（如 '7 mils diameter'）或参数变化形式表达。每篇论文有且仅有一个该类节点。",
        "scope_note": "歧义来源于等效数值在不同单位下的表达。不同的数值通常代表不同的严重程度，不应合并。",
        "merge_rules": [
            "MERGE: 相同单位的相同数值",
            "MERGE: 不同兼容单位间的等效值（如 '7 mils' ↔ '0.007 inch'）",
            "DO NOT MERGE: 即使单位相同但数值不同（如 '7 mils' vs '14 mils'）",
            "DO NOT MERGE: 不同的定性严重程度描述（如 'slight' vs 'severe'）",
            "DO NOT MERGE: 故障严重程度 vs 故障类型 vs 故障部位",
            "DO NOT MERGE: 剩余使用寿命（一种预测值）与故障严重程度",
        ],
        "desc_template": "一个简洁的英文句子（40-80词），描述该严重程度指标、具体数值或范围，以及其在退化级别中的含义。",
    },
    "07-Compound Fault": {
        "type_key": "07-Compound-Fault",
        "definition": "论文涉及的是单一故障还是多个并发/复合故障（如 'single fault cases'、'double faults'、'compound fault' 等）。每篇论文有且仅有一个该类节点。",
        "scope_note": "歧义来源于对同一故障组合模式的不同同义表达。不同的故障数量代表不同的模式，不应合并。",
        "merge_rules": [
            "MERGE: 同一故障组合模式的同义表达（如 'compound fault' ↔ 'composite failure mode' ↔ 'combined faults'）",
            "MERGE: 仅有微小差异的单一故障表达",
            "DO NOT MERGE: 单一故障 vs 复合/多故障",
            "DO NOT MERGE: 不同故障数量（如 'double faults' vs 'triple faults'）",
            "DO NOT MERGE: 不同的具体故障组合",
        ],
        "desc_template": "一个简洁的英文句子（40-80词），描述该复合故障模式、并发故障数量和故障交互特征。",
    },
    "08-PHM Task": {
        "type_key": "08-PHM-Task",
        "definition": "论文所解决的特定故障预测与健康管理（Prognostics and Health Management）任务（如故障诊断、RUL 预测、健康监测等）。每篇论文有且仅有一个该类节点。",
        "scope_note": "歧义来源于描述同一 PHM 任务的不同术语。任务按其本质区分：diagnosis ≠ prognosis ≠ monitoring。",
        "merge_rules": [
            "MERGE: 同义的任务描述（如 'health monitoring' ↔ 'condition monitoring'）",
            "MERGE: RUL 相关表达（如 'remaining useful life prediction' ↔ 'RUL estimation' ↔ 'RUL prognostics'）",
            "DO NOT MERGE: 不同任务类型（如 'fault diagnosis' vs 'remaining useful life prediction'）",
            "DO NOT MERGE: 故障检测 vs 故障诊断（若 description 相似可合并）",
            "DO NOT MERGE: 监测任务 vs 预测任务",
        ],
        "desc_template": "一个简洁的英文句子（40-80词），描述该 PHM 任务的目标、方法和预期结果。",
    },
    "09-Problem Scenario": {
        "type_key": "09-Problem-Scenario",
        "definition": "论文所关注的具体挑战或问题设定（如小样本、类别不平衡、域迁移等）。每篇论文有且仅有一个该类节点。",
        "scope_note": "歧义来源于描述同一研究挑战的不同术语。即使同时出现，不同挑战类型也不应合并。",
        "merge_rules": [
            "MERGE: 同义的挑战描述（如 'small sample problem' ↔ 'limited labeled data'）",
            "MERGE: 不平衡相关表达（如 'class imbalance' ↔ 'imbalanced data' ↔ 'data imbalance'）",
            "MERGE: 噪声挑战相关表达（如 'noisy environment' ↔ 'noise interference'）",
            "DO NOT MERGE: 不同挑战类型（如 'small sample' vs 'class imbalance'）",
            "DO NOT MERGE: 域适应 vs 迁移学习场景",
            "DO NOT MERGE: 变工况 vs 噪声（不同挑战）",
        ],
        "desc_template": "一个简洁的英文句子（40-80词），描述该具体研究挑战、其对模型性能的影响以及提出该方法的动机。",
    },
    "10-Dataset": {
        "type_key": "10-Dataset",
        "definition": "实验所用的具体数据集（公开基准数据集或自采数据集）。歧义来源：同一数据集使用不同的命名约定。",
        "scope_note": "歧义来源于同一公开数据集的不同命名约定。不同数据集绝不应合并。",
        "merge_rules": [
            "MERGE: 同一数据集的不同名称（如 'CWRU' ↔ 'Case Western Reserve University Dataset'，'C-MAPSS' ↔ 'Commercial Modular Aero-Propulsion System Simulation'）",
            "MERGE: 数据集缩写 ↔ 全称",
            "MERGE: 同一数据集名称的微小格式差异",
            "DO NOT MERGE: 不同数据集（如 'CWRU' vs 'MFPT' vs 'PHM08'）",
            "DO NOT MERGE: 同一数据集在不同运行条件下",
            "DO NOT MERGE: 内容相似的公开数据集与私有数据集",
        ],
        "desc_template": "格式为：'Public Dataset, [数据集名称及简要描述]' 或 'Private Dataset (Self-collected): [采集方法]' 或 'Private Dataset (Simulation): [仿真工具和条件]'。",
    },
    "11-Sensor Information": {
        "type_key": "11-Sensor",
        "definition": "用于数据采集的传感器类型（如振动传感器、加速度计、电流传感器等）。歧义来源：同一传感器但使用不同术语。",
        "scope_note": "歧义来源于同一传感器类型的同义词和缩写。测量不同物理量的不同传感器类型不应合并。",
        "merge_rules": [
            "MERGE: 传感器同义词（如 'vibration sensor' ↔ 'accelerometer'，'AE sensor' ↔ 'Acoustic Emission sensor'）",
            "MERGE: 传感器缩写 ↔ 全称",
            "DO NOT MERGE: 不同传感器类型（如 'vibration sensor' vs 'current sensor' vs 'temperature sensor'）",
            "DO NOT MERGE: 测量不同现象的有源 vs 无源传感器",
            "DO NOT MERGE: 传感器类型 vs 传感器位置",
        ],
        "desc_template": "一个简洁的英文句子（40-80词），描述传感器类型、测量原理、安装位置和被测物理量。",
    },
    "12-Training Data Availability": {
        "type_key": "12-Training-Data-Size",
        "definition": "可用训练数据的数量，以样本数量、数据量或定性描述形式表达。每篇论文有且仅有一个该类节点。",
        "scope_note": "歧义来源于等效的数值表达。不同的数值代表不同的数据规模，不应合并。",
        "merge_rules": [
            "MERGE: 相同的样本数量或数据量",
            "MERGE: 等效表达（如 '50k samples' ↔ '50000 samples'）",
            "DO NOT MERGE: 不同的数值（如 10k vs 20k 样本）",
            "DO NOT MERGE: 'Limited data' vs 'abundant data'（含义相反）",
            "DO NOT MERGE: 不同的定性量表（除非 description 明确表明等效）",
        ],
        "desc_template": "一个简洁的英文句子（40-80词），描述数据集规模、样本数量和数据特征。",
    },
    "13-Noise Level": {
        "type_key": "13-Noise-Level",
        "definition": "采集数据的噪声特征，包括噪声类型、信噪比和强度描述。每篇论文有且仅有一个该类节点。",
        "scope_note": "歧义来源于描述同一噪声类型的不同术语。不同的噪声类型和 SNR 值不应合并。",
        "merge_rules": [
            "MERGE: 同一噪声类型的不同表达（如 'Gaussian noise' ↔ 'WGN' ↔ 'white Gaussian noise'）",
            "MERGE: 相同的 SNR 描述",
            "DO NOT MERGE: 不同噪声类型（如 'Gaussian' vs 'impulse' vs '1/f noise'）",
            "DO NOT MERGE: 不同 SNR 值",
            "DO NOT MERGE: 'Noisy signals' vs 具体噪声类型描述",
            "DO NOT MERGE: 'Heavy noise' vs 'light noise'（不同强度）",
        ],
        "desc_template": "一个简洁的英文句子（40-80词），描述噪声类型、信号噪声比水平及其对信号质量的影响。",
    },
    "14-Computational Resource": {
        "type_key": "14-Computational-Resource",
        "definition": "计算平台、硬件配置和所提方法的效率特征。每篇论文有且仅有一个该类节点。",
        "scope_note": "歧义来源于对同一硬件或效率特征的不同表达。不同硬件平台不应合并。",
        "merge_rules": [
            "MERGE: 同一硬件的不同描述（如 'i7-6700' ↔ 'Intel Core i7-6700'）",
            "MERGE: 相似的效率表达（如 'online' ↔ 'real-time' ↔ 'online implementation'）",
            "MERGE: 复杂度描述符（如 'low complexity' ↔ 'lightweight'——需 description 一致）",
            "DO NOT MERGE: 不同硬件平台（如 'GPU' vs 'CPU' vs 'FPGA'）",
            "DO NOT MERGE: 'Online' vs 'offline' 实现",
            "DO NOT MERGE: 不同计算复杂度级别",
        ],
        "desc_template": "一个简洁的英文句子（40-80词），描述计算平台、硬件规格和效率特征。",
    },
    "15-Data Preprocessing Algorithm": {
        "type_key": "15-Preprocessing-Algorithm",
        "definition": "在特征提取前用于预处理原始传感器数据的算法（如滤波、去噪、归一化、信号分解等）。",
        "scope_note": "歧义来源于同一预处理方法的缩写、全称和变体。不同的预处理算法绝不应合并。",
        "merge_rules": [
            "MERGE: 同一算法的缩写 ↔ 全称（如 'EMD' ↔ 'Empirical Mode Decomposition'，'DFT' ↔ 'Discrete Fourier Transform'）",
            "MERGE: 仅有微小格式差异的同一算法",
            "MERGE: description 确认的同一算法的不同名称",
            "DO NOT MERGE: 不同预处理算法（如 'EMD' vs 'Wavelet Transform' vs 'Fourier Transform'）",
            "DO NOT MERGE: 不同滤波类型（如 'low-pass filter' vs 'band-pass filter'）",
            "DO NOT MERGE: 不同公式的归一化方法",
            "DO NOT MERGE: 不同原理的分解方法",
            "CORE PRINCIPLE: 仅合并同一算法的真正别名。不同算法 ≠ 合并。",
        ],
        "desc_template": "一个简洁的英文句子（40-80词），描述该算法的输入、输出、数学原理及其在预处理流程中的作用。",
    },
    "16-Feature Extraction Algorithm": {
        "type_key": "16-Feature-Extraction-Algorithm",
        "definition": "从预处理后的数据中提取判别性特征的算法（如深度神经网络、统计特征、流形学习等）。",
        "scope_note": "歧义来源于缩写、全称和架构变体。不同的算法家族绝不应合并。",
        "merge_rules": [
            "MERGE: 同一算法的缩写 ↔ 全称（如 'LSTM' ↔ 'Long Short-Term Memory'，'CNN' ↔ 'Convolutional Neural Network'）",
            "MERGE: 双向扩展与基础算法（如 'LSTM' ↔ 'Bi-LSTM'）",
            "MERGE: 仅有微小名称差异的同一算法",
            "DO NOT MERGE: 不同算法家族（如 'CNN' vs 'LSTM' vs 'RNN' vs 'GRU'）",
            "DO NOT MERGE: 同一家族的不同深度变体（如 'ResNet-18' vs 'ResNet-101'）",
            "DO NOT MERGE: 特征提取 vs 分类（不同阶段）",
            "DO NOT MERGE: 传统特征 vs 深度学习特征",
            "CORE PRINCIPLE: 仅合并真正的别名。不同算法架构 ≠ 合并。",
        ],
        "desc_template": "一个简洁的英文句子（40-80词），描述该算法架构、输入数据类型和特征提取机制。",
    },
    "17-Core Classifier Algorithm": {
        "type_key": "17-Discriminator-Algorithm",
        "definition": "产生最终输出的核心分类或决策算法（如 SVM、随机森林、规则逻辑、混合分类器等）。",
        "scope_note": "歧义来源于缩写、全称和训练变体。不同的分类器家族绝不应合并。",
        "merge_rules": [
            "MERGE: 同一算法的缩写 ↔ 全称（如 'SVM' ↔ 'Support Vector Machine'，'TWSVM' ↔ 'Twin Support Vector Machine'）",
            "MERGE: WGAN 与 WGAN-GP → 合并（GP 是训练增强，核心算法相同）",
            "MERGE: 仅有微小名称差异的同一分类器",
            "DO NOT MERGE: 不同分类器家族（如 'SVM' vs 'Random Forest' vs 'Neural Network'）",
            "DO NOT MERGE: GAN 判别器组件 vs 完整 GAN 系统",
            "DO NOT MERGE: 混合方法 vs 其各组成部分",
            "DO NOT MERGE: 无监督聚类 vs 有监督分类",
            "CORE PRINCIPLE: 仅合并真正的别名。不同分类器范式 ≠ 合并。",
        ],
        "desc_template": "一个简洁的英文句子（40-80词），描述该分类器类型、决策机制及其在整体故障诊断框架中的作用。",
    },
    "18-Data Generation Algorithm": {
        "type_key": "18-Data-Generation-Algorithm",
        "definition": "用于增强或模拟真实测量数据的数据生成方法（如 GAN、SMOTE、FEM 仿真、Digital Twin、Monte Carlo 等）。",
        "scope_note": "歧义来源于同一生成方法的多种名称。不同的生成方法绝不应合并。",
        "merge_rules": [
            "MERGE: 同一算法的多种名称（如 'FEM' ↔ 'Finite Element Method' ↔ 'Finite Element Analysis' ↔ 'FEA'）",
            "MERGE: 'Bootstrap' ↔ 'Bootstrapping'",
            "MERGE: 'MATLAB/Simulink' ↔ 'Matlab/Simulink'（仅大小写差异）",
            "MERGE: description 确认的同一生成方法的不同名称",
            "DO NOT MERGE: GAN 变体（如 'DCGAN' vs 'WGAN' vs 'CGAN'），除非 description 确认同一架构",
            "DO NOT MERGE: 基于物理的仿真 vs 数据驱动的生成（不同范式）",
            "DO NOT MERGE: SMOTE vs GAN vs Bootstrap vs FEM（不同方法）",
            "DO NOT MERGE: Digital Twin vs 传统仿真",
            "CORE PRINCIPLE: 仅合并真正的别名。不同生成范式 ≠ 合并。",
        ],
        "desc_template": "一个简洁的英文句子（40-80词），描述该数据生成原理、输入需求和产生的合成数据类型。",
    },
    "19-Training Optimization Algorithm": {
        "type_key": "19-Training-Optimization-Algorithm",
        "definition": "用于优化模型训练的各种算法和技术，包括优化器、损失函数和训练策略（如 Adam、粒子群优化、对抗训练等）。",
        "scope_note": "歧义来源于缩写、全称和变体形式。不同的优化算法绝不应合并。",
        "merge_rules": [
            "MERGE: 同一优化器的缩写 ↔ 全称（如 'PSO' ↔ 'Particle Swarm Optimization'，'GWO' ↔ 'Grey Wolf Optimizer'）",
            "MERGE: Adam 及其变体（AdamW、AdaBound）——同一核心算法家族",
            "MERGE: 相同的损失函数表达",
            "DO NOT MERGE: 不同优化器家族（如 'Adam' vs 'SGD' vs 'PSO' vs 'GWO'）",
            "DO NOT MERGE: 不同损失函数（如 'Cross-Entropy' vs 'MSE' vs 'Focal Loss'）",
            "DO NOT MERGE: 不同训练策略（如 'adversarial training' vs 'transfer learning'）",
            "DO NOT MERGE: 优化算法 vs 评估指标",
            "CORE PRINCIPLE: 仅合并真正的别名。不同优化范式 ≠ 合并。",
        ],
        "desc_template": "一个简洁的英文句子（40-80词），描述该优化方法、更新规则及其对训练收敛和模型性能的影响。",
    },
}

ALGO_NODE_TYPE_SEQS = {15, 16, 17, 18, 19}
IMPORTANCE_PATTERNS = [
    (r'最高重要性', '最高重要性'),
    (r'一般重要性', '一般重要性'),
    (r'Not Mentioned', 'Not Mentioned'),
]


def _load_prompt_template(node_type: str) -> str:
    """Load the prompt template for a specific node_type from file."""
    # Infer from the file name, e.g. "01-Object Domain" -> "01-Object Domain_Prompt.md"
    fname = f"{node_type}_提示词.md"
    fpath = os.path.join(PROMPT_DIR, fname)
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            return f.read()
    return ""


def build_llm_prompt(node_type: str, nodes_to_disambiguate: list[dict]) -> str:
    """
    Build the LLM disambiguation prompt.
    Load the template from file and replace {node_id_N}, {node_original_name_N},
    {node_description_N} with actual data.
    """
    template = _load_prompt_template(node_type)
    if not template:
        return _build_inline_prompt(node_type, nodes_to_disambiguate)

    # Replace placeholders in the template
    nodes_sorted = sorted(nodes_to_disambiguate, key=lambda x: x["node_id"])
    lines = []
    for i, n in enumerate(nodes_sorted, 1):
        lines.append(f"**Node ID**: {n['node_id']}")
        lines.append(f"  - node_original_name: {n.get('node_original_name', '')}")
        lines.append(f"  - node_description: {n.get('node_description', '')}")
        lines.append("")

    nodes_block = "\n".join(lines)
    template = template.replace("{待处理节点列表}", nodes_block)
    return template


def _build_inline_prompt(node_type: str, nodes: list[dict]) -> str:
    """Build the prompt inline (when the template file does not exist)."""
    cfg = NODE_TYPE_PROMPTS.get(node_type, {})
    type_key = cfg.get("type_key", node_type)

    lines = []
    lines.append("# PHM 领域节点名称消歧任务")
    lines.append("")
    lines.append("## 【output格式 — 最高优先级 — 严格遵循】")
    lines.append("**输出必须仅包含一个完整的 JSON 对象，从字符 { 开始，到字符 } 结束。**")
    lines.append("**禁止包含任何解释、Markdown 代码块、推理过程文字或开场白。**")
    lines.append("")
    lines.append(f"## 【本次process的节点类型：{node_type}】")
    lines.append("")
    lines.append(f"### 类型定义\n{cfg.get('definition', '')}")
    lines.append(f"### 范围说明\n{cfg.get('scope_note', '')}")
    lines.append("")
    lines.append(f"### {node_type} 的消歧规则")
    for rule in cfg.get("merge_rules", []):
        lines.append(f"  - {rule}")
    lines.append("")

    if node_type.startswith(("15-", "16-", "17-", "18-", "19-")):
        lines.append("## 【算法类型专用规则】")
        lines.append("**核心原则：仅合并同一算法的真正别名。不同算法绝不应合并，即使属于同一算法家族。**")
        lines.append("  - 全称 ↔ 缩写：'LSTM' ↔ 'Long Short-Term Memory'")
        lines.append("  - 'AE' vs 'VAE'（不同架构）→ 不应合并")
        lines.append("  - 'CNN' vs 'LSTM' vs 'GRU'（不同家族）→ 不应合并")
        lines.append("  - 'Adam' vs 'SGD' vs 'PSO' vs 'GWO'（不同优化器）→ 不应合并")
        lines.append("  - 若不确定 → 宁可不合并（宁可分细，不要合并不同算法）")
        lines.append("")

    lines.append("## 【待process节点】")
    nodes_sorted = sorted(nodes, key=lambda x: x["node_id"])
    for n in nodes_sorted:
        lines.append(f"**Node ID**: {n['node_id']}")
        lines.append(f"  - node_original_name: {n.get('node_original_name', '')}")
        lines.append(f"  - node_description: {n.get('node_description', '')}")
        lines.append("")

    lines.append("## 【output格式说明】")
    lines.append(f"```json")
    lines.append(f'{{"{type_key}": {{"groups": [{{"node_ids": ["<node_id_1>", "<node_id_2>"], "node_name_common": "<消歧后英文名称>", "node_description_common": "<消歧后英文描述>"}}]}}}}')
    lines.append("```")
    lines.append("")
    lines.append("**字段说明：**")
    lines.append("  - `groups`：歧义组数组。若无歧义则为空数组 `[]`。")
    lines.append("  - `node_ids`：属于该组的所有 node_id，长度必须 >= 2。")
    lines.append("  - `node_name_common`：消歧后的英文名称。")
    lines.append("  - `node_description_common`：消歧后的英文描述，最大程度覆盖组内所有成员。")
    lines.append("  - 非歧义节点：不出现于输出任何位置。程序将直接把 node_original_name 复制为 node_name。")
    lines.append("")
    lines.append("## 【正确output示例】")
    lines.append(f'{{"{type_key}": {{"groups": []}}}}')
    lines.append("")
    lines.append("## 【output前必做check】")
    lines.append("  1. 每个 node_id 必须恰好出现在一个组的 node_ids 中，或不出现于任何位置。")
    lines.append("  2. 每个组的 node_ids 长度必须 >= 2。")
    lines.append("  3. node_name_common 不得为空或仅包含空白字符。")
    lines.append("  4. 输出必须是有效的 JSON。")
    lines.append("  5. 禁止 Markdown 代码块、禁止解释、禁止推理过程、禁止开场白。")
    lines.append("  6. 若此类型无歧义，输出：`{`" + type_key + f'`: {{"groups": []}}}}`')

    return "\n".join(lines)


# ============================================================================
# Part 5: disambiguation pipeline
# ============================================================================

def _compute_all_string_similarities(nodes: list[dict]) -> list[list[float]]:
    """Use numpy to batch-compute the pairwise string-similarity matrix among all nodes."""
    try:
        import numpy as np
    except ImportError:
        return None

    n = len(nodes)
    if n < 2:
        return [[1.0]]

    names = [normalize_text_for_comparison(n_.get("node_original_name", "")) for n_ in nodes]
    scores = np.zeros((n, n), dtype=np.float64)

    for i in range(n):
        scores[i, i] = 1.0
        for j in range(i + 1, n):
            s = name_similarity(names[i], names[j])
            scores[i, j] = s
            scores[j, i] = s

    return scores.tolist()


def step5_2_string_similarity_merge(
    nodes: list[dict],
    threshold: float = STRING_SIM_THRESHOLD,
) -> tuple[list[dict], list[dict], list[tuple[list[dict], str]]]:
    """
    Step 5-2: merge nodes whose string-normalization similarity is > threshold.
    Returns: (remaining_nodes, set_of_merged_node_ids, list_of_ambiguity_groups[(node_list, common_name)])
    """
    if len(nodes) < 2:
        return nodes, [], []

    # Try numpy acceleration
    sim_matrix = _compute_all_string_similarities(nodes)

    merged_ids: set[str] = set()
    groups: list[tuple[list[dict], str]] = []

    if sim_matrix is not None:
        # numpy path: read directly from the precomputed matrix
        n = len(nodes)
        for i in range(n):
            if nodes[i]["node_id"] in merged_ids:
                continue
            group = [nodes[i]]

            for j in range(i + 1, n):
                if nodes[j]["node_id"] in merged_ids:
                    continue
                if sim_matrix[i][j] > threshold:
                    group.append(nodes[j])
                    merged_ids.add(nodes[j]["node_id"])

            if len(group) >= 2:
                merged_ids.add(nodes[i]["node_id"])
                common_name = group[0].get("node_original_name", "")
                groups.append((group, common_name))
    else:
        # Pure-Python fallback
        n = len(nodes)
        for i in range(n):
            if nodes[i]["node_id"] in merged_ids:
                continue
            group = [nodes[i]]
            name_i = normalize_text_for_comparison(nodes[i].get("node_original_name", ""))

            for j in range(i + 1, n):
                if nodes[j]["node_id"] in merged_ids:
                    continue
                name_j = normalize_text_for_comparison(nodes[j].get("node_original_name", ""))
                sim = name_similarity(name_i, name_j)
                if sim > threshold:
                    group.append(nodes[j])
                    merged_ids.add(nodes[j]["node_id"])

            if len(group) >= 2:
                merged_ids.add(nodes[i]["node_id"])
                common_name = group[0].get("node_original_name", "")
                groups.append((group, common_name))

    remaining = [n_ for n_ in nodes if n_["node_id"] not in merged_ids]
    return remaining, list(merged_ids), groups


def step5_3_embedding_grouping(
    nodes: list[dict],
    sim_high: float = EMBED_SIM_HIGH,
    sim_low: float = EMBED_SIM_LOW,
) -> tuple[list[dict], list[dict], list[dict], list[tuple[list[dict], str]], list[tuple[list[dict], str]]]:
    """
    Step 5-3: vector-semantic embedding similarity grouping (numpy-accelerated).

    Returns:
      - group2_nodes: ambiguity-group nodes with similarity > sim_high
      - group3_nodes: unambiguous nodes with similarity < sim_low
      - remaining_nodes: nodes with similarity in [sim_low, sim_high], pending LLM
      - group2_detail: [(node_list, common_name)]
      - group3_detail: [(node_list, common_name)]
    """
    if len(nodes) < 2:
        return [], nodes, [], [], [(nodes, nodes[0].get("node_original_name", ""))] if nodes else []

    n = len(nodes)

    texts = [
        f"{nodes[i].get('node_type', '')} {nodes[i].get('node_original_name', '')} {nodes[i].get('node_description', '')}"
        for i in range(n)
    ]

    model = EmbeddingModel.get_instance()
    embeddings = model.encode(texts)

    # numpy batch-compute the cosine-similarity matrix
    try:
        import numpy as np
        emb_arr = np.array(embeddings, dtype=np.float64)
        norms = np.linalg.norm(emb_arr, axis=1, keepdims=True)
        norms = np.where(norms == 0, 1.0, norms)
        emb_normed = emb_arr / norms
        sim_matrix_np = emb_normed @ emb_normed.T
        sim_matrix = sim_matrix_np.tolist()
    except Exception:
        sim_matrix = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                sim_matrix[i][j] = EmbeddingModel.cosine_sim(embeddings[i], embeddings[j])

    visited: list[bool] = [False] * n
    high_groups: list[list[int]] = []

    for i in range(n):
        if visited[i]:
            continue
        group = [i]
        visited[i] = True

        for j in range(i + 1, n):
            if visited[j]:
                continue
            if sim_matrix[i][j] > sim_high:
                group.append(j)
                visited[j] = True

        if len(group) >= 2:
            high_groups.append(group)
        else:
            visited[i] = False

    visited2: list[bool] = [False] * n
    for g in high_groups:
        for idx in g:
            visited2[idx] = True

    low_groups: list[list[int]] = []
    for i in range(n):
        if visited2[i]:
            continue
        group = [i]
        visited2[i] = True

        for j in range(i + 1, n):
            if visited2[j]:
                continue
            if sim_matrix[i][j] < sim_low:
                group.append(j)
                visited2[j] = True

        if len(group) >= 2:
            low_groups.append(group)
        else:
            visited2[i] = False

    group2_detail: list[tuple[list[dict], str]] = []
    for g in high_groups:
        group_nodes = [nodes[idx] for idx in g]
        common_name = group_nodes[0].get("node_original_name", "")
        group2_detail.append((group_nodes, common_name))

    group3_detail: list[tuple[list[dict], str]] = []
    for g in low_groups:
        group_nodes = [nodes[idx] for idx in g]
        common_name = group_nodes[0].get("node_original_name", "")
        group3_detail.append((group_nodes, common_name))

    high_ids = {nodes[idx]["node_id"] for g in high_groups for idx in g}
    low_ids = {nodes[idx]["node_id"] for g in low_groups for idx in g}

    remaining = [n_ for n_ in nodes if n_["node_id"] not in high_ids and n_["node_id"] not in low_ids]

    group2_flat = [n_ for g in high_groups for idx in g for n_ in [nodes[idx]]]
    group3_flat = [n_ for g in low_groups for idx in g for n_ in [nodes[idx]]]

    return group2_flat, group3_flat, remaining, group2_detail, group3_detail


def step5_4_llm_disambiguation(
    node_type: str,
    nodes_to_llm: list[dict],
    key_manager: AdaptiveKeyManager,
) -> tuple[list[tuple[list[dict], str, str]], list[dict]]:
    """
    Step 5-4: call the LLM for ambiguity judgment.
    Returns: (list_of_ambiguity_groups[(node_list, node_name_common, node_description_common)], list_of_unambiguous_nodes)
    """
    if not nodes_to_llm:
        return [], []

    print(f"  [LLM] {node_type}: sending {len(nodes_to_llm)} node(s) for judgment...")

    prompt = build_llm_prompt(node_type, nodes_to_llm)
    result = call_llm_with_retry(prompt, LLM_CONFIG, key_manager)
    raw_text = result.get("text", "")

    if not raw_text:
        print(f"  [LLM] {node_type}: call failed; returning empty text")
        return [], nodes_to_llm

    parsed = _extract_json_from_response(raw_text)
    if parsed is None:
        print(f"  [LLM] {node_type}: JSON parsing failed (len={len(raw_text)}); skipping")
        return [], nodes_to_llm

    # Locate the result for the current node_type
    groups_data = None
    for key in [node_type, NODE_TYPE_PROMPTS.get(node_type, {}).get("type_key", "")]:
        if key in parsed:
            groups_data = parsed[key].get("groups", [])
            break

    if groups_data is None:
        for v in parsed.values():
            if isinstance(v, dict) and "groups" in v:
                groups_data = v["groups"]
                break

    if groups_data is None:
        groups_data = []

    ambiguous_groups: list[tuple[list[dict], str, str]] = []
    ambiguous_ids: set[str] = set()

    for grp in groups_data:
        nids = grp.get("node_ids", [])
        if len(nids) < 2:
            continue
        node_list = [n for n in nodes_to_llm if n["node_id"] in nids]
        if not node_list:
            continue
        common_name = grp.get("node_name_common", node_list[0].get("node_original_name", ""))
        common_desc = grp.get("node_description_common", "")
        ambiguous_groups.append((node_list, common_name, common_desc))
        ambiguous_ids.update(nids)

    unambiguous = [n for n in nodes_to_llm if n["node_id"] not in ambiguous_ids]
    return ambiguous_groups, unambiguous


def run_disambiguation_pipeline(
    nodes: list[dict],
    node_type: str,
    key_manager: AdaptiveKeyManager,
) -> dict:
    """
    Run the full disambiguation pipeline for the nodes of a given node_type.
    Returns disambiguation statistics.
    """
    stats = {
        "node_type": node_type,
        "total_need_disambiguate": len(nodes),
        "total_no_need_disambiguate": 0,
        "step5_2_string_groups": [],
        "step5_2_string_merged_count": 0,
        "step5_3_high_sim_groups": [],
        "step5_3_high_sim_count": 0,
        "step5_3_low_sim_groups": [],
        "step5_3_low_sim_count": 0,
        "step5_4_llm_sent_count": 0,
        "step5_4_llm_ambiguous_groups": [],
        "step5_4_llm_ambiguous_count": 0,
        "step5_4_llm_unambiguous_count": 0,
        "final_assigned_count": len(nodes),
    }

    # Step 5-2: string similarity > 0.9
    remaining, merged_ids, str_groups = step5_2_string_similarity_merge(nodes)
    stats["step5_2_string_merged_count"] = len(merged_ids)
    stats["step5_2_string_groups"] = [
        {
            "node_ids": [n["node_id"] for n in grp],
            "node_original_names": [n.get("node_original_name", "") for n in grp],
            "node_name_common": common_name,
        }
        for grp, common_name in str_groups
    ]

    # Step 5-3: vector-semantic embedding
    group2_flat, group3_flat, remaining2, emb_high_groups, emb_low_groups = step5_3_embedding_grouping(
        remaining, EMBED_SIM_HIGH, EMBED_SIM_LOW
    )
    stats["step5_3_high_sim_count"] = len(group2_flat)
    stats["step5_3_high_sim_groups"] = [
        {
            "node_ids": [n["node_id"] for n in grp],
            "node_original_names": [n.get("node_original_name", "") for n in grp],
            "node_name_common": common_name,
        }
        for grp, common_name in emb_high_groups
    ]
    stats["step5_3_low_sim_count"] = len(group3_flat)
    stats["step5_3_low_sim_groups"] = [
        {
            "node_ids": [n["node_id"] for n in grp],
            "node_original_names": [n.get("node_original_name", "") for n in grp],
            "node_name_common": common_name,
        }
        for grp, common_name in emb_low_groups
    ]

    # Step 5-4: LLM
    llm_ambiguous, llm_unambiguous = step5_4_llm_disambiguation(node_type, remaining2, key_manager)
    stats["step5_4_llm_sent_count"] = len(remaining2)
    stats["step5_4_llm_ambiguous_groups"] = [
        {
            "node_ids": [n["node_id"] for n in grp],
            "node_original_names": [n.get("node_original_name", "") for n in grp],
            "node_name_common": common_name,
            "node_description_common": common_desc,
        }
        for grp, common_name, common_desc in llm_ambiguous
    ]
    stats["step5_4_llm_ambiguous_count"] = sum(len(g[0]) for g in llm_ambiguous)
    stats["step5_4_llm_unambiguous_count"] = len(llm_unambiguous)

    return stats


def apply_disambiguation_results(
    nodes: list[dict],
    stats: dict,
) -> list[dict]:
    """
    Apply disambiguation statistics to the nodes; update node_name.
    Return the updated node list.
    """
    node_map: dict[str, dict] = {n["node_id"]: dict(n) for n in nodes}

    processed_ids: set[str] = set()

    # Step 5-2: string-similarity merge
    for grp_info in stats.get("step5_2_string_groups", []):
        nid_list = grp_info["node_ids"]
        common_name = grp_info["node_name_common"]
        for nid in nid_list:
            if nid in node_map:
                node_map[nid]["node_name"] = common_name
                processed_ids.add(nid)

    # Step 5-3 high: embedding high similarity
    for grp_info in stats.get("step5_3_high_sim_groups", []):
        nid_list = grp_info["node_ids"]
        common_name = grp_info["node_name_common"]
        for nid in nid_list:
            if nid in node_map:
                node_map[nid]["node_name"] = common_name
                processed_ids.add(nid)

    # Step 5-3 low: embedding low similarity (unambiguous; use node_original_name directly)
    for grp_info in stats.get("step5_3_low_sim_groups", []):
        nid_list = grp_info["node_ids"]
        for nid in nid_list:
            if nid in node_map:
                node_map[nid]["node_name"] = node_map[nid].get("node_original_name", "")
                processed_ids.add(nid)

    # Step 5-4: LLM ambiguous
    for grp_info in stats.get("step5_4_llm_ambiguous_groups", []):
        nid_list = grp_info["node_ids"]
        common_name = grp_info["node_name_common"]
        for nid in nid_list:
            if nid in node_map:
                node_map[nid]["node_name"] = common_name
                processed_ids.add(nid)

    # Step 5-4: LLM unambiguous -> keep node_name unchanged (Step 4 ensures node_name is None at this point)
    # Defensive check: if the original node_name is not None, this node should not have entered the pipeline; skip the overwrite
    for nid, node in node_map.items():
        if nid not in processed_ids:
            if node.get("node_name") is None:
                node["node_name"] = node.get("node_original_name", "")

    return list(node_map.values())


def _load_llm_assist_prompt_template(node_type: str) -> str:
    """Load the LLM-assisted secondary-disambiguation prompt template for a specific node_type from file."""
    fname = f"{node_type}_提示词.md"
    fpath = os.path.join(LLM_ASSIST_PROMPT_DIR, fname)
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            return f.read()
    return ""


def build_llm_assist_prompt(node_type: str, node_group_id_list: dict) -> str:
    """
    Build the LLM-assisted secondary-disambiguation prompt.
    Load from the template file and replace placeholders with actual ambiguity-group data.
    """
    template = _load_llm_assist_prompt_template(node_type)
    if not template:
        return ""

    input_json_str = json.dumps({node_type: node_group_id_list}, ensure_ascii=False, indent=2)
    template = template.replace("{待处理歧义组列表}", input_json_str)
    return template


def step6_llm_cross_group_disambiguation(
    stats_by_type: dict[str, dict],
    all_nodes: list[dict],
    key_manager: AdaptiveKeyManager,
) -> tuple[dict[str, dict], list[dict]]:
    """
    步骤 6：LLM 辅助的跨歧义组二次消歧判定。
    针对"字符串归一化相似度>0.9"和"向量语义 embedding 归一化相似度>0.85"的歧义组，
    判断这些歧义组之间是否仍存在歧义（即某些歧义组实际上应属于同一实体）。

    返回：(更新后的 stats_by_type, 更新后的节点列表)
    """
    print("\n[Step6] LLM 辅助跨歧义组二次消歧判定...")

    updated_stats = {nt: dict(s) for nt, s in stats_by_type.items()}
    node_map: dict[str, dict] = {n["node_id"]: dict(n) for n in all_nodes}

    total_llm_calls = 0
    total_cross_groups = 0
    total_cross_nodes = 0
    total_tokens = 0

    for node_type in sorted(updated_stats.keys()):
        s = updated_stats[node_type]

        str_groups = s.get("step5_2_string_groups", [])
        emb_high_groups = s.get("step5_3_high_sim_groups", [])

        all_groups = list(str_groups) + list(emb_high_groups)
        if len(all_groups) < 2:
            s["step6_llm_assist_groups"] = []
            s["step6_llm_assist_merged_count"] = 0
            continue

        node_group_id_list: dict[str, dict] = {}
        node_group_id_counter = 1

        for grp in all_groups:
            gid = f"node_group_id{node_group_id_counter}"
            node_group_id_counter += 1
            nid_list = grp.get("node_ids", [])
            common_name = grp.get("node_name_common", "")
            group_nodes = [n for n in node_map.values() if n.get("node_id") in nid_list]
            descriptions = [n.get("node_description", "") or "" for n in group_nodes]
            original_names = [n.get("node_original_name", "") or "" for n in group_nodes]
            desc_top10 = descriptions[:10]

            node_group_id_list[gid] = {
                "node_ids": nid_list,
                "node_name_common": common_name,
                "node_description_top10": desc_top10,
                "node_original_names": original_names,
            }

        node_group_id_list4LLM = {}
        for gid, grp_data in node_group_id_list.items():
            node_group_id_list4LLM[gid] = {
                "node_name_common": grp_data["node_name_common"],
                "node_description_top10": grp_data["node_description_top10"],
                "node_original_names": grp_data["node_original_names"],
            }

        prompt = build_llm_assist_prompt(node_type, node_group_id_list4LLM)
        if not prompt:
            print(f"  [Step6] {node_type}: 无法加载提示词模板，跳过")
            s["step6_llm_assist_groups"] = []
            s["step6_llm_assist_merged_count"] = 0
            continue

        DEBUG_DIR = os.path.join(OUTPUT_DIR, "Step6_debug")
        os.makedirs(DEBUG_DIR, exist_ok=True)
        debug_path = os.path.join(DEBUG_DIR, f"step6_{node_type}_debug.txt")

        print(f"  [Step6] {node_type}: 待判定歧义组 {len(node_group_id_list)} 个，调用 LLM...")
        t1 = time.time()
        result = call_llm_with_retry(prompt, LLM_CONFIG, key_manager)
        elapsed = time.time() - t1
        raw_text = result.get("text", "")
        tok = result.get("total_tokens", 0)
        total_tokens += tok

        # Debug: save原始 LLM response
        with open(debug_path, "w", encoding="utf-8") as f:
            f.write(f"=== Step6 {node_type} Debug ===\n\n")
            f.write(f"[PROMPT SENT TO LLM]\n{prompt}\n\n")
            f.write(f"[RAW LLM RESPONSE - len={len(raw_text)}]\n{raw_text}\n")

        parsed = _extract_json_from_response(raw_text)
        if parsed is None:
            print(f"  [Step6] {node_type}: JSON 解析失败（len={len(raw_text)}），跳过")
            s["step6_llm_assist_groups"] = []
            s["step6_llm_assist_merged_count"] = 0
            continue

        groups_data = None
        for key in [node_type, NODE_TYPE_PROMPTS.get(node_type, {}).get("type_key", "")]:
            if key in parsed:
                groups_data = parsed[key].get("groups", [])
                break

        if groups_data is None:
            for v in parsed.values():
                if isinstance(v, dict) and "groups" in v:
                    groups_data = v["groups"]
                    break

        if groups_data is None:
            groups_data = []

        # Debug: saveAll调试信息
        with open(debug_path, "a", encoding="utf-8") as f:
            f.write(f"\n[NODE_GROUP_ID_LIST_INPUT]\n{json.dumps(node_group_id_list, ensure_ascii=False, indent=2)}\n")
            f.write(f"\n[NODE_GROUP_ID_LIST_4LLM]\n{json.dumps(node_group_id_list4LLM, ensure_ascii=False, indent=2)}\n")
            f.write(f"\n[PARSED JSON]\n{json.dumps(parsed, ensure_ascii=False, indent=2)}\n\n")
            f.write(f"[EXTRACTED groups_data - len={len(groups_data)}]\n")
            f.write(f"{json.dumps(groups_data, ensure_ascii=False, indent=2)}\n")

        cross_groups = []
        cross_merged_node_count = 0

        for grp in groups_data:
            gids = grp.get("node_group_ids", [])
            if len(gids) < 2:
                continue

            all_nids = []
            for gid in gids:
                if gid in node_group_id_list:
                    all_nids.extend(node_group_id_list[gid]["node_ids"])

            if not all_nids:
                continue

            new_common_name = grp.get("node_name_common", "")
            new_common_desc = grp.get("node_description_common", "")

            for nid in all_nids:
                if nid in node_map:
                    node_map[nid]["node_name"] = new_common_name
                    if new_common_desc:
                        node_map[nid]["node_description"] = new_common_desc

            cross_merged_node_count += len(all_nids)
            cross_groups.append({
                "node_group_ids": gids,
                "node_ids": all_nids,
                "node_name_common": new_common_name,
                "node_description_common": new_common_desc,
            })

        total_llm_calls += 1
        total_cross_groups += len(cross_groups)
        total_cross_nodes += cross_merged_node_count

        s["step6_llm_assist_groups"] = cross_groups
        s["step6_llm_assist_merged_count"] = cross_merged_node_count
        print(f"  [Step6] {node_type}: LLM 调用完成，耗时 {elapsed:.1f}s，跨组合并 {len(cross_groups)} 组，影响 {cross_merged_node_count} 个节点，Token={tok}")

    print(f"\n  LLM 辅助二次判定汇总: 共调用 {total_llm_calls} 次，跨组合并 {total_cross_groups} 组，影响节点 {total_cross_nodes} 个，Token 总消耗 {total_tokens}")
    return updated_stats, list(node_map.values())


def apply_disambiguation_results_with_step6(
    nodes: list[dict],
    stats: dict,
) -> list[dict]:
    """
    将消歧统计结果（包含 step6）应用到节点，更新 node_name。
    返回更新后的节点列表。
    """
    node_map: dict[str, dict] = {n["node_id"]: dict(n) for n in nodes}

    processed_ids: set[str] = set()

    # Step 5-2: 字符串相似度merge
    for grp_info in stats.get("step5_2_string_groups", []):
        nid_list = grp_info["node_ids"]
        common_name = grp_info["node_name_common"]
        for nid in nid_list:
            if nid in node_map:
                node_map[nid]["node_name"] = common_name
                processed_ids.add(nid)

    # Step 5-3 high: embedding 高相似
    for grp_info in stats.get("step5_3_high_sim_groups", []):
        nid_list = grp_info["node_ids"]
        common_name = grp_info["node_name_common"]
        for nid in nid_list:
            if nid in node_map:
                node_map[nid]["node_name"] = common_name
                processed_ids.add(nid)

    # Step 5-3 low: embedding 低相似（none歧义，直接用 node_original_name）
    for grp_info in stats.get("step5_3_low_sim_groups", []):
        nid_list = grp_info["node_ids"]
        for nid in nid_list:
            if nid in node_map:
                node_map[nid]["node_name"] = node_map[nid].get("node_original_name", "")
                processed_ids.add(nid)

    # Step 5-4: LLM 歧义
    for grp_info in stats.get("step5_4_llm_ambiguous_groups", []):
        nid_list = grp_info["node_ids"]
        common_name = grp_info["node_name_common"]
        for nid in nid_list:
            if nid in node_map:
                node_map[nid]["node_name"] = common_name
                processed_ids.add(nid)

    # Step 6: LLM 辅助跨歧义组merge（覆盖前面AllStep的结果）
    for grp_info in stats.get("step6_llm_assist_groups", []):
        nid_list = grp_info.get("node_ids", [])
        new_common_name = grp_info.get("node_name_common", "")
        new_common_desc = grp_info.get("node_description_common", "")
        for nid in nid_list:
            if nid in node_map:
                node_map[nid]["node_name"] = new_common_name
                if new_common_desc:
                    node_map[nid]["node_description"] = new_common_desc
                processed_ids.add(nid)

    # 剩余节点：防御性check，若原始 node_name 非 None 则跳过覆盖
    for nid, node in node_map.items():
        if nid not in processed_ids:
            if node.get("node_name") is None:
                node["node_name"] = node.get("node_original_name", "")

    return list(node_map.values())


# ============================================================================
# 第6部分：消歧aggregate报告generate
# ============================================================================

def generate_stats_report(stats_by_type: dict[str, dict], output_dir: str):
    """按 node_type generate 19 个独立的消歧aggregate表。"""
    os.makedirs(output_dir, exist_ok=True)

    all_lines: list[str] = []
    all_lines.append("# 节点消歧结果aggregate总表\n")
    all_lines.append("| Node Type | 总节点 | 需消歧 | 无需消歧 | 字符串合并 | Embed高相似 | Embed低相似 | LLM歧义 | LLM非歧义 | LLM待判定 | LLM二次合并 |")
    all_lines.append("|-----------|--------|--------|----------|------------|-------------|-------------|---------|-----------|----------|------------|")

    for node_type in sorted(stats_by_type.keys()):
        s = stats_by_type[node_type]
        total = s.get("total_need_disambiguate", 0) + s.get("total_no_need_disambiguate", 0)
        str_merged = sum(len(g["node_ids"]) for g in s.get("step5_2_string_groups", []))
        emb_high = sum(len(g["node_ids"]) for g in s.get("step5_3_high_sim_groups", []))
        emb_low = sum(len(g["node_ids"]) for g in s.get("step5_3_low_sim_groups", []))
        llm_amb = s.get("step5_4_llm_ambiguous_count", 0)
        llm_unamb = s.get("step5_4_llm_unambiguous_count", 0)
        llm_sent = s.get("step5_4_llm_sent_count", 0)

        all_lines.append(
            f"| {node_type} | {total} | {s['total_need_disambiguate']} | "
            f"{s['total_no_need_disambiguate']} | {str_merged} | {emb_high} | {emb_low} | "
            f"{llm_amb} | {llm_unamb} | {llm_sent} | {s.get('step6_llm_assist_merged_count', 0)} |"
        )

    summary_path = os.path.join(output_dir, "消歧统计总表.md")
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("\n".join(all_lines))
    print(f"\n[保存] 消歧统计总表 -> {summary_path}")

    for node_type in sorted(stats_by_type.keys()):
        s = stats_by_type[node_type]
        lines = _build_type_stat_md(node_type, s)

        fname = f"{node_type}+消歧统计表.md"
        fpath = os.path.join(output_dir, fname)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"[保存] {node_type} 统计表 -> {fpath}")


def _build_type_stat_md(node_type: str, s: dict) -> list[str]:
    """构建单个 node_type 的消歧aggregate Markdown。"""
    lines: list[str] = []
    lines.append(f"# {node_type} 消歧aggregate表\n")

    total_need = s.get("total_need_disambiguate", 0)
    total_no_need = s.get("total_no_need_disambiguate", 0)
    total = total_need + total_no_need

    lines.append(f"## 基本信息\n")
    lines.append(f"- **1-1** 需要进行消歧判定的 node{{}}总数：{total_need} 个\n")
    lines.append(f"- **1-2** 不需要进行消歧判定的 node{{}}总数：{total_no_need} 个\n")
    lines.append(f"- **1-3** 当前 node_type 的 node{{}}总数：{total} 个\n")
    lines.append("")

    # 5-2 字符串归一化
    str_groups = s.get("step5_2_string_groups", [])
    str_total = sum(len(g["node_ids"]) for g in str_groups)
    lines.append(f"## Step 5-2：字符串归一化相似度 > {STRING_SIM_THRESHOLD}\n")
    lines.append(f"- **1-4** 经字符串归一化相似度 > {STRING_SIM_THRESHOLD} 的歧义 node{{}}总数：{str_total} 个\n")
    if str_groups:
        lines.append("\n消歧明细：\n")
        for idx, grp in enumerate(str_groups, 1):
            lines.append(f"{idx}）歧义组：")
            lines.append(f"   - node_ids: {', '.join(grp['node_ids'])}")
            names = [n if n else '' for n in grp.get('node_original_names', [])]
            lines.append(f"   - node_original_names: {', '.join(names)}")
            lines.append(f"   - 消歧名称 node_name_common: **{grp.get('node_name_common', '')}**")
            lines.append("")
    lines.append("")

    # 5-3 embedding
    emb_high_groups = s.get("step5_3_high_sim_groups", [])
    emb_low_groups = s.get("step5_3_low_sim_groups", [])
    emb_high_total = sum(len(g["node_ids"]) for g in emb_high_groups)
    emb_low_total = sum(len(g["node_ids"]) for g in emb_low_groups)
    llm_sent = s.get("step5_4_llm_sent_count", 0)

    lines.append(f"## Step 5-3：向量语义 embedding 相似度\n")
    lines.append(f"- **1-5** 经向量语义 embedding 归一化相似度 > {EMBED_SIM_HIGH} 的歧义 node{{}}总数：{emb_high_total} 个\n")
    lines.append(f"  - 向量语义 embedding 归一化相似度 < {EMBED_SIM_LOW} 的非歧义 node{{}}总数：{emb_low_total} 个\n")
    lines.append(f"  - 需要进一步通过 LLM 提示词判定的 node{{}}总数：{llm_sent} 个\n")

    if emb_high_groups:
        lines.append(f"\n高相似歧义组明细（> {EMBED_SIM_HIGH}）：\n")
        for idx, grp in enumerate(emb_high_groups, 1):
            lines.append(f"{idx}）歧义组：")
            lines.append(f"   - node_ids: {', '.join(grp['node_ids'])}")
            names = [n if n else '' for n in grp.get('node_original_names', [])]
            lines.append(f"   - node_original_names: {', '.join(names)}")
            lines.append(f"   - 消歧名称 node_name_common: **{grp.get('node_name_common', '')}**")
            lines.append("")
    lines.append("")

    # 5-4 LLM
    llm_amb_groups = s.get("step5_4_llm_ambiguous_groups", [])
    llm_unamb = s.get("step5_4_llm_unambiguous_count", 0)
    llm_amb_total = s.get("step5_4_llm_ambiguous_count", 0)
    llm_sent_total = s.get("step5_4_llm_sent_count", 0)

    lines.append(f"## Step 5-4：LLM Prompt判定\n")
    lines.append(f"- **1-6** 需要经 LLM 提示词判定的 node{{}}总数：{llm_sent_total} 个\n")
    lines.append(f"  - 经 LLM 提示词判定存在歧义的 node{{}}总数：{llm_amb_total} 个\n")
    lines.append(f"  - 经 LLM 提示词判定不存在歧义的 node{{}}总数：{llm_unamb} 个\n")

    if llm_amb_groups:
        lines.append("\nLLM 歧义组明细：\n")
        for idx, grp in enumerate(llm_amb_groups, 1):
            lines.append(f"{idx}）歧义组：")
            lines.append(f"   - node_ids: {', '.join(grp['node_ids'])}")
            names = [n if n else '' for n in grp.get('node_original_names', [])]
            lines.append(f"   - node_original_names: {', '.join(names)}")
            lines.append(f"   - 消歧名称 node_name_common: **{grp.get('node_name_common', '')}**")
            lines.append("")

    # Step 6 LLM 辅助跨歧义组
    step6_groups = s.get("step6_llm_assist_groups", [])
    step6_count = s.get("step6_llm_assist_merged_count", 0)
    lines.append(f"## Step 6：LLM 辅助跨歧义组二次消歧判定\n")
    lines.append(f"- **1-7** 经 LLM 辅助跨歧义组二次合并的 node{{}}总数：{step6_count} 个\n")

    if step6_groups:
        lines.append("\n跨歧义组合并明细：\n")
        for idx, grp in enumerate(step6_groups, 1):
            lines.append(f"{idx}）跨歧义组歧义组：")
            lines.append(f"   - 合并的 node_group_ids: {', '.join(grp.get('node_group_ids', []))}")
            lines.append(f"   - 合并的 node_ids: {', '.join(grp.get('node_ids', []))}")
            lines.append(f"   - 消歧名称 node_name_common: **{grp.get('node_name_common', '')}**")
            lines.append(f"   - 消歧描述 node_description_common: {grp.get('node_description_common', '')}")
            lines.append("")

    return lines


# ============================================================================
# 主程序
# ============================================================================

def main():
    t0 = time.time()

    print("=" * 70)
    print("节点名称消歧程序 V9（LLM 辅助跨歧义组二次消歧版）")
    print("=" * 70)

    # Step 1: readinput
    print(f"\n[Step1] 读取输入 JSON: {INPUT_JSON_PATH}")
    with open(INPUT_JSON_PATH, "r", encoding="utf-8") as f:
        all_papers = json.load(f)
    print(f"  -> 共 {len(all_papers)} 篇文献")

    # 展平All nodes（同时保留 paper 索引信息）
    all_nodes_v1: list[dict] = []
    paper_index_map: dict[str, int] = {}
    for pi, paper in enumerate(all_papers):
        for node in paper.get("nodes", []):
            all_nodes_v1.append(node)
            paper_index_map[node["node_id"]] = pi

    print(f"  -> 共 {len(all_nodes_v1)} 个节点")

    # Step 2: 字段adjust（v1 -> v2）
    print("\n[Step2] 执行字段调整（v1 -> v2）...")
    all_nodes_v2: list[dict] = []
    for node in all_nodes_v1:
        new_node = {
            "node_id": node.get("node_id"),
            "node_type": node.get("node_type"),
            "node_original_name": node.get("node_original_name"),
            "node_name": node.get("node_name"),
            "node_description": node.get("node_description"),
            "node_num": None,
            "node_cite_score": None,
            "node_cite_count": None,
            "node_weight": None,
            "node_algorithm_class": None,
            "node_id_list": node.get("node_case_id_list"),
        }
        all_nodes_v2.append(new_node)
    print(f"  -> v2 节点数: {len(all_nodes_v2)}")

    # Step 3: 算法类节点 importance 提取（v2 -> v3）
    print("\n[Step3] 提取算法类节点 importance 属性（15-19）...")
    all_nodes_v3: list[dict] = []
    importance_count = 0
    for node in all_nodes_v2:
        new_node = dict(node)
        t = node.get("node_type", "")
        m = re.match(r'^(\d+)-', t)
        if m and int(m.group(1)) in ALGO_NODE_TYPE_SEQS:
            new_node["node_importance"] = None
            desc = node.get("node_description") or ""
            for pattern, label in IMPORTANCE_PATTERNS:
                if re.search(pattern, desc):
                    new_node["node_importance"] = label
                    importance_count += 1
                    break
        all_nodes_v3.append(new_node)
    print(f"  -> 成功提取 {importance_count} 个节点的 importance 属性")

    # Step 4: 消歧资格判定
    print("\n[Step4] 消歧资格判定...")
    need_disambiguate: list[dict] = []
    no_need_disambiguate: list[dict] = []

    for node in all_nodes_v3:
        nn = node.get("node_name")
        non = node.get("node_original_name", "")
        # 仅当 node_name 为 None（未extract）时才需要消歧
        # "Not Mentioned" 是部分 node_type 合法的显式值（如 14-compute资源类），应直接保留
        if nn is None and non != "Not Mentioned":
            need_disambiguate.append(node)
        else:
            no_need_disambiguate.append(node)

    print(f"  -> 需要消歧的节点: {len(need_disambiguate)} 个")
    print(f"  -> 无需消歧的节点: {len(no_need_disambiguate)} 个")

    # 按 node_type 划分批次
    nodes_by_type: dict[str, list[dict]] = defaultdict(list)
    for node in need_disambiguate:
        nt = node.get("node_type", "unknown")
        nodes_by_type[nt].append(node)

    # 同时记录none需消歧的aggregate
    no_need_by_type: dict[str, int] = defaultdict(int)
    for node in no_need_disambiguate:
        nt = node.get("node_type", "unknown")
        no_need_by_type[nt] += 1

    print("\n  各类型待消歧节点分布：")
    for nt in sorted(nodes_by_type.keys()):
        print(f"    {nt}: {len(nodes_by_type[nt])} 个")

    # Step 5: 消歧流水线（字符串 + Embedding + LLM）
    print("\n[Step5] 开始消歧流水线...")

    key_manager = AdaptiveKeyManager(MULTI_API_KEYS)
    total_stats: dict[str, dict] = {}
    all_disambiguated: list[dict] = list(no_need_disambiguate)

    node_types_to_process = sorted(nodes_by_type.keys())
    llm_call_count = 0
    total_tokens = 0

    print(f"\n  {'类型':<30} {'节点':>6} {'字符串合并':>8} {'Embed合并':>8} {'Embed排除':>8} {'LLM判定':>8}")
    print(f"  {'-'*30} {'-'*6} {'-'*8} {'-'*8} {'-'*8} {'-'*8}")

    for nt in node_types_to_process:
        type_nodes = nodes_by_type[nt]

        t1 = time.time()
        stat = run_disambiguation_pipeline(type_nodes, nt, key_manager)
        stat["total_no_need_disambiguate"] = no_need_by_type.get(nt, 0)
        total_stats[nt] = stat

        updated = apply_disambiguation_results(type_nodes, stat)
        all_disambiguated.extend(updated)

        elapsed = time.time() - t1
        str_m = stat.get("step5_2_string_merged_count", 0)
        emb_h = stat.get("step5_3_high_sim_count", 0)
        emb_l = stat.get("step5_3_low_sim_count", 0)
        llm_c = stat.get("step5_4_llm_sent_count", 0)
        print(f"  {nt:<30} {len(type_nodes):>6} {str_m:>8} {emb_h:>8} {emb_l:>8} {llm_c:>8}  ({elapsed:.1f}s)")

        if stat["step5_4_llm_sent_count"] > 0:
            llm_call_count += 1

    # Step 6: LLM 辅助跨歧义组二次消歧判定
    print("\n[Step6] LLM 辅助跨歧义组二次消歧判定...")
    total_stats, all_disambiguated = step6_llm_cross_group_disambiguation(
        total_stats, all_disambiguated, key_manager
    )

    # Step 7: 回填 v3 -> v4（使用 step6 update后的结果）
    print("\n[Step7] 构建最终结果（v3 -> v4）...")

    # 重建 node_map 便于find
    final_node_map: dict[str, dict] = {n["node_id"]: n for n in all_disambiguated}

    # 将 v3 节点update（只update node_name，保留All v3 字段）
    all_nodes_v4: list[dict] = []
    for node in all_nodes_v3:
        nid = node["node_id"]
        if nid in final_node_map:
            new_node = dict(node)
            new_node["node_name"] = final_node_map[nid].get("node_name")
            all_nodes_v4.append(new_node)
        else:
            all_nodes_v4.append(dict(node))

    print(f"  -> v4 节点数: {len(all_nodes_v4)}")

    # Step 8: save JSON（保持原有嵌套结构）
    # 直接使用 all_nodes_v4（已包含 node_importance 等All v3 字段 + step6 update的 node_name）
    # all_nodes_v4 按 all_nodes_v3 的顺序排列，与原始 all_papers 的节点顺序一致
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 建立 node_id -> v4_node 的快速find
    v4_node_map: dict[str, dict] = {n["node_id"]: n for n in all_nodes_v4}

    for pi, paper in enumerate(all_papers):
        updated_nodes = []
        for node in paper.get("nodes", []):
            nid = node["node_id"]
            if nid in v4_node_map:
                # 使用 v4 节点（包含 v2/v3 新增字段 + step6 update的 node_name）
                updated_nodes.append(dict(v4_node_map[nid]))
            else:
                # 防御：理论上All nodes都应在 v4_node_map 中，此处兜底
                updated_nodes.append(node)
        all_papers[pi]["nodes"] = updated_nodes

    input_basename = os.path.basename(INPUT_JSON_PATH)
    output_json_name = input_basename.replace(".json", "_消歧.json")
    output_json_path = os.path.join(OUTPUT_DIR, output_json_name)

    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(all_papers, f, ensure_ascii=False, indent=2)
    print(f"  -> JSON 已保存: {output_json_path}")

    # Step 9: generate消歧aggregate报告
    print("\n[Step9] 生成消歧统计报告...")

    # 1) 消歧aggregate总表
    summary_lines: list[str] = []
    summary_lines.append("# 节点消歧结果aggregate总表\n")
    summary_lines.append("| Node Type | 总节点 | 需消歧 | 无需消歧 | 字符串合并 | Embed高相似 | Embed低相似 | LLM歧义 | LLM非歧义 | LLM待判定 |")
    summary_lines.append("|-----------|--------|--------|----------|------------|-------------|-------------|---------|-----------|----------|")

    for nt in sorted(total_stats.keys()):
        s = total_stats[nt]
        total = s["total_need_disambiguate"] + s["total_no_need_disambiguate"]
        str_merged = sum(len(g["node_ids"]) for g in s.get("step5_2_string_groups", []))
        emb_high = sum(len(g["node_ids"]) for g in s.get("step5_3_high_sim_groups", []))
        emb_low = sum(len(g["node_ids"]) for g in s.get("step5_3_low_sim_groups", []))
        llm_amb = s["step5_4_llm_ambiguous_count"]
        llm_unamb = s["step5_4_llm_unambiguous_count"]
        llm_sent = s["step5_4_llm_sent_count"]

        summary_lines.append(
            f"| {nt} | {total} | {s['total_need_disambiguate']} | "
            f"{s['total_no_need_disambiguate']} | {str_merged} | {emb_high} | {emb_low} | "
            f"{llm_amb} | {llm_unamb} | {llm_sent} |"
        )

    summary_path = os.path.join(OUTPUT_DIR, "消歧结果统计_md", "消歧统计总表.md")
    os.makedirs(os.path.dirname(summary_path), exist_ok=True)
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("\n".join(summary_lines))
    print(f"  -> [保存] 消歧统计总表 -> {summary_path}")

    # 2) 按类型generate 19 个独立aggregate表
    for nt in sorted(total_stats.keys()):
        lines = _build_type_stat_md(nt, total_stats[nt])
        fname = f"{nt}+消歧统计表.md"
        fpath = os.path.join(OUTPUT_DIR, "消歧结果统计_md", fname)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"  -> [保存] {nt} 统计表 -> {fpath}")

    # Total time
    elapsed = time.time() - t0

    # 汇总print
    total_cross_groups = sum(s.get("step6_llm_assist_merged_count", 0) for s in total_stats.values())

    print("\n" + "=" * 70)
    print("消歧汇总报告")
    print("=" * 70)
    print(f"  输入文件              : {input_basename}")
    print(f"  文献数量              : {len(all_papers)}")
    print(f"  节点总数              : {len(all_nodes_v3)}")
    print(f"  待消歧节点数          : {len(need_disambiguate)}")
    print(f"  无需消歧节点数        : {len(no_need_disambiguate)}")
    print(f"  LLM 调用类型数        : {llm_call_count}")
    print(f"  LLM 二次跨组合并节点数: {total_cross_groups}")
    print(f"  输出 JSON             : {output_json_name}")
    print(f"  输出统计目录          : {OUTPUT_DIR}\\消歧结果统计_md")
    print(f"  总耗时                : {elapsed:.1f} 秒")
    print("=" * 70)


if __name__ == "__main__":
    main()
