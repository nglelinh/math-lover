#!/usr/bin/env python3
"""
Generate simple static illustrations for Chapter 03 lessons.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, Polygon, Rectangle

SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SCRIPT_DIR.parent.parent / "img" / "chapter_img" / "chapter03"
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


def create_logic_puzzle():
    fig, ax = plt.subplots(figsize=(11, 6))
    ax.set_title("Logic Puzzle: Eliminate and Decide", fontsize=18, fontweight="bold", pad=18)

    box_x = [1.4, 4.5, 7.6]
    labels = ["Red Box", "Blue Box", "Yellow Box"]
    fills = [COLORS["red"], COLORS["sky"], COLORS["gold"]]

    for x, label, fill in zip(box_x, labels, fills):
        rect = Rectangle((x, 2.1), 1.9, 1.9, facecolor=fill, edgecolor=COLORS["dark"], linewidth=3)
        ax.add_patch(rect)
        ax.text(x + 0.95, 1.7, label, ha="center", fontsize=12, fontweight="bold")

    ax.text(2.35, 3.05, "X", ha="center", va="center", fontsize=34, fontweight="bold", color="white")
    ax.text(8.55, 3.05, "X", ha="center", va="center", fontsize=34, fontweight="bold", color=COLORS["dark"])
    ax.text(5.45, 3.05, "?", ha="center", va="center", fontsize=34, fontweight="bold", color="white")

    notes = [
        "1. Not in the red box",
        "2. In the blue or yellow box",
        "3. Yellow box is empty",
    ]
    for idx, note in enumerate(notes):
        ax.text(0.8, 5.2 - idx * 0.5, note, fontsize=12, bbox=dict(boxstyle="round", facecolor="white", alpha=0.95))

    arrow = FancyArrowPatch((5.45, 4.35), (5.45, 4.95), arrowstyle="-|>", mutation_scale=18, linewidth=2.5, color=COLORS["dark"])
    ax.add_patch(arrow)
    ax.text(5.45, 5.2, "Check clues one by one", ha="center", fontsize=12, color=COLORS["dark"])

    ax.set_xlim(0, 10)
    ax.set_ylim(1.2, 6.2)
    ax.axis("off")
    finish(fig, "03_01_toan_tu_duy.png")


def create_area_diagram():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.8))
    fig.suptitle("Area by Cutting and Joining", fontsize=18, fontweight="bold", y=1.02)

    ax = axes[0]
    ax.set_title("Triangle from a Rectangle", fontsize=14, fontweight="bold")
    rect = Rectangle((0.5, 0.5), 5.5, 3.5, facecolor=COLORS["green"], edgecolor=COLORS["dark"], linewidth=3)
    tri = Polygon([(0.5, 0.5), (6.0, 0.5), (6.0, 4.0)], facecolor=COLORS["orange"], edgecolor=COLORS["dark"], alpha=0.9)
    ax.add_patch(rect)
    ax.add_patch(tri)
    ax.plot([0.5, 6.0], [0.5, 4.0], color=COLORS["dark"], linewidth=2.5)
    ax.text(3.25, 4.25, "Area = base x height / 2", ha="center", fontsize=12)
    ax.set_xlim(0, 6.8)
    ax.set_ylim(0, 5)
    ax.axis("off")

    ax = axes[1]
    ax.set_title("Trapezoid as Half of a Joined Shape", fontsize=14, fontweight="bold")
    trap1 = Polygon([(0.6, 0.8), (3.0, 0.8), (2.4, 3.8), (1.2, 3.8)], facecolor=COLORS["sky"], edgecolor=COLORS["dark"], linewidth=3)
    trap2 = Polygon([(3.0, 0.8), (5.4, 0.8), (4.8, 3.8), (3.6, 3.8)], facecolor=COLORS["purple"], edgecolor=COLORS["dark"], linewidth=3)
    ax.add_patch(trap1)
    ax.add_patch(trap2)
    ax.text(3.0, 4.25, "Join two matching trapezoids", ha="center", fontsize=12)
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 5)
    ax.axis("off")

    finish(fig, "03_02_dien_tich_nang_cao.png")


def create_big_numbers():
    fig, ax = plt.subplots(figsize=(11, 5.6))
    ax.set_title("Place Value Ladder", fontsize=18, fontweight="bold", pad=16)

    names = ["ones", "tens", "hundreds", "thousands", "millions", "billions"]
    values = ["1", "10", "100", "1,000", "1,000,000", "1,000,000,000"]
    for i, (name, value) in enumerate(zip(names, values)):
        x = 0.8 + i * 1.7
        rect = Rectangle((x, 1.8), 1.2, 1.5, facecolor=list(COLORS.values())[i], edgecolor=COLORS["dark"], linewidth=2.5)
        ax.add_patch(rect)
        ax.text(x + 0.6, 2.75, value, ha="center", va="center", fontsize=12, fontweight="bold", color="white")
        ax.text(x + 0.6, 1.35, name.title(), ha="center", fontsize=11)
        if i < len(names) - 1:
            ax.annotate("x10", (x + 1.25, 2.55), (x + 1.65, 2.55), arrowprops=dict(arrowstyle="->", lw=2))

    ax.text(5.3, 0.55, "Every step left makes the value 10 times bigger.", ha="center", fontsize=12)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 4.1)
    ax.axis("off")
    finish(fig, "03_03_so_lon.png")


def create_word_problem_flow():
    fig, ax = plt.subplots(figsize=(11.5, 5.8))
    ax.set_title("Solve a Word Problem in 4 Steps", fontsize=18, fontweight="bold", pad=16)

    steps = [("Read", COLORS["sky"]), ("Plan", COLORS["green"]), ("Solve", COLORS["orange"]), ("Check", COLORS["purple"])]
    for i, (label, color) in enumerate(steps):
        x = 0.8 + i * 2.65
        rect = Rectangle((x, 2.1), 1.9, 1.3, facecolor=color, edgecolor=COLORS["dark"], linewidth=3)
        ax.add_patch(rect)
        ax.text(x + 0.95, 2.75, label, ha="center", va="center", fontsize=14, fontweight="bold", color="white")
        if i < len(steps) - 1:
            arr = FancyArrowPatch((x + 1.95, 2.75), (x + 2.55, 2.75), arrowstyle="-|>", mutation_scale=18, linewidth=2.5, color=COLORS["dark"])
            ax.add_patch(arr)

    ax.text(1.7, 1.2, "Find the important numbers", ha="center", fontsize=11)
    ax.text(4.35, 1.2, "Choose the right operation", ha="center", fontsize=11)
    ax.text(7.0, 1.2, "Work step by step", ha="center", fontsize=11)
    ax.text(9.65, 1.2, "Does the answer make sense?", ha="center", fontsize=11)

    ax.set_xlim(0, 11.5)
    ax.set_ylim(0.3, 4.2)
    ax.axis("off")
    finish(fig, "03_04_bai_toan_do.png")


def create_pascal_triangle():
    fig, ax = plt.subplots(figsize=(8.4, 7))
    ax.set_title("Pascal Triangle", fontsize=18, fontweight="bold", pad=18)

    rows = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1],
    ]

    for r, row in enumerate(rows):
        y = 6 - r
        start_x = 4 - 0.55 * (len(row) - 1)
        for c, value in enumerate(row):
            x = start_x + c * 1.1
            face = COLORS["gold"] if c == 2 and r >= 2 else COLORS["sky"]
            circ = Circle((x, y), 0.38, facecolor=face, edgecolor=COLORS["dark"], linewidth=2.5)
            ax.add_patch(circ)
            ax.text(x, y, str(value), ha="center", va="center", fontsize=12, fontweight="bold")

    ax.text(4, 0.6, "Each inside number = the sum of two numbers above it", ha="center", fontsize=12)
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 6.9)
    ax.axis("off")
    finish(fig, "03_05_tam_giac_pascal.png")


def create_grid_and_sudoku():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.8))
    fig.suptitle("Grid Logic and Sudoku", fontsize=18, fontweight="bold", y=1.02)

    ax = axes[0]
    ax.set_title("Magic 3 x 3 Grid", fontsize=14, fontweight="bold")
    grid = np.array([[2, 7, 6], [9, 5, 1], [4, 3, 8]])
    for r in range(3):
        for c in range(3):
            ax.add_patch(Rectangle((c, 2 - r), 1, 1, facecolor=COLORS["gray"], edgecolor=COLORS["dark"], linewidth=2))
            ax.text(c + 0.5, 2.5 - r, str(grid[r, c]), ha="center", va="center", fontsize=16, fontweight="bold")
    ax.text(1.5, -0.35, "Every row and column sums to 15", ha="center", fontsize=11)
    ax.set_xlim(0, 3)
    ax.set_ylim(-0.7, 3)
    ax.axis("off")

    ax = axes[1]
    ax.set_title("Sudoku 4 x 4", fontsize=14, fontweight="bold")
    grid = [["1", "", "3", "4"], ["3", "4", "1", "2"], ["", "1", "4", ""], ["4", "", "2", "3"]]
    for r in range(4):
        for c in range(4):
            face = COLORS["green"] if grid[r][c] == "" else "white"
            ax.add_patch(Rectangle((c, 3 - r), 1, 1, facecolor=face, edgecolor=COLORS["dark"], linewidth=2))
            if grid[r][c]:
                ax.text(c + 0.5, 3.5 - r, grid[r][c], ha="center", va="center", fontsize=16, fontweight="bold")
            else:
                ax.text(c + 0.5, 3.5 - r, "?", ha="center", va="center", fontsize=16, fontweight="bold", color=COLORS["dark"])
    ax.plot([2, 2], [0, 4], color=COLORS["dark"], linewidth=3)
    ax.plot([0, 4], [2, 2], color=COLORS["dark"], linewidth=3)
    ax.text(2, -0.35, "Use row, column, and mini-square clues", ha="center", fontsize=11)
    ax.set_xlim(0, 4)
    ax.set_ylim(-0.7, 4)
    ax.axis("off")

    finish(fig, "03_06_luoi_so.png")


def create_patterns():
    fig, ax = plt.subplots(figsize=(11, 5.8))
    ax.set_title("Find the Pattern", fontsize=18, fontweight="bold", pad=16)

    seq1 = [2, 5, 8, 11, 14]
    seq2 = [1, 4, 9, 16, 25]
    x = np.arange(len(seq1))

    ax.scatter(x, seq1, s=240, color=COLORS["sky"], edgecolors=COLORS["dark"], linewidth=2, label="Add 3")
    ax.plot(x, seq1, color=COLORS["sky"], linewidth=2)
    ax.scatter(x, seq2, s=240, color=COLORS["orange"], edgecolors=COLORS["dark"], linewidth=2, label="Square numbers")
    ax.plot(x, seq2, color=COLORS["orange"], linewidth=2)

    for i, value in enumerate(seq1):
        ax.text(i, value + 0.9, str(value), ha="center", fontsize=10)
    for i, value in enumerate(seq2):
        ax.text(i, value + 0.9, str(value), ha="center", fontsize=10)

    ax.annotate("+3", (1.5, 9), (0.8, 12), arrowprops=dict(arrowstyle="->", lw=2), fontsize=12)
    ax.annotate("+5, +7, +9 ...", (2.4, 16), (2.7, 22), arrowprops=dict(arrowstyle="->", lw=2), fontsize=12)
    ax.set_xlim(-0.4, 4.5)
    ax.set_ylim(0, 30)
    ax.set_xticks([])
    ax.grid(alpha=0.2)
    ax.legend(loc="upper left")
    finish(fig, "03_07_tim_quy_luat.png")


def create_math_games():
    fig, ax = plt.subplots(figsize=(11.5, 5.8))
    ax.set_title("Math Games Build Smart Strategies", fontsize=18, fontweight="bold", pad=16)

    left = Rectangle((0.8, 1.2), 3.0, 3.2, facecolor=COLORS["sky"], edgecolor=COLORS["dark"], linewidth=3)
    mid = Rectangle((4.25, 1.2), 3.0, 3.2, facecolor=COLORS["gold"], edgecolor=COLORS["dark"], linewidth=3)
    right = Rectangle((7.7, 1.2), 3.0, 3.2, facecolor=COLORS["green"], edgecolor=COLORS["dark"], linewidth=3)
    for rect in (left, mid, right):
        ax.add_patch(rect)

    ax.text(2.3, 3.65, "Guess the Number", ha="center", fontsize=14, fontweight="bold")
    ax.text(2.3, 2.4, "1 ... 50\nAlways test the middle", ha="center", fontsize=12)

    ax.text(5.75, 3.65, "24 Game", ha="center", fontsize=14, fontweight="bold")
    ax.text(5.75, 2.4, "3, 4, 6, 2\nUse + - x / to make 24", ha="center", fontsize=12)

    ax.text(9.2, 3.65, "Logic Riddle", ha="center", fontsize=14, fontweight="bold")
    ax.text(9.2, 2.4, "Read carefully\nThink before guessing", ha="center", fontsize=12)

    ax.set_xlim(0, 11.5)
    ax.set_ylim(0.5, 5)
    ax.axis("off")
    finish(fig, "03_08_toan_vui.png")


def create_fibonacci():
    fig, ax = plt.subplots(figsize=(11, 5.8))
    ax.set_title("Fibonacci Pattern", fontsize=18, fontweight="bold", pad=16)

    seq = [1, 1, 2, 3, 5, 8, 13]
    x = np.arange(len(seq))
    ax.bar(x, seq, color=[COLORS["green"], COLORS["green"], COLORS["sky"], COLORS["sky"], COLORS["orange"], COLORS["orange"], COLORS["purple"]], edgecolor=COLORS["dark"])
    ax.plot(x, seq, color=COLORS["dark"], linewidth=2, marker="o")

    for i, value in enumerate(seq):
        ax.text(i, value + 0.4, str(value), ha="center", fontsize=11, fontweight="bold")

    ax.text(1.9, 12.5, "1 + 2 = 3", fontsize=11)
    ax.text(3.2, 11.1, "2 + 3 = 5", fontsize=11)
    ax.text(4.2, 9.3, "3 + 5 = 8", fontsize=11)
    ax.text(5.0, 7.0, "5 + 8 = 13", fontsize=11)
    ax.set_xticks(x)
    ax.set_xticklabels([f"Term {i+1}" for i in x], fontsize=10)
    ax.set_ylim(0, 16)
    ax.grid(axis="y", alpha=0.2)
    finish(fig, "03_09_fibonacci.png")


def create_review_map():
    fig, ax = plt.subplots(figsize=(11.5, 5.8))
    ax.set_title("Chapter 3 Review Map", fontsize=18, fontweight="bold", pad=16)

    nodes = [
        (1.4, 3.6, "Logic"),
        (3.7, 3.6, "Area"),
        (6.0, 3.6, "Patterns"),
        (8.3, 3.6, "Games"),
        (10.0, 2.0, "Review"),
    ]
    for x, y, label in nodes[:-1]:
        circ = Circle((x, y), 0.72, facecolor=COLORS["sky"], edgecolor=COLORS["dark"], linewidth=2.5)
        ax.add_patch(circ)
        ax.text(x, y, label, ha="center", va="center", fontsize=12, fontweight="bold")

    star = Polygon([(9.5, 1.5), (9.8, 2.2), (10.6, 2.2), (10.0, 2.65), (10.25, 3.35), (9.5, 2.9), (8.75, 3.35), (9.0, 2.65), (8.4, 2.2), (9.2, 2.2)],
                   closed=True, facecolor=COLORS["gold"], edgecolor=COLORS["dark"], linewidth=2.5)
    ax.add_patch(star)
    ax.text(9.5, 2.42, "Review", ha="center", va="center", fontsize=12, fontweight="bold")

    for x, y, _ in nodes[:-1]:
        ax.annotate("", (9.05, 2.45), (x + 0.68, y - 0.25), arrowprops=dict(arrowstyle="->", lw=2))

    ax.text(5.8, 0.9, "Put every idea together and explain what you learned.", ha="center", fontsize=12)
    ax.set_xlim(0.2, 11)
    ax.set_ylim(0.4, 4.8)
    ax.axis("off")
    finish(fig, "03_10_on_tap.png")


if __name__ == "__main__":
    print("Generating Chapter 03 illustrations...")
    print("-" * 50)
    create_logic_puzzle()
    create_area_diagram()
    create_big_numbers()
    create_word_problem_flow()
    create_pascal_triangle()
    create_grid_and_sudoku()
    create_patterns()
    create_math_games()
    create_fibonacci()
    create_review_map()
    print("-" * 50)
    print(f"All Chapter 03 illustrations saved to {OUTPUT_DIR}")
