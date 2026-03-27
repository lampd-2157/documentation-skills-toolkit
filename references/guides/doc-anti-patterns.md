# Documentation Anti-Patterns — Top 10 Mistakes

> 10 lỗi phổ biến nhất khi viết documentation. Mỗi anti-pattern kèm bad/good example và skill/rule ngăn chặn.

---

## 1. The Prose-Only Runbook

**Vấn đề:** Runbook chỉ có text mô tả, không có commands copy-paste được.

```markdown
<!-- BAD -->
### Check disk usage
Check the disk usage on the data partition. If it's too high,
clean up old logs. Contact the infrastructure team if needed.
```

```markdown
<!-- GOOD -->
### Check disk usage
```bash
df -h /data
# Expected: Use% < 80%
# If > 90%:
sudo /opt/scripts/cleanup-logs.sh --older-than 7d
```

**Prevented by:** `ops-runbook-writer.md` Iron Law — "Every runbook MUST have copy-paste commands AND expected output"

---

## 2. The Stale Screenshot

**Vấn đề:** Screenshots từ UI cũ, không match version hiện tại. Reader bị confuse.

```markdown
<!-- BAD -->
![Dashboard](images/dashboard-v1.png)
<!-- Screenshot từ 2025, UI đã redesign hoàn toàn -->
```

```markdown
<!-- GOOD -->
![Dashboard](images/dashboard-v2.5.png)
<!-- Last verified: 2026-03-26 | Matches v2.5.0 UI -->
```

**Prevented by:** `training-doc-writer.md` Guardrail — "Screenshots/diagrams up-to-date — match current UI/system"

---

## 3. The Missing Prerequisites

**Vấn đề:** Guide giả định reader đã có sẵn mọi thứ. Reader stuck ở step 1.

```markdown
<!-- BAD -->
### Step 1: Deploy the application
Run the deploy script to push to production.
```

```markdown
<!-- GOOD -->
## Prerequisites
- [ ] Node.js >= 18 installed (`node --version`)
- [ ] Docker running (`docker ps`)
- [ ] AWS CLI configured (`aws sts get-caller-identity`)
- [ ] Access to production cluster (request via IPortal)

### Step 1: Deploy the application
```

**Prevented by:** `training-doc-writer.md` Iron Law — "Prerequisites -> Steps -> Expected Result -> Troubleshooting — skip any = incomplete"

---

## 4. The Wall of Text

**Vấn đề:** Một khối text dài không có headings, tables, hay code blocks. Không ai đọc.

```markdown
<!-- BAD -->
The system uses PostgreSQL 15 running on Ubuntu 22.04 with a replication
setup where the primary is at 10.0.1.30 and the replica at 10.0.1.31.
The backup runs every 6 hours using pg_dump and stores to both S3 and
local NAS with 30 day retention. The monitoring uses Prometheus with
Grafana dashboards accessible at grafana.internal...
```

```markdown
<!-- GOOD -->
## System Inventory

| System     | IP        | Role        |
|------------|-----------|-------------|
| DB Primary | 10.0.1.30 | PostgreSQL  |
| DB Replica | 10.0.1.31 | Read-only   |

## Backup Strategy

| Method  | Schedule | Retention | Storage    |
|---------|----------|-----------|------------|
| pg_dump | Every 6h | 30 days   | S3 + local |
```

**Prevented by:** `docs-engineer.md` §3 — Document Structure Standards, heading hierarchy

---

## 5. The Orphan Doc

**Vấn đề:** Doc tồn tại trong repo nhưng không được link từ đâu cả. Không ai tìm thấy.

```text
<!-- BAD -->
docs/
├── index.md              # No link to secret-runbook
├── operations/
│   └── main-runbook.md
└── hidden/
    └── secret-runbook.md  # Orphan — nobody knows it exists
```

```text
<!-- GOOD -->
docs/
├── index.md              # Links to all sections
├── operations/
│   ├── index.md          # Links to all runbooks
│   └── main-runbook.md
│   └── backup-runbook.md # Linked from operations/index.md
```

**Prevented by:** `docs-engineer.md` §3.1 — Folder taxonomy with index pages, `mkdocs.yml` nav structure

---

## 6. The Credential Leak

**Vấn đề:** Hardcode passwords, tokens, API keys trong docs. Security risk.

```markdown
<!-- BAD -->
### Connect to database
```bash
psql -h db.prod.internal -U admin -p SuperSecret123!
```

```markdown
<!-- GOOD -->
### Connect to database
```bash
psql -h db.prod.internal -U "$DB_USER" -p "$DB_PASS"
# Credentials: stored in 1Password vault "Infrastructure"
```

**Prevented by:** `ops-runbook-writer.md` Red Flag — "Hardcode credentials in docs -> Dùng $ENV_VAR placeholder, NEVER plaintext"

---

## 7. The Assumption Trap

**Vấn đề:** Dùng từ "obviously", "simply", "just", "easily" — alienate readers không biết.

```markdown
<!-- BAD -->
Simply configure the reverse proxy and obviously you'll need to
just update the DNS records. It's easy.
```

```markdown
<!-- GOOD -->
### Step 1: Configure the reverse proxy

Edit the Nginx config:
```nginx
server {
    listen 443 ssl;
    server_name app.example.com;
    proxy_pass http://localhost:8080;
}
```

### Step 2: Update DNS records

Add an A record pointing `app.example.com` to the server IP.
```

**Prevented by:** `docs-engineer.md` §2.3 — Google Writing Style (active voice, present tense, short sentences)

---

## 8. The Copy-Paste Drift

**Vấn đề:** Cùng 1 nội dung copy-paste vào nhiều docs, rồi chỉ update 1 chỗ. Các bản copy khác bị stale.

```markdown
<!-- BAD -->
<!-- runbook-a.md: "Server IP: 10.0.1.10" (updated) -->
<!-- runbook-b.md: "Server IP: 10.0.1.5"  (stale!) -->
<!-- guide-c.md:   "Server IP: 10.0.1.5"  (stale!) -->
```

```markdown
<!-- GOOD — Single Source of Truth -->
<!-- inventory.md: Server Inventory table (updated once) -->
<!-- runbook-a.md: "See [Server Inventory](inventory.md)" -->
<!-- runbook-b.md: "See [Server Inventory](inventory.md)" -->
```

**Prevented by:** DRY principle — link thay vì copy. `docs-lifecycle-guide.md` quarterly audit catches drift.

---

## 9. The Dead Link

**Vấn đề:** Links trỏ tới resources đã move/delete. Reader hit 404.

```markdown
<!-- BAD -->
See the [deployment guide](docs/old-folder/deploy.md) for details.
<!-- File đã move sang docs/operations/deploy-runbook.md -->
```

```markdown
<!-- GOOD -->
See the [deployment runbook](operations/deploy-runbook.md) for details.
<!-- Verified: 2026-03-26 -->
```

**Prevented by:** Pre-commit hook `markdown-link-check` + quarterly audit `find broken links`

---

## 10. The Kitchen Sink

**Vấn đề:** 1 doc cố cover mọi thứ — setup, operations, troubleshooting, training, architecture. Kết quả: 2000+ dòng, không ai đọc hết.

```text
<!-- BAD -->
everything-you-need-to-know.md  (2500 lines)
  - Setup instructions
  - Architecture overview
  - Operations manual
  - Troubleshooting guide
  - Training material
  - API documentation
```

```text
<!-- GOOD — 1 doc = 1 purpose -->
docs/
├── getting-started/quick-start.md     (< 100 lines)
├── development/architecture.md        (< 200 lines)
├── operations/runbook.md              (< 300 lines)
├── operations/troubleshooting.md      (< 200 lines)
├── training/onboarding.md             (< 200 lines)
└── development/api-reference.md       (< 300 lines)
```

**Prevented by:** `docs-engineer.md` §3 — Folder taxonomy. Skill template guideline: mỗi section <= 50 dòng.

---

## Quick Reference

| # | Anti-Pattern | Signal | Fix |
|---|-------------|--------|-----|
| 1 | Prose-Only Runbook | No code blocks in runbook | Add copy-paste commands |
| 2 | Stale Screenshot | UI doesn't match image | Re-capture or use Mermaid |
| 3 | Missing Prerequisites | Reader stuck at step 1 | Add prerequisites checklist |
| 4 | Wall of Text | No headings for 50+ lines | Break into sections + tables |
| 5 | Orphan Doc | Doc not in any nav/index | Add to mkdocs.yml nav |
| 6 | Credential Leak | Plaintext passwords | Use $ENV_VAR placeholders |
| 7 | Assumption Trap | "simply", "obviously", "just" | Remove; add explicit steps |
| 8 | Copy-Paste Drift | Same content in 3+ files | Link to single source |
| 9 | Dead Link | 404 when clicking links | Run link checker |
| 10 | Kitchen Sink | Doc > 500 lines | Split by purpose |

---

> **Version:** 1.0.0 | **Cập nhật:** 2026-03-26
