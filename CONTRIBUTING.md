# Contributing Guide

> Hướng dẫn đóng góp vào **Documentation Skills Toolkit**.

---

## 🤝 Cách đóng góp

| Loại               | Mô tả                                            | Cần PR?    |
| ------------------ | ------------------------------------------------ | ---------- |
| **Fix typo**       | Sửa lỗi chính tả, format                         | ✅          |
| **Thêm template**  | Thêm template mới vào `doc-templates-library.md` | ✅          |
| **Thêm skill**     | Tạo skill mới theo `skill-template.md`           | ✅ + Review |
| **Cải tiến skill** | Cập nhật nội dung skill hiện tại                 | ✅ + Review |

---

## 📐 Skill Authoring Guide

### Cấu trúc bắt buộc (6 sections)

Mọi skill **PHẢI** có đủ 6 sections theo thứ tự:

```text
1. ## Context / Bối cảnh        — Mô tả scope, trigger, output
2. ## ⛔ THE IRON LAW            — 1 rule tối thượng, KHÔNG vi phạm
3. ## 🛡 Guardrails              — Checklist kiểm soát chất lượng
4. ## 🚩 Red Flags — STOP       — Dấu hiệu cần dừng lại
5. ## Remember                   — Bảng tóm tắt rules quan trọng
6. ## 🔗 Related Skills          — Cross-reference tới skills khác
```

### Naming Convention

- **File name:** `kebab-case.md` — ví dụ: `ops-runbook-writer.md`
- **Agent field:** Dùng `[Documentation Agent]` (generic, không gắn dự án cụ thể)
- **Related Skills:** CHỈ link tới files trong `templates/` — không link ra bên ngoài

### Checklist trước khi submit

- [ ] Có đủ 6 sections bắt buộc
- [ ] Iron Law rõ ràng, 1 câu duy nhất
- [ ] Guardrails có ≥ 3 items
- [ ] Decision tree trong "Khi nào dùng Skill này"
- [ ] Pre-delivery checklist trước Red Flags
- [ ] Related Skills chỉ link internal

---

## 📋 Template Authoring Guide

### Thêm template mới

1. Chọn ID tiếp theo: `T9`, `T10`, ...
2. Viết template trong `references/doc-templates-library.md`
3. Format bắt buộc:

```markdown
## T[N]: [Template Name] Template

\```markdown
# [Document Title]

| Field     | Value   |
| --------- | ------- |
| **Field** | [value] |

## [Section 1]
[content]

## [Section 2]
[content]
\```
```

4. Cập nhật Template Index ở đầu file

---

## ✅ PR Checklist

Trước khi tạo Pull Request:

- [ ] `markdownlint` pass — 0 errors
- [ ] File naming: kebab-case lowercase
- [ ] YAML metadata header (nếu applicable)
- [ ] Không có project-specific references
- [ ] Related Skills chỉ link internal
- [ ] README.md updated (nếu thêm skill/template mới)
- [ ] Test trên local: `mkdocs build --strict` pass (nếu applicable)

---

## 📝 Style Guide

| Rule                    | Ví dụ đúng                   | Ví dụ sai                   |
| ----------------------- | ---------------------------- | --------------------------- |
| **kebab-case filename** | `ops-runbook-writer.md`      | `OpsRunbookWriter.md`       |
| **Active voice**        | "Click Save"                 | "Save should be clicked"    |
| **Present tense**       | "This command installs"      | "This command will install" |
| **Short sentences**     | Max 25 words/sentence        | —                           |
| **YAML header**         | `title`, `status`, `updated` | No header                   |
| **Code blocks**         | Always specify language      | No language tag             |

---

## 🤗 Code of Conduct

- **Respectful** — Feedback mang tính xây dựng
- **Constructive** — Đề xuất giải pháp, không chỉ nêu vấn đề
- **Inclusive** — Document cho mọi skill level, không assume knowledge

---

> **Version:** 1.0.0 | **Cập nhật:** 2026-03-26
