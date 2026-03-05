## Design System: GLASSMORPHISM SIMPLE UI

### Pattern
- **Name:** Minimal Single Column
- **Conversion Focus:** Single CTA focus. Large typography. Lots of whitespace. No nav clutter. Mobile-first.
- **CTA Placement:** Center, large CTA button
- **Color Strategy:** Minimalist: Brand + white #FFFFFF + accent. Buttons: High contrast 7:1+. Text: Black/Dark grey
- **Sections:** 1. Hero headline, 2. Short description, 3. Benefit bullets (3 max), 4. CTA, 5. Footer

### Style
- **Name:** Exaggerated Minimalism
- **Keywords:** Bold minimalism, oversized typography, high contrast, negative space, loud minimal, statement design
- **Best For:** Fashion, architecture, portfolios, agency landing pages, luxury brands, editorial
- **Performance:** ÔÜí Excellent | **Accessibility:** Ô£ô WCAG AA

### Colors
| Role | Hex |
|------|-----|
| Primary | #2563EB |
| Secondary | #3B82F6 |
| CTA | #F97316 |
| Background | #F8FAFC |
| Text | #1E293B |

### Typography
- **Heading:** Inter
- **Body:** Inter
- **Mood:** spatial, legible, glass, system, clean, neutral
- **Best For:** Spatial computing, AR/VR, glassmorphism interfaces
- **Google Fonts:** https://fonts.google.com/share?selection.family=Inter:wght@300;400;500;600
- **CSS Import:**
```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');
```

### Key Effects
font-size: clamp(3rem 10vw 12rem), font-weight: 900, letter-spacing: -0.05em, massive whitespace

### Avoid (Anti-patterns)
- Complex signup
- No preview

### Pre-Delivery Checklist
- [ ] No emojis as icons (use SVG: Heroicons/Lucide)
- [ ] cursor-pointer on all clickable elements
- [ ] Hover states with smooth transitions (150-300ms)
- [ ] Light mode: text contrast 4.5:1 minimum
- [ ] Focus states visible for keyboard nav
- [ ] prefers-reduced-motion respected
- [ ] Responsive: 375px, 768px, 1024px, 1440px

