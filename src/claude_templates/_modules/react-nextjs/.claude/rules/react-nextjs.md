# React / Next.js Best Practices

## Component Patterns

### Server vs Client Components (Next.js App Router)

- **Server Components by default** — only add `"use client"` when you need interactivity
- Server Components: data fetching, DB queries, accessing backend resources
- Client Components: event handlers, useState, useEffect, browser APIs

### Component Structure

```tsx
interface UserCardProps {
  user: User;
  onSelect?: (id: string) => void;
}

export function UserCard({ user, onSelect }: UserCardProps) {
  // early return for edge cases
  if (!user) return null;

  return (
    <div onClick={() => onSelect?.(user.id)}>
      <h3>{user.name}</h3>
    </div>
  );
}
```

- Props interface named `{Component}Props`
- One component per file
- Prefer composition over prop drilling
- Early returns for edge cases

## App Router Conventions

- `page.tsx` — route component
- `layout.tsx` — shared wrapper (persists across navigation)
- `loading.tsx` — Suspense fallback
- `error.tsx` — error boundary (`"use client"` required)
- `not-found.tsx` — 404 page

## State Management

| Scope | Solution |
|-------|----------|
| Local component | `useState`, `useReducer` |
| Shared (small) | React Context |
| App-wide | Zustand, Jotai |
| Server state | React Query / SWR |

NEVER store server data in local state — use React Query or SWR.

## Data Fetching

- Server Components: `fetch()` or direct DB queries
- Client Components: React Query / SWR for caching and revalidation
- Server Actions for mutations (form submissions, updates)
- Always handle loading and error states

## Race Condition Prevention

- `useEffect` MUST return a cleanup function for async work
- Use `AbortController` for fetch requests in effects
- Use `useRef` for tracking mounted state
- Prefer React Query over raw useEffect + fetch

```tsx
useEffect(() => {
  const controller = new AbortController();
  fetch(url, { signal: controller.signal }).then(setData);
  return () => controller.abort();
}, [url]);
```

## Performance

- `React.memo()` for expensive renders with stable props
- `useMemo` / `useCallback` only when you measure a performance issue
- `React.lazy()` + `Suspense` for code splitting
- Use Next.js `<Image>` for automatic optimization
- Avoid re-renders: lift state up or use context selectively

## Anti-Patterns — NEVER Do

1. **`any` type annotations** — use proper TypeScript types
2. **useEffect without cleanup for async work** — causes race conditions
3. **Array index as React key** — use stable identifiers
4. **State updates after unmount** — memory leak
5. **Inline styles** — use Tailwind or CSS modules
6. **Fetching in useEffect without caching** — use React Query / SWR
7. **Prop drilling through 3+ levels** — use Context or composition
