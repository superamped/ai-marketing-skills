---
name: search-page-audit
description: "Run a 38-point SEO + AI optimization audit on any URL. Evaluates SEO fundamentals, content structure, AI/GEO readiness, and E-E-A-T authority signals. Returns a scored report with prioritized fixes. Use when asked to audit a page, check search visibility, or evaluate a URL for SEO and AI readiness."
compatibility: "Requires internet access to fetch URLs, robots.txt, sitemap.xml, and llms.txt"
metadata:
  author: superamped
  version: "1.0"
  website: "https://superamped.com"
---

# Search Audit

## Usage

Ask your AI tool to audit a URL for search and AI readiness. You can optionally request a focus area — `seo-only`, `geo-only`, `eeat-only`, or `content-only`.

## Process

### Step 1: Fetch & Parse

Fetch the page at the provided URL. Extract:

- Full HTML source (for schema, meta tags, heading structure)
- Rendered page content (for content evaluation)

Then fetch these three files from the same domain:

- `{domain}/robots.txt` — check for AI crawler directives
- `{domain}/sitemap.xml` — check for existence
- `{domain}/llms.txt` — check for existence

### Step 2: SEO Fundamentals (10 checks)

Evaluate traditional SEO hygiene. These are prerequisites — if broken, nothing else matters.

1. **HTTPS** — Page is served over HTTPS
2. **Title tag** — Exists, 50-60 characters, descriptive
3. **Meta description** — Exists, 150-160 characters, includes target intent
4. **Single H1** — Exactly one H1 tag present
5. **Heading hierarchy** — Logical order (H1 > H2 > H3), no skipped levels, no empty headings
6. **Image alt text** — All images have descriptive alt attributes
7. **Clean URL** — Descriptive, readable, no excessive parameters
8. **Internal links** — Links to and from related pages on the site
9. **Crawlable content** — Key content in standard HTML, not hidden behind JavaScript rendering
10. **Page speed** — No obvious performance issues (heavy uncompressed images, render-blocking scripts, excessive DOM size)

### Step 3: Content Structure (10 checks)

Evaluate how well the content is structured for both human readers and AI extraction.

11. **Direct answer up front** — Each section leads with the key insight in the first 1-2 sentences
12. **Question-based headings** — H2s/H3s mirror how users phrase queries (What is..., How do I..., Why does...)
13. **Short paragraphs** — 2-4 sentences per paragraph, no wall-of-text blocks
14. **FAQ section** — Dedicated Q&A section with real customer/user questions, 1-3 sentence answers
15. **Comparison tables** — Side-by-side content uses tables (35% higher AI extractability)
16. **Lists for structure** — Numbered lists for processes, bullet points for features/options
17. **"[TERM] is..." definitions** — Key concepts defined with at least two defining sentences
18. **Conversational keywords** — 5+ natural, long-tail query variations woven into content
19. **Intent clusters** — Covers related follow-up questions a user would likely ask next
20. **Multimedia** — Images, video, or infographics present as content signals

### Step 4: AI & GEO Readiness (10 checks)

Evaluate technical signals that determine whether AI systems can find, extract, and cite this page.

21. **AI crawler access** — robots.txt does not block GPTBot, ClaudeBot, or other AI user agents
22. **llms.txt exists** — Domain has an llms.txt file communicating AI crawling policies
23. **Organization schema** — JSON-LD with @type Organization present (site-wide entity definition)
24. **Article/Page schema** — Appropriate JSON-LD for the content type (Article, HowTo, Product) with dateModified
25. **FAQPage schema** — Separate FAQPage JSON-LD if FAQ section exists
26. **Author schema** — Author entity linked in structured data
27. **BreadcrumbList schema** — JSON-LD clarifying site hierarchy
28. **Schema validates** — All structured data passes validation (well-formed JSON, no errors)
29. **Mobile responsive** — Content readable and functional across screen sizes
30. **Sitemap inclusion** — Domain has a sitemap.xml and it's accessible

### Step 5: E-E-A-T & Authority (8 checks)

Evaluate trust signals that determine whether AI systems choose to cite this page over competitors.

31. **Author identified** — Content has a named author, not "admin" or anonymous
32. **Author bio present** — Author bio with credentials, expertise, and link to author page
33. **Author page exists** — Dedicated author page with full credentials, external profiles, and publication history
34. **Sources cited** — Key claims backed by specific data points with clear attribution
35. **Original data or insight** — Contains first-party research, proprietary analysis, or unique expert perspective
36. **Freshness signals** — Publication date and/or last-updated date visible on page
37. **Trust pages accessible** — Privacy policy, terms, and relevant compliance pages exist and are linked
38. **About page with entity info** — About Us/About page clearly defines the business entity

## Output Format

Present the report in this exact structure:

```
# Page Audit Report

**URL:** [url]
**Date:** [current date]
**Overall Score:** X/38

---

## SEO Fundamentals (X/10)

✓/✗ HTTPS
✓/✗ Title tag — [note: actual title, character count]
✓/✗ Meta description — [note: actual description, character count]
✓/✗ Single H1
✓/✗ Heading hierarchy
✓/✗ Image alt text — [note: X of Y images have alt text]
✓/✗ Clean URL
✓/✗ Internal links
✓/✗ Crawlable content
✓/✗ Page speed

## Content Structure (X/10)

✓/✗ Direct answer up front
✓/✗ Question-based headings
✓/✗ Short paragraphs
✓/✗ FAQ section
✓/✗ Comparison tables
✓/✗ Lists for structure
✓/✗ "[TERM] is..." definitions
✓/✗ Conversational keywords
✓/✗ Intent clusters
✓/✗ Multimedia

## AI & GEO Readiness (X/10)

✓/✗ AI crawler access — [note: which crawlers blocked/allowed]
✓/✗ llms.txt
✓/✗ Organization schema
✓/✗ Article/Page schema — [note: type found, dateModified present?]
✓/✗ FAQPage schema
✓/✗ Author schema
✓/✗ BreadcrumbList schema
✓/✗ Schema validates
✓/✗ Mobile responsive
✓/✗ Sitemap inclusion

## E-E-A-T & Authority (X/8)

✓/✗ Author identified — [note: author name if found]
✓/✗ Author bio present
✓/✗ Author page exists
✓/✗ Sources cited — [note: X citations found]
✓/✗ Original data or insight
✓/✗ Freshness signals — [note: dates found]
✓/✗ Trust pages accessible
✓/✗ About page with entity info

---

## Score Summary

| Category | Score | Rating |
|----------|-------|--------|
| SEO Fundamentals | X/10 | |
| Content Structure | X/10 | |
| AI & GEO Readiness | X/10 | |
| E-E-A-T & Authority | X/8 | |
| **Overall** | **X/38** | |

**Rating scale:** 90%+ Excellent | 75-89% Good | 60-74% Needs Work | Below 60% Poor

---

## Priority Fixes

[Top 5 failed criteria ranked by impact. For each:]

1. **[Failed criterion]** — [Why it matters + specific fix with actual suggested text/code where possible]
2. ...
```

## Rules

- Be objective. If borderline, lean toward FAIL and explain in priority fixes.
- Be specific in fixes — suggest actual meta description text, actual schema JSON, actual heading rewrites. "Add a meta description" is not useful. "Add meta description: '[suggested text]'" is.
- For schema checks, search page source for `<script type="application/ld+json">` and evaluate each block.
- Priority fixes should weight: technical foundation > AI readiness > content structure > E-E-A-T (you can't build authority on a broken page).
- If user specifies a focus area, still run all checks but only expand detail on the requested section.