# Prompt Templates — Documentation Skills Toolkit

> Prompt templates giúp AI agent tạo tài liệu đúng chuẩn. Hoạt động với mọi AI agent: Claude, ChatGPT, Antigravity, Copilot, hoặc bất kỳ agent nào.

## Cách dùng

**AI Agent (Recommended):**

1. Chọn prompt phù hợp từ bảng bên dưới
2. Mở file prompt → copy phần **Prompt**
3. Paste vào AI agent → sửa đoạn có dấu `<<<< SỬA ... >>>>` bằng thông tin thực tế
4. AI tạo doc → bạn review và chỉnh sửa
5. Validate: `make lint`

**Manual:**

1. Chọn template từ [templates/](../templates/README.md)
2. Scaffold: `./scripts/docs-toolkit new <type> "<title>"`
3. Đọc skill tương ứng → điền nội dung thủ công

## Chọn prompt

| Bạn muốn... | Prompt | Skill | Template |
|---|---|---|---|
| Tạo runbook vận hành | [create-runbook.md](create-runbook.md) | ops-runbook-writer | T1 |
| Ghi nhận architecture decision | [create-adr.md](create-adr.md) | project-doc-writer | T2/T9/T10 |
| Viết hướng dẫn step-by-step | [create-howto.md](create-howto.md) | project-doc-writer | T3 |
| Tạo module training | [create-training.md](create-training.md) | training-doc-writer | T4 |
| Document hạ tầng mạng | [create-network.md](create-network.md) | ops-runbook-writer | T5 |
| Viết postmortem sau sự cố | [create-postmortem.md](create-postmortem.md) | ops-runbook-writer | T6 |
| Lên kế hoạch bảo trì | [create-maintenance.md](create-maintenance.md) | ops-runbook-writer | T7 |
| Viết release notes | [create-release-notes.md](create-release-notes.md) | project-doc-writer | T8 |
| Tạo bài kiểm tra kiến thức | [create-knowledge-check.md](create-knowledge-check.md) | training-doc-writer | T11 |
| Viết security policy | [create-security-policy.md](create-security-policy.md) | infra-security-doc | — |
| Không biết dùng gì | [select-skill.md](select-skill.md) | — | — |
| Review doc hiện có | [review-doc.md](review-doc.md) | — | — |

## Workflow

```text
Chọn prompt  →  Copy prompt  →  Sửa phần <<<< >>>>  →  Paste vào AI agent
                                                     ↓
                                              AI tạo document
                                                     ↓
                                           Review + chỉnh sửa
                                                     ↓
                                              make lint (verify)
                                                     ↓
                                              Commit + PR
```

## Tips

- **Thêm context:** Đính kèm thông tin hệ thống, config, logs khi paste prompt — AI sẽ tạo doc chính xác hơn
- **Review luôn:** AI tạo draft tốt nhưng bạn cần verify thông tin kỹ thuật (IP, commands, thông số)
- **Iterate:** Nếu output chưa đúng ý, yêu cầu AI sửa cụ thể — không cần chạy lại từ đầu

---

> **Version:** 4.0.0 | **Updated:** 2026-03-30
