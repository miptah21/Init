# Linear Design Specification

A design specification reverse-engineered from Linear's web and desktop application interface. Optimized for high-density developer tools, task tracking dashboards, issue managers, and dark-themed productivity apps.

## 1. Visual Vibe & Philosophy
- **Core Tone:** Technical, focused, high-density, and premium dark mode.
- **Key Characteristics:**
  - Strict dark mode hierarchy (near-black background with dark grey cards).
  - High-contrast, razor-thin borders to separate UI sections.
  - Micro-glows and gradient borders for active states or notifications.
  - Inline keyboard shortcuts visual cues (`Kbd` tags) present across UI.
  - Compact padding and layout density designed for efficiency.

## 2. Design Tokens

### Colors (Dark Mode Focus)
- **Background App:** `hsl(240, 20%, 3%)` / `#08070a`
- **Surface Main (Cards/Sidebar):** `hsl(240, 10%, 6%)` / `#0f0f11`
- **Surface Hover:** `hsl(240, 10%, 10%)` / `#18181b`
- **Border Default:** `hsl(240, 6%, 15%)` / `#232326`
- **Border Focused:** `hsl(240, 5%, 26%)` / `#3f3f46`
- **Text Primary:** `hsl(0, 0%, 93%)` / `#eeeeee`
- **Text Secondary:** `hsl(240, 5%, 65%)` / `#a1a1aa`
- **Accent Purple:** `hsl(236, 57%, 59%)` / `#5e6ad2`
- **Accent Orange:** `hsl(25, 95%, 50%)` / `#f06414` (Alerts/Active tasks)

### Typography
- **UI & Body Font:** Inter, or system sans-serif stack (`-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`).
- **Monospace (Shortcuts/Metadata):** JetBrains Mono, or system monospace stack (`SFMono-Regular, Consolas, "Liberation Mono", Menlo, Courier, monospace`).
- **Weights:**
  - Regular: `400`
  - Medium (Labels/Menus): `500`
  - Semi-Bold (Header/Bold Text): `600`
- **Line Heights:** UI: `1.25`, Body: `1.5`.

### Spacing (Dense 4px Base)
- `space-1`: `4px`
- `space-2`: `8px`
- `space-3`: `12px`
- `space-4`: `16px`
- `space-5`: `20px`
- `space-6`: `24px`
- `space-8`: `32px`

### Radii & Borders
- **Border Radius:**
  - Card/Dialog: `6px`
  - Inputs / Buttons: `4px`
  - Keyboard Shortcut Badge: `3px`
- **Borders:** `1px solid var(--border-default)`

### Elevation & Inner Highlights
- **Inner Top Highlight (Button/Card):** `box-shadow: inset 0 1px 0 0 rgba(255, 255, 255, 0.05)`
- **Dropdown Menu Shadow:** `0 10px 30px -10px rgba(0, 0, 0, 0.5), 0 0 0 1px var(--border-default)`
- **Accent Glow (Focus):** `box-shadow: 0 0 0 1px var(--accent-purple), 0 0 8px rgba(94, 106, 210, 0.25)`

---

## 3. Component Specifications

### Buttons
- **Base Style:** Border `1px solid var(--border-default)`, background `#161618`, text `#eeeeee`, border-radius `4px`, padding `6px 10px`, typography medium `12px`, inner top highlight `box-shadow: inset 0 1px 0 rgba(255,255,255,0.05)`.
- **Hover:** Background `#1f1f23`, border-color `var(--border-focused)`.
- **Keyboard indicator:** Buttons often feature a tiny grey key label on the right side.

### Keyboard Shortcut Badge (KBD)
- **Base Style:** Background `#18181b`, border `1px solid #232326`, border-radius `3px`, padding `1px 4px`, font-family `monospace`, font-size `10px`, text `#a1a1aa`, shadow `box-shadow: 0 1px 0 rgba(0,0,0,0.2)`.

### Issue/Task Cards
- **Base Style:** Background `#0f0f11`, border `1px solid var(--border-default)`, padding `12px`, border-radius `6px`.
- **Hover:** Border-color `var(--border-focused)`, background `#141416`, cursor pointer.
- **Header:** Small project color-dot (e.g. green/purple/orange) next to ID (e.g. `LIN-102`).
