# Prompt: Tạo Incident Postmortem

> **Skill:** ops-runbook-writer | **Template:** T6 | **Output:** Báo cáo phân tích sau sự cố

## Cách dùng

### AI Agent (Recommended)

1. Copy toàn bộ nội dung trong khung **Prompt** bên dưới
2. Mở AI agent bạn đang dùng (Claude, ChatGPT, Antigravity, Copilot...)
3. Paste prompt vào, sau đó **sửa dòng "Tạo postmortem cho:"** — thay đoạn mô tả ví dụ bằng sự cố thực tế, kèm timeline nếu có
4. Gửi prompt → AI tạo postmortem → bạn review kết quả
5. Chạy `make lint` để verify markdown format

**Ví dụ thực tế:** Nếu bạn cần viết postmortem cho sự cố API, sửa thành:

```text
Bước 3: Tạo postmortem cho:
API gateway trả 503 liên tục trong 20 phút,
nguyên nhân do certificate hết hạn, ảnh hưởng 500 users.

Timeline:
- 09:00 Monitoring alert: API 503 spike
- 09:10 Team xác nhận SSL cert expired
- 09:15 Renew cert + restart nginx
- 09:20 Service recovered
```

### Manual

```bash
./scripts/docs-toolkit new postmortem "API Gateway 503"
```

Sau đó mở file vừa tạo, đọc `skills/ops-runbook-writer.md` (phần Iron Law + Guardrails), điền nội dung thủ công.

---

## Prompt

```text
Bạn là Documentation Agent. Hãy tạo incident postmortem.

Bước 1: Đọc file skills/ops-runbook-writer.md — ghi nhớ Iron Law và Guardrails.
Bước 2: Đọc file templates/incident-postmortem.md — đây là cấu trúc output.
Bước 3: Tạo postmortem cho:

Database connection pool exhaustion gây downtime 45 phút
trên production, ảnh hưởng 2000 users.

Timeline:
- 14:00 Alert CPU spike trên DB server
- 14:15 DB connections maxed out (500/500)
- 14:30 DBA restart connection pool + increase limit
- 14:45 Recovery confirmed, all services healthy
<<<< SỬA ĐOẠN NÀY THÀNH SỰ CỐ CỦA BẠN >>>>

Yêu cầu bắt buộc (Iron Law):
- PHẢI có Timeline chính xác (thời gian + sự kiện)
- PHẢI có Root Cause Analysis (5 Whys hoặc tương đương)
- PHẢI có Action Items với owner + deadline
- PHẢI có Lessons Learned

UI Standards:
- Dùng admonitions (!!! info/warning/danger) cho metadata và cảnh báo
- Dùng task lists (- [ ]) cho checklists
- Commands dài (>60 chars) đặt trong code blocks, không trong table cells

Security:
- KHÔNG hardcode IP, password, token, internal URL — dùng placeholders: <INTERNAL_IP>, <PASSWORD>, <API_TOKEN>

Tự kiểm tra trước khi hoàn thành:
- [ ] Impact assessment: ai bị ảnh hưởng, bao lâu, severity
- [ ] Timeline đầy đủ từ detect tới recovery
- [ ] Root cause rõ ràng (không blame cá nhân)
- [ ] Action items có owner + deadline cụ thể
- [ ] Lessons learned có prevention measures
- [ ] Đã thêm vào mkdocs.yml nav section
```
