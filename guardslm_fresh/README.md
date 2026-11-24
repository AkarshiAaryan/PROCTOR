# GuardSLM Fresh Workspace

Welcome to the clean, uncluttered workspace. All legacy pilots, template generators, and obsolete scratch files have been excluded. This directory contains **strictly the authentic source datasets** from **StudyChat**, **Eedi**, and **Geometry of Harmfulness (GoH Shard 1)**.

---

## 1. Directory Structure

```text
guardslm_fresh/
├── README.md                  # This guide
├── studychat_cases.jsonl       # 2,214 authentic undergraduate CS & programming conversations (66 MB)
├── eedi_cases.jsonl            # 1,971 authentic math Socratic tutoring dialogues (9.9 MB)
├── goh_shard1_cases.jsonl      # 10,000 authentic multi-turn red-team attack trajectories (177 MB)
│
├── samples/                   # Curated 20-sample packs for human reading or direct LLM copy-pasting
│   ├── studychat_sample_20.md # Formatted Markdown transcript of 20 CS dialogues
│   ├── studychat_sample_20.json
│   ├── eedi_sample_20.md      # Formatted Markdown transcript of 20 Socratic math dialogues
│   ├── eedi_sample_20.json
│   ├── goh_shard1_sample_20.md# Formatted Markdown transcript of 20 adversarial attack trajectories
│   └── goh_shard1_sample_20.json
│
└── raw_shards/                # Original gzipped source archives
    ├── studychat_conversations.jsonl.gz (17 MB)
    ├── eedi_interventions.jsonl.gz (1.4 MB)
    └── goh_trajectories_shard_01.jsonl.gz (56 MB)
```

---

## 2. Dataset Overview & Schema

Each `.jsonl` file contains one complete, self-contained record per line:

### A. StudyChat (`studychat_cases.jsonl` — 2,214 cases)
* **Domain**: Computer Science, Data Structures, Algorithms, Python, Debugging
* **Contents**:
  * `case_id`: e.g. `"STUDYCHAT_0001"`
  * `assignment_code`: Assignment identifier (e.g., `"a4"`)
  * `scenario_title`: Topic title (e.g., `"The R-squared score"`)
  * `conversation`: Full multi-turn student/assistant dialogue with authentic student code, errors, and questions.

### B. Eedi (`eedi_cases.jsonl` — 1,971 cases)
* **Domain**: K–12 & Diagnostic Mathematics, Misconception Diagnosis
* **Contents**:
  * `case_id`: e.g. `"EEDI_0001"`
  * `subject_area`: Math topic (e.g., `"Rounding to Decimal Places"`)
  * `diagnostic_math_question`: The actual math question given to the student
  * `conversation`: Human tutor Socratic interactions, probing questions, and tagged pedagogical moves (`<Getting Student to Relate>`, etc.).

### C. Geometry of Harmfulness (`goh_shard1_cases.jsonl` — 10,000 cases)
* **Domain**: Multi-Turn Adversarial Red-Teaming & Safety
* **Contents**:
  * `case_id`: e.g. `"GOH_SHARD1_00001"`
  * `attack_framework`: Strategy used (e.g., `"actorattack"`, `"crescendo"`)
  * `red_team_objective`: Attack goal
  * `target_model`: Target LLM tested
  * `conversation`: Turn-by-turn attacker prompts and model responses.

---

## 3. Grounded Tri-Source Synthesis for GuardSLM

When building organic benchmark dialogues from these files:
1. **Context Anchor**: Take a real academic problem from `studychat_cases.jsonl` (CS) or `eedi_cases.jsonl` (Math).
2. **Benign Track (Track A)**: Pair the problem with authentic Socratic pedagogy from Eedi (scaffolded questioning, no direct code dumps, diagnosed cognitive misconceptions).
3. **Harmful Track (Track B)**: Pair the same problem with an adversarial trajectory from GoH (ActorAttack persona roleplay, emergency escalation, obfuscated prompt injection).
