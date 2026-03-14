---
name: ad-campaign-analyzer
description: "Grade running ads as Red (stop) / Yellow (hold) / Green (scale) with creative fatigue detection, LTV:CAC analysis, and scaling recommendations."
compatibility: "No special requirements. Accepts campaign data as CSV, table, or pasted text."
metadata:
  author: superamped
  version: "1.0"
  website: "https://superamped.com"
---

# Ad Campaign Analyzer

## Usage

Use when reviewing a running campaign to decide what to kill, keep, or scale. Works for daily 15-minute ad reviews, weekly creative refresh planning, and monthly performance trend reviews.

## Process

### Step 1: Gather Inputs

Ask the user for:
1. **Campaign data** — one of:
   - CSV or table with columns: ad/ad set name, impressions, clicks, conversions, spend, CPA
   - Pasted text from ads manager
   - Structured list of metrics per ad
2. **Target CPA** — the maximum they're willing to pay per acquisition
3. **AOV (Average Order Value)** — what they earn per conversion on the front end
4. **Product/pricing info** — what they sell, offer details, known conversion benchmarks
5. **Daily budget per ad set** (optional) — for scaling calculations
6. **Days running** (optional) — for statistical significance judgment
7. **Historical data** (optional) — from previous review for trend comparison

### Step 2: Parse Campaign Data

Normalize the input into a consistent table structure:

| Ad / Ad Set | Impressions | Clicks | CTR | Conversions | Spend | CPA | Days Running |
|-------------|------------|--------|-----|-------------|-------|-----|-------------|

Calculate any missing derived metrics:
- **CTR** = clicks / impressions × 100
- **CPA** = spend / conversions (∞ if 0 conversions)
- **Conversion rate** = conversions / clicks × 100

### Step 3: Grade Each Ad — Red / Yellow / Green

#### 🔴 RED = STOP

Kill this ad. It's burning money.

Criteria (any one triggers Red):
- Spent **1.5–2x target CPA** with zero conversions
- CPA is **2x+ target CPA** with statistically significant spend
- Consistently worsening metrics over multiple days with no improvement signs
- CTR below 0.5% after 1,000+ impressions (the creative isn't connecting)

**Action:** Turn off immediately. Redirect budget to greens.

#### 🟡 YELLOW = LEAVE ALONE

Don't touch it. It needs more data or is borderline.

Criteria:
- CPA is close to target (within 0.5–1.5x) but not enough data to be confident
- Fewer than 1,000 impressions or fewer than 20 clicks — too early to judge
- Spend is under 1x target CPA — hasn't had a fair chance yet
- Metrics are mixed (good CTR but low conversion, or vice versa)

**Action:** Do nothing. Check again tomorrow. Resist the urge to tweak.

#### 🟢 GREEN = SCALE

This ad is working. Give it more budget.

Criteria:
- CPA is consistently **at or below target CPA**
- Has statistically significant data (generally 10+ conversions)
- Metrics are stable or improving over time
- CTR is healthy for the targeting type

**Action:** Scale using the **20% Rule** — increase daily budget by 20% every 48 hours.

### Step 4: Benchmark Comparison

Compare each ad's metrics against industry benchmarks:

**CTR Benchmarks (by targeting type):**
| Targeting | Expected CTR |
|-----------|-------------|
| Broad / run-of-network | 1–3% |
| Interest-based targeting | 2–4% |
| Lookalike / community-targeted | 3–5% |

**CPA Targets by Offer Price:**
| Offer Price Range | Expected CPA Range |
|-------------------|-------------------|
| $7–27 (low ticket) | $20–40 |
| $37–97 (mid ticket) | $40–120 |
| $97+ (high ticket) | Varies — must model LTV |

### Step 4b: Funnel Debugging — Find the Leak

Before changing creative, check whether the ad is actually the problem. Work from the surface inward:

1. **Creative** — Is the CTR acceptable? Low CTR = the ad isn't connecting. Test new hooks, visuals, or headlines.
2. **Landing page** — CTR is fine but conversions are flat? The LP is the problem.
3. **Messaging** — LP structure looks okay but still no conversions? The fundamental message may not be resonating.
4. **Product and pricing** — Different angles all fail? The offer itself may be the issue.
5. **Market** — Everything above looks solid but the right people still aren't converting? The segment may be wrong.

**Work from #1 → #5 in order.** Most founders jump to #3 or #4 when the actual problem is #1 or #2.

**Data thresholds — don't debug on noise:**
- **< 1,000 impressions per ad variant:** Too early to judge CTR.
- **< 100 LP visitors:** Too early to judge landing page conversion.
- **< 10 conversions on a green ad:** Scale cautiously — the trend may not hold.

### Step 5: Flag Creative Fatigue

Check for fatigue signals across the data:

- **Declining CTR** over time (even if still "okay" in absolute terms)
- **Rising CPA** despite no changes to targeting or budget
- **Dropping conversion rate** with stable traffic quality
- **Frequency above 3** (same people seeing the ad too many times)

If fatigue is detected, flag which ads are affected and recommend:
- New creative variation (different angle, format, or style)
- Audience refresh (new targeting or exclusions)
- Copy refresh (same visual, new headline)

### Step 6: Profitability Check

The North Star: **Is AOV > CPA?**

For each green ad, calculate:
- **Profit per conversion** = AOV − CPA
- **ROAS** = AOV / CPA (must be > 1.0 to be profitable)
- **Break-even CPA** = AOV (you make $0 at this point)
- **Margin at current CPA** = (AOV − CPA) / AOV × 100

### Step 6b: LTV:CAC Health Check

If LTV data is available, assess the pricing-level health of the campaign:

**LTV:CAC Ratio Benchmarks:**

| Pricing Function | Average LTV:CAC |
|-----------------|----------------|
| No pricing function | 1.68 |
| Yearly pricing review | 3.23 |
| Continuous optimization | 11.09 |

**Interpret the ratio:**
- **< 1:1** — Losing money on every customer. Stop spending until unit economics are fixed.
- **1:1 – 3:1** — Marginal. Campaigns may appear profitable on front-end ROAS but are destroying value over time.
- **3:1 – 5:1** — Healthy. Scale greens confidently.
- **> 5:1** — Excellent. May be under-investing in acquisition.

**Monetization impact reminder:** A 1% improvement in monetization yields a 12.7% increase in bottom-line revenue — roughly 4x the impact of acquisition and 2x the impact of retention. If LTV:CAC is weak, the fix may be pricing, not ads.

### Step 6c: Attribution Notes

When analyzing multi-channel campaigns, note attribution limitations:
- Single-channel campaigns: last-click is sufficient.
- Multi-channel campaigns: flag that attribution is approximate.
- Don't over-complicate analytics. The goal is action (red/yellow/green), not perfect measurement.

### Step 7: Generate Scaling Recommendations

For each green ad, provide specific scaling numbers:

**The 20% Rule:**
- Current daily budget → recommended new budget (current × 1.2)
- When to apply: 48 hours after last budget change
- Next check-in date

For the overall campaign:
- Total daily spend recommendation
- Budget reallocation from reds to greens
- When to add new creatives to the mix

## Output Format

```
# Campaign Analysis

**Date:** [current date]
**Campaign:** [campaign name or description]
**Period:** [date range of data]
**Target CPA:** $[amount]
**AOV:** $[amount]

---

## Traffic Light Summary

| Grade | Count | % of Spend |
|-------|-------|-----------|
| 🔴 Red (Stop) | X | X% |
| 🟡 Yellow (Wait) | X | X% |
| 🟢 Green (Scale) | X | X% |

**Campaign Health:** [Healthy / Needs Attention / Critical] — [one sentence summary]

---

## Ad-Level Grades

| Ad / Ad Set | Grade | Spend | CPA | Target CPA | CTR | Conv. | Action |
|-------------|-------|-------|-----|-----------|-----|-------|--------|
| [name] | 🔴 | $X | $X | $X | X% | X | Stop — [reason] |
| [name] | 🟡 | $X | $X | $X | X% | X | Wait — [reason] |
| [name] | 🟢 | $X | $X | $X | X% | X | Scale to $X/day |

---

## Benchmark Comparison

| Metric | Your Average | Benchmark | Status |
|--------|-------------|-----------|--------|
| CTR | X% | X–X% | ✅ On track / ⚠️ Below / 🔥 Above |
| Conversion Rate | X% | X–X% | ✅ / ⚠️ / 🔥 |
| CPA | $X | $X–X | ✅ / ⚠️ / 🔥 |

---

## Creative Fatigue Alerts

[List any ads showing fatigue signals, or "No fatigue signals detected."]

---

## Profitability

| Ad / Ad Set | CPA | AOV | Profit/Conv. | ROAS | Margin |
|-------------|-----|-----|-------------|------|--------|
| [name] | $X | $X | $X | X.Xx | X% |

**Overall ROAS:** X.Xx
**Overall Profit/Conversion:** $X

---

## Action Items

### Immediate (Today)
- [ ] Stop: [list red ads]
- [ ] Scale: [list green ads with specific new budgets]

### This Week
- [ ] [Creative refresh, new tests, etc.]

### Review Cadence
- Next daily check: [tomorrow]
- Next weekly review: [date]
- Next monthly review: [date]

---

## Scaling Plan

| Ad | Current Budget | New Budget | Apply On | Next Increase |
|----|---------------|-----------|----------|---------------|
| [name] | $X/day | $X/day | [date] | $X/day on [date] |

**Total daily spend:** $X → $X (recommended)
```

## Rules

- The grading method is deliberately binary. Red means stop, not "let's give it one more day." Kill losers fast and feed winners.
- Yellow is the discipline zone. Don't "optimize" yellows. Either there's enough data to judge or there isn't.
- The 20% rule exists because ad platforms optimize delivery around your budget. Jumping budgets overnight resets the algorithm's learning.
- CPA is the North Star, not CTR. A high-CTR ad that doesn't convert is worse than a low-CTR ad with great CPA.
- These benchmarks are starting points. After 2-4 weeks, your own data becomes the benchmark.
- If everything is red, the problem isn't the ads — it's the offer or the funnel.
- Creative fatigue is inevitable. Plan for it. Have your next batch of creatives ready before the current ones die.
