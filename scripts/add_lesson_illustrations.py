#!/usr/bin/env python3
"""Add Wikimedia illustrations to lesson posts that lack them.

Matches topic keywords from title/filename/body to curated image URLs,
then inserts 2–4 images at hook, core, activity, and example sections.
"""

from __future__ import annotations

import argparse
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENTS = ROOT / "contents"

WIKIMEDIA_MARKER = "upload.wikimedia.org"
MIN_EXISTING = 2
TARGET_IMAGES = 3
TITLE_BOOST = 20
FILENAME_BOOST = 10

WIKIMEDIA_BLOCK_RE = re.compile(
    r"\n*!\[[^\]]*\]\(https://upload\.wikimedia\.org[^)]+\)\s*\n+"
    r"\*(?:Ảnh|Image):[^\n]+\*\s*\n",
    re.MULTILINE,
)


@dataclass(frozen=True)
class LessonImage:
    key: str
    url: str
    alt_vi: str
    alt_en: str
    math_diagram: bool


# Verified Wikimedia URLs (HTTP 200 with User-Agent)
IMAGES: dict[str, LessonImage] = {
    # Chapter 01 — patterns
    "even_odd_line": LessonImage(
        "even_odd_line",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/EvenOddNumberLine.svg/960px-EvenOddNumberLine.svg.png",
        "Trục số — số chẵn và số lẻ",
        "Number line showing even and odd numbers",
        True,
    ),
    "powers_chart": LessonImage(
        "powers_chart",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Powers_chart.png/960px-Powers_chart.png",
        "Bảng lũy thừa — nhân đôi từng bước",
        "Powers chart — multiply by 2 each step",
        True,
    ),
    "triangular": LessonImage(
        "triangular",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Triangular_number_10_with_triangle.svg/960px-Triangular_number_10_with_triangle.svg.png",
        "Số tam giác — xếp chấm thành tam giác",
        "Triangular number dot pattern",
        True,
    ),
    "square_numbers": LessonImage(
        "square_numbers",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Square_number_16_as_sum_of_two_triangular_numbers.svg/960px-Square_number_16_as_sum_of_two_triangular_numbers.svg.png",
        "Số chính phương 1, 4, 9, 16…",
        "Square numbers visual pattern",
        True,
    ),
    "arithmetic_progression": LessonImage(
        "arithmetic_progression",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Academ_Arithmetic_progressions_along_a_knotted_loop.svg/960px-Academ_Arithmetic_progressions_along_a_knotted_loop.svg.png",
        "Cấp số cộng — tăng đều từng bước",
        "Arithmetic progression diagram",
        True,
    ),
    "fibonacci_rabbits": LessonImage(
        "fibonacci_rabbits",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Fibonacci_Rabbits_mk.svg/960px-Fibonacci_Rabbits_mk.svg.png",
        "Dãy Fibonacci — bài toán thỏ đẻ",
        "Fibonacci rabbits diagram",
        True,
    ),
    "fibonacci_spiral": LessonImage(
        "fibonacci_spiral",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Fibonacci_spiral_2019.svg/960px-Fibonacci_spiral_2019.svg.png",
        "Xoắn ốc Fibonacci",
        "Fibonacci spiral diagram",
        True,
    ),
    "pascal_triangle": LessonImage(
        "pascal_triangle",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Pascal_triangle.svg/960px-Pascal_triangle.svg.png",
        "Tam giác Pascal — mẫu hình số",
        "Pascal's triangle diagram",
        True,
    ),
    "binary": LessonImage(
        "binary",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Binary_decomposition.png/960px-Binary_decomposition.png",
        "Phân rã nhị phân — toán trong máy tính",
        "Binary decomposition diagram",
        True,
    ),
    "number_line": LessonImage(
        "number_line",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Number_line.svg/960px-Number_line.svg.png",
        "Trục số — thứ tự các số",
        "Number line diagram",
        True,
    ),
    "abacus": LessonImage(
        "abacus",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Abacus.svg/960px-Abacus.svg.png",
        "Bàn tính — cộng trừ nhanh",
        "Abacus math tool",
        True,
    ),
    "panzhu_addition": LessonImage(
        "panzhu_addition",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Panzhu_Suanfa_addition_diagrams.png/960px-Panzhu_Suanfa_addition_diagrams.png",
        "Sơ đồ cộng nhanh trên bàn tính",
        "Abacus addition diagram",
        True,
    ),
    "sieve_primes": LessonImage(
        "sieve_primes",
        "https://upload.wikimedia.org/wikipedia/commons/e/eb/Sieve_of_Eratosthenes.gif",
        "Sàng Eratosthenes — lọc số nguyên tố",
        "Sieve of Eratosthenes animation",
        True,
    ),
    "balance_scale": LessonImage(
        "balance_scale",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Balance_scale.svg/960px-Balance_scale.svg.png",
        "Cân đĩa — hai vế bằng nhau",
        "Balance scale for equations",
        True,
    ),
    # Geometry diagrams
    "circle": LessonImage(
        "circle",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Circle.svg/960px-Circle.svg.png",
        "Hình tròn — tất cả điểm cách tâm bằng nhau",
        "Circle geometry diagram",
        True,
    ),
    "square_shape": LessonImage(
        "square_shape",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Square_%28geometry%29.svg/960px-Square_%28geometry%29.svg.png",
        "Hình vuông — bốn cạnh bằng nhau",
        "Square geometry diagram",
        True,
    ),
    "rectangle": LessonImage(
        "rectangle",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Rectangle.svg/960px-Rectangle.svg.png",
        "Hình chữ nhật",
        "Rectangle geometry diagram",
        True,
    ),
    "triangle": LessonImage(
        "triangle",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Triangle.svg/960px-Triangle.svg.png",
        "Hình tam giác",
        "Triangle geometry diagram",
        True,
    ),
    "equilateral": LessonImage(
        "equilateral",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Equilateral_triangle.svg/960px-Equilateral_triangle.svg.png",
        "Tam giác đều — ba cạnh bằng nhau",
        "Equilateral triangle diagram",
        True,
    ),
    "parallelogram": LessonImage(
        "parallelogram",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Parallelogram.svg/960px-Parallelogram.svg.png",
        "Hình bình hành",
        "Parallelogram diagram",
        True,
    ),
    "rhombus": LessonImage(
        "rhombus",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Rhombus.svg/960px-Rhombus.svg.png",
        "Hình thoi",
        "Rhombus diagram",
        True,
    ),
    "trapezoid": LessonImage(
        "trapezoid",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Trapezoid.svg/960px-Trapezoid.svg.png",
        "Hình thang",
        "Trapezoid diagram",
        True,
    ),
    "cube": LessonImage(
        "cube",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Cube.svg/960px-Cube.svg.png",
        "Hình lập phương — khối 3D",
        "Cube 3D shape",
        True,
    ),
    "sphere": LessonImage(
        "sphere",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Sphere.svg/960px-Sphere.svg.png",
        "Hình cầu",
        "Sphere 3D shape",
        True,
    ),
    "cone": LessonImage(
        "cone",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Cone_%28geometry%29.svg/960px-Cone_%28geometry%29.svg.png",
        "Hình nón",
        "Cone 3D shape",
        True,
    ),
    # Stats / probability
    "bar_chart": LessonImage(
        "bar_chart",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Bar_chart.svg/960px-Bar_chart.svg.png",
        "Biểu đồ cột — so sánh dữ liệu",
        "Bar chart diagram",
        True,
    ),
    "pie_chart": LessonImage(
        "pie_chart",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Pie_chart.svg/960px-Pie_chart.svg.png",
        "Biểu đồ tròn — phần trăm",
        "Pie chart for percentages",
        True,
    ),
    "dice": LessonImage(
        "dice",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Dice.svg/960px-Dice.svg.png",
        "Xúc xắc — thí nghiệm xác suất",
        "Dice for probability",
        True,
    ),
    # Real-world photos
    "crayons": LessonImage(
        "crayons",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Bellen%27s_More_than_Peach_Multicultural_Crayons_-_DPLA_-_927cf31c64d28975ac993f8d433722c9_%28page_1%29.jpg/960px-Bellen%27s_More_than_Peach_Multicultural_Crayons_-_DPLA_-_927cf31c64d28975ac993f8d433722c9_%28page_1%29.jpg",
        "Bút màu để chia đều",
        "Colorful crayons for sharing",
        False,
    ),
    "socks": LessonImage(
        "socks",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/BLW_Pair_of_socks.jpg/960px-BLW_Pair_of_socks.jpg",
        "Đôi tất ghép cặp",
        "Pair of socks",
        False,
    ),
    "buttons": LessonImage(
        "buttons",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Plastic_buttons_20190306.jpg/960px-Plastic_buttons_20190306.jpg",
        "Nút áo nhiều màu",
        "Colorful buttons",
        False,
    ),
    "cherries": LessonImage(
        "cherries",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Sweet_cherries_in_basket_2018_G1.jpg/960px-Sweet_cherries_in_basket_2018_G1.jpg",
        "Chùm cherry để chia đều",
        "Cherries in a basket",
        False,
    ),
    "grapes": LessonImage(
        "grapes",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/DFC_3937_Bunches_of_plump_juicy_red_grapes_piled_together_ready_to_snack_on.jpg/960px-DFC_3937_Bunches_of_plump_juicy_red_grapes_piled_together_ready_to_snack_on.jpg",
        "Chùm nho đỏ",
        "Red grapes bunch",
        False,
    ),
    "eggs": LessonImage(
        "eggs",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/A_Basket_of_Brown_Eggs_at_Gold_Coast_Prime_Rib.jpg/960px-A_Basket_of_Brown_Eggs_at_Gold_Coast_Prime_Rib.jpg",
        "Giỏ trứng — bài toán trừ",
        "Basket of brown eggs",
        False,
    ),
    "market_vn": LessonImage(
        "market_vn",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Safe_vegetables_in_Vietnam_VOA.jpg/960px-Safe_vegetables_in_Vietnam_VOA.jpg",
        "Chợ rau quả Việt Nam",
        "Vegetable market in Vietnam",
        False,
    ),
    "vegetables_shop": LessonImage(
        "vegetables_shop",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Vegetables_shop.jpg/960px-Vegetables_shop.jpg",
        "Quầy rau củ tại chợ",
        "Vegetables shop stall",
        False,
    ),
    "market_scene": LessonImage(
        "market_scene",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Market_scene_with_shoppers_browsing_vegetables_and_fruits_in_an_outdoor_market_undefined.jpg/960px-Market_scene_with_shoppers_browsing_vegetables_and_fruits_in_an_outdoor_market_undefined.jpg",
        "Chợ ngoài trời — mua bán hằng ngày",
        "Outdoor market scene",
        False,
    ),
    "earth": LessonImage(
        "earth",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/The_Earth_seen_from_Apollo_17.jpg/960px-The_Earth_seen_from_Apollo_17.jpg",
        "Trái đất — số lớn trong vũ trụ",
        "Earth from space",
        False,
    ),
    "moon": LessonImage(
        "moon",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/A_New_View_of_the_Moon.jpg/960px-A_New_View_of_the_Moon.jpg",
        "Mặt trăng — khoảng cách và số lớn",
        "The Moon",
        False,
    ),
    "city_lights": LessonImage(
        "city_lights",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/City_Lights_of_Asia_and_Middle_East_2016.png/960px-City_Lights_of_Asia_and_Middle_East_2016.png",
        "Đèn thành phố — hàng triệu người",
        "City lights at night",
        False,
    ),
    "children": LessonImage(
        "children",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Children_Learning_Together.jpg/960px-Children_Learning_Together.jpg",
        "Hai bạn cùng học và chia sẻ",
        "Children learning together",
        False,
    ),
    "soccer": LessonImage(
        "soccer",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Soccer_ball.svg/960px-Soccer_ball.svg.png",
        "Quả bóng đá — toán trong thể thao",
        "Soccer ball",
        False,
    ),
    "basketball": LessonImage(
        "basketball",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Kent_Benson_attempts_a_hook_shot_over_Ken_Ferdinand.jpg/960px-Kent_Benson_attempts_a_hook_shot_over_Ken_Ferdinand.jpg",
        "Bóng rổ — tính điểm và tỷ số",
        "Basketball game action",
        False,
    ),
    "cooking": LessonImage(
        "cooking",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Cooking_food.jpg/960px-Cooking_food.jpg",
        "Nấu ăn — đo lường nguyên liệu",
        "Cooking food in kitchen",
        False,
    ),
    "shopping_cart": LessonImage(
        "shopping_cart",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Shopping_cart.jpg/960px-Shopping_cart.jpg",
        "Giỏ hàng — toán khi mua sắm",
        "Shopping cart",
        False,
    ),
    "traffic": LessonImage(
        "traffic",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Traffic_light.jpg/960px-Traffic_light.jpg",
        "Đèn giao thông — toán trong giao thông",
        "Traffic light",
        False,
    ),
    "road": LessonImage(
        "road",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Road_in_Pyongyang.jpg/960px-Road_in_Pyongyang.jpg",
        "Con đường — khoảng cách và tốc độ",
        "Road for distance math",
        False,
    ),
    "laptop_code": LessonImage(
        "laptop_code",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Programming_code.jpg/960px-Programming_code.jpg",
        "Mã lập trình — toán trong tin học",
        "Programming code on screen",
        False,
    ),
    "camera": LessonImage(
        "camera",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Camera.jpg/960px-Camera.jpg",
        "Máy ảnh — toán trong phim ảnh",
        "Camera for film math",
        False,
    ),
    "cloud_weather": LessonImage(
        "cloud_weather",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Cloud.jpg/960px-Cloud.jpg",
        "Mây trời — dự báo thời tiết",
        "Clouds and weather",
        False,
    ),
    "thermometer": LessonImage(
        "thermometer",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Thermometer.jpg/960px-Thermometer.jpg",
        "Nhiệt kế — đo nhiệt độ",
        "Thermometer for temperature",
        False,
    ),
    "hospital": LessonImage(
        "hospital",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Hospital.jpg/960px-Hospital.jpg",
        "Bệnh viện — toán trong y tế",
        "Hospital building",
        False,
    ),
    "building": LessonImage(
        "building",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Building.jpg/960px-Building.jpg",
        "Tòa nhà — toán trong kiến trúc",
        "Building architecture",
        False,
    ),
    "bridge": LessonImage(
        "bridge",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Bridge_over_the_Sukhona_River_at_Sokol%2C_June_2008.jpg/960px-Bridge_over_the_Sukhona_River_at_Sokol%2C_June_2008.jpg",
        "Cây cầu — toán trong kiến trúc",
        "Bridge structure",
        False,
    ),
    "farm_field": LessonImage(
        "farm_field",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Agriculture_field.jpg/960px-Agriculture_field.jpg",
        "Cánh đồng — toán trong nông nghiệp",
        "Agriculture field",
        False,
    ),
    "board_games": LessonImage(
        "board_games",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Board_games.jpg/960px-Board_games.jpg",
        "Trò chơi board game — chiến lược và xác suất",
        "Board games",
        False,
    ),
    "street_numbers": LessonImage(
        "street_numbers",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Coltman_Street%2C_Hull_-_geograph.org.uk_-_1194325.jpg/960px-Coltman_Street%2C_Hull_-_geograph.org.uk_-_1194325.jpg",
        "Số nhà hai bên đường",
        "Street house numbers",
        False,
    ),
}

# Keyword rules: higher weight = stronger match. Each rule lists image keys in priority order.
TOPIC_RULES: list[tuple[int, list[str], list[str]]] = [
    (10, ["pascal", "tam giac pascal"], ["pascal_triangle", "triangular"]),
    (10, ["fibonacci"], ["fibonacci_spiral", "fibonacci_rabbits", "arithmetic_progression"]),
    (10, ["so nguyen to", "prime", "eratosthenes", "sieve"], ["sieve_primes", "number_line", "abacus"]),
    (9, ["phan so", "fraction", "half", "quarter", "third"], ["pie_chart", "balance_scale"]),
    (9, ["hinh hoc", "geometry", "hinh tam giac", "hinh vuong", "hinh tron", "hinh chu nhat"], ["triangle", "square_shape", "circle", "rectangle"]),
    (9, ["goc", "angle", "duong thang", "line"], ["triangle", "parallelogram", "rectangle"]),
    (9, ["dien tich", "area", "chu vi", "perimeter"], ["rectangle", "triangle", "circle"]),
    (9, ["the tich", "volume", "hinh hop", "hinh lap phuong", "hinh cau", "hinh non", "hinh tru"], ["cube", "sphere", "cone", "rectangle"]),
    (9, ["hinh thoi", "rhombus"], ["rhombus", "parallelogram"]),
    (9, ["hinh thang", "trapezoid"], ["trapezoid", "triangle"]),
    (9, ["hinh binh hanh", "parallelogram"], ["parallelogram", "rectangle"]),
    (8, ["xac suat", "probability"], ["dice", "bar_chart"]),
    (8, ["thong ke", "statistics", "bieu do", "du lieu"], ["bar_chart", "pie_chart", "dice"]),
    (8, ["ma nhi phan", "binary", "tin hoc", "computer", "lap trinh", "programming"], ["binary", "laptop_code", "number_line"]),
    (8, ["phuong trinh", "equation", "dai so", "algebra", "bien so", "variable"], ["balance_scale", "number_line", "abacus"]),
    (8, ["day so", "sequence", "quy luat", "pattern", "mau hinh", "luoi so"], ["arithmetic_progression", "even_odd_line", "powers_chart"]),
    (8, ["so am", "negative"], ["number_line", "even_odd_line"]),
    (8, ["so chinh phuong", "square number"], ["square_numbers", "powers_chart"]),
    (8, ["so thap phan", "decimal"], ["number_line", "abacus"]),
    (8, ["phan tram", "percent", "ti le"], ["pie_chart", "bar_chart"]),
    (8, ["tien", "money", "coin", "tai chinh", "finance"], ["market_vn", "shopping_cart", "vegetables_shop"]),
    (8, ["thoi gian", "time", "clock", "dong ho", "xem dong ho"], ["number_line", "abacus"]),
    (8, ["do luong", "measure", "don vi", "unit", "can nang", "khoi luong"], ["balance_scale", "number_line"]),
    (8, ["ty le", "ratio", "proportion"], ["pie_chart", "balance_scale"]),
    (7, ["phep nhan", "multiply", "multiplication", "nhan nhanh"], ["powers_chart", "abacus", "triangular"]),
    (7, ["phep chia", "division", "divide", "chia nhanh"], ["abacus", "cherries", "buttons"]),
    (7, ["phep cong", "addition", "add"], ["abacus", "panzhu_addition", "market_vn"]),
    (7, ["phep tru", "subtraction", "subtract"], ["eggs", "abacus", "market_scene"]),
    (7, ["ucln", "bcnn", "gcd", "lcm", "uoc chung", "boi chung"], ["sieve_primes", "number_line"]),
    (7, ["so chan", "even", "skip count", "cap doi"], ["even_odd_line", "socks", "buttons"]),
    (7, ["so lon", "billion", "million", "population", "vu tru", "space"], ["earth", "city_lights", "moon"]),
    (7, ["suy luan", "logic", "reasoning", "puzzle", "game"], ["board_games", "balance_scale", "pascal_triangle"]),
    (6, ["the thao", "sport", "bong da", "soccer", "football"], ["soccer", "basketball", "children"]),
    (6, ["bong ro", "basketball"], ["basketball", "soccer"]),
    (6, ["am nhac", "music"], ["pie_chart", "number_line"]),
    (6, ["kien truc", "architecture", "building"], ["building", "bridge", "rectangle"]),
    (6, ["y te", "health", "hospital"], ["hospital", "thermometer"]),
    (6, ["nau an", "cooking", "kitchen"], ["cooking", "market_vn", "balance_scale"]),
    (6, ["mua sam", "shopping"], ["shopping_cart", "market_vn", "vegetables_shop"]),
    (6, ["giao thong", "traffic", "transport"], ["traffic", "road", "number_line"]),
    (6, ["nong nghiep", "agriculture", "farm"], ["farm_field", "market_vn"]),
    (6, ["du lich", "travel", "tourism"], ["earth", "bridge", "road"]),
    (6, ["thoi tiet", "weather"], ["cloud_weather", "thermometer"]),
    (6, ["tro choi", "game"], ["board_games", "dice", "soccer"]),
    (6, ["phim anh", "film", "movie", "camera"], ["camera", "pie_chart"]),
    (6, ["nghe thuat", "art"], ["building", "triangle", "square_shape"]),
    (6, ["khoa hoc", "science", "astronomy", "thien van"], ["earth", "moon", "sphere"]),
    (6, ["kho", "warehouse", "inventory"], ["shopping_cart", "cube", "bar_chart"]),
    (5, ["on tap", "review", "tong ket"], ["number_line", "abacus", "bar_chart"]),
    (4, ["continuity", "uniform"], ["number_line", "triangle"]),
]

CHAPTER_DEFAULTS: dict[str, list[str]] = {
    "chapter00": ["number_line", "triangle"],
    "chapter01": ["even_odd_line", "socks", "abacus"],
    "chapter02": ["powers_chart", "sieve_primes", "abacus"],
    "chapter03": ["balance_scale", "pascal_triangle", "arithmetic_progression"],
    "chapter04": ["pie_chart", "balance_scale", "number_line"],
    "chapter05": ["square_numbers", "sieve_primes", "number_line"],
    "chapter06": ["pie_chart", "number_line", "market_vn"],
    "chapter07": ["bar_chart", "dice", "binary"],
    "chapter08": ["triangle", "rectangle", "circle"],
}


def strip_accents(text: str) -> str:
    normalized = unicodedata.normalize("NFD", text)
    return "".join(c for c in normalized if unicodedata.category(c) != "Mn")


def normalize(text: str) -> str:
    text = strip_accents(text.lower())
    text = re.sub(r"[^a-z0-9\s/_-]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def keyword_matches(text: str, keyword: str) -> bool:
    """Match multi-word phrases as substrings; short tokens need word boundaries."""
    if " " in keyword or len(keyword) >= 7:
        return keyword in text
    pattern = rf"(^| ){re.escape(keyword)}( |$)"
    return re.search(pattern, text) is not None


def parse_front_matter(content: str) -> tuple[dict[str, str], str]:
    if not content.startswith("---"):
        return {}, content
    end = content.find("\n---", 3)
    if end == -1:
        return {}, content
    fm_block = content[3:end]
    body = content[end + 4 :].lstrip("\n")
    meta: dict[str, str] = {}
    for line in fm_block.splitlines():
        if ":" in line:
            key, val = line.split(":", 1)
            meta[key.strip()] = val.strip().strip("'\"")
    return meta, body


def count_wikimedia(content: str) -> int:
    return len(re.findall(r"upload\.wikimedia\.org", content))


def score_images(
    search_text: str,
    chapter_category: str,
    title_text: str = "",
    filename_text: str = "",
) -> list[str]:
    scores: dict[str, int] = {}

    for weight, keywords, image_keys in TOPIC_RULES:
        for kw in keywords:
            if not keyword_matches(search_text, kw):
                continue
            title_hit = bool(title_text and keyword_matches(title_text, kw))
            filename_hit = bool(filename_text and keyword_matches(filename_text, kw))
            for i, key in enumerate(image_keys):
                boost = 0
                if i == 0:
                    if title_hit:
                        boost += TITLE_BOOST
                    if filename_hit:
                        boost += FILENAME_BOOST
                scores[key] = scores.get(key, 0) + weight - i + boost

    for key in CHAPTER_DEFAULTS.get(chapter_category, ["number_line", "abacus"]):
        scores[key] = scores.get(key, 0) + 1

    ranked = sorted(scores.items(), key=lambda x: (-x[1], x[0]))

    primary: list[str] = []
    if title_text:
        for _weight, keywords, image_keys in TOPIC_RULES:
            if any(keyword_matches(title_text, kw) for kw in keywords):
                primary = [k for k in image_keys if k in IMAGES][:TARGET_IMAGES]
                break

    chosen: list[str] = []
    for key in primary + [k for k, _ in ranked]:
        if key not in chosen:
            chosen.append(key)
        if len(chosen) >= TARGET_IMAGES + 2:
            break
    return chosen


def format_image_block(img: LessonImage, lang: str) -> str:
    alt = img.alt_vi if lang == "vi" else img.alt_en
    caption = "*Ảnh: Wikimedia Commons — sơ đồ toán học*" if img.math_diagram else "*Ảnh: Wikimedia Commons*"
    if lang == "en" and img.math_diagram:
        caption = "*Image: Wikimedia Commons — math diagram*"
    elif lang == "en":
        caption = "*Image: Wikimedia Commons*"
    return f"\n\n![{alt}]({img.url})\n\n{caption}\n\n"


SECTION_FLAGS = re.M | re.I
SECTION_PATTERNS = [
    re.compile(r"^## (Mở đầu|Giới thiệu|Introduction|Objectives|Mục tiêu)\b", SECTION_FLAGS),
    re.compile(
        r"^## (Khám phá toán học|Core Idea|Khám phá|Kiến thức đã biết|Prerequisites|Kiến thức cần có|Câu chuyện)\b",
        SECTION_FLAGS,
    ),
    re.compile(
        r"^## (Hoạt động khám phá|Ví dụ|Examples|Activities|Toán học qua các thời đại)\b",
        SECTION_FLAGS,
    ),
    re.compile(r"^## (\d+\.|Phần \d+)", SECTION_FLAGS),
    re.compile(r"^## (Bài tập|Exercises|Câu hỏi|Tổng kết)\b", SECTION_FLAGS),
]


def find_intro_insert_pos(body: str) -> int | None:
    """Insert after opening hook before first ## if no dedicated hook section."""
    m = re.search(r"^## ", body, re.M)
    if not m:
        return None
    intro = body[: m.start()].strip()
    if len(intro) < 40:
        return None
    # After first paragraph in intro
    para = re.search(r"\n\n", intro)
    if para:
        return para.end()
    return len(intro)


def insert_into_section(body: str, pattern: re.Pattern[str], image_block: str) -> tuple[str, bool]:
    match = pattern.search(body)
    if not match:
        return body, False

    start = match.end()
    rest = body[start:]
    next_header = re.search(r"\n## |\n---\n", rest)
    section_end = start + (next_header.start() if next_header else len(rest))
    section = body[start:section_end]

    if WIKIMEDIA_MARKER in section:
        return body, False

    # Skip past header-adjacent blank lines, insert after first paragraph
    local = section.lstrip("\n")
    offset = len(section) - len(local)
    para_break = re.search(r"\n\n", local)
    if para_break:
        insert_at = start + offset + para_break.end()
    else:
        insert_at = section_end

    return body[:insert_at] + image_block + body[insert_at:], True


def strip_wikimedia_blocks(content: str) -> str:
    return WIKIMEDIA_BLOCK_RE.sub("\n", content)


def add_illustrations(
    content: str,
    path: Path,
    *,
    min_existing: int = MIN_EXISTING,
    reapply: bool = False,
) -> tuple[str, int]:
    meta, body = parse_front_matter(content)
    existing = count_wikimedia(content)
    if reapply:
        if existing >= 4 and "chapter01" in path.as_posix():
            return content, 0
        content = strip_wikimedia_blocks(content)
        meta, body = parse_front_matter(content)
        existing = 0
    elif existing >= min_existing:
        return content, 0

    lang = meta.get("lang", "vi")
    categories = meta.get("categories", "")
    chapter_cat = categories.strip("- ").split(",")[0].strip() if categories else ""
    if not chapter_cat:
        m = re.search(r"chapter\d+", path.as_posix())
        chapter_cat = m.group(0) if m else "chapter01"

    title = meta.get("title", path.stem)
    title_text = normalize(title)
    filename_text = normalize(path.stem)
    search_text = normalize(f"{title} {path.stem} {body[:4000]}")

    image_keys = score_images(search_text, chapter_cat, title_text, filename_text)
    blocks = [format_image_block(IMAGES[k], lang) for k in image_keys if k in IMAGES]

    if not blocks:
        return content, 0

    added = 0
    new_body = body

    # 1) Intro hook — prefer inserting after local chapter SVG
    if added < TARGET_IMAGES:
        local_svg = re.search(
            r"!\[[^\]]*\]\(\{\{ site\.baseurl \}\}/img/chapter_img/[^)]+\)",
            new_body,
        )
        if local_svg:
            pos = local_svg.end()
            while pos < len(new_body) and new_body[pos] in "\n":
                pos += 1
            new_body = new_body[:pos] + blocks[added] + new_body[pos:]
            added += 1
        else:
            pos = find_intro_insert_pos(new_body)
            if pos is not None and WIKIMEDIA_MARKER not in new_body[:pos]:
                new_body = new_body[:pos] + blocks[added] + new_body[pos:]
                added += 1

    # 2–4) Section-based insertions
    for pattern in SECTION_PATTERNS:
        if added >= TARGET_IMAGES:
            break
        new_body, ok = insert_into_section(new_body, pattern, blocks[added])
        if ok:
            added += 1

    if added == 0:
        return content, 0

    fm_end = content.find("\n---", 3)
    if fm_end == -1:
        return new_body, added
    return content[: fm_end + 4] + "\n" + new_body, added


def iter_lesson_files() -> list[Path]:
    files = sorted(CONTENTS.glob("**/chapter*/_posts/*.md"))
    return files


def main() -> None:
    parser = argparse.ArgumentParser(description="Add Wikimedia illustrations to lesson posts")
    parser.add_argument("--dry-run", action="store_true", help="Print changes without writing")
    parser.add_argument("--file", type=str, help="Process a single file path")
    parser.add_argument(
        "--reapply",
        action="store_true",
        help="Remove existing Wikimedia blocks and re-insert (skips chapter01 with 4+ images)",
    )
    parser.add_argument(
        "--min-existing",
        type=int,
        default=MIN_EXISTING,
        help="Skip files that already have this many Wikimedia images",
    )
    args = parser.parse_args()

    targets = [Path(args.file)] if args.file else iter_lesson_files()
    total_added = 0
    changed_files = 0
    skipped = 0

    for path in targets:
        if not path.exists():
            print(f"SKIP missing: {path}")
            continue
        original = path.read_text(encoding="utf-8")
        if not args.reapply and count_wikimedia(original) >= args.min_existing:
            skipped += 1
            continue

        updated, n = add_illustrations(
            original,
            path,
            min_existing=args.min_existing,
            reapply=args.reapply,
        )
        if n == 0:
            skipped += 1
            continue

        changed_files += 1
        total_added += n
        rel = path.relative_to(ROOT)
        print(f"UPDATED {rel} (+{n} images)")

        if not args.dry_run:
            path.write_text(updated, encoding="utf-8")

    print(
        f"\nDone: {changed_files} files updated, {total_added} images added, {skipped} skipped."
    )


if __name__ == "__main__":
    main()