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

Đọc file skills/AGENT-CARDS.json để hiểu danh sách skills:
- docs-engineer — Setup MkDocs, chuẩn hóa markdown
- ops-runbook-writer — Runbook, network docs, incident docs
- training-doc-writer — Training, onboarding, curriculum
- project-doc-writer — ADR, tech spec, how-to guide
- infra-security-doc — Security policy, RBAC, audit

Tôi cần: viết tài liệu hướng dẫn deploy ứng dụng lên Kubernetes
cho team DevOps, bao gồm commands và troubleshooting.
<<<< SỬA ĐOẠN NÀY THÀNH NHU CẦU CỦA BẠN >>>>

Hãy recommend:
1. Skill nào phù hợp nhất (và tại sao)
2. Template nào nên dùng (T1-T11)
3. File prompt nào trong prompts/ để bắt đầu
4. Nếu cần kết hợp nhiều skills, gợi ý thứ tự
```
