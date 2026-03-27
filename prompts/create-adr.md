# Prompt: Tạo Architecture Decision Record (ADR)

> **Skill:** project-doc-writer | **Template:** T2 (Nygard) / T9 (MADR) / T10 (Lightweight) | **Output:** ADR

## Cách dùng

### AI Agent (Recommended)

1. Copy toàn bộ nội dung trong khung **Prompt** bên dưới
2. Mở AI agent bạn đang dùng (Claude, ChatGPT, Antigravity, Copilot...)
3. Paste prompt vào, sau đó **sửa dòng "Tạo ADR cho:"** — thay đoạn mô tả ví dụ bằng quyết định thực tế của bạn
4. Gửi prompt → AI tạo ADR → bạn review kết quả
5. Chạy `make lint` để verify markdown format

**Ví dụ thực tế:** Nếu bạn cần ghi nhận quyết định chọn message queue, sửa thành:

```text
Bước 3: Tạo ADR cho:
Chọn RabbitMQ làm message broker thay vì Kafka.
Team 5 người, traffic ~1000 msg/s, cần routing phức tạp,
không cần replay/stream processing.
```

### Chọn format ADR

| Format | Khi nào dùng | Template |
|---|---|---|
| **Nygard** (classic) | Decision đã rõ, cần ghi nhận | T2 (`templates/adr.md`) |
| **MADR** (structured) | Nhiều options, cần phân tích pros/cons | T9 (`templates/adr-madr.md`) |
| **Lightweight** (~15 dòng) | Quick decision, POC, spike | T10 (`templates/adr-lightweight.md`) |

### Manual

```bash
./scripts/docs-toolkit new adr "Chọn RabbitMQ"
```

Sau đó mở file vừa tạo, đọc `skills/project-doc-writer.md` (phần Iron Law + Guardrails), điền nội dung thủ công.

---

## Prompt

```text
Bạn là Documentation Agent. Hãy tạo Architecture Decision Record (ADR).

Bước 1: Đọc file skills/project-doc-writer.md — ghi nhớ Iron Law và Guardrails.
Bước 2: Đọc file templates/adr.md (hoặc templates/adr-madr.md nếu cần phân tích nhiều options).
Bước 3: Tạo ADR cho:

Chọn PostgreSQL làm database chính cho hệ thống e-commerce,
thay thế MongoDB hiện tại. Team có kinh nghiệm SQL,
cần ACID transactions, data volume ~50GB.
<<<< SỬA ĐOẠN NÀY THÀNH QUYẾT ĐỊNH CỦA BẠN >>>>

Yêu cầu bắt buộc (Iron Law):
- PHẢI có Context (tại sao cần quyết định này)
- PHẢI có Decision (quyết định gì, chọn option nào)
- PHẢI có Consequences (positive + negative + risks)

UI Standards:
- Dùng admonitions (!!! info/warning/danger) cho metadata và cảnh báo
- Dùng task lists (- [ ]) cho checklists
- Commands dài (>60 chars) đặt trong code blocks, không trong table cells

Tự kiểm tra trước khi hoàn thành:
- [ ] Context giải thích rõ vấn đề cần giải quyết
- [ ] Decision rõ ràng, không mập mờ
- [ ] Consequences có cả positive VÀ negative
- [ ] Status field: Proposed / Accepted / Deprecated
```
