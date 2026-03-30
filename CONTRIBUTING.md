# Contributing Guide

> Hướng dẫn đóng góp vào **Documentation Skills Toolkit**.

---

## Cách đóng góp

| Loại               | Mô tả                                                      | Cần PR?    |
| ------------------ | ---------------------------------------------------------- | ---------- |
| **Fix typo**       | Sửa lỗi chính tả, format                                   | Yes          |
| **Thêm template**  | Thêm template mới vào `templates/` directory | Yes          |
| **Thêm skill**     | Tạo skill mới theo `skills/skill-template.md`               | Yes + Review |
| **Cải tiến skill** | Cập nhật nội dung skill hiện tại trong `skills/`            | Yes + Review |

---

## Skill Authoring Guide

### Cấu trúc bắt buộc (6 sections)

Mọi skill **PHẢI** có đủ 6 sections theo thứ tự:

```text
1. ## Context / Bối cảnh        — Mô tả scope, trigger, output (+ Version, Last Updated)
2. ## ⛔ THE IRON LAW            — 1 rule tối thượng, KHÔNG vi phạm
3. ## 🛡 Guardrails              — Checklist kiểm soát chất lượng
4. ## 🚩 Red Flags — STOP       — Dấu hiệu cần dừng lại
5. ## Remember                   — Bảng tóm tắt rules quan trọng
6. ## 🔗 Related Skills          — Cross-reference tới skills khác
```

### Naming Convention

- **File location:** Tất cả skills nằm trong `skills/` directory
- **File name:** `kebab-case.md` — ví dụ: `ops-runbook-writer.md`
- **Agent field:** Dùng `[Documentation Agent]` (generic, không gắn dự án cụ thể)
- **Related Skills:** CHỈ link tới files trong `skills/`, `docs/`, `templates/` — không link ra bên ngoài

### Validation

```bash
# Validate skill structure trước khi submit
python3 scripts/validate_skill.py skills/your-new-skill.md

# Lint markdown
npx markdownlint-cli2 skills/your-new-skill.md
```

### Checklist trước khi submit

- [ ] File nằm trong `skills/` directory
- [ ] Có đủ 6 sections bắt buộc
- [ ] Iron Law rõ ràng, 1 câu duy nhất
- [ ] Guardrails có 2-5 items
- [ ] Red Flags có 3-6 entries
- [ ] Remember có ≤ 6 rules
- [ ] Context table có **Version** và **Last Updated** rows
- [ ] `python3 scripts/validate_skill.py` passes
- [ ] Related Skills chỉ link internal

---

## Template Authoring Guide

### Thêm template mới

1. Chọn ID tiếp theo: `T12`, `T13`, ...
2. Tạo file mới trong `templates/` — ví dụ: `templates/your-template.md`
3. Template là file markdown thuần — copy-paste được ngay
4. Cập nhật `templates/README.md` index table
5. Cập nhật `README.md` Templates table

---

## PR Checklist

Trước khi tạo Pull Request:

- [ ] `markdownlint` pass — 0 errors
- [ ] File naming: kebab-case lowercase
- [ ] YAML metadata header (nếu applicable)
- [ ] Không có project-specific references
- [ ] Related Skills chỉ link internal
- [ ] README.md updated (nếu thêm skill/template mới)
- [ ] CHANGELOG.md updated
- [ ] Test trên local: `mkdocs build --strict` pass (nếu applicable)

---

## Style Guide

| Rule                    | Ví dụ đúng                   | Ví dụ sai                   |
| ----------------------- | ---------------------------- | --------------------------- |
| **kebab-case filename** | `ops-runbook-writer.md`      | `OpsRunbookWriter.md`       |
| **Active voice**        | "Click Save"                 | "Save should be clicked"    |
| **Present tense**       | "This command installs"      | "This command will install" |
| **Short sentences**     | Max 25 words/sentence        | —                           |
| **YAML header**         | `title`, `status`, `updated` | No header                   |
| **Code blocks**         | Always specify language       | No language tag             |

---

## Directory Map

```text
skills/                    # 5 skills + template + AGENT-CARDS.json
templates/                 # 11 document templates (T1-T11)
prompts/                   # 13 prompt templates cho AI agent
docs/                      # Guides: getting-started, lifecycle, recipes...
config/                    # Configs: markdownlint, cspell, pre-commit...
examples/                  # Starter configs cho project khác
scripts/                   # CLI tools: setup.sh, docs-toolkit, validate_skill.py
evals/                     # Eval test suite cho mỗi skill
demo-site/                 # MkDocs example site
```

### Thêm prompt template mới

- **File location:** `prompts/` directory
- **Naming:** `create-<type>.md` hoặc `<action>.md` (ví dụ: `create-runbook.md`, `review-doc.md`)
- **Format:** Theo cấu trúc trong `prompts/README.md` — phải có: Cách dùng (AI + Manual), Prompt section, Validation checklist

---

## Code of Conduct

- **Respectful** — Feedback mang tính xây dựng
- **Constructive** — Đề xuất giải pháp, không chỉ nêu vấn đề
- **Inclusive** — Document cho mọi skill level, không assume knowledge

---

> **Version:** 5.4.0 | **Updated:** 2026-03-30
