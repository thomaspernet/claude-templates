---
paths:
  - "**/notebooks/**"
  - "**/reports/**"
---

# Visualization Rules

## Every Chart MUST Have

- **Title** — descriptive, not just variable names
- **Axis labels** — with units (e.g., "Revenue (USD)", "Time (days)")
- **Source annotation** — where the data comes from
- **Legend** — if multiple series

## Style Conventions

- Default figure size: `figsize=(10, 6)`
- Use colorblind-safe palettes: `viridis`, `cividis`, or seaborn `colorblind`
- Font size: 12pt minimum for axis labels, 14pt for titles
- Grid lines: light gray, behind data
- Remove chart junk — no unnecessary borders, backgrounds, or decorations

## Tool Selection

| Use case | Tool |
|----------|------|
| Static plots for reports | matplotlib / seaborn |
| Interactive exploration | plotly |
| Quick EDA | pandas `.plot()` or seaborn |
| Publication quality | matplotlib with custom style |

## Saving

- Save all figures to `reports/figures/`
- Use descriptive filenames: `{analysis}_{chart_type}_{date}.png`
- Save as PNG (300 DPI) for reports, SVG for web
- Always `plt.tight_layout()` or `bbox_inches='tight'` before saving
