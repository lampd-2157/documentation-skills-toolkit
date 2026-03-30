---
name: my-custom-skill
description: "Mô tả ngắn gọn skill + các trigger keywords. Ví dụ: Viết tài liệu X khi
  user đề cập đến keyword1, keyword2, keyword3."
compatibility: "MkDocs Material >= 9.0"
skill_version: "1.0.0"
author: "[Your Name / GitHub handle]"
---

# Skill: [Tên Skill]

## Viết [loại tài liệu]

**Agent:** [Documentation Agent]
**Source:** [Nguồn tham khảo — link nếu có]

---

## Context / Bối cảnh

| Key          | Value                                                |
| ------------ | ---------------------------------------------------- |
| **Category** | [docs / ops / security / training / ...]             |
| **Priority** | [core / high / medium]                               |
| **Triggers** | [Khi nào dùng skill này — keywords + scenarios]      |
| **Output**   | [Loại file output — ví dụ: policy .md, runbook .md]  |
| **Scope**    | IN: [...]. OUT: [...]                                |
| **Version**  | 1.0.0                                                |
| **Last Updated** | [YYYY-MM-DD]                                    |

> Mô tả ngắn 1-2 câu skill này làm gì.

---

## THE IRON LAW

**[Viết 1 câu bold — quy tắc không thể phá vỡ cho skill này.]**

> Ví dụ: "Every runbook MUST have copy-paste commands AND expected output — prose-only = useless."

---

## Guardrails

- [ ] [Guardrail 1 — checklist item phòng ngừa lỗi phổ biến]
- [ ] [Guardrail 2]
- [ ] [Guardrail 3]
- [ ] [Guardrail 4 — tối thiểu 2, tối đa 5]

---

## Khi nào dùng Skill này

```text
User request
  ├── [Scenario A]?
  │     └── YES → Dùng skill này (Section X)
  ├── [Scenario B]?
  │     └── YES → Dùng skill này (Section Y)
  └── [Thuộc domain khác]?
        └── NO  → Xem [related-skill].md
```

| Dùng skill này khi...  | KHÔNG dùng khi...       |
| ---------------------- | ----------------------- |
| [Use case 1]           | [Anti use case 1]       |
| [Use case 2]           | [Anti use case 2]       |

---

## 1. [Section chính 1]

[Nội dung hướng dẫn chi tiết]

---

## 2. [Section chính 2]

[Nội dung hướng dẫn chi tiết]

---

## Pre-delivery Checklist

Trước khi báo "done", verify:

- [ ] [Check 1 — liên quan đến Iron Law]
- [ ] [Check 2 — liên quan đến output quality]
- [ ] [Check 3 — markdown lint pass]

---

## Error Journal — Never Repeat Failures

| Date     | Error       | Root Cause    | Prevention Rule     |
| -------- | ----------- | ------------- | ------------------- |
| template | [Ví dụ lỗi] | [Nguyên nhân] | [Cách phòng ngừa]  |

> **Rule:** Mỗi lần phát hiện lỗi → thêm 1 row.

---

## Red Flags — STOP

| Action                        | Problem                            |
| ----------------------------- | ---------------------------------- |
| [Hành động nguy hiểm 1]      | → [Hậu quả + cách fix]            |
| [Hành động nguy hiểm 2]      | → [Hậu quả + cách fix]            |
| [Hành động nguy hiểm 3]      | → [Hậu quả + cách fix]            |

---

## Remember

| Rule              | Description                          |
| ----------------- | ------------------------------------ |
| **[Rule 1]**      | [Mô tả ngắn]                        |
| **[Rule 2]**      | [Mô tả ngắn]                        |
| **[Rule 3]**      | [Mô tả ngắn — tối đa 6 rules]      |

## Related Skills

| Khi cần...                     | Xem skill                        |
| ------------------------------ | -------------------------------- |
| [Related domain 1]             | `[skill-name].md`                |
| [Related domain 2]             | `[skill-name].md`                |

> **See also:** [Templates](../../templates/)

<!-- Used: YYYY-MM-DD -->
