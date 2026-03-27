# Prompt: Tạo Security Policy

> **Skill:** infra-security-doc | **Template:** — | **Output:** Chính sách bảo mật

## Cách dùng

### AI Agent (Recommended)

1. Copy toàn bộ nội dung trong khung **Prompt** bên dưới
2. Mở AI agent bạn đang dùng (Claude, ChatGPT, Antigravity, Copilot...)
3. Paste prompt vào, sau đó **sửa dòng "Tạo security policy cho:"** — thay đoạn mô tả ví dụ bằng policy thực tế của bạn
4. Gửi prompt → AI tạo policy → bạn review kết quả
5. Chạy `make lint` để verify markdown format

**Ví dụ thực tế:** Nếu bạn cần viết password policy, sửa thành:

```text
Bước 3: Tạo security policy cho:
Password Policy cho toàn bộ nhân viên công ty.
Yêu cầu: min 12 ký tự, MFA bắt buộc, rotate 90 ngày,
no password reuse (10 lần gần nhất).

Scope: Tất cả accounts trên Active Directory + cloud services.
```

### Manual

```bash
./scripts/docs-toolkit new security-policy "Password Policy"
```

Sau đó mở file vừa tạo, đọc `skills/infra-security-doc.md` (phần Iron Law + Guardrails), điền nội dung thủ công.

---

## Prompt

```text
Bạn là Documentation Agent. Hãy tạo security policy document.

Bước 1: Đọc file skills/infra-security-doc.md — ghi nhớ Iron Law và Guardrails.
Bước 2: Tạo security policy cho:

Access Control Policy cho production Kubernetes cluster.
RBAC-based, áp dụng cho team DevOps (10 người) và SRE (5 người).

Scope: Tất cả production namespaces, staging cho testing.
<<<< SỬA ĐOẠN NÀY THÀNH POLICY CỦA BẠN >>>>

Yêu cầu bắt buộc (Iron Law):
- PHẢI có Scope (áp dụng cho ai, hệ thống nào)
- PHẢI có Policy Statements (quy định cụ thể)
- PHẢI có Enforcement (vi phạm thì xử lý thế nào)
- PHẢI có Audit (kiểm tra tuân thủ bằng cách nào)

UI Standards:
- Dùng admonitions (!!! info/warning/danger) cho metadata và cảnh báo
- Dùng task lists (- [ ]) cho checklists
- Commands dài (>60 chars) đặt trong code blocks, không trong table cells

Tự kiểm tra trước khi hoàn thành:
- [ ] Scope rõ ràng (teams, systems, environments)
- [ ] Policy statements cụ thể, actionable
- [ ] Enforcement table (violation type → consequence → escalation)
- [ ] Audit schedule và method
- [ ] Review date (6 tháng từ effective date)
- [ ] Đã thêm vào mkdocs.yml nav section
```
