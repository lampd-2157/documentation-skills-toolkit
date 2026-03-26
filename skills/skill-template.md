# Skill: [Tên Skill]

## [Subtitle ngắn — mô tả 1 dòng]

**Agent:** [Emoji + Tên Agent]

<!--
╔══════════════════════════════════════════════════════╗
║  SKILL TEMPLATE v1.0 — Universal Best Practices     ║
║                                                      ║
║  Sources:                                            ║
║  • IPortal Request (35 skills, 7 agents)             ║
║  • antigravity-workflows (guardrails)                ║
║  • tech-leads-club/agent-skills (references/)        ║
║  • planning-with-files (error journal)               ║
║  • ui-ux-pro-max-skill (pre-delivery checklist)      ║
║                                                      ║
║  Instructions:                                       ║
║  1. Copy file này khi tạo skill mới                  ║
║  2. Điền nội dung giữa các [ ] placeholders          ║
║  3. Xóa các "💡 Hướng dẫn:" và section không cần    ║
║  4. Sections có ⚠️ OPTIONAL → xóa nếu không cần     ║
║  5. Giữ thứ tự sections — KHÔNG đảo                  ║
║  6. Version: set to 1.0.0 for new skills             ║
║  7. Last Updated: set to current date (YYYY-MM-DD)   ║
╚══════════════════════════════════════════════════════╝
-->

---

## Context / Bối cảnh

| Key              | Value                                            |
| ---------------- | ------------------------------------------------ |
| **Category**     | [infrastructure / development / qa / docs / ops] |
| **Priority**     | [core / high / medium / low]                     |
| **Triggers**     | [Khi nào agent nên tự động dùng skill này?]      |
| **Output**       | [Skill này tạo ra cái gì? Code / doc / config?]  |
| **Scope**        | [Phạm vi: IN scope ↔ OUT of scope]               |
| **Version**      | [1.0.0]                                           |
| **Last Updated** | [YYYY-MM-DD]                                      |

> [Mô tả narrative 1-2 câu — skill này dùng để làm gì, agent nào chịu trách nhiệm.]

<!--
💡 Hướng dẫn: Kết hợp structured metadata + narrative blockquote.
   - Table: agent scan nhanh, script parse được, format nhất quán
   - Blockquote: người đọc hiểu ngữ cảnh, tại sao skill tồn tại
   - Category: infrastructure | development | qa | docs | ops | orchestration | architecture | data
   - Priority: core (luôn cần) | high (thường xuyên) | medium (khi cần) | low (hiếm)
   - Triggers: điều kiện cụ thể để agent activate skill
   - Output: sản phẩm cụ thể (measurable)
   - Scope: rõ ràng IN/OUT — tránh dùng sai skill
   - Version: semver format (1.0.0) — bump when skill content changes
   - Last Updated: date of last modification (YYYY-MM-DD)
-->

---

## ⛔ THE IRON LAW

**[MỘT CÂU DUY NHẤT — quy tắc tối quan trọng, KHÔNG BAO GIỜ vi phạm]**

<!--
💡 Hướng dẫn: Iron Law = quy tắc cao nhất. Ví dụ:
   ✅ "NEVER deploy without backup — NO EXCEPTIONS."
   ✅ "ALL changes MUST be backward compatible."
   ❌ "Try to follow best practices" (quá mơ hồ)
   ❌ Nhiều hơn 1 câu (quá phức tạp để nhớ)
-->

---

## 🛡 Guardrails

<!--
💡 Hướng dẫn: Guardrails = proactive prevention (ngăn LỖI trước khi xảy ra).
   Khác với Red Flags (reactive — dừng SAU khi phát hiện sai).
   Mỗi guardrail = 1 checkbox mà agent verify TRƯỚC khi bắt đầu task.
   Tối thiểu: 2 | Tối đa: 5 (quá nhiều = agent bỏ qua hết)
-->

- [ ] [Verify điều kiện tiên quyết TRƯỚC khi bắt đầu]
- [ ] [Check data source / input validity]
- [ ] [Confirm scope với stakeholder nếu ambiguous]

---

## 🎯 Khi nào dùng Skill này

<!--
💡 Hướng dẫn: Decision tree giúp agent biết KHI NÀO nên activate skill.
   Không có section này → agent phải đoán → dùng sai skill.
   Format: dùng flowchart text hoặc bảng điều kiện.
-->

```text
User request
  ├── Liên quan đến [domain X]?
  │     ├── YES → Dùng skill này
  │     └── NO  → Xem [skill-khác.md]
  │
  └── Đã có [prerequisite Y]?
        ├── YES → Bắt đầu từ Section 2
        └── NO  → Bắt đầu từ Section 1
```

| Dùng skill này khi... | KHÔNG dùng khi...          |
| --------------------- | -------------------------- |
| [Trigger condition 1] | [Out-of-scope condition 1] |
| [Trigger condition 2] | [Out-of-scope condition 2] |

---

## 1. [Main Content — Section đầu tiên]

<!--
💡 Hướng dẫn: Đây là phần nội dung chính.
   Best practices cho content:
   1. Chia thành sections đánh số (1, 2, 3...)
   2. Mỗi section = 1 task/concept cụ thể
   3. Code examples dùng ✅/❌ để so sánh đúng/sai
   4. Giữ mỗi section < 50 dòng (cognitive load)
   5. Nếu section > 50 dòng → tách ra references/
-->

### 1.1 [Sub-section nếu cần]

[Nội dung chính]

### 1.2 Good / Bad Examples

```javascript
// ✅ GOOD — [giải thích tại sao đúng]
const result = await fetchData({ timeout: 5000 });

// ❌ BAD — [giải thích tại sao sai]
const result = await fetchData(); // no timeout = hang forever
```

---

## 2. [Main Content — Section tiếp theo]

[Thêm sections tùy complexity của skill]

---

## 📖 References — ⚠️ OPTIONAL

<!--
💡 Hướng dẫn: Dùng references/ khi skill có:
   - Bảng lookup lớn (> 50 rows)
   - Schema definitions dài
   - Code snippets dài mà agent chỉ cần khi implement

   Tạo files trong: skills/references/[skill-name]-*.md
   Trong skill chính chỉ giữ summary + link.

   Benefit: Giảm cognitive load (token count) khi agent đọc skill.
   Pattern từ: tech-leads-club/agent-skills
-->

> 📖 **[Tên reference]** → [link-to-reference.md](references/link-to-reference.md)
>
> [Mô tả 1 dòng: file chứa gì]

---

## ✅ Pre-delivery Checklist — [Loại Output] — ⚠️ OPTIONAL

<!--
💡 Hướng dẫn: Chỉ thêm khi skill tạo ra OUTPUT cụ thể có thể validate.
   Ví dụ: workflow JSON, API endpoint, document, Slack message.
   KHÔNG thêm cho skills thuần "hướng dẫn" (như debugging, planning).

   Mỗi item phải:
   ✅ Kiểm chứng được (có/không, pass/fail)
   ❌ Không mơ hồ ("looks good" — không đo được)

   Pattern từ: ui-ux-pro-max-skill
-->

Trước khi báo "done", verify:

- [ ] [Measurable check 1 — ví dụ: "JSON.parse() passes"]
- [ ] [Measurable check 2 — ví dụ: "All endpoints return 200"]
- [ ] [Measurable check 3 — ví dụ: "No secrets in output"]
- [ ] [Measurable check 4 — ví dụ: "Tested on staging"]

---

## 📓 Error Journal — Never Repeat Failures — ⚠️ OPTIONAL

<!--
💡 Hướng dẫn: Chỉ thêm khi skill thường gặp lỗi recurring.
   Ví dụ: deploy skills, build skills, integration skills.
   KHÔNG thêm cho stable/ít-error skills (docs, planning).

   Table này là "living document" — agent thêm row mỗi lần fix bug.
   Seed 2-3 entries từ lịch sử lỗi thật để agent thấy pattern.

   Pattern từ: planning-with-files (Never Repeat Failures rule)
-->

Ghi lại lỗi đã fix để không lặp lại:

| Date       | Error                | Root Cause        | Prevention Rule     |
| ---------- | -------------------- | ----------------- | ------------------- |
| yyyy-mm-dd | [Mô tả lỗi ngắn gọn] | [Nguyên nhân gốc] | [Rule ngăn lặp lại] |

> **Rule:** Mỗi lần fix bug trong domain này → thêm 1 row.

---

## 🚩 Red Flags — STOP

<!--
💡 Hướng dẫn: Red Flags = reactive (DỪNG khi phát hiện sai).
   Khác Guardrails (proactive — verify trước).
   Mỗi flag = hành động nguy hiểm + hậu quả + cách đúng.
   Tối thiểu: 3 flags | Tối đa: 6
-->

| Action                  | Problem                      |
| ----------------------- | ---------------------------- |
| [Hành động nguy hiểm 1] | → [Hậu quả + hành động đúng] |
| [Hành động nguy hiểm 2] | → [Hậu quả + hành động đúng] |
| [Hành động nguy hiểm 3] | → [Hậu quả + hành động đúng] |

---

## Remember

<!--
💡 Hướng dẫn: Summary table — agent đọc nhanh khi cần refresh.
   Mỗi row = 1 rule ngắn gọn (≤ 15 từ).
   Tối đa 6 rules. Agent không nhớ được nhiều hơn.
-->

| Rule                 | Description                 |
| -------------------- | --------------------------- |
| **[Rule keyword 1]** | [Mô tả ngắn — tối đa 15 từ] |
| **[Rule keyword 2]** | [Mô tả ngắn]                |
| **[Rule keyword 3]** | [Mô tả ngắn]                |

## 🔗 Related Skills

<!--
💡 Hướng dẫn: Cross-references giúp agent navigate giữa skills.
   Chỉ link skills TRỰC TIẾP liên quan.
   Tối đa 4 entries (quá nhiều = noise).
-->

| Khi cần...             | Xem skill            |
| ---------------------- | -------------------- |
| [Use case liên quan 1] | `related-skill-1.md` |
| [Use case liên quan 2] | `related-skill-2.md` |

<!-- Used: yyyy-mm-dd -->

<!--
╔══════════════════════════════════════════════════════╗
║  📊 QUALITY CHECKLIST — Verify trước khi ship        ║
║                                                      ║
║  Structure:                                          ║
║  □ THE IRON LAW = 1 câu duy nhất, mạnh, cụ thể      ║
║  □ Guardrails có 2-5 checkbox items                  ║
║  □ Red Flags có 3-6 entries                          ║
║  □ Remember có ≤ 6 rules                             ║
║  □ Sections theo đúng thứ tự template                ║
║                                                      ║
║  Content:                                            ║
║  □ Tổng lines ≤ 250 (threshold cognitive load)       ║
║  □ Mỗi section ≤ 50 dòng                             ║
║  □ Code examples có ✅/❌ so sánh                     ║
║  □ Không có placeholder [ ] chưa điền                ║
║  □ <!-- Used: yyyy-mm-dd --> ở cuối file             ║
║                                                      ║
║  Optional sections:                                  ║
║  □ Pre-delivery Checklist → chỉ khi có output        ║
║  □ Error Journal → chỉ khi error-prone               ║
║  □ References → chỉ khi data > 50 rows               ║
║  □ Metadata table → recommended cho mọi skill        ║
║                                                      ║
║  Anti-patterns:                                      ║
║  ✗ Iron Law > 1 câu                                  ║
║  ✗ Guardrails > 5 items (agent bỏ qua hết)           ║
║  ✗ Section > 50 dòng mà chưa tách references         ║
║  ✗ Red Flags mơ hồ ("be careful")                    ║
║  ✗ Remember > 6 rules                                ║
╚══════════════════════════════════════════════════════╝
-->
