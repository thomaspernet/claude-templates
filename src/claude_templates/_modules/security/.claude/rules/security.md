# Security Best Practices

## Input Validation

- Validate ALL user input at system boundaries (API endpoints, form handlers)
- Use allowlists over blocklists: define what IS valid, not what isn't
- Validate type, length, format, and range
- Use Pydantic models for automatic validation in Python
- Never trust client-side validation alone — always validate server-side

## Injection Prevention

### SQL Injection

```python
# Good: parameterized query
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))

# Bad: string concatenation
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
```

### XSS (Cross-Site Scripting)

- Escape all user-supplied content before rendering in HTML
- Use framework auto-escaping (React does this by default)
- Never use `dangerouslySetInnerHTML` or `v-html` with user data
- Set `Content-Security-Policy` headers

### Command Injection

- Never pass user input to `os.system()`, `subprocess.shell=True`
- Use `subprocess.run(["cmd", "arg"])` with list arguments
- Validate and sanitize file paths to prevent directory traversal

## Authentication

### JWT Tokens

- Short expiry (15-60 minutes for access tokens)
- Use refresh tokens for session extension
- Store in httpOnly cookies (not localStorage)
- Validate signature, expiry, and issuer on every request
- Rotate signing keys periodically

### Passwords

- Use bcrypt, scrypt, or argon2 for hashing — NEVER MD5 or SHA
- Enforce minimum length (12+ characters)
- Check against known breached passwords (HaveIBeenPwned API)
- Rate limit login attempts

## Authorization

- Check permissions on every request, not just UI visibility
- Use role-based (RBAC) or attribute-based (ABAC) access control
- Principle of least privilege — grant minimum necessary access
- Never rely on client-side permission checks alone

## Secrets Management

- NEVER hardcode secrets in source code
- Use environment variables or secret managers (Vault, AWS Secrets Manager)
- Rotate secrets on a schedule
- Use different secrets per environment (dev/staging/prod)
- Add secrets to `.gitignore` — `.env`, `credentials.json`, `*.key`
- Use `git-secrets` or pre-commit hooks to prevent accidental commits

## HTTP Security Headers

```
Content-Security-Policy: default-src 'self'
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-XSS-Protection: 0  (rely on CSP instead)
```

## CORS

- Never use `Access-Control-Allow-Origin: *` in production
- Specify exact allowed origins
- Limit allowed methods and headers
- Set appropriate `max-age` for preflight caching

## Dependency Security

- Run `npm audit` / `pip audit` / `safety check` regularly
- Enable Dependabot or Renovate for automated updates
- Pin dependency versions in production
- Review changelogs before upgrading major versions

## Anti-Patterns — NEVER Do

1. **Hardcoded secrets** — use env vars or secret managers
2. **String concatenation in queries** — parameterize everything
3. **MD5/SHA for passwords** — use bcrypt/argon2
4. **Wildcard CORS** — specify exact origins
5. **Storing tokens in localStorage** — use httpOnly cookies
6. **No rate limiting** — brute force attacks on auth endpoints
7. **Trusting client-side validation** — always validate server-side
8. **Logging secrets** — never log tokens, passwords, API keys
