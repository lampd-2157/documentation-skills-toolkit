<!-- markdownlint-disable MD046 -->
# Case Study: Tạo "Ansible for Network" bằng v5.3.0 Workflow

> Mô tả chi tiết quá trình AI agent tạo ra file
> [ansible-network-howto.md](how-to/ansible-network-howto.md) —
> từ **Routing CLI** + **Phase 0 Interview** + **Health Dashboard** tới push code.
>
> v5.3.0 bổ sung: `docs-toolkit route` (CLI phân tích tự động), `docs-toolkit wizard`
> (interactive mode), `generate_health_dashboard.py` (quality overview), và
> `routing-feedback.yaml` (feedback loop).

---

## Bối cảnh

**Yêu cầu:** Viết hướng dẫn sử dụng Ansible để quản lý thiết bị mạng Cisco IOS — bao gồm cài đặt, cấu hình inventory, viết playbook backup config và deploy VLAN.

**Người dùng:** Network engineer, biết Linux cơ bản, chưa dùng Ansible.

---

## Phase 0: Smart Routing + Interview (v5.3.0)

### 0.1: Routing CLI — `docs-toolkit route`

**NEW in v5.3.0:** Thay vì đọc thủ công `routing-signals.yaml`, chạy 1 lệnh:

```bash
./scripts/docs-toolkit route "Viết how-to guide sử dụng Ansible cho network automation, có troubleshooting và copy-paste commands"
```

**Output thực tế:**

```text
Smart Routing Analysis
──────────────────────────────────────────────────
Input: Viết how-to guide sử dụng Ansible cho network automation,
       có troubleshooting và copy-paste commands
──────────────────────────────────────────────────

Skill Scores:

  ██████████████░░░░░░ 0.70 project-doc-writer ASK USER ★
  Keywords: how-to, guide
  Templates: adr=T2, howto=T3, release-notes=T8, adr-madr=T9, adr-lightweight=T10

  ████████████░░░░░░░░ 0.60 ops-runbook-writer ASK USER
  Keywords: troubleshooting
  Templates: runbook=T1, network=T5, postmortem=T6, maintenance=T7

Composition Rule: How-to with commands
  Primary: project-doc-writer
  Secondary Iron Law: ops-runbook-writer

Recommendation: Suggest project-doc-writer but confirm with user (confidence 0.70)
```

**Phân tích output:**

| Element | Ý nghĩa |
|---------|---------|
| `0.70 project-doc-writer ★` | Skill score cao nhất, được đề xuất. Keywords match: "how-to", "guide" |
| `0.60 ops-runbook-writer` | Skill thứ 2 match. Keyword: "troubleshooting" |
| `ASK USER` | Confidence < 0.8 → CLI suggest nhưng hỏi user confirm |
| `Composition Rule: How-to with commands` | Hai skills match → auto-detect composition rule |
| `Primary: project-doc-writer` | Structure T3 (Prerequisites → Steps → Verify) |
| `Secondary Iron Law: ops-runbook-writer` | "Every command MUST be copy-paste ready + expected output" |

!!! tip "So sánh: v5.3.0 CLI vs v5.0.0 manual"
    **v5.0.0:** AI phải đọc `routing-signals.yaml` → tự parse keywords → tính confidence thủ công.
    **v5.3.0:** 1 lệnh CLI → output visual với confidence bars, keyword matches, composition rules.
    Kết quả: nhanh hơn, minh bạch hơn, reproducible (chạy lại luôn cho cùng kết quả).

!!! note "JSON mode cho automation"
    ```bash
    ./scripts/docs-toolkit route --json "Viết how-to guide..."
    ```
    Trả về JSON — dùng trong CI pipeline hoặc script tự động.

### 0.1b: Alternative — Wizard Mode (v5.3.0)

Thay vì chạy `route` + tự customize prompt, dùng **wizard** cho workflow tất-cả-trong-một:

```bash
./scripts/docs-toolkit wizard
```

Wizard hỏi interactive:

```text
╔══════════════════════════════════════╗
║   Documentation Wizard - Phase 0    ║
╚══════════════════════════════════════╝

Mô tả ngắn về doc cần tạo:
> Viết how-to guide sử dụng Ansible cho network automation

[Routing Analysis]
  ★ project-doc-writer (0.60) — Keywords: hướng dẫn
  Composition: How-to with commands

Audience (ai sẽ đọc doc này?):
> Network engineer, biết Linux cơ bản, chưa dùng Ansible

Scope (doc bao gồm những gì?):
> Cài đặt Ansible, inventory, playbook backup + deploy VLAN

Environment (môi trường/tools):
> Ubuntu/CentOS, Ansible 2.16+, Cisco IOS/IOS-XE, SSH

Ghi chú thêm (Enter để bỏ qua):
> Credentials qua Ansible Vault

Chọn template [T3]:
> T3

Tên file (không cần .md):
> ansible-network-howto

✅ Created: output/ansible-network-howto.md
```

!!! success "Wizard = Route + Interview + Scaffold trong 1 lệnh"
    Wizard chạy routing analysis tự động, hỏi Phase 0 interview questions,
    rồi tạo file doc từ template — tất cả trong terminal.
    Dùng khi muốn workflow nhanh nhất. Dùng `route` riêng khi chỉ cần phân tích.

### 0.2: Phase 0 Interview

Dù dùng wizard hay manual, interview context là:

**Layer 1 — Universal (luôn hỏi):**

```text
1. AUDIENCE: Network Engineer / Junior SysAdmin — biết Linux cơ bản, chưa dùng Ansible
2. SCOPE: Cài đặt Ansible, cấu hình inventory, viết playbook backup config + deploy VLAN.
          Không cover initial network topology setup.
3. ENVIRONMENT: Linux (Ubuntu/CentOS), Ansible 2.16+, Cisco IOS/IOS-XE devices, SSH có sẵn
```

**Layer 2 — How-to specific:**

```text
4. TASK cụ thể: Cài đặt → inventory → vault → gather-facts → backup → deploy VLAN
5. PREREQUISITES: Python 3.8+, SSH connectivity, enable password
6. EXPECTED OUTPUT: Người đọc có thể chạy playbook backup + deploy VLAN sau khi follow guide
```

**Layer 3 — Deep-dive:** Bỏ qua (how-to guide đơn giản, không có phân tích kiến trúc phức tạp).

!!! success "Interview outcome"
    AI có đủ context để: chọn đúng prerequisites (Python version cụ thể, SSH test command),
    viết troubleshooting phù hợp (4 lỗi thực tế), và xác định scope rõ ràng.

### 0.3: Template Section Tiers Decision

**T3 How-to Guide — section tiers** (từ `skills/AGENT-CARDS.json`):

| Section | Tier | Quyết định | Lý do |
|---------|------|-----------|-------|
| Prerequisites | Required | INCLUDE | Critical — setup validation |
| Steps | Required | INCLUDE | 6 steps chính |
| Verify | Required | INCLUDE | Trong mỗi step có verify block |
| Troubleshooting | Recommended | INCLUDE | 4 lỗi phổ biến thực tế |
| Rollback | Optional | SKIP | Không có rollback cho cài đặt Ansible |
| Security Notes | Optional | INCLUDE | Vault là phần thiết yếu của flow |
| FAQ | Optional | SKIP | Troubleshooting đủ chi tiết rồi |
| Next Steps | Optional | INCLUDE | Hướng dẫn tiếp tục sau khi setup xong |

---

## Step 1: Chọn Skill + Template

### AI Agent đã làm gì?

Smart Routing CLI từ Phase 0 đã tự động xác định:

- **Primary skill:** `project-doc-writer` → structure T3 How-to Guide
- **Secondary Iron Law:** `ops-runbook-writer` → commands quality standards
- **Template:** T3 (Prerequisites → Steps → Verify → Troubleshooting)

**Cross-check với AGENTS.md:**

| User wants to... | Use skill | Template |
|---|---|---|
| Write how-to guide | project-doc-writer | T3 |

"Hướng dẫn step-by-step cho 1 task cụ thể?" → T3 How-to Guide. Đúng.

!!! success "Result"
    Skill: `project-doc-writer` + `ops-runbook-writer` Iron Law | Template: T3
    **Tự động** từ composition rule — `docs-toolkit route` xác nhận.

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

**Sau (customized — với interview context từ Phase 0):**

```text
Hướng dẫn sử dụng Ansible để quản lý thiết bị mạng Cisco IOS,
bao gồm cài đặt, cấu hình inventory, viết playbook backup config
và deploy VLAN.

Audience: Network engineer, biết Linux cơ bản, chưa dùng Ansible.
Environment: Ubuntu/CentOS, Ansible 2.16+, Cisco IOS/IOS-XE.
Scope: Không cover initial topology setup.
```

!!! tip "Best Practice: Interview context → prompt context"
    Interview answers từ Phase 0 được embed trực tiếp vào prompt.
    AI nhận được context đầy đủ → output chính xác hơn, ít iteration hơn.

!!! success "Result"
    Prompt customized với interview context, paste vào AI agent → AI bắt đầu đọc skill + template

---

## Step 3: AI Build Doc

### AI Agent đã làm gì?

1. **Đọc skill file** `skills/project-doc-writer.md` → Iron Law + Guardrails
2. **Đọc template** `templates/howto-guide.md` → structure T3
3. **Đọc thêm** `skills/ops-runbook-writer.md` → Iron Law cho commands
4. **Generate** với section tiers từ Phase 0 decision

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

    **Fix:** Review output vs template tiers từ Phase 0. Xóa sections không trong tier decision.
    Đây là lý do **luôn cần review** — AI tạo draft tốt nhưng có thể over-generate.

!!! success "Result"
    Output file đầy đủ structure T3 + ops-runbook Iron Law + Phase 0 Interview Context block

---

## Step 4: Verify — Lint + Score + Security + Health

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

**Kết quả thực tế:**

```text
PASS 6.0/6 ansible-network-howto.md [structure:1 | commands:1 | prerequisites:1 | metadata:1 | visual_uiux:1 | freshness:1]
```

| Criterion | Score | Lý do |
|-----------|-------|-------|
| structure | 1 | YAML frontmatter đầy đủ (+ skill/template/routing fields) |
| commands | 1 | Copy-paste commands + expected output (ops-runbook Iron Law) |
| prerequisites | 1 | Prerequisites section rõ ràng với task list |
| metadata | 1 | YAML đầy đủ: title, description, author, status, tags, skill, template |
| visual_uiux | 1 | Admonitions + task lists + mermaid diagram |
| freshness | 1 | File mới tạo/updated gần đây |

### 4.3: Security Scan

```bash
make security-scan
```

**Expected result:**

```text
Scanning: demo-site/docs/guides/how-to/ansible-network-howto.md
PASS: No hardcoded IPs, credentials, or tokens found
File uses safe patterns: 10.0.x.x (example range), vault variables, placeholders
```

### 4.4: Health Dashboard (NEW in v5.3.0)

Sau khi verify file mới, chạy dashboard để xem tổng quan quality toàn project:

```bash
make health-dashboard
# hoặc: python3 scripts/generate_health_dashboard.py
```

**Output thực tế (trích):**

```text
# Doc Health Dashboard
> Auto-generated: 2026-03-30 16:25

## Overview
| Metric | Count |
|--------|-------|
| Skills | 6 |
| Templates | 14 |
| Prompts | 15 |
| Eval test cases | 29 |
| Documentation files | 18 |

## Quality Scores
| File | Score | Status | Freshness |
|------|-------|--------|-----------|
| ansible-network-howto.md | 6.0/6 | PASS | 0d old |     ← file vừa tạo
| docs-engineer.md | 5.5/6 | PASS | 4d old |
| project-doc-writer.md | 5.5/6 | PASS | 3d old |
| ...
| adr-catalog.md | 1.5/6 | FAIL | no date found |       ← cần cải thiện
| getting-started.md | 2.5/6 | FAIL | no date found |

Average: 3.1/6 | Pass: 6 | Warn: 3 | Fail: 11
```

!!! info "Health Dashboard giúp gì?"
    Sau khi tạo doc mới, dashboard cho thấy **toàn cảnh quality** — không chỉ file vừa tạo
    mà cả project. Phát hiện docs cũ cần update, files thiếu metadata, freshness alerts.
    Team lead nhìn vào 1 bảng biết ngay trạng thái documentation.

!!! success "Result"
    Lint: 0 errors | Score: 6.0/6 PASS | Security: PASS | Dashboard: overview generated

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
- [ ] Phase 0 Interview Context block hiển thị đúng
- [ ] Code blocks có copy button

### 5.3: Commit

```bash
git add demo-site/docs/guides/how-to/ansible-network-howto.md demo-site/mkdocs.yml
git commit -m "docs(guides): add Ansible network automation how-to (T3, v5.3.0 workflow)"
git push
```

!!! success "Result"
    Doc live trên MkDocs site, accessible qua navigation

---

## Step 6: Log Feedback (NEW in v5.3.0)

Sau khi doc hoàn thành, log routing decision vào feedback loop:

```yaml
# config/routing-feedback.yaml — append entry:
feedback_log:
  - date: "2026-03-30"
    input: "Viết how-to guide sử dụng Ansible cho network automation"
    routed_to: "project-doc-writer"
    confidence: 0.70
    correct: true
    user_correction: null
```

!!! tip "Feedback loop cải thiện routing theo thời gian"
    Sau khi tích lũy đủ entries (`min_samples: 5`), hệ thống tự động
    điều chỉnh `keyword_adjustments` — tăng confidence cho patterns đúng,
    giảm cho patterns sai. Ví dụ: nếu "network" luôn route đúng tới
    `ops-runbook-writer` → boost +0.05 cho keyword đó.

    Config: `max_adjustment: 0.2`, `feedback_ttl_days: 90`

---

## Tổng kết: Workflow v5.3.0 trong thực tế

```text
Phase 0  ROUTE CLI   → docs-toolkit route → visual analysis     (~30 giây)
Phase 0  INTERVIEW   → Layer 1+2 questions → context gathered    (~3 phút)
Phase 0  SECTIONS    → T3 tier decision table                    (~1 phút)
Step 1   CHỌN        → Auto từ composition rule + cross-check    (~1 phút)
Step 2   PROMPT      → prompts/create-howto.md → customize       (~2 phút)
Step 3   AI BUILD    → AI đọc skill + template → generate doc    (~5 phút)
Step 4   VERIFY      → lint + score + security + health dashboard(~3 phút)
Step 5   PUBLISH     → mkdocs.yml + make serve + commit          (~3 phút)
Step 6   FEEDBACK    → Log routing decision                      (~30 giây)
                                                        Total: ~19 phút
```

### So sánh: v5.3.0 vs v5.0.0 vs v4.0.0 vs Manual

| Metric | v5.3.0 AI Agent | v5.0.0 AI Agent | v4.0.0 AI Agent | Manual (v3.x) |
|--------|-----------------|-----------------|-----------------|----------------|
| **Routing** | CLI 1 lệnh (`route`) | Đọc YAML thủ công | Manual | Manual |
| **Interview** | Wizard hoặc manual | Manual | Không có | Không có |
| **Section control** | Explicit tier decision | Explicit tier | Không có | Không có |
| **Verify** | lint + score + security + **dashboard** | lint + score + security | lint + score | lint |
| **Feedback loop** | `routing-feedback.yaml` | Không có | Không có | Không có |
| **Consistency** | Rất cao | Rất cao | Cao | Thấp |
| **Quality score** | 6/6 | 5-6/6 | 4-5/6 | 3-4/6 |

### v5.3.0 Tools cheat sheet

| Tool | Command | Khi nào dùng |
|------|---------|-------------|
| Route | `docs-toolkit route "mô tả"` | Phân tích keywords + confidence trước khi tạo doc |
| Route JSON | `docs-toolkit route --json "mô tả"` | Dùng trong CI/script automation |
| Wizard | `docs-toolkit wizard` | Tạo doc interactive (route + interview + scaffold) |
| Score | `python3 scripts/score_docs.py <file>` | Chấm điểm 1 file cụ thể |
| Dashboard | `make health-dashboard` | Xem quality overview toàn project |
| Security | `make security-scan` | Scan secrets/credentials trong docs |

### Lessons Learned

1. **`docs-toolkit route` thay thế đọc YAML thủ công** — 1 lệnh cho output visual, reproducible, shareable
2. **Composition rule auto-detect** — CLI tự phát hiện khi 2+ skills match, không cần nhớ rules
3. **Wizard cho người mới** — không cần biết prompt structure, wizard hỏi từng bước
4. **Health Dashboard sau mỗi doc mới** — phát hiện knock-on effects (docs cũ, freshness alerts)
5. **Feedback loop là investment dài hạn** — routing accuracy tăng theo thời gian khi log đủ entries
6. **AI over-generates** — có thể thêm sections không thuộc template. Luôn review vs tier decision
7. **Interview context = output tốt hơn** — "Cisco IOS + Ubuntu + Ansible 2.16+" cho output cụ thể hơn "network automation"
8. **mkdocs.yml là bước dễ quên nhất** — cần checklist reminder hoặc automation
