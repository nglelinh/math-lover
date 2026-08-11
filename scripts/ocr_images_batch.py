#!/usr/bin/env python3
"""OCR exam images under on-thi-lop-6/de-thi/_downloads/img/."""
from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMG_DIR = ROOT / "on-thi-lop-6/de-thi/_downloads/img"
OCR_DIR = ROOT / "on-thi-lop-6/de-thi/_downloads/ocr"
OCR_DIR.mkdir(parents=True, exist_ok=True)

PRIORITY = [
    "tran", "dai", "nghia", "tuoitre", "dap-an-toan", "nguyen-tat",
    "amsterdam", "cau-giay", "luong-the", "marie", "thanh-xuan",
    "nam-tu-liem", "archimedes", "phan-toan", "phan-trac", "giang-vo",
    "hoatieu", "loigiaihay",
]


def out_name(path: Path) -> str:
    h = hashlib.md5(path.name.encode()).hexdigest()[:10]
    base = path.stem
    m = re.search(
        r"(de-thi-vao-lop-6[^.]+|dap-an-[^.]+|bai-\d+[^.]*|nam-\d{4}[^.]*)$",
        base,
        re.I,
    )
    label = m.group(1) if m else base[-60:]
    label = re.sub(r"[^a-zA-Z0-9._-]+", "_", label)[:70]
    return f"{label}__{h}.md"


def ocr_one(path: Path) -> tuple[str, bool, int, str]:
    out = OCR_DIR / out_name(path)
    if out.exists() and out.stat().st_size > 150:
        return path.name, True, out.stat().st_size, "skip"
    tmp = OCR_DIR / f"_t_{hashlib.md5(path.name.encode()).hexdigest()[:12]}"
    try:
        subprocess.run(
            ["tesseract", str(path), str(tmp), "-l", "vie+eng", "--psm", "6"],
            capture_output=True,
            text=True,
            timeout=120,
            check=False,
        )
        txt = Path(str(tmp) + ".txt")
        if not txt.exists():
            return path.name, False, 0, "fail"
        text = txt.read_text(errors="ignore")
        txt.unlink(missing_ok=True)
        out.write_text(
            f"# OCR: {path.name}\n\n> Source image: `{path.name}`\n\n{text}\n",
            encoding="utf-8",
        )
        return path.name, True, out.stat().st_size, "new"
    except Exception:
        return path.name, False, 0, "fail"


def parse_args(argv: list[str]) -> tuple[int, bool]:
    only_all = "--all" in argv
    nums = [a for a in argv if re.fullmatch(r"\d+", a)]
    limit = int(nums[0]) if nums else 9999
    return limit, not only_all


def write_index() -> int:
    mds = [p for p in OCR_DIR.glob("*.md") if p.name != "INDEX.md"]
    mds_by_size = sorted(mds, key=lambda p: -p.stat().st_size)
    lines = [
        f"# OCR index ({len(mds)} files)\n",
        "## Lớn nhất\n",
    ]
    for p in mds_by_size[:50]:
        lines.append(f"- [{p.name}](./{p.name}) — {p.stat().st_size} B")
    lines.append("\n## Tất cả\n")
    for p in sorted(mds, key=lambda p: p.name):
        lines.append(f"- [{p.name}](./{p.name}) ({p.stat().st_size} B)")
    (OCR_DIR / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(mds)


def main() -> int:
    limit, only_priority = parse_args(sys.argv[1:])
    imgs: list[Path] = []
    for p in sorted(IMG_DIR.iterdir()):
        if not p.is_file():
            continue
        n = p.name.lower()
        if only_priority and not any(k in n for k in PRIORITY):
            continue
        imgs.append(p)
    imgs = imgs[:limit]
    mode = "priority" if only_priority else "ALL"
    print(f"OCR {len(imgs)} images ({mode}), workers=4", flush=True)
    ok = fail = skip = 0
    with ThreadPoolExecutor(max_workers=4) as ex:
        futs = [ex.submit(ocr_one, p) for p in imgs]
        for i, fut in enumerate(as_completed(futs), 1):
            name, success, size, status = fut.result()
            if status == "skip":
                skip += 1
            elif success:
                ok += 1
            else:
                fail += 1
            if i % 25 == 0 or status == "fail":
                print(
                    f"[{i}/{len(imgs)}] new={ok} skip={skip} fail={fail} "
                    f"{name[:60]} ({size})",
                    flush=True,
                )
    total = write_index()
    print(f"DONE new={ok} skip={skip} fail={fail} total_md={total}")
    return 0 if ok or skip else 1


if __name__ == "__main__":
    raise SystemExit(main())
