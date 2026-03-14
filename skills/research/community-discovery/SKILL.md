---
name: community-discovery
description: "Discover 100+ online communities across Reddit, Slack, Discord, Facebook, LinkedIn, and forums, scored by Signal-to-Noise ratio."
compatibility: "Requires internet access for web search and community directory lookups."
metadata:
  author: superamped
  version: "1.0"
  website: "https://superamped.com"
---

# Community Discovery

## Usage

Use when finding communities to engage with organically, identifying where a target market spends time online, or planning community-led GTM strategy.

## Process

### Step 1: Gather Inputs

Ask the user for:
1. **Audience description** — who they're targeting (job title, industry, stage). Example: "B2B SaaS founders at seed stage", "freelance UX designers", "e-commerce store owners"
2. **Product category** (optional) — what they sell, to help filter relevance and identify tool-adjacent communities
3. **Minimum member count** (optional) — exclude communities below a threshold (default: no minimum — small communities are included with a flag)

Extract from the audience description:
- **Identity/role:** Who is the person (founder, marketer, developer, etc.)
- **Industry/vertical:** What sector or market they're in
- **Business type/stage:** Solo, SMB, startup, agency, enterprise — or consumer
- **Problem domain:** What they're trying to solve (inferred from product category if provided)

### Step 2: Generate Search Queries

Generate 8 search queries to surface communities across platform types. Mix these angles:

**Platform-specific queries:**
- "slack community [identity/role]"
- "discord server [industry/niche]"
- "facebook group [job title or problem]"
- "linkedin group [industry]"
- "[identity] community forum"

**Directory-based queries:**
- "hive.one [audience topic]"
- "slofile [slack community] [niche]"
- "disboard [discord] [niche]"

**Discovery-angle queries:**
- "best communities for [identity]"
- "where do [audience] hang out online"
- "[industry] online community"

### Step 3: Search Platform Directories

Search these community directories first — they surface communities across many platforms in one pass:

| Directory | What It Indexes | How to Search |
|-----------|----------------|---------------|
| hive.one | Audience-indexed communities by topic | Search by topic or person |
| slofile.com | Public Slack workspaces | Search by keyword |
| disboard.org | Discord servers by tag | Search by tag/keyword |
| discadia.com | Discord servers | Search by category/keyword |
| commsor.com | Community index | Browse by category |

For each directory, search with the audience's identity, industry, and problem domain terms. Collect all relevant results.

### Step 4: Search Each Platform Directly

#### Reddit
Search for subreddits using:
- "site:reddit.com [identity/role]"
- "reddit [industry] community"
- "r/findareddit [audience description]"

Collect subreddit name, member count, and description.

#### Slack & Discord
Use slofile.com and disboard.org searches from Step 3. Also search:
- "[industry] slack community"
- "[niche] discord server"

#### Facebook Groups
Search: "facebook group [identity/role]" and "facebook group [industry]". Note: member counts require browsing Facebook directly — estimate when not verifiable.

#### LinkedIn Groups
Search: "linkedin group [industry]" and "linkedin group [job title]". Note: LinkedIn groups vary widely in activity — flag low-activity groups.

#### Other Platforms
Search for:
- **Mighty Networks / Circle:** "[industry] community mighty networks" or "[niche] circle community"
- **Geneva:** "[identity] geneva community"
- **Luma:** "[niche] luma community events"
- **Discourse forums:** "[industry] forum site:community.* OR site:forum.*"
- **Industry-specific forums:** "[industry] forum" + check known industry directories

### Step 5: Normalize All Results

Compile all discovered communities into a single list. For each entry, record:

| Field | Description |
|-------|-------------|
| Name | Community name |
| URL | Direct link to the community |
| Platform Type | Reddit / Slack / Discord / Facebook Group / LinkedIn Group / Forum / Other |
| Member Count | Total member/subscriber count (or "unverified" if unknown) |
| Description | One-line summary of what the community is about |
| Source | Where it was discovered (directory name or search) |

**Deduplication:** If the same community appears from multiple sources, keep one entry and note it appeared in multiple places (stronger signal of relevance).

**Member count = 0 or unknown:** Include but flag as "unverified." Small/unknown-size communities are still worth noting if relevance is high.

### Step 6: Score Each Community

Score every community on two dimensions:

#### Dimension 1: Relevance (1–5)

| Score | Signal |
|-------|--------|
| 5 | Community is built specifically for this exact audience (identity + industry match) |
| 4 | Strong match — same role or same industry, minor gaps |
| 3 | Adjacent — related audience, overlapping interests |
| 2 | Loose match — your audience is a minority here |
| 1 | Tangential — topic overlap but very different audience |

#### Dimension 2: Noise (1–5)

| Score | Signal |
|-------|--------|
| 1 | Very low noise — tightly moderated, mostly signal |
| 2 | Low noise — mostly on-topic with occasional spam |
| 3 | Moderate noise — mixed quality, some spam |
| 4 | High noise — significant spam or off-topic content |
| 5 | Very high noise — dominated by promotions or irrelevant content |

#### Signal-to-Noise Rating

| Rating | Criteria |
|--------|----------|
| **High** | Relevance ≥ 4 AND Noise ≤ 2 |
| **Medium** | Relevance 3–4 OR Noise = 3 (not both extremes) |
| **Low** | Relevance ≤ 2 OR Noise ≥ 4 |

### Step 7: Sort and Finalize

Sort the full list:
1. **Primary:** Signal-to-Noise rating (High → Medium → Low)
2. **Secondary:** Member count (largest first within each tier)

Flag communities where member count is unverified — place them after verified-count communities within the same S/N tier.

## Output Format

```
# Community Discovery: [Audience Description]

**Date:** [current date]
**Audience:** [description]
**Communities found:** [count] across [X] platforms
**Signal-to-Noise breakdown:** High: [X] | Medium: [X] | Low: [X]

---

## High Signal Communities

| # | Name | URL | Platform | Members | S/N | Notes |
|---|------|-----|----------|---------|-----|-------|
| 1 | [name] | [url] | [type] | [count] | High | [brief note on why it's a fit] |

---

## Medium Signal Communities

| # | Name | URL | Platform | Members | S/N | Notes |
|---|------|-----|----------|---------|-----|-------|
| 1 | [name] | [url] | [type] | [count] | Medium | [brief note] |

---

## Low Signal Communities

| # | Name | URL | Platform | Members | S/N | Notes |
|---|------|-----|----------|---------|-----|-------|
| 1 | [name] | [url] | [type] | [count] | Low | [brief note] |

---

## Platform Coverage Summary

| Platform | Count | High S/N | Notes |
|----------|-------|----------|-------|
| Reddit | X | X | [observation] |
| Slack | X | X | |
| Discord | X | X | |
| Facebook Groups | X | X | |
| LinkedIn Groups | X | X | |
| Forums/Other | X | X | |

---

## Observations

[2-3 bullet points on where this audience is most concentrated, any surprising findings, or gaps]

## Recommended Next Steps

1. [e.g., "Join the top 3 High S/N communities and lurk for 1 week before engaging"]
2. [e.g., "No LinkedIn groups had high activity — deprioritize LinkedIn as a community channel"]
```

## Rules

- Aim for 100+ communities total. If the audience is niche, 50 is acceptable — flag it.
- Platform coverage matters more than raw count. A list with 100 Reddit results and 0 Slack results may miss important communities.
- Community size is a secondary factor. A 200-member Slack group of exactly your target buyer is often more valuable than a 50k-member Discord with 5% audience match.
- Never invent communities that weren't found via search — only include verified results.
- Never guess member counts — mark unknown counts as "unverified."
- Don't skip platforms because they seem unlikely — search all 5 categories and let the results speak.
- If fewer than 20 communities are found, the search was too narrow — broaden by using more generic identity/industry terms.
- If the audience description is very broad (e.g., "small businesses", "marketers"), ask the user to narrow it before proceeding.
- Flag if all high-signal communities are very small (under 500 members) — the audience may not have a strong online community presence.
