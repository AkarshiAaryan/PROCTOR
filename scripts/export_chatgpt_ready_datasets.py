#!/usr/bin/env python3
"""
GuardSLM: Export Source Datasets into Standardized, ChatGPT-Ready Test Cases

This script standardizes the raw corpora from:
1. StudyChat (Undergraduate CS conversations)
2. Eedi (Math Socratic tutoring interventions)
3. Geometry of Harmfulness Shard 1 (Multi-turn adversarial red-teaming trajectories)

Into clean, self-contained, and intuitive test-case formats optimized for:
- Direct ingestion into ChatGPT / Claude / Gemini context windows
- Uploading to ChatGPT Code Interpreter / Advanced Data Analysis
- Human inspection in clean Markdown format
"""

import gzip
import json
import os
import sys

WORKSPACE = "/home/regenesis/Desktop/Web Dev/dataset-analysis"
OUTPUT_DIR = os.path.join(WORKSPACE, "datasets/chatgpt_ready_source_benchmarks")
SAMPLES_DIR = os.path.join(OUTPUT_DIR, "samples")
os.makedirs(SAMPLES_DIR, exist_ok=True)

STUDYCHAT_SRC = os.path.join(WORKSPACE, "GuardSLM_source_exports/studychat/shards/studychat_conversations.jsonl.gz")
EEDI_SRC = os.path.join(WORKSPACE, "GuardSLM_source_exports/eedi/shards/eedi_interventions.jsonl.gz")
GOH_SRC = os.path.join(WORKSPACE, "GuardSLM_source_exports/geometry_of_harmfulness/shards/goh_trajectories_shard_01.jsonl.gz")

def export_studychat():
    print("Processing StudyChat...")
    out_jsonl = os.path.join(OUTPUT_DIR, "studychat_test_cases.jsonl")
    sample_md = os.path.join(SAMPLES_DIR, "studychat_sample_20.md")
    sample_json = os.path.join(SAMPLES_DIR, "studychat_sample_20.json")

    cases = []
    samples = []

    with gzip.open(STUDYCHAT_SRC, "rt", encoding="utf-8") as f_in, open(out_jsonl, "w", encoding="utf-8") as f_out:
        for idx, line in enumerate(f_in, start=1):
            raw = json.loads(line)
            
            # Format clean messages
            formatted_messages = []
            for m in raw.get("messages", []):
                role = m.get("role") or ("user" if m.get("speaker") == "student" else "assistant")
                speaker = "Student" if (m.get("speaker") == "student" or role == "user" or role == "student") else "AI Assistant"
                formatted_messages.append({
                    "sequence": m.get("sequence"),
                    "turn": m.get("turn_index"),
                    "speaker": speaker,
                    "role": "user" if speaker == "Student" else "assistant",
                    "text": (m.get("text") or "").strip(),
                    "dialogue_act": m.get("original_dialogue_act")
                })
            
            clean_case = {
                "case_id": f"STUDYCHAT_{idx:04d}",
                "dataset": "StudyChat",
                "domain": "Computer Science & Programming",
                "assignment_code": raw.get("topic", "unspecified"),
                "scenario_title": raw.get("chat_title", "").strip() or f"CS Programming Inquiry {idx}",
                "academic_term": raw.get("semester"),
                "total_turns": raw.get("total_turns", len(formatted_messages)//2),
                "total_messages": len(formatted_messages),
                "original_conversation_id": raw.get("conversation_id"),
                "conversation": formatted_messages
            }
            
            f_out.write(json.dumps(clean_case, ensure_ascii=False) + "\n")
            if idx <= 20:
                samples.append(clean_case)

    # Write samples in JSON
    with open(sample_json, "w", encoding="utf-8") as f_sjson:
        json.dump(samples, f_sjson, indent=2, ensure_ascii=False)

    # Write samples in human/ChatGPT-ready Markdown
    with open(sample_md, "w", encoding="utf-8") as f_smd:
        f_smd.write("# StudyChat: Curated 20 Representative Test Cases for ChatGPT\n\n")
        f_smd.write("> **Dataset**: StudyChat (Undergraduate Computer Science Conversations)\n")
        f_smd.write("> **Domain**: Python Programming, Data Science, Algorithms, Data Structures, Debugging\n\n---\n\n")
        for sc in samples:
            f_smd.write(f"## Test Case `{sc['case_id']}`: {sc['scenario_title']}\n")
            f_smd.write(f"- **Assignment Topic**: `{sc['assignment_code']}` | **Semester**: `{sc['academic_term']}`\n")
            f_smd.write(f"- **Conversation Length**: {sc['total_turns']} turns ({sc['total_messages']} messages)\n\n")
            f_smd.write("### Multi-Turn Dialogue Transcript:\n\n")
            for m in sc["conversation"]:
                f_smd.write(f"**[{m['speaker']} (Turn {m['turn']})]**:\n{m['text']}\n\n")
            f_smd.write("---\n\n")

    print(f"StudyChat complete. Exported {idx} cases.")

def export_eedi():
    print("Processing Eedi...")
    out_jsonl = os.path.join(OUTPUT_DIR, "eedi_test_cases.jsonl")
    sample_md = os.path.join(SAMPLES_DIR, "eedi_sample_20.md")
    sample_json = os.path.join(SAMPLES_DIR, "eedi_sample_20.json")

    samples = []
    with gzip.open(EEDI_SRC, "rt", encoding="utf-8") as f_in, open(out_jsonl, "w", encoding="utf-8") as f_out:
        for idx, line in enumerate(f_in, start=1):
            raw = json.loads(line)
            
            formatted_messages = []
            for m in raw.get("messages", []):
                speaker_raw = m.get("speaker") or ""
                is_student = "student" in speaker_raw.lower()
                speaker = "Student" if is_student else "Human Tutor"
                talk_move = m.get("talk_move")
                if talk_move == "<None>":
                    talk_move = None
                    
                formatted_messages.append({
                    "sequence": m.get("sequence"),
                    "speaker": speaker,
                    "role": "user" if is_student else "assistant",
                    "text": (m.get("text") or "").strip(),
                    "pedagogical_talk_move": talk_move
                })

            clean_case = {
                "case_id": f"EEDI_{idx:04d}",
                "dataset": "Eedi",
                "domain": "Mathematics & Pedagogical Tutoring",
                "subject_area": raw.get("subject_name", "General Mathematics"),
                "question_id": raw.get("question_id"),
                "diagnostic_math_question": (raw.get("question_text") or "").strip(),
                "total_messages": len(formatted_messages),
                "student_message_count": raw.get("student_message_count", sum(1 for m in formatted_messages if m["role"] == "user")),
                "tutor_message_count": raw.get("tutor_message_count", sum(1 for m in formatted_messages if m["role"] == "assistant")),
                "original_intervention_id": raw.get("intervention_id"),
                "conversation": formatted_messages
            }
            
            f_out.write(json.dumps(clean_case, ensure_ascii=False) + "\n")
            if idx <= 20:
                samples.append(clean_case)

    # Write samples in JSON
    with open(sample_json, "w", encoding="utf-8") as f_sjson:
        json.dump(samples, f_sjson, indent=2, ensure_ascii=False)

    # Write samples in Markdown
    with open(sample_md, "w", encoding="utf-8") as f_smd:
        f_smd.write("# Eedi: Curated 20 Representative Test Cases for ChatGPT\n\n")
        f_smd.write("> **Dataset**: Eedi Question-Anchored Human Tutoring Interventions\n")
        f_smd.write("> **Domain**: K–12 & Diagnostic Mathematics, Misconception Diagnosis, Socratic Scaffolding\n\n---\n\n")
        for ec in samples:
            f_smd.write(f"## Test Case `{ec['case_id']}`: {ec['subject_area']}\n")
            f_smd.write(f"- **Question ID**: `{ec['question_id']}` | **Messages**: {ec['total_messages']} ({ec['student_message_count']} Student, {ec['tutor_message_count']} Tutor)\n")
            f_smd.write("### Diagnostic Question Given to Student:\n")
            f_smd.write(f"```text\n{ec['diagnostic_math_question']}\n```\n\n")
            f_smd.write("### Human Tutor Interventions Transcript:\n\n")
            for m in ec["conversation"]:
                move_tag = f" _(Pedagogical Move: {m['pedagogical_talk_move']})_" if m.get("pedagogical_talk_move") else ""
                f_smd.write(f"**[{m['speaker']} (Seq {m['sequence']})]{move_tag}**:\n{m['text']}\n\n")
            f_smd.write("---\n\n")

    print(f"Eedi complete. Exported {idx} cases.")

def export_goh_shard1():
    print("Processing Geometry of Harmfulness (GoH) Shard 1...")
    out_jsonl = os.path.join(OUTPUT_DIR, "goh_shard1_test_cases.jsonl")
    sample_md = os.path.join(SAMPLES_DIR, "goh_shard1_sample_20.md")
    sample_json = os.path.join(SAMPLES_DIR, "goh_shard1_sample_20.json")

    samples = []
    with gzip.open(GOH_SRC, "rt", encoding="utf-8") as f_in, open(out_jsonl, "w", encoding="utf-8") as f_out:
        for idx, line in enumerate(f_in, start=1):
            raw = json.loads(line)
            
            formatted_messages = []
            for m in raw.get("messages", []):
                speaker_raw = m.get("speaker") or ""
                role_raw = m.get("role") or ""
                is_attacker = "attacker" in speaker_raw.lower() or role_raw == "user"
                speaker = "Attacker" if is_attacker else "Target Model"
                
                formatted_messages.append({
                    "sequence": m.get("sequence"),
                    "turn": m.get("turn_idx"),
                    "speaker": speaker,
                    "role": "user" if is_attacker else "assistant",
                    "text": (m.get("text") or "").strip()
                })

            clean_case = {
                "case_id": f"GOH_SHARD1_{idx:05d}",
                "dataset": "Geometry of Harmfulness (Shard 1)",
                "domain": "Multi-Turn Adversarial Red-Teaming",
                "attack_framework": raw.get("attack_framework", "unspecified"),
                "goal_type": raw.get("goal_type", "harmful"),
                "red_team_objective": (raw.get("objective") or "").strip(),
                "target_model": raw.get("model_name"),
                "attack_successful": raw.get("framework_success", False),
                "total_turns": raw.get("executed_turns", len(formatted_messages)//2),
                "total_messages": len(formatted_messages),
                "original_trajectory_id": raw.get("trajectory_id"),
                "conversation": formatted_messages
            }
            
            f_out.write(json.dumps(clean_case, ensure_ascii=False) + "\n")
            if idx <= 20:
                samples.append(clean_case)

    # Write samples in JSON
    with open(sample_json, "w", encoding="utf-8") as f_sjson:
        json.dump(samples, f_sjson, indent=2, ensure_ascii=False)

    # Write samples in Markdown
    with open(sample_md, "w", encoding="utf-8") as f_smd:
        f_smd.write("# Geometry of Harmfulness (GoH Shard 1): Curated 20 Representative Test Cases for ChatGPT\n\n")
        f_smd.write("> **Dataset**: Geometry of Harmfulness in Multi-Turn Attacks (Shard 1)\n")
        f_smd.write("> **Domain**: Multi-Turn Adversarial Jailbreaks, ActorAttack, Crescendo Escalation, Roleplay\n\n---\n\n")
        for gc in samples:
            status_str = "BREACH / SUCCESS" if gc["attack_successful"] else "DEFENDED / REFUSED"
            f_smd.write(f"## Test Case `{gc['case_id']}`: {gc['attack_framework'].upper()} Attack\n")
            f_smd.write(f"- **Objective**: `{gc['red_team_objective']}`\n")
            f_smd.write(f"- **Goal Type**: `{gc['goal_type'].upper()}` | **Target Model**: `{gc['target_model']}` | **Attack Outcome**: `{status_str}`\n")
            f_smd.write(f"- **Trajectory Length**: {gc['total_turns']} turns ({gc['total_messages']} messages)\n\n")
            f_smd.write("### Multi-Turn Adversarial Dialogue Transcript:\n\n")
            for m in gc["conversation"]:
                f_smd.write(f"**[{m['speaker']} (Turn {m['turn']})]**:\n{m['text']}\n\n")
            f_smd.write("---\n\n")

    print(f"GoH Shard 1 complete. Exported {idx} cases.")

if __name__ == "__main__":
    export_studychat()
    export_eedi()
    export_goh_shard1()
    print("All datasets successfully exported to ChatGPT-ready format!")
