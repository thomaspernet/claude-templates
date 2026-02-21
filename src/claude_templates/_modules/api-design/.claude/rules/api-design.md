# API Design Best Practices (REST)

## Resource Naming

- Use nouns, not verbs: `/users`, not `/getUsers`
- Plural for collections: `/users`, `/orders`
- Nested for relationships: `/users/{id}/orders`
- Consistent casing: kebab-case for URLs, snake_case for JSON fields

## HTTP Methods

| Method | Purpose | Idempotent | Response |
|--------|---------|-----------|----------|
| GET | Read resource(s) | Yes | 200 + body |
| POST | Create resource | No | 201 + body + Location header |
| PUT | Full update | Yes | 200 + body |
| PATCH | Partial update | Yes | 200 + body |
| DELETE | Remove resource | Yes | 204 no body |

## Status Codes

| Code | When |
|------|------|
| 200 | Success (GET, PUT, PATCH) |
| 201 | Created (POST) |
| 204 | No content (DELETE) |
| 400 | Bad request (validation error) |
| 401 | Unauthorized (no/invalid credentials) |
| 403 | Forbidden (valid credentials, no permission) |
| 404 | Not found |
| 409 | Conflict (duplicate, version mismatch) |
| 422 | Unprocessable entity (semantic validation) |
| 500 | Internal server error |

## Error Response Format

Consistent structure for all errors:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Email is required",
    "details": [
      {"field": "email", "message": "This field is required"}
    ]
  }
}
```

- Always include a machine-readable `code`
- Always include a human-readable `message`
- Never expose stack traces or internal details

## Pagination

### Cursor-based (Recommended)

```
GET /users?cursor=abc123&limit=20
Response: { "data": [...], "next_cursor": "def456", "has_more": true }
```

- Stable with concurrent inserts/deletes
- Use for real-time feeds, large datasets

### Offset-based

```
GET /users?offset=40&limit=20
Response: { "data": [...], "total": 150 }
```

- Simple but drifts with concurrent changes
- Use for admin dashboards, small datasets

## Versioning

- URL prefix: `/v1/users` (simple, explicit)
- Start with v1 from day one
- Never break existing versions — add new fields, never remove

## Authentication

- JWT for stateless APIs (include in `Authorization: Bearer <token>`)
- Session cookies for browser-based apps
- API keys for service-to-service (`X-API-Key` header)
- Always use HTTPS

## Rate Limiting

- Return `429 Too Many Requests` when exceeded
- Include headers: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`
- Different limits per endpoint (read vs write)

## Anti-Patterns — NEVER Do

1. **Verbs in URLs** — `/getUser/123` should be `GET /users/123`
2. **Inconsistent response format** — always same structure
3. **200 for errors** — use appropriate status codes
4. **Exposing internal IDs** — use UUIDs, not auto-increment IDs
5. **No pagination on list endpoints** — always paginate collections
6. **Breaking changes without versioning** — never remove fields from existing versions
