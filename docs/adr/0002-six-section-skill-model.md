# ADR-0002: Six-Section Skill Model

| Field | Value |
|-------|-------|
| **Status** | Accepted |
| **Date** | 2026-03-26 |
| **Author** | DulapReal |

## Context

Cần chuẩn hóa cấu trúc skill files. Mỗi skill phải consistent, dễ parse bởi validator, dễ đọc bởi cả human và AI agent.

## Decision

Áp dụng 6-section model bắt buộc cho mọi skill:

1. Context / Bối cảnh (metadata + narrative)
2. THE IRON LAW (1 rule tối thượng)
3. Guardrails (2-5 proactive checks)
4. Red Flags — STOP (3-6 reactive warnings)
5. Remember (≤6 rules summary)
6. Related Skills (≤5 cross-references)

## Consequences

- **Positive:** Consistent structure, automated validation, AI-parseable
- **Negative:** Rigid — mọi skill phải fit vào 6 sections
- **Risks:** Complex skills (security, ops) có thể vượt size limits
