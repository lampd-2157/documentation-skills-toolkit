# Prompt: Tạo Architecture Diagram

> **Skill:** project-doc-writer | **Template:** T12 | **Output:** Architecture diagram documentation

## Cách dùng

### AI Agent (Recommended)

1. Copy toàn bộ nội dung trong khung **Prompt** bên dưới
2. Mở AI agent bạn đang dùng (Claude, ChatGPT, Antigravity, Copilot...)
3. Paste prompt vào, sau đó **sửa dòng "Tạo architecture diagram cho:"** — thay đoạn mô tả ví dụ bằng hệ thống thực tế của bạn
4. Gửi prompt → AI tạo docs → bạn review kết quả
5. Chạy `make lint` để verify markdown format

**Ví dụ thực tế:** Nếu bạn cần document kiến trúc cho e-commerce platform, sửa thành:

```text
Bước 3: Tạo architecture diagram cho:
E-commerce Platform — Microservices architecture xử lý orders, payments, inventory.
Components: API Gateway, Order Service, Payment Service, Inventory Service, PostgreSQL, Redis, RabbitMQ.
Deployment: AWS EKS, 2 AZ, ALB.

Audience: Backend developer mới join team, cần hiểu tổng quan hệ thống.
```

### Manual

Copy template `templates/architecture-diagram.md`, đọc `skills/project-doc-writer.md` (Iron Law + Guardrails), điền nội dung thủ công.

---

## Phase 0: Interview (Recommended)

Trước khi tạo doc, hãy hỏi user để gather context. Copy câu hỏi từ [interview-before-create.md](interview-before-create.md) hoặc hỏi tối thiểu 3 câu:

1. **Audience:** Ai đọc doc này? New dev, architect, ops team?
2. **Scope:** Document toàn bộ system hay 1 subsystem? Bao gồm deployment view?
3. **Environment:** Cloud provider? On-prem? Container orchestration? Key technologies?

> Có answers rồi? Tiếp tục với prompt bên dưới — thay thông tin vào đoạn `<<<< SỬA >>>>`.

---

## Prompt

```text
Bạn là Documentation Agent. Hãy tạo architecture diagram documentation.

Bước 1: Đọc file skills/project-doc-writer.md — ghi nhớ Iron Law và Guardrails.
Bước 2: Đọc file templates/architecture-diagram.md — đây là cấu trúc output.
Bước 3: Tạo architecture diagram cho:

Internal Tools Platform — Monorepo với 3 services: Auth, Dashboard, Notifications.
Stack: Node.js (Express), PostgreSQL, Redis, deployed trên Kubernetes.
External integrations: Slack API, SendGrid, Okta SSO.

Audience: Developer mới join team, cần hiểu system overview.
<<<< SỬA ĐOẠN NÀY THÀNH HỆ THỐNG CỦA BẠN >>>>

Yêu cầu bắt buộc (từ Template T12):
- PHẢI có Context Diagram (hệ thống tương tác với bên ngoài như thế nào)
- PHẢI có Component Diagram (các thành phần bên trong giao tiếp ra sao)
- PHẢI có Data Flow (dữ liệu di chuyển như thế nào cho các use case chính)
- PHẢI dùng Mermaid syntax cho mọi diagram

UI Standards:
- Dùng admonitions (!!! info/warning/danger) cho metadata và cảnh báo
- Mỗi diagram phải có bảng mô tả bổ sung (không chỉ diagram không)
- Code blocks có language tag (mermaid, bash, json)

Security:
- KHÔNG hardcode IP nội bộ, credentials, internal URL — dùng placeholders
- Tham khảo docs/security-placeholders.md

Flexible Sections:
- Required: Context Diagram, Component Diagram, Data Flow
- Recommended: Technology Stack, Deployment View, Security Boundaries
- Optional: Performance Considerations, Evolution Roadmap

Tự kiểm tra trước khi hoàn thành:
- [ ] Có Context Diagram với actors và external systems
- [ ] Có Component Diagram với internal services
- [ ] Có Data Flow cho ít nhất 1 use case chính
- [ ] Mọi diagram dùng Mermaid syntax hợp lệ
- [ ] Mọi diagram có bảng mô tả kèm theo
- [ ] Không có real credentials/IPs
```
