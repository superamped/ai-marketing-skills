---
name: competitor-keyword-analysis
description: "Map a competitor's organic search presence using Keywords Everywhere MCP — top keywords, traffic metrics, and content theme clusters."
compatibility: "Requires Keywords Everywhere MCP. Returns empty data gracefully if not connected."
metadata:
  author: superamped
  version: "1.0"
  website: "https://superamped.com"
---

# Competitor Keyword Analysis

## Usage

Use for a quick SEO snapshot of a competitor's organic presence, or as input to competitor-content-analysis for deeper content strategy mapping.

## Process

### Step 1: Gather Inputs

Ask the user for:
1. **Competitor name** — the company to analyze
2. **Competitor domain** — e.g., `example.com` (no protocol)
3. **Country code** (optional) — defaults to "us"

### Step 2: Validate MCP

Check that Keywords Everywhere MCP is connected.

**If not connected**, return empty data with the note: "Keywords Everywhere MCP not configured — SEO data not available." Don't block the user — return gracefully.

### Step 3: Domain Keywords

Pull `get_domain_keywords`:
- **domain:** competitor domain
- **country:** from input or "us"
- **num:** 100

This returns the top keywords the competitor ranks for, with estimated monthly traffic and SERP position per keyword.

### Step 4: Traffic Metrics

Pull `get_domain_traffic_metrics`:
- **domains:** [competitor domain]
- **country:** same as Step 3

This returns estimated monthly organic traffic and total ranking keywords for the domain.

### Step 5: Cluster into Content Themes

Group the top keywords into 3-5 content themes by topic similarity. For each theme:
- **Theme name** — descriptive label (e.g., "project management guides", "pricing comparisons")
- **Keywords in theme** — count
- **Combined estimated traffic** — sum of traffic for keywords in the theme
- **Top keyword** — highest-traffic keyword in the theme

These themes represent the competitor's content pillars from an SEO perspective.

## Output Format

```
# Keyword Analysis: [Competitor Name]

**Domain:** [domain]
**Date:** [current date]
**Estimated monthly organic traffic:** [X]
**Total ranking keywords:** [X]

## Top Keywords

| Keyword | Est. Monthly Traffic | SERP Position |
|---------|---------------------|---------------|
| | | |

## Content Themes

| Theme | Keywords | Combined Traffic | Top Keyword |
|-------|----------|-----------------|-------------|
| | | | |

## Data Sources
- Keywords Everywhere: connected / not connected
- Country: [code]
- Domain keywords pulled: [count]
```

## Rules

- Never invent traffic numbers — all data comes from Keywords Everywhere.
- Never call `get_related_keywords` or `get_pasf_keywords` — those are for keyword expansion, not competitor mapping.
- If the domain returns very few keywords (< 10), the competitor may have minimal organic presence or the domain may be wrong — flag it.
- If traffic metrics return zero, the domain may be too new or not indexed — flag it.
- If Keywords Everywhere MCP is not connected, clearly state that and return an empty report structure.
