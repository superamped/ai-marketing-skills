---
name: competitor-landscape
description: "Cross-competitor comparison — feature matrix, pricing comparison, 2x2 positioning map, aggregate SWOT, moat landscape, and strategic recommendations."
compatibility: "No special requirements. Best results when provided with detailed competitor data from prior analysis."
metadata:
  author: superamped
  version: "1.0"
  website: "https://superamped.com"
---

# Competitor Landscape

## Usage

Use after analyzing 2+ competitors — you have individual profiles and need the comparative view. Also useful for preparing a board deck, investor update, or strategy doc that needs a market landscape section.

## Process

### Step 1: Gather Inputs

Ask the user for:
1. **Your product info** — name, key features, pricing, differentiators
2. **Competitor data** — for at least 2 competitors, provide for each:
   - Name and URL
   - Key features
   - Pricing (model, tiers, price points)
   - Target audience
   - Positioning (their headline/value prop)
   - Strengths and weaknesses
   - Social proof signals (customer count, notable logos, review scores)
3. **Custom axes for positioning map** (optional) — default: market presence vs. product breadth

If the user has previously run competitor-site-analysis or competitor-content-analysis, they can reference those outputs.

### Step 2: Feature Comparison Matrix

Build a side-by-side feature comparison across all competitors and the user's product:

| Feature / Capability | Your Product | Competitor A | Competitor B | Competitor C |
|---------------------|-------------|-------------|-------------|-------------|
| [feature 1] | [status] | [status] | [status] | [status] |
| [feature 2] | [status] | [status] | [status] | [status] |

**Status values:** Full / Partial / Missing / Unknown

Include:
- Core features that define the category (everyone should have these)
- Differentiating features (only some competitors have)
- Your unique features (only you have — highlight these)
- Features competitors have that you don't (gaps to assess)

Sort rows by strategic importance, not alphabetically.

### Step 3: Pricing Comparison

Build a pricing comparison table:

| Dimension | Your Product | Competitor A | Competitor B | Competitor C |
|-----------|-------------|-------------|-------------|-------------|
| **Model** | | | | |
| **Free tier** | | | | |
| **Entry price** | | | | |
| **Mid-tier price** | | | | |
| **Enterprise** | | | | |
| **Value metric** | | | | |
| **Annual discount** | | | | |
| **Trial** | | | | |
| **Key upgrade trigger** | | | | |

**Pricing signals to flag:**
- Where you're significantly cheaper or more expensive than the market
- Competitors using per-seat pricing where value doesn't scale with headcount (vulnerability)
- Competitors with no free tier in a PLG market (acquisition barrier)
- Mismatches between pricing model and GTM motion

### Step 4: Positioning Map

Plot all competitors + your product on a 2x2 positioning map.

**Default axes:** Market Presence (low → high) vs. Product Breadth (focused → broad)

Score each company 1-10 on both axes:
- **Market presence** — traffic volume, review count, brand recognition signals, funding stage
- **Product breadth** — number of features, integrations, use cases served

**Alternative axis options** (offer to the user):
- Customer satisfaction (from review scores) vs. Market share (from traffic)
- Price level (low → high) vs. Feature depth (basic → advanced)
- PLG friendliness (self-serve → sales-required) vs. Enterprise readiness (SMB → enterprise)

Present as a labeled quadrant:

```
                    High Market Presence
                          |
         Established      |      Market Leaders
         Niche Players    |
    ----------------------+----------------------
                          |
         Emerging         |      Growing
         Focused          |      Contenders
                          |
                    Low Market Presence

    Focused ←————— Product Breadth ——————→ Broad
```

Place each competitor and your product in the appropriate quadrant. **Identify the gap:** Where is there open space on the map? That's potential positioning territory.

### Step 5: Aggregate SWOT

Synthesize across all competitors into a landscape-level view:

**Strengths across competitors** — what does the market generally do well? These are table stakes you must match.

**Common weaknesses** — what do multiple competitors struggle with? These are opportunities.

**Industry opportunities** — macro trends, technology shifts, or market gaps that no competitor has captured yet.

**Industry threats** — forces that affect everyone in this space (regulation, new entrants, platform risk, commoditization).

### Step 6: Moat Landscape

Summarize the moat picture across all competitors:

| Moat | Competitor A | Competitor B | Competitor C | You |
|------|-------------|-------------|-------------|-----|
| Network effects | | | | |
| Switching costs | | | | |
| Scale economies | | | | |
| Brand recognition | | | | |
| Regulatory / IP | | | | |
| Distribution | | | | |
| Data advantage | | | | |

**Key insights:**
- Moats that NO competitor has built = opportunity to build first-mover defensibility
- Moats that ALL competitors have = table stakes, not differentiators
- Your unique moats = lean into these in positioning

### Step 7: Content Comparison (if data available)

If competitor data includes content strategy info, compare content approaches:

| Content Type | Competitor A | Competitor B | Competitor C | You |
|---|---|---|---|---|
| Blog | | | | |
| Comparison pages | | | | |
| Guides / pillars | | | | |
| Glossary / programmatic | | | | |
| Templates / tools | | | | |
| Gated content | | | | |

If no content analysis data exists, skip this section and note it.

### Step 8: Strategic Recommendations

Synthesize everything into actionable recommendations:

**Where you win** — your clearest competitive advantages based on feature gaps, pricing position, moat differences, and competitor weaknesses. Be specific.

**Where you're vulnerable** — honest assessment of where competitors are ahead. What would you need to invest in to close the gap?

**Market gaps** — opportunities no one is serving well, informed by:
- Empty space on the positioning map
- Features no competitor offers
- Audience segments being ignored
- Pricing models no one has tried

**Positioning recommendation** — based on the full landscape, where should you position? What's your angle? What should you NOT compete on?

**Messaging landmines** — claims competitors make that you should avoid competing on directly (because they're stronger there) or because they're becoming commoditized.

## Output Format

```
# Competitive Landscape: [Product Name]

**Date:** [current date]
**Competitors:** [list]

## Feature Comparison
[matrix from Step 2]

## Pricing Comparison
[table from Step 3]

## Positioning Map
[quadrant from Step 4]

## Aggregate SWOT
[landscape-level SWOT from Step 5]

## Moat Landscape
[moat comparison from Step 6]

## Content Comparison
[content type coverage from Step 7, if available]

## Strategic Recommendations

### Where You Win
[from Step 8]

### Where You're Vulnerable
[from Step 8]

### Market Gaps
[from Step 8]

### Positioning Recommendation
[from Step 8]

### Messaging Landmines
[from Step 8]
```

## Rules

- Need at least 2 competitors for comparison. A landscape analysis with one competitor is just a profile.
- Never invent data — if information is missing for a competitor, note "data not available."
- Never present a positioning map without explaining why you chose the axes.
- Never make strategic recommendations without citing evidence from the data.
- If competitor data has inconsistent depth (one has full pricing, another doesn't), flag that comparison will be uneven.
- If the market appears highly fragmented (5+ direct competitors with no clear leader), note this.
- Be honest if the user's product appears to be in a weak position on the map — suggest what to improve.
- The positioning map is most valuable when you customize the axes to match your strategic question.
