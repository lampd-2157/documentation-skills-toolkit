# Walkthrough: Tạo Document Đầu Tiên

> Hands-on exercise: tạo document đầu tiên từ A-Z. Đọc [Getting Started](getting-started.md) trước nếu chưa hiểu toolkit hoạt động thế nào.
>
> **Thời gian:** ~20 phút | **Yêu cầu:** Git, Python 3.8+, Node.js 20+

---

## Bước 1: Clone và Setup

```bash
# Clone toolkit
git clone https://github.com/lampd-2157/documentation-skills-toolkit.git
cd documentation-skills-toolkit

# One-command setup
bash scripts/setup.sh
```

**Kết quả mong đợi:**

```text
Setting up Documentation Skills Toolkit...
  Detected OS: Linux
  MkDocs installed
  markdownlint-cli2 installed
  ...
  Verified: 3 passed, 0 failed
Setup complete!
```

---

## Bước 2: Chọn Skill phù hợp

Bạn cần viết loại document nào? Đọc bảng dưới và chọn:

| Cần viết gì? | Dùng Skill | Template |
|---------------|-----------|----------|
| Runbook vận hành server | `ops-runbook-writer` | T1 Runbook |
| Ghi nhận quyết định kiến trúc | `project-doc-writer` | T2 ADR |
| Hướng dẫn step-by-step | `project-doc-writer` | T3 How-to |
| Training cho team | `training-doc-writer` | T4 Training |
| Document network/server | `ops-runbook-writer` | T5 Network |

> **Ví dụ này:** Tạo Runbook cho Nginx service (T1).

---

## Bước 2.1: Chọn cách tiếp cận

**AI Agent (Recommended):**
Mở [prompts/create-runbook.md](../prompts/create-runbook.md) — copy phần Prompt,
paste vào AI agent (Claude, ChatGPT, Antigravity, Copilot...),
sửa đoạn có dấu `<<<< SỬA ... >>>>` bằng thông tin thực tế, ví dụ "Nginx Load Balancer".
AI sẽ đọc skill + template và tạo doc cho bạn. Sau đó nhảy tới **Bước 6** (Verify).

**Manual:** Tiếp tục Bước 3 bên dưới.

---

## Bước 3: Đọc Skill trước khi viết

```bash
# Mở skill file để hiểu quy tắc
cat skills/ops-runbook-writer.md | head -40
```

**Ghi nhớ 3 điều quan trọng từ skill:**

1. **Iron Law:** "Every runbook MUST have copy-paste commands AND expected output"
2. **Guardrails:** Mọi command phải test được, contact info phải up-to-date
3. **Structure:** Overview → Health Checks → Common Tasks → Troubleshooting → Escalation

---

## Bước 4: Scaffold document từ template

```bash
# Tạo runbook mới bằng CLI
./scripts/docs-toolkit new runbook "Nginx Load Balancer"
```

**Kết quả:**

```text
Created: docs/operations/runbooks/nginx-load-balancer-runbook.md

Next steps:
  1. Edit the file and fill in the placeholders
  2. Run: docs-toolkit validate docs/operations/runbooks/nginx-load-balancer-runbook.md
  3. Preview: make serve
  4. Add to mkdocs.yml nav section
```

---

## Bước 5: Điền nội dung vào template

Mở file `docs/operations/runbooks/nginx-load-balancer-runbook.md` và thay thế các `[placeholder]`.

Có 2 cách tiếp cận:

**Cách 1: Dùng AI Agent (Recommended)** —
Mở [prompts/create-runbook.md](../prompts/create-runbook.md), copy phần Prompt,
paste vào AI agent (Claude, ChatGPT, Antigravity, Copilot...).
AI sẽ đọc skill + template và tạo nội dung.
Bạn chỉ cần **review và chỉnh sửa** cho phù hợp thực tế.

**Cách 2: Viết thủ công** —
Mở file bằng editor, thay từng `[placeholder]` theo hướng dẫn trong skill.
Đọc **Iron Law** (1 câu) + **Guardrails** (3-5 checkboxes) của skill tương ứng.

**Trước (template):**

```markdown
## Health Checks
| Check        | Command                | Expected | Alert If    |
| ------------ | ---------------------- | -------- | ----------- |
| [check name] | `[copy-paste command]` | [output] | [condition] |
```

**Sau (đã điền):**

```markdown
## Health Checks
| Check        | Command                          | Expected         | Alert If       |
| ------------ | -------------------------------- | ---------------- | -------------- |
| Nginx alive  | `curl -sI http://localhost:80`   | `HTTP/1.1 200`   | No 200 response |
| Config valid | `nginx -t`                       | `syntax is ok`   | syntax error   |
| Disk usage   | `df -h /var/log/nginx`           | `Use% < 80%`    | > 90%          |
```

> **Iron Law check:** Mỗi row có command copy-paste được + expected output? ✅

---

## Bước 6: Verify document

```bash
# Lint markdown
make lint

# Validate (nếu là skill file)
make validate
```

**Kết quả mong đợi:**

```text
Summary: 0 error(s)
```

> Nếu có lỗi, đọc error message và fix. Phổ biến nhất:
>
> - MD031: Thiếu blank line trước/sau code block
> - MD040: Code block thiếu language tag (thêm `bash`, `text`, `json`...)

---

## Bước 7: Preview trên browser

```bash
# Start dev server
make serve
```

Mở browser tại `http://localhost:8000` — tìm document vừa tạo trong navigation.

**Kiểm tra:**

- [ ] Markdown render đúng (tables, code blocks, headings)
- [ ] Mermaid diagrams hiển thị (nếu có)
- [ ] Links hoạt động

---

## Bước 8: Commit và Push

```bash
# Stage file mới
git add docs/operations/runbooks/nginx-load-balancer-runbook.md

# Commit theo conventional format
git commit -m "docs(ops): add nginx load balancer runbook"

# Push
git push
```

---

## Bước 9: Pre-delivery Checklist

Trước khi gọi "done", verify theo skill's checklist:

- [ ] Mọi command trong doc đã test — copy-paste chạy được
- [ ] Expected output ghi rõ — người đọc biết kết quả đúng/sai
- [ ] Contact info / escalation matrix up-to-date
- [ ] Diagrams render đúng trong MkDocs
- [ ] IP addresses, hostnames, ports chính xác

---

## Tổng kết Flow

```text
1. CHỌN SKILL     → Đọc Iron Law + Guardrails
2. SCAFFOLD        → ./scripts/docs-toolkit new <type> <title>
3. ĐIỀN NỘI DUNG  → Thay [placeholder] bằng content thật
4. VERIFY          → make lint (0 errors)
5. PREVIEW         → make serve (check browser)
6. COMMIT          → git add + commit + push
7. CHECKLIST       → Verify theo skill's Pre-delivery Checklist
```

## Các loại document khác

| Muốn tạo... | Command |
|-------------|---------|
| ADR | `./scripts/docs-toolkit new adr "Decision Title"` |
| How-to guide | `./scripts/docs-toolkit new howto "Task Name"` |
| Training module | `./scripts/docs-toolkit new training "Topic"` |
| Network topology | `./scripts/docs-toolkit new network "Environment"` |
| Postmortem | `./scripts/docs-toolkit new postmortem "Incident"` |
| Knowledge check | `./scripts/docs-toolkit new knowledge-check "Topic"` |
| Security policy | `./scripts/docs-toolkit new security-policy "Policy"` |

> **Danh sách đầy đủ:** `./scripts/docs-toolkit list`

---

> **Version:** 1.0.0 | **Cập nhật:** 2026-03-27
