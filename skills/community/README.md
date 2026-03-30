# Community Skills — Skill Marketplace

Custom skills contributed by the team. Each skill follows the same 6-section structure as core skills.

## How to Contribute a Skill

### 1. Create skill file

Copy `skills/skill-template.md` and customize:

```bash
cp skills/skill-template.md skills/community/my-skill.md
```

### 2. Required structure

Your skill MUST have all 6 sections:

1. **Context / Bối cảnh** — Category, triggers, scope
2. **THE IRON LAW** — 1 bold non-negotiable rule
3. **Guardrails** — 2-5 checklist items
4. **Red Flags** — 3-6 stop signals (table format)
5. **Remember** — ≤6 rules
6. **Related Skills** — ≤5 links

### 3. Required YAML frontmatter

```yaml
---
name: my-custom-skill
description: "Trigger keywords and description..."
compatibility: "MkDocs Material >= 9.0"
skill_version: "1.0.0"
---
```

### 4. Validate

```bash
python3 scripts/validate_skill.py skills/community/my-skill.md
```

All checks must pass before submitting.

### 5. Submit

Create a PR with:

- Skill file in `skills/community/`
- Test cases in `evals/community-my-skill/test-cases.md`
- (Optional) Template in `templates/` if your skill needs one
- (Optional) Prompt in `prompts/create-my-type.md`

## Current Community Skills

| Skill | Author | Version | Description |
|-------|--------|---------|-------------|
| *None yet* | — | — | Be the first contributor! |

## Quality Standards

- Must pass `python3 scripts/validate_skill.py`
- Iron Law must be specific and actionable (not generic)
- Red Flags must cover real failure scenarios
- Scope IN/OUT must be clear — no overlap with core skills
- Token count ≤ 8K, section length ≤ 100 lines
