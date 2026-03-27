<!-- Template T7: Maintenance Window — Copy this file and customize -->
# Maintenance: [Title]

!!! info "Document Metadata"
    | Field | Value |
    |-------|-------|
    | **Schedule** | YYYY-MM-DD HH:MM — HH:MM (UTC+7) |
    | **Duration** | [X hours] |
    | **Impact** | [services affected] |
    | **Downtime** | None / Partial / Full |
    | **Owner** | [team/person] |
    | **Approved by** | [approver] |

## Pre-checks

- [ ] Backup completed and verified
- [ ] Rollback plan ready and tested
- [ ] Stakeholders notified (≥24h advance)
- [ ] Monitoring dashboard open

## Procedure

### Step 1: [description]

```bash
[command]
```

!!! check "Verify"
    Expected: `[expected output]`

### Step 2: [description]

```bash
[command]
```

!!! check "Verify"
    Expected: `[expected output]`

## Rollback

### Step 1: [rollback step]

```bash
[command]
```

## Post-checks

- [ ] All services healthy
- [ ] No error spike in monitoring (15 min observation)
- [ ] Performance within SLA
- [ ] Stakeholders notified: complete
