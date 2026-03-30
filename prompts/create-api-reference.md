# Prompt: Tạo API Reference

> **Skill:** api-doc-writer | **Template:** T13 | **Output:** API reference documentation

## Cách dùng

### AI Agent (Recommended)

1. Copy toàn bộ nội dung trong khung **Prompt** bên dưới
2. Mở AI agent bạn đang dùng (Claude, ChatGPT, Antigravity, Copilot...)
3. Paste prompt vào, sau đó **sửa dòng "Tạo API reference cho:"** — thay đoạn mô tả ví dụ bằng API thực tế của bạn
4. Gửi prompt → AI tạo docs → bạn review kết quả
5. Chạy `make lint` để verify markdown format

**Ví dụ thực tế:** Nếu bạn cần viết docs cho User Management API, sửa thành:

```text
Bước 3: Tạo API reference cho:
User Management API — CRUD operations cho user accounts.
Endpoints: GET /users, GET /users/:id, POST /users, PUT /users/:id, DELETE /users/:id.
Auth: Bearer token. Format: JSON. Base URL: https://api.example.com/v1

Audience: Backend developer, đã biết REST API basics.
```

### Manual

Copy template `templates/api-reference.md`, đọc `skills/api-doc-writer.md` (Iron Law + Guardrails), điền nội dung thủ công.

---

## Phase 0: Interview (Recommended)

Trước khi tạo doc, hãy hỏi user để gather context. Copy câu hỏi từ [interview-before-create.md](interview-before-create.md) hoặc hỏi tối thiểu 3 câu:

1. **Audience:** Ai đọc doc này? Frontend dev, backend dev, external partners?
2. **Scope:** Endpoint nào cần document? Bao gồm auth, rate limits, webhooks?
3. **Environment:** Base URL? Auth method? API version? Response format?

> Có answers rồi? Tiếp tục với prompt bên dưới — thay thông tin vào đoạn `<<<< SỬA >>>>`.

---

## Prompt

```text
Bạn là Documentation Agent. Hãy tạo API reference documentation.

Bước 1: Đọc file skills/api-doc-writer.md — ghi nhớ Iron Law và Guardrails.
Bước 2: Đọc file templates/api-reference.md — đây là cấu trúc output.
Bước 3: Tạo API reference cho:

Task Management API — CRUD operations cho tasks và projects.
Endpoints: GET/POST /tasks, GET/PUT/DELETE /tasks/:id, GET /projects.
Auth: Bearer token (JWT). Format: JSON. Base URL: https://api.example.com/v1

Audience: Backend developer integrate task system.
<<<< SỬA ĐOẠN NÀY THÀNH API CỦA BẠN >>>>

Yêu cầu bắt buộc (Iron Law):
- PHẢI có request example (curl) cho MỌI endpoint
- PHẢI có response example (JSON) cho MỌI endpoint
- PHẢI có error codes table (≥ 5 HTTP status codes)
- PHẢI có authentication section với copy-paste example

UI Standards:
- Dùng admonitions (!!! info/warning/danger) cho metadata và cảnh báo
- Endpoint headers dùng format: ### `METHOD /path`
- Code blocks có language tag (bash, json)

Security:
- KHÔNG hardcode API key, token, internal URL — dùng placeholders: <API_TOKEN>, example.com
- Tham khảo docs/security-placeholders.md

Flexible Sections:
- Required: Overview, Endpoints, Error Codes
- Recommended: Authentication, Rate Limits, Changelog
- Optional: SDKs, Webhooks, Migration Guide

Tự kiểm tra trước khi hoàn thành:
- [ ] Mỗi endpoint có request + response example
- [ ] Error codes table đầy đủ (400, 401, 403, 404, 500+)
- [ ] Auth section có curl command chạy được ngay
- [ ] Không có real credentials/URLs
- [ ] Pagination documented nếu API trả list
- [ ] Rate limits documented
```
