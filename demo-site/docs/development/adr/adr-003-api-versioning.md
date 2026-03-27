---
title: "ADR-003: Use URL Path Versioning for API"
description: "Quick decision — API versioning strategy"
author: Demo Team
created: 2026-03-20
updated: 2026-03-20
status: accepted
tags: [adr, api, versioning]
---

# ADR: Use URL Path Versioning for API

**Date:** 2026-03-20 | **Status:** Accepted | **Author:** Tech Lead

## Problem

API cần versioning strategy. Team nhỏ (5 developers), 2 API consumers (mobile app + web dashboard).

## Decision

Dùng URL path versioning: `/api/v1/users`, `/api/v2/users`.

## Reason

Đơn giản nhất, dễ debug (version visible trong URL), team đã quen pattern này từ project trước. Header-based versioning phức tạp hơn không cần thiết cho scale hiện tại.

## Impact

- API routes có prefix `/api/v{N}/`
- Khi cần breaking change → tạo version mới, maintain cũ 6 tháng
- Docs cần update per-version
