#!/usr/bin/env python3
"""Generate local SVGs for optional modern-application lessons."""

from __future__ import annotations

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from generate_child_friendly_svgs import (  # noqa: E402
    CORAL,
    GREEN,
    INK,
    MUTED,
    TEAL,
    WHITE,
    YELLOW,
    card,
    circle,
    line,
    number_token,
    rect,
    save,
    svg,
    text,
)


def scene_on_off_pairs():
    parts = [card(80, 110, 800, 320)]
    parts.append(text(480, 170, "Even number = complete on/off pairs", size=28))
    for index, (bit, label) in enumerate([(1, "on"), (0, "off"), (1, "on"), (0, "off")]):
        x = 160 + index * 170
        fill = TEAL if bit else WHITE
        parts.append(rect(x, 210, 120, 120, fill=fill, stroke=INK, sw=4, rx=20))
        parts.append(text(x + 60, 280, bit, size=46))
        parts.append(text(x + 60, 380, label, size=22, fill=MUTED))
    return svg("even odd computer switches", parts)


def scene_repeat_loop():
    parts = [card(90, 100, 780, 340)]
    parts.append(text(480, 160, "Repeat 4 times: add 5", size=32))
    values = [0, 5, 10, 15, 20]
    for index, value in enumerate(values):
        x = 160 + index * 140
        fill = TEAL if index else YELLOW
        parts.extend(number_token(x, 270, value, fill=fill))
        if index < len(values) - 1:
            parts.append(line(x + 40, 270, x + 100, 270, marker=True))
    parts.append(text(480, 390, "A coding loop is skip counting with a start button", size=24, fill=MUTED))
    return svg("skip counting coding loop", parts)


def scene_score_variable():
    parts = [card(120, 110, 720, 320)]
    parts.append(rect(200, 180, 220, 160, fill=YELLOW, stroke=INK, sw=4, rx=22))
    parts.append(text(310, 250, "score", size=34))
    parts.append(text(310, 310, "7", size=54))
    parts.append(text(520, 250, "catch star", size=28, fill=MUTED, anchor="start"))
    parts.append(text(520, 310, "score = score + 1", size=28, anchor="start"))
    parts.append(text(480, 390, "The box remembers a number that can change", size=24, fill=MUTED))
    return svg("score variable in a game", parts)


def scene_progress_bar():
    parts = [card(110, 120, 740, 300)]
    parts.append(text(480, 180, "Download bar: 3 of 4 equal parts", size=30))
    parts.append(rect(180, 230, 600, 80, fill=WHITE, stroke=INK, sw=4, rx=18))
    parts.append(rect(180, 230, 450, 80, fill=TEAL, stroke=INK, sw=4, rx=18))
    parts.append(text(480, 280, "3 / 4", size=36, fill=INK))
    parts.append(text(480, 370, "Same fraction as three pizza slices of four", size=24, fill=MUTED))
    return svg("fraction progress bar", parts)


def scene_number_lock():
    parts = [card(80, 100, 800, 340)]
    parts.append(text(480, 160, "Two game events meet again at the LCM", size=28))
    for index, value in enumerate([4, 8, 12, 16]):
        parts.extend(number_token(170 + index * 90, 250, value, fill=TEAL if value != 12 else GREEN))
    for index, value in enumerate([6, 12, 18]):
        parts.extend(number_token(170 + index * 90, 360, value, fill=CORAL if value != 12 else GREEN))
    parts.append(rect(620, 210, 200, 180, fill=YELLOW, stroke=INK, sw=4, rx=22))
    parts.append(text(720, 280, "lock", size=28))
    parts.append(text(720, 340, "12", size=48))
    return svg("number lock and shared multiples", parts)


def scene_map_scale():
    parts = [card(90, 110, 780, 320)]
    parts.append(text(480, 170, "Map scale 1 cm : 100 m", size=32))
    parts.append(rect(160, 230, 200, 16, fill=CORAL, stroke=INK, sw=3, rx=6))
    parts.append(text(260, 290, "3 cm on paper", size=24))
    parts.append(line(400, 238, 520, 238, marker=True))
    parts.append(rect(560, 214, 240, 50, fill=TEAL, stroke=INK, sw=4, rx=14))
    parts.append(text(680, 248, "300 m walk", size=26))
    parts.append(text(480, 380, "Keep the ratio. Change the size.", size=26, fill=MUTED))
    return svg("map scale ratio", parts)


def scene_data_bits():
    parts = [card(70, 100, 820, 340)]
    parts.append(text(270, 160, "News chart", size=26))
    values = [90, 150, 110]
    fills = [CORAL, TEAL, YELLOW]
    for index, value in enumerate(values):
        x = 140 + index * 80
        parts.append(rect(x, 360 - value, 50, value, fill=fills[index], stroke=INK, sw=4, rx=10))
    parts.append(line(120, 360, 380, 360, sw=6))
    parts.append(circle(560, 250, 70, fill=YELLOW, stroke=INK, sw=4))
    parts.append(text(560, 260, "H / T", size=28))
    parts.append(text(560, 360, "1 of 2", size=24, fill=MUTED))
    for index, bit in enumerate([1, 0, 1]):
        x = 700 + (index % 1) * 0
        y = 180 + index * 80
        fill = TEAL if bit else WHITE
        parts.append(rect(700, y, 70, 60, fill=fill, stroke=INK, sw=4, rx=12))
        parts.append(text(735, y + 42, bit, size=30))
    parts.append(text(735, 430, "bits", size=22, fill=MUTED))
    return svg("data chance and computer bits", parts)


def scene_character_combos():
    parts = [card(80, 100, 800, 340)]
    parts.append(text(480, 160, "Hats 2  x  shirts 3  =  6 outfits", size=30))
    hats = ["A", "B"]
    shirts = ["1", "2", "3"]
    for index, hat in enumerate(hats):
        parts.extend(number_token(180, 230 + index * 90, hat, fill=YELLOW))
    for index, shirt in enumerate(shirts):
        parts.extend(number_token(400, 210 + index * 80, shirt, fill=TEAL))
    total = 0
    for hat_index, _hat in enumerate(hats):
        for shirt_index, _shirt in enumerate(shirts):
            x = 620 + (total % 3) * 70
            y = 210 + (total // 3) * 90
            parts.append(rect(x - 24, y - 24, 48, 48, fill=CORAL, stroke=INK, sw=3, rx=10))
            parts.append(text(x, y + 8, str(total + 1), size=20))
            total += 1
    return svg("counting choices in games", parts)


def render_all():
    mapping = {
        "img/chapter_img/chapter01/90_even_odd_computer.svg": scene_on_off_pairs(),
        "img/chapter_img/chapter02/90_skip_loop.svg": scene_repeat_loop(),
        "img/chapter_img/chapter03/90_score_variable.svg": scene_score_variable(),
        "img/chapter_img/chapter04/90_progress_bar.svg": scene_progress_bar(),
        "img/chapter_img/chapter05/90_number_lock.svg": scene_number_lock(),
        "img/chapter_img/chapter06/90_map_scale.svg": scene_map_scale(),
        "img/chapter_img/chapter07/90_data_bits.svg": scene_data_bits(),
        "img/chapter_img/chapter09/90_character_combos.svg": scene_character_combos(),
    }
    for relative_path, content in mapping.items():
        save(relative_path, content)
        print(f"Created {relative_path}")


if __name__ == "__main__":
    render_all()
