# Prompt: Review Document

> Dùng để review và chấm điểm chất lượng tài liệu theo quality scorecard.

## Cách dùng

### AI Agent (Recommended)

1. Copy toàn bộ nội dung trong khung **Prompt** bên dưới
2. Mở AI agent bạn đang dùng (Claude, ChatGPT, Antigravity, Copilot...)
3. Paste prompt vào, sau đó **sửa dòng "Đọc file cần review:"** — thay đường dẫn ví dụ bằng file thực tế cần review
4. Gửi prompt → AI review và chấm điểm → bạn xem kết quả

**Ví dụ thực tế:** Nếu bạn cần review runbook vừa viết, sửa thành:

```text
Bước 2: Đọc file cần review:
docs/operations/runbooks/redis-cluster-runbook.md
```

### Manual

Đọc [docs/doc-quality-scorecard.md](../docs/doc-quality-scorecard.md) → tự chấm điểm từng tiêu chí (0/0.5/1).

---

## Prompt

```text
Bạn là Documentation Reviewer. Hãy review tài liệu theo quality scorecard.

Bước 1: Đọc file docs/doc-quality-scorecard.md để hiểu 10 tiêu chí chấm điểm.
Bước 2: Đọc file cần review:
docs/operations/runbooks/nginx-load-balancer-runbook.md
<<<< SỬA ĐƯỜNG DẪN NÀY THÀNH FILE CẦN REVIEW >>>>

Bước 3: Chấm điểm từng tiêu chí (0 / 0.5 / 1 điểm):

1. Structure — đúng template, heading hierarchy
2. Commands — code blocks có language tag, copy-paste ready
3. Prerequisites — liệt kê đầy đủ
4. Metadata — YAML frontmatter có title + status
5. Visual & UI/UX — admonitions cho metadata/warnings, task lists, diagrams, code blocks cho long commands
6. Metadata — YAML frontmatter có title + status
7. Markdown quality — không trailing spaces, đúng format
8. Freshness — date cập nhật trong 90 ngày
9. Audience clarity — rõ viết cho ai
10. Tested — có vẻ đã được test bởi người không viết

Bước 4: Tổng kết:
- Tổng điểm: X/10
- Điểm mạnh (2-3 điểm)
- Cần cải thiện (2-3 điểm, kèm gợi ý sửa cụ thể)
```
