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

!!! info "Document Metadata"

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

### Step 1: Enable maintenance page

```bash
sudo ln -sf /etc/nginx/maintenance.conf /etc/nginx/sites-enabled/default && sudo nginx -s reload
```

!!! check "Verify"
    Expected: `curl -s -o /dev/null -w "%{http_code}" https://app.demo-lab.local` returns `503`

### Step 2: Stop application

```bash
sudo systemctl stop myapp
```

!!! check "Verify"
    Expected: `systemctl status myapp` shows inactive

### Step 3: Create final backup

```bash
sudo -u postgres pg_dump -Fc mydb > /backup/pre-upgrade-$(date +%Y%m%d).dump
```

!!! check "Verify"
    Expected: File exists and size > 0

### Step 4: Stop PostgreSQL 15

```bash
sudo systemctl stop postgresql@15-main
```

!!! check "Verify"
    Expected: `pg_isready` returns "no response"

### Step 5: Install PostgreSQL 16

```bash
sudo apt install postgresql-16
```

!!! check "Verify"
    Expected: `pg_lsclusters` shows 16/main

### Step 6: Run pg_upgrade

```bash
sudo -u postgres /usr/lib/postgresql/16/bin/pg_upgrade \
  -b /usr/lib/postgresql/15/bin \
  -B /usr/lib/postgresql/16/bin \
  -d /var/lib/postgresql/15/main \
  -D /var/lib/postgresql/16/main \
  --check
```

!!! check "Verify"
    Expected: Check mode passes with "Clusters are compatible"

### Step 7: Execute upgrade

```bash
sudo -u postgres /usr/lib/postgresql/16/bin/pg_upgrade \
  -b /usr/lib/postgresql/15/bin \
  -B /usr/lib/postgresql/16/bin \
  -d /var/lib/postgresql/15/main \
  -D /var/lib/postgresql/16/main
```

!!! check "Verify"
    Expected: "Upgrade Complete" message

### Step 8: Start PostgreSQL 16

```bash
sudo systemctl start postgresql@16-main
```

!!! check "Verify"
    Expected: `pg_isready` returns "accepting connections"

### Step 9: Run ANALYZE

```bash
sudo -u postgres /usr/lib/postgresql/16/bin/vacuumdb --all --analyze-in-stages
```

!!! check "Verify"
    Expected: Completes without errors

### Step 10: Update connection config

```bash
sudo sed -i 's/port = 5433/port = 5432/' /etc/postgresql/16/main/postgresql.conf && sudo systemctl restart postgresql@16-main
```

!!! check "Verify"
    Expected: `psql -p 5432 -c 'SELECT version()'` shows PostgreSQL 16

### Step 11: Start application

```bash
sudo systemctl start myapp
```

!!! check "Verify"
    Expected: `curl -s https://app.demo-lab.local/health` returns `{"status":"ok"}`

### Step 12: Disable maintenance page

```bash
sudo ln -sf /etc/nginx/app.conf /etc/nginx/sites-enabled/default && sudo nginx -s reload
```

!!! check "Verify"
    Expected: `curl -s https://app.demo-lab.local` returns 200

---

## Rollback

If any step fails after Step 6:

### Step 1: Stop PostgreSQL 16

```bash
sudo systemctl stop postgresql@16-main
```

### Step 2: Restore PostgreSQL 15

```bash
sudo systemctl start postgresql@15-main
```

### Step 3: Verify data

```bash
psql -c 'SELECT count(*) FROM users'
```

!!! check "Verify"
    Expected: Count matches pre-upgrade value

### Step 4: Start application

```bash
sudo systemctl start myapp
```

### Step 5: Disable maintenance

```bash
sudo ln -sf /etc/nginx/app.conf /etc/nginx/sites-enabled/default && sudo nginx -s reload
```

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
