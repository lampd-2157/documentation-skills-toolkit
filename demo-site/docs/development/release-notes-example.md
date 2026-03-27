---
title: "Release Notes — v2.5.0"
description: "Major release with dark mode, API rate limiting, and performance improvements"
author: "Development Team"
created: 2026-03-26
updated: 2026-03-26
status: approved
tags: [release, v2.5.0, changelog]
---

# Release Notes — v2.5.0

**Date:** 2026-03-26 | **Author:** Development Team

## Highlights

- Dark mode support across all pages
- API rate limiting (100 req/min per user)
- 40% faster page load on dashboard

## New Features

| Feature              | Description                                       | Docs Link                          |
| -------------------- | ------------------------------------------------- | ---------------------------------- |
| Dark mode            | Toggle between light/dark themes in Settings      | User Guide |
| API rate limiting    | 100 requests/min per authenticated user           | API Docs   |
| Export to PDF        | Export any page as PDF via toolbar button          | How-to     |
| Bulk user import     | Import users from CSV file in Admin panel         | Admin Guide |

## Bug Fixes

| Issue                              | Fix                                    | Affected Area |
| ---------------------------------- | -------------------------------------- | ------------- |
| Dashboard timeout on large datasets | Added pagination (50 items/page)       | Dashboard     |
| Email notifications not sent       | Fixed SMTP config loading order        | Notifications |
| Search returns stale results       | Rebuilt search index on data change    | Search        |
| Mobile menu overlaps content       | Fixed z-index and responsive breakpoint | UI/Mobile     |

## Performance Improvements

| Metric         | Before   | After    | Improvement |
| -------------- | -------- | -------- | ----------- |
| Dashboard load | 2.1s     | 1.2s     | -43%        |
| API response   | 180ms    | 120ms    | -33%        |
| Search latency | 350ms    | 150ms    | -57%        |
| Bundle size    | 1.8 MB   | 1.2 MB   | -33%        |

!!! danger "Breaking Changes"

    **API v1 endpoints deprecated.** All `/api/v1/*` endpoints will be removed in v3.0.0. Migrate to `/api/v2/*` before then.

    Migration steps:

    1. Update API base URL from `/api/v1/` to `/api/v2/`
    2. Update authentication header from `X-API-Key` to `Authorization: Bearer <token>`
    3. Response format changed: `{ data: [...] }` wrapper added to all list endpoints

## Known Issues

| Issue                          | Workaround                    | ETA Fix |
| ------------------------------ | ----------------------------- | ------- |
| PDF export missing Mermaid diagrams | Screenshot diagrams manually | v2.5.1  |
| Dark mode flicker on first load    | Add `prefers-color-scheme` CSS | v2.5.1  |

## Upgrade Instructions

1. Pull latest code:
   ```bash
   git pull origin main
   ```

2. Install new dependencies:
   ```bash
   npm install
   ```

3. Run database migrations:
   ```bash
   npm run migrate
   ```

4. Restart application:
   ```bash
   sudo systemctl restart myapp
   ```

5. Verify:
   ```bash
   curl -s http://localhost:3000/health
   # Expected: {"status":"ok","version":"2.5.0"}
   ```
