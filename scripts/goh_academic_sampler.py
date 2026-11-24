#!/usr/bin/env python3
"""
GoH Academic Usable Subset Sampler
=================================
Provides structured access to the curated subset of Geometry of Harmfulness (GoH)
cases that are directly relevant to academic integrity, exam proctoring, and CS educational labs.

Features:
- Reads from `GuardSLM_source_exports/geometry_of_harmfulness/goh_academic_usable_subset.jsonl`.
- Implements deterministic indexing and circular wrap-around if the index exceeds total cases.
"""

import json
import os
from typing import Dict, Any, List

SUBSET_PATH = "GuardSLM_source_exports/geometry_of_harmfulness/goh_academic_usable_subset.jsonl"

_CACHE: List[Dict[str, Any]] = []

def load_usable_goh() -> List[Dict[str, Any]]:
    global _CACHE
    if not _CACHE:
        if not os.path.exists(SUBSET_PATH):
            raise FileNotFoundError(f"GoH usable subset file not found at: {SUBSET_PATH}")
        with open(SUBSET_PATH, "r", encoding="utf-8") as f:
            _CACHE = [json.loads(line) for line in f if line.strip()]
    return _CACHE

def get_goh_case(index: int) -> Dict[str, Any]:
    """
    Retrieves a GoH trajectory from the usable academic subset.
    Automatically wraps around (modulo) if index >= total cases.
    """
    cases = load_usable_goh()
    total = len(cases)
    if total == 0:
        raise ValueError("GoH usable subset is empty.")
    wrapped_index = index % total
    return cases[wrapped_index]

def get_total_cases() -> int:
    return len(load_usable_goh())

if __name__ == "__main__":
    cases = load_usable_goh()
    print(f"[*] GoH Usable Academic Subset loaded: {len(cases)} trajectories.")
    
    # Test wrap around
    print("\n--- Testing Wrap-Around Logic ---")
    case_0 = get_goh_case(0)
    case_wrap = get_goh_case(len(cases)) # Should wrap around to 0
    print(f"Index 0:    traj_id={case_0['trajectory_id']} | objective={case_0['objective'][:60]}...")
    print(f"Index {len(cases)}:  traj_id={case_wrap['trajectory_id']} | objective={case_wrap['objective'][:60]}...")
    assert case_0['trajectory_id'] == case_wrap['trajectory_id'], "Wrap-around assertion failed!"
    print("[✓] Wrap-around logic verified successfully!")
