# -*- coding: utf-8 -*-
r"""
v7_modules/03_llm_client.py
============================
LLM call client. Directly copied from v6_modules.m03_llm_client.
"""

import json
import time
import requests
from typing import Any, Optional

from . import m00_config as cfg


class LLMCallError(Exception):
    pass


def chat_llm(
    messages: list[dict],
    model: str = "",
    temperature: float = 0.1,
    max_tokens: int = 4096,
) -> str:
    model = model or cfg.LLM_MODEL
    # Refuse to make outbound requests with the placeholder credentials shipped in
    # the public release. Callers must populate BFGA_LLM_API_KEY / BFGA_LLM_API_URL.
    cfg.validate_llm_credentials()
    url = cfg.API_URL
    headers = {
        "Authorization": f"Bearer {cfg.API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=cfg.LLM_TIMEOUT)
        resp.raise_for_status()
        data = resp.json()
        if "choices" not in data or not data["choices"]:
            raise LLMCallError(f"No choices in response: {data}")
        return data["choices"][0]["message"]["content"]
    except requests.exceptions.Timeout:
        raise LLMCallError("LLM request timeout")
    except requests.exceptions.RequestException as e:
        raise LLMCallError(f"LLM request failed: {e}")


def parse_json_response(text: str) -> Any:
    text = text.strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    import re
    m = re.search(r"```(?:json)?\s*([\s\S]+?)\s*```", text)
    if m:
        candidate = m.group(1).strip()
        try:
            return json.loads(candidate)
        except json.JSONDecodeError:
            pass

    for start_char, end_char in [("[", "]"), ("{", "}")]:
        idx = text.find(start_char)
        if idx >= 0:
            depth = 0
            end_idx = -1
            for i, ch in enumerate(text[idx:], start=idx):
                if ch == start_char:
                    depth += 1
                elif ch == end_char:
                    depth -= 1
                    if depth == 0:
                        end_idx = i + 1
                        break
            if end_idx > 0:
                candidate = text[idx:end_idx]
                try:
                    return json.loads(candidate)
                except json.JSONDecodeError:
                    pass

    raise ValueError(f"Cannot parse JSON from LLM response:\n{text[:500]}")
