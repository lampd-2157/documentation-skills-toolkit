# Prompt: Tạo Release Notes

> **Skill:** project-doc-writer | **Template:** T8 | **Output:** Tóm tắt version release

## Cách dùng

### AI Agent (Recommended)

1. Copy toàn bộ nội dung trong khung **Prompt** bên dưới
2. Mở AI agent bạn đang dùng (Claude, ChatGPT, Antigravity, Copilot...)
3. Paste prompt vào, sau đó **sửa dòng "Tạo release notes cho:"** — thay đoạn mô tả ví dụ bằng version + changes thực tế
4. Gửi prompt → AI tạo release notes → bạn review kết quả
5. Chạy `make lint` để verify markdown format

**Ví dụ thực tế:** Nếu bạn cần viết release notes cho app, sửa thành:

```text
Bước 3: Tạo release notes cho:
MyApp v3.2.0 — thêm OAuth2 login, fix pagination bug,
upgrade React từ 18 lên 19, deprecate /api/v1 endpoints.
```

### Manual

```bash
./scripts/docs-toolkit new release-notes "v3.2.0"
```

Sau đó mở file vừa tạo, đọc `skills/project-doc-writer.md` (phần Iron Law + Guardrails), điền nội dung thủ công.

---

## Prompt

```text
Bạn là Documentation Agent. Hãy tạo release notes.

Bước 1: Đọc file skills/project-doc-writer.md — ghi nhớ Iron Law và Guardrails.
Bước 2: Đọc file templates/release-notes.md — đây là cấu trúc output.
Bước 3: Tạo release notes cho:

MyApp v2.5.0 — thêm dark mode, fix login timeout bug,
upgrade dependencies, breaking change: API response format đổi
từ snake_case sang camelCase.
<<<< SỬA ĐOẠN NÀY THÀNH VERSION + CHANGES CỦA BẠN >>>>

Yêu cầu bắt buộc (Iron Law):
- PHẢI có Context (version này giải quyết gì)
- PHẢI phân loại: Added / Changed / Fixed / Breaking Changes
- PHẢI có upgrade guide nếu có breaking changes

UI Standards:
- Dùng admonitions (!!! info/warning/danger) cho metadata và cảnh báo
- Dùng task lists (- [ ]) cho checklists
- Commands dài (>60 chars) đặt trong code blocks, không trong table cells

Security:
- KHÔNG hardcode IP, password, token, internal URL — dùng placeholders: <INTERNAL_IP>, <PASSWORD>, <API_TOKEN>

Tự kiểm tra trước khi hoàn thành:
- [ ] Version number và date rõ ràng
- [ ] Changes phân loại đúng (Added/Changed/Fixed/Removed)
- [ ] Breaking changes có migration guide
- [ ] Highlights tóm tắt 2-3 điểm quan trọng nhất
- [ ] Đã thêm vào mkdocs.yml nav section
```
