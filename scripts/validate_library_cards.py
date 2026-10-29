#!/usr/bin/env python3
"""Validate the structural completeness of IdeaFoundry component cards."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


EN_FIELDS = (
    "Component Summary",
    "Source Type",
    "Source Papers",
    "Source-Paper Role",
    "Evidence Anchor",
    "Theoretical Foundation",
    "Input",
    "Output",
    "Core Mechanism",
    "Suitable Problem Types",
    "Applicability Conditions",
    "Failure or Mismatch Conditions",
    "Known Variants",
    "Research Reuse Pattern",
    "Task-Independent Abstraction",
    "Theoretical Grounding Level",
    "Tags",
)

ZH_FIELDS = (
    "组件摘要",
    "来源类型",
    "来源论文",
    "来源论文角色",
    "证据锚点",
    "理论基础",
    "输入",
    "输出",
    "核心机制",
    "适用问题类型",
    "适用条件",
    "失效或不匹配条件",
    "已知变体",
    "研究复用模式",
    "任务无关抽象",
    "理论扎实程度",
    "标签",
)

CARD_RE = re.compile(
    r"(?ms)^### C(?P<id>\d+)\..*?(?=^### C\d+\.|^## 5\.|\Z)"
)
HEADING_RE = re.compile(r"(?m)^#### (?P<name>[^\r\n]+)\s*$")
MOJIBAKE = ("\ufffd", "Ã", "Â", "â€", "ðŸ")


def parse_ids(raw: str | None) -> set[int] | None:
    if not raw:
        return None
    result: set[int] = set()
    for item in raw.split(","):
        item = item.strip()
        if not item:
            continue
        if "-" in item:
            start, end = (int(part) for part in item.split("-", 1))
            result.update(range(start, end + 1))
        else:
            result.add(int(item))
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("library", type=Path)
    parser.add_argument(
        "--language", choices=("en", "zh"), required=True,
        help="Select the canonical heading set.",
    )
    parser.add_argument(
        "--ids", help="Comma-separated IDs or inclusive ranges, e.g. 269-280,301."
    )
    args = parser.parse_args()

    text = args.library.read_text(encoding="utf-8-sig")
    failures: list[str] = []
    for fragment in MOJIBAKE:
        if fragment in text:
            failures.append(f"file contains possible mojibake fragment: {fragment!r}")

    selected = parse_ids(args.ids)
    expected = ZH_FIELDS if args.language == "zh" else EN_FIELDS
    cards = {int(match.group("id")): match.group(0) for match in CARD_RE.finditer(text)}
    target_ids = sorted(selected if selected is not None else cards)

    for card_id in target_ids:
        card = cards.get(card_id)
        if card is None:
            failures.append(f"C{card_id:03d}: card not found")
            continue
        headings = [match.group("name").strip() for match in HEADING_RE.finditer(card)]
        missing = [field for field in expected if field not in headings]
        duplicate = sorted({field for field in headings if headings.count(field) > 1})
        unexpected = [field for field in headings if field not in expected]
        if missing:
            failures.append(f"C{card_id:03d}: missing headings: {', '.join(missing)}")
        if duplicate:
            failures.append(f"C{card_id:03d}: duplicate headings: {', '.join(duplicate)}")
        if unexpected:
            failures.append(f"C{card_id:03d}: unexpected/merged headings: {', '.join(unexpected)}")

        bodies: dict[str, str] = {}
        for index, field in enumerate(expected):
            marker = f"#### {field}"
            if marker not in card:
                continue
            start = card.index(marker) + len(marker)
            later = [card.find(f"#### {name}", start) for name in expected[index + 1 :]]
            later = [position for position in later if position >= 0]
            end = min(later) if later else len(card)
            body = card[start:end].strip().strip("-").strip()
            bodies[field] = body
            if not body or body in {"...", "TBD", "TODO"}:
                failures.append(f"C{card_id:03d}: empty or placeholder field: {field}")

        level_field = "理论扎实程度" if args.language == "zh" else "Theoretical Grounding Level"
        level_body = bodies.get(level_field, "")
        levels = re.findall(r"\bLevel\s+([ABC])\b", level_body)
        if level_body and (len(levels) != 1 or re.search(r"Level\s+[ABC]\s*/\s*[ABC]", level_body)):
            failures.append(
                f"C{card_id:03d}: grounding field must choose exactly one of Level A, Level B, or Level C"
            )

        source_field = "来源论文" if args.language == "zh" else "Source Papers"
        source_body = bodies.get(source_field, "")
        invalid_source_patterns = (
            r"(?i)(?:^|\n)\s*-\s*C\d+\s*(?:[,，;；.]|$)",
            r"(?i)(?:^|\n)\s*-\s*(?:paper\s*\d+|论文\s*\d+)\b",
            r"(?i)(?:^|\n)\s*-\s*\d+\.pdf\b",
            r"(?i)\b\d+\.pdf\b",
            r"\.\.\.|…",
        )
        if source_body and any(re.search(pattern, source_body) for pattern in invalid_source_patterns):
            failures.append(
                f"C{card_id:03d}: source must use the complete official paper title, not an ID, filename, abbreviation, or ellipsis"
            )

    if failures:
        print("IdeaFoundry card validation failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print(f"Validated {len(target_ids)} {args.language} card(s) in {args.library}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
