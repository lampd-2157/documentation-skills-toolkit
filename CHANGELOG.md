# Changelog

All notable changes to this project will be documented in this file.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). This project adheres to [Semantic Versioning](https://semver.org/).

---

## [2.2.1] — 2026-03-27

### Changed

- **Project restructure** — Eliminated `references/` catch-all directory; replaced with purpose-driven directories:
  - `config/` — project configs (markdownlint, cspell, pre-commit, link-check)
  - `docs/` — human-readable guides (standard open-source convention)
  - `examples/` — starter configs for other projects (mkdocs-starter, github-actions, VS Code snippets)
  - `templates/` — promoted to top-level, split monolithic file into 8 individual template files (T1-T8)
- **`scripts/setup.sh`** — Moved from `references/config/` to `scripts/` (consolidate all scripts)
- **Config file renames** for consistency: `markdownlint-config.json` → `markdownlint.json`, `pre-commit-config.yaml` → `pre-commit.yaml`, `markdown-link-check.json` → `link-check.json`
- **CI/CD** — Switched from markdownlint-cli2-action to direct `npx` with explicit `--config` flag
- **Internal files** — Moved `AUDIT.md` and `push.md` to `.internal/` (hidden directory)

### Removed

- **`references/`** directory — replaced by `config/`, `docs/`, `examples/`, `templates/`
- **Root `.markdownlint-cli2.jsonc`** — no longer needed; CI and Makefile use `--config` flag directly
- **Monolithic `doc-templates-library.md`** — replaced by 8 individual template files in `templates/`

---

## [2.2.0] — 2026-03-27

### Added

- **`skills/infra-security-doc.md`** — New skill: security policy, RBAC/ABAC access control matrix, audit log standards, vulnerability disclosure, security checklist for infra changes
- **Incident Postmortem template (§4.3)** in `ops-runbook-writer.md` — Full postmortem structure with 5 Whys root cause analysis, timeline, impact assessment, action items
- **`.github/workflows/docs-ci.yml`** — GitHub Actions CI/CD: markdownlint + validate_skill.py + mkdocs build (strict) on PR and push to main
- **`Makefile`** at root — `make serve/lint/validate/build/setup/all` + scaffold shortcuts (`make new-runbook TITLE="..."`)
- **Evals for infra-security-doc** in `evals/` directory

### Changed

- **README.md** — Updated to 5 skills, added Makefile and CI/CD to project structure, version bump to 2.2.0
- **`ops-runbook-writer.md`** — Added comprehensive §4.3 Incident Postmortem Template (5 Whys, timeline, action items table)

---

## [2.1.0] — 2026-03-27

### Added

- **YAML frontmatter** in all skill files — enables automatic skill triggering with `name`, `description`, `compatibility` fields
- **`skills/training-doc-writer.md`** — New skill: training, onboarding, curriculum, learning path (split from training-guide-writer)
- **`skills/project-doc-writer.md`** — New skill: ADR, tech spec, how-to guide, quick reference (split from training-guide-writer)
- **`evals/` directory** — Eval test suite with `evals.json` and per-skill `test-cases.md` for verifying skill triggers and output format
- **"Pushy" descriptions** in YAML frontmatter — extensive trigger keywords for better skill matching

### Changed

- **`training-guide-writer.md` → split into 2 skills** — single-responsibility: training-doc-writer (training/onboarding) + project-doc-writer (ADR/spec/guide)
- **Mermaid config** — Removed `mermaid2` plugin dependency, using native MkDocs Material `pymdownx.superfences.fence_code_format` (compatible with Material >= 9.0)
- **`docs-engineer.md`** — Updated mkdocs.yml sample to remove mermaid2, updated cross-references to new skills
- **`ops-runbook-writer.md`** — Updated cross-references to new split skills
- **README.md** — Updated to reflect 4 skills, new project structure with `evals/`, version bump to 2.1.0

### Removed

- **`skills/training-guide-writer.md`** — Replaced by `training-doc-writer.md` + `project-doc-writer.md`
- **`mkdocs-mermaid2-plugin`** dependency — No longer needed with MkDocs Material >= 9.0

---

## [2.0.0] — 2026-03-26

### Added

- **`skills/` directory** — Dedicated folder for all skill files (previously at root)
- **`scripts/validate_skill.py`** — Validates skill files have all 6 required sections
- **`scripts/docs-toolkit`** — CLI tool to scaffold new docs from templates
- **`references/guides/skill-composition-recipes.md`** — Maps real-world tasks to skill combinations
- **`references/guides/doc-quality-scorecard.md`** — Scoring rubric (0-10) for doc quality
- **`references/guides/doc-anti-patterns.md`** — Top 10 documentation mistakes to avoid
- **`references/config/cspell.json`** — Spell check configuration (cspell)
- **Version + Last Updated** metadata fields in all skill Context tables
- **OS detection** in setup.sh (Linux, macOS, WSL, Windows)
- **5 new demo-site examples** — T4 Training, T5 Network, T6 Postmortem, T7 Maintenance, T8 Release Notes
- **`references/guides/getting-started-guide.md`** — Comprehensive guide for first-time users
- **CHANGELOG.md** (this file)

### Changed

- **Project structure reorganized:**
  - `references/` split into 3 tiers: `config/`, `guides/`, `templates/`
  - Skills moved from root to `skills/` directory
- **README.md** — Rewritten: concise (~130 lines), links to detailed docs
- **CONTRIBUTING.md** — Updated paths for new directory structure
- **setup.sh** — Added OS detection, WSL support, pip3 fallback
- **pre-commit-config.yaml** — Added cspell + markdown-link-check hooks

### Removed

- Root-level skill files (moved to `skills/`)
- Flat `references/` structure (split into organized subfolders)

---

## [1.1.1] — 2026-03-26

### Fixed

- Minor formatting fixes in README badges

---

## [1.1.0] — 2026-03-26

### Added

- Initial public release
- 3 core skills: docs-engineer, ops-runbook-writer, training-guide-writer
- Universal skill template (6-section model)
- 8 document templates (T1-T8)
- MkDocs demo site with 4 example docs
- Complete setup infrastructure (setup.sh, markdownlint, pre-commit, GitHub Actions)
- VS Code snippets (9 templates)
- CONTRIBUTING.md
- MIT License
