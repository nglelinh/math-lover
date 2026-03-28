"""Validate Vietnamese lesson interactive coverage."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LESSON_GLOB = "contents/vi/chapter*/_posts/*.md"
MAPPING_PATH = ROOT / "_data" / "vi_interactive_lessons.json"
REQUIRED_MARKER = "{% include vi-interactive-lesson.html %}"
VALID_TEMPLATES = {
    "number-lab",
    "array-lab",
    "fraction-lab",
    "measurement-lab",
    "geometry-lab",
    "data-lab",
    "sequence-lab",
    "balance-lab",
    "challenge-lab",
}


def is_hidden(text: str) -> bool:
    return re.search(r"^hidden:\s*true\s*$", text, re.MULTILINE) is not None


def load_mapping() -> dict[str, dict[str, str]]:
    if not MAPPING_PATH.exists():
        raise FileNotFoundError(f"Missing mapping file: {MAPPING_PATH}")

    with MAPPING_PATH.open(encoding="utf-8") as handle:
        data = json.load(handle)

    if not isinstance(data, dict):
        raise ValueError("Interactive lesson mapping must be a JSON object.")

    return data


def main() -> int:
    mapping = load_mapping()
    published_failures: list[str] = []
    mapping_failures: list[str] = []
    template_counter: Counter[str] = Counter()
    published_count = 0
    hidden_count = 0

    for path in sorted(ROOT.glob(LESSON_GLOB)):
        relative_path = path.as_posix().replace(f"{ROOT.as_posix()}/", "")
        text = path.read_text(encoding="utf-8")
        hidden = is_hidden(text)
        config = mapping.get(relative_path)

        if hidden:
            hidden_count += 1
        else:
            published_count += 1

        if config is None:
            mapping_failures.append(f"{relative_path}: missing mapping entry")
            if not hidden:
                published_failures.append(f"{relative_path}: missing mapping entry")
            continue

        template = config.get("template")
        container_id = config.get("container_id")
        guidance = config.get("guidance")

        if template not in VALID_TEMPLATES:
            mapping_failures.append(
                f"{relative_path}: invalid template {template!r}"
            )
        else:
            template_counter[template] += 1

        if not container_id:
            mapping_failures.append(f"{relative_path}: missing container_id")

        if not guidance:
            mapping_failures.append(f"{relative_path}: missing guidance text")

        if REQUIRED_MARKER not in text:
            issue = f"{relative_path}: missing interactive include marker"
            mapping_failures.append(issue)
            if not hidden:
                published_failures.append(issue)

    if published_failures or mapping_failures:
        print("Vietnamese interactive coverage check failed.", file=sys.stderr)
        if published_failures:
            print("\nPublished lesson issues:", file=sys.stderr)
            for issue in published_failures:
                print(f"- {issue}", file=sys.stderr)
        if mapping_failures:
            print("\nAll lesson mapping issues:", file=sys.stderr)
            for issue in mapping_failures:
                print(f"- {issue}", file=sys.stderr)
        return 1

    print(
        "Vietnamese interactive coverage OK: "
        f"{published_count} published lessons, {hidden_count} hidden lessons."
    )
    print("Template inventory:")
    for template, count in sorted(template_counter.items()):
        print(f"- {template}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
