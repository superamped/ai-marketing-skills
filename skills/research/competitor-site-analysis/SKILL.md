---
name: competitor-site-analysis
description: "Visit a competitor's website and extract structured data across 5 dimensions: overview, positioning, pricing, social proof, and hiring signals."
compatibility: "Requires internet access. Optional: Playwright MCP for JS-rendered pages."
metadata:
  author: superamped
  version: "1.0"
  website: "https://superamped.com"
---

# Competitor Site Analysis

## Usage

Use for a quick website data pull on a competitor, or as a first step before deeper analysis. Produces a structured 5-section profile from publicly available website information.

## Process

### Step 1: Gather Inputs

Ask the user for:
1. **Competitor name** — the company to analyze
2. **Competitor URL** — their homepage URL
3. **Specific sections to focus on** (optional) — default: all 5

### Step 2: Validate & Fetch

Confirm you have competitor name and URL. Fetch the homepage to verify it's reachable.

**If the site is unreachable**, behind a login wall, or returns errors — tell the user and stop.

### Step 3: Fetch Website Pages

Fetch up to 6 pages. Adapt URLs based on what the site actually has — not every site uses the same paths.

| Page | Typical URLs to Try | What to Extract |
|------|---------------------|-----------------|
| Homepage | `/` | Tagline, headline, value prop, target audience signals, trust badges, social proof |
| Pricing | `/pricing`, `/plans` | Model, tiers, price points, value metric, free tier, annual discount, trial, feature-by-tier gating |
| Features | `/features`, `/product` | Key features, integrations, platform capabilities |
| About | `/about`, `/about-us`, `/company` | Founded, team size signals, stage/funding signals, mission |
| Customers | `/customers`, `/case-studies` | Customer logos, testimonials, case study count, industries served |
| Careers | `/careers`, `/jobs`, `/about/careers` | Open roles by department, total headcount signals, strategic hiring patterns |

**If a page doesn't exist** (404, redirect to homepage), skip it and note "not found" for that section. Don't guess.

### Step 4: Structure Findings

Organize extracted data into 5 sections:

#### Section 1: Company Overview
- Tagline (their words, not yours)
- Founded / age signals
- Stage / funding signals (bootstrapped, seed, Series X — based on about page, team size, office count)
- Team size signals (exact if stated, otherwise estimate from about page)
- Headquarters / markets
- Primary GTM motion: PLG / sales-led / content-led / community-led (based on homepage CTA — "Start free" vs. "Book a demo" vs. both)
- Partnerships / integrations as distribution (from features page or homepage)

#### Section 2: Product & Positioning
- Homepage headline (exact quote)
- Value proposition (what they promise in 1-2 sentences)
- Target audience (who the site speaks to)
- Key features (top 5-8 from features page)
- Integrations (notable ones)
- Product-led vs. sales-led signals (self-serve signup? demo request? both?)
- Free trial / freemium availability

#### Section 3: Pricing & Feature Monetization
- Pricing model (per-seat, usage-based, flat, freemium, custom)
- Tier breakdown with price points
- Value metric (what they charge per unit of)
- Annual discount percentage
- Free tier — what's included, what's limited
- Enterprise tier — custom pricing or listed?

**Feature monetization** — if the pricing page shows feature-by-tier breakdowns:
- Which features are free vs. gated?
- What's the key unlock at each paid tier? (the feature that justifies the upgrade)
- What do they gate behind enterprise? (reveals what they consider highest-value)
- Any usage limits that force upgrades? (seats, API calls, storage, etc.)

**If pricing is not public**, note "not public — sales-led motion" and any signals about pricing level.

#### Section 4: Social Proof & Trust
- Customer logos (notable names)
- Testimonial highlights (1-2 strongest quotes)
- Case study count and themes
- Trust signals (G2 badges, security certs, compliance badges)
- Community size (if visible — Slack, Discord, forum)
- Social media follower counts (if visible on site)

#### Section 5: Hiring Signals
- Total open roles (if listed)
- Roles by department — engineering, sales, marketing, product, customer success, etc.
- Notable hires or role types that signal strategic direction (e.g., "ML Engineer" = investing in AI, "Enterprise AE" = moving upmarket, "Developer Advocate" = building community)
- Hiring velocity signals — "urgently hiring", multiple roles in one department

**If no careers page exists**, note "no public careers page" and move on.

## Output Format

Present the 5-section structured website profile:

```
# Competitor Site Analysis: [Name]

**URL:** [url]
**Date:** [current date]

## 1. Company Overview
[structured findings]

## 2. Product & Positioning
[structured findings]

## 3. Pricing & Feature Monetization
[structured findings]

## 4. Social Proof & Trust
[structured findings]

## 5. Hiring Signals
[structured findings]
```

## Rules

- Never invent data — if a page is inaccessible or info isn't visible, mark "not found."
- Never fetch more than 6 pages per competitor.
- Never guess at pricing — if it's not public, say so.
- Don't add strategic interpretation — this skill extracts, it doesn't analyze. Save strategic assessment for competitor-landscape.
- Keep extraction factual. Quote headlines, list features, note prices. Don't editorialize.
- If key pages (pricing, features) are missing or inaccessible, flag that the profile will have gaps.
- If the site is heavily JS-rendered and content is sparse, suggest using Playwright MCP if available.
