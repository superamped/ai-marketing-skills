# AI Marketing Skills

This repo contains standalone marketing skills in the `skills/` directory. Each skill is a self-contained markdown prompt with YAML frontmatter.

## Available Skills

### Ads
- `skills/ads/ad-angles/SKILL.md` — Brainstorm ad concepts using 5 messaging angles, formats, and visual styles
- `skills/ads/ad-campaign-analyzer/SKILL.md` — Red/Yellow/Green campaign grading with creative fatigue detection and scaling recommendations
- `skills/ads/ad-creative/SKILL.md` — Render ad concepts as HTML with 5 template styles, optionally screenshot via Playwright MCP

### Content
- `skills/content/content-strategy/SKILL.md` — Plan content pillars, topic clusters, editorial calendar, and keyword mapping by buyer stage
- `skills/content/social-post-writer/SKILL.md` — Generate social posts from a topic using 9 proven templates with platform adaptation
- `skills/content/content-repurposer/SKILL.md` — Turn long-form content into a week of short-form social posts via Hub & Spoke method

### Conversion
- `skills/conversion/conversion-audit/SKILL.md` — 53-point conversion audit covering customer focus, narrative arc, copy, design, CTAs, and proof

### Reddit
- `skills/reddit/reply-writer/SKILL.md` — Draft native Reddit replies in 3 rotating formats with subreddit tone calibration

### Research
- `skills/research/channel-discovery/SKILL.md` — Map marketing channels for a target audience, score on 5 criteria, recommend top 3
- `skills/research/community-discovery/SKILL.md` — Discover 100+ online communities across Reddit, Slack, Discord, Facebook, LinkedIn, and forums
- `skills/research/competitor-content-analysis/SKILL.md` — Analyze a competitor's content engine — inventory, SEO plays, comparison pages, gaps
- `skills/research/competitor-discovery/SKILL.md` — Search the web for competitors, produce a ranked list of direct/adjacent/tangential competitors
- `skills/research/competitor-keyword-analysis/SKILL.md` — Map a competitor's organic search presence via Keywords Everywhere MCP
- `skills/research/competitor-landscape/SKILL.md` — Cross-competitor comparison — feature matrix, positioning map, SWOT, strategic recommendations
- `skills/research/competitor-site-analysis/SKILL.md` — Extract structured data from a competitor's website across 5 dimensions
- `skills/research/influencer-discovery/SKILL.md` — Discover 100+ influencers across YouTube, X/Twitter, blogs, newsletters, and podcasts
- `skills/research/keyword-research/SKILL.md` — Expand a seed keyword into clustered keyword universe via Keywords Everywhere MCP

### Search
- `skills/search/search-page-audit/SKILL.md` — 38-point SEO + AI optimization audit for any URL

## How to Use

**Claude Code plugin users:** Skills are auto-discovered — just ask Claude to run any skill by name.

**Other tools:** When a user asks to run an audit (or any skill), read the corresponding `SKILL.md` file and follow its instructions exactly. Pass the user's input (e.g. a URL) as the argument.

## Conventions

- Skills live in `skills/<category>/<skill-name>/SKILL.md`
- Each skill defines its own process, output format, and rules
- Do not improvise outside what the skill specifies — follow the SKILL.md

## Integrations

Some skills use MCP servers. See `integrations/` for setup guides.
- **Keywords Everywhere** — keyword data, traffic metrics, backlinks
- **Playwright** — browser automation, screenshots
