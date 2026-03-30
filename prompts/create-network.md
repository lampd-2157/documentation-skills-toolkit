# Prompt: Tạo Network Topology Document

> **Skill:** ops-runbook-writer | **Template:** T5 | **Output:** Tài liệu hạ tầng mạng

## Cách dùng

### AI Agent (Recommended)

1. Copy toàn bộ nội dung trong khung **Prompt** bên dưới
2. Mở AI agent bạn đang dùng (Claude, ChatGPT, Antigravity, Copilot...)
3. Paste prompt vào, sau đó **sửa dòng "Tạo network topology document cho:"** — thay đoạn mô tả ví dụ bằng hạ tầng mạng thực tế
4. Gửi prompt → AI tạo document → bạn review kết quả
5. Chạy `make lint` để verify markdown format

**Ví dụ thực tế:** Nếu bạn cần document hạ tầng AWS VPC, sửa thành:

```text
Bước 3: Tạo network topology document cho:
AWS VPC production: 3 AZs, public/private subnets mỗi AZ,
NAT gateway, ALB, 20 EC2 instances, RDS Multi-AZ.
```

### Manual

```bash
./scripts/docs-toolkit new network "AWS VPC Production"
```

Sau đó mở file vừa tạo, đọc `skills/ops-runbook-writer.md` (phần Iron Law + Guardrails), điền nội dung thủ công.

---

## Phase 0: Interview (Recommended)

Trước khi tạo doc, hãy hỏi user để gather context. Copy câu hỏi từ [interview-before-create.md](interview-before-create.md) hoặc hỏi tối thiểu 3 câu:

1. **Audience:** Ai đọc doc này? Role + level?
2. **Scope:** Cover gì? Không cover gì?
3. **Environment:** Production/lab? OS? Versions?

> Có answers rồi? Tiếp tục với prompt bên dưới — thay thông tin vào đoạn `<<<< SỬA >>>>`.

---

## Prompt

```text
Bạn là Documentation Agent. Hãy tạo network topology document.

Bước 1: Đọc file skills/ops-runbook-writer.md — ghi nhớ Iron Law và Guardrails.
Bước 2: Đọc file templates/network-topology.md — đây là cấu trúc output.
Bước 3: Tạo network topology document cho:

Production environment gồm 3 VLAN (Management, Application, Database),
2 firewall zones, 10 servers, kết nối Internet qua 2 ISP.

IP ranges: 10.0.1.0/24 (Mgmt), 10.0.2.0/24 (App), 10.0.3.0/24 (DB).
<<<< SỬA ĐOẠN NÀY THÀNH HẠ TẦNG MẠNG CỦA BẠN >>>>

Yêu cầu bắt buộc (Iron Law):
- Mọi command kiểm tra PHẢI copy-paste chạy được ngay
- PHẢI có diagram (Mermaid) hoặc bảng mô tả topology
- PHẢI có server inventory table (hostname, IP, role, OS)

UI Standards:
- Dùng admonitions (!!! info/warning/danger) cho metadata và cảnh báo
- Dùng task lists (- [ ]) cho checklists
- Commands dài (>60 chars) đặt trong code blocks, không trong table cells

Security:
- KHÔNG hardcode IP, password, token, internal URL — dùng placeholders: <INTERNAL_IP>, <PASSWORD>, <API_TOKEN>

Flexible Sections:
- Required sections: PHẢI có (xem template header comment)
- Recommended sections: NÊN có nếu relevant
- Optional sections: ĐƯỢC thêm nếu phù hợp context (ví dụ: Rollback, Security Notes, FAQ)

Tự kiểm tra trước khi hoàn thành:
- [ ] VLAN layout rõ ràng (ID, subnet, purpose)
- [ ] Firewall rules documented
- [ ] Server inventory table đầy đủ
- [ ] Có diagram (Mermaid) hoặc ASCII topology
- [ ] Health check commands cho network devices
- [ ] Đã thêm vào mkdocs.yml nav section
```
