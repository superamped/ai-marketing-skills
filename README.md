# AI Marketing Skills

Open-source AI marketing skills for AI coding agents. Create strategy, research competitors, do SEO, write copy and content, analyze campaigns, and more — all from your terminal.

Works with [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [Codex](https://github.com/openai/codex), [OpenCode](https://opencode.ai), [Cursor](https://cursor.com), and any tool that reads `AGENTS.md`.

## What are skills?

Skills are standalone markdown files that give AI coding tools specialised marketing capabilities. Each skill is a single-purpose prompt that produces one output. Drop them into your project and run them.

## Skills

| Skill | What it does |
|-------|-------------|
| **Search Page Audit** | 38-point SEO + AI optimization audit on any URL — covers SEO fundamentals, content structure, AI/GEO readiness, and E-E-A-T authority signals |

## Getting Started

1. Clone this repo
2. Copy the `skills/` folder into your project
3. Run the skill using your AI coding tool

**Claude Code** — Copy `skills/` to `.claude/skills/` in your project, then run `/search-audit <url>`

**Codex** — Copy `skills/` to `.agents/skills/` in your project, then run `/search-audit <url>`

**OpenCode** — Copy `skills/` to `.agents/skills/` or `.claude/skills/` in your project, then run `/search-audit <url>`

**Cursor / Other** — Reference the skill in your prompt or copy `AGENTS.md` to your project root

## Community

Join the [Growth Engineering Community](https://superamped.com/growth-engineering-community) — a community for marketers and founders engineering growth with AI.

## License

MIT. See [LICENSE](LICENSE) for details.
