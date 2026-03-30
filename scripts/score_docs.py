#!/usr/bin/env python3
"""
Automated documentation quality scorer.

Scores documents on 6 automatable criteria (out of 10 from doc-quality-scorecard).
4 criteria require human review and are not scored here.

Usage:
    python3 scripts/score_docs.py                          # Score all skills/ and docs/
    python3 scripts/score_docs.py docs/getting-started.md  # Score specific file
    python3 scripts/score_docs.py --format markdown        # Markdown output (for PR comments)
    python3 scripts/score_docs.py --ci                     # GitHub Actions annotations

Scoring:
    6 criteria × 1 point each = max 6 points
    ≥ 4/6 = PASS | 3/6 = WARNING | < 3/6 = FAIL

Freshness Alerts:
    Documents older than 90 days get a dedicated warning.
    Use --ci flag to emit ::warning annotations for GitHub Actions.
"""

import re
import sys
from pathlib import Path
from datetime import datetime, timedelta

# ── Colors ───────────────────────────────────────────────
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
BOLD = "\033[1m"
RESET = "\033[0m"

PASS_THRESHOLD = 4
WARN_THRESHOLD = 3
FRESHNESS_DAYS = 90


def score_doc(filepath):
    """Score a single document. Returns (score, max_score, details)."""
    path = Path(filepath)
    content = path.read_text(encoding="utf-8")
    details = {}

    # 1. Structure (1pt): YAML frontmatter + heading hierarchy
    has_frontmatter = bool(re.match(r"^---\s*\n.*?\n---", content, re.DOTALL))
    has_h1 = bool(re.search(r"^# ", content, re.MULTILINE))
    has_h2 = bool(re.search(r"^## ", content, re.MULTILINE))
    structure_ok = has_frontmatter and has_h1 and has_h2
    details["structure"] = (1 if structure_ok else 0.5 if has_h1 and has_h2 else 0,
                            "frontmatter + h1 + h2" if structure_ok else "missing frontmatter" if not has_frontmatter else "weak hierarchy")

    # 2. Commands testable (1pt): code blocks with language tag
    code_blocks = re.findall(r"```(\w+)", content)
    has_code = len(code_blocks) >= 1
    details["commands"] = (1 if has_code else 0,
                           f"{len(code_blocks)} code blocks" if has_code else "no code blocks")

    # 3. Prerequisites (1pt): mentions prerequisites or requirements
    has_prereq = bool(re.search(r"(prerequisites|requirements|cần có|cần thiết)", content, re.IGNORECASE))
    details["prerequisites"] = (1 if has_prereq else 0,
                                "found" if has_prereq else "not found")

    # 4. Metadata (1pt): YAML has title + status/updated
    fm_match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if fm_match:
        fm_keys = re.findall(r"^(\w[\w-]*):", fm_match.group(1), re.MULTILINE)
        has_title = "title" in fm_keys or "name" in fm_keys
        has_status = "status" in fm_keys or "updated" in fm_keys
        meta_ok = has_title and has_status
    else:
        meta_ok = False
        has_title = False
    details["metadata"] = (1 if meta_ok else 0.5 if has_title else 0,
                           "complete" if meta_ok else "partial" if has_title else "missing")

    # 5. Visual & UI/UX (1pt): diagrams/admonitions/task lists
    has_mermaid = bool(re.search(r"```mermaid", content))
    has_admonition = bool(re.search(r"^!!! ", content, re.MULTILINE))
    has_tasklist = bool(re.search(r"^- \[[ x]\] ", content, re.MULTILINE))
    visual_hits = sum([has_mermaid, has_admonition, has_tasklist])
    visual_score = 1 if visual_hits >= 2 else 0.5 if visual_hits == 1 else 0
    visual_parts = []
    if has_mermaid:
        visual_parts.append("mermaid")
    if has_admonition:
        visual_parts.append("admonitions")
    if has_tasklist:
        visual_parts.append("task lists")
    details["visual_uiux"] = (visual_score,
                              " + ".join(visual_parts) if visual_parts else "plain text")

    # 6. Freshness (1pt): updated/created date within 90 days
    date_match = re.search(r"(?:updated|created|date|cập nhật|Last Updated|Used:).*?(\d{4}-\d{2}-\d{2})", content, re.IGNORECASE)
    if date_match:
        try:
            doc_date = datetime.strptime(date_match.group(1), "%Y-%m-%d")
            days_old = (datetime.now() - doc_date).days
            fresh = days_old <= FRESHNESS_DAYS
            details["freshness"] = (1 if fresh else 0,
                                    f"{days_old}d old" if fresh else f"stale ({days_old}d)")
        except ValueError:
            details["freshness"] = (0.5, "invalid date format")
    else:
        details["freshness"] = (0, "no date found")

    total = sum(d[0] for d in details.values())
    return total, 6, details


def format_terminal(files, results):
    """Print results in terminal format with colors."""
    total_pass = 0
    total_warn = 0
    total_fail = 0
    stale_docs = []

    for f, (score, max_score, details) in zip(files, results):
        if score >= PASS_THRESHOLD:
            status = f"{GREEN}PASS{RESET}"
            total_pass += 1
        elif score >= WARN_THRESHOLD:
            status = f"{YELLOW}WARN{RESET}"
            total_warn += 1
        else:
            status = f"{RED}FAIL{RESET}"
            total_fail += 1

        criteria = " | ".join(f"{k}:{v[0]}" for k, v in details.items())
        print(f"  {status} {score:.1f}/{max_score} {f.name} [{criteria}]")

        # Track stale docs for freshness alert
        freshness_score, freshness_desc = details["freshness"]
        if freshness_score == 0 and "stale" in freshness_desc:
            stale_docs.append((f, freshness_desc))

    # Summary
    all_scores = [(f.name, s) for f, (s, _, _) in zip(files, results)]
    avg = sum(s for _, s in all_scores) / len(all_scores) if all_scores else 0
    print(f"\n{'=' * 50}")
    print(f"{BOLD}Doc Quality Summary:{RESET} {len(files)} file(s) scored")
    print(f"  Average: {avg:.1f}/6")
    print(f"  {GREEN}Pass (>={PASS_THRESHOLD}): {total_pass}{RESET}")
    if total_warn:
        print(f"  {YELLOW}Warn ({WARN_THRESHOLD}): {total_warn}{RESET}")
    if total_fail:
        print(f"  {RED}Fail (<{WARN_THRESHOLD}): {total_fail}{RESET}")

    # Freshness Alerts
    if stale_docs:
        print(f"\n{YELLOW}{BOLD}Freshness Alerts ({len(stale_docs)} stale docs):{RESET}")
        for f, desc in stale_docs:
            print(f"  {YELLOW}WARNING{RESET} {f} — {desc} (>{FRESHNESS_DAYS} days)")
        print(f"  {YELLOW}Tip: Update these docs or set a new 'updated' date in frontmatter{RESET}")

    print(f"{'=' * 50}")
    return stale_docs


def format_markdown(files, results):
    """Print results in Markdown format (for PR comments)."""
    lines = []
    lines.append("## Doc Quality Score")
    lines.append("")
    lines.append("| File | Score | Structure | Commands | Prerequisites | Metadata | Visual | Freshness |")
    lines.append("|------|-------|-----------|----------|---------------|----------|--------|-----------|")

    stale_docs = []
    all_scores = []

    for f, (score, max_score, details) in zip(files, results):
        if score >= PASS_THRESHOLD:
            badge = "PASS"
        elif score >= WARN_THRESHOLD:
            badge = "WARN"
        else:
            badge = "FAIL"

        cells = []
        for k in ["structure", "commands", "prerequisites", "metadata", "visual_uiux", "freshness"]:
            val, desc = details[k]
            if val >= 1:
                cells.append(f"{val}")
            elif val > 0:
                cells.append(f"{val}")
            else:
                cells.append(f"0")

        line = f"| `{f.name}` | **{score:.1f}/6** {badge} | {' | '.join(cells)} |"
        lines.append(line)
        all_scores.append(score)

        freshness_score, freshness_desc = details["freshness"]
        if freshness_score == 0 and "stale" in freshness_desc:
            stale_docs.append((f, freshness_desc))

    avg = sum(all_scores) / len(all_scores) if all_scores else 0
    total_pass = sum(1 for s in all_scores if s >= PASS_THRESHOLD)
    total_warn = sum(1 for s in all_scores if WARN_THRESHOLD <= s < PASS_THRESHOLD)
    total_fail = sum(1 for s in all_scores if s < WARN_THRESHOLD)

    lines.append("")
    lines.append(f"**Average: {avg:.1f}/6** | Pass: {total_pass} | Warn: {total_warn} | Fail: {total_fail}")

    if stale_docs:
        lines.append("")
        lines.append(f"### Freshness Alerts ({len(stale_docs)} stale)")
        lines.append("")
        for f, desc in stale_docs:
            lines.append(f"- `{f}` — {desc}")

    print("\n".join(lines))
    return stale_docs


def format_ci(files, results):
    """Print GitHub Actions ::warning annotations for stale/failing docs."""
    stale_docs = []
    for f, (score, max_score, details) in zip(files, results):
        freshness_score, freshness_desc = details["freshness"]
        if freshness_score == 0 and "stale" in freshness_desc:
            stale_docs.append((f, freshness_desc))
            print(f"::warning file={f}::Stale document — {freshness_desc} (>{FRESHNESS_DAYS} days since last update)")

        if score < WARN_THRESHOLD:
            print(f"::warning file={f}::Low doc quality score: {score:.1f}/6")

    # Also output terminal format
    format_terminal(files, results)
    return stale_docs


def main():
    args = sys.argv[1:]

    # Parse flags
    output_format = "terminal"
    file_args = []
    for arg in args:
        if arg == "--format" or arg == "-f":
            continue
        elif arg == "markdown":
            if args[args.index(arg) - 1] in ("--format", "-f"):
                output_format = "markdown"
                continue
        elif arg == "--ci":
            output_format = "ci"
            continue
        elif arg == "--markdown":
            output_format = "markdown"
            continue
        else:
            file_args.append(arg)

    if file_args:
        files = [Path(a) for a in file_args]
    else:
        files = sorted(
            list(Path("skills").glob("*.md")) +
            list(Path("docs").glob("*.md"))
        )
        files = [f for f in files if f.name != "skill-template.md"]

    if not files:
        print(f"{YELLOW}No files found to score{RESET}")
        sys.exit(0)

    # Score all files
    results = []
    for f in files:
        if not f.exists():
            print(f"{RED}  File not found: {f}{RESET}")
            results.append((0, 6, {}))
            continue
        results.append(score_doc(f))

    # Filter out not-found files
    valid = [(f, r) for f, r in zip(files, results) if r[2]]
    if not valid:
        print(f"{YELLOW}No valid files scored{RESET}")
        sys.exit(0)

    valid_files, valid_results = zip(*valid)

    if output_format == "markdown":
        format_markdown(valid_files, valid_results)
    elif output_format == "ci":
        format_ci(valid_files, valid_results)
    else:
        format_terminal(valid_files, valid_results)

    # Warn-only: don't fail CI on doc scores (informational)
    sys.exit(0)


if __name__ == "__main__":
    main()
