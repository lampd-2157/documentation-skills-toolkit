# Documentation Skills Toolkit

![Version](https://img.shields.io/badge/version-2.2.0-blue)
![Skills](https://img.shields.io/badge/skills-5-green)
![Templates](https://img.shields.io/badge/templates-8-orange)
![License](https://img.shields.io/badge/license-MIT-brightgreen)

> **Bộ skill chuẩn hóa cho documentation** — dùng được cho mọi dự án, không phụ thuộc vào bất kỳ hệ thống cụ thể nào.

---

## Toolkit này giải quyết vấn đề gì?

| Vấn đề                                    | Toolkit giải quyết                          |
| ----------------------------------------- | ------------------------------------------- |
| Docs rải rác, format không thống nhất     | **5 Skills** chuẩn hóa cách viết mọi loại doc |
| Viết doc từ đầu mất thời gian             | **8 Templates** copy-paste, điền nội dung là xong |
| Không biết viết runbook/guide đúng cách   | Mỗi skill có **Iron Law** + **Guardrails** hướng dẫn |
| Docs cũ, không ai review                  | **Docs-as-Code** pipeline: lint → review → deploy → audit |
| Mỗi người viết 1 kiểu                    | **CLI tool** tự tạo doc đúng format chuẩn    |

## Cách hoạt động (3 bước)

```text
1. CHỌN SKILL        Bạn cần viết gì? → Chọn 1 trong 5 skills hướng dẫn
   ┌──────────────────────────────────────────────────────────┐
   │  docs-engineer        → Setup MkDocs, chuẩn Markdown    │
   │  ops-runbook-writer   → Runbook, network, server docs   │
   │  training-doc-writer  → Training, onboarding, curriculum │
   │  project-doc-writer   → ADR, tech spec, how-to, guide   │
   │  infra-security-doc   → Security policy, RBAC, audit    │
   └──────────────────────────────────────────────────────────┘

2. COPY TEMPLATE      Chọn template phù hợp (T1-T8) → copy → điền nội dung
   Hoặc dùng CLI:  ./scripts/docs-toolkit new runbook "Tên service"

3. VERIFY & PUBLISH   Lint → Review → Deploy
   markdownlint ✅ → PR review ✅ → mkdocs gh-deploy ✅
```

> **Lần đầu dùng?** Đọc [Getting Started Guide](references/guides/getting-started-guide.md) — hướng dẫn chi tiết từ A-Z.

---

## Quick Start

```bash
# Clone repo
git clone https://github.com/lampd-2157/documentation-skills-toolkit.git
cd documentation-skills-toolkit

# One-command setup (MkDocs + markdownlint + pre-commit)
bash references/config/setup.sh

# Tạo doc mới từ template
./scripts/docs-toolkit new runbook "My Service"

# Xem demo site
cd demo-site && pip install -r requirements.txt && mkdocs serve

# Hoặc dùng Makefile
make setup    # One-command setup
make serve    # Start dev server
make all      # lint + validate + build
```

---

## 5 Skills

Mỗi skill là một **bộ quy tắc** hướng dẫn cách viết 1 loại documentation cụ thể. Tất cả skills tuân thủ cùng cấu trúc 6 sections: Context → Iron Law → Guardrails → Red Flags → Remember → Related Skills.

| Skill | Khi nào dùng | Iron Law (quy tắc tối thượng) |
|-------|-------------|-------------------------------|
| [docs-engineer](skills/docs-engineer.md) | Setup MkDocs, chuẩn hóa markdown, chọn plugins | "Every document MUST pass markdownlint AND render correctly in MkDocs" |
| [ops-runbook-writer](skills/ops-runbook-writer.md) | Viết runbook, ops manual, network/server docs | "Every runbook MUST have copy-paste commands AND expected output" |
| [training-doc-writer](skills/training-doc-writer.md) | Viết training, onboarding, curriculum, learning path | "Every training doc MUST have Prerequisites → Steps → Expected Result → Troubleshooting" |
| [project-doc-writer](skills/project-doc-writer.md) | Viết ADR, tech spec, how-to guide, quick reference | "Every project doc MUST have Context → Decision/Steps → Consequences/Result" |
| [infra-security-doc](skills/infra-security-doc.md) | Viết security policy, RBAC, audit log, vulnerability | "Every security doc MUST have Scope → Policy → Enforcement → Audit" |

## 8 Templates (T1-T8)

Copy-paste từ [doc-templates-library.md](references/templates/doc-templates-library.md), hoặc dùng CLI:

| ID  | Template            | CLI command | Use Case |
| --- | ------------------- | ----------- | -------- |
| T1  | Runbook             | `docs-toolkit new runbook "Name"` | Vận hành hệ thống |
| T2  | ADR                 | `docs-toolkit new adr "Decision"` | Ghi nhận architecture decision |
| T3  | How-to Guide        | `docs-toolkit new howto "Task"` | Hướng dẫn step-by-step |
| T4  | Training Module     | `docs-toolkit new training "Topic"` | Training nội bộ |
| T5  | Network Topology    | `docs-toolkit new network "Env"` | Document network infrastructure |
| T6  | Incident Postmortem | `docs-toolkit new postmortem "Title"` | Phân tích sau sự cố |
| T7  | Maintenance Window  | `docs-toolkit new maintenance "Title"` | Kế hoạch bảo trì |
| T8  | Release Notes       | `docs-toolkit new release-notes "vX.Y"` | Tóm tắt version release |

---

## Tooling

| Tool | Command | Mô tả |
|------|---------|-------|
| Scaffold | `./scripts/docs-toolkit new <type> <title>` | Tạo doc mới từ template |
| Validate | `python3 scripts/validate_skill.py` | Kiểm tra cấu trúc skill file |
| Lint | `npx markdownlint-cli2 "**/*.md"` | Kiểm tra markdown format |
| Spell | `npx cspell "**/*.md"` | Kiểm tra chính tả |
| Preview | `mkdocs serve` | Xem trước trên localhost:8000 |
| Build | `mkdocs build --strict` | Build production |

---

## Project Structure

```text
documentation-skills-toolkit/
├── .github/workflows/              # CI/CD
│   └── docs-ci.yml                # Lint + validate + build
├── skills/                         # 5 skills + 1 template
│   ├── docs-engineer.md            # Skill 1: MkDocs & Markdown
│   ├── ops-runbook-writer.md       # Skill 2: Runbook & operations
│   ├── training-doc-writer.md      # Skill 3: Training & onboarding
│   ├── project-doc-writer.md       # Skill 4: ADR, spec, guide
│   ├── infra-security-doc.md       # Skill 5: Security & compliance
│   └── skill-template.md           # Template tạo skill mới
├── evals/                          # Eval test suite cho mỗi skill
│   ├── evals.json                  # Test prompts tổng hợp
│   ├── docs-engineer/
│   ├── ops-runbook-writer/
│   ├── training-doc-writer/
│   └── project-doc-writer/
├── references/
│   ├── config/                     # Configs (setup.sh, markdownlint, cspell...)
│   ├── guides/                     # Hướng dẫn chi tiết
│   └── templates/                  # 8 doc templates (T1-T8)
├── scripts/                        # CLI tools
├── demo-site/                      # MkDocs demo site (all 8 examples)
├── Makefile                        # make serve/lint/validate/build
├── CHANGELOG.md                    # Version history
├── CONTRIBUTING.md                 # Hướng dẫn đóng góp
└── LICENSE                         # MIT
```

---

## Tài liệu & Hướng dẫn

| Doc | Mô tả | Đọc khi... |
|-----|-------|-------------|
| [Getting Started Guide](references/guides/getting-started-guide.md) | Hướng dẫn từ A-Z cho người mới | Lần đầu dùng toolkit |
| [Lifecycle Guide](references/guides/docs-lifecycle-guide.md) | Write → Lint → Review → Publish → Audit | Setup Docs-as-Code pipeline |
| [Composition Recipes](references/guides/skill-composition-recipes.md) | Kết hợp skills cho task thực tế | Không biết dùng skill nào |
| [Quality Scorecard](references/guides/doc-quality-scorecard.md) | Chấm điểm chất lượng doc (0-10) | Review / audit docs |
| [Anti-Patterns](references/guides/doc-anti-patterns.md) | 10 lỗi documentation phổ biến | Tránh sai lầm khi viết |
| [Plugin Catalog](references/guides/mkdocs-plugins-catalog.md) | MkDocs plugins chọn lọc | Mở rộng MkDocs site |
| [Infra Knowledge Base](references/guides/infra-knowledge-base.md) | Cấu trúc docs cho team infra | Team infra/ops mới bắt đầu |
| [Contributing](CONTRIBUTING.md) | Cách đóng góp skills & templates | Muốn thêm skill/template mới |

---

## License

MIT — [LICENSE](LICENSE)

> **Created by [DulapReal](https://github.com/lampd-2157)** — Infrastructure & Automation Engineer
>
> Version 2.2.0 | 2026-03-27
