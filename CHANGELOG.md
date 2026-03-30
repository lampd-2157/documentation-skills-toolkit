# Changelog

All notable changes to this project will be documented in this file.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). This project adheres to [Semantic Versioning](https://semver.org/).

---

## [5.4.0] — 2026-03-30

### Added

- **T14: Security Policy template** — `templates/security-policy.md`: Purpose, Scope, Policy Statements, Enforcement, Audit Schedule, Compliance Mapping
- **`prompts/create-architecture-diagram.md`** — Prompt template cho AI agents tạo architecture diagram (T12)
- **Demo-site examples** — T12 Architecture Diagram (E-Commerce Platform) + T13 API Reference (Task Management API)
- **Routing Playground** — `docs/routing-playground.md`: interactive guide test Smart Routing với ví dụ high/medium/low confidence
- **Community Skills Marketplace** — `skills/community/SKILL-TEMPLATE.md` full template + review process + CI validation cho community skills
- **Health Dashboard CI** — `.github/workflows/health-dashboard.yml`: weekly auto-generate dashboard → GitHub issue
- **Conventional Commits config** — `config/commitlint.yaml`: types, scopes, rules, examples cho commit message chuẩn
- **Version automation** — `scripts/bump-version.sh` + `make bump-version V=X.Y.Z` auto-update tất cả version footers
- **Version drift detection** — `make check-versions` kiểm tra footers match CHANGELOG, tích hợp vào `make check`
- **CLI generators** — `docs-toolkit new architecture-diagram` + `docs-toolkit new api-reference` (T12, T13)
- **Composition recipes R10, R11** — API Reference + Security, Architecture Diagram + ADR

### Fixed

- **Version sync** — 6 files version footer lệch (README 5.0.0, AGENTS 5.0.0, CONTRIBUTING 4.2.0, prompts 5.0.0/4.2.0, AGENT-CARDS 5.2.0) → tất cả 5.4.0
- **Missing index entries** — templates/README thiếu T12+T13, prompts/README thiếu create-api-reference + create-architecture-diagram
- **Orphaned T12** — Architecture Diagram template không được registered → gán vào project-doc-writer trong AGENT-CARDS
- **AGENTS.md outdated** — Cập nhật từ "5 skills, 11 templates" → "6 skills, 14 templates, 15 prompts" + CLI commands mới
- **CI link checker** — Bỏ `head -30` limit, giờ check toàn bộ `skills/` + `docs/`

### Changed

- **`skills/AGENT-CARDS.json`** — v5.4.0: T12 sections → project-doc-writer, T14 sections → infra-security-doc
- **`scripts/docs-toolkit`** — v5.3.0: thêm architecture-diagram + api-reference generators, `list` hiển thị T12-T14
- **`docs/getting-started.md`** — Smart Routing section header v5.0.0 → v5.0.0+ với note v5.3.0 CLI enhancements
- **`Makefile`** — Thêm `bump-version`, `check-versions` targets; `check` bao gồm `check-versions`

---

## [5.3.0] — 2026-03-30

### Added

- **Interactive Routing CLI** — `docs-toolkit route "description"` analyzes keywords, shows confidence scores with visual bars, detects composition rules
- **Wizard Mode** — `docs-toolkit wizard` interactive Phase 0 interview in terminal: asks context questions, runs routing, creates doc
- **AI Feedback Loop** — `config/routing-feedback.yaml` structure for logging routing decisions and keyword adjustments over time
- **Doc Health Dashboard** — `scripts/generate_health_dashboard.py` generates Markdown overview: quality scores, freshness alerts, skill coverage
- **`scripts/route_analyzer.py`** — Standalone routing engine: parses `routing-signals.yaml`, matches keywords, calculates confidence, detects composition rules
- **Makefile targets** — `make route`, `make wizard`, `make health-dashboard`

---

## [5.2.0] — 2026-03-30

### Added

- **T12: Architecture Diagram template** — `templates/architecture-diagram.md`: Context diagram, Component diagram, Data flow, Technology stack, Deployment view, Security boundaries (all Mermaid-ready)
- **T13: API Reference template** — `templates/api-reference.md`: Endpoints with request/response examples, error codes, authentication, rate limits, changelog
- **`api-doc-writer` skill** — New skill (6th): REST API, GraphQL, gRPC, webhook, SDK docs. Iron Law: every endpoint MUST have request + response + error codes
- **`prompts/create-api-reference.md`** — Prompt template for AI agents to generate API docs
- **Skill Versioning** — All skills now have `skill_version` field in YAML frontmatter, validated by `validate_skill.py`
- **Skill Marketplace** — `skills/community/` directory with README, contribution guide, and PR template for custom skill submissions
- **Routing: api-doc-writer signals** — `config/routing-signals.yaml` updated with API keywords + "API docs with security" composition rule
- **Evals: api-doc-writer** — 4 test cases (REST API, GraphQL, webhook, API+security composition)

### Changed

- **`skills/AGENT-CARDS.json`** — v5.2.0: 6 skills (added api-doc-writer with T13 template sections)
- **Templates count** — 11 → 13 (T12 Architecture Diagram, T13 API Reference)
- **Skills count** — 5 → 6 (added api-doc-writer)

---

## [5.1.0] — 2026-03-30

### Added

- **Doc Freshness Alerts** — `score_docs.py` hiển thị dedicated warning section cho docs >90 ngày chưa update
- **CI Doc Scoring PR Comment** — GitHub Actions tự post doc quality score table vào PR comment (update, không spam)
- **Markdown output format** — `score_docs.py --markdown` cho PR-friendly output, `--ci` cho GitHub Actions annotations
- **MkDocs Tag-based Navigation** — Tags plugin enabled, tags hiển thị trên mỗi page, tags index page
- **ADR Auto-linking** — `docs-toolkit adr link <adr1> <adr2>` tự update "Related ADRs" section trong cả 2 files
- **VS Code Snippets T9-T11** — Thêm snippets cho ADR MADR (T9), ADR Lightweight (T10), Knowledge Check (T11), Phase 0 Interview

### Fixed

- **`.internal/push.md`** — Fix stale `references/` paths (removed in v2.2.1), add missing scopes (`prompts/`, `config/`, `examples/`, `.github/`, `.internal/`)
- **`docs-toolkit`** — Updated to v5.1.0, added `adr link` subcommand with usage help

---

## [5.0.1] — 2026-03-30

### Fixed

- **Version footers removed** — Xóa footer `> **Version:** X.X.X` khỏi tất cả docs/ và demo-site/ files; `README.md` + `CHANGELOG.md` là single source of truth cho version
- **`ansible-network-howto.md`** — Updated for v5.0.0 workflow: Phase 0 Interview Context block,
  Smart Routing build log, enhanced YAML frontmatter (skill/template/routing fields)
- **`case-study-ansible-network.md`** — Rewritten for v5.0.0: Phase 0 Smart Routing analysis,
  composition rule, interview Layer 1+2, section tiers decision, Step 6 Security Scan
- **`docs/getting-started.md`** — Added Section 5b: Smart Routing — confidence scoring, composition rules table, Phase 0 interview, template section tiers
- **`docs/skill-composition-recipes.md`** — Added routing reference note pointing to `config/routing-signals.yaml`
- **`README.md`** — Case study row updated to v5.0.0 workflow (Smart Routing + Interview)

---

## [5.0.0] — 2026-03-30

### Added

- **Smart Routing** — `config/routing-signals.yaml`: keyword-based skill selection + confidence scoring + composition rules
- **Composition rules** — 5 pre-defined multi-skill combinations (how-to+ops, runbook+security, training+ops, security+ADR, docs standalone)
- **Confidence scoring** — Auto-select >= 0.8, ask confirm 0.5-0.8, fallback select-skill < 0.5

### Changed

- **`prompts/select-skill.md`** — AI đọc routing-signals.yaml, phân tích keywords + confidence
- **`skills/AGENT-CARDS.json`** — v5.0.0, reference routing-signals.yaml
- **`AGENTS.md`** — Smart Routing note trong Skill Selection

---

## [4.3.0] — 2026-03-30

### Added

- **Flexible template tiers** — Mỗi template (T1-T11) có 3 tiers: `required` / `recommended` / `optional`
- **Section tier metadata** — HTML comment block trong mỗi template file định nghĩa tiers
- **`AGENT-CARDS.json` `template_sections`** — AI agent biết sections nào required/optional cho mỗi template

### Changed

- **Templates (T1-T11)** — Thêm `<!-- sections: required/recommended/optional -->` metadata
- **`skills/AGENT-CARDS.json`** — v4.3.0, thêm `template_tiers` + `template_sections` per skill
- **Prompts (10 files)** — Thêm "Flexible Sections" rule
- **`AGENTS.md`** — Thêm "Template Section Tiers" section + validation rule

---

## [4.2.0] — 2026-03-30

### Added

- **Interview flow** — `prompts/interview-before-create.md`: 3-layer interview (Universal → Type-specific → Deep-dive) trước khi tạo doc
- **Phase 0 Interview** trong tất cả 13 `create-*.md` prompts — AI hỏi Audience, Scope, Environment trước khi generate

### Changed

- **`AGENTS.md`** — Workflow thêm bước Interview, boundary "DO NOT generate without interviewing"
- **`prompts/README.md`** — Workflow 6 bước (interview → chọn → copy → paste → review → validate)
- **Prompt count** — 12 → 13 templates (thêm interview-before-create.md)

---

## [4.1.0] — 2026-03-30

### Added

- **Security framework** — Placeholder standards cho sensitive data (`docs/security-placeholders.md`)
- **`scripts/docs-secret-scan.sh`** — Scan docs tìm hardcoded secrets (IPs, passwords, tokens, webhooks)
- **`make security-scan`** — Makefile target chạy secret scanner
- **Case study: Ansible Network** — Real-world v4.0.0 workflow example (`docs/case-study-ansible-network.md`)
- **Demo: Ansible Network How-to** — T3 example tạo bởi AI agent (`demo-site/docs/guides/how-to/ansible-network-howto.md`)

### Changed

- **`AGENTS.md`** — Thêm Security section + boundary "DO NOT hardcode credentials"
- **Prompts (10 files)** — Thêm Security rule vào tất cả `create-*.md`
- **All docs** — Version footers sync to 4.x.0

---

## [4.0.0] — 2026-03-28

### Added

- **AI-Agent-First workflow** — Recommended approach: AI agent tạo docs từ prompt templates (tool-agnostic: Claude, ChatGPT, Antigravity, Copilot, hoặc bất kỳ agent nào)
- **`AGENTS.md`** — Agent context file duy nhất, tool-agnostic, hướng dẫn AI agent cách dùng toolkit
- **`prompts/` directory** — 12 prompt templates cho AI agent tạo docs (create-runbook, create-adr, select-skill, review-doc...)
- **`skills/AGENT-CARDS.json`** — JSON summary of all 5 skills cho agent fast-lookup (<2KB thay vì ~16K tokens)

### Changed

- **Templates (T1-T11)** — UI/UX upgrade: admonitions cho metadata, task lists cho checklists, step-by-step code blocks cho procedures
- **Demo site (7 files)** — Apply UI patterns, responsive tables CSS, sortable tables JS
- **`demo-site/mkdocs.yml`** — Enable `pymdownx.tasklist`, `navigation.instant.prefetch`, sortable tables
- **`demo-site/extra.css`** — Responsive tables, expanded width (68rem), cell borders, zebra striping
- **`docs/getting-started.md`** — Prerequisites table, AI Agent (Recommended) + Manual workflow, Prompts concept section
- **`docs/walkthrough-first-doc.md`** — Full 11-step workflow với pass/fail handling cho mỗi bước
- **`docs/doc-quality-scorecard.md`** — Gộp #5 Visual & UI/UX (giữ thang 10)
- **`scripts/score_docs.py`** — Thêm `visual_uiux` criterion (mermaid + admonitions + task lists)
- **`scripts/docs-toolkit`** — Auto-register new docs in mkdocs.yml nav
- **`Makefile`** — Lint/validate error guidance (AI Agent + Manual fix hints)
- **`.gitignore`** — Thêm generated config files (setup.sh tạo ở root)
- **`README.md`** — v4.0.0, workflow 3 bước dạng table, thêm `prompts/`
- **`CONTRIBUTING.md`** — Update directory map, thêm `prompts/` contribution guide

---

## [3.1.0] — 2026-03-27

### Added

- **ADR tracking system** — `docs/adr/` directory with 3 toolkit ADRs (MkDocs Material, 6-section model, directory restructure) + registry README
- **`docs-toolkit adr list`** — CLI command to display ADR registry from `docs/adr/`
- **Demo site T9-T11** — 3 new examples: ADR-002 PostgreSQL MADR (T9), ADR-003 API Versioning Lightweight (T10), Docker Knowledge Check (T11)
- **`scripts/score_docs.py`** — Automated doc quality scorer: 6 automatable criteria (structure, commands, prerequisites, metadata, markdown, freshness)
- **CI `score-docs` job** — 5th CI job runs doc quality scoring on every PR
- **Makefile** — 8 new scaffold targets (T5-T11 + security-policy + quick-reference) + `score` target

---

## [3.0.0] — 2026-03-27

### Added

- **`docs/diataxis-mapping.md`** — Diátaxis framework alignment guide: maps toolkit skills/templates to 4 documentation quadrants (Tutorials, How-to, Reference, Explanation)
- **`docs/adr-catalog.md`** — ADR format guide: 3 formats (Nygard/MADR/Lightweight) + decision tree + lifecycle + naming conventions
- **`docs/incident-patterns.md`** — 6-category failure taxonomy (Config/Hardware/Resource/Time/Database/Cascading) with real-world examples + investigation checklists
- **`docs/training-assessment-guide.md`** — Assessment design with Bloom's Taxonomy mapping + competency tracking
- **`templates/adr-madr.md` (T9)** — MADR format ADR for complex decisions with structured pros/cons
- **`templates/adr-lightweight.md` (T10)** — Lightweight ADR for quick decisions (~15 lines)
- **`templates/knowledge-check.md` (T11)** — Knowledge check with collapsible Q&A + scenario-based assessment
- **4 new CLI generators** in `docs-toolkit`: `adr-madr`, `knowledge-check`, `security-policy`, `quick-reference`
- **YAML frontmatter validation** in `validate_skill.py` — checks `name`, `description`, `compatibility` fields
- **Token-based size check** in `validate_skill.py` — replaces arbitrary line limits with token warning (>8K) + section length check (≤100 lines/section)
- **Post-install validation** in `setup.sh` — verifies MkDocs, markdownlint, pre-commit after installation
- **`scripts/**` path trigger** in CI — scripts changes now trigger CI pipeline

### Changed

- **Related Skills** in all 5 skills trimmed to ≤4 entries + "See also" for external references
- **`skill-template.md`** quality checklist updated: "≤250 lines" → "≤8K tokens, section ≤100 lines"
- **`validate_skill.py`** — zero external dependencies (removed PyYAML, uses regex), Related Skills limit 4→5
- **README.md** — 11 templates (T1-T11), v3.0.0, added 4 new guides to docs table
- **CONTRIBUTING.md** — updated template IDs "T12, T13...", directory map shows 11 templates

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
