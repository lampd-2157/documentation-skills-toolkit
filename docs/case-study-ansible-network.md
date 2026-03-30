<!-- markdownlint-disable MD046 -->
# Case Study: Tạo "Ansible for Network" bằng v5.0.0 Workflow (Smart Routing + Interview)

> Mô tả chi tiết quá trình AI agent tạo ra file
> [ansible-network-howto.md](../demo-site/docs/guides/how-to/ansible-network-howto.md) —
> từ Smart Routing + Phase 0 Interview tới push code.

---

## Bối cảnh

**Yêu cầu:** Viết hướng dẫn sử dụng Ansible để quản lý thiết bị mạng Cisco IOS — bao gồm cài đặt, cấu hình inventory, viết playbook backup config và deploy VLAN.

**Người dùng:** Network engineer, biết Linux cơ bản, chưa dùng Ansible.

---

## Phase 0: Smart Routing + Interview (NEW in v5.0.0)

### 0.1: Routing Analysis

**User request:** "Viết hướng dẫn sử dụng Ansible để quản lý thiết bị mạng Cisco IOS"

AI agent đọc `config/routing-signals.yaml` → phân tích keywords:

| Keyword | Matches skill | Boost |
|---------|--------------|-------|
| "hướng dẫn" / "guide" | `project-doc-writer` | +0.1 |
| "step-by-step" | `project-doc-writer` | +0.1 |
| "network" | `ops-runbook-writer` | +0.1 |
| "troubleshooting" | `ops-runbook-writer` | +0.1 |

**Confidence scores:**

- `project-doc-writer`: 0.5 base + 0.2 = **0.7** (dưới ngưỡng auto-select 0.8)
- `ops-runbook-writer`: 0.5 base + 0.2 = **0.7** (dưới ngưỡng auto-select 0.8)

**Result:** Hai skills cùng match → kiểm tra `composition_rules` trong routing-signals.yaml:

!!! success "Composition Rule Applied: \"How-to with commands\""
    **Signals:** `project-doc-writer` + `ops-runbook-writer`
    **When:** Request là how-to guide nhưng có network/server commands
    **Result:**
    - Primary: `project-doc-writer` → structure T3 (Prerequisites → Steps → Verify)
    - Secondary Iron Law: `ops-runbook-writer` → "Every command MUST be copy-paste ready + expected output"

!!! tip "Tại sao dùng composition rule?"
    Nếu chỉ dùng `project-doc-writer`, các commands có thể thiếu expected output.
    Nếu chỉ dùng `ops-runbook-writer`, doc sẽ có dạng SOP/runbook thay vì how-to guide.
    Composition rule kết hợp: structure từ project-doc + command quality từ ops-runbook Iron Law.

### 0.2: Phase 0 Interview

AI agent chạy interview trước khi generate theo `prompts/interview-before-create.md`:

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
| Prerequisites | Required | ✅ INCLUDE | Critical — setup validation |
| Steps | Required | ✅ INCLUDE | 6 steps chính |
| Verify | Required | ✅ INCLUDE | Trong mỗi step có verify block |
| Troubleshooting | Recommended | ✅ INCLUDE | 4 lỗi phổ biến thực tế |
| Rollback | Optional | ⏭️ SKIP | Không có rollback cho cài đặt Ansible |
| Security Notes | Optional | ✅ INCLUDE | Vault là phần thiết yếu của flow |
| FAQ | Optional | ⏭️ SKIP | Troubleshooting đủ chi tiết rồi |
| Next Steps | Optional | ✅ INCLUDE | Hướng dẫn tiếp tục sau khi setup xong |

---

## Step 1: Chọn Skill + Template

### AI Agent đã làm gì?

Smart Routing từ Phase 0 đã tự động xác định:

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
    **Tự động** từ composition rule — không cần manual decision.

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
PASS 5.5/6 ansible-network-howto.md [structure:1 | commands:1 | prerequisites:1 | metadata:1 | visual_uiux:1 | freshness:0.5]
```

| Criterion | Score | Lý do |
|-----------|-------|-------|
| structure | 1 | YAML frontmatter đầy đủ (+ skill/template/routing fields mới) |
| commands | 1 | Copy-paste commands + expected output (ops-runbook Iron Law) |
| prerequisites | 1 | Prerequisites section rõ ràng với task list |
| metadata | 1 | YAML đầy đủ: title, description, author, status, tags, skill, template |
| visual_uiux | 1 | Admonitions + task lists + mermaid diagram |
| freshness | 0.5 | File mới tạo hôm nay |

### 4.3: Security Scan (NEW in v5.0.0)

```bash
make security-scan
```

**Expected result:**

```text
Scanning: demo-site/docs/guides/how-to/ansible-network-howto.md
PASS: No hardcoded IPs, credentials, or tokens found
File uses safe patterns: 10.0.x.x (example range), vault variables, placeholders
```

!!! success "Result"
    Lint: 0 errors | Score: >= 4/6 PASS | Security: PASS

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
git commit -m "docs(guides): add Ansible network automation how-to (T3, v5.0.0 workflow)"
git push
```

!!! success "Result"
    Doc live trên MkDocs site, accessible qua navigation

---

## Tổng kết: Workflow v5.0.0 trong thực tế

```text
Phase 0  ROUTING     → routing-signals.yaml → composition rule    (~1 phút)
Phase 0  INTERVIEW   → Layer 1+2 questions → context gathered     (~3 phút)
Phase 0  SECTIONS    → T3 tier decision table                     (~1 phút)
Step 1   CHỌN        → Auto từ composition rule + cross-check     (~1 phút)
Step 2   PROMPT      → prompts/create-howto.md → customize        (~2 phút)
Step 3   AI BUILD    → AI đọc skill + template → generate doc     (~5 phút)
Step 4   VERIFY      → lint + score + security scan               (~3 phút)
Step 5   PUBLISH     → mkdocs.yml + make serve + commit           (~3 phút)
                                                         Total: ~19 phút
```

### So sánh: v5.0.0 vs v4.0.0 vs Manual

| Metric | v5.0.0 AI Agent | v4.0.0 AI Agent | Manual (v3.x) |
|--------|-----------------|-----------------|----------------|
| **Thời gian** | ~19 phút | ~15 phút | ~60-90 phút |
| **Skill selection** | Auto (composition rule) | Manual | Manual |
| **Context quality** | High (interview Layer 1+2) | Basic | Biến thiên |
| **Section control** | Explicit tier decision | Không có | Không có |
| **Security check** | Có (Step 4.3) | Không | Không |
| **Consistency** | Rất cao | Cao | Thấp |
| **Quality score** | 5-6/6 | 4-5/6 | 3-4/6 |

### Lessons Learned

1. **AI over-generates** — có thể thêm sections không thuộc template. Luôn review vs tier decision table từ Phase 0
2. **Composition rule tự động** — không cần manual decision, routing-signals.yaml xử lý
3. **Interview context = output tốt hơn** — "Cisco IOS + Ubuntu + Ansible 2.16+" cho output cụ thể hơn "network automation"
4. **Tier decision trước** — quyết định optional sections trước khi generate → ít phải xóa sau
5. **Security scan là bước bắt buộc** — đặc biệt với docs có IP, credentials, tokens
6. **mkdocs.yml là bước dễ quên nhất** — cần checklist reminder hoặc automation
7. **Layer 3 interview** — bỏ qua được cho how-to guide đơn giản, cần cho runbook phức tạp hoặc security policy
