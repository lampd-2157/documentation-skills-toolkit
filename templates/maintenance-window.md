<!-- Template T7: Maintenance Window — Copy this file and customize -->
# Maintenance: [Title]

| Field           | Value                            |
| --------------- | -------------------------------- |
| **Schedule**    | YYYY-MM-DD HH:MM — HH:MM (UTC+7) |
| **Duration**    | [X hours]                        |
| **Impact**      | [services affected]              |
| **Downtime**    | None / Partial / Full            |
| **Owner**       | [team/person]                    |
| **Approved by** | [approver]                       |

## Pre-checks
- [ ] Backup completed and verified
- [ ] Rollback plan ready and tested
- [ ] Stakeholders notified (≥24h advance)
- [ ] Monitoring dashboard open

## Procedure
| #   | Step          | Command     | Verify            |
| --- | ------------- | ----------- | ----------------- |
| 1   | [description] | `[command]` | [expected output] |
| 2   | [description] | `[command]` | [expected output] |

## Rollback
| #   | Step            | Command     |
| --- | --------------- | ----------- |
| 1   | [rollback step] | `[command]` |

## Post-checks
- [ ] All services healthy
- [ ] No error spike in monitoring (15 min observation)
- [ ] Performance within SLA
- [ ] Stakeholders notified: complete
