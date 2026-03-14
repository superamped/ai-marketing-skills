---
name: keyword-research
description: "Expand a seed keyword into a clustered keyword universe using Keywords Everywhere MCP — grouped by search intent, scored, and prioritized."
compatibility: "Requires Keywords Everywhere MCP."
metadata:
  author: superamped
  version: "1.0"
  website: "https://superamped.com"
---

# Keyword Research

## Usage

Use when planning content around a topic before writing, building a keyword map for a new content area, finding question-based keywords for GEO optimization, or identifying gaps where competitors rank and you don't.

## Process

### Step 1: Gather Inputs

Ask the user for:
1. **Seed topic or keyword** — e.g., "AI search optimization", "B2B SaaS customer acquisition"
2. **Country code** (optional) — for localised volumes (default: "us")
3. **Competitor domain(s)** (optional) — to identify keyword gaps
4. **Number of clusters** (optional) — default: let the data dictate

### Step 2: Validate & Prepare

- Confirm the Keywords Everywhere MCP server is connected. If not configured, tell the user — this skill requires it.
- Check credit balance with **Get Credit Balance** before starting — warn the user if credits are low.

**Credit estimate formula:** `(related_count + pasf_count) * 2` credits for expansion + `total_unique_keywords * 1` credit for metrics. A typical run with 100 related + 100 PASF keywords costs ~500 credits. Warn if balance would drop below 1,000 after the run.

### Step 3: Expand the Seed

Run two Keywords Everywhere tools against the seed keyword:

1. **Get Related Keywords** (num: 100) — returns a list of keyword strings (no metrics yet)
2. **Get "People Also Search For" Keywords** (num: 100) — returns a list of keyword strings (no metrics yet)

**If PASF returns empty results:** This is common for newer or niche terms. Proceed with the related keywords only. If the combined list is thin (< 30 keywords), consider running a second expansion on a broader variant of the seed.

Combine the results into a single deduplicated keyword list.

If the seed returns fewer than 20 keywords total, it may be too narrow. Suggest broader alternatives to the user.

### Step 3b: Pull Metrics

Run **Get Keyword Data** on the deduplicated keyword list to get volume, CPC, competition, and trend data for every keyword.

**Batch in groups of 50 keywords per API call** to avoid oversized responses. Run batches in parallel where possible.

Parameters: `country: "us"` (or from user input), `currency: "usd"`, `dataSource: "cli"` (includes clickstream data for more accurate volumes).

### Step 4: Competitor Gap Analysis (optional)

If competitor domain(s) were provided:

1. **Get Domain Keywords** for each competitor — returns keywords they rank for
2. Cross-reference with the expanded keyword list from Step 3
3. Flag keywords where competitors rank but the user's domain doesn't — these are gaps
4. Add any high-volume competitor keywords that didn't appear in the Step 3 expansion

If no competitors provided, skip this step.

### Step 5: Cluster by Intent

Group the full keyword list into semantic clusters. Each cluster represents a potential piece of content.

**Pre-clustering: Filter brand/navigational noise**

Before clustering, separate out brand-specific and product-name keywords. These are navigational queries for specific tools, not topics you'd write content about. List them in an "Excluded: Brand/Navigational Keywords" section at the end — they're useful market intelligence but shouldn't inflate your topic clusters.

**Clustering rules:**
- Group keywords that would be answered by the same piece of content
- Name each cluster after its core topic (not the highest-volume keyword)
- Assign an intent to each cluster:
  - **Informational** — "what is", "how to", "why does" — answered by blog posts, guides
  - **Commercial** — "best", "vs", "review", "pricing" — answered by comparison pages, landing pages
  - **Navigational** — brand-specific or product-specific queries — answered by product/feature pages
  - **Transactional** — "buy", "sign up", "get started" — answered by landing pages, pricing pages
- A cluster should have 3–20 keywords. If larger, split into sub-clusters. If smaller, consider merging.
- Keywords with very low volume (< 10/mo) can be grouped into clusters but shouldn't form their own cluster
- Drop zero-volume keywords entirely

**Within each cluster, identify:**
- The **primary keyword** — highest volume keyword that best represents the cluster's intent
- **Question keywords** — any keywords phrased as questions (valuable for H2 headings and FAQ sections)
- **Long-tail keywords** — lower volume, more specific phrases (valuable for weaving into content)

### Step 6: Prioritize

Score each cluster for content priority:

| Signal | What to look at |
|--------|----------------|
| **Total volume** | Sum of all keyword volumes in the cluster |
| **Competition** | Average competition score (lower = easier to rank) |
| **Gap opportunity** | Are competitors ranking here and you're not? (from Step 4) |
| **Intent fit** | Does this cluster match content you'd actually create? |
| **Question density** | Clusters with more question keywords are better for GEO |

Rank clusters by a blended priority — not just volume. A low-competition cluster with good question density and a clear gap often beats a high-volume, high-competition cluster.

## Output Format

```
# Keyword Research: [Seed Topic]

**Seed:** [seed keyword]
**Date:** [current date]
**Total keywords found:** [X]
**Clusters:** [X]

---

## Cluster 1: [Cluster Name]

**Intent:** Informational / Commercial / Navigational / Transactional
**Primary keyword:** [keyword] ([volume]/mo)
**Total cluster volume:** [X]/mo
**Avg competition:** [X]
**Gap opportunity:** Yes / No
**Priority:** High / Medium / Low

| Keyword | Volume | CPC | Competition | Type |
|---------|--------|-----|-------------|------|
| [keyword] | [vol] | [cpc] | [comp] | Primary |
| [question keyword]? | [vol] | [cpc] | [comp] | Question |
| [long-tail keyword] | [vol] | [cpc] | [comp] | Long-tail |

---

## Cluster 2: [Cluster Name]
[Same format...]

---

## Summary

| Cluster | Intent | Primary Keyword | Volume | Competition | Priority |
|---------|--------|----------------|--------|-------------|----------|
| [name] | [intent] | [keyword] | [vol] | [comp] | High |
| [name] | [intent] | [keyword] | [vol] | [comp] | Medium |

## Recommended Next Steps

- [Which clusters to write first and why]
- [Suggested content type for each high-priority cluster]
- [Any gaps that need competitor research first]
```

## Rules

- Never invent keyword volumes or competition scores — all data must come from the Keywords Everywhere API.
- Never cluster keywords you haven't actually retrieved — don't pad clusters with guesses.
- Never present unclustered keyword dumps — always group and prioritize.
- If the MCP server is not connected, stop and tell the user.
- If credit balance is low (< 100 credits), warn before starting.
- If the seed returns fewer than 20 keywords, suggest broadening.
- If the seed returns 1000+ keywords, confirm they want the full expansion or suggest narrowing.
- Country code matters — volumes vary significantly by market. Default to "us" if no country specified.
- Run this skill periodically (quarterly) on core topics to catch new keywords and shifting volumes.
