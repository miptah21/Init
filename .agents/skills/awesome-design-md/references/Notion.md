# Notion Design Specification

A design specification reverse-engineered from Notion's user interface. Optimized for rich-text editors, documentation databases, clean knowledge bases, and wiki-like product documentation.

## 1. Visual Vibe & Philosophy
- **Core Tone:** Warm, documentation-focused, cozy, and organic/analog.
- **Key Characteristics:**
  - Soft neutral whites and off-white/beige backgrounds that feel like paper.
  - Distinctive use of serif fonts for headings to give an editorial, structured feeling.
  - Emoji icons serving as standard page/component headers.
  - Clean separators and subtle callout boxes.
  - Simple, rounded, border-less buttons or soft card layouts.

## 2. Design Tokens

### Colors (Warm Theme Focus)
- **Background App:** `#fbfbfa` or `#ffffff`
- **Surface Hover:** `rgba(55, 53, 47, 0.08)` (Default menu/sidebar hover highlight)
- **Text Primary (Off-black):** `#37352f` (Less harsh than pure black)
- **Text Secondary (Muted):** `#787774`
- **Border Default:** `rgba(55, 53, 47, 0.16)` / `#e9e9e6`
- **Accent Highlight:**
  - Yellow: `#fbe5c5` (Highlight background)
  - Grey Callout Background: `#f1f1ef`
  - Red Text: `#eb5757`

### Typography
- **Header/Display Font:** Georgia, Lyon-New, or fallback Serif (`"Lyon-Text", Georgia, YuMincho, "BIZ UDPMincho", serif`).
- **Body Font:** System sans-serif stack (`ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif`).
- **Weights:**
  - Regular: `400`
  - Medium (Interactive/Subheadings): `500`
  - Semi-Bold (Section headers): `600`
  - Bold: `700`
- **Line Heights:** Headings: `1.3`, Body: `1.5`.

### Spacing
- `space-1`: `4px`
- `space-2`: `8px`
- `space-3`: `12px`
- `space-4`: `16px`
- `space-6`: `24px`
- `space-8`: `32px`
- `space-12`: `48px`

### Radii & Borders
- **Border Radius:**
  - Standard Cards / Callouts / Menus: `3px` or `4px` (Very small, cozy radius)
  - Large Elements: `8px`
- **Borders:** `1px solid var(--border)`

### Shadows & Elevation
- **Floating Menu Shadow:** `0px 2px 4px rgba(15, 15, 15, 0.05), 0px 8px 16px rgba(15, 15, 15, 0.1)`
- **Card Separator:** Bottom border instead of box shadow.

---

## 3. Component Specifications

### Buttons
- **Inline Hover Button:** Background `transparent`, text `var(--text-primary)`, padding `4px 8px`, border-radius `3px`, transition `background 100ms ease-in`. Hover: Background `var(--surface-hover)`.

### Callout Box
- **Base Style:** Background `#f1f1ef`, border-radius `3px`, padding `16px 16px 16px 12px`, display `flex`, gap `12px`, text `var(--text-primary)`.
- **Icon:** Features an emoji or custom icon on the left side of the content.

### Breadcrumb Navigation
- Small text, grey color (`#787774`), typography system sans-serif `14px`, items separated by a grey slash (`/`), hover state shifts text color to `#37352f` with a subtle background highlight.
