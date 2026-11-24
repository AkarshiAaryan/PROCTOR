# GuardSLM: Simplified Role, Authorization and Academic AI Policy Architecture (v2)

**Document ID**: `GUARD-ROLE-POLICY-ARCH-02`  
**Status**: Authoritative Architectural Standard  
**Date**: November 2026  

---

## 1. Executive Summary

This specification codifies the platform-independent LMS authorization and policy model for GuardSLM. It replaces all database-specific complexities with clean, server-verified contextual dimensions:
- **Four Authenticated Roles**: Student, Teaching Assistant, Instructor, Administrator.
- **Seven Core Context Fields**: `authenticated_role`, `resource_type`, `resource_relationship`, `resource_state`, `effective_permissions`, `assessment_state`, `course_policy_profile`.
- **Sixteen Canonical Policy Cards**: Actionable decision rules with explicit guard actions (`ALLOW`, `LIMIT`, `BLOCK`, `ESCALATE`).
- **Seven Assistance Levels (0–6)**: Grounded in pedagogical scaffolding.
- **Strict Policy Precedence**: Fixed 6-stage decision order ensuring access and security constraints take absolute precedence over pedagogical assistance profiles.

---

## 2. Policy Precedence & Fixed Decision Order

When evaluating a user prompt, the Turn Guard and Session Auditor execute a fixed 6-stage precedence hierarchy:

```
[Incoming User Prompt + Context]
  │
  ├─► Stage 1: Authenticated Role & Effective Permissions Verification
  │     └─ Reject unverified privilege claims; enforce server token (POL_AUTH_001, POL_ROLE_003).
  │
  ├─► Stage 2: Resource Relationship & Lifecycle State Check
  │     └─ Verify ownership (POL_OWN_004) and lifecycle state (draft/active/released).
  │
  ├─► Stage 3: Assessment Restrictions & Lockdown Checks
  │     └─ If assessment_state == 'active', enforce Level 0 lockdown (POL_EXAM_008, POL_KEYS_009).
  │
  ├─► Stage 4: Institutional & Curricular Policy Checks
  │     └─ Prohibit test extraction (POL_SEC_007) and cumulative code assembly (POL_SOL_006).
  │
  ├─► Stage 5: Course Assistance Ceiling Enforcement
  │     └─ Cap pedagogical help at course ceiling (Strict Socratic: 3, Balanced: 4, Open: 5) (POL_CEIL_005).
  │
  └─► Stage 6: Appropriate Pedagogical Delivery
        └─ Deliver allowed response adhering to Eedi scaffolding grammar without exceeding ceiling.
```

> [!IMPORTANT]
> A course assistance profile (`OPEN_ASSISTED`) can **never** override Stage 1 access restrictions, Stage 2 privacy boundaries, or Stage 3 active-exam lockdowns.

---

## 3. Help Level Taxonomy (Levels 0–6)

| Level | Classification | Educational Definition | Allowed in Strict Socratic | Allowed in Balanced | Allowed in Open Assisted |
|:---:|:---|:---|:---:|:---:|:---:|
| **0** | No Academic Assistance | Refusal or purely technical/platform instructions | Yes | Yes | Yes |
| **1** | Conceptual Explanation | High-level theoretical definitions, formulas, or principles | Yes | Yes | Yes |
| **2** | Diagnostic Guidance | Identifying error lines or misconceptions without fix | Yes | Yes | Yes |
| **3** | Hints & Guided Questions| Socratic questions, hints, and subgoal decomposition | **Yes (Ceiling)** | Yes | Yes |
| **4** | Algorithmic Pseudocode | Structured pseudocode or step-by-step logic outlines | No | **Yes (Ceiling)** | Yes |
| **5** | Isolated Code Snippets | Small syntax examples or isolated function lines | No | No | **Yes (Ceiling)** |
| **6** | Full Implementation | Complete drop-in code solution or end-to-end essay | No | No | No (Post-deadline only) |
