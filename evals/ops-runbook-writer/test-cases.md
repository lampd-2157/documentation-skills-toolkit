# Test Cases — ops-runbook-writer

## TC-1: Viết runbook cơ bản

- **Prompt:** "Viết runbook cho service nginx trên Ubuntu 22.04"
- **Expected:** Runbook đầy đủ theo SkeltonThatcher template
- **Verify:**
  - [ ] YAML header có title, status, updated
  - [ ] Health Checks table với command + expected output
  - [ ] Common Tasks: Start/Stop/Restart commands
  - [ ] Troubleshooting section với root cause + fix
  - [ ] Escalation matrix (P1-P4)

## TC-2: Network topology documentation

- **Prompt:** "Document network topology cho production với 3 VLAN"
- **Expected:** Network docs theo Section 3 template
- **Verify:**
  - [ ] Mermaid diagram topology
  - [ ] VLAN Layout table (ID, Name, Subnet, Purpose)
  - [ ] Firewall Rules Summary table

## TC-3: Incident response playbook

- **Prompt:** "Tạo incident response playbook cho database outage"
- **Expected:** Incident SOP với severity classification
- **Verify:**
  - [ ] Severity matrix (P1-P4) với response time
  - [ ] Step-by-step commands với expected output
  - [ ] Rollback procedure
  - [ ] Escalation contacts

## TC-4: Implicit trigger test

- **Prompt:** "Hệ thống bị lỗi, cần quy trình xử lý"
- **Expected:** Skill trigger dù không dùng từ "runbook"
- **Verify:**
  - [ ] Skill ops-runbook-writer được trigger
  - [ ] Output có incident response structure

## TC-5: Maintenance window

- **Prompt:** "Viết maintenance window plan cho database migration"
- **Expected:** Maintenance window template đầy đủ
- **Verify:**
  - [ ] Pre-checks checklist
  - [ ] Steps với commands
  - [ ] Post-checks
  - [ ] Rollback plan documented
