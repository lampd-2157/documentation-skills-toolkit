# Demo Site — Documentation Skills Toolkit

> Chạy demo site để xem output thực tế khi dùng bộ toolkit.

## Quick Start

```bash
cd demo-site

# Install dependencies
pip install mkdocs-material mkdocs-mermaid2-plugin

# Run local
mkdocs serve
# → Mở http://localhost:8000
```

## Files mẫu

| File                                              | Template dùng | Nội dung                     |
| ------------------------------------------------- | ------------- | ---------------------------- |
| `docs/index.md`                                   | —             | Landing page                 |
| `docs/getting-started/quick-start.md`             | T3 How-to     | Setup MkDocs                 |
| `docs/operations/runbooks/proxmox-vm-runbook.md`  | T1 Runbook    | VM quản lý trên Proxmox      |
| `docs/development/adr/adr-001-mkdocs.md`          | T2 ADR        | Tại sao chọn MkDocs-Material |
| `docs/guides/how-to/google-workspace-new-user.md` | T3 How-to     | Tạo user GWS mới             |
