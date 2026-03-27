# Prompt: Tạo Training Module

> **Skill:** training-doc-writer | **Template:** T4 | **Output:** Module training nội bộ

## Cách dùng

### AI Agent (Recommended)

1. Copy toàn bộ nội dung trong khung **Prompt** bên dưới
2. Mở AI agent bạn đang dùng (Claude, ChatGPT, Antigravity, Copilot...)
3. Paste prompt vào, sau đó **sửa dòng "Tạo training module cho:"** — thay đoạn mô tả ví dụ bằng topic thực tế của bạn
4. Gửi prompt → AI tạo module → bạn review kết quả
5. Chạy `make lint` để verify markdown format

**Ví dụ thực tế:** Nếu bạn cần tạo training về Terraform, sửa thành:

```text
Bước 3: Tạo training module cho:
Terraform Basics cho team DevOps, từ init tới apply.

Audience: Developer biết cloud cơ bản, chưa dùng IaC.
Duration: 3 giờ.
```

### Manual

```bash
./scripts/docs-toolkit new training "Terraform Basics"
```

Sau đó mở file vừa tạo, đọc `skills/training-doc-writer.md` (phần Iron Law + Guardrails), điền nội dung thủ công.

---

## Prompt

```text
Bạn là Documentation Agent. Hãy tạo training module.

Bước 1: Đọc file skills/training-doc-writer.md — ghi nhớ Iron Law và Guardrails.
Bước 2: Đọc file templates/training-module.md — đây là cấu trúc output.
Bước 3: Tạo training module cho:

Git Basics cho team development, từ clone tới pull request.

Audience: Developer mới, chưa dùng Git bao giờ.
Duration: 2 giờ.
<<<< SỬA ĐOẠN NÀY THÀNH TOPIC CỦA BẠN >>>>

Yêu cầu bắt buộc (Iron Law):
- PHẢI có Prerequisites (cài đặt gì trước)
- PHẢI có Steps rõ ràng với hands-on exercises
- PHẢI có Expected Result cho mỗi exercise
- PHẢI có Troubleshooting cho common errors

UI Standards:
- Dùng admonitions (!!! info/warning/danger) cho metadata và cảnh báo
- Dùng task lists (- [ ]) cho checklists
- Commands dài (>60 chars) đặt trong code blocks, không trong table cells

Tự kiểm tra trước khi hoàn thành:
- [ ] Prerequisites liệt kê tools cần cài + phiên bản
- [ ] Mỗi lesson có objective rõ ràng
- [ ] Có hands-on lab với commands chạy được
- [ ] Expected result cho mỗi lab step
- [ ] Knowledge check hoặc quiz ở cuối
```
