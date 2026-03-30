# Document Quality Scorecard

> Đánh giá chất lượng documentation một cách khách quan. Dùng cho self-review, peer review, và quarterly audit.

---

## Scoring Rubric

Mỗi tiêu chí cho điểm **0 / 0.5 / 1**. Tổng điểm tối đa: **10**.

| #  | Criteria | 0 (Fail) | 0.5 (Partial) | 1 (Pass) |
|----|----------|----------|---------------|----------|
| 1  | **Structure** | Không có sections rõ ràng | Có sections nhưng thiếu/sai thứ tự | Đầy đủ template structure |
| 2  | **Commands testable** | Không có commands / untested | Có commands nhưng thiếu expected output | Mọi command copy-paste ready + expected output |
| 3  | **Prerequisites** | Không list prerequisites | List chưa đầy đủ | Đầy đủ với versions + links |
| 4  | **Expected results** | Không có expected result | Một số steps có result | Mọi step có expected result |
| 5  | **Visual & UI/UX** | Không có diagram, plain text | Có diagram HOẶC admonitions (chưa đầy đủ) | Admonitions cho metadata/warnings, task lists cho checklists, diagrams/visual aids |
| 6  | **Metadata** | Không có YAML header | YAML header thiếu fields | Đầy đủ: title, status, updated, tags |
| 7  | **Markdown quality** | Lint errors > 5 | Lint errors 1-5 | markdownlint passes, 0 errors |
| 8  | **Freshness** | Updated > 6 tháng trước | Updated 3-6 tháng trước | Updated trong 90 ngày |
| 9  | **Audience clarity** | Không specify audience | Audience mơ hồ | Explicit audience + difficulty level |
| 10 | **Non-author tested** | Chưa ai test | Chỉ author self-review | Tested bởi non-author successfully |

---

## Scoring Tiers

| Score | Tier | Action |
|-------|------|--------|
| **9-10** | Excellent | Ship it. Quarterly review chỉ cần format check |
| **7-8** | Good | Minor improvements needed. Fix trước khi publish |
| **5-6** | Needs Improvement | Significant gaps. Rewrite weak sections |
| **< 5** | Rewrite Required | Viết lại từ đầu theo template chuẩn |

---

## Cách sử dụng

### Self-Review (trước khi tạo PR)

1. Mở scorecard này
2. Chấm điểm từng tiêu chí cho doc của bạn
3. Ghi score vào PR description
4. Fix mọi tiêu chí < 0.5 trước khi submit

### Peer Review (khi review PR)

1. Reviewer chấm điểm theo scorecard
2. Comment score + tiêu chí cần cải thiện
3. Approve nếu score >= 7
4. Request changes nếu score < 7

### Quarterly Audit

1. List tất cả docs trong `docs/`
2. Chấm điểm mỗi doc
3. Sort by score ascending
4. Docs score < 5 → rewrite priority
5. Docs score 5-6 → improvement sprint
6. Report: average score, trend, worst docs

---

## Scorecard Template (copy-paste)

```markdown
## Doc Quality Score: [doc-name.md]

| # | Criteria | Score | Note |
|---|----------|-------|------|
| 1 | Structure | _/1 | |
| 2 | Commands testable | _/1 | |
| 3 | Prerequisites | _/1 | |
| 4 | Expected results | _/1 | |
| 5 | Visual & UI/UX | _/1 | |
| 6 | Metadata | _/1 | |
| 7 | Markdown quality | _/1 | |
| 8 | Freshness | _/1 | |
| 9 | Audience clarity | _/1 | |
| 10 | Non-author tested | _/1 | |
| **Total** | | **_/10** | |

**Tier:** [Excellent/Good/Needs Improvement/Rewrite]
**Reviewer:** [name] | **Date:** [YYYY-MM-DD]
```

---

## Tips

- **Score thấp nhất thường là #10 (non-author test)** — Đây cũng là tiêu chí quan trọng nhất. Hãy pair-review docs.
- **#2 và #4 liên quan chặt** — Nếu commands không testable thì expected results cũng sẽ thiếu.
- **#8 (Freshness) là automatic** — Setup quarterly audit script:

  ```bash
  find docs/ -name "*.md" -mtime +90 -type f | sort
  ```

- **#5 (Visual & UI/UX) mới gộp** — Bao gồm cả diagrams VÀ admonitions/task lists/code blocks formatting.
- **Aim for 8+** — Score 7 là minimum acceptable cho production docs.

---
