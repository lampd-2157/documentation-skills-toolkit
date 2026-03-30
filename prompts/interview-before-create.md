# Interview Template — Hỏi trước khi tạo doc

> Dùng trước khi tạo bất kỳ doc nào. AI agent hỏi user các câu hỏi để gather context, sau đó mới generate doc chất lượng cao.

## Cách dùng

### AI Agent (Recommended)

1. Copy phần **Interview Questions** bên dưới
2. Paste vào AI agent **TRƯỚC KHI** paste prompt tạo doc
3. AI sẽ hỏi bạn từng layer — trả lời đầy đủ
4. Sau khi có answers → AI tự tạo doc với context chính xác

### Manual

Tự trả lời các câu hỏi bên dưới, ghi notes ra file, dùng làm input khi điền template.

---

## Interview Questions

### Layer 1: Universal (luôn hỏi)

```text
Trước khi tạo document, tôi cần hỏi bạn một số câu hỏi:

1. AUDIENCE — Ai sẽ đọc doc này?
   - Role? (DevOps, developer, network engineer, manager...)
   - Level? (junior, senior, mixed team)
   - Đã biết gì? (context/knowledge họ đã có)

2. SCOPE — Doc này cover những gì?
   - Mục tiêu chính? (1-2 câu)
   - Không cover gì? (explicit exclusions)
   - Output mong đợi? (reader đọc xong sẽ làm được gì)

3. ENVIRONMENT — Context kỹ thuật?
   - Production / staging / lab / general guide?
   - OS / platform? (Ubuntu, CentOS, Windows, cloud...)
   - Tools/versions cụ thể? (Ansible 2.16, K8s 1.30, PostgreSQL 16...)
```

### Layer 2: Type-specific (hỏi theo loại doc)

```text
Tùy theo loại doc bạn muốn tạo, tôi cần thêm:

RUNBOOK (T1):
- Service/system nào?
- SLA requirements? (uptime target, response time)
- On-call rotation hiện tại? (ai, channel nào)
- Common issues đã gặp?

ADR (T2/T9/T10):
- Options đã xem xét? (ít nhất 2-3)
- Constraints? (budget, timeline, team size, tech stack)
- Ai quyết định? (decision makers)
- Deadline quyết định?

HOW-TO (T3):
- Task cụ thể là gì? (1 câu)
- User đã biết gì trước khi bắt đầu?
- Có cần multi-platform? (Linux + macOS + Windows?)
- Expected output sau khi hoàn thành?

TRAINING (T4):
- Topic + duration?
- Hands-on lab cần thiết bị/access gì?
- Assessment criteria? (pass/fail thế nào)

POSTMORTEM (T6):
- Incident xảy ra khi nào? Timeline?
- Impact? (ai bị ảnh hưởng, bao lâu)
- Root cause đã biết chưa?
- Action items đã có chưa?

MAINTENANCE (T7):
- Hệ thống nào bị ảnh hưởng?
- Downtime dự kiến?
- Rollback plan?
- Stakeholders cần notify?

SECURITY POLICY:
- Policy áp dụng cho ai? (teams, systems)
- Compliance requirements? (SOC2, ISO27001, internal)
- Enforcement mechanism? (technical controls vs process)
```

### Layer 3: Deep-dive (chỉ hỏi cho docs quan trọng/phức tạp)

```text
Cho documents quan trọng (production runbook, security policy, ADR lớn):

1. STAKEHOLDERS — Ai cần review doc này trước khi publish?
2. DEPENDENCIES — Doc này phụ thuộc vào docs nào khác?
3. LIFECYCLE — Bao lâu review 1 lần? (quarterly, yearly)
4. SENSITIVE DATA — Có chứa IPs, credentials, internal URLs không?
   → Nếu có: dùng placeholders theo docs/security-placeholders.md
```

---

## Ví dụ thực tế

**User request:** "Viết runbook cho Redis cluster"

**AI interview:**

```text
AI: Trước khi tạo runbook, tôi cần hỏi:

1. AUDIENCE: Ai sẽ dùng runbook này?
User: Team SRE, 5 người, senior level, đã biết Linux + Redis cơ bản.

2. SCOPE: Cover những gì?
User: Daily operations + troubleshooting. Không cover initial setup.

3. ENVIRONMENT: Production hay lab?
User: Production. Ubuntu 22.04, Redis 7.2, 3 nodes cluster + sentinel.

4. (Runbook-specific) SLA?
User: 99.9% uptime, P1 response 15 phút.

5. Common issues?
User: Memory full, replication lag, sentinel failover stuck.
```

**Sau interview → AI tạo doc với context đầy đủ:** audience đúng level, scope rõ ràng, commands cho đúng Redis 7.2 trên Ubuntu 22.04, troubleshooting cover đúng issues đã gặp.

---

## Tips

- **Không cần trả lời tất cả** — Layer 1 là bắt buộc, Layer 2 tùy loại doc, Layer 3 chỉ cho docs quan trọng
- **Càng chi tiết càng tốt** — "Redis 7.2 cluster 3 nodes" tốt hơn "Redis"
- **Nói rõ exclusions** — "Không cover setup từ đầu" giúp AI không lạc scope
- **Mention sensitive data sớm** — AI sẽ dùng placeholders từ đầu thay vì phải fix sau

---

> **Version:** 5.4.0 | **Updated:** 2026-03-30
