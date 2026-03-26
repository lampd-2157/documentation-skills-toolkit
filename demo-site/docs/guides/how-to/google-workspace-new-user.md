---
title: "How to: Tạo User Google Workspace mới"
description: "Hướng dẫn step-by-step tạo account Google Workspace cho nhân viên mới"
author: "IT Team"
created: 2026-03-26
updated: 2026-03-26
status: approved
tags: [google-workspace, how-to, onboarding]
---

# How to Tạo User Google Workspace Mới

> **Audience:** IT Admin / HR
> **Time:** ~10 minutes
> **Difficulty:** ⭐ Beginner

## Prerequisites

- [ ] Quyền Super Admin hoặc User Management Admin trên Google Workspace
- [ ] Thông tin nhân viên: họ tên, email, department, manager

## Steps

### Step 1: Truy cập Admin Console

Mở [admin.google.com](https://admin.google.com) → đăng nhập bằng admin account.

**Expected result:** Thấy Dashboard quản trị Google Workspace.

### Step 2: Tạo user mới

1. Navigate: **Directory** → **Users** → **Add new user**
2. Điền thông tin:

| Field         | Giá trị              |
| ------------- | -------------------- |
| First name    | [Tên]                |
| Last name     | [Họ]                 |
| Primary email | `ten.ho@company.com` |
| Org unit      | `/{Department}`      |

3. Click **Add new user**

**Expected result:** User xuất hiện trong danh sách. Email chào mừng được gửi.

!!! tip
    Dùng naming convention: `firstname.lastname@company.com` để đồng nhất.

### Step 3: Add user vào Groups

1. Navigate: **Directory** → **Groups**
2. Click vào group cần add (ví dụ: `team-infra@company.com`)
3. **Add members** → nhập email user mới → **Add**

**Expected result:** User nhận email notification về group membership.

### Step 4: Enable 2FA

1. Navigate: **Security** → **2-Step Verification**
2. Đảm bảo policy "Enforcement" cho OU của user mới
3. Thông báo user setup 2FA trong **7 ngày đầu**

!!! warning
    Nếu user không setup 2FA trong thời hạn, account sẽ bị lock theo policy.

## Verify

- [ ] User đăng nhập thành công tại [accounts.google.com](https://accounts.google.com)
- [ ] User nhận được email từ groups đã add
- [ ] 2FA enrolled (kiểm tra tại Admin Console → User details)

## Troubleshooting

### Error: "This email address is already in use"

**Cause:** Email đã tồn tại (có thể đã bị xóa nhưng chưa quá 20 ngày)
**Fix:**

1. Admin Console → **Directory** → **Users**
2. Filter: **Recently deleted**
3. Nếu thấy user → **Delete permanently** hoặc **Restore** rồi rename

### Error: User không nhận email group

**Cause:** Group delivery settings = "All emails" chưa bật
**Fix:**

1. Google Groups → Group settings
2. Verify member delivery preference = "Each email"

## Next Steps

- [Security 2FA Guide](../security-2fa.md) — Chi tiết setup 2FA
- [Proxmox VM Runbook](../../operations/runbooks/proxmox-vm-runbook.md) — Setup VM cho user mới
