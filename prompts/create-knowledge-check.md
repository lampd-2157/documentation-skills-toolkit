# Prompt: Tạo Knowledge Check

> **Skill:** training-doc-writer | **Template:** T11 | **Output:** Bài kiểm tra kiến thức

## Cách dùng

### AI Agent (Recommended)

1. Copy toàn bộ nội dung trong khung **Prompt** bên dưới
2. Mở AI agent bạn đang dùng (Claude, ChatGPT, Antigravity, Copilot...)
3. Paste prompt vào, sau đó **sửa dòng "Tạo knowledge check cho:"** — thay đoạn mô tả ví dụ bằng topic thực tế
4. Gửi prompt → AI tạo bài kiểm tra → bạn review kết quả
5. Chạy `make lint` để verify markdown format

**Ví dụ thực tế:** Nếu bạn cần tạo quiz về Kubernetes, sửa thành:

```text
Bước 3: Tạo knowledge check cho:
Kubernetes basics, dành cho developer đã hoàn thành training K8s 101.

Level: Beginner.
Pass criteria: >= 70% correct.
```

### Manual

```bash
./scripts/docs-toolkit new knowledge-check "Kubernetes Basics"
```

Sau đó mở file vừa tạo, đọc `skills/training-doc-writer.md` (phần Iron Law + Guardrails), điền nội dung thủ công.

---

## Prompt

```text
Bạn là Documentation Agent. Hãy tạo knowledge check (bài kiểm tra kiến thức).

Bước 1: Đọc file skills/training-doc-writer.md — ghi nhớ Iron Law và Guardrails.
Bước 2: Đọc file templates/knowledge-check.md — đây là cấu trúc output.
Bước 3: Tạo knowledge check cho:

Docker basics, dành cho developer mới học container.

Level: Beginner, đã hoàn thành training module Docker Basics.
Pass criteria: >= 80% correct.
<<<< SỬA ĐOẠN NÀY THÀNH TOPIC CỦA BẠN >>>>

Yêu cầu bắt buộc (Iron Law):
- PHẢI có Prerequisites (học xong gì trước khi làm bài)
- Câu hỏi PHẢI có answer + explanation (dùng collapsible)
- PHẢI có scenario-based questions (không chỉ lý thuyết)

UI Standards:
- Dùng admonitions (!!! info/warning/danger) cho metadata và cảnh báo
- Dùng task lists (- [ ]) cho checklists
- Commands dài (>60 chars) đặt trong code blocks, không trong table cells

Security:
- KHÔNG hardcode IP, password, token, internal URL — dùng placeholders: <INTERNAL_IP>, <PASSWORD>, <API_TOKEN>

Tự kiểm tra trước khi hoàn thành:
- [ ] Ít nhất 3 câu multiple choice
- [ ] Ít nhất 1 scenario-based question
- [ ] Mỗi câu có answer + explanation trong collapsible block
- [ ] Assessment summary table ở cuối
- [ ] Pass criteria rõ ràng
- [ ] Đã thêm vào mkdocs.yml nav section
```
