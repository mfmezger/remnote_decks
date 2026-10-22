# /// script
# dependencies = ["matplotlib", "numpy"]
# ///
"""Generate the PNG images used by visual flashcards (run: uv run scripts/make_images.py)."""

from math import erf, sqrt
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch

OUT = Path(__file__).resolve().parent.parent / "pilot" / "images"
BLUE, ORANGE, GREY, GREEN, RED = "#2563eb", "#ea580c", "#6b7280", "#16a34a", "#dc2626"
plt.rcParams.update({"font.size": 13, "axes.spines.top": False, "axes.spines.right": False})


def save(fig, name):
    fig.savefig(OUT / name, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def roc_vs_pr():
    """Binormal scores (positives N(1.5, 1), negatives N(0, 1)) at 10 % prevalence."""
    phi = np.vectorize(lambda z: 0.5 * (1 + erf(z / sqrt(2))))
    t = np.linspace(-5, 7, 400)
    tpr, fpr = 1 - phi(t - 1.5), 1 - phi(t)
    prevalence = 0.10
    precision = prevalence * tpr / (prevalence * tpr + (1 - prevalence) * fpr)

    fig, (roc, pr) = plt.subplots(1, 2, figsize=(11, 4.8))
    roc.plot(fpr, tpr, color=BLUE, lw=2.5, label="model")
    roc.plot([0, 1], [0, 1], "--", color=GREY, lw=2, label="random (AUC = 0.5)")
    roc.set(xlabel="False positive rate", ylabel="True positive rate (recall)", title="ROC curve", xlim=(0, 1), ylim=(0, 1.02))
    pr.plot(tpr, precision, color=BLUE, lw=2.5, label="model")
    pr.axhline(prevalence, ls="--", color=GREY, lw=2, label="random = prevalence (0.10)")
    pr.set(xlabel="Recall", ylabel="Precision", title="Precision-recall curve", xlim=(0, 1), ylim=(0, 1.02))
    for ax in (roc, pr):
        ax.legend(loc="lower right" if ax is roc else "upper right", frameon=False)
    fig.suptitle("Same model, 10 % positives", y=1.02)
    save(fig, "roc-vs-pr-baseline.png")


def reliability_overconfident():
    """Reliability diagram of an overconfident model; no title, the card asks for the diagnosis."""
    conf = np.arange(0.55, 1.0, 0.1)
    acc = 0.5 + 0.55 * (conf - 0.5)
    fig, ax = plt.subplots(figsize=(5.5, 5.5))
    ax.bar(conf, acc, width=0.09, color=BLUE, alpha=0.85, label="observed accuracy per bin")
    ax.bar(conf, conf - acc, bottom=acc, width=0.09, color=RED, alpha=0.25, label="gap to confidence")
    ax.plot([0.5, 1], [0.5, 1], "--", color=GREY, lw=2, label="perfect calibration")
    ax.set(xlabel="Predicted confidence", ylabel="Observed accuracy", xlim=(0.5, 1), ylim=(0.5, 1))
    ax.legend(loc="upper left", frameon=False, fontsize=11)
    save(fig, "reliability-diagram.png")


def commit(ax, x, y, label, color):
    ax.add_patch(Circle((x, y), 0.32, color=color, zorder=3))
    ax.text(x, y, label, ha="center", va="center", color="white", fontsize=12, fontweight="bold", zorder=4)


def edge(ax, a, b):
    ax.plot([a[0], b[0]], [a[1], b[1]], color=GREY, lw=2.5, zorder=1)


def branch_label(ax, x, y, text, color):
    ax.text(x, y, text, ha="center", va="center", fontsize=11, color=color, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=color))


def merge_vs_rebase():
    fig, axes = plt.subplots(1, 3, figsize=(15, 3.8))
    titles = ["Before", "git switch main\ngit merge feature", "git switch feature\ngit rebase main"]
    for ax, title in zip(axes, titles):
        ax.set_xlim(-0.6, 5.6), ax.set_ylim(-0.4, 2.4), ax.set_aspect("equal"), ax.axis("off")
        ax.set_title(title, fontsize=13, family="monospace")

    main = [(0, 0), (1, 0), (2, 0)]
    feat = [(2, 1.4), (3, 1.4)]
    before, merged, rebased = axes

    for ax in (before, merged):
        for a, b in zip(main, main[1:]):
            edge(ax, a, b)
        edge(ax, main[1], feat[0]), edge(ax, feat[0], feat[1])
        for (x, y), name in zip(main, "ABC"):
            commit(ax, x, y, name, BLUE)
        for (x, y), name in zip(feat, "DE"):
            commit(ax, x, y, name, ORANGE)
    branch_label(before, 2, -0.5, "main", BLUE)
    branch_label(before, 3, 2.1, "feature", ORANGE)

    edge(merged, main[2], (4, 0)), edge(merged, feat[1], (4, 0))
    commit(merged, 4, 0, "M", GREEN)
    merged.text(4, -0.6, "merge commit\n(2 parents)", ha="center", va="top", fontsize=10, color=GREEN)
    branch_label(merged, 5, 0, "main", BLUE)
    branch_label(merged, 3, 2.1, "feature", ORANGE)

    chain = main + [(3, 0), (4, 0)]
    for a, b in zip(chain, chain[1:]):
        edge(rebased, a, b)
    for (x, y), name in zip(main, "ABC"):
        commit(rebased, x, y, name, BLUE)
    commit(rebased, 3, 0, "D'", ORANGE), commit(rebased, 4, 0, "E'", ORANGE)
    rebased.text(3.5, 0.7, "new commits,\nnew hashes", ha="center", fontsize=10, color=ORANGE)
    branch_label(rebased, 5, 0, "feature", ORANGE)
    branch_label(rebased, 2, -0.5, "main", BLUE)
    save(fig, "merge-vs-rebase.png")


def reset_modes():
    cols = ["Branch (HEAD)", "Index (staging)", "Working tree"]
    rows = [("--soft", [1, 0, 0]), ("--mixed\n(default)", [1, 1, 0]), ("--hard", [1, 1, 1])]
    fig, ax = plt.subplots(figsize=(9, 3.9))
    ax.set_xlim(0, 4), ax.set_ylim(0, 4), ax.axis("off")
    for j, name in enumerate(cols):
        ax.text(1.5 + j, 3.55, name, ha="center", va="center", fontweight="bold")
    for i, (mode, changed) in enumerate(rows):
        y = 2.6 - i
        ax.text(0.45, y, f"git reset\n{mode}", ha="center", va="center", family="monospace", fontsize=11)
        for j, c in enumerate(changed):
            color = ORANGE if c else GREEN
            ax.add_patch(FancyBboxPatch((1.08 + j, y - 0.38), 0.84, 0.76, boxstyle="round,pad=0.02", fc=color, alpha=0.18, ec=color, lw=1.5))
            ax.text(1.5 + j, y, "reset to\n<commit>" if c else "kept", ha="center", va="center", color=color, fontweight="bold", fontsize=11)
    ax.text(2.5, -0.05, "--hard resets tracked files only; untracked files stay.", ha="center", fontsize=10, color=GREY)
    save(fig, "git-reset-modes.png")


def attention_heads():
    variants = [("Multi-head (MHA)", 8), ("Grouped-query (GQA)", 2), ("Multi-query (MQA)", 1)]
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.2))
    for ax, (title, n_kv) in zip(axes, variants):
        ax.set_xlim(-0.5, 8), ax.set_ylim(-0.9, 3.2), ax.axis("off")
        ax.set_title(title, fontsize=14)
        q_x = [0.2 + i * 0.95 for i in range(8)]
        group = 8 // n_kv
        kv_x = [sum(q_x[k * group:(k + 1) * group]) / group for k in range(n_kv)]
        for i, x in enumerate(q_x):
            ax.plot([x, kv_x[i // group]], [2.1, 0.6], color=GREY, lw=1.2, zorder=1)
            ax.add_patch(FancyBboxPatch((x - 0.35, 2.1), 0.7, 0.6, boxstyle="round,pad=0.02", fc=BLUE, ec="none", zorder=2))
            ax.text(x, 2.4, f"Q{i + 1}", ha="center", va="center", color="white", fontsize=9, zorder=3)
        for k, x in enumerate(kv_x):
            ax.add_patch(FancyBboxPatch((x - 0.38, 0.0), 0.76, 0.6, boxstyle="round,pad=0.02", fc=ORANGE, ec="none", zorder=2))
            ax.text(x, 0.3, "K/V", ha="center", va="center", color="white", fontsize=9, fontweight="bold", zorder=3)
        ax.text(3.5, -0.55, f"{n_kv} K/V head{'s' if n_kv > 1 else ''} → KV cache {n_kv}/8 of MHA", ha="center", fontsize=12)
    save(fig, "mha-gqa-mqa.png")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    roc_vs_pr()
    reliability_overconfident()
    merge_vs_rebase()
    reset_modes()
    attention_heads()
    print(f"wrote {len(list(OUT.glob('*.png')))} images to {OUT}")
