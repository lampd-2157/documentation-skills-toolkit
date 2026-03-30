---
title: Tags
description: Browse documentation by topic tags
tags: []
---

# Tags

Documents in this site are tagged by topic. Tags appear at the top of each page and are clickable.

## Tag Categories

| Category | Tags | Documents |
|----------|------|-----------|
| **Operations** | `runbook`, `operations`, `maintenance`, `incident`, `postmortem` | Runbooks, maintenance windows, postmortems |
| **Network** | `network`, `infrastructure`, `topology`, `ansible`, `cisco-ios` | Network topology, Ansible how-to |
| **Development** | `adr`, `architecture`, `api`, `release` | ADRs, release notes |
| **Training** | `training`, `onboarding`, `assessment` | Training modules, knowledge checks |
| **How-to** | `how-to`, `automation`, `setup` | Step-by-step guides |
| **Database** | `database`, `postgresql`, `upgrade` | DB-related docs |
| **Security** | `security` | Security policies, access control |

## How Tags Work

Tags are defined in each document's YAML frontmatter:

```yaml
---
title: "Document Title"
tags: [network, ansible, automation]
---
```

The MkDocs Material [tags plugin](https://squidfunk.github.io/mkdocs-material/plugins/tags/)
renders clickable tag pills at the top of each page.

To add tags to a new document, include the `tags` field in the frontmatter when
creating it with `docs-toolkit new <type> <title>`.
