#!/usr/bin/env python3
"""
Generate static illustrations for Chapter 05 lessons.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle, Wedge


SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SCRIPT_DIR.parent.parent / "img" / "chapter_img" / "chapter05"
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


def create_square_numbers():
    fig, ax = plt.subplots(figsize=(11, 5.8))
    ax.set_title("Square Numbers", fontsize=18, fontweight="bold", pad=16)

    sizes = [1, 2, 3, 4]
    colors = [COLORS["sky"], COLORS["green"], COLORS["gold"], COLORS["orange"]]
    x_offset = 0.6

    for size, color in zip(sizes, colors):
        for row in range(size):
            for col in range(size):
                ax.add_patch(Circle((x_offset + col * 0.35, 3.9 - row * 0.35), 0.12, facecolor=color, edgecolor=COLORS["dark"], linewidth=1.2))
        ax.text(x_offset + (size - 1) * 0.18, 4.45, f"{size} x {size}", ha="center", fontsize=11, fontweight="bold")
        ax.text(x_offset + (size - 1) * 0.18, 2.2, f"{size * size}", ha="center", fontsize=12)
        x_offset += size * 0.45 + 1.0

    ax.text(5.5, 0.9, "1, 4, 9, 16 ... each square number makes a perfect square.", ha="center", fontsize=12)
    ax.set_xlim(0, 11)
    ax.set_ylim(0.4, 5)
    ax.axis("off")
    finish(fig, "01_square_numbers.png")


def create_factors_multiples():
    fig, ax = plt.subplots(figsize=(11.5, 5.8))
    ax.set_title("Factors and Multiples", fontsize=18, fontweight="bold", pad=16)

    center = Circle((3.0, 2.8), 0.7, facecolor=COLORS["gold"], edgecolor=COLORS["dark"], linewidth=2.5)
    ax.add_patch(center)
    ax.text(3.0, 2.8, "12", ha="center", va="center", fontsize=18, fontweight="bold")

    factor_points = [(1.1, 4.0, "1"), (1.2, 1.6, "2"), (3.0, 4.4, "3"), (4.8, 4.0, "4"), (4.8, 1.6, "6"), (3.0, 1.0, "12")]
    for x, y, label in factor_points:
        ax.add_patch(Circle((x, y), 0.45, facecolor=COLORS["sky"], edgecolor=COLORS["dark"], linewidth=2))
        ax.text(x, y, label, ha="center", va="center", fontsize=12, fontweight="bold")
        ax.plot([3.0, x], [2.8, y], color=COLORS["dark"], linewidth=1.7)

    start_x = 6.5
    for idx, value in enumerate([3, 6, 9, 12, 15, 18]):
        x = start_x + idx * 0.75
        ax.add_patch(Rectangle((x, 2.15), 0.58, 1.15, facecolor=COLORS["green"], edgecolor=COLORS["dark"], linewidth=1.7))
        ax.text(x + 0.29, 2.73, str(value), ha="center", va="center", fontsize=11, fontweight="bold")

    ax.text(3.0, 0.4, "Factors of 12", ha="center", fontsize=12, fontweight="bold")
    ax.text(8.7, 0.4, "Multiples of 3", ha="center", fontsize=12, fontweight="bold")
    ax.set_xlim(0, 11.5)
    ax.set_ylim(0.1, 5)
    ax.axis("off")
    finish(fig, "02_factors_multiples.png")


def create_prime_numbers():
    fig, ax = plt.subplots(figsize=(11, 5.8))
    ax.set_title("Prime Numbers", fontsize=18, fontweight="bold", pad=16)

    numbers = list(range(1, 21))
    prime_set = {2, 3, 5, 7, 11, 13, 17, 19}
    for idx, number in enumerate(numbers):
        row = idx // 5
        col = idx % 5
        x = 1.0 + col * 1.9
        y = 4.3 - row * 1.0
        face = COLORS["orange"] if number in prime_set else COLORS["gray"]
        ax.add_patch(Circle((x, y), 0.36, facecolor=face, edgecolor=COLORS["dark"], linewidth=2))
        ax.text(x, y, str(number), ha="center", va="center", fontsize=12, fontweight="bold")

    ax.text(5.4, 0.65, "Prime numbers have exactly two factors: 1 and the number itself.", ha="center", fontsize=12)
    ax.text(5.4, 0.25, "The orange numbers are 2, 3, 5, 7, 11, 13, 17, 19.", ha="center", fontsize=11)
    ax.set_xlim(0, 10.8)
    ax.set_ylim(0, 5)
    ax.axis("off")
    finish(fig, "03_prime_numbers.png")


def create_gcf():
    fig, ax = plt.subplots(figsize=(11, 5.8))
    ax.set_title("Greatest Common Factor", fontsize=18, fontweight="bold", pad=16)

    left = Circle((3.7, 2.7), 1.8, facecolor=COLORS["sky"], edgecolor=COLORS["dark"], alpha=0.85, linewidth=2.5)
    right = Circle((6.2, 2.7), 1.8, facecolor=COLORS["green"], edgecolor=COLORS["dark"], alpha=0.85, linewidth=2.5)
    ax.add_patch(left)
    ax.add_patch(right)

    ax.text(2.8, 4.2, "12", fontsize=16, fontweight="bold")
    ax.text(6.9, 4.2, "18", fontsize=16, fontweight="bold")
    for x, y, label in [(2.6, 3.2, "4"), (2.3, 2.3, "12"), (2.8, 1.4, "1")]:
        ax.text(x, y, label, fontsize=13, fontweight="bold")
    for x, y, label in [(6.9, 3.2, "9"), (7.2, 2.3, "18")]:
        ax.text(x, y, label, fontsize=13, fontweight="bold")
    for x, y, label in [(4.8, 3.2, "2"), (4.7, 2.3, "3"), (4.85, 1.45, "6")]:
        ax.text(x, y, label, fontsize=13, fontweight="bold", color=COLORS["dark"])

    ax.text(5.0, 0.7, "Shared factors are 1, 2, 3, 6. The largest is 6.", ha="center", fontsize=12)
    ax.set_xlim(0.6, 9.6)
    ax.set_ylim(0.2, 5)
    ax.axis("off")
    finish(fig, "04_gcf.png")


def create_lcm():
    fig, ax = plt.subplots(figsize=(11, 5.8))
    ax.set_title("Least Common Multiple", fontsize=18, fontweight="bold", pad=16)

    row_y = [3.7, 2.6]
    labels = ["Multiples of 4", "Multiples of 6"]
    rows = [[4, 8, 12, 16, 20, 24], [6, 12, 18, 24, 30, 36]]
    for row, y, label, color in zip(rows, row_y, labels, [COLORS["sky"], COLORS["green"]]):
        ax.text(0.6, y, label, fontsize=12, fontweight="bold", va="center")
        for idx, value in enumerate(row):
            x = 3.0 + idx * 1.1
            face = COLORS["gold"] if value in {12, 24} else color
            ax.add_patch(Rectangle((x, y - 0.42), 0.8, 0.84, facecolor=face, edgecolor=COLORS["dark"], linewidth=1.8))
            ax.text(x + 0.4, y, str(value), ha="center", va="center", fontsize=12, fontweight="bold")

    arrow = FancyArrowPatch((4.1, 1.65), (4.1, 2.18), arrowstyle="-|>", mutation_scale=18, linewidth=2.0, color=COLORS["dark"])
    ax.add_patch(arrow)
    ax.text(4.1, 1.1, "The first shared multiple is 12.", ha="center", fontsize=12)
    ax.set_xlim(0.2, 10.3)
    ax.set_ylim(0.5, 4.7)
    ax.axis("off")
    finish(fig, "05_lcm.png")


def create_equivalent_fractions():
    fig, ax = plt.subplots(figsize=(11, 5.8))
    ax.set_title("Equivalent Fractions", fontsize=18, fontweight="bold", pad=16)

    fractions = [(2, 1, "1/2"), (4, 2, "2/4"), (6, 3, "3/6")]
    x_positions = [1.4, 4.4, 7.4]
    for x, (parts, shaded, label) in zip(x_positions, fractions):
        for part in range(parts):
            color = COLORS["orange"] if part < shaded else COLORS["gray"]
            ax.add_patch(Rectangle((x + part * (1.8 / parts), 2.3), 1.8 / parts, 1.1, facecolor=color, edgecolor=COLORS["dark"], linewidth=1.5))
        ax.text(x + 0.9, 1.7, label, ha="center", fontsize=14, fontweight="bold")

    ax.text(5.5, 0.8, "Different-looking fractions can name the same amount.", ha="center", fontsize=12)
    ax.set_xlim(0.5, 10.0)
    ax.set_ylim(0.5, 4.5)
    ax.axis("off")
    finish(fig, "06_equivalent_fractions.png")


def create_comparing_fractions():
    fig, ax = plt.subplots(figsize=(11, 5.8))
    ax.set_title("Comparing Fractions", fontsize=18, fontweight="bold", pad=16)

    values = [2 / 3, 3 / 4]
    labels = ["2/3", "3/4"]
    colors = [COLORS["sky"], COLORS["purple"]]
    for idx, (value, label, color) in enumerate(zip(values, labels, colors)):
        x = 2.4 + idx * 3.6
        ax.add_patch(Rectangle((x, 1.2), 1.1, 3.0, facecolor=COLORS["gray"], edgecolor=COLORS["dark"], linewidth=2))
        ax.add_patch(Rectangle((x, 1.2), 1.1, 3.0 * value, facecolor=color, edgecolor=color))
        ax.text(x + 0.55, 4.45, label, ha="center", fontsize=14, fontweight="bold")

    ax.text(5.5, 0.65, "3/4 is taller on the same whole, so 3/4 > 2/3.", ha="center", fontsize=12)
    ax.set_xlim(0.6, 10.4)
    ax.set_ylim(0.4, 5.0)
    ax.axis("off")
    finish(fig, "07_comparing_fractions.png")


def create_add_subtract_fractions():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.8))
    fig.suptitle("Adding and Subtracting Fractions", fontsize=18, fontweight="bold", y=1.02)

    ax = axes[0]
    ax.set_title("1/4 + 2/4 = 3/4", fontsize=14, fontweight="bold")
    for idx in range(4):
        color = COLORS["orange"] if idx < 3 else COLORS["gray"]
        ax.add_patch(Rectangle((1.0 + idx * 0.8, 2.0), 0.75, 1.2, facecolor=color, edgecolor=COLORS["dark"], linewidth=1.8))
    ax.text(2.5, 1.4, "Same denominator: add the numerators", ha="center", fontsize=11)
    ax.axis("off")

    ax = axes[1]
    ax.set_title("5/6 - 2/6 = 3/6", fontsize=14, fontweight="bold")
    for idx in range(6):
        color = COLORS["green"] if idx < 3 else COLORS["gray"]
        ax.add_patch(Wedge((2.5, 2.6), 1.4, 60 * idx, 60 * (idx + 1), facecolor=color, edgecolor=COLORS["dark"], linewidth=1.8))
    ax.text(2.5, 0.8, "Think of taking pieces away from one whole.", ha="center", fontsize=11)
    ax.axis("off")

    finish(fig, "08_add_subtract_fractions.png")


def create_mixed_numbers():
    fig, ax = plt.subplots(figsize=(11, 5.8))
    ax.set_title("Mixed Numbers", fontsize=18, fontweight="bold", pad=16)

    for idx in range(4):
        color = COLORS["gold"] if idx < 4 else COLORS["gray"]
        ax.add_patch(Rectangle((1.2 + idx * 0.45, 2.0), 0.42, 1.2, facecolor=color, edgecolor=COLORS["dark"], linewidth=1.5))
    for idx in range(4):
        color = COLORS["orange"] if idx < 3 else COLORS["gray"]
        ax.add_patch(Rectangle((4.2 + idx * 0.45, 2.0), 0.42, 1.2, facecolor=color, edgecolor=COLORS["dark"], linewidth=1.5))

    ax.text(2.1, 3.6, "1 whole", ha="center", fontsize=13, fontweight="bold")
    ax.text(5.1, 3.6, "3/4", ha="center", fontsize=13, fontweight="bold")
    ax.text(3.6, 1.0, "7/4 = 1 3/4", ha="center", fontsize=16, fontweight="bold", color=COLORS["dark"])
    ax.set_xlim(0.4, 8.4)
    ax.set_ylim(0.5, 4.5)
    ax.axis("off")
    finish(fig, "09_mixed_numbers.png")


def create_review():
    fig, ax = plt.subplots(figsize=(11.5, 5.8))
    ax.set_title("Chapter 5 Review", fontsize=18, fontweight="bold", pad=16)

    nodes = [
        (1.6, 3.8, "Square\nNumbers", COLORS["sky"]),
        (3.8, 3.8, "Prime\nNumbers", COLORS["orange"]),
        (6.0, 3.8, "GCF\nLCM", COLORS["green"]),
        (8.2, 3.8, "Fractions", COLORS["purple"]),
        (5.0, 1.7, "Solve\nProblems", COLORS["gold"]),
    ]
    for x, y, label, color in nodes:
        ax.add_patch(Circle((x, y), 0.72, facecolor=color, edgecolor=COLORS["dark"], linewidth=2.4))
        ax.text(x, y, label, ha="center", va="center", fontsize=11, fontweight="bold")

    for x, y, _, _ in nodes[:-1]:
        ax.annotate("", (5.0, 1.7), (x, y - 0.8), arrowprops=dict(arrowstyle="->", lw=2))

    ax.text(5.0, 0.7, "Use the right idea for each problem, then explain your choice.", ha="center", fontsize=12)
    ax.set_xlim(0.5, 10.2)
    ax.set_ylim(0.4, 4.9)
    ax.axis("off")
    finish(fig, "10_chapter5_review.png")


if __name__ == "__main__":
    print("Generating Chapter 05 illustrations...")
    print("-" * 50)
    create_square_numbers()
    create_factors_multiples()
    create_prime_numbers()
    create_gcf()
    create_lcm()
    create_equivalent_fractions()
    create_comparing_fractions()
    create_add_subtract_fractions()
    create_mixed_numbers()
    create_review()
    print("-" * 50)
    print(f"All Chapter 05 illustrations saved to {OUTPUT_DIR}")
