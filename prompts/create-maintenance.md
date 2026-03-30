# Prompt: Tạo Maintenance Window Plan

> **Skill:** ops-runbook-writer | **Template:** T7 | **Output:** Kế hoạch bảo trì hệ thống

## Cách dùng

### AI Agent (Recommended)

1. Copy toàn bộ nội dung trong khung **Prompt** bên dưới
2. Mở AI agent bạn đang dùng (Claude, ChatGPT, Antigravity, Copilot...)
3. Paste prompt vào, sau đó **sửa dòng "Tạo maintenance plan cho:"** — thay đoạn mô tả ví dụ bằng kế hoạch bảo trì thực tế
4. Gửi prompt → AI tạo plan → bạn review kết quả
5. Chạy `make lint` để verify markdown format

**Ví dụ thực tế:** Nếu bạn cần lên kế hoạch upgrade Kubernetes, sửa thành:

```text
Bước 3: Tạo maintenance plan cho:
Upgrade Kubernetes cluster từ 1.28 lên 1.30,
3 master + 5 worker nodes, rolling upgrade.

Schedule: Chủ nhật, 01:00-05:00 UTC.
Systems affected: Tất cả microservices trên cluster.
```

### Manual

```bash
./scripts/docs-toolkit new maintenance "K8s Upgrade 1.30"
```

Sau đó mở file vừa tạo, đọc `skills/ops-runbook-writer.md` (phần Iron Law + Guardrails), điền nội dung thủ công.

---

## Prompt

```text
Bạn là Documentation Agent. Hãy tạo maintenance window plan.

Bước 1: Đọc file skills/ops-runbook-writer.md — ghi nhớ Iron Law và Guardrails.
Bước 2: Đọc file templates/maintenance-window.md — đây là cấu trúc output.
Bước 3: Tạo maintenance plan cho:

Upgrade PostgreSQL từ 14 lên 16 trên production cluster.
Downtime dự kiến 30 phút.

Schedule: Thứ 7, 02:00-04:00 UTC.
Systems affected: DB primary + 2 replicas, API service.
<<<< SỬA ĐOẠN NÀY THÀNH KẾ HOẠCH BẢO TRÌ CỦA BẠN >>>>

Yêu cầu bắt buộc (Iron Law):
- Mọi command PHẢI copy-paste chạy được ngay
- PHẢI có pre-checks trước khi bắt đầu
- PHẢI có rollback procedure chi tiết
- PHẢI có post-checks sau khi hoàn thành

UI Standards:
- Dùng admonitions (!!! info/warning/danger) cho metadata và cảnh báo
- Dùng task lists (- [ ]) cho checklists
- Commands dài (>60 chars) đặt trong code blocks, không trong table cells

Security:
- KHÔNG hardcode IP, password, token, internal URL — dùng placeholders: <INTERNAL_IP>, <PASSWORD>, <API_TOKEN>

Tự kiểm tra trước khi hoàn thành:
- [ ] Pre-checks: backup, health check, notification
- [ ] Procedure: từng bước có command + expected output
- [ ] Rollback: plan B nếu fail, với trigger conditions
- [ ] Post-checks: verify service healthy sau maintenance
- [ ] Communication: notify stakeholders trước/sau
- [ ] Đã thêm vào mkdocs.yml nav section
```
