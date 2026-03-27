# ADR-0003: Purpose-Driven Directory Structure

| Field | Value |
|-------|-------|
| **Status** | Accepted |
| **Date** | 2026-03-27 |
| **Author** | DulapReal |

## Context

`references/` directory là catch-all mixing configs, guides, templates. Gây confusion cho new users, vi phạm single-responsibility principle.

## Decision

Eliminate `references/`, thay bằng 4 directories:
- `config/` — project configs consumed by tooling
- `docs/` — human-readable guides
- `examples/` — starter configs cho other projects
- `templates/` — copy-paste document templates

## Consequences

- **Positive:** Mỗi directory có 1 purpose rõ ràng, dễ navigate
- **Negative:** Breaking change — tất cả internal links phải update
- **Risks:** Contributors quen cấu trúc cũ cần thời gian adapt
