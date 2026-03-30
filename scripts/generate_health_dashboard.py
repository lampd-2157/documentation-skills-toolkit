#!/usr/bin/env python3
"""
Doc Health Dashboard Generator.

Generates a Markdown dashboard summarizing doc quality, freshness, and coverage.
Output can be viewed directly or served via MkDocs.

Usage:
    python3 scripts/generate_health_dashboard.py                    # Print to stdout
    python3 scripts/generate_health_dashboard.py --output docs/health-dashboard.md
"""

import re
import sys
from pathlib import Path
from datetime import datetime

# Reuse scoring from score_docs.py
sys.path.insert(0, str(Path(__file__).parent))
from score_docs import score_doc, PASS_THRESHOLD, WARN_THRESHOLD, FRESHNESS_DAYS


def count_files(directory, pattern="*.md"):
    """Count markdown files in a directory."""
    path = Path(directory)
    if not path.exists():
        return 0
    return len(list(path.rglob(pattern)))


def get_skill_info():
    """Read skill metadata from AGENT-CARDS.json."""
    import json
    cards_path = Path("skills/AGENT-CARDS.json")
    if not cards_path.exists():
        return []
    data = json.loads(cards_path.read_text(encoding="utf-8"))
    return data.get("skills", [])


def get_template_count():
    """Count template files."""
    return count_files("templates", "*.md")


def get_eval_count():
    """Count eval test cases from evals.json."""
    import json
    evals_path = Path("evals/evals.json")
    if not evals_path.exists():
        return 0
    data = json.loads(evals_path.read_text(encoding="utf-8"))
    total = 0
    for skill in data.get("skills", []):
        total += len(skill.get("evals", []))
    return total


def generate_dashboard():
    """Generate the health dashboard markdown."""
    lines = []
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    lines.append("# Doc Health Dashboard")
    lines.append("")
    lines.append(f"> Auto-generated: {now}")
    lines.append("")

    # ── Overview metrics ──
    skills = get_skill_info()
    template_count = get_template_count()
    eval_count = get_eval_count()
    prompt_count = count_files("prompts", "*.md")
    doc_count = count_files("docs", "*.md")

    lines.append("## Overview")
    lines.append("")
    lines.append("| Metric | Count |")
    lines.append("|--------|-------|")
    lines.append(f"| Skills | {len(skills)} |")
    lines.append(f"| Templates | {template_count} |")
    lines.append(f"| Prompts | {prompt_count} |")
    lines.append(f"| Eval test cases | {eval_count} |")
    lines.append(f"| Documentation files | {doc_count} |")
    lines.append("")

    # ── Quality scores ──
    files = sorted(
        list(Path("skills").glob("*.md")) +
        list(Path("docs").glob("*.md"))
    )
    files = [f for f in files if f.name != "skill-template.md" and f.exists()]

    if files:
        results = []
        for f in files:
            try:
                results.append((f, *score_doc(f)))
            except Exception:
                continue

        lines.append("## Quality Scores")
        lines.append("")
        lines.append("| File | Score | Status | Freshness |")
        lines.append("|------|-------|--------|-----------|")

        pass_count = 0
        warn_count = 0
        fail_count = 0
        stale_docs = []

        for f, score, max_score, details in results:
            if score >= PASS_THRESHOLD:
                status = "PASS"
                pass_count += 1
            elif score >= WARN_THRESHOLD:
                status = "WARN"
                warn_count += 1
            else:
                status = "FAIL"
                fail_count += 1

            fresh_score, fresh_desc = details.get("freshness", (0, "unknown"))
            if fresh_score == 0 and "stale" in str(fresh_desc):
                stale_docs.append(f)

            lines.append(f"| `{f.name}` | {score:.1f}/6 | {status} | {fresh_desc} |")

        avg = sum(s for _, s, _, _ in results) / len(results) if results else 0
        lines.append("")
        lines.append(f"**Average: {avg:.1f}/6** | Pass: {pass_count} | Warn: {warn_count} | Fail: {fail_count}")
        lines.append("")

        # ── Freshness alerts ──
        if stale_docs:
            lines.append("## Freshness Alerts")
            lines.append("")
            lines.append(f"{len(stale_docs)} document(s) older than {FRESHNESS_DAYS} days:")
            lines.append("")
            for f in stale_docs:
                lines.append(f"- `{f}`")
            lines.append("")

    # ── Skill coverage ──
    lines.append("## Skill Coverage")
    lines.append("")
    lines.append("| Skill | Templates | Triggers | Iron Law |")
    lines.append("|-------|-----------|----------|----------|")
    for s in skills:
        templates = ", ".join(s.get("templates", [])) or "—"
        trigger_count = len(s.get("triggers", []))
        iron_law = s.get("iron_law", "—")
        if len(iron_law) > 60:
            iron_law = iron_law[:57] + "..."
        lines.append(f"| `{s['id']}` | {templates} | {trigger_count} | {iron_law} |")
    lines.append("")

    return "\n".join(lines)


def main():
    args = sys.argv[1:]
    output_path = None

    for i, arg in enumerate(args):
        if arg == "--output" and i + 1 < len(args):
            output_path = args[i + 1]

    dashboard = generate_dashboard()

    if output_path:
        Path(output_path).write_text(dashboard, encoding="utf-8")
        print(f"Dashboard written to {output_path}")
    else:
        print(dashboard)


if __name__ == "__main__":
    main()
