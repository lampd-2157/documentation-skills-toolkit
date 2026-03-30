# New Skill Contribution

## Skill Details

- **Name:** `skills/community/<name>.md`
- **Author:** @
- **Version:** 1.0.0

## Checklist

- [ ] Skill file follows 6-section structure
- [ ] YAML frontmatter has `name`, `description`, `compatibility`, `skill_version`
- [ ] `python3 scripts/validate_skill.py skills/community/<name>.md` passes
- [ ] Iron Law is specific and actionable
- [ ] Red Flags table has 3-6 entries
- [ ] Scope IN/OUT does not overlap with core skills
- [ ] Test cases in `evals/community-<name>/test-cases.md`
- [ ] Token count ≤ 8K

## Optional

- [ ] Template file in `templates/`
- [ ] Prompt file in `prompts/create-<type>.md`
- [ ] VS Code snippet in `examples/docs.code-snippets`
- [ ] Routing signals in `config/routing-signals.yaml`
