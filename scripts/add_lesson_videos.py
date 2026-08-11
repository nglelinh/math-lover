#!/usr/bin/env python3
"""Add curated YouTube educational video links to lesson posts.

Each lesson gets 2-3 topic-matched videos from popular edu channels.
"""

from __future__ import annotations

import argparse
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENTS = ROOT / "contents"

YOUTUBE_MARKER = "youtube.com/watch"
MIN_EXISTING = 2
TARGET_VIDEOS = 3
TITLE_BOOST = 20
FILENAME_BOOST = 10

VIDEO_SECTION_VI = "## Video tham khảo"
VIDEO_SECTION_EN = "## Watch and Learn"

VIDEO_SECTION_RE = re.compile(
    r"^## (Video tham khảo|Watch and Learn)\b.*?(?=^## |\Z)",
    re.M | re.S,
)


@dataclass(frozen=True)
class EduVideo:
    key: str
    video_id: str
    title_vi: str
    title_en: str
    channel: str
    vi_ok: bool = True
    en_ok: bool = True


# Curated popular educational videos (verified via yt-dlp / oembed)
VIDEOS: dict[str, EduVideo] = {
    # Numbers & patterns
    "even_odd_ka": EduVideo(
        "even_odd_ka", "SFRTTUtAjg4",
        "Giới thiệu số chẵn và số lẻ — Khan Academy",
        "Introduction to even and odd numbers — Khan Academy",
        "Khan Academy",
    ),
    "number_line_ma": EduVideo(
        "number_line_ma", "RSJOTBJlKNA",
        "Trục số — Math Antics",
        "The Number Line — Math Antics",
        "Math Antics",
    ),
    "patterns_ma": EduVideo(
        "patterns_ma", "vV7C7bXm4VI",
        "Mẫu hình số — Math Antics",
        "Number Patterns — Math Antics",
        "Math Antics",
    ),
    "fib_np": EduVideo(
        "fib_np", "Nu-lW-Ifyec",
        "Bí ẩn dãy Fibonacci — Numberphile",
        "Fibonacci Mystery — Numberphile",
        "Numberphile",
    ),
    "pascal_np": EduVideo(
        "pascal_np", "0iMtlus-afo",
        "Tam giác Pascal — Numberphile",
        "Pascal's Triangle — Numberphile",
        "Numberphile",
    ),
    # Operations
    "add_ka": EduVideo(
        "add_ka", "AuX7nPBqDts",
        "Phép cộng cơ bản — Khan Academy",
        "Basic addition — Khan Academy",
        "Khan Academy",
    ),
    "add_regroup_ka": EduVideo(
        "add_regroup_ka", "9hM32lsQ4aI",
        "Cộng có nhớ — Khan Academy",
        "Adding with regrouping — Khan Academy",
        "Khan Academy",
    ),
    "sub_regroup_ka": EduVideo(
        "sub_regroup_ka", "9T3AAn-Cw3g",
        "Trừ có nhớ — số ba chữ số — Khan Academy",
        "Subtracting: three digit numbers and basic regrouping — Khan Academy",
        "Khan Academy",
    ),
    "sub_borrow_ka": EduVideo(
        "sub_borrow_ka", "egjDLFX9VHg",
        "Trừ có mượn (nhóm) — Khan Academy",
        "Subtracting with regrouping (borrowing) — Khan Academy",
        "Khan Academy",
    ),
    "place_value_ma": EduVideo(
        "place_value_ma", "T5Qf0qSSJFI",
        "Giá trị hàng — Math Antics",
        "Place Value — Math Antics",
        "Math Antics",
    ),
    "place_value_ka": EduVideo(
        "place_value_ka", "wx2gI8iwMCA",
        "Giới thiệu giá trị hàng — Khan Academy",
        "Introduction to place value — Khan Academy",
        "Khan Academy",
    ),
    "even_odd_kids": EduVideo(
        "even_odd_kids", "eF_FxSW8QwY",
        "Số chẵn và số lẻ — Math for Kids",
        "Even and Odd Numbers — Math for Kids",
        "Math for Kids",
    ),
    "vi_sub_borrow": EduVideo(
        "vi_sub_borrow", "zZtQiVYqIeQ",
        "Cách trừ dọc có mượn — Toán Tư duy Kes",
        "Vertical subtraction with borrowing — Toán Tư duy Kes",
        "Toán Tư duy Kes",
        en_ok=False,
    ),
    "vi_large_numbers": EduVideo(
        "vi_large_numbers", "2rh1hKpfxI4",
        "Đọc và viết số lớn — Toán lớp 4",
        "Reading and writing large numbers — grade 4",
        "Toán Tiểu học",
        en_ok=False,
    ),
    "mult_ka": EduVideo(
        "mult_ka", "mvOkMYCygps",
        "Phép nhân cơ bản — Khan Academy",
        "Basic multiplication — Khan Academy",
        "Khan Academy",
    ),
    "mult_intro_ka": EduVideo(
        "mult_intro_ka", "RNxwasijbAo",
        "Giới thiệu phép nhân — Khan Academy",
        "Intro to multiplication — Khan Academy",
        "Khan Academy",
    ),
    "mult_lattice_ka": EduVideo(
        "mult_lattice_ka", "gS6TfWUv97I",
        "Nhân kiểu lưới — Khan Academy",
        "Lattice multiplication — Khan Academy",
        "Khan Academy",
    ),
    "div_ma": EduVideo(
        "div_ma", "KGMf314LUc0",
        "Phép chia cơ bản — Math Antics",
        "Basic Division — Math Antics",
        "Math Antics",
    ),
    "div_long_ka": EduVideo(
        "div_long_ka", "8Ft5iHhauJ0",
        "Chia dài — Khan Academy",
        "Introduction to long division — Khan Academy",
        "Khan Academy",
    ),
    "div_long_ma": EduVideo(
        "div_long_ma", "HdU_rf7eMTI",
        "Chia số hai chữ số — Math Antics",
        "Long Division with 2-Digit Divisors — Math Antics",
        "Math Antics",
    ),
    # Fractions & decimals
    "frac_parts_ma": EduVideo(
        "frac_parts_ma", "CA9XLJpQp3c",
        "Phân số là các phần — Math Antics",
        "Fractions Are Parts — Math Antics",
        "Math Antics",
    ),
    "frac_what_ma": EduVideo(
        "frac_what_ma", "I1u3pM9g9o8",
        "Phân số là gì? — Math Antics",
        "What Are Fractions? — Math Antics",
        "Math Antics",
    ),
    "frac_line_ma": EduVideo(
        "frac_line_ma", "pWJzqTYS8no",
        "Phân số trên trục số — Math Antics",
        "Fractions on the Number Line — Math Antics",
        "Math Antics",
    ),
    "frac_add_ma": EduVideo(
        "frac_add_ma", "5juto2ze8Lg",
        "Cộng trừ phân số — Math Antics",
        "Adding and Subtracting Fractions — Math Antics",
        "Math Antics",
    ),
    "frac_mult_ma": EduVideo(
        "frac_mult_ma", "qmfXyR7Z6Lk",
        "Nhân phân số — Math Antics",
        "Multiplying Fractions — Math Antics",
        "Math Antics",
    ),
    "frac_simp_ma": EduVideo(
        "frac_simp_ma", "AtBUQH8Tkqc",
        "Rút gọn phân số — Math Antics",
        "Simplifying Fractions — Math Antics",
        "Math Antics",
    ),
    "frac_vi_vj": EduVideo(
        "frac_vi_vj", "XBLL9DXfdeM",
        "Khái niệm phân số lớp 4 — VietJack",
        "Fractions grade 4 — VietJack",
        "VietJack Tiểu học",
    ),
    "frac_equiv_vi": EduVideo(
        "frac_equiv_vi", "c0thGlyVsqA",
        "Rút gọn phân số lớp 4 — VietJack",
        "Simplifying fractions grade 4 — VietJack",
        "VietJack Tiểu học",
    ),
    "decimal_place_ma": EduVideo(
        "decimal_place_ma", "KG6ILNOiMgM",
        "Giá trị chữ số thập phân — Math Antics",
        "Decimal Place Value — Math Antics",
        "Math Antics",
    ),
    "decimal_arith_ma": EduVideo(
        "decimal_arith_ma", "kwh4SD1ToFc",
        "Tính toán số thập phân — Math Antics",
        "Decimal Arithmetic — Math Antics",
        "Math Antics",
    ),
    "percent_ma": EduVideo(
        "percent_ma", "JeVSmq1Nrpw",
        "Phần trăm là gì? — Math Antics",
        "What Are Percentages? — Math Antics",
        "Math Antics",
    ),
    # Primes & factors
    "prime_factor_ma": EduVideo(
        "prime_factor_ma", "SXPsfr-Fnu4",
        "Ước chung bằng phân tích thừa số — Math Antics",
        "LCM: Prime Factorization — Math Antics",
        "Math Antics",
    ),
    "gcf_ma": EduVideo(
        "gcf_ma", "CUEOL3_Wm3Y",
        "Ước chung lớn nhất — Math Antics",
        "GCF: Greatest Common Factor — Math Antics",
        "Math Antics",
    ),
    # Algebra & equations
    "algebra_ma": EduVideo(
        "algebra_ma", "NybHckSEQBI",
        "Đại số là gì? — Math Antics",
        "What Is Algebra? — Math Antics",
        "Math Antics",
    ),
    "equation_ma": EduVideo(
        "equation_ma", "l3XzepN03KQ",
        "Giải phương trình bước 1 — Math Antics",
        "Solving Basic Equations Part 1 — Math Antics",
        "Math Antics",
    ),
    "equation2_ma": EduVideo(
        "equation2_ma", "LDIiYKYvvdA",
        "Giải phương trình hai bước — Math Antics",
        "Solving 2-Step Equations — Math Antics",
        "Math Antics",
    ),

    # Negatives & integers
    "negative_ma": EduVideo(
        "negative_ma", "OAoLCXpao6s",
        "Số âm — Math Antics",
        "Negative Numbers — Math Antics",
        "Math Antics",
    ),
    "int_add_ma": EduVideo(
        "int_add_ma", "_BgblvF90UE",
        "Cộng trừ số nguyên — Math Antics",
        "Adding & Subtracting Integers — Math Antics",
        "Math Antics",
    ),
    # Geometry
    "area_ma": EduVideo(
        "area_ma", "xCdxURXMdFY",
        "Diện tích — Math Antics",
        "Area — Math Antics",
        "Math Antics",
    ),
    "circle_ma": EduVideo(
        "circle_ma", "O-cawByg2aA",
        "Hình tròn, chu vi và diện tích — Math Antics",
        "Circles, Circumference And Area — Math Antics",
        "Math Antics",
    ),
    "volume_ma": EduVideo(
        "volume_ma", "qJwecTgce6c",
        "Thể tích — Math Antics",
        "Volume — Math Antics",
        "Math Antics",
    ),
    "triangle_ka": EduVideo(
        "triangle_ka", "KUhdMbx5ges",
        "Tính chất tam giác — Khan Academy",
        "Review of triangle properties — Khan Academy",
        "Khan Academy",
    ),
    "geom_vi_vj": EduVideo(
        "geom_vi_vj", "e7xS59eDyRg",
        "Ôn tập hình học lớp 4 — VietJack",
        "Geometry review grade 4 — VietJack",
        "VietJack Tiểu học",
    ),
    "coord_ma": EduVideo(
        "coord_ma", "9Uc62CuQjc4",
        "Mặt phẳng tọa độ — Math Antics",
        "Graphing On The Coordinate Plane — Math Antics",
        "Math Antics",
    ),
    # Stats & probability
    "prob_ka": EduVideo(
        "prob_ka", "uzkc-qNVoOk",
        "Xác suất cơ bản — Khan Academy",
        "Probability explained — Khan Academy",
        "Khan Academy",
    ),
    "data_ma": EduVideo(
        "data_ma", "hcgThf5mv38",
        "Dữ liệu và biểu đồ — Math Antics",
        "Data And Graphs — Math Antics",
        "Math Antics",
    ),
    # Time, money, measurement
    "time_ma": EduVideo(
        "time_ma", "QU-XUmujbuM",
        "Xem đồng hồ — Math Antics",
        "Telling Time — Math Antics",
        "Math Antics",
    ),
    "money_ma": EduVideo(
        "money_ma", "DbYbIB4m3RM",
        "Tiền đô-la và xu — Math Antics",
        "Dollars And Cents — Math Antics",
        "Math Antics",
    ),
    "distance_ma": EduVideo(
        "distance_ma", "dNcJ4-JVN5M",
        "Đo khoảng cách — Math Antics",
        "Measuring Distance — Math Antics",
        "Math Antics",
    ),
    # Vietnamese primary school
    "vi_mult": EduVideo(
        "vi_mult", "3063JLw0UGU",
        "Nhân hai chữ số lớp 3 — Luyện Thi 123",
        "Grade 3 multiplication — Luyện Thi 123",
        "Luyện Thi 123", en_ok=False,
    ),
    "vi_table3": EduVideo(
        "vi_table3", "8yoMIulmEsQ",
        "Bảng nhân 3 — Dâu Tây TV",
        "Times table of 3 — Dâu Tây TV",
        "Dâu Tây TV", en_ok=False,
    ),
    "vi_div": EduVideo(
        "vi_div", "ZR5LP_yQGS8",
        "Phép chia có dư lớp 3 — Thầy Huấn",
        "Division with remainder grade 3 — Thầy Huấn",
        "Thầy Huấn Tiểu học", en_ok=False,
    ),
    "vi_div2": EduVideo(
        "vi_div2", "8neRbeLtUY4",
        "Chia ba chữ số lớp 3 — Cô Giáo Nga",
        "Three-digit division grade 3 — Cô Giáo Nga",
        "Cô Giáo Nga Tiểu Học", en_ok=False,
    ),
    "vi_general": EduVideo(
        "vi_general", "1MItnAP54bs",
        "Toán lớp 3 — phương pháp tư duy — Cô Hiền",
        "Grade 3 math thinking — Cô Hiền",
        "TOÁN CÔ HIỀN", en_ok=False,
    ),
    # Enrichment / review
    "symmetry_ma": EduVideo(
        "symmetry_ma", "QHq3CSoal0I",
        "Đối xứng — Math Antics",
        "Symmetry — Math Antics",
        "Math Antics",
    ),
    "powers10_ma": EduVideo(
        "powers10_ma", "qJB19dAZPpY",
        "Nhân chia lũy thừa 10 — Math Antics",
        "Multiply and Divide by Powers of 10 — Math Antics",
        "Math Antics",
    ),
    "square_ma": EduVideo(
        "square_ma", "B4zejSI8zho",
        "Lũy thừa và căn bậc hai — Math Antics",
        "Exponents and Square Roots — Math Antics",
        "Math Antics",
    ),
    "ratio_ma": EduVideo(
        "ratio_ma", "RQ2nYUBVvqI",
        "Tỷ số và tỷ lệ — Math Antics",
        "Ratios And Rates — Math Antics",
        "Math Antics",
    ),
    "proportion_ma": EduVideo(
        "proportion_ma", "USmit5zUGas",
        "Tỷ lệ thuận — Math Antics",
        "Proportions — Math Antics",
        "Math Antics",
    ),
    "prime_ka": EduVideo(
        "prime_ka", "mIStB5X4U8M",
        "Số nguyên tố — Khan Academy",
        "Prime numbers — Khan Academy",
        "Khan Academy",
    ),
}

TOPIC_RULES: list[tuple[int, list[str], list[str]]] = [
    (10, ["so chan", "even", "odd", "cap doi"], ["even_odd_ka", "number_line_ma", "even_odd_kids"]),
    (10, ["so lon", "trieu", "ty", "million", "billion", "place value"], ["place_value_ma", "powers10_ma", "vi_large_numbers"]),
    (10, ["to hop", "hoan vi", "nguyen ly", "dem co he", "cay kha nang", "combinatorics", "counting method"], ["prob_ka", "mult_ka", "patterns_ma"]),
    (9, ["phep dem", "dem cach", "counting carefully"], ["prob_ka", "patterns_ma", "mult_ka"]),
    (10, ["mau hinh", "pattern", "day so", "sequence", "quy luat"], ["patterns_ma", "number_line_ma", "fib_np"]),
    (10, ["fibonacci"], ["fib_np", "pascal_np", "patterns_ma"]),
    (10, ["pascal"], ["pascal_np", "patterns_ma", "fib_np"]),
    (9, ["phep cong", "addition", "add"], ["add_ka", "add_regroup_ka", "vi_general"]),
    (9, ["phep tru", "subtraction", "subtract"], ["sub_regroup_ka", "sub_borrow_ka", "vi_sub_borrow"]),
    (9, ["phep nhan", "multiplication", "multiply", "nhan nhanh"], ["mult_ka", "mult_intro_ka", "vi_mult"]),
    (9, ["phep chia", "division", "divide", "chia nhanh"], ["div_ma", "div_long_ka", "vi_div"]),
    (9, ["phan so", "fraction", "half", "quarter", "third"], ["frac_parts_ma", "frac_what_ma", "frac_vi_vj"]),
    (9, ["bang nhau", "equivalent", "rut gon phan"], ["frac_simp_ma", "frac_equiv_vi", "frac_line_ma"]),
    (9, ["so sanh phan", "compare fraction"], ["frac_what_ma", "frac_line_ma", "frac_vi_vj"]),
    (8, ["so thap phan", "decimal"], ["decimal_place_ma", "decimal_arith_ma", "frac_line_ma"]),
    (8, ["phan tram", "percent"], ["percent_ma", "decimal_arith_ma", "data_ma"]),
    (8, ["so nguyen to", "prime", "eratosthenes"], ["prime_ka", "prime_factor_ma", "gcf_ma"]),
    (8, ["ucln", "bcnn", "gcd", "lcm", "uoc chung", "boi chung"], ["gcf_ma", "prime_factor_ma", "vi_div2"]),
    (8, ["so am", "negative"], ["negative_ma", "int_add_ma", "number_line_ma"]),
    (8, ["so chinh phuong", "square number"], ["square_ma", "patterns_ma", "mult_ka"]),
    (8, ["phuong trinh", "equation", "dai so", "algebra", "bien so"], ["equation_ma", "algebra_ma", "equation2_ma"]),
    (8, ["can bang", "balanced scale", "mystery box"], ["equation_ma", "algebra_ma", "frac_line_ma"]),
    (8, ["hinh hoc", "geometry", "hinh tam giac", "hinh vuong", "hinh tron"], ["area_ma", "circle_ma", "geom_vi_vj"]),
    (8, ["dien tich", "area", "chu vi", "perimeter"], ["area_ma", "circle_ma", "geom_vi_vj"]),
    (8, ["the tich", "volume"], ["volume_ma", "area_ma", "circle_ma"]),
    (8, ["goc", "angle", "duong thang"], ["triangle_ka", "symmetry_ma", "coord_ma"]),
    (8, ["xac suat", "probability"], ["prob_ka", "data_ma", "patterns_ma"]),
    (8, ["thong ke", "statistics", "bieu do", "du lieu", "data"], ["data_ma", "prob_ka", "percent_ma"]),
    (8, ["ma nhi phan", "binary", "tin hoc", "lap trinh"], ["powers10_ma", "patterns_ma", "decimal_place_ma"]),
    (7, ["thoi gian", "time", "dong ho", "clock"], ["time_ma", "distance_ma", "vi_general"]),
    (7, ["tien", "money", "tai chinh"], ["money_ma", "decimal_arith_ma", "percent_ma"]),
    (7, ["do luong", "measure", "don vi"], ["distance_ma", "time_ma", "area_ma"]),
    (7, ["ty le", "ratio", "proportion", "ti le"], ["ratio_ma", "proportion_ma", "percent_ma"]),
    (6, ["the thao", "sport", "bong da"], ["mult_ka", "data_ma", "prob_ka"]),
    (6, ["on tap", "review", "tong ket"], ["patterns_ma", "number_line_ma", "vi_general"]),
    (5, ["continuity", "uniform"], ["algebra_ma", "number_line_ma", "patterns_ma"]),
]

# Hand-curated overrides (Chapter 01 — topic-accurate, verified IDs)
LESSON_VIDEO_OVERRIDES: dict[str, list[str]] = {
    "26-01-01-01_01_Kham_pha_so": ["even_odd_ka", "number_line_ma", "even_odd_kids"],
    "26-01-01-01_02_Mau_hinh": ["patterns_ma", "number_line_ma", "fib_np"],
    "26-01-01-01_11_Phep_tru": ["sub_regroup_ka", "sub_borrow_ka", "vi_sub_borrow"],
    "26-01-01-01_12_Phep_cong": ["add_ka", "add_regroup_ka", "vi_general"],
    "26-01-01-03_03_So_lon": ["place_value_ma", "powers10_ma", "vi_large_numbers"],
    "26-01-01-01_15_Quy_luat": ["patterns_ma", "fib_np", "powers10_ma"],
    "2024-01-01-discovering-even-numbers": ["even_odd_ka", "number_line_ma", "even_odd_kids"],
}

# Filename stem rules (longer / more specific patterns first)
STEM_VIDEO_RULES: list[tuple[str, list[str]]] = [
    # Chapter 00
    ("continuity_and_uniform", ["algebra_ma", "number_line_ma", "patterns_ma"]),
    # EN — skip counting & algebra intro
    ("skip-counting-by-2s", ["even_odd_ka", "mult_intro_ka", "patterns_ma"]),
    ("skip-counting-by-5s", ["mult_ka", "mult_intro_ka", "powers10_ma"]),
    ("skip-counting-by-10s", ["powers10_ma", "place_value_ma", "mult_ka"]),
    ("mystery-box", ["equation_ma", "algebra_ma", "number_line_ma"]),
    ("balanced-scale", ["equation_ma", "algebra_ma", "equation2_ma"]),
    ("number-patterns", ["patterns_ma", "fib_np", "number_line_ma"]),
    ("halves-and-quarters", ["frac_parts_ma", "frac_what_ma", "frac_vi_vj"]),
    ("thirds-and-sixths", ["frac_parts_ma", "frac_what_ma", "frac_line_ma"]),
    ("comparing-fractions", ["frac_what_ma", "frac_line_ma", "frac_vi_vj"]),
    ("fraction-puzzles", ["frac_what_ma", "frac_add_ma", "patterns_ma"]),
    ("mot-nua-va-mot-phan-tu", ["frac_parts_ma", "frac_what_ma", "frac_vi_vj"]),
    # Chapter 02 — operations & primes
    ("phep_nhan", ["mult_ka", "mult_intro_ka", "vi_mult"]),
    ("phep_chia", ["div_ma", "div_long_ka", "vi_div"]),
    ("so_nguyen_to", ["prime_ka", "prime_factor_ma", "gcf_ma"]),
    ("ucln_bcnn", ["gcf_ma", "prime_factor_ma", "vi_div2"]),
    ("nhan_nhanh", ["mult_ka", "mult_lattice_ka", "vi_mult"]),
    ("chia_nhanh", ["div_ma", "div_long_ma", "vi_div"]),
    ("tinh_chat", ["patterns_ma", "algebra_ma", "add_ka"]),
    ("phan_so_nang_cao", ["frac_add_ma", "frac_simp_ma", "frac_vi_vj"]),
    ("02_10_on_tap", ["mult_ka", "div_ma", "vi_general"]),
    # Chapter 03 — thinking & real-life math
    ("tam_giac_pascal", ["pascal_np", "fib_np", "patterns_ma"]),
    ("phuong_trinh_nang_cao", ["equation2_ma", "equation_ma", "algebra_ma"]),
    ("phuong_trinh", ["equation_ma", "equation2_ma", "algebra_ma"]),
    ("day_so_tim_quy_luat", ["patterns_ma", "fib_np", "number_line_ma"]),
    ("fibonacci", ["fib_np", "pascal_np", "patterns_ma"]),
    ("luoi_so", ["patterns_ma", "pascal_np", "data_ma"]),
    ("tim_quy_luat", ["patterns_ma", "fib_np", "number_line_ma"]),
    ("game_puzzle", ["patterns_ma", "prob_ka", "fib_np"]),
    ("bai_toan_do", ["equation_ma", "patterns_ma", "algebra_ma"]),
    ("toan_tu_duy", ["patterns_ma", "algebra_ma", "equation_ma"]),
    ("suy_luan", ["patterns_ma", "algebra_ma", "equation_ma"]),
    ("toan_vui", ["patterns_ma", "prob_ka", "fib_np"]),
    ("ky_nang_giai_toan", ["equation_ma", "patterns_ma", "vi_general"]),
    ("toan_hoc_lap_trinh", ["powers10_ma", "patterns_ma", "decimal_place_ma"]),
    ("toan_hoc_khoa_hoc_may_tinh", ["powers10_ma", "patterns_ma", "decimal_place_ma"]),
    ("toan_hoc_thien_van", ["place_value_ma", "powers10_ma", "vi_large_numbers"]),
    ("toan_hoc_khong_gian", ["volume_ma", "area_ma", "powers10_ma"]),
    ("toan_hoc_kien_truc", ["area_ma", "geom_vi_vj", "symmetry_ma"]),
    ("toan_hoc_nghe_thuat", ["symmetry_ma", "patterns_ma", "area_ma"]),
    ("toan_hoc_the_thao", ["mult_ka", "data_ma", "prob_ka"]),
    ("toan_hoc_am_nhac", ["patterns_ma", "fib_np", "mult_ka"]),
    ("toan_hoc_y_te", ["percent_ma", "data_ma", "prob_ka"]),
    ("toan_hoc_nau_an", ["frac_mult_ma", "ratio_ma", "percent_ma"]),
    ("toan_hoc_mua_sam", ["money_ma", "percent_ma", "decimal_arith_ma"]),
    ("toan_hoc_tai_chinh", ["money_ma", "percent_ma", "decimal_arith_ma"]),
    ("toan_hoc_giao_thong", ["distance_ma", "time_ma", "ratio_ma"]),
    ("toan_hoc_du_lich", ["distance_ma", "time_ma", "money_ma"]),
    ("toan_hoc_thoi_gian", ["time_ma", "distance_ma", "patterns_ma"]),
    ("toan_hoc_thoi_tiet", ["data_ma", "percent_ma", "patterns_ma"]),
    ("toan_hoc_nong_nghiep", ["percent_ma", "ratio_ma", "mult_ka"]),
    ("toan_hoc_tro_choi", ["prob_ka", "patterns_ma", "mult_ka"]),
    ("toan_hoc_phim_anh", ["ratio_ma", "percent_ma", "patterns_ma"]),
    ("toan_hoc_khoa_hoc", ["data_ma", "powers10_ma", "patterns_ma"]),
    ("toan_hoc_trong_kho", ["mult_ka", "percent_ma", "data_ma"]),
    ("cuoc_song_khong_toan", ["patterns_ma", "algebra_ma", "vi_general"]),
    ("tong_ket_chuong_3", ["equation_ma", "patterns_ma", "vi_general"]),
    ("bai_hoc_cuoi_cung", ["patterns_ma", "algebra_ma", "vi_general"]),
    ("03_10_on_tap", ["patterns_ma", "equation_ma", "vi_general"]),
    # Chapter 04 — fractions & algebra
    ("phan_so_bang_nhau", ["frac_simp_ma", "frac_equiv_vi", "frac_line_ma"]),
    ("so_sanh_phan_so", ["frac_what_ma", "frac_line_ma", "frac_vi_vj"]),
    ("cong_tru_phan_so", ["frac_add_ma", "frac_what_ma", "frac_vi_vj"]),
    ("hon_so", ["frac_what_ma", "frac_line_ma", "frac_vi_vj"]),
    ("dai_so_bien_so", ["algebra_ma", "equation_ma", "number_line_ma"]),
    ("ty_le_thuan_nghich", ["ratio_ma", "proportion_ma", "percent_ma"]),
    ("04_10_on_tap", ["frac_parts_ma", "frac_vi_vj", "vi_general"]),
    ("phan_so", ["frac_parts_ma", "frac_what_ma", "frac_vi_vj"]),
    # Chapter 05 — number theory
    ("so_chinh_phuong", ["square_ma", "patterns_ma", "mult_ka"]),
    ("uoc_chung_lon_nhat", ["gcf_ma", "prime_factor_ma", "vi_div2"]),
    ("boi_chung_nho_nhat", ["prime_factor_ma", "gcf_ma", "vi_div2"]),
    ("uoc_so_va_boi_so", ["gcf_ma", "prime_factor_ma", "patterns_ma"]),
    ("so_am", ["negative_ma", "int_add_ma", "number_line_ma"]),
    # Chapter 06 — decimals, measure, money
    ("cong_tru_so_thap_phan", ["decimal_arith_ma", "decimal_place_ma", "frac_line_ma"]),
    ("nhan_chia_so_thap_phan", ["decimal_arith_ma", "decimal_place_ma", "percent_ma"]),
    ("ti_le_phan_tram_nang_cao", ["percent_ma", "money_ma", "data_ma"]),
    ("phan_tram_ung_dung", ["percent_ma", "money_ma", "data_ma"]),
    ("ti_le_thuan_va", ["ratio_ma", "proportion_ma", "percent_ma"]),
    ("ti_so_va_ti_le", ["ratio_ma", "proportion_ma", "percent_ma"]),
    ("phan_so_thap_phan", ["decimal_place_ma", "frac_line_ma", "frac_vi_vj"]),
    ("ti_le_phan_tram", ["percent_ma", "decimal_arith_ma", "data_ma"]),
    ("so_thap_phan", ["decimal_place_ma", "decimal_arith_ma", "frac_line_ma"]),
    ("do_luong_don_vi", ["distance_ma", "time_ma", "area_ma"]),
    ("thoi_gian_xem_dong_ho", ["time_ma", "distance_ma", "vi_general"]),
    ("06_10_on_tap", ["decimal_place_ma", "percent_ma", "time_ma"]),
    ("01_09_tien", ["money_ma", "decimal_arith_ma", "percent_ma"]),
    ("01_08_thoi_gian", ["time_ma", "distance_ma", "vi_general"]),
    ("01_10_do_luong", ["distance_ma", "time_ma", "area_ma"]),
    ("01_19_ty_le", ["ratio_ma", "proportion_ma", "percent_ma"]),
    # Chapter 07 — stats & probability
    ("ma_nhi_phan", ["powers10_ma", "patterns_ma", "decimal_place_ma"]),
    ("du_lieu_thu_thap", ["data_ma", "prob_ka", "percent_ma"]),
    ("thong_ke", ["data_ma", "prob_ka", "percent_ma"]),
    ("bieu_do", ["data_ma", "prob_ka", "percent_ma"]),
    ("xac_suat", ["prob_ka", "data_ma", "patterns_ma"]),
    ("07_10_on_tap", ["data_ma", "prob_ka", "powers10_ma"]),
    # Chapter 08 — geometry
    ("hinh_tru", ["volume_ma", "circle_ma", "area_ma"]),
    ("hinh_cau_va_hinh_non", ["volume_ma", "circle_ma", "area_ma"]),
    ("the_tich_hinh_hop", ["volume_ma", "area_ma", "circle_ma"]),
    ("dien_tich_hinh_tam_giac_va_hinh_tron", ["area_ma", "circle_ma", "geom_vi_vj"]),
    ("hinh_thoi_va_hinh_thang", ["area_ma", "geom_vi_vj", "triangle_ka"]),
    ("hinh_chu_nhat_va_hinh_binh_hanh", ["area_ma", "geom_vi_vj", "triangle_ka"]),
    ("hinh_tam_giac_hinh_vuong", ["triangle_ka", "area_ma", "geom_vi_vj"]),
    ("dien_tich_nang_cao", ["area_ma", "circle_ma", "geom_vi_vj"]),
    ("goc_duong_thang", ["triangle_ka", "symmetry_ma", "coord_ma"]),
    ("chu_vi_dien_tich", ["area_ma", "circle_ma", "geom_vi_vj"]),
    ("hinh_khoi", ["volume_ma", "area_ma", "circle_ma"]),
    ("hinh_hoc", ["area_ma", "geom_vi_vj", "triangle_ka"]),
    # Chapter 09 — combinatorics & counting
    ("09_07_on_tap", ["prob_ka", "mult_ka", "patterns_ma"]),
    ("09_06_cay_kha_nang", ["patterns_ma", "mult_ka", "prob_ka"]),
    ("09_05_to_hop", ["pascal_np", "prob_ka", "patterns_ma"]),
    ("09_04_hoan_vi", ["mult_ka", "patterns_ma", "fib_np"]),
    ("09_03_nguyen_ly_nhan", ["mult_ka", "mult_intro_ka", "prob_ka"]),
    ("09_02_nguyen_ly_cong", ["add_ka", "prob_ka", "patterns_ma"]),
    ("09_01_dem_co_he_thong", ["prob_ka", "patterns_ma", "mult_ka"]),
    ("counting-carefully", ["prob_ka", "patterns_ma", "mult_ka"]),
    ("addition-principle", ["add_ka", "prob_ka", "patterns_ma"]),
    ("multiplication-principle", ["mult_ka", "mult_intro_ka", "prob_ka"]),
    ("order-matters", ["mult_ka", "patterns_ma", "fib_np"]),
    ("unordered-choices", ["pascal_np", "prob_ka", "patterns_ma"]),
    ("tree-diagrams", ["patterns_ma", "mult_ka", "prob_ka"]),
    ("chapter-review", ["prob_ka", "mult_ka", "patterns_ma"]),
]


def resolve_videos_from_stem(stem: str) -> list[str] | None:
    norm = normalize(stem)
    for pattern, keys in STEM_VIDEO_RULES:
        if pattern in norm:
            valid = [k for k in keys if k in VIDEOS]
            if len(valid) >= 2:
                return valid[:TARGET_VIDEOS]
    return None


CHAPTER_DEFAULTS: dict[str, list[str]] = {
    "chapter00": ["algebra_ma", "number_line_ma"],
    "chapter01": ["even_odd_ka", "patterns_ma", "add_ka"],
    "chapter02": ["mult_ka", "div_ma", "prime_factor_ma"],
    "chapter03": ["algebra_ma", "equation_ma", "patterns_ma"],
    "chapter04": ["frac_parts_ma", "frac_vi_vj", "algebra_ma"],
    "chapter05": ["square_ma", "prime_factor_ma", "gcf_ma"],
    "chapter06": ["decimal_place_ma", "percent_ma", "time_ma"],
    "chapter07": ["data_ma", "prob_ka", "powers10_ma"],
    "chapter08": ["area_ma", "volume_ma", "triangle_ka"],
    "chapter09": ["prob_ka", "mult_ka", "patterns_ma"],
}


def strip_accents(text: str) -> str:
    normalized = unicodedata.normalize("NFD", text)
    return "".join(c for c in normalized if unicodedata.category(c) != "Mn")


def normalize(text: str) -> str:
    text = strip_accents(text.lower())
    text = re.sub(r"[^a-z0-9\s/_-]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def keyword_matches(text: str, keyword: str) -> bool:
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


def count_youtube(content: str) -> int:
    return len(re.findall(r"youtube\.com/watch", content))


def score_videos(
    search_text: str,
    chapter_category: str,
    title_text: str = "",
    filename_text: str = "",
    lang: str = "vi",
) -> list[str]:
    scores: dict[str, int] = {}

    for weight, keywords, video_keys in TOPIC_RULES:
        for kw in keywords:
            if not keyword_matches(search_text, kw):
                continue
            title_hit = bool(title_text and keyword_matches(title_text, kw))
            filename_hit = bool(filename_text and keyword_matches(filename_text, kw))
            for i, key in enumerate(video_keys):
                boost = 0
                if i == 0:
                    if title_hit:
                        boost += TITLE_BOOST
                    if filename_hit:
                        boost += FILENAME_BOOST
                scores[key] = scores.get(key, 0) + weight - i + boost

    for key in CHAPTER_DEFAULTS.get(chapter_category, ["patterns_ma", "number_line_ma"]):
        scores[key] = scores.get(key, 0) + 1

    ranked = sorted(scores.items(), key=lambda x: (-x[1], x[0]))

    primary: list[str] = []
    if title_text:
        for _w, keywords, video_keys in TOPIC_RULES:
            if any(keyword_matches(title_text, kw) for kw in keywords):
                primary = list(video_keys)
                break

    chosen: list[str] = []
    for key in primary + [k for k, _ in ranked]:
        if key not in VIDEOS:
            continue
        v = VIDEOS[key]
        if lang == "vi" and not v.vi_ok:
            continue
        if lang == "en" and not v.en_ok:
            continue
        if key not in chosen:
            chosen.append(key)
        if len(chosen) >= TARGET_VIDEOS + 1:
            break

    # Ensure vi lessons get at least one Vietnamese channel when possible
    if lang == "vi" and not any(VIDEOS[k].en_ok is False or "Viet" in VIDEOS[k].channel or "Thầy" in VIDEOS[k].channel or "Cô" in VIDEOS[k].channel for k in chosen[:3]):
        for key, _ in ranked:
            v = VIDEOS.get(key)
            if not v or not v.vi_ok or v.en_ok:
                continue
            if "Viet" in v.channel or "Thầy" in v.channel or "Cô" in v.channel or "Dâu" in v.channel or "Luyện" in v.channel or "TOÁN" in v.channel:
                if key not in chosen:
                    if len(chosen) >= TARGET_VIDEOS:
                        chosen[-1] = key
                    else:
                        chosen.append(key)
                    break

    return chosen[:TARGET_VIDEOS]


def video_url(video_id: str) -> str:
    return f"https://www.youtube.com/watch?v={video_id}"


def format_video_section(video_keys: list[str], lang: str) -> str:
    lines: list[str] = []
    if lang == "vi":
        lines.append(VIDEO_SECTION_VI)
        lines.append("")
        lines.append("Xem thêm trên YouTube để củng cố bài học:")
        lines.append("")
        for i, key in enumerate(video_keys, 1):
            v = VIDEOS[key]
            lines.append(f"{i}. [{v.title_vi}]({video_url(v.video_id)}) — {v.channel}")
        lines.append("")
        lines.append("*Video: YouTube — kênh giáo dục; nội dung phù hợp lứa tuổi 8–10*")
    else:
        lines.append(VIDEO_SECTION_EN)
        lines.append("")
        lines.append("Popular educational videos to reinforce this lesson:")
        lines.append("")
        for i, key in enumerate(video_keys, 1):
            v = VIDEOS[key]
            lines.append(f"{i}. [{v.title_en}]({video_url(v.video_id)}) — {v.channel}")
        lines.append("")
        lines.append("*Videos: YouTube — educational channels suitable for ages 8–10*")
    lines.append("")
    return "\n".join(lines)


INSERT_BEFORE_PATTERNS = [
    re.compile(r"^## Góc cha mẹ\b", re.M | re.I),
    re.compile(r"^## Bài tập", re.M | re.I),
    re.compile(r"^## Câu hỏi suy nghĩ", re.M | re.I),
    re.compile(r"^## Exercises\b", re.M | re.I),
    re.compile(r"^## For Parents\b", re.M | re.I),
    re.compile(r"^## Parent", re.M | re.I),
    re.compile(r"^## Think\b", re.M | re.I),
]


def find_insert_position(body: str) -> int:
    for pattern in INSERT_BEFORE_PATTERNS:
        m = pattern.search(body)
        if m:
            return m.start()
    # Fallback: append at end
    return len(body.rstrip())


def strip_video_section(content: str) -> str:
    return VIDEO_SECTION_RE.sub("", content)


def collapse_separators(text: str) -> str:
    """Collapse duplicate horizontal rules left from re-insertion."""
    text = re.sub(r"(\n---\n)(?:\s*\n---\n)+", r"\1", text)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text


def add_videos(content: str, path: Path, *, reapply: bool = False) -> tuple[str, int]:
    if reapply:
        content = strip_video_section(content)

    if not reapply and count_youtube(content) >= MIN_EXISTING:
        return content, 0

    meta, body = parse_front_matter(content)
    if VIDEO_SECTION_VI in body or VIDEO_SECTION_EN in body:
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

    override = LESSON_VIDEO_OVERRIDES.get(path.stem) or resolve_videos_from_stem(path.stem)
    if override:
        keys = [k for k in override if k in VIDEOS]
    else:
        keys = score_videos(search_text, chapter_cat, title_text, filename_text, lang)
    if len(keys) < 2:
        return content, 0

    section = format_video_section(keys[:TARGET_VIDEOS], lang)
    pos = find_insert_position(body)
    before = body[:pos].rstrip()
    after = body[pos:].lstrip()
    if after.startswith("---"):
        new_body = before + "\n\n" + section + "\n\n" + after
    else:
        new_body = before + "\n\n---\n\n" + section + "\n\n" + after

    new_body = collapse_separators(new_body)
    fm_end = content.find("\n---", 3)
    if fm_end == -1:
        return new_body, len(keys[:TARGET_VIDEOS])
    return content[: fm_end + 4] + "\n" + new_body, len(keys[:TARGET_VIDEOS])


def iter_lesson_files() -> list[Path]:
    return sorted(CONTENTS.glob("**/chapter*/_posts/*.md"))


def main() -> None:
    parser = argparse.ArgumentParser(description="Add YouTube video links to lesson posts")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--file", type=str)
    parser.add_argument("--reapply", action="store_true")
    args = parser.parse_args()

    targets = [Path(args.file).resolve()] if args.file else iter_lesson_files()
    changed = 0
    added = 0
    skipped = 0

    for path in targets:
        if not path.exists():
            print(f"SKIP missing: {path}")
            continue
        original = path.read_text(encoding="utf-8")
        if not args.reapply and count_youtube(original) >= MIN_EXISTING:
            skipped += 1
            continue
        updated, n = add_videos(original, path, reapply=args.reapply)
        if n == 0:
            skipped += 1
            continue
        changed += 1
        added += n
        print(f"UPDATED {path.relative_to(ROOT)} (+{n} videos)")
        if not args.dry_run:
            path.write_text(updated, encoding="utf-8")

    print(f"\nDone: {changed} files, {added} videos added, {skipped} skipped.")


if __name__ == "__main__":
    main()