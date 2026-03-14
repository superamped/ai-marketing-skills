---
name: influencer-discovery
description: "Discover 100+ influencers across YouTube, X/Twitter, blogs, newsletters, podcasts, and Instagram — scored by Audience Overlap."
compatibility: "Requires internet access for web search and profile lookups."
metadata:
  author: superamped
  version: "1.0"
  website: "https://superamped.com"
---

# Influencer Discovery

## Usage

Use when finding influencers to partner with for sponsorships, affiliate deals, or co-marketing. Also useful for identifying thought leaders your target audience already follows, building a media list for outreach or PR, or understanding who shapes opinion in your niche before creating content.

## Process

### Step 1: Gather Inputs

Ask the user for:
1. **Industry/niche** — the topic domain (e.g., "B2B SaaS marketing", "personal finance for millennials", "indie game development")
2. **Target audience** — who follows these influencers, framed as the buyer (e.g., "SaaS founders", "freelance developers", "e-commerce store owners")
3. **Platform focus** (optional) — prioritize specific platforms (YouTube, X/Twitter, Newsletters, Podcasts, Instagram). Default: search all.
4. **Minimum follower count** (optional) — exclude influencers below a threshold. Default: no minimum (micro-influencers included).

Extract from inputs:
- **Niche keywords:** The 3-5 topic terms that define the industry
- **Audience profile:** Who the target audience is (role, stage, problem domain)
- **Platform priorities:** Which platforms to weight more heavily

### Step 2: Generate Search Queries

Generate 10 search queries to surface influencers across platform types and discovery angles:

**"Top influencers" list queries:**
- "top [niche] influencers [current year]"
- "best [niche] creators to follow"
- "top [audience] thought leaders"

**Platform-specific queries:**
- "top [niche] youtube channels"
- "[niche] youtube [subscribers OR creators]"
- "best [niche] newsletter substack"
- "top [niche] podcast"
- "[niche] twitter thought leaders"

**Cross-platform discovery:**
- "[niche] conference speakers [current year]"
- "who sponsors [niche] newsletters"
- "[niche] podcast guest list"

### Step 3: Search YouTube

Search YouTube for top channels in the niche:
- Use queries: "top [niche] YouTube channels", "[audience] YouTube", "[niche keyword] tutorial/advice channel"
- For each channel found, collect: Channel name, URL, subscriber count, content focus
- Aim for 20-30 YouTube channels across macro (500k+), mid-tier (50k-500k), and micro (<50k) tiers

### Step 4: Search X/Twitter

Search for thought leaders on X/Twitter:
- Use queries: "[niche] twitter", "best [niche] accounts to follow", "[identity/role] twitter"
- Check "listicles" — blog posts titled "Best [niche] accounts to follow on Twitter/X" often list 10-20 accounts at once
- Include both prolific posters (daily content) and respected practitioners (less frequent but high-quality takes)

### Step 5: Search Blogs, Newsletters, and Podcasts

#### Blogs
- Search: "top [niche] blogs", "best [niche] blog to read", "[niche] writers"
- Look for independent writers with their own sites

#### Newsletters
- Search: "best [niche] newsletter", "[niche] substack", "[niche] email newsletter"
- Check Substack's discover page for the niche if applicable

#### Podcasts
- Search: "top [niche] podcast", "best [niche] podcast", "[audience] podcast"
- Check Apple Podcasts and Spotify charts if accessible

### Step 6: Search Meta (Facebook and Instagram)

- Search: "[niche] facebook page", "[identity] instagram", "[niche] instagram creator"
- Focus on public profiles and pages
- Meta is lower priority for most B2B niches — if the niche skews consumer or visual, prioritize more heavily

### Step 7: Mine Cross-Platform Discovery Sources

#### Conference Speaker Lists
- Search: "[niche] conference [current year] speakers", "[niche] summit speakers"
- Conference keynote and session speakers are pre-vetted as recognized voices
- Extract speaker names → find their primary platform

#### Podcast Guest Cross-References
- Search: "[top podcast in niche] guests", "most popular [niche] podcast episodes"
- Repeat guests on multiple podcasts = high-credibility signal

#### Newsletter Curator Lists
- Search: "who sponsors [niche] newsletters", "[niche] newsletter sponsors"
- Companies sponsoring newsletters indicate which newsletters have a commercially valuable audience

### Step 8: Normalize All Results

Compile all discovered influencers into a single list. For each entry, record:

| Field | Description |
|-------|-------------|
| Name | Person or brand name |
| Primary Platform | The platform where they have the largest/most active presence |
| X/Twitter URL | Profile URL or "—" |
| YouTube URL | Channel URL or "—" |
| Newsletter/Blog URL | URL or "—" |
| Podcast URL | URL or "—" |
| Instagram/Facebook URL | URL or "—" |
| Primary Follower Count | Count on their primary platform |
| Content Type | What they primarily create (tutorials, opinion/takes, case studies, interviews, tools) |
| Source | Where they were discovered |

**Deduplication:** If the same person appears from multiple discovery sources, merge into one entry. Multiple discovery sources = stronger relevance signal.

### Step 9: Score Each Influencer

Score every influencer on Relevance (1–5):

| Score | Signal |
|-------|--------|
| 5 | Content is directly about the target audience's core problems — almost every post/video is on-target |
| 4 | Strong match — most content is relevant, occasional tangents |
| 3 | Adjacent — their niche overlaps meaningfully but isn't a perfect match |
| 2 | Loose match — some relevant content but audience is broader or different |
| 1 | Tangential — topic surface-level overlap but different audience |

#### Audience Overlap Rating

| Rating | Criteria |
|--------|----------|
| **High** | Relevance ≥ 4 |
| **Medium** | Relevance = 3 |
| **Low** | Relevance ≤ 2 |

### Step 10: Sort and Finalize

Sort the full list:
1. **Primary:** Audience Overlap rating (High → Medium → Low)
2. **Secondary:** Primary follower count (largest first within each tier)

Include micro-influencers (1K–50K followers) alongside macro — do not exclude them.

## Output Format

```
# Influencer Discovery: [Industry/Niche]

**Date:** [current date]
**Industry/Niche:** [description]
**Target Audience:** [description]
**Influencers found:** [count] across [X] platforms
**Audience Overlap breakdown:** High: [X] | Medium: [X] | Low: [X]

---

## High Overlap Influencers

| # | Name | Primary Platform | Followers | X/Twitter | YouTube | Newsletter/Blog | Podcast | Instagram/FB | Content Type | Discovery Source |
|---|------|-----------------|-----------|-----------|---------|-----------------|---------|-------------|-------------|-----------------|
| 1 | [name] | [platform] | [count] | [url or —] | [url or —] | [url or —] | [url or —] | [url or —] | [type] | [source] |

---

## Medium Overlap Influencers
[Same table structure]

---

## Low Overlap Influencers
[Same table structure]

---

## Platform Coverage Summary

| Platform | Count | High Overlap | Notes |
|----------|-------|-------------|-------|
| X/Twitter | X | X | [observation] |
| YouTube | X | X | |
| Newsletter/Blog | X | X | |
| Podcast | X | X | |
| Instagram/Facebook | X | X | |

---

## Observations
[2-3 bullet points: where this niche's influencer ecosystem is concentrated, tier distribution, notable patterns]

## Partnership Opportunities
[Top 3-5 influencers worth prioritizing for sponsorship or collaboration, with a 1-sentence reason each]

## Recommended Next Steps
1. [e.g., "Reach out to top 3 High Overlap newsletter authors — newsletter sponsorships often have fastest lead time"]
2. [e.g., "Monitor [top X/Twitter account] for mentions of problems your product solves"]
```

## Rules

- Aim for 100+ influencers total. For narrow B2B niches, 50 is acceptable — flag it.
- Never invent influencer accounts or inflate follower counts — only include verified results from search.
- Never exclude micro-influencers (1K–50K) — they are often the highest-value partnerships for niche B2B audiences.
- Never focus only on one platform — cross-platform coverage is a core output requirement.
- Discovery source matters: an influencer found via conference speakers + podcast guest + YouTube search is more credible than one found via a single listicle.
- Follower counts are best-effort estimates — verify before outreach.
- If fewer than 30 influencers are found, try broader synonyms for the niche or audience.
