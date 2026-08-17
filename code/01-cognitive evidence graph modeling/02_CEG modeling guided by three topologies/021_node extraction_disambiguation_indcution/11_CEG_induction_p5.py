"""
zotero_knowledge_graph_extractor_hyperparam-assign_v8.py
===================================================
Augment each node in the disambiguation-induction-node JSON with the following properties:
  - node_cite_score : the case_id's corresponding journal 2yr_mean_citedness
  - node_cite_count : the case_id's corresponding paper cite_count
  - node_num        : always 1

Journal-impact-factor lookup priority (with caching):
  1. Locally maintained JOURNAL_IF_TABLE (exact / fuzzy match)
  2. OpenAlex API (search by journal name; retrieve 2yr_mean_citedness)
  3. LLM with web access (triggered when OpenAlex fails; generates initial values)
  4. All failed -> awaiting manual completion

LLM-generated-value highlighting:
  - Markdown report: marked with a 🔵 plus "【LLM-generated, awaiting manual confirmation】"
    annotation
  - HTML report: orange background + red border for prominent highlighting
  - HTML report mirrors the full Markdown content

Data-source notes:
  OpenAlex API returned journal-metric field meanings:
    - summary_stats.2yr_mean_citedness : 2-year mean citation count (closest concept to
      Clarivate JCR IF)
    - summary_stats.h_index            : h-index
    - cited_by_count                  : journal's lifetime citation count
  Note: OpenAlex data is sourced from Scopus, != Clarivate JCR Impact Factor.
        For JCR IF, visit https://jcr.clarivate.com or maintain a local JCR data table.

Output files (in the same directory as the input JSON, with dynamically derived names):
  1. {original filename}_hyperparam-assign.json  -- JSON array with properties filled in
                                                    (node_cite_score / node_cite_count / node_num)
  2. {original filename}_journal-IF-mapping-table.md -- publish_source -> 2yr_mean_citedness mapping result
  3. {original filename}_hyperparam-property-assign.md -- per-case_id property-assignment details
  4. {original filename}_hyperparam-assign-report.html -- HTML format (mirrors full Markdown,
                                                           includes LLM markers)
"""

import json
import os
import re
import time
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock, Semaphore
from typing import Optional

# ============================================================================
# LLM configuration (migrated from the induction-mapping-table script)
# ============================================================================
LLM_CONFIG = {
    "provider": "gemini",
    "model": "gemini-3.5-flash",
    "base_url": os.environ.get("BFGA_LLM_API_URL", "https://YOUR.LLM.ENDPOINT/"),
    "timeout": 300,
}

# IMPORTANT: Provide your own API keys before running. The list below should be filled with valid keys.
API_KEYS = []

# Maximum number of concurrency slots per API Key
# Total concurrency = num_api_keys * PER_KEY_CONCURRENCY
PER_KEY_CONCURRENCY = 2

LLM_TEMPERATURE = 0.0


# ============================================================================
# Path configuration
# ============================================================================
INPUT_JSON_PATH = r"./data/03_induction/[2277EAKD][ZZZRPFBV]合并节点_规范性审查_合并_规范性审查_消歧_规范性审查_归纳_规范性审查.json"

OUTPUT_BASE_DIR = (
    r"./data/03_induction"
    r"/A2-induction-output"
)

# OpenAlex API configuration
OPENALEX_BASE_URL = "https://api.openalex.org"
OPENALEX_REQUEST_TIMEOUT = 10
OPENALEX_RATE_LIMIT_DELAY = 0.2

# Fallback values: used when all strategies (local-exact / local-fuzzy / OpenAlex / LLM) fail
# Goal: avoid massive "manual completion needed" cases that break downstream normalization
DEFAULT_FALLBACK_CITE_SCORE = 1.0
DEFAULT_FALLBACK_SOURCE_LABEL = (
    f"default fallback={DEFAULT_FALLBACK_CITE_SCORE} "
    f" (local table + OpenAlex + LLM all failed to retrieve)"
)


# ============================================================================
# RoundRobinKeyManager: thread-safe API key round-robin manager
# ============================================================================

class RoundRobinKeyManager:
    """Thread-safe round-robin Key manager with per-Key rate limiting (max N concurrent requests per Key)."""

    def __init__(self, keys: list[str], per_key_limit: int = PER_KEY_CONCURRENCY):
        self._keys = keys
        self._lock = Lock()
        self._idx = 0
        self._usage: dict[str, int] = {}
        self._sems: list[Semaphore] = [Semaphore(per_key_limit) for _ in keys]
        self._per_key_limit = per_key_limit

    def get_key(self) -> str:
        with self._lock:
            key = self._keys[self._idx % len(self._keys)]
            self._idx += 1
            self._usage[key] = self._usage.get(key, 0) + 1
            return key

    def acquire(self, key: str) -> int:
        """Acquire one concurrency slot for the given Key; returns the Key index. Blocks until a slot is available."""
        key_idx = self._keys.index(key)
        self._sems[key_idx].acquire()
        return key_idx

    def release(self, key_idx: int):
        """Release one concurrency slot for the given Key index."""
        self._sems[key_idx].release()

    @property
    def total_keys(self) -> int:
        return len(self._keys)

    @property
    def per_key_limit(self) -> int:
        return self._per_key_limit

    @property
    def max_concurrent(self) -> int:
        return len(self._keys) * self._per_key_limit

    def usage_report(self) -> dict[str, int]:
        with self._lock:
            return dict(self._usage)


_key_manager: Optional[RoundRobinKeyManager] = None


def get_key_manager() -> RoundRobinKeyManager:
    global _key_manager
    if _key_manager is None:
        _key_manager = RoundRobinKeyManager(API_KEYS)
    return _key_manager


# ============================================================================
# LLM call (ported from the induction mapping script)
# ============================================================================

def _call_gemini_single_key(prompt: str, config: dict, api_key: str) -> dict:
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

    model_name = config.get("model", "gemini-3.5-flash")
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


def call_llm_single_try(prompt: str, config: dict, api_key: str) -> str:
    result = _call_gemini_single_key(prompt, config, api_key)
    return result["text"]


def call_llm_with_key_manager(prompt: str, config: dict, key_manager: RoundRobinKeyManager) -> str:
    """
    Acquire a key slot -> call LLM -> release slot.
    Automatically acquires/releases per-key concurrent slots; under multi-thread concurrency, each key is rate-limited independently.
    """
    key = key_manager.get_key()
    key_idx = key_manager.acquire(key)
    try:
        try:
            return call_llm_single_try(prompt, config, key)
        except Exception as e:
            err_msg = str(e).lower()
            if any(kw in err_msg for kw in [
                "quota", "rate", "limit", "429",
                "resource_exhausted", "internal error",
                "timeout", "connection",
            ]):
                print(f"      [Key {key_idx + 1}] LLM request failed ({type(e).__name__}): {e}")
                raise
            raise
    finally:
        key_manager.release(key_idx)


# ============================================================================
# Journal name normalization
# ============================================================================

def normalize_journal_name(name: str) -> str:
    if not name:
        return ""
    text = name.lower().strip()

    text = re.sub(r"\s*\([^)]*\)", "", text)
    text = re.sub(r"\b(19|20)\d{2}\b", "", text)
    text = re.sub(r"\bedition\b", "", text)

    stopwords = [
        "the", "of", "and", "in", "for", "on", "with",
        "a", "an", "to", "by", "from", "at",
        "journal", "journals",
    ]
    for w in stopwords:
        text = re.sub(r"\b" + w + r"\b", "", text)

    text = re.sub(r"[^a-z0-9]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


# ============================================================================
# Local journal impact-factor table
# ============================================================================

JOURNAL_IF_TABLE: list[dict] = [
    # Format: journal_name, normalized_name, issn, cite_score, year, source
    # Replace with real data; the source field records the data source (e.g. JCR / Scopus CiteScore / SJR).
    # Example:
    # {"journal_name": "IEEE Transactions on Industrial Electronics",
    #  "normalized_name": "ieeetransactionsonindustrialelectronics",
    #  "issn": "0278-0046", "cite_score": 12.5, "year": 2023,
    #  "source": "Clarivate JCR"},
]


# ============================================================================
# OpenAlex API lookup
# ============================================================================

def _normalize_for_openalex(name: str) -> str:
    text = name.strip()
    # Strip parenthesized notes: "Journal (some note)" -> "Journal"
    text = re.sub(r"\s*\([^)]*\)", "", text)
    # Normalize IEEE abbreviation: "IEEE Trans. on" -> "IEEE"
    text = re.sub(r"ieee\s*trans\.?\s*on?", "ieee", text, flags=re.IGNORECASE)
    text = re.sub(r"\btrans\.?\b", "", text, flags=re.IGNORECASE)
    # Strip conference-proceedings volume/part suffixes (the main cause of OpenAlex 400 Bad Request):
    #   ", PTS 1-3"  /  ", PTS 1 AND 2"  /  ", PT 1-4"  /  ", PART 1-3"  /  ", VOL 1"
    #   ", VOLS 1-3"  /  ", BOOK 1"  /  ", ED 1"
    text = re.sub(
        r",\s*(pts?|pt|parts?|vols?|vol|books?|ed|eds)\.?\s*\d+(\s*[-–]\s*\d+|\s+(and|to)\s+\d+)?\b",
        "",
        text,
        flags=re.IGNORECASE,
    )
    # Strip trailing Roman-numeral / numeric volume marks:
    #   "II" / "III" / "IV" / "2" / "2ND"
    #   "MECHATRONICS AND INTELLIGENT MATERIALS II, PTS 1-6" -> "MECHATRONICS AND INTELLIGENT MATERIALS"
    text = re.sub(
        r",?\s+\b(II|III|IV|VI|VII|VIII|IX|X|\d+(\.\d+)?(st|nd|rd|th)?)\b\s*$",
        "",
        text,
        flags=re.IGNORECASE,
    )
    # Strip pure-numeric tails: "RESEARCH ADVANCES 1.1" -> "RESEARCH ADVANCES"
    text = re.sub(r"\s+\d+(\.\d+)+\s*$", "", text)
    # Collapse extra whitespace
    text = re.sub(r"\s+", " ", text).strip()
    # Strip trailing residual commas
    text = text.rstrip(",").strip()
    return text


def _fuzzy_score(s1: str, s2: str) -> float:
    try:
        from rapidfuzz import fuzz
        return fuzz.ratio(s1, s2) / 100.0
    except ImportError:
        import difflib
        return difflib.SequenceMatcher(None, s1, s2).ratio()


def _fetch_from_openalex(publish_source: str) -> tuple[float | None, str]:
    if not publish_source:
        return None, ""

    search_name = _normalize_for_openalex(publish_source)
    if not search_name:
        return None, ""

    try:
        url = f"{OPENALEX_BASE_URL}/journals"
        params = {
            "filter": f"display_name.search:{search_name}",
            "per_page": 5,
            "mailto": "research@example.com",
        }
        resp = requests.get(url, params=params, timeout=OPENALEX_REQUEST_TIMEOUT)
        resp.raise_for_status()
        data = resp.json()
        results = data.get("results", [])
    except requests.exceptions.Timeout:
        print(f"    [OpenAlex] Timeout [{publish_source}]")
        return None, ""
    except requests.exceptions.ConnectionError:
        print(f"    [OpenAlex] Network connection failed [{publish_source}]")
        return None, ""
    except Exception as e:
        print(f"    [OpenAlex] Query exception [{publish_source}]: {e}")
        return None, ""

    if not results:
        print(f"    [OpenAlex] Journal not found [{publish_source}]")
        return None, ""

    best_sim = 0.0
    best_journal = None

    for j in results:
        oa_name = j.get("display_name", "") or ""
        sim = _fuzzy_score(
            normalize_journal_name(publish_source),
            normalize_journal_name(oa_name),
        )
        if sim > best_sim:
            best_sim = sim
            best_journal = j

    if best_sim >= 0.60 and best_journal is not None:
        summary = best_journal.get("summary_stats") or {}
        impact = summary.get("2yr_mean_citedness")
        h_index = summary.get("h_index")
        cited_by = best_journal.get("cited_by_count", 0)
        oa_name = best_journal.get("display_name", "")

        if impact is not None and impact > 0:
            src = (
                f"OpenAlex 2yr_mean_citedness={impact:.2f} "
                f"(h={h_index}, cited_by={cited_by}, similarity={best_sim:.0%})"
            )
            return float(impact), src

        if cited_by > 0:
            print(
                f"    [OpenAlex] Journal [{oa_name}] has no 2yr_mean_citedness, "
                f"cited_by={cited_by}, for reference only"
            )

    return None, ""


# ============================================================================
# LLM 联网query期刊影响因子
# ============================================================================

_LLM_GENERATED_CACHE: dict[str, tuple[float, str]] = {}


def _fetch_from_llm(publish_source: str) -> tuple[float | None, str]:
    """
    通过 LLM 联网查询期刊影响因子，返回 (impact_value, source)。
    LLM 查询仅作为 OpenAlex 失败后的 fallback，
    目的是为期刊提供一个初始影响因子值，避免后续映射报错。
    """
    if not publish_source:
        return None, ""

    if publish_source in _LLM_GENERATED_CACHE:
        return _LLM_GENERATED_CACHE[publish_source]

    prompt = (
        f"你是一个学术期刊信息查询助手。请联网查询以下期刊的最新影响因子或近似期刊指标。\n\n"
        f"期刊名称：{publish_source}\n\n"
        f"请返回以下格式的 JSON（只返回 JSON，不要有其他文字）：\n"
        f'{{"journal": "期刊全名", "impact_factor": 数值, "source": "数据来源（如 JCR 2023 / Scopus CiteScore 2023 等）", "year": 年份, "note": "备注说明"}}\n\n'
        f"要求：\n"
        f"1. impact_factor 必须是数值类型（JCR Impact Factor 或 Scopus CiteScore 均可，保留1位小数）\n"
        f"2. 如果无法查到确切数据，请基于期刊的学科领域和声誉给出一个合理估算值（并说明估算依据，保留2位小数）\n"
        f"3. 如果完全无法判断，请返回 null 而非杜撰数值\n"
        f"4. 只返回 JSON，不要有其他解释文字"
    )

    try:
        km = get_key_manager()
        raw_text = call_llm_with_key_manager(prompt, LLM_CONFIG, km)
    except Exception as e:
        print(f"    [LLM] lookup failed [{publish_source}]: {e}")
        _LLM_GENERATED_CACHE[publish_source] = (None, "")
        return None, ""

    # Parse JSON
    impact_value = None
    source_label = ""
    try:
        # Try to extract JSON from LLM response
        json_match = re.search(r"\{.*\}", raw_text, re.DOTALL)
        if json_match:
            data = json.loads(json_match.group())
            if data.get("impact_factor") is not None:
                impact_value = float(data["impact_factor"])
            source_label = data.get("source", "LLM-generated (unknown source)")
        else:
            # Try direct parsing
            data = json.loads(raw_text)
            if data.get("impact_factor") is not None:
                impact_value = float(data["impact_factor"])
            source_label = data.get("source", "LLM-generated (unknown source)")
    except Exception:
        # JSON parse failure; try extracting the value with regex
        num_match = re.search(r"impact_factor[\"']?:\s*(\d+\.?\d*)", raw_text, re.IGNORECASE)
        if num_match:
            impact_value = float(num_match.group(1))
            source_match = re.search(r"source[\"']?:[\s]*[\"']([^\"']+)[\"']", raw_text)
            source_label = source_match.group(1) if source_match else "LLM-generated"
        else:
            print(f"    [LLM] unable to parse response [{publish_source}]: {raw_text[:200]}")
            _LLM_GENERATED_CACHE[publish_source] = (None, "")
            return None, ""

    if impact_value is not None:
        src = f"LLM-generated ({source_label}) [WARNING: pending manual confirmation]"
        _LLM_GENERATED_CACHE[publish_source] = (impact_value, src)
        print(f"    [LLM] generated impact factor [{publish_source}]: {impact_value}")
    else:
        _LLM_GENERATED_CACHE[publish_source] = (None, "")
        print(f"    [LLM] unable to generate valid value [{publish_source}]")

    return _LLM_GENERATED_CACHE[publish_source]


# ============================================================================
# Journal impact-factor lookup entry (three-tier cache)
# ============================================================================

# Cache: publish_source -> (impact_value, source_label)
_OPENALEX_CACHE: dict[str, tuple[float | None, str]] = {}


def lookup_journal_cite_score(publish_source: str) -> tuple[float | None, str]:
    """
    Look up the journal impact factor for a publish_source; tries in order:
      1. Local table exact match
      2. Local table fuzzy match
      3. OpenAlex API lookup
      4. LLM online query (triggered when OpenAlex fails)
      5. All fail -> (DEFAULT_FALLBACK_CITE_SCORE, fallback marker)
        - Returns 1.0 to avoid breaking downstream normalization and explicitly labels "fallback" in source.
        - Callers can detect this by checking if source contains "default fallback value".
    """
    if not publish_source:
        return None, ""

    norm = normalize_journal_name(publish_source)

    # Strategy 1: local-table exact match
    if norm in _JOURNAL_EXACT_INDEX:
        entry = _JOURNAL_EXACT_INDEX[norm]
        return entry["cite_score"], f"{entry.get('source', 'unknown')} {entry.get('year', '')}"

    # Strategy 2: local-table fuzzy match
    if JOURNAL_IF_TABLE:
        best_sim_val = 0.0
        best_entry = None
        for entry in JOURNAL_IF_TABLE:
            entry_norm = entry.get("normalized_name", "")
            sim = _fuzzy_score(norm, entry_norm)
            if sim > best_sim_val:
                best_sim_val = sim
                best_entry = entry
        if best_sim_val >= 0.85 and best_entry is not None:
            return best_entry["cite_score"], (
                f"{best_entry.get('source', 'unknown')} {best_entry.get('year', '')} "
                f"[local fuzzy {best_sim_val:.0%}]"
            )

    # Strategy 3: OpenAlex API (with cache)
    if publish_source not in _OPENALEX_CACHE:
        time.sleep(OPENALEX_RATE_LIMIT_DELAY)
        _OPENALEX_CACHE[publish_source] = _fetch_from_openalex(publish_source)

    cached_val, cached_src = _OPENALEX_CACHE[publish_source]

    # Strategy 4: OpenAlex failed -> trigger LLM online query
    if cached_val is None:
        llm_val, llm_src = _fetch_from_llm(publish_source)
        if llm_val is not None:
            return llm_val, llm_src

    # Strategy 5: all fail -> default fallback value
    if cached_val is None:
        return DEFAULT_FALLBACK_CITE_SCORE, DEFAULT_FALLBACK_SOURCE_LABEL

    return cached_val, cached_src


# ============================================================================
# JSON I/O
# ============================================================================

def load_json(path: str) -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# ============================================================================
# Core processing
# ============================================================================

def process_hyperparameters(input_json_path: str) -> dict:
    papers = load_json(input_json_path)

    unique_sources: dict[str, dict] = {}
    journal_if_results: list[dict] = []
    stats = {
        "total_papers": len(papers),
        "total_nodes": 0,
        "journal_if_matched": 0,
        "journal_if_from_openalex": 0,
        "journal_if_from_local": 0,
        "journal_if_from_llm": 0,
        "journal_if_from_fallback": 0,
        "journal_if_pending": 0,
    }

    # Pre-compute each paper's metadata (no I/O or LLM calls involved)
    paper_metas: list[dict] = []
    for paper in papers:
        case_id = paper.get("case_id", "")
        publish_source = (paper.get("publish_source") or "").strip()
        cite_count = paper.get("cite_count")
        nodes: list[dict] = paper.get("nodes", [])

        stats["total_nodes"] += len(nodes)

        if publish_source:
            if publish_source not in unique_sources:
                unique_sources[publish_source] = {"case_ids": [], "cite_count": cite_count}
            if case_id not in unique_sources[publish_source]["case_ids"]:
                unique_sources[publish_source]["case_ids"].append(case_id)

        paper_metas.append({
            "paper": paper,
            "case_id": case_id,
            "publish_source": publish_source,
            "cite_count": cite_count,
            "nodes": nodes,
        })

    # === Key step: concurrent journal impact-factor lookup ===
    # Total concurrency = num_api_keys * PER_KEY_CONCURRENCY
    # Consistent with the per-key slot limiting inside RoundRobinKeyManager
    km = get_key_manager()
    max_workers = km.max_concurrent
    print(f"  [Concurrency config] API Keys={km.total_keys} x per-Key concurrency={km.per_key_limit} = "
          f"total concurrency={max_workers}")

    lookup_results: list[tuple[float | None, str] | None] = [None] * len(paper_metas)

    def _lookup_one(idx: int, meta: dict) -> None:
        try:
            lookup_results[idx] = lookup_journal_cite_score(meta["publish_source"])
        except Exception as e:
            print(f"  [Concurrency exception] case_id={meta['case_id']} "
                  f"publish_source='{meta['publish_source']}': {e}")
            lookup_results[idx] = (None, "")

    if max_workers <= 1 or len(paper_metas) <= 1:
        for i, meta in enumerate(paper_metas):
            _lookup_one(i, meta)
    else:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(_lookup_one, i, meta)
                       for i, meta in enumerate(paper_metas)]
            for fut in as_completed(futures):
                fut.result()

    # === Serial back-fill into papers / journal_if_results / stats (order matches input) ===
    for meta, result in zip(paper_metas, lookup_results):
        case_id = meta["case_id"]
        publish_source = meta["publish_source"]
        cite_count = meta["cite_count"]
        nodes = meta["nodes"]
        cite_score, source_label = result if result is not None else (None, "")

        is_fallback = bool(cite_score is not None and "default fallback value" in source_label)

        if cite_score is not None:
            stats["journal_if_matched"] += 1
            src_lower = source_label.lower()
            if is_fallback:
                stats["journal_if_from_fallback"] += 1
            elif "llm" in src_lower or "web generated" in src_lower:
                stats["journal_if_from_llm"] += 1
            elif "openalex" in src_lower:
                stats["journal_if_from_openalex"] += 1
            else:
                stats["journal_if_from_local"] += 1
        else:
            stats["journal_if_pending"] += 1

        # Round to 2 decimal places
        cite_score_rounded = round(cite_score, 2) if cite_score is not None else None

        case_ids_for_source = unique_sources.get(publish_source, {}).get("case_ids", [case_id])

        journal_if_results.append({
            "publish_source": publish_source,
            "cite_score": cite_score_rounded,
            "source": source_label if cite_score else "pending manual completion",
            "case_ids": case_ids_for_source,
        })

        # Assign values for each node
        for node in nodes:
            node["node_cite_score"] = cite_score_rounded
            node["node_cite_count"] = cite_count
            node["node_num"] = 1

    # Deduplicate
    seen = set()
    journal_if_dedup = []
    for r in journal_if_results:
        if r["publish_source"] not in seen:
            seen.add(r["publish_source"])
            journal_if_dedup.append(r)

    stats["unique_journals"] = len(seen)

    return {
        "papers": papers,
        "journal_if_results": journal_if_dedup,
        "stats": stats,
    }


# ============================================================================
# Markdown report generation
# ============================================================================

_PENDING_BLOCK = """
> ⚠️ **Important: the following journal impact factors were not auto-matched and need manual completion**
>
> Please look up the actual data in the following authoritative sources:
> - [Clarivate JCR](https://jcr.clarivate.com) (requires institutional subscription)
> - [Scopus CiteScore](https://www.scopus.com/sources)
> - [LetPub journal lookup](https://www.letpub.com.cn/index.php?page=journalapp)
> - [SJR - Scimago Journal Rank](https://www.scimagojr.com)
> - [OpenAlex](https://openalex.org)
>
> After completion please update the local `JOURNAL_IF_TABLE` or contact the maintainer.
"""

_LLM_WARNING_BLOCK = """
> 🔵 **LLM-generated data warning**
>
> The following journal impact factors were generated by the LLM via web search, **not from OpenAlex's official data**.
> The values are for reference only; **please always verify manually before use**, especially for formal academic contexts.
>
> Generation basis: the LLM searches the web for the journal's JCR Impact Factor or Scopus CiteScore,
> and combines journal reputation and subject area to give an estimated value.
"""

_FALLBACK_BLOCK = """
> ⚙️ **Default fallback value warning**
>
> For the following journals, **all** of the local table + OpenAlex + LLM web search failed to obtain a valid impact factor.
> The program has uniformly assigned the value **`DEFAULT_FALLBACK_CITE_SCORE = 1.0`** to ensure downstream normalization does not fail.
>
> These journals are most likely **conference proceedings** or non-mainstream journals,
> suggested in [DBLP](https://dblp.org), [Springer Link](https://link.springer.com),
> [IEEEXplore Proceedings](https://ieeexplore.ieee.org/browse/conferences/title/) 等
> 会议/丛书来源中查询其真实指标（如果有），再更新 `JOURNAL_IF_TABLE`。
> 如确为非正式会议论文集（无公认 IF），该 1.0 兜底值可视为有效占位。
"""


def generate_markdown_reports(result: dict, output_base_dir: str, base_name: str) -> tuple[str, str]:
    stats = result["stats"]
    journal_if_results = result["journal_if_results"]
    papers = result["papers"]

    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    # Group rows
    openalex_rows = [r for r in journal_if_results
                     if r["cite_score"] is not None
                     and "openalex" in r["source"].lower()]
    local_rows = [r for r in journal_if_results
                  if r["cite_score"] is not None
                  and ("llm" not in r["source"].lower()
                       and "联网生成" not in r["source"]
                       and "openalex" not in r["source"].lower()
                       and "默认兜底值" not in r["source"])]
    llm_rows = [r for r in journal_if_results
                if r["cite_score"] is not None
                and ("llm" in r["source"].lower() or "联网生成" in r["source"])]
    fallback_rows = [r for r in journal_if_results
                     if r["cite_score"] is not None
                     and "默认兜底值" in r["source"]]
    pending_rows = [r for r in journal_if_results if r["cite_score"] is None]

    openalex_rows.sort(key=lambda x: x["cite_score"] or 0, reverse=True)
    llm_rows.sort(key=lambda x: x["cite_score"] or 0, reverse=True)
    fallback_rows.sort(key=lambda x: x["publish_source"])
    pending_rows.sort(key=lambda x: x["publish_source"])

    # -------------------------------------------------------------------------
    # Report 1: journal impact-factor mapping table
    # -------------------------------------------------------------------------
    report1_lines: list[str] = []

    report1_lines.append("# Journal Impact-Factor Mapping Table\n")
    report1_lines.append(f"**Input file**: `{base_name}.json`\n")
    report1_lines.append(f"**Generated at**: {timestamp}\n\n")
    report1_lines.append(
        "**Data source**: OpenAlex API (Scopus `2yr_mean_citedness`) + LLM online query + default fallback\n\n"
    )
    report1_lines.append(
        "**Important note**: OpenAlex's `2yr_mean_citedness` comes from Scopus and is NOT equivalent to "
        "the Clarivate JCR Impact Factor. If JCR IF is required, please visit "
        "[JCR](https://jcr.clarivate.com) (institutional subscription) or "
        "[LetPub](https://www.letpub.com.cn/index.php?page=journalapp).\n\n"
    )

    # LLM warning
    if llm_rows:
        report1_lines.append(_LLM_WARNING_BLOCK)
        report1_lines.append("\n---\n\n")

    # Default fallback warning
    if fallback_rows:
        report1_lines.append(_FALLBACK_BLOCK)
        report1_lines.append("\n---\n\n")

    # Pending-match warning
    if pending_rows:
        report1_lines.append(_PENDING_BLOCK)
        report1_lines.append("\n---\n\n")

    # Statistics summary
    report1_lines.append("## Statistics Summary\n\n")
    report1_lines.append("| Metric | Value |\n|------|------|\n")
    report1_lines.append(f"| Distinct journals | {stats['unique_journals']} |\n")
    report1_lines.append(f"| Matched | {stats['journal_if_matched']} |\n")
    report1_lines.append(f"|   |-- OpenAlex success | {stats['journal_if_from_openalex']} |\n")
    report1_lines.append(f"|   |-- LLM-generated | {stats['journal_if_from_llm']} |\n")
    report1_lines.append(f"|   |-- Default fallback | {stats.get('journal_if_from_fallback', 0)} |\n")
    report1_lines.append(f"|   `-- Local table hit | {stats['journal_if_from_local']} |\n")
    report1_lines.append(f"| Pending manual completion | {stats['journal_if_pending']} |\n")
    report1_lines.append("\n---\n\n")

    # OpenAlex matched journals
    if openalex_rows:
        report1_lines.append("## OpenAlex Matched Journals (sorted by 2yr_mean_citedness, descending)\n\n")
        report1_lines.append(
            "| # | publish_source | 2yr_mean_citedness | source | source papers |\n"
        )
        report1_lines.append(
            "|---|----------------|--------------------|--------|----------|\n"
        )
        for i, r in enumerate(openalex_rows, 1):
            case_ids_str = ", ".join(r["case_ids"])
            report1_lines.append(
                f"| {i} | {r['publish_source']} | "
                f"**{r['cite_score']:.2f}** | {r['source']} | {case_ids_str} |\n"
            )
        report1_lines.append("\n---\n\n")

    # LLM-generated journals (highlighted)
    if llm_rows:
        report1_lines.append(
            "## LLM-Generated Journals (for reference only; pending manual confirmation)\n\n"
        )
        report1_lines.append(
            "| # | publish_source | impact factor | source | source papers |\n"
        )
        report1_lines.append(
            "|---|----------------|----------|--------|----------|\n"
        )
        for i, r in enumerate(llm_rows, 1):
            case_ids_str = ", ".join(r["case_ids"])
            report1_lines.append(
                f"| {i} | **[LLM] {r['publish_source']}** | "
                f"**{r['cite_score']:.2f}** | {r['source']} | {case_ids_str} |\n"
            )
        report1_lines.append("\n---\n\n")

    # Default fallback journals (highlighted)
    if fallback_rows:
        report1_lines.append(
            f"## Default Fallback Journals (uniformly assigned {DEFAULT_FALLBACK_CITE_SCORE})\n\n"
        )
        report1_lines.append(
            "| # | publish_source | impact factor | source | source papers |\n"
        )
        report1_lines.append(
            "|---|----------------|----------|--------|----------|\n"
        )
        for i, r in enumerate(fallback_rows, 1):
            case_ids_str = ", ".join(r["case_ids"])
            report1_lines.append(
                f"| {i} | **[FALLBACK] {r['publish_source']}** | "
                f"**{r['cite_score']:.2f}** | {r['source']} | {case_ids_str} |\n"
            )
        report1_lines.append("\n---\n\n")

    # Pending journals
    if pending_rows:
        report1_lines.append("## Pending Manual Completion\n\n")
        report1_lines.append(
            "| # | publish_source | 2yr_mean_citedness | source | source papers |\n"
        )
        report1_lines.append(
            "|---|----------------|--------------------|--------|----------|\n"
        )
        for i, r in enumerate(pending_rows, 1):
            case_ids_str = ", ".join(r["case_ids"])
            report1_lines.append(
                f"| {i} | **[PENDING] {r['publish_source']}** | "
                f"**pending** | - | {case_ids_str} |\n"
            )

    report1_path = os.path.join(output_base_dir, f"{base_name}_journal-IF-mapping-table.md")
    with open(report1_path, "w", encoding="utf-8") as f:
        f.writelines(report1_lines)
    print(f"  [Report 1] Journal impact-factor mapping table -> {report1_path}")

    # -------------------------------------------------------------------------
    # Report 2: hyperparameter property assignment report
    # -------------------------------------------------------------------------
    report2_lines: list[str] = []

    report2_lines.append("# Hyperparameter Property Assignment Report\n\n")
    report2_lines.append(f"**Input file**: `{base_name}.json`\n")
    report2_lines.append(f"**Generated at**: {timestamp}\n\n")

    report2_lines.append("## Assignment Notes\n\n")
    report2_lines.append("| Property | Source | Assignment rule |\n")
    report2_lines.append("|------|------|----------|\n")
    report2_lines.append(
        "| `node_cite_score` | publish_source -> OpenAlex 2yr_mean_citedness / LLM online | "
        "Shared across all nodes of the same paper |\n"
    )
    report2_lines.append(
        "| `node_cite_count` | Paper-level cite_count | Shared across all nodes of the same paper |\n"
    )
    report2_lines.append("| `node_num` | Constant | Uniformly set to 1 |\n\n")

    report2_lines.append("## Global Statistics\n\n")
    report2_lines.append(f"- Papers: {stats['total_papers']}\n")
    report2_lines.append(f"- Total nodes: {stats['total_nodes']}\n")
    report2_lines.append(f"- Distinct journals: {stats['unique_journals']}\n")
    report2_lines.append(
        f"- Matched journal impact factors: {stats['journal_if_matched']} "
        f"(OpenAlex {stats['journal_if_from_openalex']} + "
        f"LLM online {stats['journal_if_from_llm']} + "
        f"local table {stats['journal_if_from_local']} + "
        f"default fallback {stats.get('journal_if_from_fallback', 0)})\n"
    )
    report2_lines.append(
        f"- LLM-generated: {stats['journal_if_from_llm']} "
        f"(for reference only; pending manual confirmation)\n"
    )
    report2_lines.append(
        f"- Default fallback: {stats.get('journal_if_from_fallback', 0)} "
        f"(uniform {DEFAULT_FALLBACK_CITE_SCORE}; recommend manual verification)\n"
    )
    report2_lines.append(f"- Pending journal impact factors: {stats['journal_if_pending']}\n\n")
    report2_lines.append("---\n\n")

    report2_lines.append("## Per-Paper Assignment Details\n\n")

    for paper in papers:
        case_id = paper.get("case_id", "")
        paper_title = paper.get("paper_title", "(no title)")
        publish_source = paper.get("publish_source") or "(none)"
        cite_count = paper.get("cite_count", "(none)")
        cite_score = None
        cite_score_src = "(none)"

        for p in journal_if_results:
            if p["publish_source"] == publish_source:
                cite_score = p["cite_score"]
                cite_score_src = p["source"] if cite_score is not None else "pending manual completion"
                break

        nodes: list[dict] = paper.get("nodes", [])
        node_count = len(nodes)
        node_ids = [n.get("node_id", "") for n in nodes]

        is_llm = cite_score is not None and (
            "llm" in cite_score_src.lower() or "联网生成" in cite_score_src
        )
        is_fallback = cite_score is not None and "默认兜底值" in cite_score_src
        is_pending = cite_score is None

        if is_llm:
            report2_lines.append(f"### 🔵 [{case_id}] {paper_title} （LLM联网generate）\n\n")
        elif is_fallback:
            report2_lines.append(f"### ⚙️ [{case_id}] {paper_title} （default兜底）\n\n")
        elif is_pending:
            report2_lines.append(f"### 🔴 [{case_id}] {paper_title} （待人工补全）\n\n")
        else:
            report2_lines.append(f"### [{case_id}] {paper_title}\n\n")

        report2_lines.append(
            f"| 项目 | 值 |\n|------|---|\n"
            f"| case_id | {case_id} |\n"
            f"| publish_source | {publish_source} |\n"
        )

        if cite_score is None:
            report2_lines.append(f"| cite_score | ⚠️ **待人工补全** |\n")
        elif is_llm:
            report2_lines.append(
                f"| cite_score | 🔵 **{cite_score:.2f}** "
                f"({cite_score_src}) |\n"
            )
        elif is_fallback:
            report2_lines.append(
                f"| cite_score | ⚙️ **{cite_score:.2f}** "
                f"({cite_score_src}) |\n"
            )
        else:
            report2_lines.append(
                f"| cite_score | **{cite_score:.2f}** ({cite_score_src}) |\n"
            )

        report2_lines.append(
            f"| cite_count | {cite_count} |\n"
            f"| node_num | 1 |\n"
            f"| 节点数量 | {node_count} |\n"
            f"| 节点 ID 列表 | `{'`, `'.join(node_ids)}` |\n\n"
        )

        if is_llm:
            report2_lines.append(
                "> 🔵 **LLM 联网生成数据**，仅供参考，请参考上方「期刊影响因子对照表」中的 LLM 生成清单，"
                "务必人工核实后使用。\n\n"
            )
        elif is_fallback:
            report2_lines.append(
                f"> ⚙️ **默认兜底值**（{DEFAULT_FALLBACK_CITE_SCORE}），本地表 + OpenAlex + LLM 均未能获取该期刊的有效影响因子，"
                "该值仅为占位以保证下游归一化不报错，请参考上方「期刊影响因子对照表」中的兜底清单，"
                "必要时人工核实后更新 `JOURNAL_IF_TABLE`。\n\n"
            )
        elif is_pending:
            report2_lines.append(
                "> ⚠️ 该期刊影响因子未匹配，请参考上方「期刊影响因子对照表」中的待补全清单。\n\n"
            )

        report2_lines.append("---\n\n")

    report2_path = os.path.join(output_base_dir, f"{base_name}_超参数属性赋值.md")
    with open(report2_path, "w", encoding="utf-8") as f:
        f.writelines(report2_lines)
    print(f"  [报告2] 超参数属性赋值报告 → {report2_path}")

    return report1_path, report2_path


# ============================================================================
# HTML 报告generate（同步 Markdown 全部内容）
# ============================================================================

def generate_html_report(result: dict, output_base_dir: str, base_name: str) -> str:
    stats = result["stats"]
    journal_if_results = result["journal_if_results"]
    papers = result["papers"]
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    # Group rows
    openalex_rows = [r for r in journal_if_results
                     if r["cite_score"] is not None and "openalex" in r["source"].lower()]
    llm_rows = [r for r in journal_if_results
                if r["cite_score"] is not None
                and ("llm" in r["source"].lower() or "联网生成" in r["source"])]
    local_rows = [r for r in journal_if_results
                  if r["cite_score"] is not None
                  and "openalex" not in r["source"].lower()
                  and "llm" not in r["source"].lower()
                  and "联网生成" not in r["source"]
                  and "默认兜底值" not in r["source"]]
    fallback_rows = [r for r in journal_if_results
                     if r["cite_score"] is not None
                     and "默认兜底值" in r["source"]]
    pending_rows = [r for r in journal_if_results if r["cite_score"] is None]

    openalex_rows.sort(key=lambda x: x["cite_score"] or 0, reverse=True)
    llm_rows.sort(key=lambda x: x["cite_score"] or 0, reverse=True)
    fallback_rows.sort(key=lambda x: x["publish_source"])

    # ---- Journal mapping table HTML ----
    tbl1_body = ""

    if openalex_rows:
        tbl1_body += f'<h3>OpenAlex Matched Journals ({len(openalex_rows)})</h3>\n<table>\n<thead><tr>'
        for h in ["#", "publish_source", "2yr_mean_citedness", "source", "Source Papers"]:
            tbl1_body += f"<th>{h}</th>"
        tbl1_body += "</tr></thead><tbody>\n"
        for i, r in enumerate(openalex_rows, 1):
            case_ids_str = ", ".join(r["case_ids"])
            tbl1_body += (
                f"<tr><td>{i}</td><td>{r['publish_source']}</td>"
                f"<td><strong>{r['cite_score']:.2f}</strong></td>"
                f"<td>{r['source']}</td><td>{case_ids_str}</td></tr>\n"
            )
        tbl1_body += "</tbody></table>\n"

    if llm_rows:
        tbl1_body += (
            f'<h3 class="llm-section">[LLM] LLM-Generated Journals (for reference only; pending manual confirmation) ({len(llm_rows)})</h3>\n'
            '<div class="llm-warning">'
            "[LLM] <strong>[LLM-generated data warning]</strong> The following journal impact factors were generated "
            "automatically by an LLM via online lookup; the values are for reference only and "
            "<strong>must be manually verified before use</strong>."
            "</div>\n<table class='llm-table'>\n<thead><tr>"
        )
        for h in ["#", "publish_source", "影响因子", "source", "来源paper"]:
            tbl1_body += f"<th>{h}</th>"
        tbl1_body += "</tr></thead><tbody>\n"
        for i, r in enumerate(llm_rows, 1):
            case_ids_str = "、".join(r["case_ids"])
            tbl1_body += (
                f"<tr class='llm-row'><td>{i}</td>"
                f"<td><strong class='llm-journal'>{r['publish_source']}</strong></td>"
                f"<td><strong class='llm-value'>{r['cite_score']:.2f}</strong></td>"
                f"<td>{r['source']}</td><td>{case_ids_str}</td></tr>\n"
            )
        tbl1_body += "</tbody></table>\n"

    if fallback_rows:
        tbl1_body += (
            f'<h3 class="fallback-section">⚙️ 默认兜底期刊（统一 {DEFAULT_FALLBACK_CITE_SCORE}）（{len(fallback_rows)} 种）</h3>\n'
            '<div class="fallback-warning">'
            f"⚙️ <strong>【默认兜底值警告】</strong>以下期刊的本地表 + OpenAlex + LLM "
            f"<strong>均未能获取</strong>有效影响因子，程序已统一赋值为 "
            f"<strong>{DEFAULT_FALLBACK_CITE_SCORE}</strong> 以保证下游归一化不报错。"
            "该值仅为占位，建议人工核实后更新 <code>JOURNAL_IF_TABLE</code>。"
            "</div>\n<table class='fallback-table'>\n<thead><tr>"
        )
        for h in ["#", "publish_source", "影响因子", "source", "来源paper"]:
            tbl1_body += f"<th>{h}</th>"
        tbl1_body += "</tr></thead><tbody>\n"
        for i, r in enumerate(fallback_rows, 1):
            case_ids_str = "、".join(r["case_ids"])
            tbl1_body += (
                f"<tr class='fallback-row'><td>{i}</td>"
                f"<td><strong class='fallback-journal'>{r['publish_source']}</strong></td>"
                f"<td><strong class='fallback-value'>{r['cite_score']:.2f}</strong></td>"
                f"<td>{r['source']}</td><td>{case_ids_str}</td></tr>\n"
            )
        tbl1_body += "</tbody></table>\n"

    if pending_rows:
        pending_links = (
            '<a href="https://jcr.clarivate.com" target="_blank">Clarivate JCR</a>、'
            '<a href="https://www.letpub.com.cn/index.php?page=journalapp" target="_blank">LetPub</a>、'
            '<a href="https://www.scopus.com/sources" target="_blank">Scopus CiteScore</a>、'
            '<a href="https://www.scimagojr.com" target="_blank">SJR</a>'
        )
        pending_warning_text = "⚠️ 【待人工补全】请在 " + pending_links + " 等权威来源中查询真实数据。"
        tbl1_body += (
            '<h3 class="pending-section">⚠️ 待人工补全期刊（' + str(len(pending_rows)) + ' 种）</h3>\n'
            '<div class="pending-warning">'
            + pending_warning_text +
            '</div>\n<table class="pending-table">\n<thead><tr>'
        )
        for h in ["#", "publish_source", "2yr_mean_citedness", "source", "来源paper"]:
            tbl1_body += '<th>' + h + '</th>'
        tbl1_body += '</tr></thead><tbody>\n'
        for i, r in enumerate(pending_rows, 1):
            case_ids_str = "、".join(r["case_ids"])
            tbl1_body += (
                '<tr class="pending-row"><td>' + str(i) + '</td>'
                '<td><strong class="pending-journal">' + r["publish_source"] + '</strong></td>'
                '<td><strong>待补全</strong></td><td>—</td><td>' + case_ids_str + '</td></tr>\n'
            )
        tbl1_body += '</tbody></table>\n'

    # ---- paper属性明细 HTML ----
    papers_body = ""
    for paper in papers:
        case_id = paper.get("case_id", "")
        paper_title = paper.get("paper_title", "（无标题）")
        publish_source = paper.get("publish_source") or "（无）"
        cite_count = paper.get("cite_count", "（无）")
        cite_score = None
        cite_score_src = "（无）"
        for p in journal_if_results:
            if p["publish_source"] == publish_source:
                cite_score = p["cite_score"]
                cite_score_src = p["source"] if cite_score is not None else "⚠️ 待人工补全"
                break
        nodes: list[dict] = paper.get("nodes", [])
        node_count = len(nodes)
        node_ids = [n.get("node_id", "") for n in nodes]

        is_llm = cite_score is not None and (
            "llm" in cite_score_src.lower() or "联网生成" in cite_score_src
        )
        is_fallback = cite_score is not None and "默认兜底值" in cite_score_src
        is_pending = cite_score is None

        title_cls = "paper-title"
        if is_llm:
            title_cls = "paper-title llm-paper"
        elif is_fallback:
            title_cls = "paper-title fallback-paper"
        elif is_pending:
            title_cls = "paper-title pending-paper"

        prefix = ""
        if is_llm:
            prefix = "🔵 "
        elif is_fallback:
            prefix = "⚙️ "
        elif is_pending:
            prefix = "🔴 "

        cs_display = ""
        if cite_score is None:
            cs_display = "<td class='pending-val'>⚠️ 待人工补全</td>"
        elif is_llm:
            cs_display = (
                f"<td><strong class='llm-value'>{cite_score:.2f}</strong> "
                f"({cite_score_src})</td>"
            )
        elif is_fallback:
            cs_display = (
                f"<td><strong class='fallback-value'>{cite_score:.2f}</strong> "
                f"({cite_score_src})</td>"
            )
        else:
            cs_display = (
                f"<td><strong>{cite_score:.2f}</strong> ({cite_score_src})</td>"
            )

        warn_html = ""
        if is_llm:
            warn_html = (
                '<tr><td colspan="2" class="llm-cell">'
                "🔵 <strong>LLM 联网生成数据</strong>，仅供参考，务必人工核实后使用。"
                "</td></tr>"
            )
        elif is_fallback:
            warn_html = (
                f'<tr><td colspan="2" class="fallback-cell">'
                f"⚙️ <strong>默认兜底值（{DEFAULT_FALLBACK_CITE_SCORE}）</strong>，"
                "本地表 + OpenAlex + LLM 均未能获取该期刊的有效影响因子，"
                "该值仅为占位以保证下游归一化不报错。"
                "</td></tr>"
            )
        elif is_pending:
            warn_html = (
                '<tr><td colspan="2" class="pending-cell">'
                "⚠️ 该期刊影响因子未匹配，请参考上方「期刊影响因子对照表」中的待补全清单。"
                "</td></tr>"
            )

        papers_body += f"""
        <tr>
          <td class="{title_cls}">{prefix}[{case_id}] {paper_title}</td>
          <td>{publish_source}</td>
          {cs_display}
          <td>{cite_count}</td>
          <td>1</td>
          <td>{node_count}</td>
          <td class="node-ids">{"`, `".join(node_ids)}</td>
        </tr>
        {warn_html}
"""

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>超参数赋值报告</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: "Microsoft YaHei", "Segoe UI", Arial, sans-serif;
          font-size: 13px; background: #f0f2f5; color: #333; line-height: 1.6; }}
  .container {{ max-width: 1400px; margin: 0 auto; padding: 20px; }}
  h1 {{ text-align: center; color: #1a1a2e; margin-bottom: 6px; font-size: 22px; }}
  .subtitle {{ text-align: center; color: #888; font-size: 12px; margin-bottom: 28px; }}
  .summary-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
                   gap: 14px; margin-bottom: 28px; }}
  .stat-card {{ background: #fff; border-radius: 10px; padding: 16px 20px;
                box-shadow: 0 2px 8px rgba(0,0,0,.07); }}
  .stat-card .label {{ color: #888; font-size: 11px; text-transform: uppercase;
                        letter-spacing: .5px; margin-bottom: 4px; }}
  .stat-card .value {{ font-size: 26px; font-weight: 700; color: #2c3e50; }}
  .stat-card.highlight .value {{ color: #e67e22; }}
  .stat-card.llm .value {{ color: #d35400; }}
  .stat-card.fallback .value {{ color: #b7950b; }}

  .section {{ background: #fff; border-radius: 10px; padding: 20px 24px;
              margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,.07); }}
  h2 {{ color: #34495e; font-size: 15px; border-left: 4px solid #3498db;
        padding-left: 10px; margin: 0 0 14px; }}
  h3 {{ color: #34495e; font-size: 13px; margin: 16px 0 10px; }}
  h3.llm-section {{ color: #d35400; border-left: 4px solid #e67e22; padding-left: 10px; }}
  h3.fallback-section {{ color: #7d6608; border-left: 4px solid #b7950b; padding-left: 10px; }}
  h3.pending-section {{ color: #c0392b; border-left: 4px solid #e74c3c; padding-left: 10px; }}

  table {{ width: 100%; border-collapse: collapse; font-size: 12px;
           margin-bottom: 16px; table-layout: auto; }}
  thead th {{ background: #34495e; color: #fff; padding: 9px 8px;
              text-align: left; font-weight: 600; white-space: nowrap; }}
  tbody td {{ padding: 8px 8px; border-bottom: 1px solid #ecf0f3;
              vertical-align: top; word-break: break-all; }}
  tbody tr:last-child td {{ border-bottom: none; }}
  tbody tr:hover {{ background: #f8f9fb; }}

  /* LLM 标记样式 */
  .llm-warning {{ background: #fff3e0; border: 2px solid #e67e22; border-radius: 6px;
                  padding: 10px 14px; margin-bottom: 12px; color: #d35400;
                  font-size: 12px; line-height: 1.7; }}
  table.llm-table {{ border: 2px solid #e67e22; border-radius: 6px; overflow: hidden; }}
  table.llm-table thead th {{ background: #e67e22; }}
  .llm-row td {{ background: #fff8f0; }}
  .llm-journal {{ color: #d35400; }}
  .llm-value {{ color: #d35400; font-size: 14px; }}

  /* 默认兜底样式 */
  .fallback-warning {{ background: #fef9e7; border: 2px solid #b7950b; border-radius: 6px;
                       padding: 10px 14px; margin-bottom: 12px; color: #7d6608;
                       font-size: 12px; line-height: 1.7; }}
  .fallback-warning code {{ background: #fcf3cf; color: #6e2c00; padding: 1px 5px;
                            border-radius: 3px; font-family: Consolas, monospace; }}
  table.fallback-table {{ border: 2px solid #b7950b; border-radius: 6px; overflow: hidden; }}
  table.fallback-table thead th {{ background: #b7950b; }}
  .fallback-row td {{ background: #fef9e7; }}
  .fallback-journal {{ color: #6e2c00; }}
  .fallback-value {{ color: #7d6608; font-size: 14px; }}

  /* 待补全样式 */
  .pending-warning {{ background: #fdf2f2; border: 2px solid #e74c3c; border-radius: 6px;
                      padding: 10px 14px; margin-bottom: 12px; color: #c0392b;
                      font-size: 12px; line-height: 1.7; }}
  .pending-warning a {{ color: #c0392b; font-weight: 600; }}
  table.pending-table {{ border: 2px solid #e74c3c; border-radius: 6px; overflow: hidden; }}
  table.pending-table thead th {{ background: #e74c3c; }}
  .pending-row td {{ background: #fff8f8; }}
  .pending-journal {{ color: #c0392b; }}

  /* 文献明细样式 */
  .paper-title {{ font-weight: 600; }}
  .llm-paper {{ color: #d35400; }}
  .fallback-paper {{ color: #7d6608; }}
  .pending-paper {{ color: #c0392b; }}
  .node-ids {{ font-family: Consolas, monospace; font-size: 11px; color: #666;
               white-space: nowrap; max-width: 300px; overflow: hidden;
               text-overflow: ellipsis; }}
  .llm-cell {{ background: #fff8f0 !important; color: #d35400; font-size: 12px;
               padding: 8px 10px !important; }}
  .fallback-cell {{ background: #fef9e7 !important; color: #7d6608; font-size: 12px;
                    padding: 8px 10px !important; }}
  .pending-cell {{ background: #fff8f8 !important; color: #c0392b; font-size: 12px;
                   padding: 8px 10px !important; }}
  .pending-val {{ color: #c0392b; font-weight: 600; }}

  .footer {{ text-align: center; color: #aaa; font-size: 11px;
              margin-top: 24px; padding-top: 16px; border-top: 1px solid #e0e0e0; }}
</style>
</head>
<body>
<div class="container">
  <h1>📊 超参数赋值报告</h1>
  <p class="subtitle">
    输入: {base_name}.json | 生成时间: {timestamp}
  </p>

  <!-- 统计卡片 -->
  <div class="summary-grid">
    <div class="stat-card highlight">
      <div class="label">文献数量</div>
      <div class="value">{stats['total_papers']}</div>
    </div>
    <div class="stat-card">
      <div class="label">节点总数</div>
      <div class="value">{stats['total_nodes']}</div>
    </div>
    <div class="stat-card">
      <div class="label">期刊种类数</div>
      <div class="value">{stats['unique_journals']}</div>
    </div>
    <div class="stat-card">
      <div class="label">✅ 已匹配</div>
      <div class="value">{stats['journal_if_matched']}</div>
    </div>
    <div class="stat-card">
      <div class="label">　　├ OpenAlex</div>
      <div class="value">{stats['journal_if_from_openalex']}</div>
    </div>
    <div class="stat-card llm">
      <div class="label">　　├ 🔵 LLM联网</div>
      <div class="value">{stats['journal_if_from_llm']}</div>
    </div>
    <div class="stat-card fallback">
      <div class="label">　　├ ⚙️ 默认兜底</div>
      <div class="value">{stats.get('journal_if_from_fallback', 0)}</div>
    </div>
    <div class="stat-card">
      <div class="label">　　└ 本地表</div>
      <div class="value">{stats['journal_if_from_local']}</div>
    </div>
    <div class="stat-card">
      <div class="label">⚠️ 待补全</div>
      <div class="value">{stats['journal_if_pending']}</div>
    </div>
  </div>

  <!-- 期刊对照表 -->
  <div class="section">
    <h2>📋 期刊影响因子对照表</h2>
    {tbl1_body}
  </div>

  <!-- 文献属性明细 -->
  <div class="section">
    <h2>📄 各文献属性赋值明细</h2>
    <table>
      <thead>
        <tr>
          <th>文献标题</th>
          <th>publish_source</th>
          <th>cite_score</th>
          <th>cite_count</th>
          <th>node_num</th>
          <th>节点数量</th>
          <th>节点 ID 列表</th>
        </tr>
      </thead>
      <tbody>
        {papers_body}
      </tbody>
    </table>
  </div>

  <div class="footer">
    由 zotero_knowledge_graph_extractor_超参数赋值_v8.py 自动生成
  </div>
</div>
</body>
</html>"""

    html_path = os.path.join(output_base_dir, f"{base_name}_超参数赋值报告.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  [报告3] HTML报告 → {html_path}")
    return html_path


# ============================================================================
# Main flow
# ============================================================================

def main():
    print("=" * 70)
    print("Hyperparameter assignment script V8")
    print("=" * 70)

    print(f"\n[Step 1] Reading input JSON:\n  {INPUT_JSON_PATH}")
    if not os.path.exists(INPUT_JSON_PATH):
        raise FileNotFoundError(f"Input file does not exist: {INPUT_JSON_PATH}")

    print(f"\n[Step 2] Starting processing (OpenAlex + LLM queries)...")
    result = process_hyperparameters(INPUT_JSON_PATH)
    stats = result["stats"]

    print(f"\n  Papers:           {stats['total_papers']}")
    print(f"  Total nodes:      {stats['total_nodes']}")
    print(f"  Distinct journals: {stats['unique_journals']}")
    print(f"  Matched:          {stats['journal_if_matched']}")
    print(f"    `-- OpenAlex:   {stats['journal_if_from_openalex']}")
    print(f"    └ LLM联网:      {stats['journal_if_from_llm']} 种")
    print(f"    └ 本地表:       {stats['journal_if_from_local']} 种")
    print(f"  待人工补全:       {stats['journal_if_pending']} 种")

    print(f"\n[Step3] 保存超参数赋值后的 JSON...")
    base_name = os.path.splitext(os.path.basename(INPUT_JSON_PATH))[0]
    output_json_name = f"{base_name}_超参数赋值.json"
    output_json_path = os.path.join(OUTPUT_BASE_DIR, output_json_name)
    os.makedirs(OUTPUT_BASE_DIR, exist_ok=True)
    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(result["papers"], f, ensure_ascii=False, indent=2)
    print(f"  [JSON] 超参数赋值结果 → {output_json_path}")

    print(f"\n[Step4] 生成 Markdown 报告...")
    report1, report2 = generate_markdown_reports(result, OUTPUT_BASE_DIR, base_name)

    print(f"\n[Step5] 生成 HTML 报告...")
    html_path = generate_html_report(result, OUTPUT_BASE_DIR, base_name)

    print(f"\n{'=' * 70}")
    print("全部完成！")
    print(f"  JSON:    {output_json_path}")
    print(f"  报告1:   {report1}")
    print(f"  报告2:   {report2}")
    print(f"  报告3:   {html_path}")
    print("=" * 70)


if __name__ == "__main__":
    main()
