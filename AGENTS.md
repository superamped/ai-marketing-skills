# AI Marketing Skills

This repo contains standalone marketing skills in the `skills/` directory. Each skill is a self-contained markdown prompt with YAML frontmatter.

## Available Skills

- `skills/search-page-audit/SKILL.md` — 38-point SEO + AI optimization audit for any URL

## How to Use

When a user asks to run an audit (or any skill), read the corresponding `SKILL.md` file and follow its instructions exactly. Pass the user's input (e.g. a URL) as the argument.

## Conventions

- Skills live in `skills/<skill-name>/SKILL.md`
- Each skill defines its own process, output format, and rules
- Do not improvise outside what the skill specifies — follow the SKILL.md
