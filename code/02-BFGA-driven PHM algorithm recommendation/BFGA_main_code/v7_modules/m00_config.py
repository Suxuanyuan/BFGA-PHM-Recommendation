# -*- coding: utf-8 -*-
r"""
v7_modules/00_config.py
========================
v7 configuration objects and constant definitions.

Based on v6's m00_config.py, adds:
  - Fact sufficiency 19-point system parameters
  - Concurrent pruning-exploration-aggregation loop parameters
  - W-sum group combination upper limit
  - Feedback decision threshold

LLM credentials are NO LONGER hard-coded. They are read from environment variables
(BFGA_LLM_API_KEY / BFGA_LLM_API_URL / BFGA_LLM_MODEL / BFGA_LLM_TIMEOUT) at import
time. See the repository root `.env.example` for how to provide them.
If the environment variables are unset the module falls back to *literal placeholders*
so that `import` succeeds, but every chat call will fail with a clear `LLMCallError`
until the caller provides real credentials. Never commit a populated `.env`.
"""


# ============================================================
# LLM configuration — sourced from environment for safe distribution.
# ============================================================
import os as _os_config

_API_KEY_PLACEHOLDER = "REPLACE_ME_WITH_YOUR_LLM_API_KEY"
_API_URL_PLACEHOLDER = "https://api.example.com/v1/chat/completions"

API_KEY = _os_config.environ.get("BFGA_LLM_API_KEY", _API_KEY_PLACEHOLDER)
API_URL = _os_config.environ.get("BFGA_LLM_API_URL", _API_URL_PLACEHOLDER)
LLM_MODEL = _os_config.environ.get("BFGA_LLM_MODEL", "gemini-3.5-flash")


def _coerce_timeout(raw_value: str | None, default: int) -> int:
    try:
        return int(raw_value) if raw_value else default
    except (TypeError, ValueError):
        return default


LLM_TIMEOUT = _coerce_timeout(_os_config.environ.get("BFGA_LLM_TIMEOUT"), 300)


def validate_llm_credentials() -> None:
    """Raise ValueError if API credentials were not supplied via environment.

    Call this from the entry-points that actually make LLM calls (e.g.
    `parse_background_with_llm` in `m04_background_parser.py`). Just `import`-ing
    the module will not raise so that non-LLM callers can still load the schema.
    """
    if API_KEY == _API_KEY_PLACEHOLDER or not API_KEY:
        raise ValueError(
            "BFGA LLM API key is not configured. Set BFGA_LLM_API_KEY in your "
            "environment (see .env.example at the repository root) before running "
            "any code path that calls the LLM."
        )
    if API_URL == _API_URL_PLACEHOLDER or not API_URL:
        raise ValueError(
            "BFGA LLM API URL is not configured. Set BFGA_LLM_API_URL in your "
            "environment (see .env.example at the repository root)."
        )

# ============================================================
# External file paths (relative to the repository root)
#
# Both locations are environment-overridable so a user running on a different
# checkout or a different operating system can adjust without editing this file.
# When the environment variable is unset we resolve the path relative to the
# repository root (the directory that contains this very file is
# `code/.../v7_modules/`, so 4 levels up is the repo root).
# ============================================================
from pathlib import Path as _Path_config

_REPO_ROOT = _Path_config(__file__).resolve().parents[4]


def _resolve_repo_rel(env_var: str, default_relpath: str) -> str:
    """Return absolute path string. Prefer env override, fall back to repo-relative."""
    override = _os_config.environ.get(env_var)
    if override:
        return override
    return str(_REPO_ROOT / default_relpath)


# Source-papers metadata file. The aggregated CEG (with nodes/edges) is produced
# by the CEG construction pipeline and is not bundled here.
GRAPH_PATH = _resolve_repo_rel("BFGA_GRAPH_PATH", "data/CEG data/CEG data for 2027cases.json")
# Default output directory for any case-level JSON / Markdown reports.
OUTPUT_DIR = _resolve_repo_rel("BFGA_OUTPUT_DIR", "data/output")

# ============================================================
# Default reasoning configuration (v7)
# ============================================================
DEFAULT_CONFIG = {
    # Graph reasoning main loop
    "Epoch_max": 5,
    "Thinking_belief_init": 0.0,
    "Thinking_belief_threshold": 0.99,

    # Aggregation phase
    "Top_K": 3,
    "N_non_alg_type_count_max": 19,  # v7: 19-type fact sufficiency upper limit
    "vote_entropy_threshold": 0.90,

    # Pruning phase - basic dynamic width (v7 changed to W_init=2)
    "W_init": 2,  # v7: default pruning width 2
    "W_expand_gamma": 3,
    "W_expand_hard_cap": 3,
    "pruning_entropy_threshold": 0.50,
    "disable_dynamic_width_below_entropy": 1.10,

    # v7 new: concurrent pruning-exploration-aggregation loop
    # Take TopN from effective candidate node sorting as W-sum group source
    "pruning_top_n_candidates": 10,
    # W-sum group feedback decision threshold: when algorithm vote ratio improvement count
    # brought by a group's candidate set >= this value, judge as success
    "feedback_gain_threshold": 3,
    # Maximum backtracking times (to prevent infinite loop)
    "max_feedback_times": 5,
    # Per-round concurrent exploration timeout (to prevent a branch from hanging)
    "concurrent_explore_timeout": 60,

    # Node matching
    "string_similarity_threshold": 0.80,

    # Recommendation output
    "enable_node_type_filter": True,
    "node_type_low_support_z_threshold": 3.00,
    "epsilon": 1e-9,

    # Logging
    "log_detail_level": "debug",
}

# ============================================================
# Node type constants (same as v6)
# ============================================================
NON_ALG_TYPE_CODES = set(range(1, 15))
INDUCTION_TYPE_CODES = {15, 16, 17, 18, 19}
ALG_TYPE_CODES = {15, 16, 17, 18, 19}

NODE_TYPE_CODE_TO_NAME = {
    1: "01-Object Domain",
    2: "02-Object Type",
    3: "03-Operating Conditions",
    4: "04-Fault Location",
    5: "05-Fault Mode",
    6: "06-Fault Severity",
    7: "07-Compound Fault",
    8: "08-PHM Task",
    9: "09-Problem Scenario",
    10: "10-Dataset",
    11: "11-Sensor Information",
    12: "12-Training Data Availability",
    13: "13-Noise Level",
    14: "14-Computational Resource",
    15: "15-Data Preprocessing Algorithm",
    16: "16-Feature Extraction Algorithm",
    17: "17-Core Classifier Algorithm",
    18: "18-Data Generation Algorithm",
    19: "19-Training Optimization Algorithm",
}

INDUCTION_TYPE_NAMES = {
    "15": "15-Data Preprocessing Algorithm-Induction",
    "16": "16-Feature Extraction Algorithm-Induction",
    "17": "17-Core Classifier Algorithm-Induction",
    "18": "18-Data Generation Algorithm-Induction",
    "19": "19-Training Optimization Algorithm-Induction",
}

ALG_TYPE_FULL_NAMES = {
    "15-Data Preprocessing Algorithm": "15-Data Preprocessing Algorithm",
    "16-Feature Extraction Algorithm": "16-Feature Extraction Algorithm",
    "17-Core Classifier Algorithm": "17-Core Classifier Algorithm",
    "18-Data Generation Algorithm": "18-Data Generation Algorithm",
    "19-Training Optimization Algorithm": "19-Training Optimization Algorithm",
}

# v7 new: algorithm type code to English name mapping (for N_pruning array)
ALG_TYPE_ID_TO_NAME = {
    15: "15-Data Preprocessing Algorithm",
    16: "16-Feature Extraction Algorithm",
    17: "17-Core Classifier Algorithm",
    18: "18-Data Generation Algorithm",
    19: "19-Training Optimization Algorithm",
}


import re as _re_type_code

# Optimization: LRU cache for node_type -> type_code to avoid repeated regex matching per call.
# Measured under N=8424 nodes graph, single Epoch calls compute_vote_ratio_denominator hundreds of times,
# each node type_code is computed repeatedly, caching significantly reduces regex overhead.
_type_code_cache: dict[str, int] = {}


def get_type_code(node_type: str) -> int:
    """Extract the first two digits from node_type string as the type code."""
    cached = _type_code_cache.get(node_type)
    if cached is not None:
        return cached
    import re
    match = re.match(r"^(\d{2})", node_type)
    if match:
        code = int(match.group(1))
    else:
        code = 0
    _type_code_cache[node_type] = code
    return code


def is_non_algorithm_node(node_type: str) -> bool:
    """Determine if node is a non-algorithm node (01-14 or 15-Induction ~ 19-Induction)."""
    code = get_type_code(node_type)
    if code in NON_ALG_TYPE_CODES:
        return True
    if code in INDUCTION_TYPE_CODES and "Induction" in node_type:
        return True
    return False


def is_induction_node(node_type: str) -> bool:
    """Determine if node is an algorithm induction node (15-Induction ~ 19-Induction)."""
    code = get_type_code(node_type)
    return code in INDUCTION_TYPE_CODES and "Induction" in node_type


def is_concrete_algorithm_node(node_type: str) -> bool:
    """Determine if node is a concrete algorithm node (15-19, excluding Induction)."""
    code = get_type_code(node_type)
    return code in ALG_TYPE_CODES and "Induction" not in node_type


def compute_vote_ratio_denominator(
    alg_node_type: str,
    Non_alg_group: list[str],
    node_idx: dict[str, dict],
) -> int:
    """Compute vote_ratio denominator for a concrete algorithm class node_type.

    Rules (v8.x modification 4 - differentiated denominator by algorithm class):
      - 1-14 nodes (any node_type code 1-14 non-algorithm nodes): all counted in denominator
      - -Induction nodes with same code as alg_node_type: counted in denominator
      - -Induction nodes with other codes: not counted in denominator (according to 01-default
        edge connecting-by-code rule, this Induction node won't contribute vote to this
        algorithm class, so denominator should not be inflated)

    Returns:
        int denominator value. If all denominator items are 0, return 1 (avoid division by zero).

    Examples:
      Non_alg_group contains 1-14 each 1 + 15-Induction × 1 + 16-Induction × 1
      - alg_node_type = "15-DataPreprocessingAlgorithm"   → denominator = 14 + 1 = 15
      - alg_node_type = "18-DataGenerationAlgorithm"      → denominator = 14 + 0 = 14
    """
    if not Non_alg_group or node_idx is None:
        return 1

    target_code = get_type_code(alg_node_type)
    # Illegal algorithm class (neither 15-19 nor Induction 15-19) → default path: all counted
    if not (15 <= target_code <= 19):
        return max(1, len(Non_alg_group))

    count = 0
    for nid in Non_alg_group:
        node = node_idx.get(nid)
        if node is None:
            continue
        nt = node.get("node_type", "")
        if not nt:
            continue
        code = get_type_code(nt)
        # 1-14 nodes: counted in denominator
        if 1 <= code <= 14:
            count += 1
            continue
        # 15-19-Induction nodes: counted in denominator only when code matches
        if 15 <= code <= 19 and "Induction" in nt and code == target_code:
            count += 1
        # Other cases (Induction but code doesn't match): not counted
    return max(1, count)
