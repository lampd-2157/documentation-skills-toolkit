---
name: api-doc-writer
description: "Viết tài liệu API (.md): REST API reference, GraphQL schema docs,
  gRPC service docs, webhook documentation, SDK guides. Dùng skill này khi
  người dùng đề cập đến: tạo API docs, viết endpoint reference, document API,
  OpenAPI spec, Swagger, request/response examples — dù không gọi đích danh.
  Khi có từ khóa: API, endpoint, REST, GraphQL, gRPC, webhook, SDK,
  OpenAPI, Swagger, request, response, HTTP method, rate limit, API key,
  bearer token, pagination, versioning API → trigger skill này."
compatibility: "MkDocs Material >= 9.0"
skill_version: "1.0.0"
---

# Skill: API Doc Writer

## Viết tài liệu API Reference & Integration Guide

**Agent:** 📡 [Documentation Agent]
**Source:** Adapted — [Google API Design Guide](https://cloud.google.com/apis/design), [Stripe API Docs](https://stripe.com/docs/api), [Microsoft REST API Guidelines](https://github.com/microsoft/api-guidelines)

---

## Context / Bối cảnh

| Key          | Value                                                                                               |
| ------------ | --------------------------------------------------------------------------------------------------- |
| **Category** | docs                                                                                                |
| **Priority** | high                                                                                                |
| **Triggers** | Khi cần viết API reference, endpoint docs, SDK guide, webhook docs                                  |
| **Output**   | API reference .md, endpoint docs .md, integration guide .md                                         |
| **Scope**        | IN: REST API, GraphQL, gRPC, webhooks, SDK docs. OUT: architecture decisions, runbooks, training |
| **Version**      | 1.0.0                                                                                               |
| **Last Updated** | 2026-03-30                                                                                          |

> Chuyên viết tài liệu API. Mọi endpoint PHẢI có request example + response example + error codes. API docs phải đủ chi tiết để developer integrate mà không cần hỏi thêm.

---

## ⛔ THE IRON LAW

**Every API doc MUST have request example + response example + error codes for EVERY endpoint — docs without examples = useless docs.**

---

## 🛡 Guardrails

- [ ] Mỗi endpoint có: Method + Path + Parameters + Request example + Response example
- [ ] Error codes table có ≥ 5 HTTP status codes (400, 401, 403, 404, 500)
- [ ] Authentication section rõ ràng với copy-paste curl command
- [ ] Rate limits documented (limit, window, headers, retry strategy)
- [ ] All examples use placeholder values (`<API_TOKEN>`, `example.com`) — KHÔNG hardcode real credentials

---

## 🚩 Red Flags — STOP nếu thấy

| Signal | Vấn đề | Hành động |
|--------|--------|-----------|
| Endpoint không có request example | Developer không biết gọi API thế nào | Thêm curl + code example |
| Response chỉ có description, không có JSON | Không biết data format | Thêm full JSON response |
| Thiếu error codes table | Không biết handle errors | Thêm bảng HTTP code + error code + resolution |
| Hardcoded API key / real URL | Security risk | Replace bằng `<API_TOKEN>`, `example.com` |
| Thiếu authentication section | Developer block ngay bước đầu | Thêm auth guide với examples |
| Không có pagination info | Responses bị truncated bất ngờ | Document page/limit params + meta object |

---

## Remember

1. **Examples-first:** Mỗi endpoint = 1 request example + 1 success response + 1 error response. Developer đọc examples trước, details sau.
2. **Copy-paste ready:** Mọi curl command phải chạy được ngay (chỉ cần thay `<API_TOKEN>`).
3. **Error handling explicit:** Không chỉ list HTTP codes — mỗi error cần resolution guide.
4. **Consistent format:** Tất cả endpoints dùng cùng 1 format: Method → Path → Params → Request → Response → Errors.
5. **Version awareness:** API version rõ ràng trong URL hoặc header. Document breaking changes.
6. **Security by default:** Dùng placeholder cho mọi credentials. Reference `docs/security-placeholders.md`.

---

## 🔗 Related Skills

| Skill | Khi nào dùng kèm |
|-------|-------------------|
| [project-doc-writer](project-doc-writer.md) | API design decisions (ADR), technical specs |
| [infra-security-doc](infra-security-doc.md) | API security policies, access control |
| [docs-engineer](docs-engineer.md) | MkDocs setup, API docs site structure |

---

## §1 Templates & Structure

### §1.1 REST API Reference (T13)

Dùng template `templates/api-reference.md`:

```text
# [API Name] — API Reference

Overview
Authentication
Endpoints (mỗi endpoint: Method + Path + Params + Request + Response)
Error Codes
Rate Limits
Changelog
```

**Required sections:** Overview, Endpoints, Error Codes
**Recommended:** Authentication, Rate Limits, Changelog
**Optional:** SDKs, Webhooks, Migration Guide

### §1.2 Endpoint Documentation Pattern

Mỗi endpoint PHẢI theo format:

```text
### `METHOD /path/:param`

[1-line description]

**Parameters:**
| Param | Type | Required | Default | Description |

**Request:**
```bash
curl example
```

**Response (200 OK):**
```json
{response}
```
```

### §1.3 GraphQL Schema Docs

```text
# [API Name] — GraphQL Reference

Schema Overview (types + queries + mutations)
Authentication
Queries (mỗi query: signature + variables + response)
Mutations (mỗi mutation: input + response + errors)
Subscriptions (nếu có)
Error Handling
```

### §1.4 Webhook Documentation

```text
# [Service] — Webhook Reference

Overview (event-driven, delivery guarantees)
Event Types (table: event + trigger + payload)
Payload Format (JSON example)
Verification (signature validation code example)
Retry Policy (schedule, backoff, failure handling)
```

---

## §2 Quality Checklist

Trước khi publish API docs, verify:

- [ ] **Completeness:** Mỗi endpoint có request + response + errors
- [ ] **Accuracy:** Examples match actual API behavior (test curl commands)
- [ ] **Security:** No real credentials, tokens, or internal URLs
- [ ] **Consistency:** All endpoints follow same format
- [ ] **Discoverability:** Clear navigation, grouped by resource
- [ ] **Versioning:** API version documented, breaking changes noted

---

## §3 Common API Doc Patterns

### Pagination

```json
{
  "data": [...],
  "meta": {
    "page": 1,
    "limit": 20,
    "total": 142,
    "has_more": true
  }
}
```

Document: `page`, `limit` params + `meta` object in response.

### Error Response

```json
{
  "error": {
    "code": "validation_error",
    "message": "Human-readable message",
    "details": [{"field": "name", "issue": "required"}]
  }
}
```

Document: error `code` enum + `details` structure for each error type.

### Versioning

| Strategy | URL | Header | Pros | Cons |
|----------|-----|--------|------|------|
| URL path | `/v1/resources` | — | Simple, visible | URL changes |
| Header | `/resources` | `API-Version: 2026-03-30` | Clean URLs | Hidden |
| Query param | `/resources?v=1` | — | Easy to test | Pollutes params |

Document which strategy the API uses + sunset policy for old versions.
