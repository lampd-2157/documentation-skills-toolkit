# Diátaxis Framework Mapping

> Map giữa Documentation Skills Toolkit và Diátaxis framework — giúp teams hiểu cách organize documentation theo chuẩn quốc tế.
>
> Source: [Diátaxis](https://diataxis.fr/) — Được adopt bởi Python, Canonical, Django, NumPy

---

## Diátaxis là gì?

Framework chia documentation thành 4 quadrants dựa trên 2 trục:

- **Practical ↔ Theoretical** (hành động vs hiểu biết)
- **Learning ↔ Working** (đang học vs đang làm)

```text
                  LEARNING                    WORKING
            ┌─────────────────┬─────────────────┐
PRACTICAL   │   TUTORIALS     │   HOW-TO GUIDES │
            │   (learning by  │   (task-focused  │
            │    doing)        │    instructions) │
            ├─────────────────┼─────────────────┤
THEORETICAL │  EXPLANATION     │   REFERENCE      │
            │  (understanding  │   (specifications │
            │   context)       │    & lookup)      │
            └─────────────────┴─────────────────┘
```

## Mapping: Toolkit → Diátaxis

| Diátaxis Quadrant | Toolkit Skill | Templates | Ví dụ |
|---|---|---|---|
| **Tutorials** (learning by doing) | `training-doc-writer.md` | T4 Training, T11 Knowledge Check | Onboarding module, Git basics training |
| **How-to Guides** (task-focused) | `project-doc-writer.md` | T3 How-to Guide | Setup Google Workspace, Deploy to staging |
| **Reference** (lookup/specs) | `ops-runbook-writer.md` | T1 Runbook, T5 Network Topology | Server inventory, VLAN layout, firewall rules |
| **Explanation** (understanding) | `project-doc-writer.md` | T2 ADR, T9 MADR, T10 Lightweight ADR | Architecture decisions, technical specs |

### Cross-cutting Skills

| Skill | Diátaxis Role |
|---|---|
| `docs-engineer.md` | **Foundation** — setup platform cho tất cả quadrants |
| `infra-security-doc.md` | **Reference + How-to** — security policies (reference) + hardening guides (how-to) |

## Khi nào dùng quadrant nào?

Decision tree:

```text
User cần documentation
  ├── Đang HỌC (learning)?
  │     ├── Cần LÀM theo (hands-on)?
  │     │     └── TUTORIAL → training-doc-writer + T4
  │     └── Cần HIỂU tại sao (context)?
  │           └── EXPLANATION → project-doc-writer + T2 ADR
  └── Đang LÀM VIỆC (working)?
        ├── Cần hoàn thành 1 task cụ thể?
        │     └── HOW-TO → project-doc-writer + T3
        └── Cần tra cứu thông tin?
              └── REFERENCE → ops-runbook-writer + T1/T5
```

## Best Practices

### DO

- Tách documentation theo quadrant — KHÔNG mix tutorial với reference trong 1 file
- Bắt đầu từ How-to (most common) → rồi mở rộng sang Tutorial + Reference
- Dùng cross-links giữa quadrants ("Xem thêm: [Tutorial]", "Reference: [Runbook]")

### DON'T

- Viết "Explanation" cho mọi thứ — chỉ khi context thực sự cần thiết
- Mix "Tutorial" với "How-to" — Tutorial = learning journey, How-to = task completion
- Bỏ qua "Reference" — đây là doc type được dùng nhiều nhất khi on-call

---

> **Version:** 4.0.0 | **Updated:** 2026-03-30
