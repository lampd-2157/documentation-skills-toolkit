# Documentation Skills Toolkit

![Version](https://img.shields.io/badge/version-2.0.0-blue)
![Skills](https://img.shields.io/badge/skills-3-green)
![Templates](https://img.shields.io/badge/templates-8-orange)
![License](https://img.shields.io/badge/license-MIT-brightgreen)

> **Bộ skill chuẩn hóa cho documentation** — dùng được cho mọi dự án, không phụ thuộc vào bất kỳ hệ thống cụ thể nào.

---

## Quick Start

```bash
# Clone repo
git clone https://github.com/lampd-2157/documentation-skills-toolkit.git
cd documentation-skills-toolkit

# One-command setup
bash references/config/setup.sh

# Scaffold a new doc
./scripts/docs-toolkit new runbook "My Service"

# Preview demo site
cd demo-site && pip install -r requirements.txt && mkdocs serve
```

---

## Project Structure

```text
documentation-skills-toolkit/
├── skills/                         # Skill files (3 core + 1 template)
│   ├── docs-engineer.md            # MkDocs platform & Markdown standards
│   ├── ops-runbook-writer.md       # Runbook & operations docs
│   ├── training-guide-writer.md    # Training & guide docs
│   └── skill-template.md           # Universal 6-section template
├── references/
│   ├── config/                     # Machine-readable configs
│   │   ├── setup.sh               # One-command setup script
│   │   ├── mkdocs-starter.yml     # Ready-to-use MkDocs config
│   │   ├── markdownlint-config.json
│   │   ├── pre-commit-config.yaml
│   │   ├── github-actions-docs.yml # CI/CD pipeline
│   │   ├── cspell.json            # Spell check config
│   │   ├── requirements.txt       # Python dependencies
│   │   └── docs.code-snippets     # VS Code snippets (9 templates)
│   ├── guides/                     # Human-readable guides
│   │   ├── docs-lifecycle-guide.md # Write → Lint → Review → Publish → Audit
│   │   ├── skill-composition-recipes.md  # Task → skill combinations
│   │   ├── doc-quality-scorecard.md      # Scoring rubric (0-10)
│   │   ├── doc-anti-patterns.md          # Top 10 mistakes to avoid
│   │   ├── infra-knowledge-base.md       # Starter structure for infra teams
│   │   └── mkdocs-plugins-catalog.md     # 20 curated MkDocs plugins
│   └── templates/
│       └── doc-templates-library.md      # 8 copy-paste templates (T1-T8)
├── scripts/
│   ├── docs-toolkit                # CLI: scaffold new docs from templates
│   └── validate_skill.py          # Validate skill file structure
├── demo-site/                      # Working MkDocs example site
├── CHANGELOG.md
├── CONTRIBUTING.md
└── LICENSE                         # MIT
```

---

## Skill Map

```text
Bạn cần làm gì?
  ├── Setup MkDocs / chuẩn hóa Markdown?     → skills/docs-engineer.md
  ├── Viết runbook / ops manual / network?    → skills/ops-runbook-writer.md
  ├── Viết training / guide / ADR?            → skills/training-guide-writer.md
  ├── Cần template copy-paste nhanh?          → references/templates/doc-templates-library.md
  └── Cần combine nhiều skills?               → references/guides/skill-composition-recipes.md
```

## Templates (T1-T8)

| ID  | Template            | Skill                | Use Case                    |
| --- | ------------------- | -------------------- | --------------------------- |
| T1  | Runbook             | ops-runbook-writer   | System operation procedures |
| T2  | ADR                 | training-guide-writer | Architecture decisions     |
| T3  | How-to Guide        | training-guide-writer | Step-by-step instructions  |
| T4  | Training Module     | training-guide-writer | Internal training          |
| T5  | Network Topology    | ops-runbook-writer   | Network documentation      |
| T6  | Incident Postmortem | ops-runbook-writer   | Post-incident learning     |
| T7  | Maintenance Window  | ops-runbook-writer   | Planned change requests    |
| T8  | Release Notes       | training-guide-writer | Version release summary    |

---

## Tooling

| Tool | Command | Purpose |
|------|---------|---------|
| Scaffold | `./scripts/docs-toolkit new <type> <title>` | Create doc from template |
| Validate | `python3 scripts/validate_skill.py` | Check skill file structure |
| Lint | `npx markdownlint-cli2 "**/*.md"` | Check markdown format |
| Spell | `npx cspell "**/*.md"` | Check spelling |
| Preview | `mkdocs serve` | Local preview |
| Build | `mkdocs build --strict` | Production build |

---

## Documentation

| Doc | Purpose |
|-----|---------|
| [Lifecycle Guide](references/guides/docs-lifecycle-guide.md) | Write → Lint → Review → Publish → Audit |
| [Composition Recipes](references/guides/skill-composition-recipes.md) | Which skills to combine for common tasks |
| [Quality Scorecard](references/guides/doc-quality-scorecard.md) | Score your docs objectively (0-10) |
| [Anti-Patterns](references/guides/doc-anti-patterns.md) | Top 10 documentation mistakes |
| [Plugin Catalog](references/guides/mkdocs-plugins-catalog.md) | 20 curated MkDocs plugins |
| [Infra Knowledge Base](references/guides/infra-knowledge-base.md) | Starter structure for infra teams |
| [Contributing](CONTRIBUTING.md) | How to contribute skills & templates |
| [Changelog](CHANGELOG.md) | Version history |

---

## License

MIT — [LICENSE](LICENSE)

> **Created by [DulapReal](https://github.com/lampd-2157)** — Infrastructure & Automation Engineer
>
> Version 2.0.0 | 2026-03-26
