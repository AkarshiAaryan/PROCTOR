# GuardSLM Handover Package (4,000 Sessions Target)

Welcome to the streamlined GuardSLM benchmark handover directory.

---

## 1. Quick File Index

| File | Purpose | Size / Records |
| :--- | :--- | :---: |
| [`HANDOVER_GUIDE.md`](file:///home/regenesis/Desktop/Web%20Dev/dataset-analysis/guardslm_handover/HANDOVER_GUIDE.md) | **Master Handover Document**: Step-by-step methodologies, source case extraction, GoH attack mappings, schemas, labels, and the 4,000-session division. | Full Guide |
| [`sessions_dataset.html`](file:///home/regenesis/Desktop/Web%20Dev/dataset-analysis/guardslm_handover/sessions_dataset.html) | **Visual Reference Viewer**: Interactive web viewer displaying all decision chips, badges, and CUA formatting. | 19 KB |
| [`guardslm_grounded_sessions_S001_S232.jsonl`](file:///home/regenesis/Desktop/Web%20Dev/dataset-analysis/guardslm_handover/guardslm_grounded_sessions_S001_S232.jsonl) | **Completed Baseline Corpus**: 232 sessions, 995 turns, 100% schema compliant. | 1.1 MB |
| [`studychat_cases.jsonl`](file:///home/regenesis/Desktop/Web%20Dev/dataset-analysis/guardslm_handover/studychat_cases.jsonl) | **StudyChat Source Pool**: Real university CS/ML assignment tutoring cases. | 2,214 cases (69 MB) |
| [`eedi_cases.jsonl`](file:///home/regenesis/Desktop/Web%20Dev/dataset-analysis/guardslm_handover/eedi_cases.jsonl) | **Eedi Source Pool**: Diagnostic mathematics misconception questions. | 1,971 cases (10 MB) |
| [`goh_shard1_cases.jsonl`](file:///home/regenesis/Desktop/Web%20Dev/dataset-analysis/guardslm_handover/goh_shard1_cases.jsonl) | **GoH Shard 1 Source Pool**: Multi-turn adversarial red-team trajectories. | 10,000 cases (185 MB) |
| [`validation_harness.py`](file:///home/regenesis/Desktop/Web%20Dev/dataset-analysis/guardslm_handover/validation_harness.py) | **Automated Validator**: Tests schema compliance, data types, and turn structures. | Executable CLI |
| [`template_runner.py`](file:///home/regenesis/Desktop/Web%20Dev/dataset-analysis/guardslm_handover/template_runner.py) | **Batch Runner Template**: Python script template for staging 8-session batches. | Executable Template |

---

## 2. 4,000 Sessions Benchmark Allocation (2,000 per Contributor)

- **Contributor 1**: Sessions `S-001` through `S-2000` (232 complete, 1,768 remaining; output to `guardslm_grounded_sessions_S233_S2000.jsonl`).
  - StudyChat pool: `0001`–`1100` (Next: `0420`).
  - Eedi pool: `0001`–`0950` (Next: `0268`).
  - GoH pool: `00001`–`05000`.
- **Contributor 2**: Sessions `S-2001` through `S-4000` (2,000 sessions; output to `guardslm_grounded_sessions_S2001_S4000.jsonl`).
  - StudyChat pool: `1101`–`2200` (Starts: `1101`).
  - Eedi pool: `0951`–`1900` (Starts: `0951`).
  - GoH pool: `05001`–`10000`.

---

## 3. Quick Verification Command

```bash
python3 guardslm_handover/validation_harness.py --input guardslm_handover/guardslm_grounded_sessions_S001_S232.jsonl
```
