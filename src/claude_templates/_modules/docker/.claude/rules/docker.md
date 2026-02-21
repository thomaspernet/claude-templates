# Docker Best Practices

## Dockerfile

### Multi-Stage Builds

Separate build and runtime stages to minimize image size:

```dockerfile
# Build stage
FROM python:3.12-slim AS builder
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN pip install uv && uv sync --frozen --no-dev

# Runtime stage
FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /app/.venv /app/.venv
COPY src/ ./src/
ENV PATH="/app/.venv/bin:$PATH"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Layer Caching

- Copy dependency files BEFORE copying source code
- Dependencies change rarely; source code changes often
- Order instructions from least to most frequently changed

### .dockerignore

Always include a `.dockerignore`:
```
.git
.venv
node_modules
__pycache__
*.pyc
.env
.pytest_cache
```

### Security

- NEVER run as root in production:
  ```dockerfile
  RUN adduser --disabled-password appuser
  USER appuser
  ```
- NEVER copy `.env` or secrets into the image
- Use `--no-cache-dir` for pip to reduce image size
- Pin base image versions: `python:3.12.3-slim`, not `python:latest`

### Image Size

- Use `-slim` or `-alpine` base images
- Combine RUN commands to reduce layers: `RUN apt-get update && apt-get install -y pkg && rm -rf /var/lib/apt/lists/*`
- Remove build dependencies in the same layer they're installed
- Use multi-stage builds to exclude build tools from final image

## Docker Compose

```yaml
services:
  app:
    build: .
    ports:
      - "8000:8000"
    env_file: .env
    depends_on:
      db:
        condition: service_healthy
    restart: unless-stopped

  db:
    image: postgres:16-alpine
    volumes:
      - pgdata:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: ${DB_NAME}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5

volumes:
  pgdata:
```

### Compose Patterns

- Use `depends_on` with `condition: service_healthy` — not just `depends_on`
- Use named volumes for persistent data
- Use `env_file` instead of inline environment variables
- Use `restart: unless-stopped` for production

## Health Checks

```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1
```

- Add health checks to every service
- Check actual functionality, not just port availability
- Keep health check endpoints lightweight

## Anti-Patterns — NEVER Do

1. **Running as root** — always create and switch to a non-root user
2. **Copying secrets into the image** — use env vars or Docker secrets
3. **Using `latest` tag** — pin specific versions
4. **No .dockerignore** — bloats context and potentially leaks secrets
5. **One RUN per command** — combine to reduce layers
6. **No health checks** — services restart blindly on failure
