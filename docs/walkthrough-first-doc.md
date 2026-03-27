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

Mở terminal, **đảm bảo đang ở thư mục root** của toolkit (nơi có file `Makefile`):

```bash
cd ~/documentation-skills-toolkit

# Kiểm tra format markdown (tất cả file .md trong project)
make lint

# Kiểm tra cấu trúc skill files (chỉ cần khi sửa files trong skills/)
make validate
```

> `make lint` chạy `markdownlint` trên tất cả `.md` files. `make validate` chạy `validate_skill.py` kiểm tra 6-section structure.

**Kết quả mong đợi:**

```text
Summary: 0 error(s)
```

> Nếu có lỗi, đọc error message và fix. Phổ biến nhất:
>
> - MD031: Thiếu blank line trước/sau code block
> - MD040: Code block thiếu language tag (thêm `bash`, `text`, `json`...)

---

## Bước 7: Kiểm tra mkdocs.yml

CLI `docs-toolkit` đã **tự động thêm** doc mới vào `mkdocs.yml` nav. Tuy nhiên, nó append ở cuối file — bạn cần mở `mkdocs.yml` và **di chuyển entry** vào đúng section:

```yaml
# Mở demo-site/mkdocs.yml, tìm entry vừa được thêm ở cuối, di chuyển vào đúng section:
nav:
  - Operations:
    - Runbooks:
      - Proxmox VM (T1): operations/runbooks/proxmox-vm-runbook.md
      - Nginx LB: operations/runbooks/nginx-load-balancer-runbook.md  # ← di chuyển vào đây
```

---

## Bước 8: Chấm điểm chất lượng

```bash
# Chấm điểm doc vừa tạo (6 tiêu chí tự động, max 6/6)
python3 scripts/score_docs.py docs/operations/runbooks/nginx-load-balancer-runbook.md
```

**Kết quả mong đợi:**

```text
  PASS 5.0/6 nginx-load-balancer-runbook.md [structure:1 | commands:1 | prerequisites:1 | metadata:0.5 | visual_uiux:0.5 | freshness:1]
```

> Score >= 4/6 là PASS. Nếu thấp hơn, xem tiêu chí nào bị 0 và cải thiện.
> Muốn review đầy đủ 10 tiêu chí? Dùng prompt [prompts/review-doc.md](../prompts/review-doc.md).

---

## Bước 9: Preview trên browser

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

## Bước 10: Commit và Push

```bash
# Stage file mới + mkdocs.yml
git add docs/operations/runbooks/nginx-load-balancer-runbook.md demo-site/mkdocs.yml

# Commit theo conventional format
git commit -m "docs(ops): add nginx load balancer runbook"

# Push
git push
```

---

## Bước 11: Pre-delivery Checklist

Trước khi gọi "done", verify theo skill's checklist:

- [ ] Mọi command trong doc đã test — copy-paste chạy được
- [ ] Expected output ghi rõ — người đọc biết kết quả đúng/sai
- [ ] Contact info / escalation matrix up-to-date
- [ ] Diagrams render đúng trong MkDocs
- [ ] IP addresses, hostnames, ports chính xác

---

## Tổng kết Flow

```text
AI Agent (Recommended):
  1. CHỌN PROMPT    → prompts/create-<type>.md
  2. AI TẠO DOC     → Paste prompt vào AI agent → review kết quả
  3. MKDOCS.YML     → Thêm doc vào nav (AI agent tự làm)
  4. LINT            → make lint (0 errors)
  5. SCORE           → python3 scripts/score_docs.py <file> (>= 4/6)
  6. PREVIEW         → make serve (check browser)
  7. COMMIT          → git add + commit + push

Manual:
  1. CHỌN SKILL     → Đọc Iron Law + Guardrails
  2. SCAFFOLD        → ./scripts/docs-toolkit new <type> <title> (auto thêm mkdocs.yml)
  3. ĐIỀN NỘI DUNG  → Thay placeholder bằng content thật
  4. LINT            → make lint (0 errors)
  5. SCORE           → python3 scripts/score_docs.py <file> (>= 4/6)
  6. PREVIEW         → make serve (check browser)
  7. COMMIT          → git add + commit + push
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
