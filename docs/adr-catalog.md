# ADR Catalog — Architecture Decision Records Guide

> Hướng dẫn sử dụng ADR trong dự án: chọn format, naming conventions, lifecycle management.
>
> Sources: [joelparkerhenderson/architecture-decision-record](https://github.com/joelparkerhenderson/architecture-decision-record), [adr.github.io/madr](https://adr.github.io/madr/)

---

## Chọn ADR Format

| Format | Khi nào dùng | Ví dụ | Template |
| ------ | ------------ | ----- | -------- |
| **Nygard** | Standard decisions — team đã quen ADR, cần Context → Decision → Consequences | Chọn database, chọn framework | [adr.md](../templates/adr.md) (T2) |
| **MADR** | Complex decisions — nhiều stakeholders, cần structured pros/cons cho từng option | Migration strategy, architecture overhaul, vendor selection | [adr-madr.md](../templates/adr-madr.md) (T9) |
| **Lightweight** | Quick decisions — experiments, POC, small scope, < 5 phút viết | Library choice, config change, naming convention | [adr-lightweight.md](../templates/adr-lightweight.md) (T10) |

### Decision Tree

```text
Quyết định cần document
  ├── Ảnh hưởng ≤ 1 team, dễ revert?
  │     └── Lightweight ADR (T10) — viết trong 5 phút
  ├── Ảnh hưởng nhiều teams, cần alternatives analysis?
  │     ├── ≤ 3 options, pros/cons rõ ràng?
  │     │     └── Nygard ADR (T2) — standard choice
  │     └── > 3 options, cần structured evaluation?
  │           └── MADR (T9) — detailed comparison
  └── Không chắc?
        └── Bắt đầu với Nygard (T2) — đủ cho 80% trường hợp
```

---

## ADR Lifecycle

```text
Proposed → Accepted → [Active] → Deprecated / Superseded
    │          │                       │
    │          │                       └── Superseded by ADR-NNN
    │          └── Team review + approval
    └── Author draft
```

| Status | Ý nghĩa | Action required |
| ------ | -------- | --------------- |
| **Proposed** | Draft, đang chờ review | Team review trong 1 sprint |
| **Accepted** | Đã approved, đang áp dụng | Follow decision |
| **Deprecated** | Không còn relevant | Document lý do deprecate |
| **Superseded** | Thay thế bởi ADR mới | Link tới ADR mới |

### Review Schedule

- **Mandatory review:** mỗi 6 tháng cho ADR status "Accepted"
- **Trigger review:** khi context thay đổi (new tech, team restructure, scale change)
- **Sunset clause:** ADR chưa được review > 12 tháng → tự động chuyển "Needs Review"

---

## Naming Conventions

### File naming

```text
docs/development/adr/
├── 0001-use-mkdocs-material.md
├── 0002-choose-postgresql.md
├── 0003-adopt-microservices.md
└── README.md                    # ADR index/registry
```

**Rules:**

- Prefix số 4 chữ số: `0001`, `0002`, ...
- kebab-case, lowercase
- Present tense imperative verb: `choose-database` (không phải `chose-database`)
- Max 50 ký tự trong filename (không tính prefix + extension)

### CLI scaffold

```bash
# Nygard format (default)
./scripts/docs-toolkit new adr "Choose Database"
# → docs/development/adr/adr-001-choose-database.md

# MADR format
# Copy templates/adr-madr.md manually và rename

# Lightweight format
# Copy templates/adr-lightweight.md manually và rename
```

---

## ADR Registry

Mỗi project nên có `docs/development/adr/README.md` làm registry:

```markdown
# Architecture Decision Records

| # | Title | Status | Date | Superseded by |
|---|-------|--------|------|---------------|
| 1 | [Use MkDocs Material](0001-use-mkdocs-material.md) | Accepted | 2026-01-15 | — |
| 2 | [Choose PostgreSQL](0002-choose-postgresql.md) | Accepted | 2026-02-01 | — |
| 3 | [Adopt REST over GraphQL](0003-adopt-rest.md) | Deprecated | 2026-02-15 | ADR-005 |
```

**Update rules:**

- Thêm row mỗi khi tạo ADR mới
- Update status khi ADR được review/deprecated
- Link "Superseded by" khi có ADR thay thế

---

## Best Practices

### DO

- Viết ADR **ngay khi quyết định**, không phải sau khi implement
- Bao gồm **Alternatives Considered** — dù chỉ 1 alternative
- Ghi rõ **trade-offs** chấp nhận — giúp người sau hiểu context
- **Link related ADRs** — decisions thường có dependencies
- **Review quarterly** — context thay đổi, decision có thể outdated

### DON'T

- Viết ADR cho decisions quá nhỏ (naming conventions → dùng Lightweight)
- Sửa ADR đã Accepted — tạo ADR mới Supersede ADR cũ
- Bỏ trống Consequences — phần quan trọng nhất
- Viết ADR quá dài (> 2 pages) — split thành Tech Spec + ADR

---

> **Version:** 4.0.0 | **Updated:** 2026-03-30
