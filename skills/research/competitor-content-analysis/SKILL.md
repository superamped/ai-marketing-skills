---
name: competitor-content-analysis
description: "Analyze a competitor's content engine — what they publish, what earns traffic, what SEO plays they run, and where the content gaps are."
compatibility: "Requires internet access. Optional: Keywords Everywhere MCP for traffic metrics, Playwright MCP for JS-rendered pages."
metadata:
  author: superamped
  version: "1.0"
  website: "https://superamped.com"
---

# Competitor Content Analysis

## Usage

Use before building or refreshing your content strategy — map the competitive content landscape first. Also useful for identifying content gaps and opportunities vs. a specific competitor, or understanding what's earning a competitor organic traffic and why.

## Process

### Step 1: Gather Inputs

Ask the user for:
1. **Competitor name** — the company to analyze
2. **Competitor URL** — their homepage domain
3. **Your product description** — what you sell and who it's for (needed to assess relevance of competitor content)
4. **Keyword data** (optional) — if the user has previously run competitor-keyword-analysis, they can provide that data. Otherwise, this skill will attempt to pull it via Keywords Everywhere MCP if connected.

### Step 2: Content Inventory via Sitemap

Fetch `{url}/sitemap.xml` (and `{url}/sitemap_index.xml` if it's an index). Extract:

- **Total page count** by section (blog, guides, resources, docs, landing pages, etc.)
- **URL patterns** — how content is organized (`/blog/`, `/resources/`, `/guides/`, `/learn/`, `/glossary/`, `/templates/`, `/vs/`, `/alternatives/`, `/compare/`)
- **Publication dates** — when pages were published (if sitemap includes `<lastmod>`)
- **Publishing velocity** — how many new pages per month (recent 6 months)

If sitemap is unavailable, fall back to fetching the blog index and resource pages, then use keyword data to infer content scope from ranking URLs.

### Step 3: Content Categorization

From the sitemap URLs and page fetches, categorize content into types:

| Content Type | URL Patterns to Look For | What It Signals |
|---|---|---|
| Blog posts | `/blog/`, `/posts/` | Core content engine — topics, frequency, depth |
| Guides / pillar pages | `/guides/`, `/learn/`, `/resources/`, `/academy/` | Hub-and-spoke SEO strategy, authority building |
| Comparison pages | `/vs/`, `/compare/`, `/alternatives/`, `*-vs-*`, `*-alternative*` | Commercial intent capture, direct competitor targeting |
| "Best of" / listicle pages | `best-*`, `top-*` | Category keyword capture |
| Glossary / definitions | `/glossary/`, `/dictionary/`, `what-is-*` | Programmatic SEO, awareness-stage traffic |
| Templates / tools | `/templates/`, `/tools/`, `/calculator/`, `/generator/` | Product-led content, high-intent capture |
| Case studies | `/case-studies/`, `/customers/`, `/success-stories/` | Social proof content, bottom-of-funnel |
| Webinars / video | `/webinars/`, `/events/`, `/videos/` | Event-driven content, lead capture |
| White papers / ebooks | `/whitepapers/`, `/ebooks/`, `/reports/` | Gated content for lead gen |
| Landing pages | `/solutions/`, `/for/`, `/use-cases/` | Segment-specific or use-case-specific targeting |
| Changelog / updates | `/changelog/`, `/updates/`, `/whats-new/` | Product velocity signaling |

Count pages per category. Note which categories exist and which don't — absent categories are potential opportunities.

### Step 4: Comparison & Alternative Pages

This gets its own step because it's high-value commercial intent content that directly affects competitive positioning.

Search for and fetch:
- Pages on their site matching `/vs/`, `/compare/`, `/alternatives/` patterns
- WebSearch: `site:{domain} vs` and `site:{domain} alternatives`

For each comparison page found:
- **Who they compare against** — which competitors do they target?
- **How they position themselves** — what dimensions do they claim to win on?
- **Are they targeting YOUR product?** — flag immediately if yes
- **Search ranking** — do these pages actually rank? (check via Keywords Everywhere if connected)

**If they have no comparison pages**, that's a gap you can exploit — especially for "[their name] alternatives" and "[their name] vs [your name]" keywords.

### Step 5: SEO Content Plays

Using keyword data (provided by user or pulled via Keywords Everywhere MCP), identify:

- **Dedicated keyword pages** — pages clearly built to rank for a specific term (exact-match URL slugs, optimized titles)
- **Programmatic content** — patterns that suggest templated/scaled content (e.g., 50 glossary pages, "[tool] integration" pages for every integration)
- **Hub-and-spoke structure** — pillar pages with clusters of supporting content
- **High-traffic content** — their top 10 pages by estimated traffic. What topics? What format?
- **Content themes** — cluster their ranking keywords into 3-5 themes. These are their content pillars.
- **Commercial vs. informational split** — what percentage of their traffic comes from commercial intent keywords (vs, best, pricing, alternative, review) vs. informational (how to, what is, guide)?

If no keyword data is available, assess these qualitatively from sitemap and page content.

### Step 6: Gated Content & Lead Gen

Assess their content-based lead generation:

Fetch their resource center / content library page if it exists. Look for:
- **Gated vs. ungated ratio** — what do they put behind email capture?
- **Types of gated content** — white papers, ebooks, templates, webinars, reports, tools
- **Lead magnets** — what do they offer in exchange for email? (visible on blog sidebars, popups, footer CTAs)
- **Content upgrade patterns** — do blog posts have in-post lead magnets related to the topic?
- **Nurture signals** — newsletter signup presence, "subscribe" CTAs, email course mentions

What they gate reveals what they believe is high enough value to trade for contact info. What they leave ungated is their traffic play.

### Step 7: Social Content & Distribution

Assess how they distribute content and where they're active:

Fetch their homepage footer and about page for social links. For each channel found:
- **Which platforms** — Twitter/X, LinkedIn, YouTube, TikTok, Instagram, etc.
- **Content type per platform** — do they repurpose blog content? Original social content? Video?
- **Posting frequency** — if visible (recent posts on embedded feeds)

Also check:
- **Newsletter** — is there a newsletter signup? What do they promise (frequency, content type)?
- **Podcast** — do they have one? Where is it distributed?
- **YouTube** — do they publish video content? What kind (tutorials, webinars, thought leadership)?

### Step 8: Content Gap Analysis

Cross-reference competitor content against your position:

**If keyword data is available:**
- Keywords they rank for that you don't — content they've written that you haven't
- Keywords you rank for that they don't — your existing advantages
- Keywords neither of you rank for — unclaimed territory

**If no keyword data is available**, assess gaps qualitatively:
- Content types they have that you don't (comparison pages, glossary, templates)
- Topics they cover extensively that you haven't touched
- Formats they use that you haven't tried

**For every gap, assess:**
- Can you cover this topic better? (more depth, better data, fresher perspective)
- Is the traffic worth it? (use keyword data to estimate opportunity size)
- Does it align with your product and audience?

### Step 9: Synthesize & Present

Present the content intelligence brief:

1. **One-paragraph summary** of their content strategy (volume, maturity, primary plays)
2. **Content inventory snapshot** — pages by type, publishing velocity
3. **Their content pillars** — the 3-5 themes dominating their organic presence
4. **Top performing content** — their 5-10 highest-traffic pages with format and topic
5. **Comparison page landscape** — what they own, what's missing
6. **Content gaps and opportunities** — specific topics/formats you can pursue
7. **Recommended content ideas** — 5-10 specific pieces with rationale, sorted by estimated impact

Ask: "Does this match what you've seen? Any content of theirs that stood out to you that I should factor in?"

## Output Format

```
# Content Analysis: [Competitor Name]

**URL:** [url]
**Date:** [current date]
**Total indexed pages:** [X]
**Publishing velocity:** [X pages/month]

## Content Inventory

| Content Type | Count | Notable |
|---|---|---|
| Blog posts | | |
| Guides / pillars | | |
| Comparison pages | | |
| Glossary / definitions | | |
| Templates / tools | | |
| Case studies | | |
| Gated content | | |
| Landing pages | | |

## Content Pillars
[Their 3-5 core content themes with estimated traffic per theme]

## Top Performing Content

| Page | Est. Monthly Traffic | Keywords Ranking | Format | Topic |
|---|---|---|---|---|
| [url] | [X] | [X] | [format] | [topic] |

## Comparison & Alternative Pages
[What they have, who they target, what's missing]

## SEO Content Plays
[Programmatic content, hub-and-spoke, dedicated keyword pages]

## Gated Content & Lead Gen
[What they gate, lead magnets, nurture signals]

## Social & Distribution
[Channels, content type per channel, engagement, newsletter]

## Content Gaps & Opportunities

| Opportunity | Type | Est. Traffic | Difficulty | Why |
|---|---|---|---|---|
| [topic/page] | [new/improve] | [X] | [low/med/high] | [rationale] |

## Recommended Content Ideas
[5-10 specific pieces with format, target keyword, and why]

## Data Sources
- Sitemap: accessible / not accessible
- Keywords Everywhere: connected / not connected
- Pages fetched: [list]
```

## Rules

- Never invent traffic numbers — all data must come from Keywords Everywhere or be clearly marked as estimates.
- Never recommend content ideas that don't align with the user's product and audience.
- Always cluster and prioritize — never present raw keyword dumps.
- If Keywords Everywhere MCP is not connected, note that SEO analysis will be limited to qualitative assessment. The skill still works — it just won't have traffic metrics.
- If the competitor has very little content (< 20 pages), flag that they may not have a content strategy worth analyzing.
- If the competitor has a comparison page targeting your product, flag it immediately.
- For a full competitive content landscape, recommend running this on 2-3 competitors and comparing their approaches.
