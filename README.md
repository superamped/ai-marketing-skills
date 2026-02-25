# AI Marketing Skills

Open-source AI marketing skills for AI coding agents. Create strategy, research competitors, do SEO, write copy and content, analyze campaigns, and more — all from your terminal.

Works with [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [Codex](https://github.com/openai/codex), [OpenCode](https://opencode.ai), [Cursor](https://cursor.com), and any tool that reads `AGENTS.md`.

## What are skills?

Skills are standalone markdown files that give AI coding tools specialised marketing capabilities. Each skill is a single-purpose prompt that produces one output. Drop them into your project and run them.

## Skills

### Ads

| Skill | What it does |
|-------|-------------|
| **Ad Angles** | Brainstorm ad concepts by combining 5 messaging angles (Problem, Solution, Comparison, Proof, Curiosity), formats, and visual styles |
| **Ad Campaign Analyzer** | Grade running ads as Red (stop) / Yellow (hold) / Green (scale) with creative fatigue detection and scaling recommendations |
| **Ad Creative** | Render ad concepts as HTML with 5 template styles (cookie-cutter, ugly, meme, branded, native), optionally screenshot via Playwright |

### Content

| Skill | What it does |
|-------|-------------|
| **Content Strategy** | Plan content pillars, topic clusters, editorial calendar, and keyword research by buyer stage |
| **Social Post Writer** | Generate social posts from a topic using 9 proven templates (Story, Observation, Contrarian, Listicle, etc.) with platform adaptation |
| **Content Repurposer** | Turn long-form content into a week of short-form social posts using Hub & Spoke method |

### Conversion

| Skill | What it does |
|-------|-------------|
| **Conversion Audit** | 53-point conversion audit covering customer focus, narrative arc (Pain-Dream-Fix), copy quality, design, CTAs, and proof |

### Reddit

| Skill | What it does |
|-------|-------------|
| **Reply Writer** | Draft native Reddit replies in 3 rotating formats with subreddit tone calibration |

### Research

| Skill | What it does |
|-------|-------------|
| **Channel Discovery** | Map marketing channels for a target audience, score on 5 criteria, recommend top 3 to prioritize |
| **Community Discovery** | Discover 100+ online communities across Reddit, Slack, Discord, Facebook, LinkedIn, and forums — scored by Signal-to-Noise |
| **Competitor Content Analysis** | Analyze a competitor's content engine — inventory, SEO plays, comparison pages, gated content, and gap analysis |
| **Competitor Discovery** | Search the web for competitors, produce a ranked list of direct, adjacent, and tangential competitors |
| **Competitor Keyword Analysis** | Map a competitor's organic search presence — top keywords, traffic metrics, content theme clusters |
| **Competitor Landscape** | Cross-competitor comparison — feature matrix, pricing, 2x2 positioning map, aggregate SWOT, and strategic recommendations |
| **Competitor Site Analysis** | Extract structured data from a competitor's website — overview, positioning, pricing, social proof, hiring signals |
| **Influencer Discovery** | Discover 100+ influencers across YouTube, X/Twitter, blogs, newsletters, podcasts, and Instagram — scored by Audience Overlap |
| **Keyword Research** | Expand a seed keyword into a clustered keyword universe — grouped by search intent, scored, and prioritized |

### Search

| Skill | What it does |
|-------|-------------|
| **Search Page Audit** | 38-point SEO + AI optimization audit on any URL — covers SEO fundamentals, content structure, AI/GEO readiness, and E-E-A-T authority signals |

## Integrations

Some skills use MCP (Model Context Protocol) servers for live data. These are optional — skills degrade gracefully without them.

| Integration | What it provides | Required by | Optional for |
|-------------|-----------------|-------------|--------------|
| [Keywords Everywhere](integrations/keywords-everywhere.md) | Keyword volumes, traffic metrics, backlink data | Keyword Research, Competitor Keyword Analysis | Competitor Content Analysis |
| [Playwright](integrations/playwright.md) | Browser automation for screenshots and JS-rendered pages | — | Ad Creative, Competitor Content Analysis, Competitor Site Analysis |

A template [`.mcp.json`](.mcp.json) is included — replace `YOUR_API_KEY` with your Keywords Everywhere API key.

## Getting Started

1. Clone this repo
2. Copy the `skills/` folder into your project
3. Run the skill using your AI coding tool

**Claude Code** — Copy `skills/` to `.claude/skills/` in your project, then ask Claude to run a skill

**Codex** — Copy `skills/` to `.agents/skills/` in your project, then ask Codex to run a skill

**OpenCode** — Copy `skills/` to `.agents/skills/` or `.claude/skills/` in your project, then ask OpenCode to run a skill

**Cursor / Other** — Reference the skill in your prompt or copy `AGENTS.md` to your project root

## Community

Join the [Growth Engineering Community](https://superamped.com/growth-engineering-community) — a community for marketers and founders engineering growth with AI.

## License

MIT. See [LICENSE](LICENSE) for details.
