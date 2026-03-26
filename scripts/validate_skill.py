#!/usr/bin/env python3
"""
Validate skill files follow the required 6-section structure.

Usage:
    python3 scripts/validate_skill.py                    # Validate all skills/
    python3 scripts/validate_skill.py skills/my-skill.md # Validate specific file
"""

import re
import sys
import os
from pathlib import Path

# ── Colors ───────────────────────────────────────────────
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
BOLD = "\033[1m"
RESET = "\033[0m"

# ── Required Sections ────────────────────────────────────
REQUIRED_SECTIONS = [
    ("Context / Bối cảnh", r"##\s+Context\s*/\s*Bối cảnh"),
    ("THE IRON LAW", r"##\s+⛔\s+THE IRON LAW"),
    ("Guardrails", r"##\s+🛡\s+Guardrails"),
    ("Red Flags — STOP", r"##\s+🚩\s+Red Flags"),
    ("Remember", r"##\s+Remember"),
    ("Related Skills", r"##\s+🔗\s+Related Skills"),
]

OPTIONAL_SECTIONS = [
    ("Khi nào dùng Skill này", r"##\s+🎯\s+Khi nào dùng"),
    ("Pre-delivery Checklist", r"##\s+✅\s+Pre-delivery"),
    ("Error Journal", r"##\s+📓\s+Error Journal"),
]

CONTEXT_FIELDS = ["Category", "Priority", "Triggers", "Output", "Scope"]
VERSION_FIELDS = ["Version", "Last Updated"]


def validate_skill(filepath):
    """Validate a single skill file. Returns (pass_count, fail_count, warnings)."""
    path = Path(filepath)
    if not path.exists():
        print(f"{RED}  File not found: {filepath}{RESET}")
        return 0, 1, 0

    content = path.read_text(encoding="utf-8")
    lines = content.split("\n")
    total_lines = len(lines)

    print(f"\n{BLUE}{BOLD}Validating: {path.name}{RESET}")
    print(f"  Lines: {total_lines}")

    passes = 0
    fails = 0
    warnings = 0

    # ── Check required sections ──────────────────────────
    for name, pattern in REQUIRED_SECTIONS:
        if re.search(pattern, content):
            print(f"  {GREEN}✅ {name}{RESET}")
            passes += 1
        else:
            print(f"  {RED}❌ {name} — MISSING{RESET}")
            fails += 1

    # ── Check optional sections ──────────────────────────
    for name, pattern in OPTIONAL_SECTIONS:
        if re.search(pattern, content):
            print(f"  {GREEN}✅ {name} (optional){RESET}")

    # ── Check Context metadata fields ────────────────────
    context_match = re.search(
        r"##\s+Context\s*/\s*Bối cảnh(.*?)(?=\n##\s)", content, re.DOTALL
    )
    if context_match:
        context_block = context_match.group(1)
        for field in CONTEXT_FIELDS:
            if re.search(rf"\*\*{field}\*\*", context_block):
                passes += 1
            else:
                print(f"  {RED}❌ Context missing field: {field}{RESET}")
                fails += 1

        # Check version fields
        for field in VERSION_FIELDS:
            if re.search(rf"\*\*{field}\*\*", context_block):
                passes += 1
            else:
                print(f"  {YELLOW}⚠️  Context missing field: {field} (recommended){RESET}")
                warnings += 1

    # ── Check Iron Law is exactly 1 bold sentence ────────
    iron_match = re.search(
        r"##\s+⛔\s+THE IRON LAW\s*\n+\*\*(.+?)\*\*", content
    )
    if iron_match:
        iron_text = iron_match.group(1).strip()
        # Check it's roughly one sentence (no period-separated sentences)
        sentence_count = len([s for s in iron_text.split(". ") if s.strip()])
        if sentence_count <= 2:
            print(f"  {GREEN}✅ Iron Law: 1 sentence{RESET}")
            passes += 1
        else:
            print(f"  {YELLOW}⚠️  Iron Law has {sentence_count} sentences (should be 1){RESET}")
            warnings += 1
    elif re.search(r"##\s+⛔\s+THE IRON LAW", content):
        print(f"  {RED}❌ Iron Law: not a bold sentence{RESET}")
        fails += 1

    # ── Check Guardrails count (2-5 items) ───────────────
    guard_match = re.search(
        r"##\s+🛡\s+Guardrails(.*?)(?=\n##\s)", content, re.DOTALL
    )
    if guard_match:
        checkboxes = re.findall(r"- \[[ x]\]", guard_match.group(1))
        count = len(checkboxes)
        if 2 <= count <= 5:
            print(f"  {GREEN}✅ Guardrails: {count} items (2-5 required){RESET}")
            passes += 1
        else:
            print(f"  {YELLOW}⚠️  Guardrails: {count} items (should be 2-5){RESET}")
            warnings += 1

    # ── Check Red Flags count (3-6 entries) ──────────────
    red_match = re.search(
        r"##\s+🚩\s+Red Flags(.*?)(?=\n##\s)", content, re.DOTALL
    )
    if red_match:
        # Count table rows (lines starting with |, excluding header/separator)
        table_rows = [
            l
            for l in red_match.group(1).split("\n")
            if l.strip().startswith("|") and not re.match(r"\|\s*-", l.strip())
        ]
        # Subtract header row
        row_count = max(0, len(table_rows) - 1)
        if 3 <= row_count <= 6:
            print(f"  {GREEN}✅ Red Flags: {row_count} entries (3-6 required){RESET}")
            passes += 1
        else:
            print(f"  {YELLOW}⚠️  Red Flags: {row_count} entries (should be 3-6){RESET}")
            warnings += 1

    # ── Check Remember count (≤6 rules) ──────────────────
    remember_match = re.search(
        r"##\s+Remember(.*?)(?=\n##\s|\Z)", content, re.DOTALL
    )
    if remember_match:
        table_rows = [
            l
            for l in remember_match.group(1).split("\n")
            if l.strip().startswith("|") and not re.match(r"\|\s*-", l.strip())
        ]
        row_count = max(0, len(table_rows) - 1)
        if row_count <= 6:
            print(f"  {GREEN}✅ Remember: {row_count} rules (≤6 required){RESET}")
            passes += 1
        else:
            print(f"  {YELLOW}⚠️  Remember: {row_count} rules (should be ≤6){RESET}")
            warnings += 1

    # ── Check Related Skills count (≤4) ──────────────────
    related_match = re.search(
        r"##\s+🔗\s+Related Skills(.*?)(?=\n##\s|\Z)", content, re.DOTALL
    )
    if related_match:
        table_rows = [
            l
            for l in related_match.group(1).split("\n")
            if l.strip().startswith("|") and not re.match(r"\|\s*-", l.strip())
        ]
        row_count = max(0, len(table_rows) - 1)
        if row_count <= 4:
            print(f"  {GREEN}✅ Related Skills: {row_count} entries (≤4 required){RESET}")
            passes += 1
        else:
            print(f"  {YELLOW}⚠️  Related Skills: {row_count} entries (should be ≤4){RESET}")
            warnings += 1

    # ── Check total lines ────────────────────────────────
    if total_lines > 500:
        print(f"  {RED}❌ Total lines: {total_lines} (max 500){RESET}")
        fails += 1
    elif total_lines > 300:
        print(f"  {YELLOW}⚠️  Total lines: {total_lines} (recommended ≤250){RESET}")
        warnings += 1
    else:
        print(f"  {GREEN}✅ Total lines: {total_lines}{RESET}")
        passes += 1

    return passes, fails, warnings


def main():
    args = sys.argv[1:]

    if not args:
        # Default: validate all skills/ directory
        skills_dir = Path("skills")
        if not skills_dir.exists():
            # Try relative to script location
            script_dir = Path(__file__).parent.parent
            skills_dir = script_dir / "skills"

        if not skills_dir.exists():
            print(f"{RED}skills/ directory not found{RESET}")
            sys.exit(1)

        files = sorted(
            f
            for f in skills_dir.glob("*.md")
            if f.name != "skill-template.md"
        )
    else:
        files = [Path(a) for a in args]

    if not files:
        print(f"{YELLOW}No skill files found to validate{RESET}")
        sys.exit(0)

    total_passes = 0
    total_fails = 0
    total_warnings = 0

    for f in files:
        p, fa, w = validate_skill(f)
        total_passes += p
        total_fails += fa
        total_warnings += w

    # ── Summary ──────────────────────────────────────────
    print(f"\n{'=' * 50}")
    print(f"{BOLD}Summary:{RESET} {len(files)} file(s) validated")
    print(f"  {GREEN}✅ Passed: {total_passes}{RESET}")
    if total_warnings:
        print(f"  {YELLOW}⚠️  Warnings: {total_warnings}{RESET}")
    if total_fails:
        print(f"  {RED}❌ Failed: {total_fails}{RESET}")
    print(f"{'=' * 50}")

    sys.exit(1 if total_fails > 0 else 0)


if __name__ == "__main__":
    main()
