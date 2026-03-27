# Test Cases — infra-security-doc

## TC-1: Security policy

- **Prompt:** "Viết security policy cho team infrastructure"
- **Expected:** Security policy template
- **Verify:**
  - [ ] Policy ID, version, status, effective/review date
  - [ ] Purpose + Scope (applies to, exceptions)
  - [ ] Policy statements with enforcement details
  - [ ] Enforcement table (violation type, consequence, escalation)

## TC-2: Access control matrix

- **Prompt:** "Tạo access control matrix RBAC cho production environment"
- **Expected:** RBAC matrix template
- **Verify:**
  - [ ] Role definitions table (role, description, criteria)
  - [ ] Permission matrix (resource x role with CRUD)
  - [ ] Access review schedule

## TC-3: Audit log standards

- **Prompt:** "Định nghĩa audit log standards cho hệ thống"
- **Expected:** Audit log requirements doc
- **Verify:**
  - [ ] Event categories table (what must be logged)
  - [ ] Structured JSON log format example
  - [ ] Retention policy table
  - [ ] List of what must NOT be in logs

## TC-4: Vulnerability disclosure

- **Prompt:** "Viết vulnerability disclosure template"
- **Expected:** Vulnerability report template
- **Verify:**
  - [ ] Report metadata (ID, severity, CVSS, status)
  - [ ] Steps to reproduce
  - [ ] Impact assessment (CIA triad)
  - [ ] Remediation (short-term + long-term)
  - [ ] Timeline table

## TC-5: Security checklist (implicit trigger)

- **Prompt:** "Review bảo mật trước khi deploy service mới"
- **Expected:** Skill trigger dù không dùng từ "security doc"
- **Verify:**
  - [ ] Skill infra-security-doc được trigger
  - [ ] Pre-deploy security checklist output
  - [ ] Auth, network, data, monitoring, dependency sections
