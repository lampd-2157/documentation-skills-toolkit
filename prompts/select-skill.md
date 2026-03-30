# Prompt: Chọn Skill Phù Hợp

> Dùng khi không biết nên dùng skill/template nào cho nhu cầu của bạn.

## Cách dùng

### AI Agent (Recommended)

1. Copy toàn bộ nội dung trong khung **Prompt** bên dưới
2. Mở AI agent bạn đang dùng (Claude, ChatGPT, Antigravity, Copilot...)
3. Paste prompt vào, sau đó **sửa dòng "Tôi cần:"** — thay đoạn mô tả ví dụ bằng nhu cầu thực tế của bạn
4. Gửi prompt → AI gợi ý skill + template + prompt phù hợp

**Ví dụ thực tế:** Nếu bạn muốn viết tài liệu onboarding, sửa thành:

```text
Tôi cần: viết tài liệu onboarding cho developer mới vào team,
bao gồm setup môi trường, coding conventions, và Git workflow.
```

### Manual

Đọc bảng Skill Selection trong [AGENTS.md](../AGENTS.md) hoặc scan nhanh [skills/AGENT-CARDS.json](../skills/AGENT-CARDS.json).

---

## Prompt

```text
Tôi đang dùng Documentation Skills Toolkit. Hãy giúp tôi chọn skill và template phù hợp.

Bước 1: Đọc file config/routing-signals.yaml để hiểu routing logic.
Bước 2: Đọc file skills/AGENT-CARDS.json để hiểu danh sách skills.

Tôi cần: viết tài liệu hướng dẫn deploy ứng dụng lên Kubernetes
cho team DevOps, bao gồm commands và troubleshooting.
<<<< SỬA ĐOẠN NÀY THÀNH NHU CẦU CỦA BẠN >>>>

Hãy phân tích theo routing signals:
1. Keywords nào match? Confidence score bao nhiêu?
2. Primary skill nào? (và tại sao)
3. Cần kết hợp secondary skill không? (check composition_rules)
4. Template nào nên dùng? (T1-T11)
5. File prompt nào trong prompts/ để bắt đầu?
```
