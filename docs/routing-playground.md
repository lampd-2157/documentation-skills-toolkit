# Routing Playground — Test Smart Routing

> Test hệ thống Smart Routing bằng cách nhập mô tả tự nhiên và xem AI chọn skill/template nào.

## Cách sử dụng

### CLI Mode

```bash
# Phân tích routing cho 1 mô tả
./scripts/docs-toolkit route "viết API docs cho payment service"

# JSON output (cho integration)
python3 scripts/route_analyzer.py --json "tạo runbook cho nginx"
```

### Wizard Mode (Interactive)

```bash
# Wizard hỏi 4 câu → routing → tạo doc
./scripts/docs-toolkit wizard
```

### Makefile shortcuts

```bash
make route DESC="viết postmortem cho DB crash hôm qua"
make wizard
```

---

## Ví dụ Routing

Thử các mô tả sau để hiểu cách routing hoạt động:

### High Confidence (>= 0.8) — Auto-select

| Input | Expected Skill | Template |
|-------|---------------|----------|
| "viết runbook cho Redis cluster" | ops-runbook-writer | T1 |
| "tạo ADR cho việc chuyển sang PostgreSQL" | project-doc-writer | T2 |
| "viết training module về Docker basics" | training-doc-writer | T4 |
| "tạo API reference cho User Management API" | api-doc-writer | T13 |
| "viết security policy cho access control" | infra-security-doc | T14 |

### Medium Confidence (0.5-0.8) — AI gợi ý + hỏi confirm

| Input | Possible Skills | Lý do |
|-------|----------------|-------|
| "document hệ thống mới" | project-doc-writer / docs-engineer | Chung chung, cần context |
| "viết hướng dẫn deploy" | project-doc-writer / ops-runbook-writer | Có thể howto hoặc runbook |

### Composition Rules — Nhiều skills kết hợp

| Input | Primary | Secondary |
|-------|---------|-----------|
| "runbook cho hệ thống có security requirements" | ops-runbook-writer | infra-security-doc |
| "how-to guide với server commands" | project-doc-writer | ops-runbook-writer |
| "training có lab với real infrastructure" | training-doc-writer | ops-runbook-writer |

---

## Cách hoạt động

```text
User input
  │
  ▼
routing-signals.yaml   ← keyword definitions + confidence base
  │
  ▼
Keyword matching       ← mỗi keyword match = +0.1 confidence
  │
  ▼
Composition check      ← nếu match >= 2 skills → apply composition rule
  │
  ▼
Confidence scoring
  ├── >= 0.8  → Auto-select skill
  ├── 0.5-0.8 → Gợi ý + hỏi confirm
  └── < 0.5   → Dùng prompts/select-skill.md
```

## Config files

| File | Mục đích |
|------|----------|
| [config/routing-signals.yaml](../config/routing-signals.yaml) | Keywords, confidence base, composition rules |
| [config/routing-feedback.yaml](../config/routing-feedback.yaml) | Feedback log — track routing accuracy |
| [scripts/route_analyzer.py](../scripts/route_analyzer.py) | Routing engine |

## Feedback Loop

Sau khi routing chọn skill, bạn có thể log feedback để cải thiện:

```yaml
# config/routing-feedback.yaml
feedback:
  - date: 2026-03-30
    input: "viết runbook cho Redis"
    suggested: ops-runbook-writer
    actual: ops-runbook-writer
    correct: true
```

Feedback giúp tune confidence scores theo thời gian.
