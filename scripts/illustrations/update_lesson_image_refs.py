#!/usr/bin/env python3
"""Switch lesson markdown image references from PNG to SVG when available."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def build_replacements():
    replacements = {}
    for svg_path in (ROOT / "img" / "chapter_img").rglob("*.svg"):
        png_ref = "chapter_img/" + str(svg_path.relative_to(ROOT / "img" / "chapter_img").with_suffix(".png"))
        svg_ref = "chapter_img/" + str(svg_path.relative_to(ROOT / "img" / "chapter_img"))
        replacements[png_ref] = svg_ref
    return replacements


def rewrite_markdown_files(replacements):
    updated = []
    for base in (ROOT / "contents" / "vi", ROOT / "contents" / "en"):
        if not base.exists():
            continue
        for path in base.rglob("*.md"):
            text = path.read_text()
            new_text = text
            for png_ref, svg_ref in replacements.items():
                new_text = new_text.replace(png_ref, svg_ref)
            if new_text != text:
                path.write_text(new_text)
                updated.append(path.relative_to(ROOT))
    return updated


def main():
    replacements = build_replacements()
    updated = rewrite_markdown_files(replacements)
    print(f"Updated {len(updated)} markdown files.")
    for path in updated:
        print(path)


if __name__ == "__main__":
    main()
