#!/usr/bin/env python3
"""OCR exam PDFs and images under on-thi-lop-6/de-thi/_downloads/.

Requires:
  - tesseract with vie+eng (`brew install tesseract tesseract-lang`)
  - pymupdf for PDFs (`pip install pymupdf`) — use env that has it, e.g.:
      /Users/.../miniconda3/bin/python3 scripts/ocr_exam_downloads.py
"""
from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DL = ROOT / "on-thi-lop-6" / "de-thi" / "_downloads"
OCR_DIR = DL / "ocr"
OCR_DIR.mkdir(parents=True, exist_ok=True)

IMG_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff", ".gif", ".bmp"}
PDF_EXTS = {".pdf"}
LANG = "vie+eng"


def out_name(p: Path, prefix: str = "") -> str:
    h = hashlib.md5(p.name.encode()).hexdigest()[:10]
    label = re.sub(r"[^a-zA-Z0-9._-]+", "_", p.stem)[-60:]
    return f"{prefix}{label}__{h}.md"


def run_tesseract(image: Path) -> str | None:
    tmp = OCR_DIR / f"_t_{hashlib.md5(str(image).encode()).hexdigest()[:12]}"
    try:
        subprocess.run(
            ["tesseract", str(image), str(tmp), "-l", LANG, "--psm", "6"],
            capture_output=True,
            text=True,
            timeout=180,
            check=False,
        )
        txt_path = Path(str(tmp) + ".txt")
        if not txt_path.exists():
            return None
        text = txt_path.read_text(errors="ignore")
        txt_path.unlink(missing_ok=True)
        return text
    except Exception as e:
        print(f"  tesseract fail {image.name}: {e}")
        return None


def ocr_pdf(pdf: Path, out_md: Path) -> bool:
    try:
        import fitz
    except ImportError:
        print("pymupdf missing")
        return False

    doc = fitz.open(pdf)
    parts: list[str] = []
    for i, page in enumerate(doc):
        text = page.get_text("text") or ""
        if len(text.strip()) < 80:
            mat = fitz.Matrix(2, 2)
            pix = page.get_pixmap(matrix=mat, alpha=False)
            img_path = OCR_DIR / f"_tmp_{hashlib.md5(pdf.name.encode()).hexdigest()[:8]}_p{i+1}.png"
            pix.save(str(img_path))
            ocr_text = run_tesseract(img_path)
            if ocr_text:
                text = ocr_text
            try:
                img_path.unlink()
            except OSError:
                pass
        parts.append(f"--- Trang {i+1} ---\n{text.strip()}\n")
    doc.close()
    body = "\n".join(parts).strip()
    if len(body) < 30:
        return False
    rel = pdf.relative_to(ROOT) if pdf.is_relative_to(ROOT) else pdf
    out_md.write_text(
        f"# OCR: {pdf.name}\n\n> Nguồn file: `{rel}`\n\n{body}\n",
        encoding="utf-8",
    )
    return True


def ocr_image(path: Path, out_md: Path) -> bool:
    text = run_tesseract(path)
    if not text or len(text.strip()) < 10:
        return False
    out_md.write_text(
        f"# OCR: {path.name}\n\n> File: `{path.name}`\n\n{text}\n",
        encoding="utf-8",
    )
    return True


def process_one(path: Path) -> tuple[str, str, int]:
    """Return (name, status, size). status: skip|ok|fail"""
    prefix = "pdf-" if path.suffix.lower() in PDF_EXTS else "img-"
    if "drive" in path.parts:
        prefix = "drive-" + prefix
    out = OCR_DIR / out_name(path, prefix=prefix)
    if out.exists() and out.stat().st_size > 150:
        return path.name, "skip", out.stat().st_size
    try:
        if path.suffix.lower() in PDF_EXTS:
            success = ocr_pdf(path, out)
        else:
            success = ocr_image(path, out)
        if success and out.exists():
            return path.name, "ok", out.stat().st_size
        return path.name, "fail", 0
    except Exception as e:
        return path.name, f"err:{e}", 0


def write_index() -> int:
    mds = [p for p in OCR_DIR.glob("*.md") if p.name != "INDEX.md"]
    mds_by_size = sorted(mds, key=lambda p: -p.stat().st_size)
    lines = [f"# OCR output index ({len(mds)} files)\n", "## Lớn nhất\n"]
    for p in mds_by_size[:50]:
        lines.append(f"- [{p.name}](./{p.name}) — {p.stat().st_size} B")
    lines.append("\n## Tất cả\n")
    for p in sorted(mds, key=lambda p: p.name):
        lines.append(f"- [{p.name}](./{p.name}) ({p.stat().st_size} B)")
    (OCR_DIR / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(mds)


def main() -> int:
    files: list[Path] = []
    for sub in ["pdf", "img", "drive"]:
        d = DL / sub
        if not d.exists():
            continue
        for p in d.rglob("*"):
            if p.is_file() and p.suffix.lower() in IMG_EXTS | PDF_EXTS:
                files.append(p)

    files = sorted(files)
    print(f"Found {len(files)} media files (pdf+img+drive)", flush=True)

    # Process PDFs first (usually fewer), then images with threads
    pdfs = [p for p in files if p.suffix.lower() in PDF_EXTS]
    imgs = [p for p in files if p.suffix.lower() in IMG_EXTS]

    ok = fail = skip = 0

    print(f"Phase A: {len(pdfs)} PDFs (sequential)", flush=True)
    for i, p in enumerate(pdfs, 1):
        name, status, size = process_one(p)
        if status == "skip":
            skip += 1
        elif status == "ok":
            ok += 1
        else:
            fail += 1
        print(f"  [pdf {i}/{len(pdfs)}] {status} {name[:70]} ({size})", flush=True)

    print(f"Phase B: {len(imgs)} images (workers=4)", flush=True)
    with ThreadPoolExecutor(max_workers=4) as ex:
        futs = [ex.submit(process_one, p) for p in imgs]
        for i, fut in enumerate(as_completed(futs), 1):
            name, status, size = fut.result()
            if status == "skip":
                skip += 1
            elif status == "ok":
                ok += 1
            else:
                fail += 1
            if i % 25 == 0 or status not in ("skip", "ok"):
                print(
                    f"  [img {i}/{len(imgs)}] new_or_ok_total={ok} skip={skip} fail={fail} "
                    f"{status} {name[:50]}",
                    flush=True,
                )

    total = write_index()
    print(f"\nDone: ok={ok} fail={fail} skip={skip} total_md={total} ocr_dir={OCR_DIR}")
    return 0 if ok or skip else 1


if __name__ == "__main__":
    raise SystemExit(main())
