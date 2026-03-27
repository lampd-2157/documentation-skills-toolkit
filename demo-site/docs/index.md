---
title: Infrastructure Documentation
description: "Tài liệu hạ tầng — demo Documentation Skills Toolkit"
status: approved
updated: 2026-03-26
hide:
  - toc
  - navigation
---

<div class="hero-banner">
  <div class="hero-pattern"></div>
  <h1>Infrastructure Documentation</h1>
  <p class="hero-subtitle">Tài liệu vận hành, hướng dẫn, và training cho team<br>Powered by Documentation Skills Toolkit</p>
  <div class="hero-badges">
    <span class="hero-badge">&#10003; Production Ready</span>
    <span class="hero-badge">&#128196; 11 Templates</span>
    <span class="hero-badge">&#9881; Auto Lint</span>
    <span class="hero-badge">&#127793; Docs-as-Code</span>
  </div>
</div>

<div class="stats-bar">
  <div class="stat">
    <div class="stat-value">11</div>
    <div class="stat-label">Templates</div>
  </div>
  <div class="stat">
    <div class="stat-value">5</div>
    <div class="stat-label">Skills</div>
  </div>
  <div class="stat">
    <div class="stat-value">12</div>
    <div class="stat-label">Examples</div>
  </div>
  <div class="stat">
    <div class="stat-value">12</div>
    <div class="stat-label">Docs</div>
  </div>
</div>

## Quick Navigation

<div class="grid-cards">

<div class="card">
  <span class="card-icon">&#128640;</span>
  <h3>Getting Started</h3>
  <p>Setup MkDocs cho project mới trong 15 phút. Multi-platform support.</p>
  <a class="card-link" href="getting-started/quick-start/">Quick Start &#8594;</a>
</div>

<div class="card">
  <span class="card-icon">&#9881;</span>
  <h3>Operations</h3>
  <p>Runbooks, network topology, incident postmortem, maintenance windows.</p>
  <a class="card-link" href="operations/runbooks/proxmox-vm-runbook/">Runbooks &#8594;</a>
</div>

<div class="card">
  <span class="card-icon">&#128736;</span>
  <h3>Development</h3>
  <p>Architecture Decision Records, release notes, technical specs.</p>
  <a class="card-link" href="development/adr/adr-001-mkdocs/">ADR &#8594;</a>
</div>

<div class="card">
  <span class="card-icon">&#127891;</span>
  <h3>Training</h3>
  <p>Onboarding modules với hands-on labs cho team members mới.</p>
  <a class="card-link" href="training/training-module-example/">Git Basics &#8594;</a>
</div>

<div class="card">
  <span class="card-icon">&#128214;</span>
  <h3>Guides</h3>
  <p>Step-by-step how-to guides cho common admin tasks.</p>
  <a class="card-link" href="guides/how-to/google-workspace-new-user/">How-to &#8594;</a>
</div>

</div>

## All Templates (T1-T11)

<div class="template-gallery">

<a class="template-item" href="operations/runbooks/proxmox-vm-runbook/">
  <div class="template-id">T1 Runbook</div>
  <div class="template-name">Proxmox VM Management</div>
  <div class="template-desc">Vận hành hệ thống, health checks, troubleshooting</div>
</a>

<a class="template-item" href="development/adr/adr-001-mkdocs/">
  <div class="template-id">T2 ADR</div>
  <div class="template-name">Why MkDocs-Material</div>
  <div class="template-desc">Architecture decision records, alternatives analysis</div>
</a>

<a class="template-item" href="guides/how-to/google-workspace-new-user/">
  <div class="template-id">T3 How-to Guide</div>
  <div class="template-name">Google Workspace New User</div>
  <div class="template-desc">Step-by-step instructions với expected results</div>
</a>

<a class="template-item" href="training/training-module-example/">
  <div class="template-id">T4 Training Module</div>
  <div class="template-name">Git Basics for Team</div>
  <div class="template-desc">Lessons, hands-on labs, knowledge checks</div>
</a>

<a class="template-item" href="operations/network-topology-example/">
  <div class="template-id">T5 Network Topology</div>
  <div class="template-name">Demo Lab Network</div>
  <div class="template-desc">VLAN layout, firewall rules, server inventory</div>
</a>

<a class="template-item" href="operations/postmortem-example/">
  <div class="template-id">T6 Incident Postmortem</div>
  <div class="template-name">DB Connection Pool</div>
  <div class="template-desc">Timeline, root cause, action items, lessons</div>
</a>

<a class="template-item" href="operations/maintenance-window-example/">
  <div class="template-id">T7 Maintenance Window</div>
  <div class="template-name">PostgreSQL Upgrade</div>
  <div class="template-desc">Pre-checks, procedure, rollback, post-checks</div>
</a>

<a class="template-item" href="development/release-notes-example/">
  <div class="template-id">T8 Release Notes</div>
  <div class="template-name">v2.5.0 Release</div>
  <div class="template-desc">Features, bug fixes, breaking changes, upgrade</div>
</a>

<a class="template-item" href="development/adr/adr-002-choose-postgresql/">
  <div class="template-id">T9 ADR (MADR)</div>
  <div class="template-name">Choose PostgreSQL</div>
  <div class="template-desc">Complex decision, structured pros/cons, multiple options</div>
</a>

<a class="template-item" href="development/adr/adr-003-api-versioning/">
  <div class="template-id">T10 ADR (Lightweight)</div>
  <div class="template-name">API Versioning Strategy</div>
  <div class="template-desc">Quick decision, minimal format, POC/spike</div>
</a>

<a class="template-item" href="training/docker-basics-knowledge-check/">
  <div class="template-id">T11 Knowledge Check</div>
  <div class="template-name">Docker Basics Assessment</div>
  <div class="template-desc">Multiple choice, scenario-based, collapsible answers</div>
</a>

</div>

## About This Site

!!! tip "Built with Documentation Skills Toolkit"
    Site này là **demo output** khi áp dụng bộ [Documentation Skills Toolkit](https://github.com/lampd-2157/documentation-skills-toolkit). Mỗi trang tương ứng với 1 template (T1-T11), viết theo skill guidelines.

!!! example "Try It Yourself"
    ```bash
    git clone https://github.com/lampd-2157/documentation-skills-toolkit.git
    cd documentation-skills-toolkit
    ./scripts/docs-toolkit new runbook "My Service"
    ```
