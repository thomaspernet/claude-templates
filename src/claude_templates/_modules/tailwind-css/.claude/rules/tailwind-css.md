# Tailwind CSS Best Practices

## Utility Conventions

- Apply utilities directly on elements — this IS the intended pattern
- Order utilities consistently: layout > spacing > sizing > typography > colors > effects
- Use Tailwind's design tokens over arbitrary values:
  ```html
  <!-- Good: uses design system -->
  <div class="p-4 text-sm text-gray-700">

  <!-- Bad: arbitrary values break consistency -->
  <div class="p-[13px] text-[13.5px] text-[#4a4a4a]">
  ```

## Responsive Design

- Mobile-first: base styles for mobile, breakpoints for larger screens
- Breakpoint prefixes: `sm:`, `md:`, `lg:`, `xl:`, `2xl:`
- Common pattern:
  ```html
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
  ```

## Component Extraction

When utility strings get long, extract into components (not @apply):

```tsx
// Good: extract a component
function Button({ children, variant = "primary" }) {
  const styles = {
    primary: "bg-blue-600 text-white hover:bg-blue-700",
    secondary: "bg-gray-200 text-gray-800 hover:bg-gray-300",
  };
  return (
    <button className={`px-4 py-2 rounded font-medium ${styles[variant]}`}>
      {children}
    </button>
  );
}

// Bad: @apply defeats the purpose of utility-first
// .btn-primary { @apply bg-blue-600 text-white hover:bg-blue-700 px-4 py-2; }
```

## The cn() Utility

Use `clsx` + `tailwind-merge` for conditional classes:

```tsx
import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

// Usage
<div className={cn("p-4 text-sm", isActive && "bg-blue-100", className)} />
```

## Dark Mode

- Use the `dark:` prefix: `bg-white dark:bg-gray-900`
- Configure in `tailwind.config`: `darkMode: "class"` (toggle) or `"media"` (system)
- Design both modes intentionally — don't just invert colors

## Custom Theme

Extend the default theme in `tailwind.config.ts`:

```ts
theme: {
  extend: {
    colors: {
      brand: { 50: "#f0f9ff", 500: "#3b82f6", 900: "#1e3a5f" },
    },
    fontFamily: {
      sans: ["Inter", ...defaultTheme.fontFamily.sans],
    },
  },
}
```

- Extend, don't replace — preserves all default utilities
- Use semantic color names: `brand`, `accent`, `surface`

## Anti-Patterns — NEVER Do

1. **Excessive arbitrary values** `[13px]` — use the design system scale
2. **@apply everywhere** — defeats utility-first, harder to maintain
3. **Inline style attributes alongside Tailwind** — pick one approach
4. **Overriding Tailwind with custom CSS** — extend the config instead
5. **Not purging unused styles** — ensure `content` paths are correct in config
6. **Ignoring responsive design** — always test on mobile sizes
