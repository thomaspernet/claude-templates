# Pydantic Best Practices

## Model Patterns

### Base Models

```python
from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID

class User(BaseModel):
    uuid: UUID
    name: str = Field(min_length=1, max_length=100)
    email: str
    created_at: datetime

class UserCreate(BaseModel):
    """Fields required for creation (no id, no timestamps)."""
    name: str = Field(min_length=1, max_length=100)
    email: str

class UserUpdate(BaseModel):
    """Optional fields for partial update."""
    name: str | None = None
    email: str | None = None

class UserResponse(BaseModel):
    """What the API returns."""
    uuid: UUID
    name: str
    email: str
    created_at: datetime
```

### Naming Convention

- `Entity` — core domain model
- `EntityCreate` — creation input (no id, no timestamps)
- `EntityUpdate` — partial update (all fields optional)
- `EntityResponse` — API output

## Validators

### Field Validators

```python
from pydantic import field_validator

class User(BaseModel):
    email: str

    @field_validator("email")
    @classmethod
    def validate_email(cls, v: str) -> str:
        if "@" not in v:
            raise ValueError("Invalid email format")
        return v.lower().strip()
```

### Model Validators

```python
from pydantic import model_validator

class DateRange(BaseModel):
    start: datetime
    end: datetime

    @model_validator(mode="after")
    def validate_range(self) -> "DateRange":
        if self.end <= self.start:
            raise ValueError("end must be after start")
        return self
```

## Serialization

- Use `model_dump()` (not deprecated `.dict()`)
- Use `model_dump(exclude_unset=True)` for partial updates
- Use `model_dump(mode="json")` for JSON-serializable output
- Use `model_json_schema()` for generating JSON schemas

## Settings Management

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    api_key: str
    debug: bool = False

    model_config = {"env_prefix": "APP_", "env_file": ".env"}
```

- Use `BaseSettings` for env var configuration
- Set `env_prefix` to namespace your variables
- Provide sensible defaults for non-sensitive values
- NEVER set defaults for secrets

## Advanced Patterns

- **Discriminated unions**: Use `Literal` field + `Union` for polymorphic models
- **Computed fields**: `@computed_field` for derived values
- **Custom types**: `Annotated[str, Field(pattern=r"^[a-z]+$")]` for reusable constraints
- **Strict mode**: `model_config = {"strict": True}` to prevent type coercion

## Anti-Patterns — NEVER Do

1. **Using dicts instead of models** — lose validation, typing, and documentation
2. **No validation on inputs** — always validate at system boundaries
3. **Mutable default values** — use `Field(default_factory=list)` not `Field(default=[])`
4. **Exposing internal models** — create separate response models
5. **Using `.dict()` or `.json()`** — deprecated, use `model_dump()` and `model_dump_json()`
6. **Ignoring `exclude_unset`** — critical for PATCH/update operations
