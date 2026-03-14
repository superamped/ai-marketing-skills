---
name: content-repurposer
description: "Take long-form content and produce a week of short-form social posts using Hub & Spoke method with 6 templates."
compatibility: "No special requirements."
metadata:
  author: superamped
  version: "1.0"
  website: "https://superamped.com"
---

# Content Repurposer

## Usage

Use when you've just published a newsletter or blog post and need social content to promote and extend it, repurposing a podcast episode or YouTube video transcript, or getting a full week of social posts from one piece of long-form content.

## Process

### Step 1: Gather Inputs

Ask the user for:
1. **Long-form content** — the hub piece. Can be:
   - A newsletter issue (pasted or file path)
   - A blog post (pasted, file path, or URL to fetch)
   - A podcast/video transcript
   - A research doc or set of notes
2. **Target platform** (optional) — LinkedIn, Twitter/X, or both (default: both)
3. **Voice/tone** — what the brand voice sounds like (casual, professional, witty, etc.)
4. **Target audience** — who follows them on social
5. **Newsletter/content link** (optional) — URL to link back to in CTA posts
6. **Subscriber/reader count** (optional) — for social proof in CTA posts
7. **Number of spokes** (optional) — default: 5 (one per template)
8. **Constraints** (optional) — things to avoid, compliance requirements

### Step 2: Extract the Core from the Hub

Read the long-form content and extract:
- **Main thesis** — the one big idea in one sentence
- **Key takeaways** — 3-7 specific, actionable points
- **Supporting stories** — personal anecdotes, examples, or case studies
- **Data/proof points** — any numbers, stats, or results mentioned
- **Contrarian or surprising elements** — anything that challenges conventional thinking
- **Tools/resources mentioned** — any recommendations, links, or references

Present this extraction to the user as a summary before generating spokes. This ensures nothing important is missed.

### Step 3: Generate Spoke Posts

Create one post for each of the spoke templates:

---

#### Template 1: Story

Tell a narrative that leads to the hub's key insight.

**Structure:**
1. **Pain/Attention** — Open with a personal story or relatable problem
2. **Agitate** — Show how things got worse
3. **Intrigue** — Introduce a turning point
4. **Positive Future** — Show the benefits
5. **Solution** — Bring clarity with a specific action or resource

**Rules:**
- First person. This is a story, not a lecture.
- Short sentences. One idea per line.
- The opening line must hook.

---

#### Template 2: Observation

Share a pattern or insight related to the hub topic.

**Structure:**
1. **Observation statement** — One clear, specific thing you noticed
2. **Evidence** — 2-4 specifics that support the observation
3. **Closer** — A short, punchy takeaway line

---

#### Template 3: Contrarian Take

Challenge a commonly held belief from the hub content.

**Structure:**
1. **Hot take** — State the contrarian position clearly
2. **Supporting points** — 3-5 reasons this take is valid
3. **Reframe** — End with a new way to think about it

---

#### Template 4: Listicle

Curate tools, resources, tips, or takeaways from the hub content.

**Structure:**
1. **Framing line** — "X [things] every [audience] should know about:"
2. **Numbered list** — Each item with a name + short description
3. **Optional closer** — A recommendation or CTA

---

#### Template 5: Meme

Turn the hub's key insight into a meme-format post.

**Structure:**
1. **Choose a meme format** — Match the hub's core tension to a template
2. **Write the caption** — The meme does the heavy lifting. Caption adds context.

**Rules:**
- Standalone. Understandable without reading the hub content.
- Use the audience's in-group language.
- Don't force it. If no natural meme angle, skip and double up on another template.

---

#### Template 6: Past vs. Present

Show how the hub topic has evolved — then vs. now.

**Structure:**
1. **Then** — What things looked like before. 3-5 bullet points.
2. **Now** — What things look like after. 3-5 bullet points (matching structure).
3. **Lesson** — One line that captures the shift.

---

### Step 4: Generate CTA Posts

Create 2 CTA posts to drive traffic back to the hub content:

#### Pre-Hub CTA (publish the day before or morning of)

```
{Attention-grabbing opener related to the topic}
{1-2 sentences of context — why this matters}

Here's what I'll cover:
1. {Takeaway 1}
2. {Takeaway 2}
3. {Takeaway 3}

Tomorrow, I'll share this with [XX,XXX] subscribers.

If you want in: {link}
```

#### Post-Hub CTA (publish the day after)

```
{Problem question or pain point}
{1-2 sentences on why most people get this wrong}

Yesterday, [XX,XXX] people got my breakdown on [topic].

Miss it? Grab it here ↓
{link}
```

**CTA rules:**
- If the user provides a subscriber count, use it for social proof.
- If no count is available, skip that line — don't make one up.
- The link should be the last element.

### Step 5: Tag Content Psychology

Tag each post with its primary emotional trigger:

| Trigger | What it does | Post types that map |
|---------|-------------|-------------------|
| **Entertains** | Generates awareness | Story, Past vs. Present |
| **Teaches** | Builds trust | Listicle, Observation |
| **Empathizes** | Deepens emotional connection | Story (pain-focused), Contrarian |
| **Makes me think** | Challenges preconceptions | Contrarian Take, Observation |

Flag if the batch is unbalanced. A good week has at least 2 different triggers represented.

### Step 6: Platform Adaptation

**LinkedIn:**
- First line is everything — shows above the "see more" fold
- Line breaks generously
- 1,300 characters is the sweet spot
- End with a question or conversation starter

**Twitter/X:**
- 280 characters for single tweets — ruthlessly edit
- Threads: first tweet stands alone
- Listicles and observations compress well into single tweets
- Stories and contrarian takes work better as threads

### Step 7: Build Publishing Schedule

| Day | Post Type | Trigger |
|-----|----------|---------|
| Day 1 (pre-hub) | Pre-Hub CTA | — |
| Day 2 (hub day) | Hub publishes | — |
| Day 3 (post-hub) | Post-Hub CTA | — |
| Day 4 | Story | Entertains / Empathizes |
| Day 5 | Observation | Teaches |
| Day 6 | Contrarian Take | Makes me think |
| Day 7 | Listicle or Past vs. Present | Teaches / Entertains |

## Output Format

```
# Content Repurposed: [Hub Title]

**Date:** [current date]
**Hub:** [title or description of the long-form piece]
**Platform(s):** [LinkedIn / Twitter / Both]
**Posts Generated:** [count]

---

## Hub Summary

**Main thesis:** [one sentence]

**Key takeaways:**
1. [takeaway]
2. [takeaway]
3. [takeaway]

**Stories/examples found:** [brief list]
**Data points found:** [brief list]
**Contrarian angles found:** [brief list]

---

## Spoke Posts

### 1. Story
**Trigger:** [Entertains / Empathizes]

[Full post text]

---

### 2. Observation
**Trigger:** [Teaches / Makes me think]

[Full post text]

---

### 3. Contrarian Take
**Trigger:** [Makes me think]

[Full post text]

---

### 4. Listicle
**Trigger:** [Teaches]

[Full post text]

---

### 5. Past vs. Present
**Trigger:** [Entertains]

[Full post text]

---

## CTA Posts

### Pre-Hub CTA
[Full post text]

### Post-Hub CTA
[Full post text]

---

## Publishing Schedule

| Day | Post | Platform | Trigger |
|-----|------|----------|---------|
| [day] | [post type] | [platform] | [trigger] |

---

## Trigger Balance

| Trigger | Count |
|---------|-------|
| Entertains | X |
| Teaches | X |
| Empathizes | X |
| Makes me think | X |

**Balance:** [Balanced / Leans toward X — consider adding Y]
```

## Rules

- The hub piece does the heavy thinking. Spokes repackage, they don't rehash. Each spoke should feel like a standalone post, not a summary.
- Never copy-paste a section of the hub and post it as a spoke. Rewrite for the platform and format.
- The Story template is the hardest but typically gets the highest engagement. It needs a real narrative arc.
- Contrarian takes only work if the original content actually has a contrarian angle. Don't manufacture one.
- CTA posts work best when they give a taste of value before asking for the click.
- If the hub is thin on material (under 500 words or only 1-2 takeaways), generate 3 spokes instead of 5 and flag that the hub could be expanded.

