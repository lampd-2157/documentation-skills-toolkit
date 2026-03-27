# Getting Started Guide — Documentation Skills Toolkit

> Hướng dẫn chi tiết cho team member lần đầu sử dụng bộ toolkit. Đọc guide này trong ~15 phút, bạn sẽ hiểu toolkit hoạt động thế nào và viết được doc đầu tiên.

---

## 1. Toolkit này là gì?

Documentation Skills Toolkit là **bộ công cụ chuẩn hóa cách viết technical documentation** cho team. Thay vì mỗi người viết docs theo cách riêng, toolkit cung cấp:

- **Skills** — Bộ quy tắc hướng dẫn cách viết từng loại doc (runbook, guide, training...)
- **Templates** — File mẫu copy-paste, chỉ cần điền nội dung
- **Tools** — CLI tạo doc tự động, lint kiểm tra format, validator kiểm tra cấu trúc
- **Pipeline** — Quy trình Docs-as-Code: Write → Lint → Review → Publish → Audit

### Tại sao cần toolkit?

```text
TRƯỚC (không có toolkit):
  - Docs rải rác trên Wiki, Drive, Confluence
  - Format không thống nhất, mỗi người viết 1 kiểu
  - Runbook chỉ có text mô tả, không chạy được
  - Docs cũ 6 tháng không ai update
  - Người mới vào team không biết docs ở đâu

SAU (có toolkit):
  - Docs tập trung trong Git repo, quản lý như code
  - Format thống nhất nhờ markdownlint tự động kiểm tra
  - Runbook có commands copy-paste + expected output
  - Quarterly audit phát hiện docs cũ
  - MkDocs site searchable, navigable, auto-deploy
```

---

## 2. Concept chính

### Skills = "Cách viết"

Mỗi skill là một file `.md` chứa bộ quy tắc cho 1 loại documentation:

| Skill | Viết cái gì | File |
|-------|-------------|------|
| **Docs Engineer** | Setup MkDocs, chuẩn Markdown, cấu trúc thư mục | `skills/docs-engineer.md` |
| **Ops Runbook Writer** | Runbook vận hành, network docs, incident docs | `skills/ops-runbook-writer.md` |
| **Training Doc Writer** | Training, onboarding, curriculum, learning path | `skills/training-doc-writer.md` |
| **Project Doc Writer** | ADR, tech spec, how-to guide, quick reference | `skills/project-doc-writer.md` |
| **Infra Security Doc** | Security policy, RBAC, audit log, vulnerability | `skills/infra-security-doc.md` |

Mỗi skill có cấu trúc giống nhau:

```text
Skill
├── Context          — Mô tả scope, khi nào dùng
├── Iron Law         — 1 quy tắc KHÔNG BAO GIỜ vi phạm
├── Guardrails       — Checklist kiểm tra TRƯỚC khi viết
├── Decision Tree    — Flowchart chọn đúng skill
├── Content          — Hướng dẫn chi tiết + ví dụ good/bad
├── Red Flags        — Dấu hiệu cần DỪNG LẠI
├── Remember         — Bảng tóm tắt rules nhanh
└── Related Skills   — Link tới skills liên quan
```

**Bạn không cần đọc hết skill.** Chỉ cần đọc **Iron Law** (1 câu) và **Guardrails** (3-5 checkboxes) là đủ để bắt đầu.

### Templates = "File mẫu"

11 templates (T1-T11) là file mẫu copy-paste sẵn. Mỗi template map tới 1 use case:

| Khi bạn cần... | Dùng template | CLI command |
|----------------|--------------|-------------|
| Viết SOP vận hành server/service | T1 Runbook | `docs-toolkit new runbook "Tên"` |
| Ghi nhận quyết định architecture | T2 ADR | `docs-toolkit new adr "Tên"` |
| Hướng dẫn step-by-step | T3 How-to Guide | `docs-toolkit new howto "Tên"` |
| Tạo module training nội bộ | T4 Training | `docs-toolkit new training "Tên"` |
| Document hạ tầng mạng | T5 Network | `docs-toolkit new network "Tên"` |
| Phân tích sau sự cố | T6 Postmortem | `docs-toolkit new postmortem "Tên"` |
| Lên kế hoạch bảo trì | T7 Maintenance | `docs-toolkit new maintenance "Tên"` |
| Tóm tắt version release | T8 Release Notes | `docs-toolkit new release-notes "vX.Y"` |
| Complex architecture decision | T9 ADR (MADR) | `docs-toolkit new adr-madr "Decision"` |
| Quick decision, POC | T10 ADR (Lightweight) | Copy `templates/adr-lightweight.md` |
| Kiểm tra kiến thức | T11 Knowledge Check | `docs-toolkit new knowledge-check "Topic"` |

### Pipeline = "Quy trình"

Docs-as-Code = quản lý docs giống source code:

```text
Write → Lint → Review → Publish → Audit
  │       │       │        │        │
  │       │       │        │        └─ Mỗi quý: tìm docs cũ > 90 ngày
  │       │       │        └─ mkdocs gh-deploy (GitHub Pages)
  │       │       └─ Pull Request + peer review
  │       └─ markdownlint + cspell tự động (pre-commit hook)
  └─ Chọn skill → copy template → viết nội dung
```

---

## 3. Setup (lần đầu)

### Prerequisites

Trước khi bắt đầu, đảm bảo đã cài:

| Tool | Kiểm tra | Cài đặt (Ubuntu/WSL) | Cài đặt (macOS) |
|------|----------|----------------------|------------------|
| **Python 3.8+** | `python3 --version` | `sudo apt update && sudo apt install python3 python3-pip` | `brew install python3` |
| **Node.js 18+** | `node --version` | [nvm](https://github.com/nvm-sh/nvm) hoặc `sudo apt install nodejs npm` | `brew install node` |
| **Git** | `git --version` | `sudo apt install git` | `brew install git` |
| **VS Code** *(optional)* | `code --version` | Cài trên Windows → mở VS Code → `Ctrl+Shift+P` → "Install code command in PATH" | `brew install --cask visual-studio-code` |

> **Ubuntu/Debian:** Luôn chạy `sudo apt update` trước khi cài đặt packages để đảm bảo package index mới nhất.

### Bước 1: Clone và cài đặt

```bash
git clone https://github.com/lampd-2157/documentation-skills-toolkit.git
cd documentation-skills-toolkit
bash scripts/setup.sh
```

Script sẽ tự động cài:

- MkDocs + Material theme + plugins
- markdownlint-cli2 (lint markdown)
- Pre-commit hooks (tự lint khi commit)
- VS Code snippets (gõ `doc-` → autocomplete)
- cspell + link-check configs

### Bước 2: Xem demo site

```bash
pip install -r demo-site/requirements.txt
make serve
# Mở http://localhost:8000
```

Demo site có ví dụ thực tế cho các templates — xem để biết output mong đợi.

### Bước 3: Áp dụng vào dự án của bạn

```bash
# Trong dự án của bạn
cd /path/to/your-project

# Copy configs
cp /path/to/toolkit/examples/mkdocs-starter.yml mkdocs.yml
cp /path/to/toolkit/config/.markdownlint.json .markdownlint.json
cp /path/to/toolkit/config/pre-commit.yaml .pre-commit-config.yaml

# Setup
pip install -r /path/to/toolkit/config/requirements.txt
pre-commit install

# Tạo cấu trúc docs
mkdir -p docs/{getting-started,operations/runbooks,development/adr,guides/how-to,training,assets/images}
echo "# Project Documentation" > docs/index.md

# Verify
mkdocs serve
```

---

## 4. Viết doc đầu tiên

### Ví dụ: Viết runbook cho Nginx

**Bước 1:** Tạo file từ template

```bash
./scripts/docs-toolkit new runbook "Nginx Load Balancer"
# → Created: docs/operations/runbooks/nginx-load-balancer-runbook.md
```

**Bước 2:** Mở skill để biết quy tắc

Mở `skills/ops-runbook-writer.md`, đọc:

- **Iron Law:** "Every runbook MUST have copy-paste commands AND expected output"
- **Guardrails:** Test commands, contact info up-to-date, severity defined, backup procedure

**Bước 3:** Điền nội dung

Mở file vừa tạo, điền các placeholder `[...]`. Quan trọng nhất:

```markdown
## Health Checks
| Check        | Command                          | Expected       |
| ------------ | -------------------------------- | -------------- |
| Nginx alive  | `curl -s localhost/health`       | `200 OK`       |
| Config valid | `sudo nginx -t`                 | `syntax is ok` |

## Troubleshooting
### 502 Bad Gateway
**Symptoms:** Browser hiển thị 502
**Root Cause:** Backend server down
**Fix:**
1. `sudo systemctl status myapp` — check backend
2. `sudo systemctl restart myapp` — restart nếu inactive
3. `curl -s localhost:8080/health` — verify backend up
**Prevention:** Setup health check monitoring
```

**Bước 4:** Verify

```bash
# Lint
npx markdownlint-cli2 docs/operations/runbooks/nginx-load-balancer-runbook.md

# Preview
make serve
# → Mở localhost:8000, navigate tới runbook, kiểm tra render
```

**Bước 5:** Commit & PR

```bash
git add docs/operations/runbooks/nginx-load-balancer-runbook.md
git commit -m "docs: add Nginx LB runbook"
git push && gh pr create
```

---

## 5. Chọn đúng skill / template

### Flowchart

```text
Bạn cần viết gì?
  │
  ├── Liên quan đến VẬN HÀNH hệ thống?
  │     ├── SOP / runbook cho service?           → T1 Runbook
  │     ├── Document network / server?           → T5 Network Topology
  │     ├── Phân tích incident đã xảy ra?        → T6 Postmortem
  │     └── Lên kế hoạch bảo trì / upgrade?     → T7 Maintenance Window
  │
  ├── Liên quan đến HƯỚNG DẪN / ĐÀO TẠO?
  │     ├── Step-by-step cho 1 task cụ thể?      → T3 How-to Guide
  │     ├── Module training cho team?             → T4 Training Module
  │     └── Cheat sheet / quick reference?       → project-doc-writer §3
  │
  ├── Liên quan đến DỰ ÁN / KIẾN TRÚC?
  │     ├── Ghi nhận quyết định architecture?    → T2 ADR
  │     ├── Technical specification?              → project-doc-writer §1.2
  │     └── Release notes cho version mới?        → T8 Release Notes
  │
  └── Không biết chọn gì?
        └── Xem docs/skill-composition-recipes.md
```

### Ví dụ thực tế

| Scenario | Template | Skill |
|----------|----------|-------|
| "Setup monitoring cho production cluster" | T1 Runbook | ops-runbook-writer |
| "Tại sao team chọn PostgreSQL thay MongoDB" | T2 ADR | project-doc-writer |
| "Hướng dẫn member mới setup dev environment" | T3 How-to | project-doc-writer |
| "Training Git workflow cho intern" | T4 Training | training-doc-writer |
| "Document VLAN layout office mới" | T5 Network | ops-runbook-writer |
| "DB crash hôm qua, cần postmortem" | T6 Postmortem | ops-runbook-writer |
| "Upgrade PostgreSQL cuối tuần này" | T7 Maintenance | ops-runbook-writer |
| "Release v3.0 cần release notes" | T8 Release Notes | project-doc-writer |

---

## 6. Workflow hàng ngày

### Viết doc mới

```bash
# 1. Tạo từ template
./scripts/docs-toolkit new <type> "<title>"

# 2. Viết nội dung (theo skill guidelines)

# 3. Lint trước khi commit
npx markdownlint-cli2 path/to/your-doc.md

# 4. Preview
make serve

# 5. Commit + PR
git add path/to/your-doc.md
git commit -m "docs: add <description>"
```

### Review doc của người khác

Dùng [Quality Scorecard](doc-quality-scorecard.md) — chấm 10 tiêu chí, mỗi tiêu chí 0-1:

1. Structure — đúng template?
2. Commands testable — copy-paste chạy được?
3. Prerequisites — list đầy đủ?
4. Expected results — mỗi step có expected output?
5. Visual aids — có diagram?
6. Metadata — có YAML header?
7. Markdown quality — lint pass?
8. Freshness — updated gần đây?
9. Audience — target audience rõ ràng?
10. Non-author tested — người khác đọc hiểu?

**Score >= 7** → approve. **Score < 7** → request changes.

### Quarterly audit

```bash
# Tìm docs cũ hơn 90 ngày
find docs/ -name "*.md" -mtime +90 -type f | sort

# Tìm docs vẫn còn draft
grep -rl "status: draft" docs/ | sort
```

---

## 7. VS Code Tips

Sau khi chạy `setup.sh`, gõ `doc-` trong VS Code sẽ hiện autocomplete cho 9 snippets:

| Prefix | Snippet |
|--------|---------|
| `doc-header` | YAML metadata header |
| `doc-runbook` | T1 Runbook skeleton |
| `doc-adr` | T2 ADR skeleton |
| `doc-howto` | T3 How-to Guide skeleton |
| `doc-training` | T4 Training Module skeleton |
| `doc-network` | T5 Network Topology skeleton |
| `doc-postmortem` | T6 Postmortem skeleton |
| `doc-maintenance` | T7 Maintenance Window skeleton |
| `doc-release` | T8 Release Notes skeleton |

---

## 8. FAQ

### "Tôi chỉ cần viết 1 doc đơn giản, có cần dùng toolkit không?"

Có. Ngay cả doc đơn giản cũng nên có YAML header + markdown lint. Dùng CLI tạo trong 5 giây: `docs-toolkit new howto "Task name"` — nhanh hơn viết từ đầu.

### "Skill file dài quá, đọc hết mất thời gian"

Không cần đọc hết. Chỉ cần đọc:

1. **Iron Law** (1 câu) — quy tắc quan trọng nhất
2. **Guardrails** (3-5 checkboxes) — verify trước khi viết
3. **Remember** (bảng cuối) — quick reference

### "Tôi muốn viết loại doc mà không có template"

Dùng template gần nhất rồi customize. Hoặc tạo skill mới:

1. Copy `skills/skill-template.md`
2. Điền 6 sections bắt buộc
3. Submit PR (xem `CONTRIBUTING.md`)

### "Docs-as-Code nghe phức tạp, team tôi chưa quen Git"

Bắt đầu từ Level 2 (xem Maturity Model trong [Lifecycle Guide](docs-lifecycle.md)):

1. Docs trong Git repo (commit + push)
2. Dùng markdownlint (tự chạy qua pre-commit hook)
3. Sau đó mới thêm PR review, CI/CD, quarterly audit

### "Toolkit này dùng cho AI agent được không?"

Có. Skills được thiết kế để cả human và AI agent đọc hiểu:

- Context table → agent biết scope
- Iron Law → agent biết constraint tuyệt đối
- Decision tree → agent biết khi nào activate skill
- Guardrails → agent verify trước khi bắt đầu

---

## 9. Tóm tắt

```text
Cần viết doc?
  → Chọn template (T1-T11)
  → Tạo bằng CLI: docs-toolkit new <type> "<title>"
  → Đọc Iron Law + Guardrails của skill tương ứng
  → Viết nội dung, điền placeholders
  → Lint: markdownlint + cspell
  → Preview: make serve
  → Commit + PR
  → Done!
```

**3 files cần nhớ:**

| File | Mục đích |
|------|----------|
| `skills/` | Đọc khi cần biết **cách viết đúng** |
| `templates/` | Đọc khi cần **file mẫu copy-paste** |
| `scripts/docs-toolkit` | Dùng khi cần **tạo doc mới nhanh** |

---

> **Version:** 3.0.0 | **Cập nhật:** 2026-03-27
