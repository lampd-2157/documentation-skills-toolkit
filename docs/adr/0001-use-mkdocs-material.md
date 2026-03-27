# ADR-0001: Use MkDocs Material as Documentation Platform

| Field | Value |
|-------|-------|
| **Status** | Accepted |
| **Date** | 2026-03-26 |
| **Author** | DulapReal |

## Context

Cần chọn static site generator cho documentation toolkit. Yêu cầu: Markdown-native, đẹp out-of-box, hỗ trợ tiếng Việt, có admonitions/tabs/diagrams, active community.

## Decision

Chọn MkDocs với Material theme (mkdocs-material >= 9.0).

## Alternatives Considered

| Option | Pros | Cons |
|--------|------|------|
| **MkDocs Material** ✅ | Đẹp, feature-rich, Markdown, Vietnamese support | Python dependency |
| Docusaurus | React ecosystem, MDX support | Heavy, requires Node.js |
| Hugo | Fastest build, Go binary | Limited Markdown extensions |
| Sphinx | Python standard, RST + MD | Complex config, học curve cao |

## Consequences

- **Positive:** Beautiful docs, admonitions, tabs, Mermaid diagrams built-in
- **Negative:** Requires Python + pip, some plugins unmaintained
- **Risks:** Material entering maintenance mode (Zensical successor planned)
