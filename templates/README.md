# Document Templates

> Copy-paste templates cho mỗi loại tài liệu. Chọn template → customize → deploy.
>
> Sources: [SkeltonThatcher/run-book-template](https://github.com/SkeltonThatcher/run-book-template), [Google Style Guide](https://developers.google.com/style), [gitlab.com/tgdp/templates](https://gitlab.com/tgdp/templates)

| #  | Template | File | Use Case | Related Skill |
|----|----------|------|----------|---------------|
| T1 | Runbook | [runbook.md](runbook.md) | System operation procedures | ops-runbook-writer.md |
| T2 | ADR | [adr.md](adr.md) | Design decisions log | project-doc-writer.md |
| T3 | How-to Guide | [howto-guide.md](howto-guide.md) | Step-by-step instructions | project-doc-writer.md |
| T4 | Training Module | [training-module.md](training-module.md) | Internal training | training-doc-writer.md |
| T5 | Network Topology | [network-topology.md](network-topology.md) | Network documentation | ops-runbook-writer.md |
| T6 | Incident Postmortem | [incident-postmortem.md](incident-postmortem.md) | Post-incident learning | ops-runbook-writer.md |
| T7 | Maintenance Window | [maintenance-window.md](maintenance-window.md) | Planned change request | ops-runbook-writer.md |
| T8 | Release Notes | [release-notes.md](release-notes.md) | Version release summary | project-doc-writer.md |
| T9 | ADR (MADR) | [adr-madr.md](adr-madr.md) | Complex decisions, structured evaluation | project-doc-writer.md |
| T10 | ADR (Lightweight) | [adr-lightweight.md](adr-lightweight.md) | Quick decisions, POC, experiments | project-doc-writer.md |
| T11 | Knowledge Check | [knowledge-check.md](knowledge-check.md) | Training assessment & validation | training-doc-writer.md |
| T12 | Architecture Diagram | [architecture-diagram.md](architecture-diagram.md) | System architecture visualization | project-doc-writer.md |
| T13 | API Reference | [api-reference.md](api-reference.md) | REST/GraphQL/gRPC API documentation | api-doc-writer.md |
| T14 | Security Policy | [security-policy.md](security-policy.md) | Security policy with enforcement | infra-security-doc.md |

> **CLI scaffold:** `./scripts/docs-toolkit new <type> <title>`
>
> **ADR format guide:** [adr-catalog.md](../docs/adr-catalog.md) — khi nào dùng T2 vs T9 vs T10
