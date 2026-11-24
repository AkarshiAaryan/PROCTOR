# GuardSLM: Open Research Questions
## Prioritized Empirical Gaps and Methodological Uncertainties (Phase 1.2)

---

## 1. Overview

With the elimination of unnecessary Moodle implementation complexities, this document catalogues only **substantive educational and safety research questions** that remain genuinely unresolved. These questions guide pre-generation pilot experiments and human expert reviews.

---

## 2. Research Questions by Area

### A. Academic Policy Validation & Configuration
1. **Empirical Distribution of Syllabus AI Policies**:
   - *Question*: What proportion of contemporary university computing and engineering courses enforce a strict *hints-only* AI policy versus a *balanced* or *open-assistance* policy?
   - *Resolution Path*: Survey syllabus AI policy statements across accredited university computer science departments (focusing on Indian institutions and global peers) to establish representative baseline policy weights.
2. **Post-Deadline Access Rights for Accommodation Students**:
   - *Question*: How should the Guard handle requests for reference solutions when an assignment deadline has passed for the majority of the class, but individual students with medical accommodations or late tokens retain active submission windows?
   - *Resolution Path*: Establish an explicit institutional convention in the benchmark guidelines: resource lifecycle state must be evaluated at the **individual user enrolment level**, not purely at the course level.

---

### B. Help-Level Calibration & Operational Boundaries
3. **Inter-Annotator Distinguishability of Intermediate Help Levels**:
   - *Question*: Can independent annotators reliably distinguish between Level 3 (Socratic Hints), Level 4 (Pseudocode Skeletons), and Level 5 (Partial Code Slices) with high agreement ($\kappa \ge 0.85$)?
   - *Resolution Path*: Run a 100-turn pilot annotation study measuring ordinal Krippendorff's alpha across intermediate levels to identify edge cases and refine annotation rubrics.
4. **Pedagogical Appropriateness of Algorithmic Skeletons**:
   - *Question*: Is providing an abstract algorithmic skeleton (Level 4) on an introductory assignment an acceptable pedagogical scaffold or an unauthorized shortcut?
   - *Resolution Path*: Convene an advisory panel of CS educators to establish course-level guidelines (e.g., Level 4 permitted in CS2/Data Structures, but restricted to Level 3 in CS1/Intro to Programming).

---

### C. Multi-Turn Trajectory Dynamics & Synthesis Ratios
5. **Multi-Turn Code Slicing Threshold ($S_{\text{ratio}}$)**:
   - *Question*: What is the empirical threshold of cumulative code extraction where legitimate modular student debugging transitions into policy-violating code assembly?
   - *Resolution Path*: Query StudyChat trajectories to measure the distribution of consecutive helper function requests during benign homework sessions, calibrating a formal $S_{\text{ratio}}$ baseline before Phase 2 generation.
6. **Auditor Label Boundary Calibration (`SUSPICIOUS` vs. `POLICY-VIOLATING`)**:
   - *Question*: At what point does repeated opportunistic probing warrant a definitive `POLICY-VIOLATING` sanction versus remaining classified as `SUSPICIOUS`?
   - *Resolution Path*: Establish formal trajectory evaluation criteria: deliberate multi-turn circumvention with successful extraction triggers `POLICY-VIOLATING`; persistent probing that fails or halts triggers `SUSPICIOUS`.

---

### D. Browser Accessibility Snapshot Engineering
7. **Snapshot Token Pruning vs. Context Window Feasibility**:
   - *Question*: Does serializing full Playwright accessibility trees overwhelm the context window and inference latency of Small Language Models (e.g., 4B–8B parameter SLMs)?
   - *Resolution Path*: Conduct a 50-turn pilot experiment comparing raw accessibility trees against normalized semantic trees to establish optimal token pruning strategies without discarding critical UI state (timers, banners, active fields).

---

### E. Dataset Composition, Coverage & Generalization
8. **Validation of the 50/20/30 Auditor Label Distribution and 60/15/25 Dataset Split**:
   - *Question*: Does a distribution of 50% Harmless, 20% Suspicious, and 30% Policy-Violating sessions across a 60% Train, 15% Validation, and 25% Test partition provide sufficient statistical power for rare policy edge cases (e.g., active exam proctoring escapes)?
   - *Resolution Path*: Analyze scenario coverage across the 16 policy families in a 100-session pilot dataset before scaling production.
9. **Out-of-Distribution Generalization Testing**:
   - *Question*: How can the benchmark evaluate whether a model has learned generalizable contextual reasoning rather than memorizing specific scenario templates?
   - *Resolution Path*: Design a held-out test partition consisting of novel combinations of roles, resource states, and course policies not present in the training set.

---

### F. Evaluation Metrics & Asymmetric Loss
10. **Asymmetric Penalty Function for Guard Decisions**:
    - *Question*: In benchmark scoring, how should GuardSLM weight False Blocks (refusing a legitimate, struggling student) versus False Allows (permitting cheating on an exam)?
    - *Resolution Path*: Define a formal dual metric reporting both **Integrity Enforcement Accuracy** (safety/compliance) and **Pedagogical Support Rate** (avoiding over-refusal of benign learners).
