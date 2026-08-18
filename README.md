# Marketing Skills for AI Agents

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-18-6f42c1)](https://agentskills.io)
[![Validate](https://github.com/superamped/ai-marketing-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/superamped/ai-marketing-skills/actions/workflows/validate.yml)
[![GitHub release](https://img.shields.io/github/v/release/superamped/ai-marketing-skills)](https://github.com/superamped/ai-marketing-skills/releases)
[![MIT License](https://img.shields.io/github/license/superamped/ai-marketing-skills)](LICENSE)

18 open-source **AI marketing skills** for practical work with Claude Code, Codex, Cursor, OpenCode, and other compatible AI agents. Research markets, audit SEO, analyze campaigns, improve conversion, and create content from your terminal.

```bash
npx skills add superamped/ai-marketing-skills
```

> These are skills, not autonomous agents. They give your existing AI agent focused instructions, workflows, quality checks, and output standards for specific marketing jobs.

## What you can do

| Ask your agent | Typical output | Skill |
|---|---|---|
| “Find and classify competitors for our B2B SaaS product.” | Ranked direct, adjacent, and tangential competitor set with evidence | [Competitor Discovery](skills/research/competitor-discovery/SKILL.md) |
| “Audit this landing page for conversion problems.” | Scored 53-point audit with prioritized fixes | [Conversion Audit](skills/conversion/conversion-audit/SKILL.md) |
| “Build a keyword map for customer onboarding software.” | Intent-clustered keyword universe with volume-based priorities when Keywords Everywhere is connected | [Keyword Research](skills/research/keyword-research/SKILL.md) |
| “Review this campaign export and tell me what to stop, hold, or scale.” | Red/Yellow/Green campaign analysis with fatigue and scaling recommendations | [Ad Campaign Analyzer](skills/ads/ad-campaign-analyzer/SKILL.md) |
| “Audit this article for traditional SEO and AI search readiness.” | 38-point SEO, GEO, and E-E-A-T report | [Search Page Audit](skills/search/search-page-audit/SKILL.md) |

## What are Agent Skills?

[Agent Skills](https://agentskills.io) are portable capability packages that an AI agent can discover and load when relevant. Each skill lives in its own directory and contains a `SKILL.md` file with YAML metadata and procedural instructions. Skills can also include scripts, references, and other resources.

Because the files are plain text, you can inspect, adapt, and version the exact marketing process your agent follows.

## Skills

### Ads

| Skill | What it does |
|---|---|
| [**Ad Angles**](skills/ads/ad-angles/SKILL.md) | Brainstorms concepts across problem, solution, comparison, proof, and curiosity angles |
| [**Ad Campaign Analyzer**](skills/ads/ad-campaign-analyzer/SKILL.md) | Grades ads Red/Yellow/Green and recommends what to stop, hold, or scale |
| [**Ad Creative**](skills/ads/ad-creative/SKILL.md) | Renders ad concepts as HTML in five styles, with optional Playwright screenshots |

### Content

| Skill | What it does |
|---|---|
| [**Content Strategy**](skills/content/content-strategy/SKILL.md) | Plans pillars, topic clusters, buyer-stage keyword mapping, and an editorial calendar |
| [**Social Post Writer**](skills/content/social-post-writer/SKILL.md) | Produces platform-adapted posts using nine practical templates |
| [**Content Repurposer**](skills/content/content-repurposer/SKILL.md) | Turns one long-form source into a week of short-form content |

### Conversion

| Skill | What it does |
|---|---|
| [**Conversion Audit**](skills/conversion/conversion-audit/SKILL.md) | Runs a 53-point audit of customer focus, narrative, copy, design, CTAs, and proof |

### Reddit

| Skill | What it does |
|---|---|
| [**Reply Writer**](skills/reddit/reply-writer/SKILL.md) | Drafts native Reddit replies with subreddit tone calibration |

### Research

| Skill | What it does |
|---|---|
| [**Channel Discovery**](skills/research/channel-discovery/SKILL.md) | Scores possible acquisition channels and recommends the top three |
| [**Community Discovery**](skills/research/community-discovery/SKILL.md) | Finds and scores relevant communities across major platforms and independent forums |
| [**Competitor Content Analysis**](skills/research/competitor-content-analysis/SKILL.md) | Maps a competitor’s content engine, SEO plays, and gaps |
| [**Competitor Discovery**](skills/research/competitor-discovery/SKILL.md) | Produces a ranked set of direct, adjacent, and tangential competitors |
| [**Competitor Keyword Analysis**](skills/research/competitor-keyword-analysis/SKILL.md) | Maps ranking keywords, estimated traffic, and content themes |
| [**Competitor Landscape**](skills/research/competitor-landscape/SKILL.md) | Compares features, pricing, positioning, moats, and strategic opportunities |
| [**Competitor Site Analysis**](skills/research/competitor-site-analysis/SKILL.md) | Extracts positioning, pricing, proof, and hiring signals from a competitor website |
| [**Influencer Discovery**](skills/research/influencer-discovery/SKILL.md) | Finds and scores influencers across video, social, newsletters, blogs, and podcasts |
| [**Keyword Research**](skills/research/keyword-research/SKILL.md) | Expands, clusters, scores, and prioritizes a keyword universe |

### Search

| Skill | What it does |
|---|---|
| [**Search Page Audit**](skills/search/search-page-audit/SKILL.md) | Runs a 38-point SEO, AI-search/GEO, and E-E-A-T audit on a URL |

## Installation

### Agent Skills CLI

Use the open Agent Skills installer for supported agents:

```bash
npx skills add superamped/ai-marketing-skills
```

The installer lets you select skills and supported hosts. Commit installed skills to your own repository when you want your team and agents to share the same version.

### Claude Code plugin

```bash
/plugin marketplace add superamped/ai-marketing-skills
/plugin install ai-marketing-skills
```

The plugin identifier remains `ai-marketing-skills`.

### Manual installation

Clone the repository and copy the desired skill directories into the Agent Skills location used by your host:

```bash
git clone https://github.com/superamped/ai-marketing-skills.git
```

| Host | Typical project location | Method |
|---|---|---|
| Claude Code | Plugin installation above | Marketplace plugin |
| Codex and Agent Skills-compatible tools | `.agents/skills/` | Skills CLI or copy selected directories |
| OpenCode | `.agents/skills/` or `.claude/skills/` | Skills CLI or copy selected directories |
| Cursor and other tools | Host-specific skills directory | Skills CLI where supported; otherwise follow the host documentation |

Host behavior changes over time. The source packages follow the Agent Skills format; consult your host’s current documentation for discovery paths and invocation behavior.

## Integrations

Most skills work with ordinary agent capabilities and internet access. Some can use external services for live evidence.

| Integration | What it provides | Required by | Optional for |
|---|---|---|---|
| [Keywords Everywhere](integrations/keywords-everywhere.md) | Keyword volume, CPC, competition, ranking, traffic, and backlink estimates | Keyword Research; Competitor Keyword Analysis | Competitor Content Analysis |
| [Playwright](integrations/playwright.md) | Browser automation, rendered-page inspection, and screenshots | — | Ad Creative; Competitor Content Analysis; Competitor Site Analysis |

A secret-free [`.mcp.json`](.mcp.json) template is included. Supply the Keywords Everywhere key securely through the `KEYWORDS_EVERYWHERE_API_KEY` environment variable. Never commit the key.

Third-party SEO figures are estimates. Skills should report the source, market, retrieval date, missing values, and credits consumed where available rather than inventing metrics.

## Contributing

Useful, focused improvements are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md), open an issue, or submit a pull request. Every contribution must remain free of client data, confidential material, credentials, and proprietary orchestration.

Run validation before submitting:

```bash
python3 -m pip install -r requirements-dev.txt
scripts/validate.sh
```

For bugs and feature requests, use [GitHub Issues](https://github.com/superamped/ai-marketing-skills/issues). See [SECURITY.md](SECURITY.md) for private vulnerability reporting.

## Community for B2B SaaS founders

Building a B2B SaaS product and using these skills to find your first customers? Apply to join [Launch Party by Superamped](https://joinlaunchparty.com/?utm_source=github&utm_medium=referral&utm_campaign=ai-marketing-skills), a community for early-stage B2B SaaS founders working through customer acquisition together.

Launch Party is an adjacent founder community, not the support channel for this repository. Use GitHub Issues for repository support.

## License

MIT. See [LICENSE](LICENSE).
