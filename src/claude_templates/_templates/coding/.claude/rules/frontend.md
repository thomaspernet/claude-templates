---
paths:
  - "**/frontend/**"
  - "**/app/**"
  - "**/components/**"
---

# Frontend Rules — TypeScript + React

## TypeScript

- Strict mode enabled — no `any` types
- Prefer `interface` over `type` for object shapes
- Export types alongside components
- Use discriminated unions for state variants

## React / Next.js

- **Server Components by default** — only add `"use client"` when you need interactivity
- **App Router** conventions: `page.tsx`, `layout.tsx`, `loading.tsx`, `error.tsx`
- Props interfaces named `{Component}Props`
- Prefer composition over prop drilling

## Race Condition Prevention

- `useEffect` MUST return a cleanup function when doing async work
- Use `AbortController` for fetch requests in effects
- Use `useRef` for tracking mounted state
- Prefer React Query / SWR for data fetching over raw useEffect + fetch

## State Management

- Local state: `useState` / `useReducer`
- Shared state: React Context for small scope, Zustand/Jotai for app-wide
- Server state: React Query / SWR — never store server data in local state

## Anti-patterns — NEVER Do

- `any` type annotations
- `useEffect` without cleanup for async operations
- Array index as React key
- Fetch calls without AbortController in effects
- State updates after unmount
- Inline styles (use Tailwind or CSS modules)
