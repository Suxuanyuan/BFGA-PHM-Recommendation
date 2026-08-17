# -*- coding: utf-8 -*-
r"""
v7_modules/04_background_parser.py
===================================
Background constraint parsing module. Directly imported from v6_modules
(replace module reference at import time).
"""

import os
import json
from pathlib import Path
from typing import Any

from . import m00_config as config
from . import m03_llm_client as llm


_PROMPT_FILES = [
    "00-HyperparameterExtraction.md",
    "01-03,08-09_ObjectAndProblemNode.md",
    "04-07_FaultInformationNode.md",
    "10-14_DataAndResourceNode.md",
    "15-20_AlgorithmNode.md",
]


# Optimization: module-level one-time cache for prompt file contents.
# Previously each call to load_external_extraction_prompts would re-read disk,
# and PROMPT_DIR path issues (v5 version path) would trigger file-not-found warnings.
_prompts_cache: dict[str, dict[str, str]] = {}


def load_external_extraction_prompts(prompt_dir: str) -> dict[str, str]:
    """Read the prompt file collection required for background parsing.

    Optimization note (performance):
      - Read results for same prompt_dir are cached in _prompts_cache, repeated calls return directly.
    """
    if prompt_dir in _prompts_cache:
        return _prompts_cache[prompt_dir]

    prompts = {}
    dir_path = Path(prompt_dir)
    for fname in _PROMPT_FILES:
        fpath = dir_path / fname
        if fpath.exists():
            prompts[fname] = fpath.read_text(encoding="utf-8")
        else:
            print(f"[WARNING] Prompt file not found: {fpath}")
            prompts[fname] = ""
    _prompts_cache[prompt_dir] = prompts
    return prompts


def build_background_parse_system_prompt(prompts: dict[str, str]) -> str:
    lines = [
        "You are a knowledge graph construction assistant in the PHM (Prognostics and Health Management) domain.",
        "Your task is to map the user's background description to the following node types based on their description.",
        "Note: the user describes the problem background (constraint conditions), not asking you to recommend algorithms.",
        "Your output must be a pure JSON array, without any explanatory text.",
        "",
        "[Available Node Types (only the following types are allowed, no new types can be created)]",
        "",
        "--- Background Fact Nodes (01-14) ---",
        "01: ObjectDomain - options: Aviation/Aerospace/Shipbuilding/Industrial/Nuclear/Electronics/Vehicle/Other",
        "02: ObjectType - device name, e.g.: Bearing/Gearbox/Motor/Engine/Battery",
        "03: OperatingCondition - options: SingleCondition/MultiCondition/VariableCondition",
        "04: FaultLocation - specific equipment part, e.g.: Rotor/Stator/BearingInnerRace/BearingOuterRace/Gear etc.",
        "05: FaultMode - e.g.: Pitting/Spalling/Wear/Crack/Unbalance/Misalignment/ShortCircuit/OpenCircuit",
        "06: FaultSeverity - options: SingleSeverity/MultiSeverity",
        "07: IncludesCompositeFault - options: NoCompositeFault/IntraStructuralCompositeFault/CrossStructuralCompositeFault",
        "08: PHMTask - options: DetectionTask/DiagnosisTask/PredictionTask/EvaluationTask/OtherTask",
        "09: ProblemScenario - options: SmallFaultSample/ZeroFaultSample/DistributionMismatch/Uncertainty/CompositeFault/ComplexSystem/EarlyDegradationPrediction/MultiSourceHeterogeneousMultimodalData/TrustworthyInterpretable/Other (10 in total, max 3)",
        "10: Dataset - specific dataset name, e.g.: CWRU/XJTU-SY/PU etc.",
        "11: SensorInformation - e.g.: AccelerationSensor/AcousticEmissionSensor/CurrentSensor etc.",
        "12: AvailableTrainingDataAmount - options: ZeroSample/Scarce/Sufficient",
        "13: NoiseLevel - options: HighNoise/Normal",
        "14: ComputingResource - options: LowResource/Unmentioned/HighResource",
        "",
        "--- Algorithm Induction Nodes (used to represent intermediate semantics at the algorithm category level, "
        "cannot be used as final recommendations) ---",
        "15-Induction: DataPreprocessingAlgorithm-Induction",
        "16-Induction: FeatureExtractionAlgorithm-Induction",
        "17-Induction: CoreDiscriminatorAlgorithm-Induction",
        "18-Induction: DataGenerationAlgorithm-Induction",
        "19-Induction: TrainingOptimizationAlgorithm-Induction",
        "",
        "--- Output Format Requirements ---",
        "Output only JSON array, no explanatory text.",
        "Each constraint object must contain: constraint_id (B001, B002...incrementing), node_type, node_name, raw_text.",
        "If a piece of text cannot be mapped to any of the above node types, skip it, do not force classification.",
        "Do not recommend specific algorithms.",
    ]
    return "\n".join(lines)


def parse_background_with_llm(
    Background_string: str,
    extraction_prompts: dict[str, str],
) -> list[dict]:
    system_prompt = build_background_parse_system_prompt(extraction_prompts)
    user_prompt = f"[User Background Description]\n{Background_string}"

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    raw_reply = llm.chat_llm(messages)
    try:
        result = llm.parse_json_response(raw_reply)
        if isinstance(result, list):
            return result
        else:
            raise ValueError(f"Expected list, got {type(result)}")
    except Exception as e:
        print(f"[WARNING] Background parsing failed: {e}")
        print(f"Raw reply: {raw_reply[:500]}")
        return []
