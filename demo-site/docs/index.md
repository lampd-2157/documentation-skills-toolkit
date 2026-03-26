---
title: Infrastructure Documentation
description: "Tài liệu hạ tầng — demo Documentation Skills Toolkit"
status: approved
updated: 2026-03-26
---

<div class="hero" markdown>

# :material-book-open-variant: Infrastructure Documentation

<p class="subtitle">Tài liệu vận hành, hướng dẫn, và training cho team — powered by Documentation Skills Toolkit</p>

<div class="badges">
  <span class="badge status-approved">:material-check-circle: Production Ready</span>
  <span class="badge status-approved">:material-file-document: 8 Templates</span>
  <span class="badge status-approved">:material-auto-fix: Auto Lint</span>
</div>

</div>

---

## :material-compass: Quick Navigation

<div class="grid-cards" markdown>

<div class="card" markdown>

### :material-rocket-launch: Getting Started

Setup MkDocs cho project mới trong 15 phút

[:octicons-arrow-right-24: Quick Start](getting-started/quick-start.md)

</div>

<div class="card" markdown>

### :material-server: Operations

Runbooks, network docs, incident response, maintenance

[:octicons-arrow-right-24: Runbooks](operations/runbooks/proxmox-vm-runbook.md)

</div>

<div class="card" markdown>

### :material-source-branch: Development

Architecture decisions, release notes, tech specs

[:octicons-arrow-right-24: ADR](development/adr/adr-001-mkdocs.md)

</div>

<div class="card" markdown>

### :material-school: Training

Onboarding modules, hands-on labs cho team members

[:octicons-arrow-right-24: Git Basics](training/training-module-example.md)

</div>

<div class="card" markdown>

### :material-book-open-page-variant: Guides

Step-by-step how-to guides cho common tasks

[:octicons-arrow-right-24: How-to Guides](guides/how-to/google-workspace-new-user.md)

</div>

</div>

---

## :material-file-document-multiple: All Examples (T1-T8)

Demo site này chứa ví dụ thực tế cho tất cả **8 document templates**:

| | Template | Example | Skill |
|---|----------|---------|-------|
| :material-book-cog: | **T1 Runbook** | [Proxmox VM Management](operations/runbooks/proxmox-vm-runbook.md) | ops-runbook-writer |
| :material-file-tree: | **T2 ADR** | [Why MkDocs-Material](development/adr/adr-001-mkdocs.md) | training-guide-writer |
| :material-list-status: | **T3 How-to** | [Google Workspace New User](guides/how-to/google-workspace-new-user.md) | training-guide-writer |
| :material-school-outline: | **T4 Training** | [Git Basics for New Members](training/training-module-example.md) | training-guide-writer |
| :material-lan: | **T5 Network** | [Demo Lab Network Topology](operations/network-topology-example.md) | ops-runbook-writer |
| :material-alert-circle: | **T6 Postmortem** | [DB Connection Pool Exhaustion](operations/postmortem-example.md) | ops-runbook-writer |
| :material-wrench-clock: | **T7 Maintenance** | [PostgreSQL 15 → 16 Upgrade](operations/maintenance-window-example.md) | ops-runbook-writer |
| :material-tag: | **T8 Release Notes** | [v2.5.0 Release](development/release-notes-example.md) | training-guide-writer |

---

## :material-lightbulb: About This Site

!!! tip "Built with Documentation Skills Toolkit"
    Site này là **demo output** khi áp dụng bộ [Documentation Skills Toolkit](https://github.com/lampd-2157/documentation-skills-toolkit). Mỗi trang tương ứng với 1 template (T1-T8), viết theo skill guidelines.

!!! info "Tech Stack"
    - **Platform:** [MkDocs-Material](https://squidfunk.github.io/mkdocs-material/) — theme + components
    - **Diagrams:** [Mermaid](https://mermaid.js.org/) — flowcharts, topology, sequence diagrams
    - **Quality:** markdownlint + cspell — auto-lint on commit
    - **Deploy:** GitHub Pages via `mkdocs gh-deploy`

!!! example "Try It Yourself"
    ```bash
    # Clone toolkit
    git clone https://github.com/lampd-2157/documentation-skills-toolkit.git
    cd documentation-skills-toolkit

    # Create your first doc
    ./scripts/docs-toolkit new runbook "My Service"
    ```
