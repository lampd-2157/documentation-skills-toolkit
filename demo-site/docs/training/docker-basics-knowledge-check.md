---
title: "Knowledge Check: Docker Basics"
description: "Bài kiểm tra kiến thức Docker cơ bản cho team"
author: Demo Team
created: 2026-03-25
updated: 2026-03-25
status: approved
tags: [training, docker, assessment]
---

# Knowledge Check: Docker Basics

| Field | Value |
|-------|-------|
| **Module** | Docker Fundamentals |
| **Audience** | Junior DevOps — Beginner |
| **Pass Criteria** | ≥ 80% correct |
| **Duration** | ~15 minutes |

## Multiple Choice

### Q1: Docker image vs container

Docker image và container khác nhau như thế nào?

??? question "Show Answer"
    **Answer:** Image là blueprint (read-only template), container là running instance của image.
    **Explanation:** Tương tự class vs object trong OOP. Image build 1 lần, chạy nhiều containers từ cùng 1 image.

### Q2: Dockerfile CMD vs ENTRYPOINT

Khi nào dùng CMD, khi nào dùng ENTRYPOINT?

??? question "Show Answer"
    **Answer:** ENTRYPOINT cho command chính (không thay đổi), CMD cho default arguments (có thể override).
    **Explanation:** Best practice: `ENTRYPOINT ["python3"]` + `CMD ["app.py"]` → user có thể override `CMD` khi `docker run`.

### Q3: Docker volume purpose

Tại sao cần Docker volumes?

??? question "Show Answer"
    **Answer:** Persist data beyond container lifecycle. Container xóa → data vẫn còn trong volume.
    **Explanation:** Without volumes, tất cả data mất khi container removed. Volumes mount host filesystem vào container.

## Scenario-based

### Scenario: Container không start được

**Given:** `docker run myapp` returns `Error: exec format error`
**When:** Team member báo lỗi trên production server (Linux AMD64)
**Expected:** Image được build trên Mac M1 (ARM64) — cần rebuild with `--platform linux/amd64` hoặc dùng multi-platform build.

## Assessment Summary

| Category | Questions | Pass Score | Learner Score | Status |
|----------|-----------|------------|---------------|--------|
| Multiple Choice | 3 | ≥ 2/3 | | |
| Scenario | 1 | Pass/Fail | | |
| **Total** | 4 | ≥ 80% | | |
