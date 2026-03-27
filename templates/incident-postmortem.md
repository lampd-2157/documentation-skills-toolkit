<!-- Template T6: Incident Postmortem — Copy this file and customize -->
# Postmortem: [Incident Title]

| Field        | Value             |
| ------------ | ----------------- |
| **Severity** | P1 / P2 / P3      |
| **Date**     | YYYY-MM-DD        |
| **Duration** | HH:MM start → end |
| **Impact**   | [users/services]  |
| **Owner**    | [incident lead]   |
| **Status**   | Draft / Reviewed  |
| **Failure Category** | Config / Hardware / Resource / Time / Database / Cascading / Other |

## Summary
[1-2 sentences: what happened and impact]

## Timeline
| Time (UTC+7) | Event              | Actor |
| ------------ | ------------------ | ----- |
| HH:MM        | [first detection]  | [who] |
| HH:MM        | [escalation]       | [who] |
| HH:MM        | [fix applied]      | [who] |
| HH:MM        | [service restored] | [who] |

## Root Cause
[Detailed analysis of why it happened]

## What Went Wrong
- [thing 1]
- [thing 2]

## What Went Right
- [thing 1]
- [thing 2]

## Action Items
| #   | Action                  | Owner  | Due Date   | Status |
| --- | ----------------------- | ------ | ---------- | ------ |
| 1   | [fix/prevention action] | [name] | YYYY-MM-DD | Open   |

## SLA Impact

| Metric              | Target   | Actual   | Breach? |
| ------------------- | -------- | -------- | ------- |
| Uptime              | 99.9%    | [actual] | Yes/No  |
| Response time (p95) | < 500ms  | [actual] | Yes/No  |
| Error rate          | < 0.1%   | [actual] | Yes/No  |
| Recovery time (RTO) | < 1 hour | [actual] | Yes/No  |

## Lessons Learned
- [lesson 1]
- [lesson 2]

## Blameless Retro Principles

- **Không blame cá nhân** — focus vào system & process, không phải người gây ra lỗi
- **Assume good intent** — mọi người đều hành động dựa trên thông tin tốt nhất họ có tại thời điểm đó
- **Tập trung vào "how" không phải "who"** — hỏi "hệ thống cho phép lỗi này xảy ra thế nào?" thay vì "ai gây ra lỗi?"
- **Chia sẻ openly** — postmortem chỉ có giá trị khi mọi người dám nói thật về những gì đã xảy ra
- **Action items phải systemic** — fix phải ở level hệ thống (automation, guardrails, monitoring) — không phải "nhắc nhở cẩn thận hơn"

> 📖 **Failure patterns guide** → [incident-patterns.md](../docs/incident-patterns.md)
