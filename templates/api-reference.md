<!-- Template T13: API Reference — Copy this file and customize -->
<!-- sections:
  required: [Overview, Endpoints, Error Codes]
  recommended: [Authentication, Rate Limits, Changelog]
  optional: [SDKs, Webhooks, Migration Guide]
-->
# [API Name] — API Reference

!!! info "Document Metadata"
    | Field | Value |
    |-------|-------|
    | **Base URL** | `https://api.example.com/v1` |
    | **Version** | v1.0.0 |
    | **Auth** | Bearer Token / API Key |
    | **Format** | JSON |

## Overview

[1-2 sentences: what this API does and who uses it]

## Authentication

All requests require authentication via Bearer token in the `Authorization` header:

```bash
curl -H "Authorization: Bearer <API_TOKEN>" \
  https://api.example.com/v1/resource
```

| Method | Header | Example |
|--------|--------|---------|
| Bearer Token | `Authorization: Bearer <token>` | API access |
| API Key | `X-API-Key: <key>` | Service-to-service |

## Endpoints

### `GET /resources`

List all resources.

**Parameters:**

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `page` | integer | No | 1 | Page number |
| `limit` | integer | No | 20 | Items per page (max 100) |
| `status` | string | No | — | Filter by status: `active`, `archived` |

**Request:**

```bash
curl -H "Authorization: Bearer <API_TOKEN>" \
  "https://api.example.com/v1/resources?page=1&limit=10"
```

**Response (200 OK):**

```json
{
  "data": [
    {
      "id": "res_abc123",
      "name": "Example Resource",
      "status": "active",
      "created_at": "2026-01-15T10:30:00Z"
    }
  ],
  "meta": {
    "page": 1,
    "limit": 10,
    "total": 42
  }
}
```

### `GET /resources/:id`

Get a single resource by ID.

**Request:**

```bash
curl -H "Authorization: Bearer <API_TOKEN>" \
  https://api.example.com/v1/resources/res_abc123
```

**Response (200 OK):**

```json
{
  "id": "res_abc123",
  "name": "Example Resource",
  "status": "active",
  "config": {},
  "created_at": "2026-01-15T10:30:00Z",
  "updated_at": "2026-03-30T08:00:00Z"
}
```

### `POST /resources`

Create a new resource.

**Request body:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | Resource name (1-255 chars) |
| `config` | object | No | Configuration object |

**Request:**

```bash
curl -X POST \
  -H "Authorization: Bearer <API_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"name": "New Resource", "config": {}}' \
  https://api.example.com/v1/resources
```

**Response (201 Created):**

```json
{
  "id": "res_def456",
  "name": "New Resource",
  "status": "active",
  "config": {},
  "created_at": "2026-03-30T12:00:00Z"
}
```

### `PUT /resources/:id`

Update a resource.

**Request body:** Same as POST (all fields optional for partial update).

**Response (200 OK):** Updated resource object.

### `DELETE /resources/:id`

Delete a resource.

**Response (204 No Content):** Empty body on success.

## Error Codes

| HTTP Code | Error Code | Description | Resolution |
|-----------|-----------|-------------|------------|
| 400 | `invalid_request` | Malformed request body | Check JSON syntax and required fields |
| 401 | `unauthorized` | Missing or invalid token | Verify API token is valid and not expired |
| 403 | `forbidden` | Insufficient permissions | Check token scopes / user role |
| 404 | `not_found` | Resource does not exist | Verify resource ID |
| 409 | `conflict` | Resource already exists | Use unique name or update existing |
| 422 | `validation_error` | Invalid field values | Check field constraints in docs |
| 429 | `rate_limited` | Too many requests | Wait and retry with backoff |
| 500 | `internal_error` | Server error | Retry; contact support if persistent |

**Error response format:**

```json
{
  "error": {
    "code": "validation_error",
    "message": "Name must be between 1 and 255 characters",
    "details": [
      {"field": "name", "issue": "too_long"}
    ]
  }
}
```

## Rate Limits

| Tier | Limit | Window | Headers |
|------|-------|--------|---------|
| Free | 100 req | per minute | `X-RateLimit-Limit`, `X-RateLimit-Remaining` |
| Pro | 1000 req | per minute | `X-RateLimit-Reset` (Unix timestamp) |

When rate limited, the API returns `429` with a `Retry-After` header (seconds).

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v1.0.0 | YYYY-MM-DD | Initial release |
