# Prompt: Tạo How-to Guide

> **Skill:** project-doc-writer | **Template:** T3 | **Output:** Hướng dẫn step-by-step

## Cách dùng

### AI Agent (Recommended)

1. Copy toàn bộ nội dung trong khung **Prompt** bên dưới
2. Mở AI agent bạn đang dùng (Claude, ChatGPT, Antigravity, Copilot...)
3. Paste prompt vào, sau đó **sửa dòng "Tạo how-to guide cho:"** — thay đoạn mô tả ví dụ bằng task thực tế của bạn
4. Gửi prompt → AI tạo guide → bạn review kết quả
5. Chạy `make lint` để verify markdown format

**Ví dụ thực tế:** Nếu bạn cần viết hướng dẫn cài đặt VPN, sửa thành:

```text
Bước 3: Tạo how-to guide cho:
Cài đặt và cấu hình WireGuard VPN trên Ubuntu server,
cho phép remote team kết nối vào internal network.

Audience: System admin mới, đã biết Linux cơ bản.
```

### Manual

```bash
./scripts/docs-toolkit new howto "Setup WireGuard VPN"
```

Sau đó mở file vừa tạo, đọc `skills/project-doc-writer.md` (phần Iron Law + Guardrails), điền nội dung thủ công.

---

## Prompt

```text
Bạn là Documentation Agent. Hãy tạo how-to guide step-by-step.

Bước 1: Đọc file skills/project-doc-writer.md — ghi nhớ Iron Law và Guardrails.
Bước 2: Đọc file templates/howto-guide.md — đây là cấu trúc output.
Bước 3: Tạo how-to guide cho:

Tạo user mới trên Google Workspace, gán vào đúng OU và groups,
setup email signature chuẩn công ty.

Audience: IT admin mới, đã biết Google Admin Console cơ bản.
<<<< SỬA ĐOẠN NÀY THÀNH TASK CỦA BẠN >>>>

Yêu cầu bắt buộc (Iron Law):
- PHẢI có Prerequisites (cần gì trước khi bắt đầu)
- PHẢI có Steps rõ ràng, đánh số thứ tự
- PHẢI có Expected Result sau mỗi bước quan trọng
- PHẢI có Troubleshooting cho common errors

UI Standards:
- Dùng admonitions (!!! info/warning/danger) cho metadata và cảnh báo
- Dùng task lists (- [ ]) cho checklists
- Commands dài (>60 chars) đặt trong code blocks, không trong table cells

Security:
- KHÔNG hardcode IP, password, token, internal URL — dùng placeholders: <INTERNAL_IP>, <PASSWORD>, <API_TOKEN>

Tự kiểm tra trước khi hoàn thành:
- [ ] Prerequisites liệt kê đầy đủ (quyền, tools, access)
- [ ] Mỗi step có action cụ thể (không mơ hồ)
- [ ] Có expected output mô tả kết quả mong đợi
- [ ] Troubleshooting cover ít nhất 2-3 common issues
- [ ] Đã thêm vào mkdocs.yml nav section
```
