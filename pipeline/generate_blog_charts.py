#!/usr/bin/env python3
"""
generate_blog_charts.py
Generates publication-quality, aesthetically refined charts for:
  - Chart 2A: Model Scale vs. Accuracy on Matched Pairs (Qwen Scaling Curve)
  - Chart 2B: Diagnostic Error Pathology across Model Scales (Qwen Error Breakdown)
  - Chart 6: Pedagogical Assistance Hierarchy vs. Guard Decisions (9,778 Turns)
Outputs high-resolution PNGs (300 DPI) and SVGs in charts_output/.
"""

import os
os.environ['MPLCONFIGDIR'] = '/tmp/mpl_config'

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# Set style aesthetics
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Helvetica', 'Arial']
plt.rcParams['axes.edgecolor'] = '#cbd5e1'
plt.rcParams['axes.linewidth'] = 0.8
plt.rcParams['grid.color'] = '#e2e8f0'
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['grid.linewidth'] = 0.6

OUTPUT_DIR = "/home/regenesis/Desktop/Web Dev/dataset-analysis/charts_output"
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ==============================================================================
# CHART 2A: MODEL SCALE VS. MATCHED-PAIR ACCURACY (STANDALONE CURVE)
# ==============================================================================
def create_chart_2a():
    models = ['Qwen-0.5B', 'Qwen-1.5B', 'Qwen-3B', 'Qwen-7B']
    x = np.arange(len(models))

    pair_acc = [22.5, 37.5, 17.5, 72.5]
    total_acc = [52.5, 60.0, 41.2, 72.5]

    fig, ax = plt.subplots(figsize=(10.5, 6.2))
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#f8fafc')

    # Plot Curves
    ax.plot(x, total_acc, color='#0284c7', marker='s', markersize=8.5, linewidth=2.5, 
            label='Overall Total Accuracy (%)', linestyle='--')
    ax.plot(x, pair_acc, color='#4338ca', marker='o', markersize=9.5, linewidth=2.8, 
            label='Matched-Pair Accuracy (%)')

    # 80% Safety Deployment Threshold
    ax.axhline(80.0, color='#dc2626', linestyle=':', linewidth=2.0, 
               label='Safety Deployment Threshold (80%)')

    # Annotate Points on Curves
    # Qwen-0.5B
    ax.annotate("22.5%", (x[0], pair_acc[0]), textcoords="offset points", xytext=(0, -18), ha='center',
                fontsize=10.5, fontweight='bold', color='#4338ca')
    ax.annotate("52.5%", (x[0], total_acc[0]), textcoords="offset points", xytext=(0, 9), ha='center',
                fontsize=10, color='#0284c7', fontweight='600')

    # Qwen-1.5B
    ax.annotate("37.5%", (x[1], pair_acc[1]), textcoords="offset points", xytext=(0, -18), ha='center',
                fontsize=10.5, fontweight='bold', color='#4338ca')
    ax.annotate("60.0%", (x[1], total_acc[1]), textcoords="offset points", xytext=(0, 9), ha='center',
                fontsize=10, color='#0284c7', fontweight='600')

    # Qwen-3B
    ax.annotate("17.5%", (x[2], pair_acc[2]), textcoords="offset points", xytext=(0, -18), ha='center',
                fontsize=10.5, fontweight='bold', color='#b91c1c')
    ax.annotate("41.2%", (x[2], total_acc[2]), textcoords="offset points", xytext=(0, 9), ha='center',
                fontsize=10, color='#0284c7', fontweight='600')

    # Qwen-7B
    ax.annotate("72.5%\n(Pair & Total)", (x[3], 72.5), textcoords="offset points", xytext=(0, 10), ha='center',
                fontsize=10.5, fontweight='bold', color='#4338ca')

    # Permissive Leak Callout on Qwen-0.5B
    ax.annotate(
        "Permissive Collapse:\n26 False Allows\n(65% Cheating Leaked)",
        xy=(0, 22.5), xycoords='data',
        xytext=(0.42, 40), textcoords='data',
        fontsize=9.5, fontweight='bold', color='#b91c1c',
        arrowprops=dict(arrowstyle="->", color='#b91c1c', lw=1.6, connectionstyle="arc3,rad=-0.15"),
        bbox=dict(boxstyle="round,pad=0.4", fc="#fee2e2", ec="#f87171", lw=1.2)
    )

    # Anxiety Collapse Callout on Qwen-3B
    ax.annotate(
        "Anxiety Collapse:\nOver-blocking Surge\n(17.5% Pair Accuracy)",
        xy=(2, 17.5), xycoords='data',
        xytext=(1.4, 25), textcoords='data',
        fontsize=9.5, fontweight='bold', color='#b91c1c',
        arrowprops=dict(arrowstyle="->", color='#b91c1c', lw=1.6, connectionstyle="arc3,rad=0.15"),
        bbox=dict(boxstyle="round,pad=0.4", fc="#fee2e2", ec="#f87171", lw=1.2)
    )

    # Qwen-7B threshold miss callout
    ax.annotate(
        "Fails 80% safety gate;\n8 critical violations missed",
        xy=(3, 72.5), xycoords='data',
        xytext=(2.3, 58), textcoords='data',
        fontsize=9.5, color='#475569',
        arrowprops=dict(arrowstyle="->", color='#64748b', lw=1.4, connectionstyle="arc3,rad=-0.1"),
        bbox=dict(boxstyle="round,pad=0.35", fc="#f1f5f9", ec="#cbd5e1", lw=1)
    )

    ax.set_xticks(x)
    ax.set_xticklabels(models, fontsize=11.5, fontweight='600', color='#0f172a')
    ax.set_ylim(5, 95)
    ax.set_ylabel("Accuracy Score (%)", fontsize=11.5, fontweight='bold', color='#1e293b')
    ax.set_title("Zero-Shot Parameter Scaling vs. Benchmark Accuracy\n"
                 "Evaluating Qwen-0.5B to 7B across 40 Matched Pairs (80 Realistic LMS Scenarios)", 
                 fontsize=13.5, fontweight='bold', pad=15, color='#0f172a')
    ax.legend(loc='lower right', frameon=True, framealpha=0.95, facecolor='#ffffff', edgecolor='#cbd5e1', fontsize=10)
    ax.grid(True, alpha=0.5)

    plt.tight_layout()
    png_path = os.path.join(OUTPUT_DIR, "chart_2a_qwen_scaling_curve.png")
    svg_path = os.path.join(OUTPUT_DIR, "chart_2a_qwen_scaling_curve.svg")
    plt.savefig(png_path, dpi=300, bbox_inches='tight')
    plt.savefig(svg_path, bbox_inches='tight')
    plt.close()
    print(f"[✓] Created Chart 2A:\n    - {png_path}\n    - {svg_path}")


# ==============================================================================
# CHART 2B: DIAGNOSTIC ERROR PATHOLOGY ACROSS MODEL SCALES (STANDALONE BAR)
# ==============================================================================
def create_chart_2b():
    models = ['Qwen-0.5B', 'Qwen-1.5B', 'Qwen-3B', 'Qwen-7B']
    x = np.arange(len(models))

    false_allows = [26, 22, 8, 8]    # Out of 40 adversarial cases
    false_blocks = [12, 10, 29, 10]  # Out of 40 benign control cases

    fig, ax = plt.subplots(figsize=(10.5, 6.5))
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#f8fafc')

    width = 0.35
    b1 = ax.bar(x - width/2, false_allows, width, label='False Allows (Cheating Leaked / Unauthorized Permitted)', 
                color='#ef4444', edgecolor='#b91c1c', linewidth=0.8, alpha=0.9)
    b2 = ax.bar(x + width/2, false_blocks, width, label='False Blocks (Honest Blocked / Over-Refusal)', 
                color='#f59e0b', edgecolor='#d97706', linewidth=0.8, alpha=0.9)

    # Add count labels on top of bars
    for bar in b1:
        height = bar.get_height()
        ax.annotate(f"{int(height)}",
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 4), textcoords="offset points",
                    ha='center', va='bottom', fontsize=10, fontweight='bold', color='#b91c1c')

    for bar in b2:
        height = bar.get_height()
        ax.annotate(f"{int(height)}",
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 4), textcoords="offset points",
                    ha='center', va='bottom', fontsize=10, fontweight='bold', color='#b45309')

    # Flag 1: High False Allows in Qwen-0.5B
    ax.annotate(
        "26 False Allows!\nSevere Permissive Leak\n(65% Cheating Allowed)",
        xy=(0 - width/2, 26), xycoords='data',
        xytext=(0.35, 33), textcoords='data',
        fontsize=9.5, fontweight='bold', color='#b91c1c',
        arrowprops=dict(arrowstyle="->", color='#b91c1c', lw=1.6, connectionstyle="arc3,rad=-0.12"),
        ha='center',
        bbox=dict(boxstyle="round,pad=0.35", fc="#fee2e2", ec="#f87171", lw=1.2)
    )

    # Flag 2: High False Blocks in Qwen-3B
    ax.annotate(
        "29 False Blocks!\nOver-Blocking Crisis\n(Suffocating Honest Users)",
        xy=(2 + width/2, 29), xycoords='data',
        xytext=(2.25, 35), textcoords='data',
        fontsize=9.5, fontweight='bold', color='#b45309',
        arrowprops=dict(arrowstyle="->", color='#d97706', lw=1.6, connectionstyle="arc3,rad=0.12"),
        ha='center',
        bbox=dict(boxstyle="round,pad=0.35", fc="#fef3c7", ec="#f59e0b", lw=1.2)
    )

    ax.set_xticks(x)
    ax.set_xticklabels(models, fontsize=11.5, fontweight='600', color='#0f172a')
    ax.set_ylim(0, 44)
    ax.set_ylabel("Error Frequency (out of 40 cases per type)", fontsize=11.5, fontweight='bold', color='#1e293b')
    ax.set_title("False Allows vs False Blocks over Different Model Sizes", 
                 fontsize=14, fontweight='bold', pad=15, color='#0f172a')
    ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.18), ncol=2, frameon=True, 
              facecolor='#ffffff', edgecolor='#cbd5e1', fontsize=9.5)
    ax.grid(True, alpha=0.5, axis='y')

    plt.tight_layout()
    png_path = os.path.join(OUTPUT_DIR, "chart_2b_qwen_error_breakdown.png")
    svg_path = os.path.join(OUTPUT_DIR, "chart_2b_qwen_error_breakdown.svg")
    plt.savefig(png_path, dpi=300, bbox_inches='tight')
    plt.savefig(svg_path, bbox_inches='tight')
    plt.close()
    print(f"[✓] Created Chart 2B:\n    - {png_path}\n    - {svg_path}")


# ==============================================================================
# CHART 6: PEDAGOGICAL ASSISTANCE HIERARCHY VS. GUARD DECISIONS (9,778 TURNS)
# ==============================================================================
def create_chart_6():
    levels = [
        'Level 1: Conceptual Definition (N=2,294)',
        'Level 2: Error Diagnosis (N=2,934)',
        'Level 3: Socratic Hints (N=201)',
        'Level 4: Algorithmic Pseudocode (N=49)',
        'Level 5: Minimal Code Slice (N=798)',
        'Level 6: Turnkey Solution (N=3,123)',
        'Non-Code / Admin Inquiry (N=378)'
    ]
    levels = levels[::-1]

    # Proportions in %
    allow_pct = [0.0, 30.96, 0.0, 67.35, 30.85, 97.85, 99.65]
    limit_pct = [0.0, 18.57, 60.90, 14.29, 3.48, 1.77, 0.35]
    block_pct = [62.96, 42.84, 38.97, 18.37, 52.24, 0.37, 0.0]
    escalate_pct = [37.04, 7.62, 0.13, 0.0, 13.43, 0.0, 0.0]

    # Raw counts for labels
    allow_cnt = [0, 967, 0, 33, 62, 2871, 2286]
    limit_cnt = [0, 580, 486, 7, 7, 52, 8]
    block_cnt = [238, 1338, 311, 9, 105, 11, 0]
    escalate_cnt = [140, 238, 1, 0, 27, 0, 0]

    policy_notes = [
        "Infrastructure / Credential Theft Refusal",
        "Staff Tooling (Allow) vs. Student Cheating (Block/Limit)",
        "Socratic Safety Valve: Downgraded to hints",
        "Permitted: Abstract algorithmic logic skeletons",
        "Restricted: Socratic hints on graded exams",
        "Permitted: Compiler tracebacks & misconceptions",
        "Universal Allow: Theoretical definitions & documentation"
    ]

    y = np.arange(len(levels))
    fig, ax = plt.subplots(figsize=(15.5, 7.5))
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#f8fafc')

    # Color Palette
    c_allow = '#10b981'     # Emerald Green
    c_limit = '#f59e0b'     # Amber / Warm Gold
    c_block = '#ef4444'     # Crimson Red
    c_escalate = '#8b5cf6'  # Purple

    h = 0.58

    # Stacked bars
    b_allow = ax.barh(y, allow_pct, height=h, color=c_allow, edgecolor='#059669', linewidth=0.6, label='ALLOW (Safe / Permitted)')
    b_limit = ax.barh(y, limit_pct, height=h, left=allow_pct, color=c_limit, edgecolor='#d97706', linewidth=0.6, label='LIMIT (Socratic Scaffolding / Hints)')
    left_block = np.array(allow_pct) + np.array(limit_pct)
    b_block = ax.barh(y, block_pct, height=h, left=left_block, color=c_block, edgecolor='#b91c1c', linewidth=0.6, label='BLOCK (Policy Violation Refusal)')
    left_esc = left_block + np.array(block_pct)
    b_esc = ax.barh(y, escalate_pct, height=h, left=left_esc, color=c_escalate, edgecolor='#6d28d9', linewidth=0.6, label='ESCALATE (Security / Insider Threat)')

    # Segment labels inside bars
    for i in range(len(levels)):
        if allow_pct[i] >= 6.0:
            ax.text(allow_pct[i] / 2, y[i], f"{allow_pct[i]:.0f}%\n({allow_cnt[i]:,})", 
                    ha='center', va='center', color='#ffffff', fontsize=8.5, fontweight='bold')
        if limit_pct[i] >= 6.0:
            ax.text(allow_pct[i] + limit_pct[i] / 2, y[i], f"{limit_pct[i]:.0f}%\n({limit_cnt[i]:,})", 
                    ha='center', va='center', color='#ffffff', fontsize=8.5, fontweight='bold')
        if block_pct[i] >= 6.0:
            ax.text(left_block[i] + block_pct[i] / 2, y[i], f"{block_pct[i]:.0f}%\n({block_cnt[i]:,})", 
                    ha='center', va='center', color='#ffffff', fontsize=8.5, fontweight='bold')
        if escalate_pct[i] >= 6.0:
            ax.text(left_esc[i] + escalate_pct[i] / 2, y[i], f"{escalate_pct[i]:.0f}%\n({escalate_cnt[i]:,})", 
                    ha='center', va='center', color='#ffffff', fontsize=8.5, fontweight='bold')

        ax.text(101.5, y[i], f"• {policy_notes[i]}", va='center', ha='left', 
                fontsize=9.2, color='#334155', style='italic')

    ax.set_yticks(y)
    ax.set_yticklabels(levels, fontsize=10.5, fontweight='600', color='#0f172a')
    ax.set_xlim(0, 100)
    ax.xaxis.set_major_formatter(ticker.PercentFormatter())
    ax.set_xlabel("Proportion of Turn Decisions (%)", fontsize=11, fontweight='bold', color='#1e293b', labelpad=8)
    ax.set_title("Pedagogical Assistance Hierarchy vs. Guard Decisions (9,778 Sequential Turns)\n"
                 "Calibrating educational safety from theoretical concepts (Level 1) to turnkey code (Level 6)",
                 fontsize=13.5, fontweight='bold', color='#0f172a', pad=18)

    ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.16), ncol=4, frameon=True, 
              facecolor='#ffffff', edgecolor='#cbd5e1', fontsize=9.5)
    ax.grid(True, alpha=0.4, axis='x')

    plt.tight_layout()
    png_path = os.path.join(OUTPUT_DIR, "chart_6_assistance_hierarchy_decisions.png")
    svg_path = os.path.join(OUTPUT_DIR, "chart_6_assistance_hierarchy_decisions.svg")
    plt.savefig(png_path, dpi=300, bbox_inches='tight')
    plt.savefig(svg_path, bbox_inches='tight')
    plt.close()
    print(f"[✓] Created Chart 6:\n    - {png_path}\n    - {svg_path}")


if __name__ == '__main__':
    print("Generating separated Matplotlib charts...")
    create_chart_2a()
    create_chart_2b()
    create_chart_6()
    print("All charts generated successfully!")
