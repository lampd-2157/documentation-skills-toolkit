---
name: infra-security-doc
description: "Viết tài liệu bảo mật hạ tầng (.md): security policy, access control
  matrix (RBAC/ABAC), audit log standards, vulnerability disclosure, security checklist.
  Dùng skill này khi người dùng đề cập đến: chính sách bảo mật, phân quyền truy cập,
  audit log, vulnerability report, security review, hardening checklist, compliance
  documentation — dù không gọi đích danh là 'security doc'. Khi có từ khóa: security,
  bảo mật, RBAC, access control, audit, vulnerability, compliance, hardening,
  firewall policy, secret management, encryption → trigger skill này."
compatibility: "MkDocs Material >= 9.0"
---

# Skill: Infra Security Doc

## Viết tài liệu Bảo mật Hạ tầng

**Agent:** 📝 [Documentation Agent]
**Source:** Adapted — [NIST SP 800-53](https://csf.tools/reference/nist-sp-800-53/), [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks), [OWASP](https://owasp.org/)

---

## Context / Bối cảnh

| Key          | Value                                                                                                |
| ------------ | ---------------------------------------------------------------------------------------------------- |
| **Category** | security / docs                                                                                      |
| **Priority** | high                                                                                                 |
| **Triggers** | Khi cần viết security policy, access control docs, audit standards, vulnerability disclosure         |
| **Output**   | Security policy .md, access control matrix .md, audit log standards .md, security checklist .md      |
| **Scope**        | IN: security policy, access control, audit logs, vulnerability, compliance. OUT: runbook, training |
| **Version**      | 1.0.0                                                                                                |
| **Last Updated** | 2026-03-27                                                                                           |

> Chuyên viết tài liệu bảo mật hạ tầng. Mọi security doc phải có scope rõ ràng, enforcement mechanism, và review schedule.

---

## ⛔ THE IRON LAW

**Every security doc MUST have Scope → Policy → Enforcement → Audit — policy without enforcement = decoration.**

---

## 🛡 Guardrails

- [ ] Không chứa credentials, keys, hoặc secrets thực tế — chỉ dùng placeholders
- [ ] Scope xác định rõ: áp dụng cho ai, hệ thống nào, từ khi nào
- [ ] Review schedule defined — security docs PHẢI có expiry/review date
- [ ] Compliance framework referenced (nếu applicable): NIST, CIS, ISO 27001

---

## 🎯 Khi nào dùng Skill này

```text
User request
  ├── Viết security policy / hardening guide?
  │     └── YES → Dùng skill này (Section 1)
  ├── Tạo access control matrix (RBAC/ABAC)?
  │     └── YES → Dùng skill này (Section 2)
  ├── Định nghĩa audit log standards?
  │     └── YES → Dùng skill này (Section 3)
  ├── Viết vulnerability disclosure template?
  │     └── YES → Dùng skill này (Section 4)
  ├── Tạo security checklist cho infra changes?
  │     └── YES → Dùng skill này (Section 5)
  └── Viết runbook / ops docs?
        └── NO  → Xem ops-runbook-writer.md
```

| Dùng skill này khi...               | KHÔNG dùng khi...              |
| ------------------------------------ | ------------------------------ |
| Viết security policy                 | Viết runbook vận hành          |
| Tạo access control matrix            | Viết training material         |
| Định nghĩa audit log standards      | Document network topology      |
| Viết vulnerability disclosure        | Viết ADR / tech spec           |
| Tạo security checklist              | Setup MkDocs platform          |

---

## 1. Security Policy Documentation

### 1.1 Security Policy Template

```markdown
# Security Policy: [Policy Name]

| Field              | Value                                      |
| ------------------ | ------------------------------------------ |
| **Policy ID**      | SEC-[NNN]                                  |
| **Version**        | [1.0]                                      |
| **Status**         | Draft / Active / Under Review / Deprecated |
| **Effective date** | YYYY-MM-DD                                 |
| **Review date**    | YYYY-MM-DD (mỗi 6 tháng)                   |
| **Owner**          | [Team/Person]                              |
| **Approved by**    | [Manager/CISO]                             |

## Purpose
[Tại sao policy này tồn tại — 1-2 câu]

## Scope
- **Applies to:** [Teams, systems, environments]
- **Exceptions:** [Nếu có, liệt kê rõ]

## Policy Statements
1. **[Statement 1]** — [Chi tiết enforcement]
2. **[Statement 2]** — [Chi tiết enforcement]
3. **[Statement 3]** — [Chi tiết enforcement]

## Enforcement
| Violation type | Consequence             | Escalation        |
| -------------- | ----------------------- | ----------------- |
| Minor          | Warning + remediation   | Team lead         |
| Major          | Access revoked + review | Security team     |
| Critical       | Immediate lockdown      | CISO + Management |

## Related Documents
- [Link to related policies]
- [Link to compliance framework]
```

### 1.2 Infrastructure Hardening Checklist

```markdown
## Hardening Checklist: [OS/Service Name]

### OS Level
- [ ] Disable root SSH login (`PermitRootLogin no`)
- [ ] SSH key-only authentication (`PasswordAuthentication no`)
- [ ] Firewall enabled — default deny inbound
- [ ] Automatic security updates enabled
- [ ] Unused services disabled
- [ ] File system permissions verified (no world-writable)

### Network Level
- [ ] TLS 1.2+ only — disable SSLv3, TLS 1.0/1.1
- [ ] Certificate valid and auto-renew configured
- [ ] DNS security (DNSSEC if applicable)
- [ ] Network segmentation verified (VLAN isolation)

### Application Level
- [ ] Dependencies up-to-date — no known CVEs
- [ ] Secrets in vault/env vars — NEVER in code/docs
- [ ] Logging enabled — audit events captured
- [ ] Rate limiting configured
- [ ] CORS policy restrictive

### Monitoring
- [ ] Failed login alerts configured
- [ ] Disk/CPU/Memory alerts active
- [ ] Certificate expiry monitoring (>30 days warning)
- [ ] Log aggregation active (ELK/Loki/CloudWatch)
```

---

## 2. Access Control Matrix

### 2.1 RBAC Matrix Template

```markdown
## Access Control Matrix — [System/Environment]

### Role Definitions
| Role            | Description                        | Assignment criteria       |
| --------------- | ---------------------------------- | ------------------------- |
| **Admin**       | Full access, system configuration  | Infrastructure team leads |
| **Operator**    | Deploy, restart, read logs         | On-call engineers         |
| **Developer**   | Read logs, access staging          | Development team          |
| **Auditor**     | Read-only, audit logs              | Security/compliance team  |
| **Viewer**      | Read documentation only            | All employees             |

### Permission Matrix
| Resource            | Admin | Operator | Developer | Auditor | Viewer |
| ------------------- | ----- | -------- | --------- | ------- | ------ |
| Production servers  | CRUD  | RU       | R         | R       | —      |
| Staging servers     | CRUD  | CRUD     | RU        | R       | —      |
| Database (prod)     | CRUD  | R        | —         | R       | —      |
| Database (staging)  | CRUD  | CRUD     | CRUD      | R       | —      |
| Secrets vault       | CRUD  | R        | —         | R       | —      |
| Monitoring dashboards | CRUD | R       | R         | R       | R      |
| Documentation       | CRUD  | CRUD     | CRUD      | R       | R      |
| Audit logs          | R     | —        | —         | R       | —      |

> **Legend:** C=Create, R=Read, U=Update, D=Delete, —=No access

### Access Review Schedule
| Review type       | Frequency  | Owner          | Action                     |
| ----------------- | ---------- | -------------- | -------------------------- |
| Role assignment   | Quarterly  | Team leads     | Verify role still needed   |
| Permission audit  | Bi-annually | Security team | Check least-privilege      |
| Offboarding       | On event   | HR + IT        | Revoke all within 24h     |
| Service accounts  | Monthly    | Infrastructure | Rotate keys, verify usage  |
```

---

## 3. Audit Log Standards

### 3.1 Audit Log Requirements

````markdown
## Audit Log Standards — [Organization/System]

### What MUST be logged
| Event category          | Examples                                        | Severity |
| ----------------------- | ----------------------------------------------- | -------- |
| **Authentication**      | Login success/fail, MFA events, token refresh   | High     |
| **Authorization**       | Permission denied, role changes, privilege escalation | Critical |
| **Data access**         | Read/write sensitive data, export, bulk queries  | High     |
| **Configuration**       | System config changes, firewall rule changes     | Critical |
| **Administrative**      | User create/delete, role assignment, key rotation | High    |

### Log format (structured JSON)
```json
{
  "timestamp": "2026-03-27T10:30:00Z",
  "level": "INFO",
  "event": "user.login.success",
  "actor": {
    "id": "user-123",
    "ip": "10.0.1.50",
    "user_agent": "Mozilla/5.0..."
  },
  "resource": {
    "type": "session",
    "id": "sess-456"
  },
  "metadata": {
    "mfa_used": true,
    "geo": "VN"
  }
}
```

### Retention Policy
| Log type           | Retention | Storage          | Access          |
| ------------------ | --------- | ---------------- | --------------- |
| Authentication     | 1 year    | S3 + hot 30 days | Security team   |
| Authorization      | 2 years   | S3 + hot 90 days | Security + Audit |
| Application        | 90 days   | ELK/Loki         | Dev + Ops       |
| Infrastructure     | 1 year    | S3 + hot 30 days | Infrastructure  |

### What MUST NOT be in logs
- Passwords or password hashes
- API keys, tokens, secrets
- Full credit card numbers (mask: `****1234`)
- Personal data beyond what's necessary (GDPR)
````

---

## 4. Vulnerability Disclosure

### 4.1 Vulnerability Disclosure Template

```markdown
## Vulnerability Report: [Title]

| Field              | Value                              |
| ------------------ | ---------------------------------- |
| **Report ID**      | VULN-[YYYY]-[NNN]                 |
| **Date reported**  | YYYY-MM-DD                         |
| **Reporter**       | [Internal/External — name if okay] |
| **Severity**       | Critical / High / Medium / Low     |
| **CVSS score**     | [0.0-10.0] (nếu applicable)       |
| **Status**         | New / Triaged / In Progress / Fixed / Won't Fix |
| **Affected system** | [System/service name + version]   |

## Description
[Mô tả vulnerability — what, where, how it can be exploited]

## Steps to Reproduce
1. [Step 1]
2. [Step 2]
3. [Observed result vs expected result]

## Impact Assessment
- **Confidentiality:** [High/Medium/Low/None]
- **Integrity:** [High/Medium/Low/None]
- **Availability:** [High/Medium/Low/None]

## Remediation
- **Short-term (mitigate):** [Workaround/mitigation steps]
- **Long-term (fix):** [Permanent fix plan]
- **ETA:** [Target date for fix]

## Timeline
| Date       | Action                    |
| ---------- | ------------------------- |
| YYYY-MM-DD | Vulnerability reported    |
| YYYY-MM-DD | Triaged + severity set    |
| YYYY-MM-DD | Fix development started   |
| YYYY-MM-DD | Fix deployed to staging   |
| YYYY-MM-DD | Fix deployed to production |
| YYYY-MM-DD | Reporter notified         |
```

---

## 5. Security Checklist cho Infrastructure Changes

### 5.1 Pre-Deploy Security Review

```markdown
## Security Review: [Change Title]

### Change Details
| Field           | Value                    |
| --------------- | ------------------------ |
| **Change type** | [Deploy/Config/Network]  |
| **Requester**   | [Name]                   |
| **Reviewer**    | [Security team member]   |
| **Date**        | YYYY-MM-DD               |

### Checklist
#### Authentication & Authorization
- [ ] No hardcoded credentials in code/config
- [ ] Service accounts use minimal required permissions
- [ ] API keys rotated if exposed or stale (>90 days)
- [ ] MFA required for admin access

#### Network & Communication
- [ ] TLS enforced for all external communication
- [ ] Internal service-to-service auth configured (mTLS/tokens)
- [ ] Firewall rules reviewed — no unnecessary open ports
- [ ] CORS/CSP headers configured correctly

#### Data Protection
- [ ] Sensitive data encrypted at rest
- [ ] PII handling compliant with privacy policy
- [ ] Backup encryption verified
- [ ] Log masking for secrets/PII confirmed

#### Monitoring & Logging
- [ ] Audit logging enabled for new endpoints/services
- [ ] Alert rules configured for security events
- [ ] Log retention matches compliance requirements

#### Dependency & Supply Chain
- [ ] No known CVEs in dependencies (`npm audit` / `pip audit`)
- [ ] Base images from trusted registries
- [ ] Dependency lock files committed

### Sign-off
| Role            | Name | Date       | Approved |
| --------------- | ---- | ---------- | -------- |
| Security reviewer | —  | YYYY-MM-DD | [ ]      |
| Tech lead       | —    | YYYY-MM-DD | [ ]      |
```

---

## ✅ Pre-delivery Checklist — Security Docs

Trước khi báo "done", verify:

- [ ] KHÔNG chứa secrets, keys, passwords thực tế — chỉ placeholders
- [ ] Scope rõ ràng — ai, hệ thống nào, từ khi nào
- [ ] Enforcement mechanism defined — policy without enforcement = useless
- [ ] Review/expiry date set — security docs PHẢI có schedule review
- [ ] Compliance framework referenced (nếu applicable)
- [ ] markdownlint pass — 0 errors

---

## 📓 Error Journal — Never Repeat Failures

| Date     | Error                             | Root Cause             | Prevention Rule                  |
| -------- | --------------------------------- | ---------------------- | -------------------------------- |
| template | Real password in security doc     | Copy-paste from config | ALWAYS search for secrets before publish |
| template | Access matrix outdated after reorg | No review schedule    | Quarterly access review mandatory |
| template | Missing audit logs for new API    | Forgot logging config  | Security checklist gate for deploys |

> **Rule:** Mỗi lần phát hiện security doc error → thêm 1 row.

---

## 🚩 Red Flags — STOP

| Action                                | Problem                                          |
| ------------------------------------- | ------------------------------------------------ |
| Real credentials in doc               | → IMMEDIATELY remove + rotate affected keys      |
| Policy without enforcement mechanism  | → Policy = decoration, thêm enforcement section  |
| Access matrix without review schedule | → Sẽ outdated trong 3 tháng, thêm review cadence |
| Security checklist quá generic        | → Customize cho specific system/change type       |
| No compliance reference               | → Xác định applicable framework (NIST/CIS/ISO)   |

---

## Remember

| Rule                   | Description                                          |
| ---------------------- | ---------------------------------------------------- |
| **No real secrets**    | NEVER include actual credentials — placeholders only |
| **Scope first**        | Define who, what, when BEFORE writing policy          |
| **Enforce or delete**  | Policy without enforcement = wasted effort            |
| **Review cadence**     | Every security doc needs a review/expiry date         |
| **Least privilege**    | Default to minimal access, grant more when justified  |
| **Log everything**     | Authentication, authorization, config changes         |

## 🔗 Related Skills

| Khi cần...                       | Xem skill                              |
| -------------------------------- | -------------------------------------- |
| Viết runbook / ops docs          | `ops-runbook-writer.md`  |
| Setup MkDocs, markdown standards | `docs-engineer.md`       |
| Viết training / onboarding docs  | `training-doc-writer.md` |
| Viết ADR, guide, tech spec       | `project-doc-writer.md`  |

> **See also:** [Templates](../templates/)

<!-- Used: 2026-03-27 -->
