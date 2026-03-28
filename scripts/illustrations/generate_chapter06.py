#!/usr/bin/env python3
"""
Generate static illustrations for Chapter 06 lessons.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, Polygon, Rectangle, Wedge


SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SCRIPT_DIR.parent.parent / "img" / "chapter_img" / "chapter06"
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


def create_decimal_numbers():
    fig, ax = plt.subplots(figsize=(11, 5.8))
    ax.set_title("Decimal Numbers", fontsize=18, fontweight="bold", pad=16)

    ax.plot([0, 10], [2.4, 2.4], color=COLORS["dark"], linewidth=2.5)
    for idx in range(11):
        ax.plot([idx, idx], [2.15, 2.65], color=COLORS["dark"], linewidth=1.5)
        ax.text(idx, 1.75, f"{idx/10:.1f}", ha="center", fontsize=10)

    points = [(2, "0.2", COLORS["sky"]), (5, "0.5", COLORS["gold"]), (7, "0.7", COLORS["orange"])]
    for x, label, color in points:
        ax.scatter([x], [2.4], s=170, color=color, edgecolors=COLORS["dark"], linewidth=2, zorder=3)
        ax.text(x, 3.0, label, ha="center", fontsize=12, fontweight="bold")

    place_cards = [("ones", "3"), ("tenths", "4"), ("hundredths", "5")]
    for idx, (name, value) in enumerate(place_cards):
        x = 1.0 + idx * 2.6
        ax.add_patch(Rectangle((x, 4.0), 1.9, 0.8, facecolor=[COLORS["sky"], COLORS["green"], COLORS["purple"]][idx], edgecolor=COLORS["dark"], linewidth=2))
        ax.text(x + 0.95, 4.4, f"{name}: {value}", ha="center", va="center", fontsize=11, fontweight="bold", color="white")

    ax.text(5.0, 0.85, "A decimal shows whole parts and smaller equal parts of one whole.", ha="center", fontsize=12)
    ax.set_xlim(-0.4, 10.4)
    ax.set_ylim(0.6, 5.2)
    ax.axis("off")
    finish(fig, "01_decimal_numbers.png")


def create_add_subtract_decimals():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.8))
    fig.suptitle("Adding and Subtracting Decimals", fontsize=18, fontweight="bold", y=1.02)

    ax = axes[0]
    ax.set_title("12.5 + 7.3 = 19.8", fontsize=14, fontweight="bold")
    ax.text(1.2, 3.8, " 12.5", fontsize=20, family="monospace")
    ax.text(1.2, 3.0, "+ 7.3", fontsize=20, family="monospace")
    ax.text(1.2, 2.55, "-----", fontsize=20, family="monospace")
    ax.text(1.2, 1.7, " 19.8", fontsize=20, family="monospace", color=COLORS["sky"])
    ax.text(2.2, 0.9, "Line up the decimal points.", ha="center", fontsize=11)
    ax.axis("off")

    ax = axes[1]
    ax.set_title("15.7 - 8.4 = 7.3", fontsize=14, fontweight="bold")
    ax.text(1.2, 3.8, " 15.7", fontsize=20, family="monospace")
    ax.text(1.2, 3.0, "- 8.4", fontsize=20, family="monospace")
    ax.text(1.2, 2.55, "-----", fontsize=20, family="monospace")
    ax.text(1.2, 1.7, "  7.3", fontsize=20, family="monospace", color=COLORS["orange"])
    ax.text(2.2, 0.9, "Subtract digit by digit.", ha="center", fontsize=11)
    ax.axis("off")

    finish(fig, "02_add_subtract_decimals.png")


def create_multiply_divide_decimals():
    fig, ax = plt.subplots(figsize=(11.5, 5.8))
    ax.set_title("Multiplying and Dividing Decimals", fontsize=18, fontweight="bold", pad=16)

    cards = [
        ("x 10", "3.5 -> 35", COLORS["sky"]),
        ("x 100", "2.75 -> 275", COLORS["green"]),
        ("/ 10", "48.6 -> 4.86", COLORS["orange"]),
        ("/ 100", "91.2 -> 0.912", COLORS["purple"]),
    ]
    for idx, (label, value, color) in enumerate(cards):
        x = 0.9 + idx * 2.6
        ax.add_patch(Rectangle((x, 2.0), 2.1, 1.5, facecolor=color, edgecolor=COLORS["dark"], linewidth=2))
        ax.text(x + 1.05, 3.0, label, ha="center", va="center", fontsize=13, fontweight="bold", color="white")
        ax.text(x + 1.05, 2.4, value, ha="center", va="center", fontsize=11, fontweight="bold", color="white")

    arrow = FancyArrowPatch((2.4, 1.2), (8.8, 1.2), arrowstyle="-|>", mutation_scale=18, linewidth=2.2, color=COLORS["dark"])
    ax.add_patch(arrow)
    ax.text(5.6, 0.7, "Moving the decimal point changes the size of the number.", ha="center", fontsize=12)
    ax.set_xlim(0.3, 11.3)
    ax.set_ylim(0.4, 4.6)
    ax.axis("off")
    finish(fig, "03_multiply_divide_decimals.png")


def create_ratios_proportions():
    fig, ax = plt.subplots(figsize=(11.5, 5.8))
    ax.set_title("Ratios and Proportions", fontsize=18, fontweight="bold", pad=16)

    for idx in range(5):
        ax.add_patch(Circle((1.2 + idx * 0.55, 3.4), 0.18, facecolor=COLORS["red"], edgecolor=COLORS["dark"], linewidth=1))
    for idx in range(3):
        ax.add_patch(Circle((1.5 + idx * 0.55, 2.6), 0.18, facecolor=COLORS["orange"], edgecolor=COLORS["dark"], linewidth=1))
    ax.text(2.2, 1.8, "5 : 3", ha="center", fontsize=18, fontweight="bold")

    boxes = [("2:4", "1:2", COLORS["sky"]), ("3:6", "1:2", COLORS["green"])]
    for idx, (left, right, color) in enumerate(boxes):
        x = 5.0 + idx * 2.7
        ax.add_patch(Rectangle((x, 2.4), 2.0, 1.2, facecolor=color, edgecolor=COLORS["dark"], linewidth=2))
        ax.text(x + 1.0, 3.0, f"{left} = {right}", ha="center", va="center", fontsize=13, fontweight="bold", color="white")

    ax.text(5.7, 1.0, "A ratio compares two amounts. A proportion says two ratios are equal.", ha="center", fontsize=12)
    ax.set_xlim(0.4, 10.8)
    ax.set_ylim(0.5, 4.8)
    ax.axis("off")
    finish(fig, "04_ratios_proportions.png")


def create_direct_inverse_proportion():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.8))
    fig.suptitle("Direct and Inverse Proportion", fontsize=18, fontweight="bold", y=1.02)

    ax = axes[0]
    ax.set_title("Direct", fontsize=14, fontweight="bold")
    x = np.arange(1, 6)
    y = 2 * x
    ax.plot(x, y, marker="o", color=COLORS["sky"], linewidth=2.5)
    ax.fill_between(x, y, color=COLORS["sky"], alpha=0.15)
    ax.set_xlim(0.8, 5.2)
    ax.set_ylim(0, 11)
    ax.grid(alpha=0.2)

    ax = axes[1]
    ax.set_title("Inverse", fontsize=14, fontweight="bold")
    x = np.arange(1, 6)
    y = 12 / x
    ax.plot(x, y, marker="o", color=COLORS["orange"], linewidth=2.5)
    ax.fill_between(x, y, color=COLORS["orange"], alpha=0.15)
    ax.set_xlim(0.8, 5.2)
    ax.set_ylim(0, 13)
    ax.grid(alpha=0.2)

    finish(fig, "05_direct_inverse_proportion.png")


def create_rectangle_parallelogram():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.8))
    fig.suptitle("Rectangle and Parallelogram", fontsize=18, fontweight="bold", y=1.02)

    ax = axes[0]
    ax.set_title("Rectangle", fontsize=14, fontweight="bold")
    rect = Rectangle((0.8, 1.2), 4.0, 2.6, facecolor=COLORS["green"], edgecolor=COLORS["dark"], linewidth=2.5)
    ax.add_patch(rect)
    ax.text(2.8, 4.1, "Area = length x width", ha="center", fontsize=12)
    ax.axis("off")

    ax = axes[1]
    ax.set_title("Parallelogram", fontsize=14, fontweight="bold")
    poly = Polygon([(1.0, 1.2), (4.6, 1.2), (4.0, 3.8), (0.4, 3.8)], facecolor=COLORS["purple"], edgecolor=COLORS["dark"], linewidth=2.5)
    ax.add_patch(poly)
    ax.plot([1.0, 1.0], [1.2, 3.8], color=COLORS["dark"], linestyle="--", linewidth=1.8)
    ax.text(2.5, 4.1, "Same formula: base x height", ha="center", fontsize=12)
    ax.axis("off")

    finish(fig, "06_rectangle_parallelogram.png")


def create_rhombus_trapezoid():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.8))
    fig.suptitle("Rhombus and Trapezoid", fontsize=18, fontweight="bold", y=1.02)

    ax = axes[0]
    ax.set_title("Rhombus", fontsize=14, fontweight="bold")
    rhombus = Polygon([(2.5, 4.0), (4.0, 2.5), (2.5, 1.0), (1.0, 2.5)], facecolor=COLORS["sky"], edgecolor=COLORS["dark"], linewidth=2.5)
    ax.add_patch(rhombus)
    ax.plot([2.5, 2.5], [1.0, 4.0], color=COLORS["dark"], linestyle="--", linewidth=1.8)
    ax.plot([1.0, 4.0], [2.5, 2.5], color=COLORS["dark"], linestyle="--", linewidth=1.8)
    ax.axis("off")

    ax = axes[1]
    ax.set_title("Trapezoid", fontsize=14, fontweight="bold")
    trap = Polygon([(0.8, 1.1), (4.4, 1.1), (3.5, 3.8), (1.7, 3.8)], facecolor=COLORS["gold"], edgecolor=COLORS["dark"], linewidth=2.5)
    ax.add_patch(trap)
    ax.plot([2.2, 2.2], [1.1, 3.8], color=COLORS["dark"], linestyle="--", linewidth=1.8)
    ax.axis("off")

    finish(fig, "07_rhombus_trapezoid.png")


def create_area_circle_triangle():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.8))
    fig.suptitle("Area of a Triangle and a Circle", fontsize=18, fontweight="bold", y=1.02)

    ax = axes[0]
    ax.set_title("Triangle", fontsize=14, fontweight="bold")
    tri = Polygon([(0.9, 1.2), (4.8, 1.2), (2.2, 4.0)], facecolor=COLORS["orange"], edgecolor=COLORS["dark"], linewidth=2.5)
    ax.add_patch(tri)
    ax.plot([2.2, 2.2], [1.2, 4.0], color=COLORS["dark"], linestyle="--", linewidth=1.8)
    ax.text(2.8, 0.6, "base x height / 2", ha="center", fontsize=12)
    ax.axis("off")

    ax = axes[1]
    ax.set_title("Circle", fontsize=14, fontweight="bold")
    circle = Circle((2.6, 2.5), 1.6, facecolor=COLORS["sky"], edgecolor=COLORS["dark"], linewidth=2.5)
    ax.add_patch(circle)
    ax.plot([2.6, 4.2], [2.5, 2.5], color=COLORS["dark"], linewidth=2)
    ax.text(2.6, 0.6, "Area = pi x r^2", ha="center", fontsize=12)
    ax.axis("off")

    finish(fig, "08_area_circle_triangle.png")


def create_volume():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.8))
    fig.suptitle("Volume", fontsize=18, fontweight="bold", y=1.02)

    ax = axes[0]
    ax.set_title("Rectangular Prism", fontsize=14, fontweight="bold")
    front = Rectangle((1.0, 1.0), 2.8, 2.4, facecolor=COLORS["green"], edgecolor=COLORS["dark"], linewidth=2.2)
    back = Rectangle((2.0, 1.8), 2.8, 2.4, facecolor="none", edgecolor=COLORS["dark"], linewidth=1.8)
    ax.add_patch(front)
    ax.add_patch(back)
    for (x1, y1), (x2, y2) in [((1.0, 1.0), (2.0, 1.8)), ((3.8, 1.0), (4.8, 1.8)), ((1.0, 3.4), (2.0, 4.2)), ((3.8, 3.4), (4.8, 4.2))]:
        ax.plot([x1, x2], [y1, y2], color=COLORS["dark"], linewidth=1.8)
    ax.axis("off")

    ax = axes[1]
    ax.set_title("Cube", fontsize=14, fontweight="bold")
    front = Rectangle((1.1, 1.1), 2.5, 2.5, facecolor=COLORS["purple"], edgecolor=COLORS["dark"], linewidth=2.2)
    back = Rectangle((2.0, 2.0), 2.5, 2.5, facecolor="none", edgecolor=COLORS["dark"], linewidth=1.8)
    ax.add_patch(front)
    ax.add_patch(back)
    for (x1, y1), (x2, y2) in [((1.1, 1.1), (2.0, 2.0)), ((3.6, 1.1), (4.5, 2.0)), ((1.1, 3.6), (2.0, 4.5)), ((3.6, 3.6), (4.5, 4.5))]:
        ax.plot([x1, x2], [y1, y2], color=COLORS["dark"], linewidth=1.8)
    ax.axis("off")

    finish(fig, "09_volume.png")


def create_review():
    fig, ax = plt.subplots(figsize=(11.5, 5.8))
    ax.set_title("Chapter 6 Review", fontsize=18, fontweight="bold", pad=16)

    nodes = [
        (1.4, 3.8, "Decimals", COLORS["sky"]),
        (3.4, 3.8, "Operations", COLORS["green"]),
        (5.4, 3.8, "Ratios", COLORS["gold"]),
        (7.4, 3.8, "Geometry", COLORS["orange"]),
        (9.4, 3.8, "Volume", COLORS["purple"]),
        (5.4, 1.5, "Review", COLORS["red"]),
    ]
    for x, y, label, color in nodes:
        ax.add_patch(Circle((x, y), 0.65, facecolor=color, edgecolor=COLORS["dark"], linewidth=2.2))
        ax.text(x, y, label, ha="center", va="center", fontsize=11, fontweight="bold")

    for x, y, _, _ in nodes[:-1]:
        ax.annotate("", (5.4, 1.5), (x, y - 0.7), arrowprops=dict(arrowstyle="->", lw=2))

    ax.text(5.4, 0.65, "Connect the ideas and choose the right formula for each problem.", ha="center", fontsize=12)
    ax.set_xlim(0.5, 10.3)
    ax.set_ylim(0.4, 4.8)
    ax.axis("off")
    finish(fig, "10_chapter6_review.png")


if __name__ == "__main__":
    print("Generating Chapter 06 illustrations...")
    print("-" * 50)
    create_decimal_numbers()
    create_add_subtract_decimals()
    create_multiply_divide_decimals()
    create_ratios_proportions()
    create_direct_inverse_proportion()
    create_rectangle_parallelogram()
    create_rhombus_trapezoid()
    create_area_circle_triangle()
    create_volume()
    create_review()
    print("-" * 50)
    print(f"All Chapter 06 illustrations saved to {OUTPUT_DIR}")
