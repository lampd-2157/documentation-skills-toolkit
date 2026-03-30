# Test Cases: api-doc-writer

## TC-API-01: REST API Reference

**Prompt:** "Tạo API reference cho User Management API — CRUD endpoints, Bearer auth, JSON format"

**Expected trigger:** `api-doc-writer`
**Expected output:**
- [ ] Has `### GET /users` style endpoint headers
- [ ] Each endpoint has curl request example
- [ ] Each endpoint has JSON response example
- [ ] Error codes table with >= 5 HTTP status codes
- [ ] Authentication section with Bearer token example
- [ ] Uses `<API_TOKEN>` placeholder (no real tokens)

## TC-API-02: GraphQL Schema Documentation

**Prompt:** "Document GraphQL API cho e-commerce: queries, mutations, subscriptions"

**Expected trigger:** `api-doc-writer`
**Expected output:**
- [ ] Schema overview with types
- [ ] Query examples with variables
- [ ] Mutation examples with input + response
- [ ] Error handling section
- [ ] Authentication method documented

## TC-API-03: Webhook Documentation

**Prompt:** "Viết webhook docs cho payment system — event types, payload format, retry policy"

**Expected trigger:** `api-doc-writer`
**Expected output:**
- [ ] Event types table (event + trigger + payload)
- [ ] Payload JSON example
- [ ] Signature verification code example
- [ ] Retry policy documented
- [ ] Security section (HMAC validation)

## TC-API-04: API with Security (Composition)

**Prompt:** "API reference cho internal microservice có OAuth2 + RBAC permissions"

**Expected trigger:** `api-doc-writer` + `infra-security-doc` (composition rule)
**Expected output:**
- [ ] Standard API reference structure (T13)
- [ ] Detailed auth section (OAuth2 flow)
- [ ] RBAC permissions per endpoint
- [ ] Security boundaries documented
