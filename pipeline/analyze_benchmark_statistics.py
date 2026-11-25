#!/usr/bin/env python3
"""
Comprehensive Statistical Profiling Script for guardslm_fresh/guardslm_2000_benchmark_no_cua.jsonl
Computes:
1. Core Scale & Text Volume Distributions
2. 5-Tier Archetype & Role Breakdown
3. 4-Tier Decision Label Spectrum & Longitudinal Turn Dynamics
4. 7-Tier Assistance Depth Hierarchy (Requested Levels 0-6 & None) with Label Cross-Tabulation
5. Canonical 11-Class Attack Taxonomy Distribution
6. Empirical Grounding & Provenance Attribution
7. Data Hygiene, CUA Absence & SHA-256 Verification
"""

import hashlib
import json
import os
import re
from collections import Counter, defaultdict

TARGET_FILE = "guardslm_fresh/guardslm_2000_benchmark_no_cua.jsonl"

def sha256_of_file(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def determine_archetype(session):
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

def main():
    print(f"Loading {TARGET_FILE}...")
    with open(TARGET_FILE, "r", encoding="utf-8") as f:
        sessions = [json.loads(line) for line in f]

    total_sessions = len(sessions)
    total_turns = sum(len(s.get("turns", [])) for s in sessions)
    
    # 1. Scale & Turn Counts
    turns_per_session = [len(s.get("turns", [])) for s in sessions]
    min_turns = min(turns_per_session)
    max_turns = max(turns_per_session)
    avg_turns = total_turns / total_sessions
    
    # Text volume
    req_words, req_chars = [], []
    reason_words, reason_chars = [], []
    reply_words, reply_chars = [], []
    
    # 2. Archetype & Roles
    archetype_counts = Counter()
    role_categories = Counter()
    
    # 3. Decision Labels & Progression
    label_counts = Counter()
    turn_label_progression = defaultdict(Counter)
    
    # 4. Assistance Depth
    level_counts = Counter()
    level_label_matrix = defaultdict(Counter)
    
    # 5. Attack Types
    attack_counts = Counter()
    attack_label_matrix = defaultdict(Counter)
    
    # 6. Provenance
    source_counts = Counter()
    
    # 7. Hygiene
    cua_count = 0
    id_errors = []
    
    for s_idx, s in enumerate(sessions):
        sid = s.get("session_id")
        expected_sid = f"S-{s_idx + 1:04d}"
        if sid != expected_sid:
            id_errors.append((s_idx, sid, expected_sid))
            
        arch = determine_archetype(s)
        archetype_counts[arch] += 1
        
        # Categorize role
        r = str(s.get("role", "")).lower()
        if "instructor" in r or "professor" in r:
            role_categories["Instructor / Professor"] += 1
        elif "ta" in r:
            role_categories["Teaching Assistant (TA)"] += 1
        elif "staff" in r:
            role_categories["Academic / Administrative Staff"] += 1
        else:
            role_categories["Student"] += 1
            
        # Provenance source
        prov_src = str(s.get("provenance", {}).get("context_anchor_source", ""))
        if "STUDYCHAT" in prov_src:
            source_counts["StudyChat (CS Coursework Logs)"] += 1
        elif "Eedi" in prov_src or "EEDI" in prov_src or "Mathematics" in s.get("role", ""):
            source_counts["Eedi (Math Misconceptions)"] += 1
        elif "GoH" in prov_src or "Academic" in prov_src:
            source_counts["Geometry of Harmfulness (Academic Integrity Shard)"] += 1
        else:
            source_counts["Direct Curated Academic Anchor"] += 1
            
        turns = s.get("turns", [])
        for t_idx, t in enumerate(turns, 1):
            if "cua_snapshot" in t:
                cua_count += 1
                
            req = t.get("request", "")
            reason = t.get("reason", "")
            reply = t.get("reply", "")
            
            req_chars.append(len(req))
            req_words.append(len(req.split()))
            reason_chars.append(len(reason))
            reason_words.append(len(reason.split()))
            reply_chars.append(len(reply))
            reply_words.append(len(reply.split()))
            
            lbl = t.get("label")
            label_counts[lbl] += 1
            turn_label_progression[t_idx][lbl] += 1
            
            lvl = t.get("requested_level")
            lvl_str = f"Level {lvl}" if lvl is not None else "Level None (Unspecified)"
            level_counts[lvl_str] += 1
            level_label_matrix[lvl_str][lbl] += 1
            
            atk = t.get("attack_type")
            attack_counts[atk] += 1
            attack_label_matrix[atk][lbl] += 1

    file_size_bytes = os.path.getsize(TARGET_FILE)
    sha_hash = sha256_of_file(TARGET_FILE)

    stats = {
        "file": TARGET_FILE,
        "file_size_bytes": file_size_bytes,
        "sha256": sha_hash,
        "total_sessions": total_sessions,
        "total_turns": total_turns,
        "turns_min": min_turns,
        "turns_max": max_turns,
        "turns_avg": avg_turns,
        "id_monotonic_errors": len(id_errors),
        "cua_snapshots_found": cua_count,
        "archetypes": dict(archetype_counts),
        "roles": dict(role_categories),
        "labels": dict(label_counts),
        "progression": {str(k): dict(v) for k, v in turn_label_progression.items()},
        "levels": dict(level_counts),
        "level_label_matrix": {k: dict(v) for k, v in level_label_matrix.items()},
        "attacks": dict(attack_counts),
        "attack_label_matrix": {k: dict(v) for k, v in attack_label_matrix.items()},
        "provenance": dict(source_counts),
        "text_metrics": {
            "request_avg_words": sum(req_words) / len(req_words),
            "request_avg_chars": sum(req_chars) / len(req_chars),
            "reason_avg_words": sum(reason_words) / len(reason_words),
            "reason_avg_chars": sum(reason_chars) / len(reason_chars),
            "reply_avg_words": sum(reply_words) / len(reply_words),
            "reply_avg_chars": sum(reply_chars) / len(reply_chars),
            "total_request_words": sum(req_words),
            "total_reply_words": sum(reply_words),
            "total_dialogue_words": sum(req_words) + sum(reply_words)
        }
    }

    print("\n--- RESULTS JSON ---")
    print(json.dumps(stats, indent=2))

if __name__ == "__main__":
    main()
