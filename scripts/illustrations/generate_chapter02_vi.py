#!/usr/bin/env python3
"""
Generate static illustrations for Vietnamese Chapter 02 lessons.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle, FancyArrowPatch, Rectangle, Wedge


SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SCRIPT_DIR.parent.parent / "img" / "chapter_img" / "chapter02"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

plt.style.use("seaborn-v0_8-bright")
COLORS = {
    "red": "#FF6B6B",
    "blue": "#4ECDC4",
    "sky": "#45B7D1",
    "orange": "#FFA07A",
    "green": "#98D8C8",
    "purple": "#8E7DBE",
    "gold": "#F4B942",
    "gray": "#E6E6E6",
    "dark": "#2F3E46",
}


def finish(fig, name):
    output_path = OUTPUT_DIR / name
    fig.savefig(output_path, dpi=160, bbox_inches="tight")
    print(f"Created: {output_path}")
    plt.close(fig)


def create_prime_chart():
    fig, ax = plt.subplots(figsize=(11, 5.8))
    ax.set_title("Prime Numbers up to 30", fontsize=18, fontweight="bold", pad=16)

    primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
    for idx, number in enumerate(range(1, 31)):
        row = idx // 6
        col = idx % 6
        x = 1.0 + col * 1.45
        y = 4.4 - row * 0.92
        face = COLORS["orange"] if number in primes else COLORS["gray"]
        ax.add_patch(Circle((x, y), 0.3, facecolor=face, edgecolor=COLORS["dark"], linewidth=1.8))
        ax.text(x, y, str(number), ha="center", va="center", fontsize=11, fontweight="bold")

    ax.text(4.8, 0.5, "Primes have exactly two factors.", ha="center", fontsize=12)
    ax.set_xlim(0.2, 9.4)
    ax.set_ylim(0.1, 5)
    ax.axis("off")
    finish(fig, "02_01_so_nguyen_to.png")


def create_gcf_lcm():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.8))
    fig.suptitle("GCF and LCM", fontsize=18, fontweight="bold", y=1.02)

    ax = axes[0]
    ax.set_title("GCF of 12 and 18", fontsize=14, fontweight="bold")
    left = Circle((1.9, 2.4), 1.4, facecolor=COLORS["sky"], edgecolor=COLORS["dark"], alpha=0.85, linewidth=2.2)
    right = Circle((3.3, 2.4), 1.4, facecolor=COLORS["green"], edgecolor=COLORS["dark"], alpha=0.85, linewidth=2.2)
    ax.add_patch(left)
    ax.add_patch(right)
    ax.text(1.1, 3.4, "4", fontsize=12, fontweight="bold")
    ax.text(1.2, 1.5, "12", fontsize=12, fontweight="bold")
    ax.text(2.45, 3.0, "2", fontsize=12, fontweight="bold")
    ax.text(2.45, 2.35, "3", fontsize=12, fontweight="bold")
    ax.text(2.45, 1.6, "6", fontsize=12, fontweight="bold")
    ax.text(3.9, 3.4, "9", fontsize=12, fontweight="bold")
    ax.text(4.0, 1.5, "18", fontsize=12, fontweight="bold")
    ax.axis("off")

    ax = axes[1]
    ax.set_title("LCM of 4 and 6", fontsize=14, fontweight="bold")
    rows = [[4, 8, 12, 16, 20], [6, 12, 18, 24, 30]]
    for y, row, color in zip([3.0, 1.8], rows, [COLORS["sky"], COLORS["green"]]):
        for idx, value in enumerate(row):
            face = COLORS["gold"] if value == 12 else color
            ax.add_patch(Rectangle((0.7 + idx * 0.9, y), 0.7, 0.55, facecolor=face, edgecolor=COLORS["dark"], linewidth=1.4))
            ax.text(1.05 + idx * 0.9, y + 0.28, str(value), ha="center", va="center", fontsize=11, fontweight="bold")
    ax.text(2.45, 0.85, "12 is the first shared multiple.", ha="center", fontsize=11)
    ax.axis("off")

    finish(fig, "02_02_ucln_bcnn.png")


def create_fast_multiplication():
    fig, ax = plt.subplots(figsize=(11, 5.8))
    ax.set_title("Quick Multiplication Patterns", fontsize=18, fontweight="bold", pad=16)

    x = np.arange(1, 6)
    values = 9 * x
    ax.bar(x - 0.15, values, width=0.3, color=COLORS["sky"], edgecolor=COLORS["dark"])
    ax.bar(x + 0.15, 11 * x, width=0.3, color=COLORS["orange"], edgecolor=COLORS["dark"])
    for idx, value in enumerate(values, start=1):
        ax.text(idx - 0.15, value + 1.2, str(value), ha="center", fontsize=10)
    for idx, value in enumerate(11 * x, start=1):
        ax.text(idx + 0.15, value + 1.2, str(value), ha="center", fontsize=10)
    ax.set_xticks(x)
    ax.set_xticklabels([f"x{n}" for n in x])
    ax.legend(["9 x n", "11 x n"], loc="upper left")
    ax.grid(axis="y", alpha=0.2)
    finish(fig, "02_03_nhan_nhanh.png")


def create_fast_division():
    fig, ax = plt.subplots(figsize=(11, 5.8))
    ax.set_title("Division with Equal Groups", fontsize=18, fontweight="bold", pad=16)

    total = 24
    groups = 4
    for idx in range(total):
        row = idx // 6
        col = idx % 6
        color = [COLORS["sky"], COLORS["green"], COLORS["orange"], COLORS["purple"]][(idx % groups)]
        ax.add_patch(Circle((1.2 + col * 1.1, 4.2 - row * 1.0), 0.18, facecolor=color, edgecolor=COLORS["dark"], linewidth=1))

    ax.text(5.5, 0.7, "24 divided into 4 equal groups gives 6 in each group.", ha="center", fontsize=12)
    ax.set_xlim(0.4, 7.4)
    ax.set_ylim(0.3, 5)
    ax.axis("off")
    finish(fig, "02_04_chia_nhanh.png")


def create_properties():
    fig, ax = plt.subplots(figsize=(11.5, 5.8))
    ax.set_title("Properties of Operations", fontsize=18, fontweight="bold", pad=16)

    cards = [
        (1.1, "3 + 5 = 5 + 3", COLORS["sky"]),
        (4.0, "2 x 7 = 7 x 2", COLORS["green"]),
        (6.9, "(1 + 2) + 4 = 1 + (2 + 4)", COLORS["orange"]),
        (1.1, "6 x (3 + 2) = 6 x 3 + 6 x 2", COLORS["purple"]),
    ]
    positions = [(1.1, 2.9), (4.0, 2.9), (6.9, 2.9), (2.7, 1.2)]
    for (x, text, color), (_, y) in zip(cards, positions):
        width = 3.0 if "6 x" not in text else 6.0
        ax.add_patch(Rectangle((x, y), width, 0.95, facecolor=color, edgecolor=COLORS["dark"], linewidth=2))
        ax.text(x + width / 2, y + 0.48, text, ha="center", va="center", fontsize=11, fontweight="bold", color="white")
    ax.set_xlim(0.4, 10.4)
    ax.set_ylim(0.5, 4.5)
    ax.axis("off")
    finish(fig, "02_05_tinh_chat.png")


def create_advanced_fractions():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.8))
    fig.suptitle("Advanced Fractions", fontsize=18, fontweight="bold", y=1.02)

    ax = axes[0]
    ax.set_title("Compare 3/4 and 5/8", fontsize=14, fontweight="bold")
    for parts, shaded, y, color, label in [(4, 3, 2.7, COLORS["sky"], "3/4"), (8, 5, 1.5, COLORS["orange"], "5/8")]:
        for idx in range(parts):
            face = color if idx < shaded else COLORS["gray"]
            ax.add_patch(Rectangle((0.8 + idx * (3.2 / parts), y), 3.0 / parts, 0.7, facecolor=face, edgecolor=COLORS["dark"], linewidth=1.2))
        ax.text(4.4, y + 0.35, label, fontsize=12, fontweight="bold", va="center")
    ax.axis("off")

    ax = axes[1]
    ax.set_title("1/2 + 1/3 = 5/6", fontsize=14, fontweight="bold")
    for idx in range(6):
        face = COLORS["green"] if idx < 5 else COLORS["gray"]
        ax.add_patch(Wedge((2.2, 2.2), 1.35, 60 * idx, 60 * (idx + 1), facecolor=face, edgecolor=COLORS["dark"], linewidth=1.3))
    ax.text(2.2, 0.5, "Common denominator helps combine parts.", ha="center", fontsize=11)
    ax.axis("off")

    finish(fig, "02_06_phan_so_nang_cao.png")


def create_decimals():
    fig, ax = plt.subplots(figsize=(11, 5.8))
    ax.set_title("Decimals on a Number Line", fontsize=18, fontweight="bold", pad=16)

    ax.plot([0, 10], [2.5, 2.5], color=COLORS["dark"], linewidth=2.5)
    for idx in range(11):
        ax.plot([idx, idx], [2.3, 2.7], color=COLORS["dark"], linewidth=1.5)
        ax.text(idx, 2.0, f"{idx/10:.1f}", ha="center", fontsize=10)
    for x, label, color in [(2.0, "0.2", COLORS["sky"]), (5.0, "0.5", COLORS["orange"]), (8.0, "0.8", COLORS["purple"])]:
        ax.scatter([x], [2.5], s=160, color=color, edgecolors=COLORS["dark"], linewidth=2, zorder=3)
        ax.text(x, 3.0, label, ha="center", fontsize=11, fontweight="bold")
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(1.4, 3.6)
    ax.axis("off")
    finish(fig, "02_07_so_thap_phan.png")


def create_percent():
    fig, ax = plt.subplots(figsize=(11, 5.8))
    ax.set_title("Percent Means Out of 100", fontsize=18, fontweight="bold", pad=16)

    cols = 10
    for idx in range(100):
        row = idx // cols
        col = idx % cols
        face = COLORS["gold"] if idx < 35 else COLORS["gray"]
        ax.add_patch(Rectangle((1 + col * 0.45, 4.2 - row * 0.35), 0.36, 0.26, facecolor=face, edgecolor="white", linewidth=0.5))
    ax.text(7.6, 2.5, "35%", fontsize=24, fontweight="bold", color=COLORS["dark"])
    ax.text(7.6, 1.9, "35 out of 100 squares are colored.", fontsize=11, ha="center")
    ax.set_xlim(0.5, 10.2)
    ax.set_ylim(0.6, 5)
    ax.axis("off")
    finish(fig, "02_08_ti_le_phan_tram.png")


def create_angles_lines():
    fig, axes = plt.subplots(2, 2, figsize=(11, 5.8))
    fig.suptitle("Cac loai goc co ban", fontsize=18, fontweight="bold", y=0.98)

    configs = [
        ("Goc nhon", 45, COLORS["blue"]),
        ("Goc vuong", 90, COLORS["sky"]),
        ("Goc tu", 120, COLORS["orange"]),
        ("Goc bet", 180, COLORS["gold"]),
    ]

    for ax, (label, degrees, color) in zip(axes.flatten(), configs):
        theta = np.deg2rad(degrees)
        ax.plot([0, 1], [0, 0], color=color, linewidth=4, solid_capstyle="round")
        ax.plot([0, np.cos(theta)], [0, np.sin(theta)], color=color, linewidth=4, solid_capstyle="round")
        ax.add_patch(Arc((0, 0), 0.72, 0.72, theta1=0, theta2=degrees, color=COLORS["red"], linewidth=2.5))
        ax.scatter([0], [0], s=40, color=COLORS["dark"], zorder=3)
        ax.text(0, 1.05, label, ha="center", va="bottom", fontsize=13, fontweight="bold")
        ax.text(0, -0.18, f"{degrees}\N{DEGREE SIGN}", ha="center", va="top", fontsize=12, color=COLORS["dark"])
        ax.set_xlim(-1.05, 1.1)
        ax.set_ylim(-0.35, 1.15)
        ax.set_aspect("equal")
        ax.axis("off")

    finish(fig, "02_09_goc_duong_thang.png")


def create_review():
    fig, ax = plt.subplots(figsize=(11.5, 5.8))
    ax.set_title("Chapter 2 Review", fontsize=18, fontweight="bold", pad=16)

    nodes = [
        (1.6, 3.6, "Prime", COLORS["orange"]),
        (3.8, 3.6, "GCF\nLCM", COLORS["green"]),
        (6.0, 3.6, "Decimals", COLORS["sky"]),
        (8.2, 3.6, "Percent", COLORS["gold"]),
        (5.0, 1.6, "Review", COLORS["purple"]),
    ]
    for x, y, label, color in nodes:
        ax.add_patch(Circle((x, y), 0.7, facecolor=color, edgecolor=COLORS["dark"], linewidth=2.3))
        ax.text(x, y, label, ha="center", va="center", fontsize=11, fontweight="bold")
    for x, y, _, _ in nodes[:-1]:
        ax.annotate("", (5.0, 1.6), (x, y - 0.78), arrowprops=dict(arrowstyle="->", lw=2))
    ax.text(5.0, 0.65, "Connect the big ideas and choose the right method.", ha="center", fontsize=12)
    ax.set_xlim(0.5, 10.0)
    ax.set_ylim(0.4, 4.6)
    ax.axis("off")
    finish(fig, "02_10_on_tap_kiem_tra.png")


if __name__ == "__main__":
    print("Generating Chapter 02 Vietnamese illustrations...")
    print("-" * 50)
    create_prime_chart()
    create_gcf_lcm()
    create_fast_multiplication()
    create_fast_division()
    create_properties()
    create_advanced_fractions()
    create_decimals()
    create_percent()
    create_angles_lines()
    create_review()
    print("-" * 50)
    print(f"All Chapter 02 Vietnamese illustrations saved to {OUTPUT_DIR}")
