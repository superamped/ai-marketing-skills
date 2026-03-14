---
name: reply-writer
description: "Draft native Reddit replies in 3 rotating formats with subreddit tone calibration."
compatibility: "No special requirements."
metadata:
  author: superamped
  version: "1.0"
  website: "https://superamped.com"
---

# Reddit Reply Writer

## Usage

Use when writing a reply to a Reddit thread, crafting authentic engagement, or preparing replies for community participation. Works for any subreddit.

## Process

### Step 1: Gather Inputs

Ask the user for:
1. **Product/brand context** — what you sell, who it's for, what tone to use (so the reply can subtly align voice without being promotional)
2. **Subreddit name** — which community the reply is for
3. **Thread title** — exact title
4. **Original post** — full text of the OP
5. **Top existing replies** — at least the top 3 replies
6. **Tone guidance** (optional) — "more casual," "technical audience," etc.

### Step 2: Thread Analysis

- Identify what the OP is actually confused about (not what they asked)
- Decide what is missing or unclear in existing replies

### Step 3: Write the Reply

Write a reply that:
- Feels human and experience-based
- Explains the reasoning or system behind the answer
- Does not sell, promote, or link
- Sounds like it belongs in this exact subreddit
- Uses natural formatting (short paragraphs, bullets if native)
- Prioritizes clarity over completeness

### Step 4: Apply Format Rotation

Auto-rotate between three formats (don't repeat consecutively in a session):

#### Format 1: "Here's What Actually Works"

**When to use:** Actionable question with a clear answer. OP needs steps, not debate.

**Structure:**
- Short framing (1-2 sentences)
- Step-by-step logic with reasoning
- No authority flexing or credentials
- End with what happens next, not a CTA

**Good Example:**
> This breaks because you're rebuilding the entire tree on each re-render. You want to memoize the expensive computation. The way this typically works: calculate once, pass down to children, children only recalculate when that specific value changes (not the parent). React doesn't know your data structure, so you have to tell it explicitly via useMemo or dependency arrays.

**Bad Example:**
> You should use React.memo! Check out this blog post I wrote about optimization techniques. It's super important to understand memoization, and our product handles this automatically. Learn more here [link].

#### Format 2: "Most People Miss This Part"

**When to use:** OP's approach is on the right track but incomplete. Thread has misconceptions.

**Structure:**
- Acknowledge what they got right
- Name the gap specifically
- Explain why it matters (the consequence)
- Add the missing nuance without being condescending

**Good Example:**
> You're right about needing backups, but most people miss the restore part. Having backups is half the equation — you need to test that restore process regularly. I've seen teams with years of backups that couldn't actually recover their data because they never validated the restore.

#### Format 3: "I've Seen This Go Wrong When..."

**When to use:** OP is asking about a pattern that has failure modes. Experience-based framing builds trust.

**Structure:**
- Real scenario where this breaks
- The cause (usually not obvious)
- What actually happens (the failure)
- How people typically fix it
- One thing to watch for going forward

**Good Example:**
> I've seen this pattern fail when you have multiple services writing to the same cache. Service A invalidates the cache, Service B hasn't noticed yet and writes stale data back. The fix is straightforward — make invalidation atomic or use versioning. I usually recommend versioning because it's easier to reason about.

### Step 5: Calibrate Tone by Subreddit Type

**Technical Subs** (r/rust, r/golang, r/django):
- Assume audience knows fundamentals
- Explain tradeoffs and system reasoning
- Use precise language
- Tone: Peer-to-peer, not tutorial

**Casual Subs** (r/learnprogramming, r/fitness, r/cooking):
- Explain why basics matter first
- Use concrete examples over abstractions
- Shorter sentences, more accessible vocabulary
- Tone: Friendly expert, not gatekeeping

**Professional Subs** (r/business, r/accounting, r/law):
- Lead with context (market, regulation, scale)
- Acknowledge complexity without being defensive
- Tone: Collaborative problem-solver, not showboating

## Output Format

The skill returns:

1. **Drafted Reply** (markdown-formatted, ready to paste)
2. **Reply Strategy Note** (2-3 sentences explaining which format was chosen and why)
3. **Tone Confidence** (Did this match the subreddit culture? High/Medium/Low)

## Rules

- No marketing language or salesy framing.
- No calls to action.
- No links unless they already exist in-thread.
- Write as if you are helping one person, not an audience.
- No repeated phrasing across multiple replies in a session.
- No brand mentions unless directly asked.
- No posting in hostile or troll-baiting threads.
- No replying to moderation bait.
- Native replies explain the *system* (why something works, not just that it works).
- Every sentence should add information — no marketing padding.
- Skip the thread if: subreddit is known for trolling, thread title contains loaded language, top replies are mostly insults, your reply would require a link as the core answer, or topic involves illegal activity.
- If guardrails fail, return "Thread skipped: [reason]" instead of drafting.
