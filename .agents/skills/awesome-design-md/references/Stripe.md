# Stripe Design Specification

A design specification reverse-engineered from Stripe's web presence. Optimized for high-credibility SaaS products, landing pages, developers tools, and payment dashboards.

## 1. Visual Vibe & Philosophy
- **Core Tone:** Trustworthy, precise, fluid, and premium.
- **Key Characteristics:** 
  - Generous negative space that feels breathable but structured.
  - Subtle, complex gradients (often multi-layered or angled).
  - Blurred colorful light leaks/glowing orbs behind key text and hero units.
  - Exceptionally clean typography with open letter-spacing.

## 2. Design Tokens

### Colors
- **Primary Indigo:** `hsl(244, 100%, 68%)` / `#635bff`
- **Secondary Slate:** `hsl(211, 73%, 15%)` / `#0a2540` (Used for headers and primary text)
- **Neutral Grey (Text):** `hsl(210, 16%, 38%)` / `#4f5b66`
- **Background Main:** `hsl(210, 40%, 98%)` / `#f8f9fa` or pure white `#ffffff`
- **Border / Divider:** `hsl(210, 20%, 93%)` / `#e3e8ee`
- **Glow Accents:**
  - Teal: `#00d4ff`
  - Pink/Purple: `#e259e9`
  - Orange: `#ff9900`

### Typography
- **Display Font:** Söhne, or fallback to system sans-serif (`-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`) with `-0.02em` letter-spacing for headers.
- **Body Font:** System sans-serif with normal or `0.01em` letter-spacing.
- **Weights:**
  - Light (Headers): `300`
  - Regular (Body): `400`
  - Medium (Navigation/UI labels): `500`
  - Semi-Bold (Subheadings): `600`
- **Line Heights:** Display: `1.15`, Body: `1.6`, UI Labels: `1.2`.

### Spacing (8px Grid)
- `space-1`: `4px`
- `space-2`: `8px`
- `space-3`: `12px`
- `space-4`: `16px`
- `space-6`: `24px`
- `space-8`: `32px`
- `space-12`: `48px`
- `space-16`: `64px`

### Radii & Borders
- **Border Radius:**
  - Standard Cards: `8px`
  - Buttons / Inputs: `4px`
  - Large Heros: `16px`
- **Borders:** `1px solid var(--border)`

### Shadows & Elevation
- **Soft Border Shadow (Card):** `0 4px 6px -1px rgba(50, 50, 93, 0.11), 0 1px 3px -1px rgba(0, 0, 0, 0.08)`
- **Hover Card Shadow:** `0 13px 27px -5px rgba(50, 50, 93, 0.25), 0 8px 16px -8px rgba(0, 0, 0, 0.3)`
- **Button Shadow:** `0 2px 5px -1px rgba(50, 50, 93, 0.1), 0 1px 1.5px -0.5px rgba(0, 0, 0, 0.07)`

---

## 3. Component Specifications

### Buttons
- **Primary:** Background `#635bff`, text white, border-radius `4px`, padding `6px 12px` or `8px 16px`. Active/Hover state: background shifts slightly darker (`#4b42db`), with a subtle upward movement (`translateY(-1px)`) and slightly stronger shadow.
- **Secondary (Link style):** Text `#635bff`, weight `600`, with a small right arrow (`→` or `chevron`) that shifts right on hover (`transform: translateX(3px)`) with a transition duration of `150ms`.

### Cards
- **Structure:** White background, `8px` border radius, soft border shadow.
- **Hover Effect:** Shifts up `2px` using `translateY(-2px)`, shadow increases to hover shadow, background transition `cubic-bezier(0.25, 0.46, 0.45, 0.94)`.

### Inputs
- **Base:** White background, border `1px solid #e3e8ee`, border-radius `4px`, padding `8px 12px`, text `#0a2540`.
- **Focus State:** Border color `#635bff` or HSL Indigo, outline none, shadow ring: `box-shadow: 0 0 0 1px rgba(99, 91, 255, 0.4), 0 1px 3px 0 rgba(0, 0, 0, 0.08)`.
