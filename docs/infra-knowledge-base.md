# Infrastructure Knowledge Base — Starter Structure

> Template cấu trúc knowledge base cho team vận hành hạ tầng đa mảng.
>
> **Dùng khi:** Team quản lý nhiều hệ thống (network, server, cloud, SaaS) và cần chuẩn hóa cách tổ chức tài liệu.

---

## 📁 Folder Structure

Copy cấu trúc này vào `docs/` của dự án, giữ hoặc bỏ mảng nào tùy team:

```text
docs/
├── index.md                              # Landing page
│
├── network/                              # 🌐 Hạ tầng mạng
│   ├── index.md                          # Tổng quan network
│   ├── topology.md                       # VLAN, subnet, diagrams (T5)
│   ├── vpn-runbook.md                    # VPN management (T1)
│   ├── dns-guide.md                      # DNS records management (T3)
│   └── firewall-rules.md                 # Firewall policies (T5)
│
├── proxmox/                              # 🖥 Server & VM (Proxmox)
│   ├── index.md                          # Tổng quan Proxmox cluster
│   ├── vm-lifecycle-runbook.md           # Create/clone/migrate VM (T1)
│   ├── backup-restore-runbook.md         # Backup schedule + restore (T1)
│   ├── maintenance-window.md             # Proxmox updates (T7)
│   └── troubleshoot.md                   # Common Proxmox issues (T1)
│
├── google-workspace/                     # 📧 Google Workspace
│   ├── index.md                          # Tổng quan GWS
│   ├── user-management.md               # Tạo/xóa/suspend user (T3)
│   ├── groups-policies.md               # Group + OU management (T3)
│   └── security-2fa.md                  # 2FA enforcement guide (T3)
│
├── automation/                           # ⚡ Automation (n8n / IPortal)
│   ├── index.md                          # Tổng quan automation stack
│   ├── workflow-runbook.md               # Deploy/rollback n8n (T1)
│   └── slack-integration.md             # Slack bot management (T3)
│
├── github/                               # 🐙 GitHub
│   ├── index.md                          # Tổng quan GitHub org
│   ├── repo-management.md               # Repo policies, branch rules (T3)
│   └── ci-cd-guide.md                   # GitHub Actions + CI/CD (T3)
│
├── incidents/                            # 🚨 Incident Management
│   ├── index.md                          # Incident response process
│   ├── severity-matrix.md               # P1-P4 definitions
│   └── postmortem/                      # Archive (T6)
│       └── YYYY-MM-DD-incident-title.md
│
└── assets/                               # 🖼 Shared assets
    ├── images/
    └── diagrams/
```

---

## 📄 Index Page Template

Mỗi mảng có 1 `index.md` theo format chuẩn:

```markdown
# [Domain Name]

## Tổng quan

| Field          | Value                  |
| -------------- | ---------------------- |
| **Owner**      | [team/person]          |
| **Services**   | [danh sách services]   |
| **Monitoring** | [tool + dashboard URL] |
| **On-call**    | [rotation schedule]    |
| **SLA**        | [uptime target]        |

## System Inventory

| System   | IP/Hostname | Role   | Status |
| -------- | ----------- | ------ | ------ |
| [system] | [ip]        | [role] | Active |

## Runbooks

| Doc                      | Mô tả        | Last Updated |
| ------------------------ | ------------ | ------------ |
| [runbook.md](runbook.md) | [mô tả ngắn] | YYYY-MM-DD   |

## Guides

| Doc                  | Mô tả        | Audience |
| -------------------- | ------------ | -------- |
| [guide.md](guide.md) | [mô tả ngắn] | [who]    |

## Recent Changes

| Date       | Change         | Author |
| ---------- | -------------- | ------ |
| YYYY-MM-DD | [what changed] | [who]  |
```

---

## 🏷 Naming Convention

| Rule         | Convention              | Ví dụ                     |
| ------------ | ----------------------- | ------------------------- |
| Folder name  | kebab-case, theo domain | `google-workspace/`       |
| Runbook file | `*-runbook.md`          | `vm-lifecycle-runbook.md` |
| Guide file   | `*-guide.md`            | `dns-guide.md`            |
| Postmortem   | `YYYY-MM-DD-title.md`   | `2026-03-15-db-outage.md` |
| Maintenance  | `maintenance-*.md`      | `maintenance-window.md`   |

---

## 🔗 Template Mapping

Mỗi loại doc map tới template cụ thể trong [templates/](../templates/README.md):

| Loại doc         | Template | Skill hướng dẫn            |
| ---------------- | -------- | -------------------------- |
| Runbook          | T1       | `ops-runbook-writer.md`    |
| Network topology | T5       | `ops-runbook-writer.md`    |
| How-to guide     | T3       | `project-doc-writer.md`    |
| ADR              | T2       | `project-doc-writer.md`    |
| Postmortem       | T6       | `ops-runbook-writer.md`    |
| Maintenance      | T7       | `ops-runbook-writer.md`    |
| Training         | T4       | `training-doc-writer.md`   |
| Release notes    | T8       | `project-doc-writer.md`    |
| Security policy  | —        | `infra-security-doc.md`    |
| Access control   | —        | `infra-security-doc.md`    |
| Audit log standards | —     | `infra-security-doc.md`    |

---

## ⚡ Quick Setup

```bash
# Tạo toàn bộ folder structure
mkdir -p docs/{network,proxmox,google-workspace,automation,github,incidents/postmortem,assets/{images,diagrams}}

# Tạo index files
for dir in network proxmox google-workspace automation github incidents; do
  echo "# $(echo $dir | sed 's/-/ /g' | sed 's/\b\(.\)/\u\1/g')" > "docs/$dir/index.md"
done

echo "# Infrastructure Documentation" > docs/index.md
```

---

> **Version:** 4.0.0 | **Updated:** 2026-03-30
