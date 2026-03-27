---
title: "Quick Start — Setup MkDocs"
description: "Hướng dẫn setup MkDocs-Material cho documentation project"
author: "Documentation Team"
created: 2026-03-26
updated: 2026-03-26
status: approved
tags: [getting-started, mkdocs, setup]
---

# :material-rocket-launch: Quick Start — Setup MkDocs

!!! abstract "Overview"
    **Audience:** Mọi thành viên team | **Time:** ~15 minutes | **Difficulty:** Beginner

## Prerequisites

- [x] Python 3.8+ installed (`python3 --version`)
- [x] pip installed (`pip --version`)
- [x] Git configured

---

## Steps

### Step 1: Install MkDocs + plugins

=== ":material-linux: Linux / WSL"

    ```bash
    pip install mkdocs-material
    export PATH="$HOME/.local/bin:$PATH"
    ```

=== ":material-apple: macOS"

    ```bash
    pip3 install mkdocs-material
    ```

=== ":material-microsoft-windows: Windows"

    ```powershell
    pip install mkdocs-material
    ```

**Expected result:**

```text
Successfully installed mkdocs-material-...
```

### Step 2: Copy starter config

```bash
cp references/config/mkdocs-starter.yml mkdocs.yml
cp references/config/markdownlint-config.json .markdownlint.json
```

!!! tip "Hoặc dùng one-command setup"
    ```bash
    bash references/config/setup.sh
    ```
    Script sẽ cài tất cả: MkDocs, markdownlint, pre-commit hooks, VS Code snippets.

### Step 3: Tạo folder structure

```bash
mkdir -p docs/{getting-started,operations/runbooks,development/adr,guides/how-to,training,assets/images}
echo "# Project Documentation" > docs/index.md
```

### Step 4: Preview local

```bash
mkdocs serve
```

**Expected result:** Mở browser tại `http://localhost:8000` — docs site hiện ra với Material theme.

!!! tip "Auto-reload"
    MkDocs tự reload khi bạn sửa file `.md`. Không cần restart server.

---

## Verify

- [x] `mkdocs serve` chạy thành công
- [x] Browser hiển thị docs site tại localhost:8000
- [x] Dark mode toggle hoạt động (icon góc phải trên)

---

## Troubleshooting

??? warning "Error: `mkdocs: command not found`"
    **Cause:** MkDocs chưa trong PATH (phổ biến trên Linux/WSL).

    **Fix:**
    ```bash
    export PATH="$HOME/.local/bin:$PATH"
    # Để fix vĩnh viễn:
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
    source ~/.bashrc
    ```

---

## Next Steps

!!! example "Tạo doc đầu tiên"
    ```bash
    ./scripts/docs-toolkit new runbook "My Service"
    ```

- [Proxmox VM Runbook](../operations/runbooks/proxmox-vm-runbook.md) — Ví dụ T1 Runbook
- [Google Workspace New User](../guides/how-to/google-workspace-new-user.md) — Ví dụ T3 How-to
