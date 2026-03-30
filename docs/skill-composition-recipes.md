# Skill Composition Recipes

> Hướng dẫn kết hợp skills khi thực hiện task thực tế. Real-world tasks thường cần **nhiều hơn 1 skill**.
>
> **v5.0.0 — Smart Routing:** Các recipes đã được tự động hóa trong
> [`config/routing-signals.yaml`](../config/routing-signals.yaml) — AI agent tự chọn skill + composition rule.
> File này hữu ích cho manual path hoặc muốn hiểu reasoning đằng sau.

---

## Nguyên tắc Composition

1. **`docs-engineer` là foundation** — Mọi task documentation đều cần markdown standards + MkDocs setup
2. **1 skill = 1 domain** — Không cố nhồi mọi thứ vào 1 skill
3. **Primary skill quyết định structure** — Secondary skill bổ sung quality/format
4. **Template trước, skill sau** — Copy template (T1-T11) rồi dùng skill để customize

---

## Recipes

### R1: Setup Documentation Project từ đầu

| Field | Value |
|-------|-------|
| **Primary** | `docs-engineer.md` |
| **Secondary** | — |
| **Templates** | `mkdocs-starter.yml`, `markdownlint.json` |

**Steps:**

1. Setup MkDocs project (`docs-engineer` §1)
2. Tạo folder structure (`docs-engineer` §3.1)
3. Configure markdownlint (`docs-engineer` §2.2)
4. Setup CI/CD (`docs-lifecycle.md` Phase 4)

---

### R2: Viết Runbook cho hệ thống mới

| Field | Value |
|-------|-------|
| **Primary** | `ops-runbook-writer.md` |
| **Secondary** | `docs-engineer.md` |
| **Templates** | T1 (Runbook) |

**Steps:**

1. Copy T1 Runbook template
2. Viết content theo `ops-runbook-writer` §1 (Overview, Health Checks, Common Tasks, Troubleshooting, Escalation)
3. Thêm Mermaid diagrams (`docs-engineer` §4.3)
4. Verify markdown standards (`docs-engineer` §2)

---

### R3: Tạo Onboarding / Training docs cho team

| Field | Value |
|-------|-------|
| **Primary** | `training-doc-writer.md` |
| **Secondary** | `docs-engineer.md` |
| **Templates** | T4 (Training Module) |

**Steps:**

1. Define audience + prerequisites (`training-doc-writer` §1.1)
2. Copy T4 Training template
3. Viết lessons + hands-on labs (`training-doc-writer` §1)
4. Tạo onboarding checklist (`training-doc-writer` §1.2)
5. Design learning path (`training-doc-writer` §1.3)

---

### R4: Document Network Infrastructure

| Field | Value |
|-------|-------|
| **Primary** | `ops-runbook-writer.md` |
| **Secondary** | `docs-engineer.md` |
| **Templates** | T5 (Network Topology) |

**Steps:**

1. Copy T5 Network template
2. Vẽ topology diagram — Mermaid (`ops-runbook-writer` §3.1)
3. Điền VLAN layout, firewall rules, certificate matrix (`ops-runbook-writer` §3)
4. Verify Mermaid renders đúng (`docs-engineer` §4.3)

---

### R5: Post-Incident Postmortem

| Field | Value |
|-------|-------|
| **Primary** | `ops-runbook-writer.md` |
| **Secondary** | `project-doc-writer.md` |
| **Templates** | T6 (Incident Postmortem) |

**Steps:**

1. Copy T6 Postmortem template
2. Điền timeline + root cause (`ops-runbook-writer` §4)
3. Viết "Lessons Learned" dưới dạng how-to guide (`project-doc-writer` §2)
4. Tạo action items + prevention rules

---

### R6: Architecture Decision Record

| Field | Value |
|-------|-------|
| **Primary** | `project-doc-writer.md` |
| **Secondary** | — |
| **Templates** | T2 (ADR) |

**Steps:**

1. Copy T2 ADR template
2. Follow ADR structure (`project-doc-writer` §1.1)
3. Document alternatives considered (pros/cons table)
4. Record consequences + risks

---

### R7: Maintenance Window Planning

| Field | Value |
|-------|-------|
| **Primary** | `ops-runbook-writer.md` |
| **Secondary** | — |
| **Templates** | T7 (Maintenance Window) |

**Steps:**

1. Copy T7 Maintenance template
2. Follow maintenance structure (`ops-runbook-writer` §4.2)
3. Viết pre-checks, steps, rollback, post-checks
4. Verify mọi command đã test (`ops-runbook-writer` Iron Law)

---

### R8: Version Release Notes

| Field | Value |
|-------|-------|
| **Primary** | `project-doc-writer.md` |
| **Secondary** | — |
| **Templates** | T8 (Release Notes) |

**Steps:**

1. Copy T8 Release Notes template
2. List features, bug fixes, breaking changes
3. Viết upgrade instructions dạng step-by-step (`project-doc-writer` §2)

---

### R9: Full Documentation Site cho team mới

| Field | Value |
|-------|-------|
| **Primary** | `docs-engineer.md` |
| **Secondary** | `ops-runbook-writer.md` + `training-doc-writer.md` + `project-doc-writer.md` |
| **Templates** | All (T1-T11) |

**Steps:**

1. Setup MkDocs + folder structure (`docs-engineer` §1, §3)
2. Dùng `infra-knowledge-base.md` để tạo domain folders
3. Viết runbooks cho critical systems (`ops-runbook-writer`)
4. Viết onboarding + training (`training-doc-writer`)
5. Setup CI/CD auto-deploy (`docs-lifecycle.md`)
6. Quarterly audit schedule (`docs-lifecycle.md` Phase 5)

---

### R10: API Reference + Security Review

| Field | Value |
|-------|-------|
| **Primary** | `api-doc-writer.md` |
| **Secondary** | `infra-security-doc.md` |
| **Templates** | T13 (API Reference) + T14 (Security Policy) |

**Steps:**

1. Document API endpoints, request/response examples (`api-doc-writer` §1-§3)
2. Add authentication section with security best practices (`infra-security-doc` §1)
3. Document rate limiting + abuse prevention
4. Add security checklist for API changes (`infra-security-doc` §5)
5. Review: mỗi endpoint có auth + error codes + rate limits

**When to use:** Khi API expose ra external hoặc cần PCI/SOC2 compliance. Internal-only API chỉ cần R10 step 1-3.

---

### R11: Architecture Diagram + ADR

| Field | Value |
|-------|-------|
| **Primary** | `project-doc-writer.md` |
| **Secondary** | `docs-engineer.md` |
| **Templates** | T12 (Architecture Diagram) + T2/T9 (ADR) |

**Steps:**

1. Tạo architecture diagram trước (`project-doc-writer`, template T12)
2. Viết ADR cho mỗi major architecture decision — reference diagram (`project-doc-writer`, template T2/T9)
3. Cross-link: ADR → diagram section, diagram → ADR list
4. Ensure Mermaid diagrams render trong MkDocs (`docs-engineer` §2)
5. Review: mỗi component trong diagram có ADR giải thích "why"

**When to use:** Khi setup hệ thống mới hoặc major refactor. Diagram giúp team hình dung tổng quan, ADR giải thích reasoning.

---

## Quick Lookup

| Task | Skills needed | Template |
|------|--------------|----------|
| Setup docs project | docs-engineer | mkdocs-starter.yml |
| Write runbook | ops-runbook + docs-engineer | T1 |
| Create training | training-doc + docs-engineer | T4 |
| Document network | ops-runbook + docs-engineer | T5 |
| Post-incident review | ops-runbook + project-doc | T6 |
| Architecture decision | project-doc | T2 |
| How-to guide | project-doc + docs-engineer | T3 |
| Plan maintenance | ops-runbook | T7 |
| Release notes | project-doc | T8 |
| Security policy | infra-security-doc | — |
| Access control matrix | infra-security-doc | — |
| Security review | infra-security-doc + ops-runbook | T14 |
| API docs + security | api-doc + infra-security-doc | T13 + T14 |
| Architecture + ADR | project-doc + docs-engineer | T12 + T2/T9 |
| Full docs site | All 6 skills | All templates |

---
