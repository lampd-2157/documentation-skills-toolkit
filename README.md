# 📝 Documentation Skills Toolkit

![Version](https://img.shields.io/badge/version-1.1.0-blue)
![Skills](https://img.shields.io/badge/skills-3-green)
![Templates](https://img.shields.io/badge/templates-8-orange)
![License](https://img.shields.io/badge/license-MIT-brightgreen)
![MkDocs](https://img.shields.io/badge/MkDocs-Material-blue?logo=markdown)
![Lint](https://img.shields.io/badge/markdownlint-configured-brightgreen)

> **Bộ skill chuẩn hóa cho documentation** — dùng được cho mọi dự án, không phụ thuộc vào bất kỳ hệ thống cụ thể nào.

---

## 🎯 Mục đích

Bộ toolkit này cung cấp các **skill templates** để tạo tài liệu chất lượng cao, bao gồm:

- **Nền tảng kỹ thuật** (MkDocs platform + Markdown standards)
- **Tài liệu vận hành** (Runbook, ops manual, network/server docs)
- **Tài liệu đào tạo** (Training, guides, project development docs)

Mỗi skill tuân thủ cấu trúc chuẩn **6 sections bắt buộc** (Context → Iron Law → Guardrails → Red Flags → Remember → Related Skills) để đảm bảo tính nhất quán và dễ maintain.

---

## 📂 Cấu trúc thư mục

```text
templates/
├── README.md                       # ← Bạn đang đọc file này
├── CONTRIBUTING.md                 # Hướng dẫn đóng góp
├── skill-template.md               # Template gốc — cấu trúc 6 sections
├── docs-engineer.md                # Skill 1: MkDocs platform & chuẩn Markdown
├── ops-runbook-writer.md           # Skill 2: Runbook & operations docs
├── training-guide-writer.md        # Skill 3: Training & guide docs
├── references/                     # Tài liệu tham chiếu & configs
│   ├── mkdocs-plugins-catalog.md   # 20 plugins chọn lọc
│   ├── doc-templates-library.md    # 8 templates copy-paste (T1-T8)
│   ├── infra-knowledge-base.md     # Starter structure cho team infra
│   ├── docs-lifecycle-guide.md     # Docs-as-Code lifecycle guide
│   ├── requirements.txt            # Python dependencies (pinned)
│   ├── setup.sh                    # One-command setup script
│   ├── mkdocs-starter.yml          # Config mkdocs.yml sẵn sàng dùng
│   ├── markdownlint-config.json    # Cấu hình markdownlint chuẩn
│   ├── github-actions-docs.yml     # CI/CD pipeline (Lint → Build → Deploy)
│   ├── pre-commit-config.yaml      # Pre-commit hooks
│   └── docs.code-snippets          # VS Code snippets (9 templates)
└── demo-site/                      # ⭐ Demo MkDocs site
    ├── mkdocs.yml + requirements.txt
    └── docs/                       # Example docs (Proxmox, GWS, ADR)
```

---

## 🗺 Skill Map — Chọn skill nào?

```text
Bạn cần làm gì?
  ├── Setup MkDocs project / chuẩn hóa Markdown?
  │     └── 📐 docs-engineer.md
  │
  ├── Viết runbook / ops manual / network docs?
  │     └── 🔧 ops-runbook-writer.md
  │
  ├── Viết training / guide / ADR / tech spec?
  │     └── 📚 training-guide-writer.md
  │
  └── Cần template copy-paste nhanh?
        └── 📋 references/doc-templates-library.md
```

| Loại tài liệu                                | Skill                      | Templates liên quan                                           |
| -------------------------------------------- | -------------------------- | ------------------------------------------------------------- |
| MkDocs setup, folder structure, markdownlint | `docs-engineer.md`         | `mkdocs-starter.yml`, `markdownlint-config.json`              |
| Runbook, SOP, server/network docs, incident  | `ops-runbook-writer.md`    | T1 (Runbook), T5 (Network), T6 (Postmortem), T7 (Maintenance) |
| Training, onboarding, how-to guide, ADR      | `training-guide-writer.md` | T2 (ADR), T3 (How-to), T4 (Training), T8 (Release Notes)      |

---

## 🚀 Quick Start — Áp dụng cho dự án mới

### Option A: One-command setup (khuyến nghị)

```bash
# Copy toolkit → chạy setup script
cp -r skills/templates/ /path/to/new-project/docs-skills/
cd /path/to/new-project
bash docs-skills/references/setup.sh
```

### Option B: Setup từng bước

#### Bước 1: Copy bộ skills vào dự án

```bash
cp -r skills/templates/ /path/to/new-project/docs-skills/
```

#### Bước 2: Install dependencies

```bash
# Copy configs
cp references/mkdocs-starter.yml mkdocs.yml
cp references/markdownlint-config.json .markdownlint.json

# Install Python + Node packages
pip install -r references/requirements.txt
npm install -g markdownlint-cli2
```

#### Bước 3: Setup VS Code snippets

```bash
mkdir -p .vscode
cp references/docs.code-snippets .vscode/
# Giờ gõ doc- trong VS Code → auto-complete 9 templates
```

#### Bước 4: Setup pre-commit hooks

```bash
cp references/pre-commit-config.yaml .pre-commit-config.yaml
pip install pre-commit && pre-commit install
# Mỗi git commit sẽ tự lint markdown
```

#### Bước 5: Verify

```bash
mkdocs serve    # Preview tại http://localhost:8000
```

### Bắt đầu viết docs

1. Chọn skill phù hợp từ **Skill Map** ở trên
2. Đọc **Iron Law** và **Guardrails** của skill đó
3. Chọn template từ `references/doc-templates-library.md`
4. Copy template → customize → verify với checklist

---

## 📋 8 Document Templates (Copy-Paste Ready)

Tất cả templates nằm trong `references/doc-templates-library.md`:

| ID     | Template            | Dùng khi...                               |
| ------ | ------------------- | ----------------------------------------- |
| **T1** | Runbook             | Viết SOP vận hành hệ thống cụ thể         |
| **T2** | ADR                 | Ghi nhận architecture decision            |
| **T3** | How-to Guide        | Hướng dẫn step-by-step cho task cụ thể    |
| **T4** | Training Module     | Tạo khóa training nội bộ                  |
| **T5** | Network Topology    | Document VLAN, firewall, server inventory |
| **T6** | Incident Postmortem | Phân tích sau sự cố (post-incident)       |
| **T7** | Maintenance Window  | Kế hoạch bảo trì hệ thống                 |
| **T8** | Release Notes       | Tóm tắt version release                   |

---

## ✅ Best Practices Checklist

Trước khi share docs cho team hoặc publish:

- [ ] **Lint passed** — `markdownlint` 0 errors
- [ ] **Build passed** — `mkdocs build` 0 warnings
- [ ] **Structure** — Heading hierarchy H1→H2→H3 (không skip)
- [ ] **Metadata** — Mọi doc có YAML header (title, status, updated)
- [ ] **File naming** — kebab-case lowercase: `my-document.md`
- [ ] **Commands testable** — Runbook commands copy-paste chạy được
- [ ] **Expected output** — Mọi step có expected result
- [ ] **Diagrams** — Mermaid render đúng (test local)
- [ ] **Links valid** — Tất cả internal/external links hoạt động
- [ ] **Non-author test** — Ít nhất 1 người khác đọc hiểu

---

## 🔧 Customize cho dự án của bạn

### Agent field

Trong mỗi skill, thay `[Documentation Agent]` bằng agent/role trong dự án:

```diff
- **Agent:** 📝 [Documentation Agent]
+ **Agent:** 📝 DevOps Team
```

### Thêm skill mới

1. Copy `skill-template.md` → đặt tên mới
2. Đảm bảo có đủ **6 sections bắt buộc**:
   - Context / Bối cảnh
   - ⛔ THE IRON LAW
   - 🛡 Guardrails
   - 🚩 Red Flags — STOP
   - Remember
   - 🔗 Related Skills
3. Cập nhật README.md (file này) — thêm vào Skill Map

---

## 📚 Nguồn tham khảo

| Source                                                                                    | Tích hợp vào                             |
| ----------------------------------------------------------------------------------------- | ---------------------------------------- |
| [squidfunk/mkdocs-material](https://github.com/squidfunk/mkdocs-material)                 | `docs-engineer.md` — theme, components   |
| [DavidAnson/markdownlint](https://github.com/DavidAnson/markdownlint)                     | `docs-engineer.md` — lint rules          |
| [Google Developer Style Guide](https://developers.google.com/style)                       | Writing tone, guide structure            |
| [SkeltonThatcher/run-book-template](https://github.com/SkeltonThatcher/run-book-template) | `ops-runbook-writer.md` — runbook format |
| [runbear-io/awesome-runbook](https://github.com/runbear-io/awesome-runbook)               | Ops best practices                       |
| [mkdocs/catalog](https://github.com/mkdocs/catalog)                                       | Plugin selection                         |
| [gitlab.com/tgdp/templates](https://gitlab.com/tgdp/templates)                            | Template patterns                        |

---

## 📚 See Also — Tài liệu bổ sung

| File                                 | Mô tả                                                              |
| ------------------------------------ | ------------------------------------------------------------------ |
| `references/infra-knowledge-base.md` | Starter folder structure cho team infra (network, Proxmox, GWS...) |
| `references/docs-lifecycle-guide.md` | Docs-as-Code lifecycle: Write → Lint → Review → Publish → Audit    |
| `references/github-actions-docs.yml` | CI/CD pipeline: Lint → Build → Deploy to GitHub Pages              |
| `references/pre-commit-config.yaml`  | Pre-commit hooks: auto-lint Markdown before commit                 |
| `references/docs.code-snippets`      | VS Code snippets — copy vào `.vscode/` → gõ `doc-`                 |
| `references/setup.sh`                | One-command setup script (install all tools)                       |
| `references/requirements.txt`        | Python dependencies (pinned versions)                              |
| `demo-site/`                         | Demo MkDocs site — `cd demo-site && mkdocs serve`                  |

---

## 📄 License

MIT — Tự do sử dụng, sửa đổi, và chia sẻ. Xem [LICENSE](LICENSE).

## ✍️ Author & Credits

> **Created by [DulapReal](https://github.com/lampd-2157)** — Infrastructure & Automation Engineer
>
> Built with ❤️ for the infra/ops community. Contributions welcome!

---

> **Version:** 1.1.1 | **Created by:** DulapReal | **Cập nhật:** 2026-03-26
