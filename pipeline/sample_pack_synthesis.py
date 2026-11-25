#!/usr/bin/env python3
"""
Append Pack 135 (S-993 to S-1000) to guardslm_fresh/guardslm_grounded_sessions.jsonl.
Grounded in GoH academic usable subset index 0 (trajectory_id: 2978).
Theme: Plagiarism evasion vs academic synthesis, translation ethics, research governance, and records integrity.
Archetypes: 2 Honest Students, 2 Mostly Honest Students, 2 Persistent Cheaters, 1 Honest Staff, 1 Staff Violator.
FINAL MILESTONE: Reaches 1,000 verified sessions (S-001 through S-1000)!
"""

import sys
import os
import json

TARGET_FILE = "/home/regenesis/Desktop/Web Dev/dataset-analysis/guardslm_fresh/guardslm_grounded_sessions.jsonl"

def load_pack_135():
    with open("scratch/part1.json", "r") as f:
        p1 = json.load(f)
    with open("scratch/part2.json", "r") as f:
        p2 = json.load(f)
    return p1 + p2

PACK_135_SESSIONS = load_pack_135()

def validate_pack():
    print(f"Validating {len(PACK_135_SESSIONS)} sessions for Pack 135...")
    expected_ids = [f"S-{i}" for i in range(993, 1001)]
    found_ids = [s["session_id"] for s in PACK_135_SESSIONS]
    assert found_ids == expected_ids, f"Session ID mismatch: {found_ids} vs {expected_ids}"
    
    honesty_counts = {}
    staff_count = 0
    student_count = 0
    keywords = ["staff", "ta", "instructor", "professor"]
    
    for s in PACK_135_SESSIONS:
        h = s["honesty_label"]
        honesty_counts[h] = honesty_counts.get(h, 0) + 1
        r = s["role"].lower()
        is_staff = any(k in r for k in keywords)
        
        # Verify no "ta" in student roles
        if not is_staff:
            student_count += 1
            assert "ta" not in r, f"Forbidden 'ta' found in student role: {s['role']}"
            assert not any(k in r for k in ["staff", "instructor", "professor"]), f"Staff keyword in student role: {s['role']}"
        else:
            staff_count += 1
            
        # Verify turns
        turns = s["turns"]
        assert len(turns) == 5, f"{s['session_id']} has {len(turns)} turns instead of 5"
        for t_idx, t in enumerate(turns, 1):
            assert t["turn"] == t_idx, f"Turn number mismatch in {s['session_id']}: {t['turn']} vs {t_idx}"
            assert t["label"] in ["ALLOW", "LIMIT", "BLOCK", "ESCALATE"], f"Invalid label {t['label']} in {s['session_id']}"
            assert isinstance(t["requested_level"], int), f"Invalid requested_level in {s['session_id']}"
            assert len(t["request"]) > 10, f"Request too short in {s['session_id']} turn {t_idx}"
            assert len(t["reply"]) > 10, f"Reply too short in {s['session_id']} turn {t_idx}"
            assert len(t["cua_snapshot"]) > 10, f"Snapshot too short in {s['session_id']} turn {t_idx}"
            assert len(t["reason"]) > 5, f"Reason too short in {s['session_id']} turn {t_idx}"
            
        # Verify provenance GoH anchor
        prov = s["provenance"]
        assert prov["context_anchor_source"] == "GoH academic usable subset index 0 (trajectory_id: 2978)", f"Invalid GoH anchor in {s['session_id']}"
        
    assert student_count == 6, f"Expected 6 student sessions, got {student_count}"
    assert staff_count == 2, f"Expected 2 staff sessions, got {staff_count}"
    assert honesty_counts.get(100, 0) == 3, f"Expected 3 honesty=100 (2 students + 1 staff), got {honesty_counts.get(100)}"
    assert (honesty_counts.get(75, 0) + honesty_counts.get(80, 0)) == 2, f"Expected 2 mostly honest, got {honesty_counts}"
    assert (honesty_counts.get(15, 0) + honesty_counts.get(0, 0)) == 2, f"Expected 2 persistent cheaters, got {honesty_counts}"
    assert honesty_counts.get(20, 0) == 1, f"Expected 1 staff violator (20), got {honesty_counts.get(20)}"
    
    print("Pack 135 internal validation PASSED! All 8 sessions conform strictly to 2:2:2:1:1 canonical distribution.")

def append_to_file():
    with open(TARGET_FILE, "r") as f:
        existing = [json.loads(line) for line in f]
    print(f"Current sessions in target file: {len(existing)}")
    assert len(existing) == 992, f"Expected 992 sessions, found {len(existing)}"
    assert existing[-1]["session_id"] == "S-992", f"Last session is {existing[-1]['session_id']}, expected S-992"
    
    with open(TARGET_FILE, "a") as f:
        for s in PACK_135_SESSIONS:
            f.write(json.dumps(s) + "\n")
            
    with open(TARGET_FILE, "r") as f:
        updated = [json.loads(line) for line in f]
    print(f"Updated session count in target file: {len(updated)}")
    assert len(updated) == 1000, f"Expected 1000 sessions, found {len(updated)}"
    assert updated[-1]["session_id"] == "S-1000", f"Last session is {updated[-1]['session_id']}, expected S-1000"
    print("============================================================")
    print("MILESTONE ACHIEVED: 1,000 VERIFIED SESSIONS REACHED!")
    print("============================================================")

if __name__ == "__main__":
    validate_pack()
    if "--execute" in sys.argv:
        append_to_file()
    else:
        print("Dry run complete. Run with --execute to append.")
