---
name: content-strategy
description: "Plan content strategy including pillars, topic clusters, editorial calendar, and keyword research by buyer stage."
compatibility: "Requires internet access for competitor and forum research. Optional: keyword data from external tools."
metadata:
  author: superamped
  version: "1.0"
  website: "https://superamped.com"
---

# Content Strategy

## Usage

Use when building or refreshing a content strategy from scratch, planning content pillars and topic clusters, creating an editorial calendar, or identifying high-priority content opportunities by buyer stage.

## Process

### Step 1: Gather Inputs

Ask the user for:

**Business Context:**
1. What does the company do?
2. Who is the ideal customer? (role, industry, pain points, language they use)
3. What's the primary goal for content? (traffic, leads, brand awareness, thought leadership)
4. What problems does your product solve?

**Customer Research:**
5. What questions do customers ask before buying?
6. What objections come up in sales calls?
7. What topics appear repeatedly in support tickets?

**Current State:**
8. Do you have existing content? What's working?
9. What resources do you have? (writers, budget, time)
10. What content formats can you produce? (written, video, audio)

**Competitive Landscape:**
11. Who are your main competitors?
12. What content gaps exist in your market?

If the user has previously run competitor-content-analysis, they can reference those outputs for richer competitive data.

### Step 2: Define Content Pillars

Content pillars are the 3-5 core topics your brand will own. Each pillar spawns a cluster of related content.

**How to Identify Pillars:**
1. **Product-led**: What problems does your product solve?
2. **Audience-led**: What does your ICP need to learn?
3. **Search-led**: What topics have volume in your space?
4. **Competitor-led**: What are competitors ranking for?

**Pillar Criteria — good pillars should:**
- Align with your product/service
- Match what your audience cares about
- Have search volume and/or social interest
- Be broad enough for many subtopics

**Pillar Structure:**
```
Pillar Topic (Hub)
├── Subtopic Cluster 1
│   ├── Article A
│   ├── Article B
│   └── Article C
├── Subtopic Cluster 2
│   ├── Article D
│   ├── Article E
│   └── Article F
└── Subtopic Cluster 3
    ├── Article G
    ├── Article H
    └── Article I
```

Most content works fine under `/blog` with good internal linking. Only use dedicated hub/spoke URL structures for major topics with layered depth.

### Step 3: Build Topic Clusters

For each pillar, generate subtopic clusters. Classify every piece of content as:

**Searchable content** captures existing demand. Optimized for people actively looking for answers.
- Target a specific keyword or question
- Match search intent exactly
- Use clear titles that match search queries
- Provide comprehensive coverage

**Shareable content** creates demand. Spreads ideas and gets people talking.
- Lead with a novel insight, original data, or counterintuitive take
- Tell stories that make people feel something
- Create content people want to share to look smart or help others

**Content Types:**

| Type | Category | Best for |
|------|----------|----------|
| Use-Case Content | Searchable | Long-tail keywords — "[persona] + [use-case]" |
| Hub and Spoke | Searchable | Comprehensive overview + related subtopics |
| Template Libraries | Searchable | High-intent keywords + product adoption |
| Thought Leadership | Shareable | Naming concepts, challenging conventional wisdom |
| Data-Driven Content | Shareable | Product data analysis, original research |
| Expert Roundups | Shareable | 15-30 experts answering one question, built-in distribution |
| Case Studies | Both | Challenge → Solution → Results → Key learnings |
| Meta Content | Shareable | Behind-the-scenes transparency |

### Step 4: Map Keywords by Buyer Stage

Map topics to the buyer's journey using proven keyword modifiers:

**Awareness Stage** — "what is," "how to," "guide to," "introduction to"

**Consideration Stage** — "best," "top," "vs," "alternatives," "comparison"

**Decision Stage** — "pricing," "reviews," "demo," "trial," "buy"

**Implementation Stage** — "templates," "examples," "tutorial," "how to use," "setup"

### Step 5: Prioritize Content Ideas

Score each idea on four factors:

| Factor | Weight | What to evaluate |
|--------|--------|-----------------|
| **Customer Impact** | 40% | How frequently did this topic come up in research? How emotionally charged? |
| **Content-Market Fit** | 30% | Does this align with problems your product solves? Can you offer unique insights? |
| **Search Potential** | 20% | Monthly search volume? How competitive? Long-tail opportunities? |
| **Resource Requirements** | 10% | Do you have expertise? What additional research is needed? |

### Step 6: Source Content Ideas

Mine these sources for ideas:

**Keyword data:** If provided (from Ahrefs, SEMrush, GSC), analyze for topic clusters, buyer stage, intent, quick wins, and content gaps.

**Call transcripts:** Extract questions, pain points, objections, language patterns, competitor mentions.

**Forum research:**
- Reddit: `site:reddit.com [topic]` — top posts, questions, frustrations
- Quora: `site:quora.com [topic]` — most-followed questions
- Indie Hackers, Hacker News, Product Hunt, industry Slack/Discord

**Competitor content:** Use web search `site:competitor.com/blog` to find:
- Top-performing posts, topics covered repeatedly
- Gaps they haven't covered
- Content structure (pillars, categories, formats)
- Topics you can cover better, angles they're missing

### Step 7: Build the Content Plan

Assemble the final strategy.

## Output Format

```
# Content Strategy

**Date:** [current date]
**Company:** [company name]
**Goal:** [primary content goal]
**Audience:** [ICP description]

---

## Content Pillars

### Pillar 1: [Name]
**Rationale:** [why this pillar]
**Connection to product:** [how it ties to what you sell]

Subtopic clusters:
- [Cluster A] — [3-5 topic ideas]
- [Cluster B] — [3-5 topic ideas]
- [Cluster C] — [3-5 topic ideas]

### Pillar 2: [Name]
[Same structure]

### Pillar 3: [Name]
[Same structure]

---

## Priority Topics

| # | Topic/Title | Type | Buyer Stage | Keyword | Priority Score | Why |
|---|-------------|------|-------------|---------|---------------|-----|
| 1 | [title] | [searchable/shareable/both] | [awareness/consideration/decision/implementation] | [keyword] | [X/10] | [customer research backing] |

---

## Topic Cluster Map

[Visual or structured representation of how content interconnects]

---

## Content Calendar (First Month)

| Week | Topic | Type | Format | Buyer Stage | Notes |
|------|-------|------|--------|-------------|-------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |

---

## Content Gaps vs. Competitors

| Gap | Competitor | Opportunity | Priority |
|-----|-----------|-------------|----------|
| [topic/format they have that you don't] | [who] | [what to do] | [high/med/low] |

---

## Recommended Next Steps

1. [Most important action]
2. [Second action]
3. [Third action]
```

## Rules

- Every piece of content must be searchable, shareable, or both. Prioritize search — search traffic is the foundation.
- Specificity beats breadth. "Project management for designers" is better than "project management tips."
- Content pillars should be broad enough for many subtopics but specific enough to match your product.
- Don't plan more content than you can produce. A realistic calendar beats an ambitious one that dies in week 3.
- Prioritize customer impact over search volume. Content that directly addresses known customer pain points converts better than high-volume generic topics.
- If no customer research exists, recommend gathering it before committing to a full content plan. Even 5 customer interviews dramatically improve content-market fit.
