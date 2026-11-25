# PROCTOR: Policy & Role Oversight for Classroom Tutoring Operations & Risks

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Benchmark Size](https://img.shields.io/badge/Benchmark-2%2C000%20Sessions%20%2F%209%2C778%20Turns-blue.svg)](#1-benchmark-overview)
[![Validation](https://img.shields.io/badge/Validation-100%25%20Canonical%20Compliance-brightgreen.svg)](#3-automated-quality-assurance)

This repository contains the official dataset releases, grounding taxonomies, generation protocols, and automated validation suite for **PROCTOR** (Policy & Role Oversight for Classroom Tutoring Operations & Risks) — a 2,000-session (9,778 dialogue turns) benchmark evaluating contextual safety gatekeeping in educational platforms.

---

## 1. Benchmark Overview

GuardSLM evaluates safety guards across **longitudinal multi-turn interactions** where users interact with AI assistants inside learning management systems (LMS). Unlike single-turn toxic prompt benchmarks, GuardSLM benchmarks:
1. **Role-Based Access Control (RBAC)**: Distinguishing authorized staff (Professors, TAs) from unauthorized student access.
2. **Pedagogical Integrity**: Guarding academic honesty (e.g. preventing direct assignment solutions while permitting Socratic hints).
3. **Multi-Turn Drift**: Catching benign interactions that drift into policy breaches in Turns 2 through 5.

### Official Dataset Releases (`guardslm_fresh/`)

| Dataset File | Volume | Turns | Description |
| :--- | :---: | :---: | :--- |
| [`guardslm_2000_benchmark_no_cua.jsonl`](guardslm_fresh/guardslm_2000_benchmark_no_cua.jsonl) | **2,000 Sessions** | **9,778 Turns** | **Pure Textual Multi-Turn Benchmark** without DOM/UI snapshots. Evaluation is based on structured institutional role metadata, active course policies, and multi-turn student/instructor dialogue. |
| [`guardslm_2000_benchmark_with_cua.jsonl`](guardslm_fresh/guardslm_2000_benchmark_with_cua.jsonl) | **2,000 Sessions** | **9,778 Turns** | **Multimodal / Context-Grounded Benchmark** with full Computer-Using Agent (`cua_snapshot`) DOM, URL, and viewport state telemetry at every turn. |

---

## 2. Empirical Benchmark Metrics (9,778 Turns)

```
  Decision Distribution across 9,778 Sequential Dialogue Turns:
  +--------------------------------------------------------------+
  |  ALLOW      : 6,219 turns (63.6%) [Benign academic inquiry]  |
  |  BLOCK      : 2,013 turns (20.6%) [Direct policy violations] |
  |  LIMIT      : 1,140 turns (11.7%) [Socratic intervention]    |
  |  ESCALATE   :   406 turns ( 4.2%) [Persistent breaches]      |
  +--------------------------------------------------------------+
```

### Longitudinal Turn Dynamics (Why Single-Turn Fails)
* **Turn 1 (Safe Baseline)**: **92.1% ALLOW**. Both honest students and cheaters start with harmless requests.
* **Turn 2 (The Slip Point)**: **37.4% LIMIT**. Students introduce unauthorized scopes or ask for direct exam/assignment answers. 70.3% of all student slips happen here.
* **Turn 3–4 (Drift & Probing)**: 29.7% of policy slips occur in turns 3 or 4 after initial safe exchanges.
* **Turn 5 (Escalation Peak)**: **15.2% ESCALATE**. Persistent adversarial actors repeatedly reject limits, triggering human staff escalation.

### User Archetypes (Target 2:2:2:1:1 Distribution)
* **Mostly Honest Slips**: 500 sessions (25.0%)
* **Honest Students**: 482 sessions (24.1%)
* **Persistent Cheaters**: 479 sessions (24.0%)
* **Honest Staff**: 270 sessions (13.5%)
* **Staff Compliance Violators**: 269 sessions (13.5%)

Instructional roles (Professors, Instructors, TAs) account for **551 sessions (27.5%)** and **2,617 turns**.

---

## 3. Tri-Source Grounding Architecture

GuardSLM synthesizes authentic interactions by grounding each session into three distinct datasets:
1. **StudyChat**: Supplies authentic undergraduate computer science and programming problem contexts.
2. **Eedi**: Supplies authentic pedagogical Socratic tutoring methodologies, misconception remediation, and diagnostic questions.
3. **Geometry of Harmfulness (GoH)**: Supplies multi-turn adversarial red-teaming trajectories (Crescendo attacks, roleplay deceptions, and persistence).

Curated 20-case samples illustrating source grounding are available in [`guardslm_fresh/samples/`](guardslm_fresh/samples/).

---

## 4. Repository Structure

```
guardslm-benchmark/
├── guardslm_fresh/
│   ├── guardslm_2000_benchmark_no_cua.jsonl   # 2,000 session canonical text benchmark
│   ├── guardslm_2000_benchmark_with_cua.jsonl # 2,000 session CUA-grounded benchmark
│   ├── sessions_test.jsonl                    # Contributor 1 standardized sessions (1,000 sessions)
│   ├── merged.jsonl                           # Contributor 2 standardized sessions (1,000 sessions)
│   └── samples/                               # 20-case ground-truth samples (Eedi, StudyChat, GoH)
├── governance/
│   ├── role_policy_architecture.md            # Institutional RBAC specification
│   ├── SESSION_GENERATION_RULES.json          # Mathematical progression and turn grammar
│   └── SOURCE_PATTERN_LIBRARY.json            # Grounded educational & adversarial pattern library
├── guardslm_handover/
│   ├── validation_harness.py                  # Strict automated 13-gate QA validation test suite
│   └── HANDOVER_GUIDE.md                      # Operational execution protocol
├── scripts/
│   ├── goh_academic_sampler.py                # Academic multi-turn adversarial sampler
│   ├── export_source_datasets.py              # Upstream source extraction tooling
│   └── build_batch_01.py                      # Batch generation harness
├── docs/
│   ├── guardslm_2000_benchmark_report.html    # Standalone interactive statistical dashboard
│   ├── no_cua_benchmark_statistics.md         # Detailed markdown profiling report
│   ├── academic_ai_policy_cards.md            # Canonical policy definitions
│   └── roles_permissions_resources.md         # Role-permission matrices
├── reports/                                   # Audit logs and traceability reports
└── README.md
```

---

## 5. Automated Quality Assurance

The benchmark is verified using [`guardslm_handover/validation_harness.py`](guardslm_handover/validation_harness.py), which enforces 13 strict schema, label, and progression gates:

```bash
# Run validation on the 2,000-session benchmark
python3 guardslm_handover/validation_harness.py guardslm_fresh/guardslm_2000_benchmark_no_cua.jsonl
```

**Validation Result**:
* Sessions Verified: **2,000 / 2,000 (100.0%)**
* Non-Canonical Decisions: **0** (Only `ALLOW`, `BLOCK`, `LIMIT`, `ESCALATE`)
* Broken References / Schema Errors: **0**

---

## 6. Interactive Visual Report

A self-contained HTML dashboard with charts and distribution tables is located at:
[`docs/guardslm_2000_benchmark_report.html`](docs/guardslm_2000_benchmark_report.html).
Open it in any web browser to view interactive visual distributions of user archetypes, longitudinal decision heatmaps, and role breakdowns.

---

## 7. Citation & Academic Reference

```bibtex
@misc{guardslm_benchmark_2026,
  author = {Aaryan, Akarshi},
  title = {GuardSLM: Contextual Safety Gatekeeping Benchmark for University Learning Platforms},
  year = {2026},
  publisher = {GitHub},
  howpublished = {\url{https://github.com/AkarshiAaryan/guardslm-benchmark}}
}
```

---

## 8. License
This project is licensed under the [MIT License](LICENSE).
