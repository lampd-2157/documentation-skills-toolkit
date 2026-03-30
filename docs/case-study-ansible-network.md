<!-- markdownlint-disable MD046 -->
# Case Study: Tạo "Ansible for Network" bằng v4.0.0 Workflow

> Mô tả chi tiết quá trình AI agent tạo ra file
> [ansible-network-howto.md](../demo-site/docs/guides/how-to/ansible-network-howto.md) —
> từ chọn skill tới push code.

---

## Bối cảnh

**Yêu cầu:** Viết hướng dẫn sử dụng Ansible để quản lý thiết bị mạng Cisco IOS — bao gồm cài đặt, cấu hình inventory, viết playbook backup config và deploy VLAN.

**Người dùng:** Network engineer, biết Linux cơ bản, chưa dùng Ansible.

---

## Step 1: Chọn Skill + Template

### AI Agent đã làm gì?

Đọc `AGENTS.md` → scan bảng Skill Selection:

| User wants to... | Use skill | Template |
|---|---|---|
| Write how-to guide | project-doc-writer | T3 |

**Reasoning:**

- "Hướng dẫn step-by-step" → **T3 How-to Guide** (không phải T1 Runbook vì đây là hướng dẫn 1 lần, không phải SOP lặp lại)
- Tuy nhiên, doc có **network commands** cần copy-paste + expected output → kết hợp `ops-runbook-writer` Iron Law

**Cross-check:** Mở `docs/getting-started.md` flowchart → "Step-by-step cho 1 task cụ thể?" → T3 How-to Guide. Đúng.

!!! tip "Best Practice: Kết hợp skills"
    Khi doc cần elements từ nhiều skills, chọn **1 primary skill** (quyết định structure) + áp dụng **Iron Law** từ secondary skill cho content quality. Ở đây:

    - **Primary:** `project-doc-writer` → structure T3 (Prerequisites → Steps → Verify → Troubleshooting)
    - **Secondary:** `ops-runbook-writer` Iron Law → "Every command MUST be copy-paste ready + expected output"

!!! success "Result"
    Skill: `project-doc-writer` + `ops-runbook-writer` Iron Law | Template: T3

---

## Step 2: Customize Prompt

### AI Agent đã làm gì?

Mở `prompts/create-howto.md` → copy phần Prompt → sửa đoạn `<<<< SỬA ĐOẠN NÀY >>>>`:

**Trước (template):**

```text
Tạo user mới trên Google Workspace, gán vào đúng OU và groups,
setup email signature chuẩn công ty.

Audience: IT admin mới, đã biết Google Admin Console cơ bản.
<<<< SỬA ĐOẠN NÀY THÀNH TASK CỦA BẠN >>>>
```

**Sau (customized):**

```text
Hướng dẫn sử dụng Ansible để quản lý thiết bị mạng Cisco IOS,
bao gồm cài đặt, cấu hình inventory, viết playbook backup config
và deploy VLAN.

Audience: Network engineer, biết Linux cơ bản, chưa dùng Ansible.
```

!!! tip "Best Practice: Context càng chi tiết → output càng tốt"
    Thêm thông tin cụ thể giúp AI tạo doc chính xác hơn:

    - Device cụ thể: "Cisco IOS" (không phải generic "network device")
    - Tasks cụ thể: "backup config + deploy VLAN" (không phải "quản lý mạng")
    - Audience level: "biết Linux cơ bản, chưa dùng Ansible"

!!! success "Result"
    Prompt customized, paste vào AI agent → AI bắt đầu đọc skill + template

---

## Step 3: AI Build Doc

### AI Agent đã làm gì?

1. **Đọc skill file** `skills/project-doc-writer.md` → ghi nhớ Iron Law + Guardrails
2. **Đọc template** `templates/howto-guide.md` → hiểu cấu trúc output
3. **Đọc thêm** `skills/ops-runbook-writer.md` → áp dụng Iron Law cho network commands
4. **Generate** nội dung theo structure T3

### Iron Law Check

| Rule | Applied? | Evidence |
|---|---|---|
| **project-doc-writer:** Context → Steps → Result | Yes | Prerequisites → 6 Steps → Verify → Troubleshooting |
| **ops-runbook-writer:** Copy-paste commands + expected output | Yes | Mọi command có code block + "Expected result" |

### UI Standards Check

| Standard | Applied? | Evidence |
|---|---|---|
| Admonitions cho metadata/warnings | Yes | `!!! info`, `!!! warning`, `!!! danger`, `!!! tip` |
| Task lists cho checklists | Yes | `- [ ]` trong Prerequisites |
| Code blocks cho commands | Yes | Tất cả commands trong fenced blocks có language tag |
| Mermaid diagram | Yes | Architecture diagram ở đầu doc |

!!! warning "Lưu ý: AI có thể thêm sections thừa"
    Trong lần build này, AI đã thêm 3 sections không thuộc T3 How-to:

    - ~~Health Check Matrix~~ (thuộc T1 Runbook)
    - ~~Escalation~~ (thuộc T1 Runbook)
    - ~~Completion Checklist~~ (không có trong template)

    **Fix:** Review output, xóa sections không thuộc template gốc. Đây là lý do **luôn cần review** — AI tạo draft tốt nhưng có thể over-generate.

!!! success "Result"
    Output file 560 dòng, đầy đủ structure T3 + ops-runbook Iron Law

---

## Step 4: Verify — Lint + Score

### 4.1: Lint

```bash
make lint
```

| Kết quả | Hành động |
|---------|-----------|
| `Summary: 0 error(s)` | PASS — doc theo template chuẩn, YAML header đúng, code blocks có language tag |

!!! tip "Tại sao lint thường pass khi dùng AI?"
    AI agent đã đọc `skills/docs-engineer.md` guardrail: "markdownlint 0 errors". Nên output thường đã clean sẵn. Nếu fail → paste errors vào AI, yêu cầu fix.

### 4.2: Score

```bash
python3 scripts/score_docs.py demo-site/docs/guides/how-to/ansible-network-howto.md
```

**Kết quả mong đợi:**

```text
PASS 5.5/6 ansible-network-howto.md [structure:1 | commands:1 | prerequisites:1 | metadata:0.5 | visual_uiux:1 | freshness:1]
```

| Criterion | Score | Lý do |
|-----------|-------|-------|
| structure | 1 | YAML frontmatter + h1 + h2 |
| commands | 1 | Nhiều code blocks có language tag |
| prerequisites | 1 | "Prerequisites" section rõ ràng |
| metadata | 0.5 | Có title nhưng thiếu status trong YAML (partial) |
| visual_uiux | 1 | Admonitions + task lists + mermaid |
| freshness | 1 | Created today |

!!! tip "Score < 4/6?"
    Xem tiêu chí nào bị 0 → fix cụ thể. Hoặc dùng `prompts/review-doc.md` để AI review đầy đủ 10 tiêu chí.

!!! success "Result"
    Lint: 0 errors | Score: >= 4/6 PASS

---

## Step 5: Register + Preview + Commit

### 5.1: Thêm vào mkdocs.yml

Nếu dùng CLI scaffold (`docs-toolkit new howto`), file tự động được append vào `mkdocs.yml`.

Nếu dùng AI agent tạo file → **phải thêm thủ công**:

```yaml
# demo-site/mkdocs.yml → nav section:
- Guides:
    - How-to:
      - Google Workspace New User (T3): guides/how-to/google-workspace-new-user.md
      - Ansible Network (T3): guides/how-to/ansible-network-howto.md  # ← thêm dòng này
```

!!! warning "Dễ quên"
    Đây là bước hay bị miss nhất. AGENTS.md + mỗi prompt đều nhắc, nhưng không có automation cho AI agent path. Luôn check sau khi `make serve`.

### 5.2: Preview

```bash
make serve
# Mở http://localhost:8000 → Guides → How-to → Ansible Network
```

Kiểm tra:

- [ ] Doc xuất hiện trong navigation sidebar
- [ ] Tables render đúng (border, zebra striping)
- [ ] Admonitions hiển thị (info/warning/danger boxes)
- [ ] Mermaid diagram render (không bị raw text)
- [ ] Code blocks có copy button

### 5.3: Commit

```bash
git add demo-site/docs/guides/how-to/ansible-network-howto.md demo-site/mkdocs.yml
git commit -m "docs(guides): add Ansible network automation how-to (T3)"
git push
```

!!! success "Result"
    Doc live trên MkDocs site, accessible qua navigation

---

## Tổng kết: Workflow v4.0.0 trong thực tế

```text
Step 1  CHỌN        → AGENTS.md → project-doc-writer + T3     (~2 phút)
Step 2  PROMPT       → prompts/create-howto.md → customize     (~3 phút)
Step 3  AI BUILD     → AI đọc skill + template → generate doc  (~5 phút)
Step 4  VERIFY       → make lint (0 errors) + score (>= 4/6)   (~2 phút)
Step 5  PUBLISH      → mkdocs.yml + make serve + commit        (~3 phút)
                                                        Total: ~15 phút
```

### So sánh: AI Agent vs Manual

| Metric | AI Agent (v4.0.0) | Manual (v3.x) |
|--------|-------------------|----------------|
| **Thời gian** | ~15 phút | ~60-90 phút |
| **Consistency** | Luôn theo template + Iron Law | Phụ thuộc người viết |
| **Quality** | Score 5-6/6 ngay lần đầu | Thường 3-4/6, cần iterate |
| **Review cần thiết** | Verify thông tin kỹ thuật + bỏ sections thừa | Review toàn bộ structure + content |

### Lessons Learned

1. **AI over-generates** — có thể thêm sections không thuộc template (Health Check, Escalation). Luôn review output vs template gốc
2. **Kết hợp skills hiệu quả** — primary skill cho structure + secondary Iron Law cho content quality
3. **Context chi tiết = output tốt** — "Cisco IOS + backup + VLAN" cho kết quả tốt hơn "network automation"
4. **Lint thường pass** — AI đã biết markdownlint rules, nhưng score có thể thấp nếu thiếu metadata
5. **mkdocs.yml là bước dễ quên nhất** — cần automation hoặc checklist reminder

---

> **Version:** 4.0.0 | **Updated:** 2026-03-30
