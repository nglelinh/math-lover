#!/usr/bin/env python3
"""
Generate static illustrations for Chapter 07 lessons.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Polygon, Rectangle, Wedge


SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SCRIPT_DIR.parent.parent / "img" / "chapter_img" / "chapter07"
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


def create_probability():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.8))
    fig.suptitle("Probability", fontsize=18, fontweight="bold", y=1.02)

    ax = axes[0]
    ax.set_title("Coin Toss", fontsize=14, fontweight="bold")
    coin = Circle((2.3, 2.5), 1.2, facecolor=COLORS["gold"], edgecolor=COLORS["dark"], linewidth=2.5)
    ax.add_patch(coin)
    ax.plot([2.3, 2.3], [1.3, 3.7], color=COLORS["dark"], linewidth=1.8)
    ax.text(1.75, 2.5, "H", ha="center", va="center", fontsize=20, fontweight="bold")
    ax.text(2.85, 2.5, "T", ha="center", va="center", fontsize=20, fontweight="bold")
    ax.text(2.3, 0.7, "1 out of 2", ha="center", fontsize=12)
    ax.axis("off")

    ax = axes[1]
    ax.set_title("Dice Roll", fontsize=14, fontweight="bold")
    die = Rectangle((1.2, 1.2), 2.4, 2.4, facecolor="white", edgecolor=COLORS["dark"], linewidth=2.5)
    ax.add_patch(die)
    for px, py in [(1.8, 3.0), (2.4, 2.4), (3.0, 1.8)]:
        ax.add_patch(Circle((px, py), 0.12, facecolor=COLORS["dark"]))
    ax.text(2.4, 0.7, "Chance of rolling 3 = 1/6", ha="center", fontsize=12)
    ax.axis("off")

    finish(fig, "01_probability.png")


def create_statistics():
    fig, ax = plt.subplots(figsize=(11.5, 5.8))
    ax.set_title("Statistics", fontsize=18, fontweight="bold", pad=16)

    values = [4, 5, 5, 6, 8]
    x = np.arange(len(values))
    ax.bar(x, values, color=COLORS["sky"], edgecolor=COLORS["dark"], width=0.65)
    for idx, value in enumerate(values):
        ax.text(idx, value + 0.18, str(value), ha="center", fontsize=11)

    ax.text(4.8, 5.9, "Mean = 5.6", fontsize=12, fontweight="bold")
    ax.text(4.8, 5.2, "Median = 5", fontsize=12, fontweight="bold")
    ax.text(4.8, 4.5, "Mode = 5", fontsize=12, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels([f"Data {i+1}" for i in x], fontsize=10)
    ax.set_ylim(0, 6.8)
    ax.grid(axis="y", alpha=0.2)
    finish(fig, "02_statistics.png")


def create_charts():
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.8))
    fig.suptitle("Charts", fontsize=18, fontweight="bold", y=1.05)

    ax = axes[0]
    ax.set_title("Bar", fontsize=13, fontweight="bold")
    ax.bar(["A", "B", "C"], [4, 7, 5], color=[COLORS["sky"], COLORS["orange"], COLORS["green"]], edgecolor=COLORS["dark"])
    ax.set_ylim(0, 8)

    ax = axes[1]
    ax.set_title("Line", fontsize=13, fontweight="bold")
    x = np.arange(1, 6)
    y = np.array([2, 3, 5, 6, 8])
    ax.plot(x, y, marker="o", color=COLORS["purple"], linewidth=2.5)
    ax.set_ylim(0, 9)
    ax.grid(alpha=0.2)

    ax = axes[2]
    ax.set_title("Pie", fontsize=13, fontweight="bold")
    ax.pie([40, 35, 25], colors=[COLORS["gold"], COLORS["sky"], COLORS["green"]], labels=["A", "B", "C"], startangle=90)

    finish(fig, "03_charts.png")


def create_equations():
    fig, ax = plt.subplots(figsize=(11, 5.8))
    ax.set_title("Solving Equations", fontsize=18, fontweight="bold", pad=16)

    cards = [
        ("3x + 5 = 17", COLORS["sky"]),
        ("3x = 12", COLORS["green"]),
        ("x = 4", COLORS["orange"]),
    ]
    for idx, (text, color) in enumerate(cards):
        x = 0.8 + idx * 3.3
        ax.add_patch(Rectangle((x, 2.0), 2.5, 1.2, facecolor=color, edgecolor=COLORS["dark"], linewidth=2))
        ax.text(x + 1.25, 2.6, text, ha="center", va="center", fontsize=16, fontweight="bold", color="white")
        if idx < 2:
            ax.text(x + 2.75, 2.6, "->", fontsize=20, fontweight="bold", color=COLORS["dark"], va="center")

    ax.text(5.5, 1.0, "Undo the operations step by step.", ha="center", fontsize=12)
    ax.set_xlim(0.3, 10.8)
    ax.set_ylim(0.6, 4.6)
    ax.axis("off")
    finish(fig, "04_equations.png")


def create_percent():
    fig, ax = plt.subplots(figsize=(11.5, 5.8))
    ax.set_title("Percent in Daily Life", fontsize=18, fontweight="bold", pad=16)

    original = 800
    discount = 25
    new_price = 600
    ax.add_patch(Rectangle((1.0, 1.8), 2.2, 2.0, facecolor=COLORS["sky"], edgecolor=COLORS["dark"], linewidth=2))
    ax.add_patch(Rectangle((4.1, 1.8), 2.2, 2.0, facecolor=COLORS["gold"], edgecolor=COLORS["dark"], linewidth=2))
    ax.add_patch(Rectangle((7.2, 1.8), 2.2, 2.0, facecolor=COLORS["green"], edgecolor=COLORS["dark"], linewidth=2))
    ax.text(2.1, 3.0, f"{original}\nold price", ha="center", va="center", fontsize=15, fontweight="bold", color="white")
    ax.text(5.2, 3.0, f"- {discount}%\ndiscount", ha="center", va="center", fontsize=15, fontweight="bold", color=COLORS["dark"])
    ax.text(8.3, 3.0, f"{new_price}\nnew price", ha="center", va="center", fontsize=15, fontweight="bold", color=COLORS["dark"])
    ax.text(5.2, 0.95, "A 25% discount means paying 75% of the original price.", ha="center", fontsize=12)
    ax.set_xlim(0.4, 10.0)
    ax.set_ylim(0.5, 4.5)
    ax.axis("off")
    finish(fig, "05_percent.png")


def create_sphere_cone():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.8))
    fig.suptitle("Sphere and Cone", fontsize=18, fontweight="bold", y=1.02)

    ax = axes[0]
    ax.set_title("Sphere", fontsize=14, fontweight="bold")
    sphere = Circle((2.5, 2.5), 1.5, facecolor=COLORS["sky"], edgecolor=COLORS["dark"], linewidth=2.5)
    ax.add_patch(sphere)
    ax.plot([2.5, 4.0], [2.5, 2.5], color=COLORS["dark"], linewidth=2)
    ax.text(3.15, 2.8, "r", fontsize=12, fontweight="bold")
    ax.axis("off")

    ax = axes[1]
    ax.set_title("Cone", fontsize=14, fontweight="bold")
    cone = Polygon([(2.5, 4.0), (1.1, 1.2), (3.9, 1.2)], facecolor=COLORS["orange"], edgecolor=COLORS["dark"], linewidth=2.5)
    ax.add_patch(cone)
    base = Wedge((2.5, 1.2), 1.4, 0, 180, width=0.25, facecolor=COLORS["gold"], edgecolor=COLORS["dark"], linewidth=1.8)
    ax.add_patch(base)
    ax.axis("off")

    finish(fig, "06_sphere_cone.png")


def create_cylinder():
    fig, ax = plt.subplots(figsize=(11, 5.8))
    ax.set_title("Cylinder", fontsize=18, fontweight="bold", pad=16)

    top = Wedge((4.0, 3.9), 1.5, 0, 360, width=0.45, facecolor=COLORS["sky"], edgecolor=COLORS["dark"], linewidth=2)
    bottom = Wedge((4.0, 1.4), 1.5, 0, 180, width=0.45, facecolor=COLORS["green"], edgecolor=COLORS["dark"], linewidth=2)
    ax.add_patch(top)
    ax.add_patch(bottom)
    ax.plot([2.5, 2.5], [1.4, 3.9], color=COLORS["dark"], linewidth=2)
    ax.plot([5.5, 5.5], [1.4, 3.9], color=COLORS["dark"], linewidth=2)
    ax.text(4.0, 0.6, "Volume = pi x r^2 x h", ha="center", fontsize=12)
    ax.set_xlim(1.0, 7.0)
    ax.set_ylim(0.3, 5.0)
    ax.axis("off")
    finish(fig, "07_cylinder.png")


def create_sequences():
    fig, ax = plt.subplots(figsize=(11.5, 5.8))
    ax.set_title("Sequences", fontsize=18, fontweight="bold", pad=16)

    seq1 = [2, 5, 8, 11, 14]
    seq2 = [2, 6, 18, 54]
    for idx, value in enumerate(seq1):
        x = 1.0 + idx * 1.3
        ax.add_patch(Circle((x, 3.5), 0.35, facecolor=COLORS["sky"], edgecolor=COLORS["dark"], linewidth=2))
        ax.text(x, 3.5, str(value), ha="center", va="center", fontsize=12, fontweight="bold")
        if idx < len(seq1) - 1:
            ax.text(x + 0.65, 3.5, "+3", ha="center", va="center", fontsize=11, fontweight="bold")

    for idx, value in enumerate(seq2):
        x = 1.5 + idx * 2.0
        ax.add_patch(Rectangle((x - 0.45, 1.3), 0.9, 0.8, facecolor=COLORS["orange"], edgecolor=COLORS["dark"], linewidth=2))
        ax.text(x, 1.7, str(value), ha="center", va="center", fontsize=12, fontweight="bold")
        if idx < len(seq2) - 1:
            ax.text(x + 1.0, 1.7, "x3", ha="center", va="center", fontsize=11, fontweight="bold")

    ax.set_xlim(0.2, 10.3)
    ax.set_ylim(0.6, 4.6)
    ax.axis("off")
    finish(fig, "08_sequences.png")


def create_binary():
    fig, ax = plt.subplots(figsize=(11.5, 5.8))
    ax.set_title("Binary Numbers", fontsize=18, fontweight="bold", pad=16)

    headers = ["8", "4", "2", "1"]
    binary = ["1", "0", "1", "0"]
    for idx, header in enumerate(headers):
        x = 1.4 + idx * 1.6
        ax.add_patch(Rectangle((x, 3.0), 1.1, 0.9, facecolor=COLORS["gray"], edgecolor=COLORS["dark"], linewidth=2))
        ax.text(x + 0.55, 3.45, header, ha="center", va="center", fontsize=14, fontweight="bold")
        ax.add_patch(Rectangle((x, 1.8), 1.1, 0.9, facecolor=COLORS["green"] if binary[idx] == "1" else COLORS["sky"], edgecolor=COLORS["dark"], linewidth=2))
        ax.text(x + 0.55, 2.25, binary[idx], ha="center", va="center", fontsize=16, fontweight="bold", color="white")

    ax.text(4.0, 0.95, "1010 in binary = 8 + 2 = 10 in decimal", ha="center", fontsize=12)
    ax.set_xlim(0.6, 9.2)
    ax.set_ylim(0.5, 4.6)
    ax.axis("off")
    finish(fig, "09_binary.png")


def create_review():
    fig, ax = plt.subplots(figsize=(11.5, 5.8))
    ax.set_title("Chapter 7 Review", fontsize=18, fontweight="bold", pad=16)

    nodes = [
        (1.3, 3.8, "Probability", COLORS["sky"]),
        (3.2, 3.8, "Data", COLORS["green"]),
        (5.1, 3.8, "Charts", COLORS["gold"]),
        (7.0, 3.8, "Equations", COLORS["orange"]),
        (8.9, 3.8, "Shapes", COLORS["purple"]),
        (5.1, 1.4, "Review", COLORS["red"]),
    ]
    for x, y, label, color in nodes:
        ax.add_patch(Circle((x, y), 0.62, facecolor=color, edgecolor=COLORS["dark"], linewidth=2.2))
        ax.text(x, y, label, ha="center", va="center", fontsize=10.5, fontweight="bold")

    for x, y, _, _ in nodes[:-1]:
        ax.annotate("", (5.1, 1.4), (x, y - 0.67), arrowprops=dict(arrowstyle="->", lw=2))

    ax.text(5.1, 0.6, "Bring together chance, data, patterns, and models from daily life.", ha="center", fontsize=12)
    ax.set_xlim(0.4, 9.9)
    ax.set_ylim(0.35, 4.8)
    ax.axis("off")
    finish(fig, "10_chapter7_review.png")


if __name__ == "__main__":
    print("Generating Chapter 07 illustrations...")
    print("-" * 50)
    create_probability()
    create_statistics()
    create_charts()
    create_equations()
    create_percent()
    create_sphere_cone()
    create_cylinder()
    create_sequences()
    create_binary()
    create_review()
    print("-" * 50)
    print(f"All Chapter 07 illustrations saved to {OUTPUT_DIR}")
