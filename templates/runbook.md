<!-- Template T1: Runbook — Copy this file and customize -->
# Runbook: [System/Service Name]

> Last verified: YYYY-MM-DD | Owner: [Team]

## Overview

!!! info "Document Metadata"
    | Field | Value |
    |-------|-------|
    | **Service** | [tên service] |
    | **Environment** | production / staging |
    | **URL** | [endpoint URL] |
    | **Repository** | [git repo link] |
    | **On-call** | [rotation schedule link] |

## Architecture
<!-- Mermaid diagram: service dependencies -->

## Health Checks

| Check        | Command                | Expected | Alert If    |
| ------------ | ---------------------- | -------- | ----------- |
| [check name] | `[copy-paste command]` | [output] | [condition] |

## Start / Stop / Restart

### Step 1: Start

```bash
[command]
```

!!! check "Verify"
    Expected: `[verify command]`

### Step 2: Stop

```bash
[command]
```

!!! check "Verify"
    Expected: `[verify command]`

### Step 3: Restart

```bash
[command]
```

!!! check "Verify"
    Expected: `[verify command]`

## Troubleshooting

### [Issue Title]

**Symptoms:** [what you see]
**Root Cause:** [why it happens]
**Fix:**

1. `[command]` — [explain]
2. `[command]` — verify: [expected output]

**Prevention:** [how to prevent recurrence]

## Escalation

| Severity | Response | Contact         | Channel          |
| -------- | -------- | --------------- | ---------------- |
| P1       | 15 min   | [name/rotation] | [phone/Slack/PD] |
| P2       | 1 hour   | [name/team]     | [Slack channel]  |
| P3       | 4 hours  | [team]          | [email/ticket]   |
