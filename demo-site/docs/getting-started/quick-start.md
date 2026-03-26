---
title: "Quick Start — Setup MkDocs"
description: "Hướng dẫn setup MkDocs-Material cho documentation project"
author: "Documentation Team"
created: 2026-03-26
updated: 2026-03-26
status: approved
tags: [getting-started, mkdocs, setup]
---

# How to Setup MkDocs cho Documentation Project

> **Audience:** Mọi thành viên team
> **Time:** ~15 minutes
> **Difficulty:** ⭐ Beginner

## Prerequisites

- [ ] Python 3.8+ installed (`python3 --version`)
- [ ] pip installed (`pip --version`)
- [ ] Git configured

## Steps

### Step 1: Install MkDocs và plugins

MkDocs-Material là theme chính thức, hỗ trợ dark mode, search, navigation, admonitions.

```bash
pip install mkdocs-material mkdocs-mermaid2-plugin
```

**Expected result:**

```text
Successfully installed mkdocs-material-... mkdocs-mermaid2-plugin-...
```

### Step 2: Copy starter config

```bash
# Copy từ toolkit
cp templates/references/mkdocs-starter.yml mkdocs.yml
cp templates/references/markdownlint-config.json .markdownlint.json
```

**Expected result:** 2 files config xuất hiện ở root project.

### Step 3: Tạo folder structure

```bash
mkdir -p docs/{getting-started,operations/runbooks,development/adr,guides/how-to,assets/images}
echo "# Project Documentation" > docs/index.md
```

### Step 4: Preview local

```bash
mkdocs serve
```

**Expected result:** Mở browser tại `http://localhost:8000` → thấy docs site.

!!! tip
    MkDocs auto-reload khi bạn sửa file `.md`. Không cần restart.

## Verify

- [ ] `mkdocs serve` chạy thành công
- [ ] Browser hiển thị docs site tại localhost:8000
- [ ] Dark mode toggle hoạt động

## Troubleshooting

### Error: `mkdocs: command not found`

**Cause:** MkDocs chưa trong PATH.
**Fix:**

```bash
# Kiểm tra pip install location
pip show mkdocs | grep Location
# Thêm vào PATH nếu cần
export PATH="$HOME/.local/bin:$PATH"
```

## Next Steps

- [Proxmox VM Runbook](../operations/runbooks/proxmox-vm-runbook.md)
- [Google Workspace New User](../guides/how-to/google-workspace-new-user.md)
