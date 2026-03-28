#!/usr/bin/env python3
"""Generate simple child-friendly SVG lesson illustrations."""

from __future__ import annotations

from html import escape
from math import cos, pi, sin
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
WIDTH = 960
HEIGHT = 540

BG = "#FFF7ED"
INK = "#223042"
MUTED = "#5F6B7A"
WHITE = "#FFFFFF"
CORAL = "#FF8A65"
TEAL = "#38B8C5"
YELLOW = "#F6C453"
GREEN = "#7BC47F"
BLUE = "#7AA8FF"
PINK = "#F9A8D4"
SAND = "#FCE7C3"


def rect(x, y, w, h, fill=WHITE, stroke=INK, sw=4, rx=24):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
    )


def circle(cx, cy, r, fill=WHITE, stroke=INK, sw=4):
    return (
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" '
        f'stroke="{stroke}" stroke-width="{sw}"/>'
    )


def ellipse(cx, cy, rx, ry, fill=WHITE, stroke=INK, sw=4):
    return (
        f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" '
        f'stroke="{stroke}" stroke-width="{sw}"/>'
    )


def line(x1, y1, x2, y2, stroke=INK, sw=6, dash=None, marker=False):
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    marker_attr = ' marker-end="url(#arrow)"' if marker else ""
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
        f'stroke-width="{sw}" stroke-linecap="round"{dash_attr}{marker_attr}/>'
    )


def polygon(points, fill=WHITE, stroke=INK, sw=4):
    joined = " ".join(f"{x},{y}" for x, y in points)
    return (
        f'<polygon points="{joined}" fill="{fill}" stroke="{stroke}" '
        f'stroke-width="{sw}" stroke-linejoin="round"/>'
    )


def path(d, fill="none", stroke=INK, sw=4):
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def text(x, y, value, size=34, weight=700, fill=INK, anchor="middle"):
    return (
        f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" '
        f'font-size="{size}" font-weight="{weight}" fill="{fill}" '
        f'text-anchor="{anchor}">{escape(str(value))}</text>'
    )


def card(x, y, w, h, fill=WHITE):
    return rect(x, y, w, h, fill=fill, stroke=INK, sw=4, rx=28)


def svg(label, parts):
    defs = """
    <defs>
      <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5"
              markerWidth="8" markerHeight="8" orient="auto-start-reverse">
        <path d="M 0 0 L 10 5 L 0 10 z" fill="#223042"/>
      </marker>
    </defs>
    """
    body = "".join(parts)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" '
        f'role="img" aria-label="{escape(label)}">{defs}'
        f'<rect width="{WIDTH}" height="{HEIGHT}" fill="{BG}"/>{body}</svg>'
    )


def save(relative_path, content):
    path = ROOT / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def dot_grid(x, y, cols, rows, radius=16, fill=TEAL):
    parts = []
    gap = radius * 2 + 14
    for row in range(rows):
        for col in range(cols):
            cx = x + col * gap
            cy = y + row * gap
            parts.append(circle(cx, cy, radius, fill=fill))
    return parts


def number_token(cx, cy, value, fill=TEAL):
    content = str(value)
    size = 30 if len(content) <= 3 else 24 if len(content) <= 4 else 20
    return [circle(cx, cy, 38, fill=fill), text(cx, cy + 12, content, size=size)]


def fraction_bar(x, y, w, h, numerator, denominator, fill=CORAL):
    parts = [rect(x, y, w, h, fill=WHITE, stroke=INK, sw=4, rx=18)]
    cell = w / denominator
    for index in range(denominator):
        if index < numerator:
            parts.append(
                rect(
                    x + index * cell,
                    y,
                    cell,
                    h,
                    fill=fill,
                    stroke="none",
                    sw=0,
                    rx=0,
                )
            )
        if index:
            parts.append(line(x + index * cell, y, x + index * cell, y + h, sw=3))
    parts.append(text(x + w / 2, y + h + 50, f"{numerator}/{denominator}", size=36))
    return parts


def analog_clock(cx, cy, radius, hour, minute):
    parts = [circle(cx, cy, radius, fill=WHITE)]
    for mark in range(12):
        angle = -pi / 2 + mark * pi / 6
        inner = radius - 18
        outer = radius - 6
        parts.append(
            line(
                cx + cos(angle) * inner,
                cy + sin(angle) * inner,
                cx + cos(angle) * outer,
                cy + sin(angle) * outer,
                sw=4,
            )
        )
    minute_angle = -pi / 2 + minute * pi / 30
    hour_angle = -pi / 2 + ((hour % 12) + minute / 60) * pi / 6
    parts.append(line(cx, cy, cx + cos(hour_angle) * (radius - 70), cy + sin(hour_angle) * (radius - 70), sw=8))
    parts.append(line(cx, cy, cx + cos(minute_angle) * (radius - 36), cy + sin(minute_angle) * (radius - 36), sw=6, stroke=CORAL))
    parts.append(circle(cx, cy, 10, fill=INK, stroke=INK, sw=0))
    return parts


def calendar(x, y, w, h, day):
    return [
        rect(x, y, w, h, fill=WHITE, stroke=INK, sw=4, rx=22),
        rect(x, y, w, 52, fill=CORAL, stroke=INK, sw=4, rx=22),
        text(x + w / 2, y + 130, day, size=64),
    ]


def money_note(x, y, w, h, value, fill):
    return [
        rect(x, y, w, h, fill=fill, stroke=INK, sw=4, rx=18),
        rect(x + 18, y + 18, w - 36, h - 36, fill="none", stroke=INK, sw=3, rx=12),
        text(x + w / 2, y + h / 2 + 14, value, size=30),
    ]


def coin(cx, cy, r, value, fill):
    return [
        circle(cx, cy, r, fill=fill, stroke=INK, sw=4),
        circle(cx, cy, r - 10, fill="none", stroke=INK, sw=3),
        text(cx, cy + 10, value, size=22),
    ]


def basic_shape(name, x, y, size, fill):
    if name == "triangle":
        return [polygon([(x, y + size), (x + size / 2, y), (x + size, y + size)], fill=fill)]
    if name == "square":
        return [rect(x, y, size, size, fill=fill, stroke=INK, sw=4, rx=8)]
    if name == "circle":
        return [circle(x + size / 2, y + size / 2, size / 2, fill=fill)]
    if name == "rectangle":
        return [rect(x, y + size * 0.15, size * 1.2, size * 0.7, fill=fill, stroke=INK, sw=4, rx=12)]
    if name == "parallelogram":
        return [
            polygon(
                [
                    (x + 28, y + size * 0.12),
                    (x + size * 1.18, y + size * 0.12),
                    (x + size * 0.98, y + size * 0.82),
                    (x - 8, y + size * 0.82),
                ],
                fill=fill,
            )
        ]
    if name == "rhombus":
        return [
            polygon(
                [
                    (x + size * 0.5, y),
                    (x + size, y + size * 0.5),
                    (x + size * 0.5, y + size),
                    (x, y + size * 0.5),
                ],
                fill=fill,
            )
        ]
    if name == "trapezoid":
        return [
            polygon(
                [
                    (x + size * 0.2, y),
                    (x + size * 0.8, y),
                    (x + size, y + size),
                    (x, y + size),
                ],
                fill=fill,
            )
        ]
    raise ValueError(f"Unsupported shape: {name}")


def sphere(cx, cy, r):
    return [
        circle(cx, cy, r, fill=BLUE),
        ellipse(cx - 12, cy - 12, r * 0.52, r * 0.28, fill="none", stroke=WHITE, sw=10),
    ]


def cone(cx, cy, w, h):
    return [
        ellipse(cx, cy - h / 2 + 18, w / 2, 20, fill=SAND),
        polygon([(cx, cy - h / 2), (cx - w / 2, cy + h / 2), (cx + w / 2, cy + h / 2)], fill=CORAL),
        ellipse(cx, cy + h / 2, w / 2, 20, fill=SAND),
    ]


def cylinder(cx, cy, w, h):
    return [
        rect(cx - w / 2, cy - h / 2, w, h, fill=TEAL, stroke=INK, sw=4, rx=8),
        ellipse(cx, cy - h / 2, w / 2, 24, fill=SAND),
        ellipse(cx, cy + h / 2, w / 2, 24, fill=SAND),
    ]


def balance_scale(left_label, right_label):
    parts = [
        line(480, 120, 480, 360, sw=10),
        line(330, 180, 630, 180, sw=10),
        line(360, 180, 330, 260, sw=4),
        line(600, 180, 630, 260, sw=4),
        rect(270, 260, 120, 28, fill=SAND, stroke=INK, sw=4, rx=8),
        rect(570, 260, 120, 28, fill=SAND, stroke=INK, sw=4, rx=8),
        text(330, 245, left_label, size=34),
        text(630, 245, right_label, size=34),
    ]
    return parts


def review_badges(tokens):
    colors = [CORAL, TEAL, YELLOW, GREEN]
    xs = [210, 400, 590, 780]
    parts = []
    for index, token in enumerate(tokens):
        parts.extend(number_token(xs[index], 270, token, fill=colors[index % len(colors)]))
    parts.append(path("M180 390 C320 470 640 470 780 390", stroke=GREEN, sw=10))
    parts.append(text(480, 430, "READY", size=40))
    return parts


def scene_even_odd():
    parts = [card(70, 120, 380, 320), card(510, 120, 380, 320)]
    parts.append(text(260, 180, "8", size=52))
    parts.append(text(700, 180, "7", size=52))
    pair_positions = [(180, 250), (300, 250), (180, 340), (300, 340)]
    for x, y in pair_positions:
        parts.append(circle(x, y, 26, fill=TEAL))
        parts.append(circle(x + 48, y, 26, fill=TEAL))
    odd_positions = [(620, 250), (740, 250), (620, 340)]
    for x, y in odd_positions:
        parts.append(circle(x, y, 26, fill=CORAL))
        parts.append(circle(x + 48, y, 26, fill=CORAL))
    parts.append(circle(724, 340, 26, fill=YELLOW))
    return svg("even and odd numbers", parts)


def scene_multiplication():
    parts = [card(120, 110, 720, 340)]
    parts.extend(dot_grid(260, 180, cols=4, rows=3, radius=18, fill=TEAL))
    parts.append(text(480, 395, "3 x 4 = 12", size=50))
    return svg("multiplication array", parts)


def scene_pattern(values, step_label):
    parts = []
    xs = [120, 290, 460, 630, 800]
    for index, value in enumerate(values):
        fill = WHITE if value == "?" else [TEAL, CORAL, YELLOW, GREEN, BLUE][index]
        parts.append(rect(xs[index] - 60, 200, 120, 120, fill=fill, stroke=INK, sw=4, rx=24))
        parts.append(text(xs[index], 275, value, size=44))
        if index < len(values) - 1:
            parts.append(line(xs[index] + 72, 260, xs[index + 1] - 72, 260, marker=True))
            parts.append(text((xs[index] + xs[index + 1]) / 2, 222, step_label, size=22, fill=MUTED))
    return svg("number pattern", parts)


def scene_basic_shapes():
    parts = [card(90, 120, 220, 280), card(370, 120, 220, 280), card(650, 120, 220, 280)]
    parts.extend(basic_shape("triangle", 140, 180, 120, CORAL))
    parts.extend(basic_shape("square", 425, 170, 130, TEAL))
    parts.extend(basic_shape("circle", 710, 165, 130, YELLOW))
    return svg("basic shapes", parts)


def scene_division():
    parts = [card(100, 120, 760, 300)]
    box_xs = [180, 420, 660]
    for x in box_xs:
        parts.append(rect(x - 90, 250, 180, 110, fill=SAND, stroke=INK, sw=4, rx=22))
    points = [
        [(x - 45, 285), (x, 285), (x + 45, 285), (x - 22, 325)]
        for x in box_xs
    ]
    for bucket in points:
        for cx, cy in bucket:
            parts.append(circle(cx, cy, 16, fill=TEAL))
    return svg("division into equal groups", parts)


def scene_fraction(numerator, denominator):
    parts = [card(140, 140, 680, 240)]
    parts.extend(fraction_bar(220, 220, 520, 70, numerator, denominator))
    return svg("fraction bar", parts)


def scene_clock_calendar():
    parts = [card(90, 120, 360, 300), card(510, 120, 360, 300)]
    parts.extend(analog_clock(270, 270, 100, 3, 0))
    parts.extend(calendar(610, 170, 160, 180, "15"))
    return svg("time and calendar", parts)


def scene_money():
    parts = [card(100, 120, 760, 300)]
    parts.extend(money_note(160, 170, 200, 110, "1000", YELLOW))
    parts.extend(money_note(390, 170, 200, 110, "2000", TEAL))
    parts.extend(money_note(620, 170, 200, 110, "2000", CORAL))
    parts.append(text(480, 360, "1000 + 2000 + 2000 = 5000", size=34))
    return svg("money values", parts)


def scene_prime_grid():
    parts = []
    start_x = 150
    start_y = 160
    gap_x = 130
    gap_y = 110
    primes = {2, 3, 5, 7, 11}
    value = 1
    for row in range(3):
        for col in range(4):
            if value > 12:
                break
            fill = CORAL if value in primes else WHITE
            cx = start_x + col * gap_x
            cy = start_y + row * gap_y
            parts.extend(number_token(cx, cy, value, fill=fill))
            value += 1
    return svg("prime numbers", parts)


def scene_ucln_bcnn():
    parts = [card(90, 120, 360, 300), card(510, 120, 360, 300)]
    parts.extend(number_token(210, 190, "12", fill=TEAL))
    parts.extend(number_token(330, 190, "18", fill=CORAL))
    parts.append(text(270, 285, "UCLN", size=28, fill=MUTED))
    parts.extend(number_token(270, 340, "6", fill=YELLOW))
    parts.extend(number_token(630, 190, "12", fill=TEAL))
    parts.extend(number_token(750, 190, "18", fill=CORAL))
    parts.append(text(690, 285, "BCNN", size=28, fill=MUTED))
    parts.extend(number_token(690, 340, "36", fill=GREEN))
    return svg("ucln and bcnn", parts)


def scene_formula(main_text, sub_text=None, chips=None):
    size = 56 if len(main_text) <= 12 else 46 if len(main_text) <= 16 else 38
    parts = [card(120, 130, 720, 280), text(480, 265, main_text, size=size)]
    if sub_text:
        parts.append(text(480, 330, sub_text, size=28, fill=MUTED))
    if chips:
        xs = [300, 480, 660]
        for index, token in enumerate(chips):
            parts.extend(number_token(xs[index], 380, token, fill=[TEAL, CORAL, YELLOW][index % 3]))
    return svg(main_text, parts)


def scene_fraction_compare(left, right, relation):
    parts = [card(70, 150, 340, 240), card(550, 150, 340, 240)]
    parts.extend(fraction_bar(120, 220, 240, 60, left[0], left[1], fill=CORAL))
    parts.extend(fraction_bar(600, 220, 240, 60, right[0], right[1], fill=TEAL))
    parts.append(text(480, 290, relation, size=72))
    return svg("fraction comparison", parts)


def scene_decimal_fraction():
    parts = [card(120, 140, 720, 260)]
    parts.extend(fraction_bar(220, 210, 240, 70, 7, 10, fill=TEAL))
    parts.append(text(480, 265, "=", size=48))
    parts.append(text(650, 275, "0.7", size=62))
    return svg("decimal fraction", parts)


def scene_percent_relation():
    parts = [card(120, 130, 720, 280)]
    parts.extend(fraction_bar(190, 220, 220, 60, 3, 4, fill=TEAL))
    parts.append(text(480, 260, "=", size=48))
    parts.append(text(660, 275, "75%", size=64))
    return svg("fraction and percent", parts)


def scene_angles():
    def angle_arc(cx, cy, radius, degrees, stroke):
        points = []
        for step in range(13):
            portion = degrees * step / 12
            theta = -portion * pi / 180
            points.append((cx + cos(theta) * radius, cy + sin(theta) * radius))
        command = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in points)
        return path(command, stroke=stroke, sw=6)

    def angle_panel(x, y, w, h, label, degrees, color):
        cx = x + w / 2
        cy = y + h / 2 + 18
        radius = 34
        ray = 82
        theta = -degrees * pi / 180
        end_x = cx + cos(theta) * ray
        end_y = cy + sin(theta) * ray

        panel = [card(x, y, w, h, fill=WHITE)]
        panel.append(text(cx, y + 42, label, size=28))
        panel.append(line(cx, cy, cx + ray, cy, stroke=color, sw=8))
        panel.append(line(cx, cy, end_x, end_y, stroke=color, sw=8))
        panel.append(circle(cx, cy, 8, fill=INK, stroke=INK, sw=0))
        panel.append(angle_arc(cx, cy, radius, degrees, stroke=CORAL))
        panel.append(text(cx, y + h - 24, f"{degrees}\N{DEGREE SIGN}", size=28, fill=MUTED))
        return panel

    parts = []
    panels = [
        (70, 110, "Góc nhọn", 45, TEAL),
        (510, 110, "Góc vuông", 90, BLUE),
        (70, 300, "Góc tù", 120, CORAL),
        (510, 300, "Góc bẹt", 180, YELLOW),
    ]

    for x, y, label, degrees, color in panels:
        parts.extend(angle_panel(x, y, 380, 150, label, degrees, color))

    return svg("cac loai goc co ban", parts)


def scene_review(tokens):
    return svg("review", review_badges(tokens))


def scene_area_perimeter():
    parts = [card(140, 120, 680, 300)]
    parts.append(rect(300, 180, 360, 180, fill=TEAL, stroke=INK, sw=5, rx=20))
    parts.append(line(300, 170, 660, 170, stroke=CORAL, sw=5, marker=True))
    parts.append(line(670, 180, 670, 360, stroke=CORAL, sw=5, marker=True))
    parts.append(text(480, 280, "AREA", size=36, fill=WHITE))
    return svg("area and perimeter", parts)


def scene_big_number():
    parts = [card(140, 120, 680, 300)]
    boxes = [200, 360, 520, 680]
    labels = ["1", "000", "000", "000"]
    fills = [CORAL, TEAL, YELLOW, GREEN]
    for x, label, fill in zip(boxes, labels, fills):
        parts.append(rect(x - 70, 210, 140, 120, fill=fill, stroke=INK, sw=4, rx=18))
        parts.append(text(x, 285, label, size=40))
    return svg("big numbers", parts)


def scene_word_problem():
    parts = [card(100, 120, 760, 300)]
    parts.append(rect(160, 180, 220, 170, fill=WHITE, stroke=INK, sw=4, rx=22))
    parts.append(rect(580, 180, 220, 170, fill=WHITE, stroke=INK, sw=4, rx=22))
    parts.append(text(270, 240, "3 bags", size=36))
    parts.append(text(270, 295, "= 12", size=48))
    parts.append(text(690, 240, "1 bag", size=36))
    parts.append(text(690, 295, "= ?", size=48))
    parts.append(line(400, 265, 560, 265, marker=True))
    return svg("word problem", parts)


def scene_pascal():
    parts = []
    rows = [
        ["1"],
        ["1", "1"],
        ["1", "2", "1"],
        ["1", "3", "3", "1"],
        ["1", "4", "6", "4", "1"],
    ]
    start_y = 120
    for row_index, row in enumerate(rows):
        start_x = 480 - (len(row) - 1) * 65
        for col_index, value in enumerate(row):
            cx = start_x + col_index * 130
            cy = start_y + row_index * 80
            parts.extend(number_token(cx, cy, value, fill=[CORAL, TEAL, YELLOW, GREEN, BLUE][row_index]))
    return svg("pascal triangle", parts)


def scene_grid_puzzle():
    parts = [card(180, 110, 600, 320)]
    cell = 90
    origin_x = 240
    origin_y = 170
    values = [["1", "2", "3", "4"], ["3", "4", "1", "2"], ["2", "1", "4", "?"], ["4", "3", "2", "1"]]
    for row in range(4):
        for col in range(4):
            x = origin_x + col * cell
            y = origin_y + row * cell
            fill = YELLOW if values[row][col] == "?" else WHITE
            parts.append(rect(x, y, cell, cell, fill=fill, stroke=INK, sw=3, rx=8))
            parts.append(text(x + cell / 2, y + 58, values[row][col], size=34))
    return svg("grid puzzle", parts)


def scene_variable_box():
    parts = [card(140, 140, 680, 260)]
    parts.append(rect(260, 220, 110, 90, fill=TEAL, stroke=INK, sw=4, rx=16))
    parts.append(text(315, 278, "x", size=42))
    parts.append(text(430, 280, "+ 2 = 5", size=54, anchor="start"))
    return svg("variable", parts)


def scene_balance_equation():
    return svg("equation balance", balance_scale("x + 1", "4"))


def scene_direct_inverse():
    parts = [card(80, 120, 360, 300), card(520, 120, 360, 300)]
    parts.extend(number_token(200, 220, "2", fill=TEAL))
    parts.extend(number_token(320, 220, "4", fill=CORAL))
    parts.append(line(200, 300, 320, 300, marker=True))
    parts.append(text(260, 285, "up", size=22, fill=MUTED))
    parts.extend(number_token(640, 220, "2", fill=TEAL))
    parts.extend(number_token(760, 320, "1", fill=YELLOW))
    parts.append(line(640, 240, 760, 300, marker=True))
    parts.append(text(700, 260, "flip", size=22, fill=MUTED))
    return svg("direct and inverse proportion", parts)


def scene_percent_discount():
    parts = [card(140, 130, 680, 280)]
    parts.append(rect(220, 210, 180, 110, fill=WHITE, stroke=INK, sw=4, rx=20))
    parts.append(text(310, 282, "100", size=58))
    parts.append(text(480, 272, "-", size=58))
    parts.extend(number_token(580, 250, "25%", fill=CORAL))
    parts.append(text(730, 282, "75", size=58))
    return svg("percent application", parts)


def scene_shape_pair(left_name, right_name):
    parts = [card(90, 120, 340, 300), card(530, 120, 340, 300)]
    parts.extend(basic_shape(left_name, 180, 180, 160, CORAL))
    parts.extend(basic_shape(right_name, 620, 180, 160, TEAL))
    return svg("shape pair", parts)


def scene_measurement():
    parts = [card(90, 120, 360, 300), card(510, 120, 360, 300)]
    parts.append(rect(150, 250, 240, 36, fill=YELLOW, stroke=INK, sw=4, rx=10))
    for mark in range(0, 11):
        x = 160 + mark * 20
        parts.append(line(x, 250, x, 228 if mark % 5 == 0 else 238, sw=3))
    parts.append(rect(610, 210, 160, 120, fill=TEAL, stroke=INK, sw=4, rx=22))
    parts.append(text(690, 280, "kg", size=54))
    return svg("measurement units", parts)


def scene_data_chart():
    parts = [card(90, 120, 340, 300), card(530, 120, 340, 300)]
    for row in range(3):
        y = 190 + row * 70
        for mark in range(5):
            x = 150 + mark * 28
            parts.append(line(x, y, x, y + 42, sw=6, stroke=TEAL))
        parts.append(line(150, y + 42, 262, y, sw=6, stroke=CORAL))
    base_x = 610
    values = [90, 150, 120]
    fills = [CORAL, TEAL, YELLOW]
    for index, value in enumerate(values):
        x = base_x + index * 70
        parts.append(rect(x, 360 - value, 48, value, fill=fills[index], stroke=INK, sw=4, rx=10))
    parts.append(line(580, 360, 820, 360, sw=6))
    return svg("data to chart", parts)


def scene_square_numbers():
    parts = [card(120, 130, 720, 280)]
    squares = [(230, 210, 1, CORAL), (420, 185, 2, TEAL), (650, 160, 3, YELLOW)]
    for x, y, side, fill in squares:
        size = 40
        for row in range(side):
            for col in range(side):
                parts.append(rect(x + col * (size + 8), y + row * (size + 8), size, size, fill=fill, stroke=INK, sw=3, rx=8))
        parts.append(text(x + side * 24, y + side * (size + 8) + 50, side * side, size=34))
    return svg("square numbers", parts)


def scene_factor_pairs():
    parts = [card(140, 130, 680, 280)]
    parts.extend(number_token(480, 210, "12", fill=TEAL))
    pairs = [("1", "12"), ("2", "6"), ("3", "4")]
    ys = [320, 320, 320]
    xs = [(250, 360), (440, 520), (610, 700)]
    fills = [CORAL, YELLOW, GREEN]
    for index, ((left, right), (x1, x2)) in enumerate(zip(pairs, xs)):
        parts.extend(number_token(x1, ys[index], left, fill=fills[index]))
        parts.extend(number_token(x2, ys[index], right, fill=fills[index]))
        parts.append(text((x1 + x2) / 2, ys[index] + 12, "x", size=28))
    return svg("factor pairs", parts)


def scene_lcm_rows():
    parts = [card(110, 130, 740, 280)]
    top = [4, 8, 12]
    bottom = [6, 12, 18]
    for index, value in enumerate(top):
        parts.extend(number_token(220 + index * 170, 220, value, fill=TEAL if value != 12 else GREEN))
    for index, value in enumerate(bottom):
        parts.extend(number_token(220 + index * 170, 340, value, fill=CORAL if value != 12 else GREEN))
    return svg("least common multiple", parts)


def scene_equivalent_fractions():
    parts = [card(70, 150, 340, 240), card(550, 150, 340, 240)]
    parts.extend(fraction_bar(120, 220, 240, 60, 1, 2, fill=CORAL))
    parts.extend(fraction_bar(600, 220, 240, 60, 2, 4, fill=TEAL))
    parts.append(text(480, 290, "=", size=72))
    return svg("equivalent fractions", parts)


def scene_fraction_add():
    parts = [card(90, 140, 780, 260)]
    parts.extend(fraction_bar(130, 220, 180, 55, 1, 4, fill=CORAL))
    parts.extend(fraction_bar(390, 220, 180, 55, 2, 4, fill=TEAL))
    parts.extend(fraction_bar(650, 220, 180, 55, 3, 4, fill=YELLOW))
    parts.append(text(350, 265, "+", size=44))
    parts.append(text(610, 265, "=", size=44))
    return svg("fraction addition", parts)


def scene_mixed_number():
    parts = [card(140, 140, 680, 260)]
    parts.extend(fraction_bar(210, 230, 170, 55, 4, 4, fill=TEAL))
    parts.extend(fraction_bar(440, 230, 170, 55, 2, 4, fill=CORAL))
    parts.append(text(700, 275, "1 1/2", size=56))
    return svg("mixed number", parts)


def scene_ratio():
    parts = [card(140, 130, 680, 280)]
    for index in range(2):
        parts.append(circle(290 + index * 70, 260, 30, fill=CORAL))
    for index in range(3):
        parts.append(circle(560 + index * 70, 260, 30, fill=TEAL))
    parts.append(text(480, 275, "2 : 3", size=54))
    return svg("ratio", parts)


def scene_volume():
    parts = [card(160, 110, 640, 320)]
    cubes = [
        (320, 290), (390, 290), (460, 290),
        (355, 230), (425, 230),
        (390, 170),
    ]
    for x, y in cubes:
        parts.append(rect(x, y, 70, 70, fill=TEAL, stroke=INK, sw=4, rx=10))
        parts.append(line(x, y, x + 25, y - 20, sw=3))
        parts.append(line(x + 70, y, x + 95, y - 20, sw=3))
        parts.append(line(x + 95, y - 20, x + 95, y + 50, sw=3))
        parts.append(line(x + 25, y - 20, x + 95, y - 20, sw=3))
    return svg("volume cubes", parts)


def scene_spinner():
    parts = [card(180, 110, 600, 320)]
    parts.append(circle(480, 270, 120, fill=WHITE))
    parts.append(path("M480 270 L480 150 A120 120 0 0 1 594 222 z", fill=CORAL, stroke=INK, sw=4))
    parts.append(path("M480 270 L594 222 A120 120 0 0 1 480 390 z", fill=TEAL, stroke=INK, sw=4))
    parts.append(path("M480 270 L480 390 A120 120 0 0 1 366 222 z", fill=YELLOW, stroke=INK, sw=4))
    parts.append(path("M480 270 L366 222 A120 120 0 0 1 480 150 z", fill=GREEN, stroke=INK, sw=4))
    parts.append(line(480, 100, 480, 190, stroke=INK, sw=8, marker=True))
    return svg("probability spinner", parts)


def scene_statistics():
    parts = [card(90, 120, 340, 300), card(530, 120, 340, 300)]
    faces = [("A", 2), ("B", 4), ("C", 3)]
    for index, (label, count) in enumerate(faces):
        y = 190 + index * 75
        parts.append(text(150, y + 18, label, size=28))
        for dot in range(count):
            parts.append(circle(220 + dot * 40, y, 16, fill=TEAL))
    values = [80, 150, 110]
    fills = [CORAL, TEAL, YELLOW]
    for index, value in enumerate(values):
        x = 610 + index * 70
        parts.append(rect(x, 360 - value, 48, value, fill=fills[index], stroke=INK, sw=4, rx=10))
    parts.append(line(580, 360, 820, 360, sw=6))
    return svg("statistics", parts)


def scene_bar_chart():
    parts = [card(150, 110, 660, 320)]
    values = [120, 190, 150]
    fills = [TEAL, CORAL, YELLOW]
    for index, value in enumerate(values):
        x = 260 + index * 150
        parts.append(rect(x, 380 - value, 90, value, fill=fills[index], stroke=INK, sw=4, rx=14))
    parts.append(line(220, 380, 760, 380, sw=8))
    return svg("bar chart", parts)


def scene_binary():
    parts = [card(120, 130, 720, 280)]
    weights = [8, 4, 2, 1]
    bits = [1, 0, 1, 1]
    for index, (weight, bit) in enumerate(zip(weights, bits)):
        x = 200 + index * 150
        fill = TEAL if bit else WHITE
        parts.append(rect(x, 190, 100, 100, fill=fill, stroke=INK, sw=4, rx=18))
        parts.append(text(x + 50, 250, bit, size=44))
        parts.append(text(x + 50, 330, weight, size=26, fill=MUTED))
    parts.append(text(480, 410, "1011 = 11", size=46))
    return svg("binary numbers", parts)


def scene_sphere_cone():
    parts = [card(90, 120, 340, 300), card(530, 120, 340, 300)]
    parts.extend(sphere(260, 270, 95))
    parts.extend(cone(700, 270, 150, 200))
    return svg("sphere and cone", parts)


def scene_cylinder():
    parts = [card(180, 110, 600, 320)]
    parts.extend(cylinder(480, 270, 220, 220))
    parts.append(line(630, 160, 630, 380, stroke=CORAL, sw=5, marker=True))
    parts.append(text(670, 285, "h", size=34, fill=MUTED))
    return svg("cylinder", parts)


def render_all():
    outputs = {
        "img/chapter_img/chapter01/03_even_vs_odd.svg": scene_even_odd(),
        "img/chapter_img/chapter01/01_03_phep_nhan.svg": scene_multiplication(),
        "img/chapter_img/chapter01/01_04_suy_luan.svg": scene_pattern(["2", "4", "6", "?", "10"], "+2"),
        "img/chapter_img/chapter01/01_05_hinh_hoc.svg": scene_basic_shapes(),
        "img/chapter_img/chapter01/01_06_phep_chia.svg": scene_division(),
        "img/chapter_img/chapter01/01_07_phan_so.svg": scene_fraction(3, 4),
        "img/chapter_img/chapter01/01_08_thoi_gian.svg": scene_clock_calendar(),
        "img/chapter_img/chapter01/01_09_tien.svg": scene_money(),
        "img/chapter_img/chapter02/02_01_so_nguyen_to.svg": scene_prime_grid(),
        "img/chapter_img/chapter02/02_02_ucln_bcnn.svg": scene_ucln_bcnn(),
        "img/chapter_img/chapter02/02_03_nhan_nhanh.svg": scene_formula("9 x 6 = 54", "10 x 6 - 6"),
        "img/chapter_img/chapter02/02_04_chia_nhanh.svg": scene_formula("14 : 4 = 3 du 2"),
        "img/chapter_img/chapter02/02_05_tinh_chat.svg": scene_formula("4 + 7 = 7 + 4"),
        "img/chapter_img/chapter02/02_06_phan_so_nang_cao.svg": scene_fraction_compare((3, 4), (2, 4), ">"),
        "img/chapter_img/chapter02/02_07_so_thap_phan.svg": scene_formula("3.6 = 3 + 6/10"),
        "img/chapter_img/chapter02/02_08_ti_le_phan_tram.svg": scene_percent_relation(),
        "img/chapter_img/chapter02/02_09_goc_duong_thang.svg": scene_angles(),
        "img/chapter_img/chapter02/02_10_on_tap_kiem_tra.svg": scene_review(["+", "1/2", "90"]),
        "img/chapter_img/chapter03/03_01_toan_tu_duy.svg": scene_pattern(["3", "6", "9", "?", "15"], "+3"),
        "img/chapter_img/chapter03/03_02_dien_tich_nang_cao.svg": scene_area_perimeter(),
        "img/chapter_img/chapter03/03_03_so_lon.svg": scene_big_number(),
        "img/chapter_img/chapter03/03_04_bai_toan_do.svg": scene_word_problem(),
        "img/chapter_img/chapter03/03_05_tam_giac_pascal.svg": scene_pascal(),
        "img/chapter_img/chapter03/03_06_luoi_so.svg": scene_grid_puzzle(),
        "img/chapter_img/chapter03/03_07_tim_quy_luat.svg": scene_pattern(["5", "10", "15", "?", "25"], "+5"),
        "img/chapter_img/chapter03/03_08_toan_vui.svg": scene_formula("2 + 3 + 4 = ?", chips=["2", "3", "4"]),
        "img/chapter_img/chapter03/03_09_fibonacci.svg": scene_pattern(["1", "1", "2", "3", "5"], "+"),
        "img/chapter_img/chapter03/03_10_on_tap.svg": scene_review(["?", "123", "grid"]),
        "img/chapter_img/chapter04/04_01_dai_so_bien_so.svg": scene_variable_box(),
        "img/chapter_img/chapter04/04_02_phuong_trinh.svg": scene_balance_equation(),
        "img/chapter_img/chapter04/04_03_phan_so_thap_phan.svg": scene_decimal_fraction(),
        "img/chapter_img/chapter04/04_04_ty_le_thuan_nghich.svg": scene_direct_inverse(),
        "img/chapter_img/chapter04/04_05_phan_tram_ung_dung.svg": scene_percent_discount(),
        "img/chapter_img/chapter04/04_06_hinh_hoc_hinh_tam_giac_hinh_vuong.svg": scene_shape_pair("triangle", "square"),
        "img/chapter_img/chapter04/04_07_do_luong_don_vi_do_dai_khoi_luong.svg": scene_measurement(),
        "img/chapter_img/chapter04/04_08_thoi_gian_xem_dong_ho_va_lich.svg": scene_clock_calendar(),
        "img/chapter_img/chapter04/04_09_du_lieu_thu_thap_va_bieu_dien_thong_tin.svg": scene_data_chart(),
        "img/chapter_img/chapter04/04_10_on_tap_tong_ket_chuong_4.svg": scene_review(["x", "%", "kg"]),
        "img/chapter_img/chapter05/01_square_numbers.svg": scene_square_numbers(),
        "img/chapter_img/chapter05/02_factors_multiples.svg": scene_factor_pairs(),
        "img/chapter_img/chapter05/03_prime_numbers.svg": scene_prime_grid(),
        "img/chapter_img/chapter05/04_gcf.svg": scene_formula("12 & 18 -> 6"),
        "img/chapter_img/chapter05/05_lcm.svg": scene_lcm_rows(),
        "img/chapter_img/chapter05/06_equivalent_fractions.svg": scene_equivalent_fractions(),
        "img/chapter_img/chapter05/07_comparing_fractions.svg": scene_fraction_compare((3, 4), (2, 4), ">"),
        "img/chapter_img/chapter05/08_add_subtract_fractions.svg": scene_fraction_add(),
        "img/chapter_img/chapter05/09_mixed_numbers.svg": scene_mixed_number(),
        "img/chapter_img/chapter05/10_chapter5_review.svg": scene_review(["9", "1/2", "12"]),
        "img/chapter_img/chapter06/01_decimal_numbers.svg": scene_formula("4.2 = 4 + 2/10"),
        "img/chapter_img/chapter06/02_add_subtract_decimals.svg": scene_formula("2.5 + 1.2 = 3.7"),
        "img/chapter_img/chapter06/03_multiply_divide_decimals.svg": scene_formula("0.5 x 4 = 2"),
        "img/chapter_img/chapter06/04_ratios_proportions.svg": scene_ratio(),
        "img/chapter_img/chapter06/05_direct_inverse_proportion.svg": scene_direct_inverse(),
        "img/chapter_img/chapter06/06_rectangle_parallelogram.svg": scene_shape_pair("rectangle", "parallelogram"),
        "img/chapter_img/chapter06/07_rhombus_trapezoid.svg": scene_shape_pair("rhombus", "trapezoid"),
        "img/chapter_img/chapter06/08_area_circle_triangle.svg": scene_shape_pair("circle", "triangle"),
        "img/chapter_img/chapter06/09_volume.svg": scene_volume(),
        "img/chapter_img/chapter06/10_chapter6_review.svg": scene_review(["0.5", "2:3", "cube"]),
        "img/chapter_img/chapter07/01_probability.svg": scene_spinner(),
        "img/chapter_img/chapter07/02_statistics.svg": scene_statistics(),
        "img/chapter_img/chapter07/03_charts.svg": scene_bar_chart(),
        "img/chapter_img/chapter07/04_equations.svg": scene_formula("2x + 3 = 11"),
        "img/chapter_img/chapter07/05_percent.svg": scene_formula("40% = 40/100"),
        "img/chapter_img/chapter07/06_sphere_cone.svg": scene_sphere_cone(),
        "img/chapter_img/chapter07/07_cylinder.svg": scene_cylinder(),
        "img/chapter_img/chapter07/08_sequences.svg": scene_pattern(["4", "7", "10", "13", "?"], "+3"),
        "img/chapter_img/chapter07/09_binary.svg": scene_binary(),
        "img/chapter_img/chapter07/10_chapter7_review.svg": scene_review(["%", "bar", "101"]),
    }
    for relative_path, content in outputs.items():
        save(relative_path, content)
    print(f"Generated {len(outputs)} SVG illustrations.")


if __name__ == "__main__":
    render_all()
