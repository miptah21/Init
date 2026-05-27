# Vercel Design Specification

A design specification reverse-engineered from Vercel's branding and interface design. Optimized for clean deployment portals, hosting dashboards, developer platform dashboards, and modern minimalistic portfolios.

## 1. Visual Vibe & Philosophy
- **Core Tone:** Stark, geometric, monochrome, and high-contrast minimal.
- **Key Characteristics:**
  - Absolute black and white styling, using greys sparingly for structure.
  - Razor-sharp corners with small, consistent border-radius.
  - Relying on typography hierarchy and layout structure rather than shadows/gradients.
  - Clean layout lines resembling grids or terminal interfaces.

## 2. Design Tokens

### Colors (Dual Mode - Light & Dark)
#### Light Mode
- **Background Main:** `#ffffff`
- **Surface Main (Cards):** `#ffffff`
- **Border Default:** `#eaeaea`
- **Text Primary:** `#000000`
- **Text Secondary:** `#666666`
- **Accent Blue:** `#0070f3`

#### Dark Mode
- **Background Main:** `#000000`
- **Surface Main (Cards):** `#111111` or `#000000`
- **Border Default:** `#333333`
- **Text Primary:** `#ffffff`
- **Text Secondary:** `#888888`
- **Accent Blue:** `#0070f3`

### Typography
- **UI & Display Font:** Geist Sans (fallback system-ui `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`).
- **Monospace:** Geist Mono (fallback `SFMono-Regular, Consolas, Menlo, monospace`).
- **Weights:**
  - Regular: `400`
  - Medium (Interactive/UI labels): `500`
  - Semi-Bold (Titles): `600`
  - Bold: `700`
- **Line Heights:** Headings: `1.25`, Body: `1.6`.

### Spacing (8px Grid)
- `space-1`: `4px`
- `space-2`: `8px`
- `space-3`: `12px`
- `space-4`: `16px`
- `space-6`: `24px`
- `space-8`: `32px`
- `space-10`: `40px`

### Radii & Borders
- **Border Radius:**
  - Standard Cards / Buttons / Inputs: `5px` or `6px`
  - Tabs / Inline UI: `4px`
- **Borders:** `1px solid var(--border)`

### Shadows & Elevation
- Vercel aesthetics generally **avoid** heavy shadows. Elevation is marked by border boundaries:
  - Base shadow (if used at all for dropdowns/popovers): `0 4px 4px rgba(0, 0, 0, 0.05)` or `0 0 0 1px var(--border)`

---

## 3. Component Specifications

### Buttons
- **Primary (Filled):**
  - Light mode: Background `#000000`, text `#ffffff`, border-radius `5px`, border `1px solid #000000`, padding `8px 14px`, transition `all 0.15s ease`. Hover: Background `#ffffff`, text `#000000`.
  - Dark mode: Background `#ffffff`, text `#000000`, border-radius `5px`, border `1px solid #ffffff`, padding `8px 14px`. Hover: Background `#000000`, text `#ffffff`.
- **Secondary (Outlined):**
  - Border `1px solid var(--border)`, background `transparent`, text `var(--text-secondary)`, padding `8px 14px`. Hover: border `1px solid var(--text-primary)`, text `var(--text-primary)`.

### Tab Navigation
- Horizontal layout with no surrounding border. Tabs are separated by spacing.
- Active tab has a solid black (light mode) or solid white (dark mode) bottom border of `2px` or a clean highlight slider background, and text color shifts to `var(--text-primary)`.

### Code Blocks / Command Snippets
- Background `#fafafa` (light mode) or `#111111` (dark mode), border `1px solid var(--border)`, padding `12px 16px`, font-family `monospace`, text alignment left, copy button appears on hover.
