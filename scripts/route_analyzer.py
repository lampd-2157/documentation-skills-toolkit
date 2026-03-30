#!/usr/bin/env python3
"""
Smart Routing Analyzer — Analyze a description and suggest the best skill + template.

Reads config/routing-signals.yaml and matches keywords from user input.
Outputs skill recommendations with confidence scores.

Usage:
    python3 scripts/route_analyzer.py "Tạo API reference cho User Management API"
    python3 scripts/route_analyzer.py --json "runbook cho nginx server"
"""

import re
import sys
from pathlib import Path

# ── Colors ───────────────────────────────────────────────
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"


def parse_routing_yaml(filepath):
    """Parse routing-signals.yaml without PyYAML dependency."""
    content = Path(filepath).read_text(encoding="utf-8")

    skills = {}
    composition_rules = []
    confidence_config = {}

    # Parse skills section
    in_skills = False
    in_composition = False
    in_confidence = False
    current_skill = None
    current_section = None

    for line in content.split("\n"):
        stripped = line.strip()

        if line.startswith("skills:"):
            in_skills = True
            in_composition = False
            in_confidence = False
            continue
        elif line.startswith("composition_rules:"):
            in_skills = False
            in_composition = True
            in_confidence = False
            continue
        elif line.startswith("confidence:"):
            in_skills = False
            in_composition = False
            in_confidence = True
            continue

        if in_skills:
            # Skill name (2-space indent, no dash)
            m = re.match(r"^  (\w[\w-]+):", line)
            if m and not stripped.startswith("-"):
                current_skill = m.group(1)
                skills[current_skill] = {"keywords": [], "templates": {}, "confidence_base": 0.5}
                current_section = None
                continue

            if current_skill:
                if stripped == "keywords:":
                    current_section = "keywords"
                    continue
                elif stripped == "templates:":
                    current_section = "templates"
                    continue
                elif stripped.startswith("templates: {}"):
                    current_section = None
                    skills[current_skill]["templates"] = {}
                    continue
                elif stripped.startswith("confidence_base:"):
                    val = stripped.split(":")[1].strip()
                    skills[current_skill]["confidence_base"] = float(val)
                    current_section = None
                    continue

                if current_section == "keywords":
                    m = re.match(r"\s+-\s+(.*)", line)
                    if m:
                        skills[current_skill]["keywords"].append(m.group(1).strip())
                elif current_section == "templates":
                    m = re.match(r"\s+(\w[\w-]*):\s*(T\d+)", line)
                    if m:
                        skills[current_skill]["templates"][m.group(1)] = m.group(2)

        if in_confidence:
            m = re.match(r"\s+(\w[\w_]+):\s*([\d.]+)", line)
            if m:
                confidence_config[m.group(1)] = float(m.group(2))

        if in_composition:
            # Parse composition rules (simplified)
            if stripped.startswith("- name:"):
                rule = {"name": stripped.split(":", 1)[1].strip().strip('"')}
                composition_rules.append(rule)
            elif stripped.startswith("signals:") and composition_rules:
                signals = re.findall(r'"([\w-]+)"', stripped)
                composition_rules[-1]["signals"] = signals
            elif stripped.startswith("primary:") and composition_rules:
                composition_rules[-1]["primary"] = stripped.split(":")[1].strip()
            elif stripped.startswith("secondary_iron_law:") and composition_rules:
                val = stripped.split(":")[1].strip()
                composition_rules[-1]["secondary"] = val if val != "null" else None

    return skills, composition_rules, confidence_config


def analyze(description, skills, composition_rules, confidence_config):
    """Analyze description and return skill scores."""
    desc_lower = description.lower()
    boost = confidence_config.get("keyword_match_boost", 0.1)
    max_conf = confidence_config.get("max_confidence", 1.0)
    auto_threshold = confidence_config.get("auto_select_threshold", 0.8)
    ask_threshold = confidence_config.get("ask_user_threshold", 0.5)

    results = []
    for skill_id, skill_data in skills.items():
        base = skill_data["confidence_base"]
        matched = []
        for kw in skill_data["keywords"]:
            if kw.lower() in desc_lower:
                matched.append(kw)

        confidence = min(base + len(matched) * boost, max_conf)
        if matched:
            results.append({
                "skill": skill_id,
                "confidence": confidence,
                "matched_keywords": matched,
                "templates": skill_data["templates"],
            })

    results.sort(key=lambda x: x["confidence"], reverse=True)

    # Check composition rules
    matched_skills = {r["skill"] for r in results if r["confidence"] >= ask_threshold}
    active_composition = None
    for rule in composition_rules:
        signals = set(rule.get("signals", []))
        if signals.issubset(matched_skills) and len(signals) > 1:
            active_composition = rule
            break

    return results, active_composition, auto_threshold, ask_threshold


def print_analysis(description, results, composition, auto_t, ask_t):
    """Print analysis results."""
    print(f"\n{BOLD}Smart Routing Analysis{RESET}")
    print(f"{DIM}{'─' * 50}{RESET}")
    print(f"{BLUE}Input:{RESET} {description}")
    print(f"{DIM}{'─' * 50}{RESET}")

    if not results:
        print(f"\n{YELLOW}No skill matched.{RESET} Use prompts/select-skill.md for manual selection.")
        return

    print(f"\n{BOLD}Skill Scores:{RESET}\n")
    for i, r in enumerate(results):
        conf = r["confidence"]
        skill = r["skill"]
        keywords = ", ".join(r["matched_keywords"])

        if conf >= auto_t:
            badge = f"{GREEN}AUTO-SELECT{RESET}"
            bar_color = GREEN
        elif conf >= ask_t:
            badge = f"{YELLOW}ASK USER{RESET}"
            bar_color = YELLOW
        else:
            badge = f"{RED}LOW{RESET}"
            bar_color = RED

        bar_len = int(conf * 20)
        bar = f"{bar_color}{'█' * bar_len}{DIM}{'░' * (20 - bar_len)}{RESET}"

        marker = " ★" if i == 0 else ""
        print(f"  {bar} {conf:.2f} {BOLD}{skill}{RESET} {badge}{marker}")
        print(f"  {DIM}Keywords: {keywords}{RESET}")

        if r["templates"]:
            templates = ", ".join(f"{k}={v}" for k, v in r["templates"].items())
            print(f"  {DIM}Templates: {templates}{RESET}")
        print()

    if composition:
        print(f"{CYAN}{BOLD}Composition Rule:{RESET} {composition['name']}")
        print(f"  Primary: {composition.get('primary', '?')}")
        secondary = composition.get('secondary')
        if secondary:
            print(f"  Secondary Iron Law: {secondary}")
        print()

    # Recommendation
    top = results[0]
    if top["confidence"] >= auto_t:
        print(f"{GREEN}{BOLD}Recommendation:{RESET} Use {BOLD}{top['skill']}{RESET} (confidence {top['confidence']:.2f})")
    elif top["confidence"] >= ask_t:
        print(f"{YELLOW}{BOLD}Recommendation:{RESET} Suggest {BOLD}{top['skill']}{RESET} but confirm with user (confidence {top['confidence']:.2f})")
    else:
        print(f"{RED}{BOLD}Recommendation:{RESET} Low confidence — use prompts/select-skill.md")


def print_json(results, composition):
    """Print JSON output."""
    import json
    output = {
        "results": results,
        "composition_rule": composition,
    }
    print(json.dumps(output, indent=2))


def main():
    args = sys.argv[1:]
    json_mode = "--json" in args
    args = [a for a in args if a != "--json"]

    if not args:
        print(f"{RED}Usage: route_analyzer.py [--json] \"description\"{RESET}")
        sys.exit(1)

    description = " ".join(args)

    # Find routing-signals.yaml
    script_dir = Path(__file__).parent
    yaml_path = script_dir.parent / "config" / "routing-signals.yaml"
    if not yaml_path.exists():
        print(f"{RED}Error: {yaml_path} not found{RESET}")
        sys.exit(1)

    skills, composition_rules, confidence_config = parse_routing_yaml(yaml_path)
    results, composition, auto_t, ask_t = analyze(description, skills, composition_rules, confidence_config)

    if json_mode:
        print_json(results, composition)
    else:
        print_analysis(description, results, composition, auto_t, ask_t)


if __name__ == "__main__":
    main()
