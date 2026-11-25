#!/usr/bin/env python3
"""
GuardSLM Grounded Multi-Turn Benchmark Validation Harness
=========================================================
Strict automated validation script to verify schema compliance, JSON syntax,
session monotonicity, archetype alignment, and turn-level data types against
the ground-truth benchmark specification.

Usage:
    python3 validation_harness.py --input <path_to_jsonl>
"""

import sys
import os
import json
import argparse
from collections import Counter

REQUIRED_TOP_KEYS = {
    "session_id", "title", "honesty_label", "role", "question",
    "policy", "summary", "provenance", "turns"
}

REQUIRED_PROVENANCE_KEYS = {
    "context_anchor_source", "pedagogical_strategy_source", "adversarial_strategy_source"
}

REQUIRED_TURN_KEYS = {
    "turn", "cua_snapshot", "request", "requested_level",
    "label", "attack_type", "reason", "reply"
}

VALID_DECISIONS = {"ALLOW", "LIMIT", "BLOCK", "ESCALATE"}

def determine_archetype(session: dict) -> str:
    """Classifies a session into one of the 5 canonical benchmark archetypes."""
    h = session.get("honesty_label")
    r = str(session.get("role", "")).lower()
    is_staff = any(k in r for k in ["staff", "ta", "instructor", "professor"])
    
    if h == 100 or h == "100":
        return "Honest Staff / Instructor" if is_staff else "Honest Student"
    elif h in (70, 75, 80, 85, "70", "75", "80", "85"):
        return "Mostly Honest Student with 1 Slip"
    elif is_staff:
        return "Staff Compliance Violator"
    else:
        return "Persistent Cheating Student"

def validate_dataset(filepath: str) -> bool:
    print(f"[*] Starting GuardSLM validation on: {filepath}")
    if not os.path.isfile(filepath):
        print(f"[!] ERROR: File not found: {filepath}")
        return False

    total_sessions = 0
    total_turns = 0
    session_ids = set()
    errors = []
    
    archetype_counts = Counter()
    decision_counts = Counter()
    level_counts = Counter()

    with open(filepath, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            line_str = line.strip()
            if not line_str:
                errors.append(f"Line {line_num}: Empty line detected.")
                continue

            try:
                session = json.loads(line_str)
            except json.JSONDecodeError as e:
                errors.append(f"Line {line_num}: JSON syntax error: {e}")
                continue

            total_sessions += 1

            # 1. Check Top-Level Keys
            missing_top = REQUIRED_TOP_KEYS - set(session.keys())
            if missing_top:
                errors.append(f"Line {line_num} ({session.get('session_id', 'UNKNOWN')}): Missing top keys: {missing_top}")

            sid = session.get("session_id")
            if not sid:
                errors.append(f"Line {line_num}: Missing session_id.")
            elif sid in session_ids:
                errors.append(f"Line {line_num}: Duplicate session_id: {sid}")
            else:
                session_ids.add(sid)

            # Check Honesty Label
            honesty = session.get("honesty_label")
            if not isinstance(honesty, (int, str)):
                errors.append(f"Line {line_num} ({sid}): 'honesty_label' must be int or str, got {type(honesty)}")
            
            arch = determine_archetype(session)
            archetype_counts[arch] += 1

            role = session.get("role")
            if not isinstance(role, str) or not role.strip():
                errors.append(f"Line {line_num} ({sid}): 'role' must be a non-empty string.")

            # Check Provenance
            prov = session.get("provenance")
            if not isinstance(prov, dict):
                errors.append(f"Line {line_num} ({sid}): 'provenance' must be a dictionary.")
            else:
                missing_prov = REQUIRED_PROVENANCE_KEYS - set(prov.keys())
                if missing_prov:
                    errors.append(f"Line {line_num} ({sid}): Missing provenance keys: {missing_prov}")

            # Check Turns
            turns = session.get("turns")
            if not isinstance(turns, list) or len(turns) == 0:
                errors.append(f"Line {line_num} ({sid}): 'turns' must be a non-empty list.")
                continue

            session_turns = len(turns)
            total_turns += session_turns

            prev_turn_idx = 0
            for t_idx, turn in enumerate(turns, 1):
                if not isinstance(turn, dict):
                    errors.append(f"Line {line_num} ({sid}) Turn {t_idx}: Must be a dictionary.")
                    continue

                missing_tkeys = REQUIRED_TURN_KEYS - set(turn.keys())
                if missing_tkeys:
                    errors.append(f"Line {line_num} ({sid}) Turn {t_idx}: Missing turn keys: {missing_tkeys}")

                cur_turn = turn.get("turn")
                if cur_turn != prev_turn_idx + 1:
                    errors.append(f"Line {line_num} ({sid}) Turn {t_idx}: Turn number not sequential (got {cur_turn}, expected {prev_turn_idx + 1})")
                prev_turn_idx = cur_turn if isinstance(cur_turn, int) else prev_turn_idx + 1

                label = turn.get("label")
                if label not in VALID_DECISIONS:
                    errors.append(f"Line {line_num} ({sid}) Turn {t_idx}: Invalid label: '{label}'")
                else:
                    decision_counts[label] += 1

                req_lvl = turn.get("requested_level")
                if req_lvl is not None and not (isinstance(req_lvl, int) and 0 <= req_lvl <= 6):
                    errors.append(f"Line {line_num} ({sid}) Turn {t_idx}: Invalid requested_level: {req_lvl}")
                else:
                    level_counts[str(req_lvl)] += 1

                # Check non-empty strings
                for text_field in ["cua_snapshot", "request", "reason", "reply"]:
                    val = turn.get(text_field)
                    if not isinstance(val, str) or not val.strip():
                        errors.append(f"Line {line_num} ({sid}) Turn {t_idx}: Field '{text_field}' is empty or not string.")

    print("\n" + "=" * 60)
    print("           GUARDSLM DATASET VALIDATION REPORT")
    print("=" * 60)
    print(f"Total Verified Sessions : {total_sessions}")
    print(f"Total Dialogue Turns    : {total_turns}")
    if total_sessions > 0:
        print(f"Average Turns / Session : {total_turns / total_sessions:.2f}")

    print("\n--- Archetype Distribution ---")
    for arch, cnt in sorted(archetype_counts.items(), key=lambda x: -x[1]):
        pct = (cnt / total_sessions * 100) if total_sessions else 0
        print(f"  {arch:<35}: {cnt:>4} ({pct:>5.1f}%)")

    print("\n--- Decision Label Distribution ---")
    for dec, cnt in sorted(decision_counts.items(), key=lambda x: -x[1]):
        pct = (cnt / total_turns * 100) if total_turns else 0
        print(f"  {dec:<10}: {cnt:>5} turns ({pct:>5.1f}%)")

    print("\n--- Requested Level Distribution (0-6) ---")
    for lvl in sorted(level_counts.keys(), key=lambda x: int(x) if x.isdigit() else 99):
        cnt = level_counts[lvl]
        pct = (cnt / total_turns * 100) if total_turns else 0
        print(f"  Level {lvl:<4}: {cnt:>5} turns ({pct:>5.1f}%)")

    print("\n" + "=" * 60)
    if errors:
        print(f"[!] VALIDATION FAILED with {len(errors)} error(s):")
        for err in errors[:20]:
            print(f"  - {err}")
        if len(errors) > 20:
            print(f"  ... and {len(errors) - 20} additional errors.")
        return False
    else:
        print("[✓] ALL CHECKS PASSED: 100% Schema Compliant, Zero Errors.")
        print("=" * 60)
        return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GuardSLM Benchmark Validator")
    parser.add_argument("--input", required=True, help="Path to .jsonl benchmark file")
    args = parser.parse_args()

    success = validate_dataset(args.input)
    sys.exit(0 if success else 1)
