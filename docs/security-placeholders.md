# Security Placeholders — Documentation Standards

> Quy chuẩn placeholder cho sensitive data trong documentation. Áp dụng cho tất cả docs tạo bởi toolkit.

---

## Tại sao cần placeholders?

Documentation thường chứa thông tin nhạy cảm: IP nội bộ, credentials, API tokens, internal URLs. Nếu docs được push lên Git (public hoặc shared repo), thông tin này bị lộ.

**Rule:** KHÔNG BAO GIỜ hardcode sensitive data trong docs. Luôn dùng placeholder format chuẩn.

---

## Placeholder Format

Tất cả placeholders dùng format `<UPPER_SNAKE_CASE>`:

### Network & Infrastructure

| Loại | Placeholder | Ví dụ sai | Ví dụ đúng |
|------|------------|-----------|------------|
| Internal IP | `<INTERNAL_IP>` | `10.0.1.50` | `<INTERNAL_IP>` hoặc `10.0.x.x` |
| Public IP | `<PUBLIC_IP>` | `203.0.113.50` | `<PUBLIC_IP>` |
| Hostname | `<HOSTNAME>` | `prod-db-01.company.local` | `<HOSTNAME>` |
| Internal URL | `<INTERNAL_URL>` | `https://jenkins.company.local` | `<INTERNAL_URL>` |
| Port (non-standard) | `<PORT>` | `8443` | `<PORT>` |
| VLAN ID (real) | `<VLAN_ID>` | `VLAN 150` | `<VLAN_ID>` |

### Credentials & Secrets

| Loại | Placeholder | Ví dụ sai | Ví dụ đúng |
|------|------------|-----------|------------|
| Password | `<PASSWORD>` | `P@ssw0rd123` | `<PASSWORD>` |
| API Token | `<API_TOKEN>` | `sk-abc123...` | `<API_TOKEN>` |
| SSH Key path | `<SSH_KEY_PATH>` | `/home/admin/.ssh/prod_key` | `<SSH_KEY_PATH>` |
| Database connection | `<DB_CONNECTION_STRING>` | `postgres://admin:pass@10.0.1.30/mydb` | `<DB_CONNECTION_STRING>` |
| AWS credentials | `<AWS_ACCESS_KEY>` | `AKIA...` | `<AWS_ACCESS_KEY>` |

### People & Organization

| Loại | Placeholder | Ví dụ sai | Ví dụ đúng |
|------|------------|-----------|------------|
| Email | `<EMAIL>` | `admin@company.com` | `<EMAIL>` |
| Phone | `<PHONE>` | `0912-345-678` | `<PHONE>` |
| Slack channel | `<SLACK_CHANNEL>` | `#prod-incidents` | `<SLACK_CHANNEL>` |
| Team name | `<TEAM_NAME>` | `SRE-Platform` | `<TEAM_NAME>` |

---

## Exceptions — Khi nào ĐƯỢC dùng real values

| Trường hợp | Cho phép | Lý do |
|-------------|---------|-------|
| RFC 5737 IPs | `192.0.2.x`, `198.51.100.x`, `203.0.113.x` | Reserved for documentation |
| RFC 2606 domains | `example.com`, `example.org` | Reserved for documentation |
| Localhost | `127.0.0.1`, `localhost` | Không phải sensitive |
| Public ports | `80`, `443`, `22`, `3306` | Well-known, không sensitive |
| Demo/lab data | IP bắt đầu `10.0.x.x` trong demo-site | Demo content, marked as example |

---

## Cách áp dụng

### Khi viết docs (AI Agent hoặc Manual)

```text
# Trong prompt hoặc khi viết:
Dùng <INTERNAL_IP> thay vì IP thực.
Dùng <PASSWORD> thay vì password thực.
Dùng example.com thay vì domain thực.
```

### Khi review docs

Chạy security scan:

```bash
make security-scan
```

### Pre-commit hook

Script tự động chạy khi commit — block nếu phát hiện secrets.

---

## Danh sách Patterns bị cấm

Các patterns sau sẽ bị `security-scan` flag:

| Pattern | Regex | Mô tả |
|---------|-------|-------|
| Private IP (10.x) | `10\.\d+\.\d+\.\d+` | Trừ demo-site/ |
| Private IP (172.16-31) | `172\.(1[6-9]\|2\d\|3[01])\.\d+\.\d+` | Internal network |
| Private IP (192.168) | `192\.168\.\d+\.\d+` | Internal network |
| Password in URL | `://[^:]+:[^@]+@` | Credentials in connection string |
| API key patterns | `(sk-\|api[_-]key\|bearer )[a-zA-Z0-9]` | Common API key formats |
| AWS keys | `AKIA[A-Z0-9]{16}` | AWS access key pattern |
| Slack webhook | `hooks\.slack\.com/services/` | Slack webhook URL |

---
