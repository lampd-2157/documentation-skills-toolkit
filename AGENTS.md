# Documentation Skills Toolkit — Agent Guide

> File này hướng dẫn AI agent (Claude, ChatGPT, Antigravity, Copilot, hoặc bất kỳ agent nào) cách sử dụng toolkit để tạo tài liệu.

## Project Overview

Bộ toolkit chuẩn hóa technical documentation. 6 skills, 14 templates (T1-T14), 15 prompt templates, CLI tool.

## Project Structure

```text
skills/        → 6 skill files (quy tắc viết doc) + AGENT-CARDS.json
templates/     → 14 document templates (T1-T14)
prompts/       → 15 prompt templates cho AI agent
docs/          → Guides và references
scripts/       → CLI tools (docs-toolkit, validate, score, route, wizard)
demo-site/     → MkDocs demo site
config/        → Lint, spell, pre-commit, routing configs
```

## How to Create Documentation

### Recommended: AI Agent Workflow

1. **Interview** — Hỏi user 3 câu trước: Audience? Scope? Environment? (xem `prompts/interview-before-create.md`)
2. Đọc `prompts/README.md` để chọn prompt phù hợp
3. Đọc prompt template tương ứng (ví dụ: `prompts/create-runbook.md`)
4. Làm theo hướng dẫn trong prompt: đọc skill → đọc template → tạo doc
5. Validate: `make lint` + `make security-scan`

### Alternative: Manual Workflow

1. Chọn skill phù hợp từ `skills/`
2. Scaffold: `./scripts/docs-toolkit new <type> "<title>"`
3. Đọc Iron Law + Guardrails của skill, điền nội dung
4. Validate: `make lint`

## Skill Selection

| User wants to... | Use skill | Template |
|---|---|---|
| Write runbook/SOP | ops-runbook-writer | T1 |
| Record architecture decision | project-doc-writer | T2/T9/T10 |
| Write how-to guide | project-doc-writer | T3 |
| Create training module | training-doc-writer | T4 |
| Document network topology | ops-runbook-writer | T5 |
| Write incident postmortem | ops-runbook-writer | T6 |
| Plan maintenance window | ops-runbook-writer | T7 |
| Write release notes | project-doc-writer | T8 |
| Create knowledge check | training-doc-writer | T11 |
| Create architecture diagram | project-doc-writer | T12 |
| Write API reference | api-doc-writer | T13 |
| Write security policy | infra-security-doc | T14 |
| Setup MkDocs site | docs-engineer | — |

> **Smart Routing:** Đọc `config/routing-signals.yaml` để tự động chọn skill dựa trên keywords.
> Không biết chọn gì? Dùng `prompts/select-skill.md` — AI sẽ phân tích keywords + confidence score.

## Commands

```bash
make serve            # Preview demo site (localhost:8000)
make lint             # Lint all markdown
make validate         # Validate skill files
make score            # Score doc quality
make build            # Build demo site (strict)
make route            # Interactive routing CLI — AI chọn skill dựa trên request (v5.3.0)
make wizard           # Wizard mode — guided doc creation from start to finish (v5.3.0)
make health-dashboard # Doc health dashboard — freshness, quality, coverage (v5.3.0)
make security-scan    # Scan for hardcoded secrets
```

## Template Section Tiers

Templates have 3 tiers (defined in each template's header comment + `skills/AGENT-CARDS.json`):

- **Required** — MUST exist in output, reject if missing
- **Recommended** — SHOULD exist, warn if missing
- **Optional** — MAY include when relevant (e.g., Rollback, Security Notes, FAQ)

> Đọc `skills/AGENT-CARDS.json` → `template_sections` để biết sections nào required/recommended/optional cho mỗi template.

## Validation Rules

- Every new doc MUST be added to `mkdocs.yml` nav section to appear on site — update nav after creating the file
- Every doc MUST pass `make lint` (0 errors)
- Every doc MUST have YAML frontmatter with title + status
- Every doc MUST include all `required` sections from template tier
- Runbooks MUST have copy-paste commands + expected output
- ADRs MUST have Context → Decision → Consequences
- Training docs MUST have Prerequisites → Steps → Expected Result

## Conventions

- Language: Vietnamese primary, English cho technical terms
- Commit format: conventional commits (`feat`/`fix`/`docs`)
- Always run `make lint` before commit

## Security

- KHÔNG hardcode sensitive data: IP nội bộ, password, token, internal URL
- Dùng placeholders: `<INTERNAL_IP>`, `<PASSWORD>`, `<API_TOKEN>`, `<INTERNAL_URL>`
- Dùng `example.com` cho domains, `192.0.2.x` cho demo IPs (RFC 5737)
- Chi tiết: đọc `docs/security-placeholders.md`
- Scan: `make security-scan`

## Boundaries

- DO NOT modify files in `skills/` unless explicitly asked
- DO NOT skip lint validation
- DO NOT generate content without reading the relevant skill file first
- DO NOT generate content without interviewing user first (Audience, Scope, Environment)
- DO NOT hardcode real credentials, IPs, or tokens in documentation

---

> **Version:** 5.4.0 | **Updated:** 2026-03-30
