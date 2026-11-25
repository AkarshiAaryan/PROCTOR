# Datawrapper CSV Exports for PROCTOR / GuardSLM

This directory contains pre-formatted, production-ready CSV files specifically engineered for direct upload into [Datawrapper](https://www.datawrapper.de/).

---

## Quick Reference & Chart Type Guide

| File | Recommended Datawrapper Chart Type | Key Visual Configuration in Datawrapper |
| :--- | :--- | :--- |
| [`01_pilot_guard_models_comparison.csv`](./01_pilot_guard_models_comparison.csv) | **Grouped Column Chart** | Add a horizontal reference line at `80.0%` labeled *"Deployment Threshold"*. Red for caught, Blue for allowed. |
| [`02_qwen_scaling_and_pair_accuracy.csv`](./02_qwen_scaling_and_pair_accuracy.csv) | **Line Chart / Grouped Column** | X-axis: `Model` or `Parameters (B)`. Add horizontal line at `80%`. Add text annotation at Qwen-3B ("Over-blocking collapse"). |
| [`02b_qwen_error_type_breakdown.csv`](./02b_qwen_error_type_breakdown.csv) | **Split / Grouped Bars** | Compares `False Allows` vs `False Blocks` across model sizes. |
| [`03_decision_spectrum_distribution.csv`](./03_decision_spectrum_distribution.csv) | **Donut Chart** | Select `Decision` as slice label and `Turns` or `Share (%)` as value. Colors: Green (`#10b981`), Red (`#ef4444`), Amber (`#f59e0b`), Purple (`#a855f7`). |
| [`04_longitudinal_turn_dynamics_percentages.csv`](./04_longitudinal_turn_dynamics_percentages.csv) | **100% Stacked Area Chart / Stacked Column** | X-axis: `Turn`. Shows dynamic surge of LIMIT at Turn 2 and ESCALATE at Turn 5. |
| [`04b_longitudinal_turn_dynamics_counts.csv`](./04b_longitudinal_turn_dynamics_counts.csv) | **Stacked Column Chart** | Shows exact volume breakdown per turn. |
| [`05_user_archetypes_distribution.csv`](./05_user_archetypes_distribution.csv) | **Grouped Bar Chart** | Compare `Target Share (%)` against `Actual Share (%)` side-by-side. |
| [`06_assistance_levels_vs_decisions.csv`](./06_assistance_levels_vs_decisions.csv) | **Stacked Bar Chart (Horizontal)** | Y-axis: `Assistance Level`. Stack: `ALLOW`, `LIMIT`, `BLOCK`, `ESCALATE`. |
| [`07_attack_taxonomy_distribution.csv`](./07_attack_taxonomy_distribution.csv) | **Bar Chart (Horizontal)** | Sort descending by `Adversarial Turns`. Inline percentage labels enabled. |
| [`08_source_grounding_breakdown.csv`](./08_source_grounding_breakdown.csv) | **Donut / Bar Chart** | Breakdown of StudyChat, Eedi, GoH, and Curated Anchors. |

---

## How to use in Datawrapper:
1. Go to [Datawrapper.de](https://www.datawrapper.de/) and click **"Create New Chart"**.
2. Under **Step 1: Upload Data**, click **"Upload CSV"** and choose one of the files from this directory, or simply copy-paste the CSV text.
3. Under **Step 2: Check & Describe**, make sure the headers look correct.
4. Under **Step 3: Visualize**, choose the recommended chart type listed in the table above and customize colors/annotations.
5. Under **Step 4: Publish & Embed**, export as high-res PNG/SVG or copy the interactive embed code for your blog.
