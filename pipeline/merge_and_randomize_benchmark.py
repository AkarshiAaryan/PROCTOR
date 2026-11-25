#!/usr/bin/env python3
"""
Merge and Randomize GuardSLM 2,000-Session Benchmark.

Combines guardslm_fresh/sessions_test.jsonl (1,000 sessions) and
guardslm_fresh/merged.jsonl (1,000 sessions).
- Randomizes only the order of sessions using random.seed(42).
- Dialogue turns within each session remain strictly untouched.
- Re-indexes session IDs sequentially from S-0001 to S-2000.
- Generates two parallel datasets:
    1. guardslm_fresh/guardslm_2000_benchmark_with_cua.jsonl (retains cua_snapshot)
    2. guardslm_fresh/guardslm_2000_benchmark_no_cua.jsonl (removes cua_snapshot)
- Source files are treated as strictly read-only.
"""

import copy
import hashlib
import json
import random
import sys

SOURCE_FILE_1 = "guardslm_fresh/sessions_test.jsonl"
SOURCE_FILE_2 = "guardslm_fresh/merged.jsonl"

OUT_WITH_CUA = "guardslm_fresh/guardslm_2000_benchmark_with_cua.jsonl"
OUT_NO_CUA = "guardslm_fresh/guardslm_2000_benchmark_no_cua.jsonl"

EXPECTED_SHA_1 = "0459cb654165bba22c8fbbd9b314031071c4f5c25a0009ab9b83074a8c2fd548"
EXPECTED_SHA_2 = "45e7423b5741b3e00eb3bdfc1bb6b8a6573d3a1c8a17c32bb67e77433fcbd939"

RANDOM_SEED = 42

def sha256_of_file(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def main():
    print("[1] Verifying source files checksums before loading...")
    sha1_before = sha256_of_file(SOURCE_FILE_1)
    sha2_before = sha256_of_file(SOURCE_FILE_2)
    
    assert sha1_before == EXPECTED_SHA_1, f"Checksum mismatch for {SOURCE_FILE_1}: {sha1_before}"
    assert sha2_before == EXPECTED_SHA_2, f"Checksum mismatch for {SOURCE_FILE_2}: {sha2_before}"
    print("    Source checksums verified OK.")

    print(f"[2] Reading {SOURCE_FILE_1} (Contributor 1)...")
    with open(SOURCE_FILE_1, "r", encoding="utf-8") as f:
        sessions_1 = [json.loads(line) for line in f]
    assert len(sessions_1) == 1000, f"Expected 1000 sessions in {SOURCE_FILE_1}, got {len(sessions_1)}"

    print(f"[3] Reading {SOURCE_FILE_2} (Contributor 2)...")
    with open(SOURCE_FILE_2, "r", encoding="utf-8") as f:
        sessions_2 = [json.loads(line) for line in f]
    assert len(sessions_2) == 1000, f"Expected 1000 sessions in {SOURCE_FILE_2}, got {len(sessions_2)}"

    all_sessions = sessions_1 + sessions_2
    assert len(all_sessions) == 2000, f"Expected 2000 total sessions, got {len(all_sessions)}"
    print(f"    Loaded {len(all_sessions)} total sessions.")

    print(f"[4] Randomizing session order using seed={RANDOM_SEED}...")
    random.seed(RANDOM_SEED)
    random.shuffle(all_sessions)

    print("[5] Re-indexing session IDs to S-0001..S-2000 and creating dual datasets...")
    sessions_with_cua = []
    sessions_no_cua = []

    for idx, raw_session in enumerate(all_sessions):
        new_sid = f"S-{idx + 1:04d}"

        # Session with CUA
        s_cua = copy.deepcopy(raw_session)
        s_cua["session_id"] = new_sid
        sessions_with_cua.append(s_cua)

        # Session without CUA
        s_no_cua = copy.deepcopy(raw_session)
        s_no_cua["session_id"] = new_sid
        for t in s_no_cua.get("turns", []):
            t.pop("cua_snapshot", None)
        sessions_no_cua.append(s_no_cua)

    print(f"[6] Writing {OUT_WITH_CUA}...")
    with open(OUT_WITH_CUA, "w", encoding="utf-8") as f:
        for s in sessions_with_cua:
            f.write(json.dumps(s) + "\n")
    print(f"    Written {len(sessions_with_cua)} sessions to {OUT_WITH_CUA}.")

    print(f"[7] Writing {OUT_NO_CUA}...")
    with open(OUT_NO_CUA, "w", encoding="utf-8") as f:
        for s in sessions_no_cua:
            f.write(json.dumps(s) + "\n")
    print(f"    Written {len(sessions_no_cua)} sessions to {OUT_NO_CUA}.")

    print("[8] Verifying source files checksums after writing...")
    sha1_after = sha256_of_file(SOURCE_FILE_1)
    sha2_after = sha256_of_file(SOURCE_FILE_2)
    assert sha1_after == EXPECTED_SHA_1, "Source file 1 was modified!"
    assert sha2_after == EXPECTED_SHA_2, "Source file 2 was modified!"
    print("    Source files remained 100% UNTOUCHED.")

    print("\n[SUCCESS] Both benchmark files generated successfully!")

if __name__ == "__main__":
    main()
