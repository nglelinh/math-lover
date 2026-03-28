#!/usr/bin/env python3
"""
Generate static illustrations for Vietnamese Chapter 04 lessons.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle, Wedge


SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SCRIPT_DIR.parent.parent / "img" / "chapter_img" / "chapter04"
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


def create_variables():
    fig, ax = plt.subplots(figsize=(11, 5.8))
    ax.set_title("Variables", fontsize=18, fontweight="bold", pad=16)

    cards = [("x + 5 = 10", COLORS["sky"]), ("x = 5", COLORS["green"]), ("x means the hidden number", COLORS["gold"])]
    for idx, (text, color) in enumerate(cards):
        x = 0.9 + idx * 3.2
        ax.add_patch(Rectangle((x, 2.0), 2.4, 1.2, facecolor=color, edgecolor=COLORS["dark"], linewidth=2))
        ax.text(x + 1.2, 2.6, text, ha="center", va="center", fontsize=14, fontweight="bold", color="white" if idx < 2 else COLORS["dark"])

    ax.text(5.5, 0.9, "A variable is a letter standing for an unknown number.", ha="center", fontsize=12)
    ax.set_xlim(0.4, 10.7)
    ax.set_ylim(0.6, 4.5)
    ax.axis("off")
    finish(fig, "04_01_dai_so_bien_so.png")


def create_equations():
    fig, ax = plt.subplots(figsize=(11, 5.8))
    ax.set_title("Equations", fontsize=18, fontweight="bold", pad=16)

    steps = [("x + 7 = 15", COLORS["sky"]), ("x = 15 - 7", COLORS["orange"]), ("x = 8", COLORS["green"])]
    for idx, (text, color) in enumerate(steps):
        x = 0.8 + idx * 3.3
        ax.add_patch(Rectangle((x, 2.0), 2.5, 1.15, facecolor=color, edgecolor=COLORS["dark"], linewidth=2))
        ax.text(x + 1.25, 2.58, text, ha="center", va="center", fontsize=15, fontweight="bold", color="white")
        if idx < 2:
            ax.text(x + 2.8, 2.58, "->", fontsize=20, fontweight="bold", color=COLORS["dark"], va="center")

    ax.text(5.5, 1.0, "Solve by undoing the operation on the hidden number.", ha="center", fontsize=12)
    ax.set_xlim(0.3, 10.8)
    ax.set_ylim(0.7, 4.5)
    ax.axis("off")
    finish(fig, "04_02_phuong_trinh.png")


def create_decimal_fractions():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.8))
    fig.suptitle("Fractions and Decimals", fontsize=18, fontweight="bold", y=1.02)

    ax = axes[0]
    ax.set_title("1/4 = 0.25", fontsize=14, fontweight="bold")
    for idx in range(4):
        face = COLORS["orange"] if idx == 0 else COLORS["gray"]
        ax.add_patch(Rectangle((1.0 + idx * 0.8, 1.8), 0.75, 1.5, facecolor=face, edgecolor=COLORS["dark"], linewidth=1.6))
    ax.axis("off")

    ax = axes[1]
    ax.set_title("3/10 = 0.3", fontsize=14, fontweight="bold")
    ax.plot([0.6, 4.8], [2.5, 2.5], color=COLORS["dark"], linewidth=2)
    for idx in range(11):
        ax.plot([0.6 + idx * 0.42, 0.6 + idx * 0.42], [2.3, 2.7], color=COLORS["dark"], linewidth=1.2)
    ax.scatter([1.86], [2.5], s=180, color=COLORS["sky"], edgecolors=COLORS["dark"], linewidth=2)
    ax.text(1.86, 3.0, "0.3", ha="center", fontsize=12, fontweight="bold")
    ax.axis("off")

    finish(fig, "04_03_phan_so_thap_phan.png")


def create_proportion():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.8))
    fig.suptitle("Direct and Inverse Relationships", fontsize=18, fontweight="bold", y=1.02)

    ax = axes[0]
    ax.set_title("Direct", fontsize=14, fontweight="bold")
    ax.plot([1, 2, 3, 4], [2, 4, 6, 8], marker="o", color=COLORS["sky"], linewidth=2.5)
    ax.fill_between([1, 2, 3, 4], [2, 4, 6, 8], color=COLORS["sky"], alpha=0.15)
    ax.grid(alpha=0.2)

    ax = axes[1]
    ax.set_title("Inverse", fontsize=14, fontweight="bold")
    ax.plot([1, 2, 3, 4], [8, 4, 2.7, 2], marker="o", color=COLORS["orange"], linewidth=2.5)
    ax.fill_between([1, 2, 3, 4], [8, 4, 2.7, 2], color=COLORS["orange"], alpha=0.15)
    ax.grid(alpha=0.2)

    finish(fig, "04_04_ty_le_thuan_nghich.png")


def create_percent_applications():
    fig, ax = plt.subplots(figsize=(11.5, 5.8))
    ax.set_title("Percent Applications", fontsize=18, fontweight="bold", pad=16)

    ax.add_patch(Rectangle((0.9, 1.8), 2.3, 2.0, facecolor=COLORS["sky"], edgecolor=COLORS["dark"], linewidth=2))
    ax.add_patch(Rectangle((4.0, 1.8), 2.3, 2.0, facecolor=COLORS["gold"], edgecolor=COLORS["dark"], linewidth=2))
    ax.add_patch(Rectangle((7.1, 1.8), 2.3, 2.0, facecolor=COLORS["green"], edgecolor=COLORS["dark"], linewidth=2))
    ax.text(2.05, 3.0, "200,000\noriginal", ha="center", va="center", fontsize=15, fontweight="bold", color="white")
    ax.text(5.15, 3.0, "-20%\ndiscount", ha="center", va="center", fontsize=15, fontweight="bold", color=COLORS["dark"])
    ax.text(8.25, 3.0, "160,000\nnew price", ha="center", va="center", fontsize=15, fontweight="bold", color=COLORS["dark"])
    ax.text(5.15, 0.95, "Percent helps describe discounts, growth, and interest.", ha="center", fontsize=12)
    ax.set_xlim(0.4, 10.0)
    ax.set_ylim(0.5, 4.5)
    ax.axis("off")
    finish(fig, "04_05_phan_tram_ung_dung.png")


def create_geometry():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.8))
    fig.suptitle("Triangle and Square", fontsize=18, fontweight="bold", y=1.02)

    ax = axes[0]
    ax.set_title("Triangle", fontsize=14, fontweight="bold")
    triangle = Polygon([(1.0, 1.0), (4.5, 1.0), (2.7, 4.0)], facecolor=COLORS["orange"], edgecolor=COLORS["dark"], linewidth=2.5)
    ax.add_patch(triangle)
    ax.axis("off")

    ax = axes[1]
    ax.set_title("Square", fontsize=14, fontweight="bold")
    square = Rectangle((1.2, 1.1), 2.8, 2.8, facecolor=COLORS["green"], edgecolor=COLORS["dark"], linewidth=2.5)
    ax.add_patch(square)
    ax.axis("off")

    finish(fig, "04_06_hinh_hoc_hinh_tam_giac_hinh_vuong.png")


def create_measurement():
    fig, ax = plt.subplots(figsize=(11.5, 5.8))
    ax.set_title("Measurement Units", fontsize=18, fontweight="bold", pad=16)

    lengths = [("km", COLORS["sky"]), ("m", COLORS["green"]), ("cm", COLORS["orange"]), ("mm", COLORS["purple"])]
    for idx, (label, color) in enumerate(lengths):
        x = 1.0 + idx * 2.0
        ax.add_patch(Rectangle((x, 2.8), 1.2, 1.0, facecolor=color, edgecolor=COLORS["dark"], linewidth=2))
        ax.text(x + 0.6, 3.3, label, ha="center", va="center", fontsize=14, fontweight="bold", color="white")
        if idx < len(lengths) - 1:
            ax.text(x + 1.45, 3.3, "x10 or x100", ha="center", va="center", fontsize=10, fontweight="bold")

    masses = [("t", COLORS["gold"]), ("kg", COLORS["sky"]), ("g", COLORS["green"])]
    for idx, (label, color) in enumerate(masses):
        x = 2.1 + idx * 2.2
        ax.add_patch(Circle((x, 1.3), 0.45, facecolor=color, edgecolor=COLORS["dark"], linewidth=2))
        ax.text(x, 1.3, label, ha="center", va="center", fontsize=13, fontweight="bold", color="white" if label != "g" else COLORS["dark"])

    ax.set_xlim(0.4, 10.6)
    ax.set_ylim(0.4, 4.6)
    ax.axis("off")
    finish(fig, "04_07_do_luong_don_vi_do_dai_khoi_luong.png")


def create_time():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.8))
    fig.suptitle("Clock and Calendar", fontsize=18, fontweight="bold", y=1.02)

    ax = axes[0]
    ax.set_title("Clock", fontsize=14, fontweight="bold")
    clock = Circle((2.5, 2.5), 1.6, facecolor="white", edgecolor=COLORS["dark"], linewidth=2.5)
    ax.add_patch(clock)
    for idx in range(12):
        angle = idx * 30
        ax.text(2.5 + 1.25 * __import__("math").cos(__import__("math").radians(90 - angle)),
                2.5 + 1.25 * __import__("math").sin(__import__("math").radians(90 - angle)),
                str(idx + 1), ha="center", va="center", fontsize=10)
    ax.plot([2.5, 2.5], [2.5, 3.5], color=COLORS["dark"], linewidth=2.3)
    ax.plot([2.5, 3.4], [2.5, 2.5], color=COLORS["red"], linewidth=2.0)
    ax.axis("off")

    ax = axes[1]
    ax.set_title("Calendar", fontsize=14, fontweight="bold")
    days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
    for idx, day in enumerate(days):
        ax.text(0.7 + idx * 0.7, 4.2, day, ha="center", fontsize=10, fontweight="bold")
    count = 1
    for row in range(4):
        for col in range(7):
            x = 0.4 + col * 0.7
            y = 3.4 - row * 0.75
            ax.add_patch(Rectangle((x, y), 0.58, 0.5, facecolor=COLORS["gray"], edgecolor="white"))
            if count <= 28:
                ax.text(x + 0.29, y + 0.25, str(count), ha="center", va="center", fontsize=9)
                count += 1
    ax.axis("off")

    finish(fig, "04_08_thoi_gian_xem_dong_ho_va_lich.png")


def create_data():
    fig, ax = plt.subplots(figsize=(11.5, 5.8))
    ax.set_title("Collecting and Displaying Data", fontsize=18, fontweight="bold", pad=16)

    sports = ["Football", "Basketball", "Swimming", "Badminton"]
    values = [10, 6, 4, 5]
    colors = [COLORS["sky"], COLORS["orange"], COLORS["green"], COLORS["purple"]]
    ax.bar(sports, values, color=colors, edgecolor=COLORS["dark"], width=0.6)
    for idx, value in enumerate(values):
        ax.text(idx, value + 0.2, str(value), ha="center", fontsize=10)
    ax.set_ylim(0, 11.5)
    ax.grid(axis="y", alpha=0.2)
    finish(fig, "04_09_du_lieu_thu_thap_va_bieu_dien_thong_tin.png")


def create_review():
    fig, ax = plt.subplots(figsize=(11.5, 5.8))
    ax.set_title("Chapter 4 Review", fontsize=18, fontweight="bold", pad=16)

    nodes = [
        (1.4, 3.8, "Algebra", COLORS["sky"]),
        (3.3, 3.8, "Decimals", COLORS["green"]),
        (5.2, 3.8, "Percent", COLORS["gold"]),
        (7.1, 3.8, "Geometry", COLORS["orange"]),
        (9.0, 3.8, "Data", COLORS["purple"]),
        (5.2, 1.4, "Review", COLORS["red"]),
    ]
    for x, y, label, color in nodes:
        ax.add_patch(Circle((x, y), 0.62, facecolor=color, edgecolor=COLORS["dark"], linewidth=2.2))
        ax.text(x, y, label, ha="center", va="center", fontsize=10.5, fontweight="bold")

    for x, y, _, _ in nodes[:-1]:
        ax.annotate("", (5.2, 1.4), (x, y - 0.67), arrowprops=dict(arrowstyle="->", lw=2))

    ax.text(5.2, 0.62, "Bring together hidden numbers, measurements, shapes, and data.", ha="center", fontsize=12)
    ax.set_xlim(0.4, 9.8)
    ax.set_ylim(0.35, 4.8)
    ax.axis("off")
    finish(fig, "04_10_on_tap_tong_ket_chuong_4.png")


if __name__ == "__main__":
    print("Generating Chapter 04 Vietnamese illustrations...")
    print("-" * 50)
    create_variables()
    create_equations()
    create_decimal_fractions()
    create_proportion()
    create_percent_applications()
    create_geometry()
    create_measurement()
    create_time()
    create_data()
    create_review()
    print("-" * 50)
    print(f"All Chapter 04 Vietnamese illustrations saved to {OUTPUT_DIR}")
