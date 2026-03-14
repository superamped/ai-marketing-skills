---
name: competitor-discovery
description: "Search the web for competitors based on product category, produce a ranked list of direct, adjacent, and tangential competitors."
compatibility: "Requires internet access for web search and competitor website fetching."
metadata:
  author: superamped
  version: "1.0"
  website: "https://superamped.com"
---

# Competitor Discovery

## Usage

Use when you don't know who your competitors are, when entering a new market, or when refreshing the competitor list after a pivot or market shift.

## Process

### Step 1: Gather Inputs

Ask the user for:
1. **Product description** — what it does, what category it's in, key features
2. **Target audience** — who buys or uses the product (role, industry, company size)
3. **Known competitors** (optional) — names or URLs to include without searching
4. **Number to find** (optional) — default: 5-7

### Step 2: Build Search Queries

Construct 4-6 search queries mixing these angles:

- **Category:** "[category] tools 2025 2026" or "[category] software"
- **Alternative:** "[product name] alternatives" or "tools like [product name]"
- **Problem:** "[primary use case] solution" or "[pain point] tool"
- **Audience:** "best [category] for [target company type]" or "[category] for [target role]"
- **Comparison:** "best [category] compared" or "top [category] platforms"
- **Review sites:** "[category] G2" or "[category] Capterra" (to mine company names from lists)

Tailor queries to the product type. A B2B SaaS product needs different queries than a marketplace or agency service.

### Step 3: Search and Collect

Run web searches for each query. For each result:
- Extract company names and domains that appear across multiple results
- Pull companies listed on review/comparison sites (G2, Capterra, etc.) — these are strong signals
- Skip aggregator sites themselves, job boards, news articles about funding, and clearly unrelated results

Compile a **candidate list** of 8-12 companies. For each, note:
- **Name**
- **URL** (homepage)
- **How found** — which search queries surfaced them

Rank candidates by frequency — companies appearing in 3+ different searches are almost certainly direct competitors.

### Step 4: Quick Profile Each Candidate

For each candidate, fetch their homepage (and pricing page if easily accessible) and extract:
- **One-liner** — what they say they do, in their own words
- **Target audience signals** — who the site speaks to
- **Overlap** — how directly they compete (direct / adjacent / tangential)

Classify each candidate:
- **Direct competitor** — same problem, same audience, similar solution
- **Adjacent competitor** — same audience but different approach, or same approach but different audience
- **Tangential** — some overlap but fundamentally different product

Drop tangential candidates unless the list would be too short (fewer than 3 direct competitors).

### Step 5: Present for Confirmation

Present the ranked list to the user:

```
I found these competitors for [product name]:

Direct competitors:
1. [Name] — [one-liner] — [url]
2. [Name] — [one-liner] — [url]
3. [Name] — [one-liner] — [url]

Adjacent competitors:
4. [Name] — [one-liner] — [url]
5. [Name] — [one-liner] — [url]

Should I save these? Any to add or remove?
```

Wait for user confirmation. They may know competitors that web search missed, or flag false positives.

## Output Format

```
# Competitor Discovery: [Product Name]

**Date:** [current date]
**Competitors found:** [X]

## Competitors

| # | Name | URL | Type | One-Liner |
|---|------|-----|------|-----------|
| 1 | [name] | [url] | Direct | [what they do] |
| 2 | [name] | [url] | Direct | [what they do] |
| 3 | [name] | [url] | Adjacent | [what they do] |

## Search Queries Used
- [query 1] — [X results]
- [query 2] — [X results]

## Recommended Next Steps
- Run competitor-site-analysis on top competitors for full profiles (pricing, moats, GTM signals)
- Run competitor-landscape after 2+ analyses for cross-competitor comparison and positioning map
```

## Rules

- Never include a company without visiting their site — one-liners must come from their actual homepage.
- Never guess at pricing — only note what's publicly visible on the homepage or pricing page.
- Never include more than 7 competitors without user approval — keep the list focused.
- If web search returns fewer than 3 relevant competitors, the category may be too niche — try broader search terms.
- If the market appears very crowded (15+ candidates found), suggest focusing on direct competitors only.
- Re-run every 6 months or after significant product/market changes.
