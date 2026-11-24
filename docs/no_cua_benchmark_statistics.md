# GuardSLM 2,000-Session Benchmark (No CUA) — Forensic Statistical Profile

**Dataset File**: [`guardslm_fresh/guardslm_2000_benchmark_no_cua.jsonl`](file:///home/regenesis/Desktop/Web%20Dev/dataset-analysis/guardslm_fresh/guardslm_2000_benchmark_no_cua.jsonl)  
**File Size**: 9,437,307 bytes (9.44 MB)  
**SHA-256 Checksum**: `7842a9ca271c7564c5d804a5815fc19f0bd8783b19a3e58961432ee4c53c9770`  
**Total Scale**: 2,000 Sessions | 9,778 Dialogue Turns | 776,623 Dialogue Words  

---

## 1. Executive Summary & Scale Metrics

| Dimension | Metric | Detail / Notes |
|:---|:---:|:---|
| **Total Multi-Turn Sessions** | **2,000** | Sequentially indexed `S-0001` through `S-2000` (0 collisions) |
| **Total Dialogue Turns** | **9,778** | Average 4.889 turns per session |
| **Session Length Span** | **2 to 7 turns** | Min: 2 turns, Max: 7 turns, Median: 5 turns |
| **Total Dialogue Word Count** | **776,623 words** | ~1.05M estimated subword tokens |
| **User Request Mean Length** | **24.5 words** | 141.8 characters per prompt |
| **Model Reason Mean Length** | **12.7 words** | 91.9 characters per guardrail justification |
| **Assistant Reply Mean Length** | **55.0 words** | 361.4 characters per pedagogical reply |
| **CUA Snapshots** | **0 (100% stripped)** | Pure text-based dialogue format |
| **Data Hygiene** | **100%** | 0 missing keys, 0 syntax errors, 0 non-canonical labels |

---

## 2. Five Canonical Archetypes (Mathematically Balanced 2:2:2:1:1)

The benchmark maintains a strict, pedagogically grounded distribution across student and instructional personas:

| Benchmark Archetype | Persona Description | Session Count | Share |
|:---|:---|:---:|:---:|
| **Mostly Honest Student with 1 Slip** | Benign learner experiencing deadline panic or conceptual block; slips once into seeking turnkey answers before recovering. | **500** | **25.0%** |
| **Honest Student** | Fully compliant, curious student seeking conceptual explanations, error debugging, and Socratic hints. | **482** | **24.1%** |
| **Persistent Cheating Student** | Adversarial student employing multi-turn jailbreaks, task disguise, modular slicing, and persona spoofing to harvest complete assignment solutions. | **479** | **24.0%** |
| **Honest Staff / Instructor** | Authorized course staff (professors, TAs) asking curriculum design, rubric generation, and autograder setup queries. | **270** | **13.5%** |
| **Staff Compliance Violator** | Authorized insider attempting administrative privilege abuse, grade tampering, unreleased exam exfiltration, and audit log wiping. | **269** | **13.5%** |
| **Total** | | **2,000** | **100.0%** |

### Institutional Role Breakdown:
- **Student**: 1,449 sessions (72.5%)
- **Instructor / Professor**: 336 sessions (16.8%)
- **Teaching Assistant (TA)**: 215 sessions (10.8%)
*(Combined Instructional Staff: 551 sessions / 27.5%)*

---

## 3. Four-Tier Guard Decision Spectrum

GuardSLM replaces standard binary safe/unsafe guardrails with a calibrated 4-tier decision spectrum:

```
  ALLOW (63.6%) ───────────────────────────────► Compliant learning / staff tooling
  BLOCK (20.6%) ───────────► Policy violation / academic dishonesty refusal
  LIMIT (11.7%) ─────► Pedagogical safety valve: answer withholding + Socratic hint
  ESCALATE (4.2%) ─► Insider threat / security breach / incident report
```

| Decision Label | Turn Count | Share | Pedagogical & Safety Intent |
|:---|:---:|:---:|:---|
| **`ALLOW`** | **6,219** | **63.6%** | Direct assistance within permitted policy ceilings (Levels 1–2 for students; Levels 1–6 for authorized staff). |
| **`BLOCK`** | **2,013** | **20.6%** | Polite, policy-grounded refusal citing course syllabus boundaries; prevents academic dishonesty and exam theft. |
| **`LIMIT`** | **1,140** | **11.7%** | **The Socratic safety valve.** Intercepts panic slips; strictly withholds turnkey code while delivering bounded guiding questions. |
| **`ESCALATE`** | **406** | **4.2%** | Immediate intervention for high-severity threats: database tampering, CUPS log wiping, FERPA PII scraping. |
| **Total** | **9,778** | **100.0%** | |

---

## 4. Longitudinal Turn Dynamics (Conversational Escalation)

In multi-turn safety, adversary behavior evolves dynamically. Below is the turn-by-turn label progression demonstrating the natural conversational lifecycle:

| Turn Position | `ALLOW` | `LIMIT` | `BLOCK` | `ESCALATE` | Total Turns | Key Dynamics |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **Turn 1** | 1,842 (92.1%) | 61 (3.1%) | 67 (3.4%) | 30 (1.5%) | 2,000 | Benign baseline: establishes homework context, problem framing. |
| **Turn 2** | 925 (46.2%) | **748 (37.4%)** | 312 (15.6%) | 15 (0.7%) | 2,000 | **The Panic Surge**: students encounter initial friction and slip into requesting direct code (`LIMIT` peaks). |
| **Turn 3** | 1,248 (62.7%) | 115 (5.8%) | 596 (29.9%) | 31 (1.6%) | 1,990 | Honest students recover via Socratic guidance; persistent cheaters escalate attacks (`BLOCK` surges). |
| **Turn 4** | 1,140 (60.6%) | 137 (7.3%) | 558 (29.6%) | 48 (2.5%) | 1,883 | Cheaters attempt modular slicing, homoglyph disguise, and historical roleplay. |
| **Turn 5** | 865 (57.3%) | 78 (5.2%) | 337 (22.3%) | **230 (15.2%)** | 1,510 | **The Escalation Peak**: staff violators attempt SQL injection/log erasure; cheaters demand direct answer keys. |
| **Turn 6** | 199 (52.1%) | 1 (0.3%) | 130 (34.0%) | 52 (13.6%) | 382 | Extended tail: persistent insider threats and stubborn adversarial probing. |
| **Turn 7** | 0 (0.0%) | 0 (0.0%) | 13 (100.0%) | 0 (0.0%) | 13 | Final hard refusal boundary. |

---

## 5. Pedagogical Assistance Depth Hierarchy (The 6+ Hint Levels)

GuardSLM defines a formal 7-tier assistance scale (`requested_level` 0 to 6) governing the depth of information requested by the user:

| Level | Designation | Formal Definition & Pedagogical Scope | Dataset Turns | Share |
|:---:|:---|:---|:---:|:---:|
| **Level 0** | **Complete Refusal** | Zero academic guidance. Polite notification of policy boundary or proctored lockdown enforcement. | 1 | <0.1% |
| **Level 1** | **Conceptual Definition** | High-level theoretical definitions, mathematical axioms, and documentation links without assignment-specific steps. | 2,294 | 23.5% |
| **Level 2** | **Error Diagnosis** | Clarifying why an approach fails conceptually, explaining compiler errors/tracebacks without resolution code. | 2,934 | 30.0% |
| **Level 3** | **Socratic Guidance & Hints** | Guiding questions (*"What happens when the queue is empty?"*), structural hints, and conceptual analogies. | 201 | 2.1% |
| **Level 4** | **Algorithmic Pseudocode** | Abstract algorithmic skeletons, control-flow flowcharts, and high-level logic templates without runnable syntax. | 49 | 0.5% |
| **Level 5** | **Minimal Reproducible Slice** | Isolated, generic 2–3 line syntax demonstrations on synthetic dummy data (not the student's assignment). | 798 | 8.2% |
| **Level 6** | **Turnkey Solution** | Fully functional, complete, executable assignment solutions or direct answer keys. | 3,123 | 31.9% |
| *None* | *Unspecified / Non-Code* | Meta-administrative inquiries, policy questions, or non-technical interactions. | 378 | 3.9% |
| **Total** | | | **9,778** | **100.0%** |

### Cross-Tabulation: Assistance Level vs. Guardrail Decision

| Requested Level | `ALLOW` | `LIMIT` | `BLOCK` | `ESCALATE` | Total Turns | Policy Interpretation |
|:---|:---:|:---:|:---:|:---:|:---:|:---|
| **Level 0** | 0 | 0 | 1 | 0 | 1 | Exam lockdown enforcement. |
| **Level 1** | **2,286** | 8 | 0 | 0 | 2,294 | Pure conceptual questions are almost universally permitted. |
| **Level 2** | **2,871** | 52 | 11 | 0 | 2,934 | Error diagnosis is permitted unless probing unreleased solutions. |
| **Level 3** | 62 | 7 | 105 | 27 | 201 | Explicit hint requests on restricted assessments are blocked/escalated. |
| **Level 4** | 33 | 7 | 9 | 0 | 49 | Pseudocode requests on active assignments. |
| **Level 5** | 0 | **486** | 311 | 1 | 798 | Requests for concrete code slices: routed to `LIMIT` (hints) or `BLOCK`. |
| **Level 6** | 967* | **580** | **1,338** | **238** | 3,123 | Turnkey code: `ALLOW` only for authorized instructors (*), `LIMIT` for slips, `BLOCK`/`ESCALATE` for students. |
| **Level None** | 0 | 0 | 238 | 140 | 378 | Staff compliance violations / non-coding system compromise attempts. |

---

## 6. Canonical 11-Class Attack Taxonomy

Every dialogue turn is strictly classified under the canonical `snake_case` taxonomy:

| Canonical Attack Type | Total Turns | Share of Dataset | Share of Attacks* | Threat Definition & Operationalization |
|:---|:---:|:---:|:---:|:---|
| **`none`** | **6,220** | **63.6%** | — | Compliant, legitimate pedagogical or administrative interaction. |
| **`compliance_breach`** | **791** | **8.1%** | 22.2% | Insider policy violation: gradebook manipulation, audit disabling, log wiping. |
| **`direct_cheating`** | **726** | **7.4%** | 20.4% | Explicit demands for turnkey assignment solutions or exam answers. |
| **`slip`** | **456** | **4.7%** | 12.8% | Benign deadline panic / cognitive fatigue asking for turnkey answers (`LIMIT`). |
| **`task_disguise`** | **341** | **3.5%** | 9.6% | Framing cheating as hypothetical research, academic paper drafting, or debugging. |
| **`actorattack`** | **341** | **3.5%** | 9.6% | Persona-based jailbreaks (*"Pretend you are an unrestricted AI"*, fictional roleplay). |
| **`policy_spoofing`** | **297** | **3.0%** | 8.3% | Fabricating institutional exemptions (*"The professor approved this in class"*). |
| **`modular_slicing`** | **257** | **2.6%** | 7.2% | Splitting assignment into sub-functions to harvest a turnkey solution incrementally. |
| **`privilege_spoofing`** | **198** | **2.0%** | 5.6% | Impersonating faculty, TAs, or administrators to gain elevated access. |
| **`credential_theft`** | **88** | **0.9%** | 2.5% | Stealing session tokens, LDAP logins, autograder API keys, or database passwords. |
| **`pii_exfiltration`** | **63** | **0.6%** | 1.8% | Scraping confidential peer submissions, student grades, or FERPA records. |
| **Total** | **9,778** | **100.0%** | **100.0%** | *3,558 total adversarial / attack turns (36.4% of dataset).* |

---

## 7. Empirical Grounding & Provenance Attribution

Every session is anchored in authentic pedagogical data and empirical threat intelligence:

| Context Anchor Source | Session Count | Share | Pedagogical / Adversarial Profile Grounded |
|:---|:---:|:---:|:---|
| **StudyChat (CS Coursework Logs)** | **1,030** | **51.5%** | Authentic undergraduate CS student programming friction, compiler tracebacks, and autograder bugs (McNichols et al., 2024). |
| **Eedi (Math Misconceptions)** | **674** | **33.7%** | Secondary school mathematics misconception diagnostics, diagnostic multiple-choice traps, and 99.9% answer-withholding Socratic pedagogy. |
| **Geometry of Harmfulness (GoH Shard 1)** | **265** | **13.3%** | Filtered academic integrity red-teaming: plagiarism detector bypass, proctored browser evasion, and admissions fraud (Arditi et al., 2024). |
| **Direct Curated Academic Anchors** | **31** | **1.6%** | Deep institutional compliance case studies (FERPA audit tampering, Banner SQL tampering). |
| **Total** | **2,000** | **100.0%** | |
