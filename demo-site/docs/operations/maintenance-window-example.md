---
title: "Maintenance: PostgreSQL 15 to 16 Upgrade"
description: "Planned maintenance window for database major version upgrade"
author: "DBA Team"
created: 2026-03-20
updated: 2026-03-20
status: approved
tags: [maintenance, database, postgresql, upgrade]
---

# Maintenance: PostgreSQL 15 to 16 Upgrade

| Field           | Value                                  |
| --------------- | -------------------------------------- |
| **Schedule**    | 2026-03-29 02:00 — 04:00 (UTC+7)      |
| **Duration**    | 2 hours                                |
| **Impact**      | Database read/write unavailable        |
| **Downtime**    | Partial — API returns maintenance page |
| **Owner**       | DBA Team                               |
| **Approved by** | Mr. DulaP (Infra Lead)                 |

---

## Pre-checks

- [ ] Full backup completed and verified (pg_dump + WAL archive)
- [ ] Rollback plan tested on staging (2026-03-25)
- [ ] Stakeholders notified via Slack #general (48h advance)
- [ ] Maintenance page configured on Nginx
- [ ] PostgreSQL 16 packages downloaded on server
- [ ] Monitoring dashboard open: `mon.demo-lab.local/d/postgres`
- [ ] Staging upgrade completed successfully (2026-03-22)

---

## Procedure

| #   | Step                          | Command                                                     | Verify                              |
| --- | ----------------------------- | ----------------------------------------------------------- | ----------------------------------- |
| 1   | Enable maintenance page       | `sudo ln -sf /etc/nginx/maintenance.conf /etc/nginx/sites-enabled/default && sudo nginx -s reload` | `curl -s -o /dev/null -w "%{http_code}" https://app.demo-lab.local` returns `503` |
| 2   | Stop application              | `sudo systemctl stop myapp`                                 | `systemctl status myapp` shows inactive |
| 3   | Create final backup           | `sudo -u postgres pg_dump -Fc mydb > /backup/pre-upgrade-$(date +%Y%m%d).dump` | File exists and size > 0 |
| 4   | Stop PostgreSQL 15            | `sudo systemctl stop postgresql@15-main`                    | `pg_isready` returns "no response"  |
| 5   | Install PostgreSQL 16         | `sudo apt install postgresql-16`                            | `pg_lsclusters` shows 16/main       |
| 6   | Run pg_upgrade                | `sudo -u postgres /usr/lib/postgresql/16/bin/pg_upgrade -b /usr/lib/postgresql/15/bin -B /usr/lib/postgresql/16/bin -d /var/lib/postgresql/15/main -D /var/lib/postgresql/16/main --check` | Check mode passes with "Clusters are compatible" |
| 7   | Execute upgrade               | `sudo -u postgres /usr/lib/postgresql/16/bin/pg_upgrade -b /usr/lib/postgresql/15/bin -B /usr/lib/postgresql/16/bin -d /var/lib/postgresql/15/main -D /var/lib/postgresql/16/main` | "Upgrade Complete" message |
| 8   | Start PostgreSQL 16           | `sudo systemctl start postgresql@16-main`                   | `pg_isready` returns "accepting connections" |
| 9   | Run ANALYZE                   | `sudo -u postgres /usr/lib/postgresql/16/bin/vacuumdb --all --analyze-in-stages` | Completes without errors |
| 10  | Update connection config      | `sudo sed -i 's/port = 5433/port = 5432/' /etc/postgresql/16/main/postgresql.conf && sudo systemctl restart postgresql@16-main` | `psql -p 5432 -c 'SELECT version()'` shows PostgreSQL 16 |
| 11  | Start application             | `sudo systemctl start myapp`                                | `curl -s https://app.demo-lab.local/health` returns `{"status":"ok"}` |
| 12  | Disable maintenance page      | `sudo ln -sf /etc/nginx/app.conf /etc/nginx/sites-enabled/default && sudo nginx -s reload` | `curl -s https://app.demo-lab.local` returns 200 |

---

## Rollback

If any step fails after Step 6:

| #   | Step                    | Command                                                       |
| --- | ----------------------- | ------------------------------------------------------------- |
| 1   | Stop PostgreSQL 16      | `sudo systemctl stop postgresql@16-main`                      |
| 2   | Restore PostgreSQL 15   | `sudo systemctl start postgresql@15-main`                     |
| 3   | Verify data             | `psql -c 'SELECT count(*) FROM users'` matches pre-upgrade    |
| 4   | Start application       | `sudo systemctl start myapp`                                  |
| 5   | Disable maintenance     | `sudo ln -sf /etc/nginx/app.conf /etc/nginx/sites-enabled/default && sudo nginx -s reload` |

---

## Post-checks

- [ ] All services healthy (`/health` endpoint returns 200)
- [ ] No error spike in monitoring (15 min observation)
- [ ] Query performance within SLA (p95 < 500ms)
- [ ] Application logs: no database errors
- [ ] PostgreSQL version confirmed: `SELECT version()` shows 16.x
- [ ] Stakeholders notified via Slack: maintenance complete
- [ ] Remove old PostgreSQL 15 cluster (after 7 days observation):
  ```bash
  sudo pg_dropcluster 15 main
  sudo apt remove postgresql-15
  ```
