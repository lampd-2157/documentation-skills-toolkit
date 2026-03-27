---
title: "Postmortem: Database Connection Pool Exhaustion"
description: "P2 incident on 2026-03-15 — connection leak caused 45-minute partial outage"
author: "Incident Lead — DulaP"
created: 2026-03-15
updated: 2026-03-20
status: reviewed
tags: [incident, postmortem, database, P2]
---

# :material-alert-circle: Postmortem: Database Connection Pool Exhaustion

!!! danger "Severity: P2 — Major | Duration: 45 min | Impact: 12% error rate"

!!! info "Incident Metadata"

    | Field        | Value                              |
    | ------------ | ---------------------------------- |
    | **Severity** | P2 — Major                         |
    | **Date**     | 2026-03-15                         |
    | **Duration** | 14:22 — 15:07 (UTC+7) — 45 min    |
    | **Impact**   | API latency 5x normal, 12% errors |
    | **Owner**    | DulaP (Incident Lead)              |
    | **Status**   | Reviewed                           |

## Summary

A connection leak in the new user search feature caused PostgreSQL connection pool exhaustion. API response times degraded from ~200ms to ~1000ms+ with 12% of requests failing with 503 errors. The issue was resolved by restarting the application server and deploying a hotfix.

## Timeline

| Time (UTC+7) | Event                                   | Actor    |
| ------------- | --------------------------------------- | -------- |
| 14:22         | Prometheus alert: API p95 > 1000ms      | Auto     |
| 14:25         | On-call engineer acknowledges alert     | TrungNV  |
| 14:30         | Identified: DB connections at 95/100    | TrungNV  |
| 14:35         | Escalated to P2, team notified          | TrungNV  |
| 14:40         | Root cause found: connection leak in PR #342 | DulaP    |
| 14:45         | Mitigation: restart app server          | DulaP    |
| 14:48         | API latency back to normal              | Auto     |
| 14:50         | Hotfix PR #345 opened                   | DulaP    |
| 15:00         | Hotfix deployed to production           | DulaP    |
| 15:07         | Incident resolved, monitoring stable    | TrungNV  |

## Root Cause

PR #342 introduced a new user search endpoint that opened database connections in a loop without properly closing them in the `finally` block. Under load, connections accumulated and exhausted the pool (max: 100).

```javascript
// BAD — connection not released on error
async function searchUsers(query) {
  const conn = await pool.acquire();
  const results = await conn.query('SELECT * FROM users WHERE name LIKE $1', [query]);
  conn.release(); // Never reached if query throws
  return results;
}

// FIX — connection released in finally block
async function searchUsers(query) {
  const conn = await pool.acquire();
  try {
    return await conn.query('SELECT * FROM users WHERE name LIKE $1', [query]);
  } finally {
    conn.release(); // Always releases, even on error
  }
}
```

!!! failure "What Went Wrong"
    - Code review missed the missing `finally` block in PR #342
    - No integration test for connection pool behavior under error conditions
    - Alert threshold (p95 > 1000ms) was too slow — should have caught at 500ms

!!! success "What Went Right"
    - Prometheus alerting detected the issue within 3 minutes
    - On-call response was fast (3 min to acknowledge)
    - Root cause identified within 15 minutes
    - Hotfix deployed within 20 minutes of root cause identification

## Action Items

| #   | Action                                            | Owner   | Due Date   | Status    |
| --- | ------------------------------------------------- | ------- | ---------- | --------- |
| 1   | Add `finally` block to all DB query functions     | DulaP   | 2026-03-18 | Completed |
| 2   | Add integration test: pool exhaustion scenario    | TrungNV | 2026-03-22 | Completed |
| 3   | Lower alert threshold: p95 > 500ms                | Infra   | 2026-03-20 | Completed |
| 4   | Add PR checklist item: "DB connections released?" | DulaP   | 2026-03-25 | Completed |
| 5   | Add connection pool metrics to Grafana dashboard  | Infra   | 2026-03-30 | Open      |

## Lessons Learned

- Always use `try/finally` or connection pool wrappers that auto-release
- Code review checklists should include resource management (connections, file handles)
- Alert thresholds should be set at 2x normal, not 5x
