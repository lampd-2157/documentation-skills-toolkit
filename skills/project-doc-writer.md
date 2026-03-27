---
name: project-doc-writer
description: "Viết tài liệu phát triển dự án (.md): ADR (Architecture Decision Record),
  technical spec, how-to guide, quick reference card, cheat sheet. Dùng skill này khi
  người dùng đề cập đến: ghi nhận quyết định kiến trúc, viết spec kỹ thuật, tạo
  hướng dẫn step-by-step, làm cheat sheet, viết PRD — dù không gọi đích danh.
  Khi có từ khóa: ADR, architecture decision, tech spec, technical specification,
  how-to, hướng dẫn sử dụng, quick reference, cheat sheet, PRD, design doc,
  API contract → trigger skill này."
compatibility: "MkDocs Material >= 9.0"
---

# Skill: Project Doc Writer

## Viết tài liệu Phát triển dự án & Hướng dẫn

**Agent:** :pencil: [Documentation Agent]
**Source:** Adapted — [Google Developer Style Guide](https://developers.google.com/style), [gitlab.com/tgdp/templates](https://gitlab.com/tgdp/templates), [mkdocs-material](https://squidfunk.github.io/mkdocs-material/)

---

## Context / Bối cảnh

| Key          | Value                                                                                               |
| ------------ | --------------------------------------------------------------------------------------------------- |
| **Category** | docs                                                                                                |
| **Priority** | high                                                                                                |
| **Triggers** | Khi cần viết ADR, technical spec, how-to guide, quick reference, cheat sheet                        |
| **Output**   | ADR .md, tech spec .md, how-to guide .md, quick reference .md                                       |
| **Scope**        | IN: ADR, tech spec, how-to guides, quick reference cards. OUT: training, runbook, ops manual     |
| **Version**      | 1.0.0                                                                                               |
| **Last Updated** | 2026-03-27                                                                                          |

> Chuyên viết tài liệu phát triển dự án và hướng dẫn sử dụng. Mọi guide phải có Prerequisites → Steps → Expected Result → Troubleshooting.

---

## :no_entry: THE IRON LAW

**Every project doc MUST have clear structure with Context → Decision/Steps → Consequences/Result — ambiguous docs = wasted decisions.**

---

## :shield: Guardrails

- [ ] ADR có đầy đủ: Context → Decision → Alternatives → Consequences
- [ ] How-to guide có: Prerequisites → Steps → Expected Result → Troubleshooting
- [ ] Technical spec có: Overview → Design → Implementation Plan → Testing Strategy
- [ ] Quick reference chỉ chứa thông tin essential — không quá 2 trang khi in

---

## :dart: Khi nào dùng Skill này

```text
User request
  ├── Viết ADR / architecture decision?
  │     └── YES → Dùng skill này (Section 1)
  ├── Viết technical spec / design doc?
  │     └── YES → Dùng skill này (Section 1.2)
  ├── Viết how-to guide / tutorial?
  │     └── YES → Dùng skill này (Section 2)
  ├── Tạo quick reference / cheat sheet?
  │     └── YES → Dùng skill này (Section 3)
  ├── Viết training / onboarding docs?
  │     └── NO  → Xem training-doc-writer.md
  └── Viết runbook / ops docs?
        └── NO  → Xem ops-runbook-writer.md
```

| Dùng skill này khi...         | KHÔNG dùng khi...              |
| ----------------------------- | ------------------------------ |
| Viết project architecture ADR | Viết training material         |
| Tạo technical spec            | Tạo onboarding docs            |
| Viết how-to guide step-by-step | Viết runbook vận hành          |
| Tạo quick reference card      | Document network topology      |

---

## 1. Project Development Docs

### 1.1 Architecture Decision Record (ADR) Template

```markdown
# ADR-[NNN]: [Decision Title]

| Field         | Value                                                    |
| ------------- | -------------------------------------------------------- |
| **Status**    | Proposed / Accepted / Deprecated / Superseded by ADR-XXX |
| **Date**      | YYYY-MM-DD                                               |
| **Author**    | [Name]                                                   |
| **Reviewers** | [Names]                                                  |

## Context
[Vấn đề hoặc cơ hội dẫn đến decision này]

## Decision
[Decision cụ thể đã chọn]

## Alternatives Considered
| Option         | Pros                 | Cons         |
| -------------- | -------------------- | ------------ |
| Option A       | [ưu điểm]            | [nhược điểm] |
| **Option B** ✅ | [ưu điểm — chọn này] | [nhược điểm] |
| Option C       | [ưu điểm]            | [nhược điểm] |

## Consequences
- **Positive:** [Lợi ích]
- **Negative:** [Trade-offs chấp nhận]
- **Risks:** [Rủi ro cần monitor]
```

### 1.2 Technical Spec Template

````markdown
# Technical Spec: [Feature Name]

## Overview
- **Goal:** [1-2 câu mục tiêu]
- **Scope:** [IN scope / OUT of scope]

## Design
### Architecture Diagram
```mermaid
[diagram]
```

### Data Flow
1. [Step 1] → [Step 2] → [Step 3]

### API Contracts (nếu có)
| Endpoint        | Method | Request         | Response      |
| --------------- | ------ | --------------- | ------------- |
| `/api/resource` | POST   | `{ name: str }` | `{ id: int }` |

## Implementation Plan
- [ ] Phase 1: [description] — ETA: [date]
- [ ] Phase 2: [description] — ETA: [date]

## Testing Strategy
| Test Type   | Coverage Target | Tool        |
| ----------- | --------------- | ----------- |
| Unit        | > 80%           | Jest/Pytest |
| Integration | Critical paths  | Supertest   |
| E2E         | Happy path      | Playwright  |

## Rollout Plan
- [ ] Deploy to staging → verify
- [ ] Canary deploy 10% → monitor 1h
- [ ] Full deploy → post-deploy checks
````

---

## 2. How-to Guides

### 2.1 Guide Structure (Google Style)

```markdown
# How to [Complete Task]

> **Audience:** [Who is this for]
> **Time:** ~[X] minutes
> **Difficulty:** ⭐ Beginner / ⭐⭐ Intermediate / ⭐⭐⭐ Advanced

## Prerequisites
- [ ] [Tool/access cần thiết 1]
- [ ] [Tool/access cần thiết 2]

## Steps

### Step 1: [Action verb + object]

[Giải thích ngắn tại sao step này cần thiết]

```bash
command-to-run --flag value
```

**Expected result:**
```
output mong đợi
```

!!! tip
    [Mẹo hữu ích cho step này]

### Step 2: [Action verb + object]
[...]

## Verify
- [ ] [Cách kiểm tra kết quả đúng]
- [ ] [Second verification point]

## Troubleshooting

??? warning "Error: [Common error message]"
    **Cause:** [Nguyên nhân phổ biến]
    **Fix:** [Cách sửa step-by-step]

## Next Steps
- [Related guide 1](link)
- [Related guide 2](link)
```

### 2.2 Good / Bad Examples

```markdown
<!-- ✅ GOOD — có prerequisites, steps rõ ràng, expected result -->
## Prerequisites
- Node.js ≥ 18 installed
- Git configured with SSH key

### Step 1: Clone the repository
```bash
git clone git@github.com:org/project.git
cd project
```
**Expected result:** Directory `project/` created with `package.json` inside.

<!-- ❌ BAD — thiếu prerequisites, không có expected result -->
### Setup
Clone the project and install dependencies.
Then configure the environment variables and start the server.
```

---

## 3. Quick Reference Cards

### 3.1 Cheat Sheet Template

````markdown
# [Tool/System] — Quick Reference

## Essential Commands
| Action     | Command          | Example              |
| ---------- | ---------------- | -------------------- |
| [Action 1] | `command [args]` | `command --flag val` |
| [Action 2] | `command [args]` | `command --flag val` |

## Keyboard Shortcuts (nếu có)
| Action | Shortcut       |
| ------ | -------------- |
| Save   | `Ctrl+S`       |
| Search | `Ctrl+Shift+F` |

## Common Patterns
```bash
# Pattern 1: [description]
command pattern here

# Pattern 2: [description]
command pattern here
```

## Glossary
| Term     | Definition                     |
| -------- | ------------------------------ |
| [Term 1] | [Giải thích ngắn gọn, ≤ 20 từ] |
| [Term 2] | [Giải thích]                   |
````

---

## :white_check_mark: Pre-delivery Checklist — Project Docs

Trước khi báo "done", verify:

- [ ] ADR có đầy đủ Alternatives Considered với pros/cons
- [ ] How-to guide có Prerequisites → Steps → Expected Result → Troubleshooting
- [ ] Tech spec có Architecture Diagram + Implementation Plan
- [ ] Quick reference không quá 2 trang — chỉ essential info
- [ ] Tất cả links valid — internal + external
- [ ] markdownlint pass — 0 errors

---

## :triangular_flag_on_post: Red Flags — STOP

| Action                            | Problem                                                 |
| --------------------------------- | ------------------------------------------------------- |
| ADR không có Alternatives         | → Decision không có context → khó hiểu sau 6 tháng      |
| How-to guide thiếu expected result | → Reader không biết đúng/sai → hỏi lại = waste time    |
| Tech spec không có rollout plan   | → Deploy blind → risk cao                                |
| Quick reference quá dài           | → Không ai đọc → nên tách thành guide riêng             |
| Copy-paste từ doc cũ              | → Verify content match current version                  |

---

## Remember

| Rule                    | Description                                               |
| ----------------------- | --------------------------------------------------------- |
| **ADR = 4 parts**       | Context → Decision → Alternatives → Consequences          |
| **How-to = 4 parts**    | Prerequisites → Steps → Expected Result → Troubleshoot    |
| **Spec = design first** | Architecture Diagram trước khi viết Implementation Plan    |
| **Active voice**        | "Click Save" not "Save should be clicked"                 |
| **Concise reference**   | Quick reference ≤ 2 trang — chỉ essential commands/info   |

## :link: Related Skills

| Khi cần...                       | Xem skill                              |
| -------------------------------- | -------------------------------------- |
| Viết training / onboarding docs  | `training-doc-writer.md`               |
| Setup MkDocs, markdown standards | `docs-engineer.md`                     |
| Viết runbook / ops docs          | `ops-runbook-writer.md`                |
| Copy-paste doc templates         | `references/templates/doc-templates-library.md`  |
| MkDocs plugins recommendation    | `references/guides/mkdocs-plugins-catalog.md` |

<!-- Used: 2026-03-27 -->
