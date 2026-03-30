# Incident Patterns — Failure Taxonomy & Prevention Guide

**Source:** Adapted from [danluu/post-mortems](https://github.com/danluu/post-mortems) — bộ sưu tập postmortem từ các hệ thống lớn (AWS, Google, GitHub, Cloudflare, Meta, v.v.)

> Tài liệu này phân loại các failure pattern phổ biến trong production systems.
> Mục tiêu: giúp team **nhận diện nhanh** loại sự cố và áp dụng đúng investigation + prevention playbook.

---

## Failure Taxonomy — 6 Category chính

### 1. Config Errors — Lỗi cấu hình

**Definition:** Sự cố do misconfiguration — sai config file, bad BGP route, firewall rule sai, typo trong environment variable, feature flag bật nhầm.

**Real-world examples:**

- **AWS S3 (2017)** — Typo trong command xóa server, gây outage toàn bộ us-east-1
- **Cloudflare (2020)** — Bad BGP route configuration khiến traffic bị drop trên diện rộng
- **GitHub (2021)** — Sai firewall rule trong maintenance khiến internal services mất kết nối
- **Facebook/Meta (2021)** — BGP withdrawal do config change khiến toàn bộ hệ thống offline 6 giờ

**Investigation checklist:**

- [ ] So sánh config hiện tại vs last-known-good config (`diff` hoặc Git history)
- [ ] Check recent config changes — ai thay đổi gì, khi nào? (`git log`, audit log)
- [ ] Verify environment variables và feature flags trên production vs staging
- [ ] Kiểm tra network config: BGP routes, DNS records, firewall rules
- [ ] Review deployment history — có config change nào đi kèm deploy gần đây?

**Prevention controls:**

- [ ] Config changes qua Pull Request — require review trước khi apply
- [ ] Automated config validation (lint, schema check) trong CI/CD pipeline
- [ ] Canary deployment cho config changes — roll out từ từ, không big-bang
- [ ] GitOps workflow — mọi config change phải qua version control
- [ ] Config drift detection — alert khi production config khác source of truth

---

### 2. Hardware & Power — Lỗi phần cứng & nguồn điện

**Definition:** Sự cố do hardware failure — mất điện data center, cooling system hỏng, disk failure, network hardware (switch, router) lỗi, fiber cắt.

**Real-world examples:**

- **AWS US-East-1 (2023)** — Power event tại data center gây cascading failures cho nhiều services
- **Google Cloud (2019)** — Network hardware failure gây mất kết nối cross-region
- **OVHcloud (2021)** — Cháy data center SBG2 tại Strasbourg, mất dữ liệu vĩnh viễn cho nhiều khách hàng
- **Microsoft Azure (2018)** — Cooling system failure tại data center San Antonio gây overheating và shutdown

**Investigation checklist:**

- [ ] Check monitoring dashboard: hardware health, temperature, power status
- [ ] Kiểm tra disk health — SMART status, I/O errors trong `dmesg`
- [ ] Review network hardware — link status, CRC errors, packet loss
- [ ] Xác nhận power redundancy — UPS status, generator, dual-feed power

**Prevention controls:**

- [ ] Multi-AZ / multi-region deployment — không depend vào 1 data center
- [ ] Regular hardware health monitoring + predictive maintenance
- [ ] Disk redundancy (RAID) + automated disk replacement workflow
- [ ] Network redundancy — dual uplinks, diverse fiber paths
- [ ] Backup power testing — UPS load test monthly, generator test quarterly

---

### 3. Resource Conflicts — Xung đột tài nguyên

**Definition:** Sự cố do race condition, resource contention, deadlock, capacity exhaustion — CPU/memory/disk hết, thread pool cạn kiệt, connection limit reached.

**Real-world examples:**

- **GitHub (2018)** — Database contention do schema migration chạy đồng thời với peak traffic
- **Cloudflare (2019)** — CPU exhaustion do regex backtracking trong WAF rule, toàn bộ edge nodes bị ảnh hưởng
- **Amazon DynamoDB (2015)** — Metadata partition contention gây latency spike trên diện rộng
- **Slack (2021)** — Connection pool exhaustion khi traffic spike đột ngột sau kỳ nghỉ

**Investigation checklist:**

- [ ] Check resource utilization: CPU, memory, disk I/O, network bandwidth
- [ ] Kiểm tra connection pools — database, HTTP client, thread pools
- [ ] Review lock contention — database locks, distributed locks, mutex
- [ ] Analyze traffic patterns — có sudden spike không? (DDoS, viral event, cron storm)
- [ ] Check for noisy neighbor — shared resources bị service khác chiếm dụng

**Prevention controls:**

- [ ] Resource limits & quotas cho mọi service (CPU, memory, connections)
- [ ] Auto-scaling policies với proper thresholds — scale trước khi hết capacity
- [ ] Connection pooling với proper sizing + circuit breaker cho external dependencies
- [ ] Load testing định kỳ — verify system behavior under 2x-3x normal load
- [ ] Rate limiting + backpressure mechanisms tại mọi service boundary

---

### 4. Time-related — Lỗi liên quan thời gian

**Definition:** Sự cố do leap second, certificate expiry, timezone bugs, NTP drift, clock skew, cron job overlap, timestamp overflow.

**Real-world examples:**

- **Cloudflare (2017)** — Leap second bug gây DNS resolver trả về negative duration
- **Microsoft Azure (2019)** — Certificate expiry trên internal service gây Multi-Factor Auth outage toàn cầu
- **Let's Encrypt (2020)** — Phải revoke 3 triệu certificates do bug trong validation timing
- **AWS (2012)** — Leap second gây CPU spike trên nhiều Linux instances chạy Java

**Investigation checklist:**

- [ ] Check NTP sync status trên tất cả servers — `chronyc tracking` hoặc `ntpq -p`
- [ ] Verify certificate expiry dates — `openssl x509 -enddate -noout -in cert.pem`
- [ ] Review timezone handling trong application code — có hardcode timezone không?
- [ ] Kiểm tra cron schedule — có job nào overlap hoặc chạy quá lâu?

**Prevention controls:**

- [ ] Automated certificate monitoring — alert 30 ngày trước expiry
- [ ] NTP monitoring + alerting khi clock drift > threshold (VD: > 100ms)
- [ ] Dùng UTC everywhere trong backend — convert timezone chỉ ở presentation layer
- [ ] Certificate auto-renewal (certbot, cert-manager) + renewal testing
- [ ] Leap second handling — verify NTP slew mode, test với fake leap second

---

### 5. Database — Lỗi database

**Definition:** Sự cố do schema migration failure, replication lag, connection pool exhaustion, backup corruption, query performance degradation, storage full.

**Real-world examples:**

- **GitHub (2018)** — Database failover loop khi primary node gặp issue, Orchestrator chuyển đổi liên tục
- **GitLab (2017)** — Mất 6 giờ production data do sai thứ tự backup/restore procedures
- **Spotify (2020)** — Replication lag gây data inconsistency giữa read replicas
- **Roblox (2021)** — Database cluster exhaustion (BoltDB) gây 73-hour outage

**Investigation checklist:**

- [ ] Check replication status — lag bao nhiêu? Replication có bị broken không?
- [ ] Review slow query log — có query nào chạy lâu bất thường?
- [ ] Kiểm tra connection pool — active connections, waiting connections, pool size
- [ ] Verify backup integrity — last successful backup khi nào? Test restore gần nhất?
- [ ] Check disk space cho database — data files, WAL/binlog, temp files

**Prevention controls:**

- [ ] Schema migration qua CI/CD — test trên staging trước, có rollback plan
- [ ] Replication monitoring + alerting khi lag > threshold (VD: > 5 seconds)
- [ ] Connection pool sizing dựa trên load testing — không đoán mò
- [ ] Automated backup verification — daily restore test vào environment riêng
- [ ] Database capacity planning — forecast growth, alert trước khi đầy

---

### 6. Cascading Failures — Sự cố lan truyền

**Definition:** Sự cố từ 1 component lan ra toàn hệ thống — retry storm, circuit breaker không hoạt động, dependency chain failure, thundering herd khi service recovery.

**Real-world examples:**

- **AWS DynamoDB (2015)** — Metadata service overload → storage nodes không resolve partition → toàn bộ DynamoDB degraded
- **Slack (2022)** — 1 database shard chậm → connection queue build up → tất cả services depend on DB bị timeout
- **Fastly (2021)** — 1 customer config change trigger bug → 85% global network nodes return 503
- **Roblox (2021)** — Consul cluster overload → service discovery fail → cascading failure kéo dài 73 giờ

**Investigation checklist:**

- [ ] Trace dependency chain — service nào fail đầu tiên? (distributed tracing, logs timeline)
- [ ] Check circuit breaker status — có circuit nào đang OPEN? Có service nào thiếu circuit breaker?
- [ ] Analyze retry patterns — có retry storm không? Retry rate tăng bao nhiêu lần?
- [ ] Review load balancer behavior — có thundering herd khi service recover không?
- [ ] Kiểm tra timeout configuration — cascading timeouts có hợp lý không? (outer > inner)

**Prevention controls:**

- [ ] Circuit breaker pattern cho mọi external dependency — fail fast thay vì chờ timeout
- [ ] Retry with exponential backoff + jitter — tránh retry storm
- [ ] Bulkhead pattern — isolate failure, không để 1 dependency kéo sập toàn bộ
- [ ] Graceful degradation — service vẫn hoạt động (degraded mode) khi dependency down
- [ ] Chaos engineering — inject failure định kỳ để verify resilience (GameDay, Chaos Monkey)

---

## Pattern Matching — Quy trình nhận diện sự cố

Khi investigate một incident, **chạy qua 6 category** để narrow down root cause nhanh nhất:

```text
Incident xảy ra
  │
  ├── 1. Config change gần đây?
  │     └── YES → Check Config Errors (Category 1)
  │
  ├── 2. Hardware alert / power event?
  │     └── YES → Check Hardware & Power (Category 2)
  │
  ├── 3. Resource exhaustion (CPU/mem/disk/connections)?
  │     └── YES → Check Resource Conflicts (Category 3)
  │
  ├── 4. Cert expiry / time-related event / NTP issue?
  │     └── YES → Check Time-related (Category 4)
  │
  ├── 5. Database errors / replication / migration?
  │     └── YES → Check Database (Category 5)
  │
  └── 6. Multiple services fail cùng lúc?
        └── YES → Check Cascading Failures (Category 6)
```

**Tips:**

- Nhiều incident thuộc **nhiều category** cùng lúc — VD: config error → cascading failure
- Bắt đầu từ category có signal rõ nhất, sau đó mở rộng investigation
- Dùng timeline để xác định **trigger event** — event đầu tiên thường chỉ đúng category
- Cross-reference với [danluu/post-mortems](https://github.com/danluu/post-mortems) để tìm incident tương tự từ các công ty khác

> **Mục tiêu cuối cùng:** Mỗi postmortem phải classify được failure category → giúp team tracking trends và đầu tư prevention đúng chỗ.

---
