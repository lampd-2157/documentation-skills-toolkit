# Prompt: Tạo Runbook

> **Skill:** ops-runbook-writer | **Template:** T1 | **Output:** Runbook vận hành hệ thống

## Cách dùng

### AI Agent (Recommended)

1. Copy toàn bộ nội dung trong khung **Prompt** bên dưới
2. Mở AI agent bạn đang dùng (Claude, ChatGPT, Antigravity, Copilot...)
3. Paste prompt vào, sau đó **sửa dòng "Tạo runbook cho:"** — thay đoạn mô tả ví dụ bằng thông tin hệ thống thực tế của bạn
4. Gửi prompt → AI tạo runbook → bạn review kết quả
5. Chạy `make lint` để verify markdown format

**Ví dụ thực tế:** Nếu bạn cần viết runbook cho Redis cluster, sửa thành:

```text
Bước 3: Tạo runbook cho:
Redis Cluster 3 nodes trên Ubuntu 22.04, dùng cho session cache,
port 6379, memory limit 4GB/node, sentinel cho HA.
```

### Manual

```bash
./scripts/docs-toolkit new runbook "Redis Cluster"
```

Sau đó mở file vừa tạo, đọc `skills/ops-runbook-writer.md` (phần Iron Law + Guardrails), điền nội dung thủ công.

---

## Prompt

```text
Bạn là Documentation Agent. Hãy tạo runbook vận hành theo quy chuẩn.

Bước 1: Đọc file skills/ops-runbook-writer.md — ghi nhớ Iron Law và Guardrails.
Bước 2: Đọc file templates/runbook.md — đây là cấu trúc output.
Bước 3: Tạo runbook cho:

Nginx load balancer trên Ubuntu 22.04,
reverse proxy cho 3 backend servers, port 80/443.
<<<< SỬA ĐOẠN NÀY THÀNH HỆ THỐNG CỦA BẠN >>>>

Yêu cầu bắt buộc (Iron Law):
- Mọi command PHẢI copy-paste chạy được ngay trên terminal
- Mọi command PHẢI có expected output kèm theo
- Có escalation matrix với contact info thực tế

UI Standards:
- Dùng admonitions (!!! info/warning/danger) cho metadata và cảnh báo
- Dùng task lists (- [ ]) cho checklists
- Commands dài (>60 chars) đặt trong code blocks, không trong table cells

Tự kiểm tra trước khi hoàn thành:
- [ ] YAML frontmatter có title, status, updated
- [ ] Mỗi command trong code block có expected output
- [ ] Health checks table đầy đủ (Check | Command | Expected | Alert If)
- [ ] Có troubleshooting section với common issues
- [ ] Có rollback procedure
- [ ] Có escalation matrix
```
