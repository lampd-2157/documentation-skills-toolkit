# Documentation Skills Toolkit — Agent Guide

> File này hướng dẫn AI agent (Claude, ChatGPT, Antigravity, Copilot, hoặc bất kỳ agent nào) cách sử dụng toolkit để tạo tài liệu.

## Project Overview

Bộ toolkit chuẩn hóa technical documentation. 5 skills, 11 templates (T1-T11), 12 prompt templates, CLI tool.

## Project Structure

```text
skills/        → 5 skill files (quy tắc viết doc) + AGENT-CARDS.json
templates/     → 11 document templates (T1-T11)
prompts/       → 12 prompt templates cho AI agent
docs/          → Guides và references
scripts/       → CLI tools (docs-toolkit, validate, score)
demo-site/     → MkDocs demo site
config/        → Lint, spell, pre-commit configs
```

## How to Create Documentation

### Recommended: AI Agent Workflow

1. Đọc `prompts/README.md` để chọn prompt phù hợp
2. Đọc prompt template tương ứng (ví dụ: `prompts/create-runbook.md`)
3. Làm theo hướng dẫn trong prompt: đọc skill → đọc template → tạo doc
4. Validate: `make lint`

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
| Write security policy | infra-security-doc | — |
| Setup MkDocs site | docs-engineer | — |

> Không biết chọn gì? Dùng `prompts/select-skill.md` hoặc đọc `skills/AGENT-CARDS.json` để scan nhanh.

## Commands

```bash
make serve      # Preview demo site (localhost:8000)
make lint       # Lint all markdown
make validate   # Validate skill files
make score      # Score doc quality
make build      # Build demo site (strict)
```

## Validation Rules

- Every doc MUST pass `make lint` (0 errors)
- Every doc MUST have YAML frontmatter with title + status
- Runbooks MUST have copy-paste commands + expected output
- ADRs MUST have Context → Decision → Consequences
- Training docs MUST have Prerequisites → Steps → Expected Result

## Conventions

- Language: Vietnamese primary, English cho technical terms
- Commit format: conventional commits (`feat`/`fix`/`docs`)
- Always run `make lint` before commit

## Boundaries

- DO NOT modify files in `skills/` unless explicitly asked
- DO NOT skip lint validation
- DO NOT generate content without reading the relevant skill file first
