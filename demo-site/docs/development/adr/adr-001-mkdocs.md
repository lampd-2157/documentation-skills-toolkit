---
title: "ADR-001: Chọn MkDocs-Material làm documentation platform"
description: "Architecture decision record — tại sao chọn MkDocs-Material thay vì các alternatives"
author: "Documentation Team"
created: 2026-03-26
updated: 2026-03-26
status: Accepted
tags: [adr, mkdocs, documentation]
---

# ADR-001: Chọn MkDocs-Material làm Documentation Platform

| Field         | Value                |
| ------------- | -------------------- |
| **Status**    | Accepted             |
| **Date**      | 2026-03-26           |
| **Author**    | Documentation Team   |
| **Reviewers** | Infra Team, Dev Team |

## Context

Team cần 1 documentation platform để:

- Tập trung tài liệu từ nhiều mảng (network, server, automation)
- Viết docs trong Markdown, quản lý qua Git
- Auto-deploy khi push code
- Hỗ trợ search, dark mode, mobile responsive

## Decision

Chọn **MkDocs-Material** làm documentation platform chính.

## Alternatives Considered

| Option                | Pros                                       | Cons                                           |
| --------------------- | ------------------------------------------ | ---------------------------------------------- |
| Confluence            | WYSIWYG editor, real-time collab           | Tốn phí, không version control, vendor lock-in |
| **MkDocs-Material** ✅ | Free, Git-based, 22k+ stars, rich features | Cần biết Markdown, CLI-based                   |
| GitBook               | UI đẹp, hosting free tier                  | Limited customization, rate limits             |
| Docusaurus            | React-based, versioning                    | Overkill cho docs project, cần Node.js         |

## Consequences

- **Positive:** Free, version control built-in, CI/CD auto-deploy, rich plugin ecosystem
- **Negative:** Team cần học Markdown (curve thấp, ~1 ngày)
- **Risks:** Nếu team member không quen CLI → cung cấp VS Code snippets + templates
