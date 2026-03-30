---
title: "API Reference — Task Management API"
status: approved
updated: 2026-03-30
tags:
  - api
  - T13
  - example
---

# Task Management API — Reference

!!! info "API Overview"
    | Field | Value |
    |-------|-------|
    | **Base URL** | `https://api.example.com/v1` |
    | **Version** | v1.0.0 |
    | **Format** | JSON |
    | **Auth** | Bearer token (JWT) |
    | **Rate limit** | 100 requests/minute |

## Authentication

All requests require a Bearer token in the `Authorization` header.

```bash
curl -X GET https://api.example.com/v1/tasks \
  -H "Authorization: Bearer <API_TOKEN>" \
  -H "Content-Type: application/json"
```

!!! warning "Token expiry"
    Tokens expire after 24 hours. Use the `/auth/refresh` endpoint to obtain a new token.

## Endpoints

### `GET /tasks`

List all tasks for the authenticated user.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `status` | string | No | Filter by status: `todo`, `in_progress`, `done` |
| `page` | integer | No | Page number (default: 1) |
| `per_page` | integer | No | Items per page (default: 20, max: 100) |

**Request:**

```bash
curl -X GET "https://api.example.com/v1/tasks?status=todo&page=1&per_page=10" \
  -H "Authorization: Bearer <API_TOKEN>"
```

**Response (200 OK):**

```json
{
  "data": [
    {
      "id": "task-001",
      "title": "Update documentation",
      "status": "todo",
      "priority": "high",
      "assignee": "user-123",
      "created_at": "2026-03-28T10:00:00Z",
      "updated_at": "2026-03-28T10:00:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "per_page": 10,
    "total": 42,
    "total_pages": 5
  }
}
```

### `GET /tasks/:id`

Get a specific task by ID.

**Request:**

```bash
curl -X GET https://api.example.com/v1/tasks/task-001 \
  -H "Authorization: Bearer <API_TOKEN>"
```

**Response (200 OK):**

```json
{
  "id": "task-001",
  "title": "Update documentation",
  "description": "Update the API reference docs for v1.0",
  "status": "todo",
  "priority": "high",
  "assignee": "user-123",
  "project_id": "proj-abc",
  "tags": ["docs", "urgent"],
  "created_at": "2026-03-28T10:00:00Z",
  "updated_at": "2026-03-28T10:00:00Z",
  "due_date": "2026-04-01T00:00:00Z"
}
```

### `POST /tasks`

Create a new task.

**Request body:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | string | Yes | Task title (max 200 chars) |
| `description` | string | No | Task description (max 5000 chars) |
| `status` | string | No | Initial status (default: `todo`) |
| `priority` | string | No | `low`, `medium`, `high` (default: `medium`) |
| `assignee` | string | No | User ID to assign |
| `project_id` | string | No | Project to associate |
| `due_date` | string | No | ISO 8601 date |

**Request:**

```bash
curl -X POST https://api.example.com/v1/tasks \
  -H "Authorization: Bearer <API_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Deploy v2.0 to staging",
    "description": "Deploy the latest release to staging environment",
    "priority": "high",
    "assignee": "user-456",
    "project_id": "proj-abc",
    "due_date": "2026-04-05T00:00:00Z"
  }'
```

**Response (201 Created):**

```json
{
  "id": "task-002",
  "title": "Deploy v2.0 to staging",
  "description": "Deploy the latest release to staging environment",
  "status": "todo",
  "priority": "high",
  "assignee": "user-456",
  "project_id": "proj-abc",
  "tags": [],
  "created_at": "2026-03-30T14:00:00Z",
  "updated_at": "2026-03-30T14:00:00Z",
  "due_date": "2026-04-05T00:00:00Z"
}
```

### `PUT /tasks/:id`

Update an existing task.

**Request:**

```bash
curl -X PUT https://api.example.com/v1/tasks/task-001 \
  -H "Authorization: Bearer <API_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "status": "in_progress",
    "priority": "medium"
  }'
```

**Response (200 OK):**

```json
{
  "id": "task-001",
  "title": "Update documentation",
  "status": "in_progress",
  "priority": "medium",
  "updated_at": "2026-03-30T15:00:00Z"
}
```

### `DELETE /tasks/:id`

Delete a task. This action is irreversible.

**Request:**

```bash
curl -X DELETE https://api.example.com/v1/tasks/task-001 \
  -H "Authorization: Bearer <API_TOKEN>"
```

**Response (204 No Content):**

No response body.

## Error Codes

| Status | Code | Description | Example |
|--------|------|-------------|---------|
| 400 | `bad_request` | Invalid request body or parameters | Missing required field `title` |
| 401 | `unauthorized` | Missing or invalid auth token | Expired JWT token |
| 403 | `forbidden` | Insufficient permissions | Editing another user's task |
| 404 | `not_found` | Resource does not exist | Task ID not found |
| 409 | `conflict` | Resource state conflict | Task already deleted |
| 422 | `validation_error` | Request body validation failed | `priority` must be low/medium/high |
| 429 | `rate_limited` | Too many requests | Exceeded 100 req/min |
| 500 | `internal_error` | Server error | Unexpected failure |

**Error response format:**

```json
{
  "error": {
    "code": "not_found",
    "message": "Task with ID 'task-999' not found",
    "request_id": "req-abc-123"
  }
}
```

## Rate Limits

| Plan | Limit | Burst |
|------|-------|-------|
| Free | 60 requests/min | 10 |
| Pro | 300 requests/min | 50 |
| Enterprise | 1000 requests/min | 100 |

Rate limit headers are included in every response:

```text
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1711800000
```

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v1.0.0 | 2026-03-30 | Initial release — CRUD tasks, projects |
| v0.9.0 | 2026-03-15 | Beta — task endpoints only |
