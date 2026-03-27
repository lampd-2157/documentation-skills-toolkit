# Training Assessment Guide — Thiết kế đánh giá hiệu quả

> Hướng dẫn thiết kế assessment cho training modules. Áp dụng Bloom's Taxonomy để đảm bảo đánh giá đúng level kiến thức và kỹ năng.

---

## 1. Bloom's Taxonomy Mapping

Mỗi level trong Bloom's Taxonomy tương ứng với loại câu hỏi phù hợp:

| Level | Mô tả | Question Type | Ví dụ |
|-------|--------|---------------|-------|
| **Remember** (Nhớ) | Recall facts, terms, concepts | Multiple choice, True/False | "Docker image và container khác nhau thế nào?" |
| **Understand** (Hiểu) | Explain ideas, summarize | Short answer, Explain in your own words | "Giải thích tại sao cần dùng multi-stage build trong Dockerfile" |
| **Apply** (Áp dụng) | Use knowledge in new situations | Hands-on lab, Command exercises | "Viết Dockerfile cho một Node.js app với multi-stage build" |
| **Analyze** (Phân tích) | Break down, compare, contrast | Scenario-based, Troubleshooting | "Given: container restart loop — phân tích log và xác định root cause" |
| **Evaluate** (Đánh giá) | Justify decisions, critique | Peer review, Design review | "Review Dockerfile này và đề xuất cải thiện về security + performance" |
| **Create** (Sáng tạo) | Design new solutions, produce | Project-based, Architecture design | "Thiết kế CI/CD pipeline cho microservices với Docker Compose" |

> **Nguyên tắc:** Training nên cover ít nhất 3 levels đầu (Remember → Apply). Advanced training nên reach Analyze hoặc cao hơn.

---

## 2. Assessment Types — Các loại đánh giá

### 2.1 Knowledge Check

- **Mục đích:** Verify learner nhớ và hiểu concepts
- **Format:** Multiple choice, True/False, short answer
- **Bloom's Level:** Remember, Understand
- **Khi nào dùng:** Sau mỗi lesson hoặc module
- **Template:** → [knowledge-check.md](../templates/knowledge-check.md)

### 2.2 Practical Lab

- **Mục đích:** Verify learner có thể áp dụng kiến thức
- **Format:** Step-by-step tasks với expected output
- **Bloom's Level:** Apply, Analyze
- **Khi nào dùng:** Sau phần theory, khi cần hands-on verification
- **Yêu cầu:** Mỗi step phải có expected result rõ ràng

### 2.3 Peer Review

- **Mục đích:** Develop critical thinking và evaluation skills
- **Format:** Review work của người khác, provide feedback
- **Bloom's Level:** Evaluate
- **Khi nào dùng:** Advanced training, team collaboration exercises
- **Yêu cầu:** Rubric rõ ràng để reviewer biết đánh giá theo tiêu chí nào

### 2.4 Scenario Test

- **Mục đích:** Test khả năng xử lý tình huống thực tế
- **Format:** Given → When → Expected structure
- **Bloom's Level:** Analyze, Evaluate, Create
- **Khi nào dùng:** Final assessment, certification
- **Yêu cầu:** Scenario phải realistic, dựa trên real-world cases

---

## 3. Pass/Fail Criteria Design — Thiết kế ngưỡng đạt/không đạt

### Cách đặt threshold

| Assessment Type   | Recommended Pass Score | Lý do                                      |
| ----------------- | ---------------------- | ------------------------------------------- |
| Knowledge Check   | ≥80%                   | Cho phép sai 1-2 câu lý thuyết             |
| Practical Lab     | 100%                   | Mọi step phải pass — partial = không an toàn |
| Peer Review       | ≥70%                   | Subjective hơn, cần flexibility             |
| Scenario Test     | ≥80%                   | Critical thinking — cho phép minor gaps     |

### Quy trình khi FAIL

1. **Identify gaps** — Xác định learner thiếu kiến thức ở đâu
2. **Provide resources** — Gợi ý tài liệu bổ sung cho phần yếu
3. **Retry window** — Cho phép thi lại sau 3-5 ngày
4. **Escalate** — Nếu fail lần 2, mentor 1-on-1 review

---

## 4. Competency Tracking — Theo dõi năng lực

### Competency Matrix Template

| Skill | Beginner | Intermediate | Advanced | Expert |
|-------|----------|-------------|----------|--------|
| [Skill 1] | Hiểu concept cơ bản | Áp dụng được trong task thường ngày | Xử lý edge cases, optimize | Thiết kế solution, mentor others |
| [Skill 2] | Biết dùng basic commands | Viết scripts, automate | Troubleshoot complex issues | Architect systems, define standards |
| [Skill 3] | Đọc hiểu documentation | Viết documentation | Review & improve docs | Define doc standards cho team |

### Progression Path

```text
Beginner (Month 1-2)
  │  Assessment: Knowledge Check ≥80%
  ▼
Intermediate (Month 3-4)
  │  Assessment: Practical Lab 100% + Knowledge Check ≥80%
  ▼
Advanced (Month 5-8)
  │  Assessment: Scenario Test ≥80% + Peer Review ≥70%
  ▼
Expert (Month 9+)
  │  Assessment: Design project + Mentor evaluation
  ▼
  Can mentor others, define standards
```

### Tracking Method

- **Per-module:** Ghi nhận pass/fail cho từng module
- **Per-skill:** Map module results vào competency matrix
- **Quarterly review:** Manager + learner review progression together

---

## 5. Best Practices — DOs and DON'Ts

### ✅ 5 DOs

1. **DO align with Bloom's Taxonomy** — Match question type với learning objective level
2. **DO include hands-on verification** — Lý thuyết alone không đủ, phải có practical proof
3. **DO set clear pass criteria TRƯỚC khi training** — Learner biết expectation từ đầu
4. **DO provide retake opportunities** — Fail lần đầu là cơ hội học, không phải punishment
5. **DO review assessments quarterly** — Update câu hỏi khi tools/processes thay đổi

### ❌ 5 DON'Ts

1. **DON'T test memorization only** — Avoid chỉ hỏi "what is X?" — hãy hỏi "when would you use X?"
2. **DON'T skip scenario-based questions** — Real-world application quan trọng hơn textbook knowledge
3. **DON'T set pass score 100% cho theory** — Không realistic, gây stress không cần thiết
4. **DON'T reuse exact same questions** — Learner sẽ share answers, assessment mất giá trị
5. **DON'T assess without feedback** — Mỗi wrong answer cần explanation tại sao sai và đáp án đúng

---

> 📖 **Related:** [Knowledge Check Template](../templates/knowledge-check.md) | [Training Doc Writer Skill](../skills/training-doc-writer.md)
