---
name: ad-creative
description: "Render ad concepts as HTML with 5 template styles (cookie-cutter, ugly, meme, branded, native), optionally screenshot via Playwright MCP."
compatibility: "Optional: Playwright MCP for screenshot capture. Degrades to HTML-only without it."
metadata:
  author: superamped
  version: "1.0"
  website: "https://superamped.com"
---

# Ad Creative

## Usage

Use when producing ad images from brainstormed concepts, creating multiple ad variations for A/B testing, or iterating on ad designs (new headline, different screenshot, color change).

## Process

### Step 1: Gather Inputs

Ask the user for:
1. **Headline text** — the main text on the ad image
2. **Brand colors** (optional) — primary color, background color, text color (hex values). If not provided, defaults: background `#0f172a`, text `#ffffff`, accent `#3b82f6`
3. **Font** (optional) — font family (default: system sans-serif stack)
4. **Logo URL** (optional) — if brand guidelines require it
5. **Product image** (optional, required for product-image and branded styles) — path to a screenshot, UI image, or visual asset
6. **Style** — cookie-cutter / ugly / meme / branded / native (default: cookie-cutter)
7. **Dimensions** — width x height in pixels. Common presets:
   - `square`: 1200x1200px (social feeds)
   - `landscape`: 1440x1000px (Reddit/display)
   - Or custom dimensions
8. **Platform** — which platform the ad is for (affects dimension defaults and template tweaks)
9. **Ad concept from ad-angles** (optional) — full concept block with headline, style, and image suggestion

### Step 1b: Select or Refine the Headline

If no headline is provided, or the headline needs strengthening, use the Hook Formula Bank:

**5 Qualities of an Irresistible Headline:**
1. **Clear, not clever** — Reader immediately knows what it's about
2. **Makes a PROMISE** — Not just "about X" but "here's what changes"
3. **Specific** — Concrete numbers, outcomes, audiences
4. **Takes a stance** — Polarizing headlines make the right reader say "that's me"
5. **Teases without revealing** — The Curiosity Gap

**Quick Headline Formulas:**
- `[Number] [Things] [Audience] should [know/avoid/use]`
- `How to [Outcome] without [Pain Point]`
- `Still [Painful Activity]? There's a better way.`
- `[Competitor], but [Differentiator]`
- `The [Number]-step [System] for [Outcome]`

**Headline Length Rules (for ad images):**
- Short headlines (< 40 chars) have the highest impact. Aim here.
- If the headline needs explanation, it's too complex for an ad image.

### Step 1c: Direct Response Checklist

Before building the HTML, verify the concept passes:
- [ ] **Single message** — The ad communicates ONE idea
- [ ] **Headline is benefit-oriented** — States what the prospect gets
- [ ] **Visual matches the headline** — Product screenshot reinforces the claim
- [ ] **CTA is clear** — Viewer knows what action to take
- [ ] **No competing elements** — No decorative graphics fighting for attention
- [ ] **Mobile-readable** — Headline text is legible at 50% zoom
- [ ] **Emotional resonance** — Activates at least one emotional trigger

### Step 2: Build the HTML

Create a self-contained HTML file using the selected template.

---

**Cookie-Cutter Template** — headline + product image + clean background:

```
┌─────────────────────────────┐
│                             │
│     HEADLINE TEXT            │
│     (large, bold)           │
│                             │
│   ┌─────────────────────┐   │
│   │   Product Image     │   │
│   │   (with shadow)     │   │
│   └─────────────────────┘   │
│                             │
└─────────────────────────────┘
```

Design rules:
- Headline: Large, bold, high contrast. Max 2 lines.
- Product image: Centered, subtle drop shadow, ~60% canvas width.
- Background: Solid color or subtle gradient using brand colors.
- No logos, decorative elements, or extra text. Minimal by design.

Headline font size: < 40 chars → 64px, 40-70 chars → 52px, > 70 chars → 42px.

---

**Ugly Ads Template** — text-heavy, high-contrast, deliberately unpolished:

```
┌─────────────────────────────┐
│   HEADLINE TEXT             │
│   (very large, bold,        │
│    fills top 60%)           │
│                             │
│   Optional: $PRICE          │
│   Optional: subtext/CTA     │
└─────────────────────────────┘
```

Design rules:
- Square format (1200x1200px) default
- Text fills the top 60% of the canvas
- No product images — text IS the creative
- Bold, heavy font weights (700-900)
- Deliberately unpolished: no gradients, shadows, rounded corners

**High-contrast color combos:**

| Combo | Background | Text | Accent |
|-------|-----------|------|--------|
| Black/Yellow | `#000000` | `#FFD700` | `#FFFFFF` |
| Red/White | `#CC0000` | `#FFFFFF` | `#FFD700` |
| Blue/White | `#003366` | `#FFFFFF` | `#FFD700` |
| White/Black | `#FFFFFF` | `#000000` | `#CC0000` |
| Yellow/Black | `#FFD700` | `#000000` | `#CC0000` |

Headline font size: < 30 chars → 96px, 30-60 chars → 72px, > 60 chars → 56px.

---

**Meme Template** — meme format for attention + benefit:

```
┌─────────────────────────────┐
│   TOP TEXT (setup)          │
│   ┌─────────────────────┐   │
│   │   Meme Image        │   │
│   └─────────────────────┘   │
│   BOTTOM TEXT (punchline)   │
└─────────────────────────────┘
```

Design rules:
- Use recognizable meme templates (Drake, Expanding Brain, etc.)
- Top text = setup (problem or old way), Bottom text = punchline (product or new way)
- Keep text short — memes with walls of text lose the format's power
- Square format (1200x1200) works best

---

**Branded Template** — professional with stats, product image, social proof:

```
┌─────────────────────────────┐
│     HEADLINE TEXT            │
│   STAT  |  STAT  |  STAT    │
│   ┌─────────────────────┐   │
│   │   Product Image     │   │
│   └─────────────────────┘   │
│   Social proof line          │
└─────────────────────────────┘
```

Design rules:
- Use the brand's actual colors
- Stats in accent color with muted labels
- Product image with shadow, centered
- Social proof line at the bottom (client names, G2 rating, etc.)

---

**Native Template** — looks like an organic social post:

```
┌─────────────────────────────┐
│  Platform · Promoted         │
│  HEADLINE TEXT               │
│  Body text (reads like       │
│   a real post)              │
│  ┌─────────────────────┐    │
│  │  Product Image       │    │
│  └─────────────────────┘    │
│  142 upvotes · 38 comments   │
└─────────────────────────────┘
```

Design rules:
- Light background (`#f8fafc` or white)
- System font stack, normal weights
- Body text reads like a genuine post, not a marketing headline
- Fake engagement metrics at bottom

---

### Step 3: Save the HTML File

Write the HTML file. Name it descriptively: `ad-{slug}.html` where `{slug}` is a kebab-cased version of the headline (truncated to 40 chars).

### Step 4: Screenshot with Playwright MCP (if available)

If Playwright MCP is configured:
1. Set viewport to the exact dimensions using `browser_resize`
2. Navigate to the HTML file using a `file://` URL
3. Screenshot the viewport
4. Save the screenshot as PNG

Playwright MCP must be configured with `--allow-unrestricted-file-access` and `--browser chromium` flags.

**If Playwright MCP is not available**, present the HTML file and tell the user they can open it in a browser and screenshot manually, or configure Playwright MCP for automated capture.

### Step 5: Verify, Present, and Iterate

Present results to the user with:
- The image preview for each ad (if screenshots were captured)
- A summary table showing all rendered ads
- File paths to both the PNG and HTML files

Ask the user if they want to iterate:
- Change a headline → update the HTML and re-screenshot
- Change colors or style → rebuild from a different template
- Change the product image → capture a new screenshot and rebuild
- Change dimensions → re-screenshot at new viewport size

**Do not consider the batch complete until the user confirms they're happy.**

## Output Format

```
# Ad Creative Output

**Date:** [current date]
**Ads Produced:** [count]
**Dimensions:** [width]x[height]px

---

## Ad 1: [Concept name]

**Headline:** [headline text]
**Style:** [branded/product/meme/ugly/native]
**Files:**
- HTML: [path]
- PNG: [path] (if Playwright available)

[Image preview if available]

---

## Upload Checklist

- [ ] Images are correct dimensions
- [ ] File size under 3MB per image
- [ ] Format is PNG or JPG
- [ ] Headlines are readable on mobile (test at 50% zoom)
- [ ] Brand colors match landing page
```

## Rules

- The cookie-cutter template is intentionally minimal. Resist the urge to add decorative elements. Simplicity converts.
- Product images should be real screenshots, not mockups or stock photos.
- If the product image has a white background, use a dark ad background (and vice versa) for contrast.
- PNG is preferred for sharp text and UI screenshots.
- The HTML file is kept so the user can tweak copy, colors, or images manually and re-screenshot.
- Visual consistency between ad and landing page reduces drop-off. Use the same colors, fonts, and design system.
