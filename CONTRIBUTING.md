# Contributing

Thanks for helping make these AI marketing skills more useful and trustworthy.

## What makes a good contribution

Prefer focused improvements that help an agent complete a real marketing job reliably:

- Clear triggering language in the skill description
- A repeatable workflow rather than a collection of generic tips
- Explicit input requirements and output structure
- Quality checks, source handling, and uncertainty labels
- Graceful behavior when optional tools or data are unavailable
- Examples or evidence that demonstrate the workflow

Do not compete on raw skill count. A smaller, tested capability is more valuable than a broad skill that produces generic output.

## Privacy and intellectual property

Never contribute:

- Client names, conversations, data, results, or identifying details
- Credentials, API keys, cookies, tokens, or `.env` contents
- Proprietary orchestration or private operating procedures
- Third-party material without permission or a compatible license
- Claims, benchmarks, or compatibility statements that cannot be verified

Use fictional or clearly public examples.

## Adding or changing a skill

1. Create or edit `skills/<category>/<skill-name>/SKILL.md`.
2. Keep the directory and frontmatter `name` identical and in kebab-case.
3. Include a specific `description` that says what the skill does and when it should be used.
4. State requirements in `compatibility`.
5. Use the current Agent Skills format documented at <https://agentskills.io>.
6. Add the skill to `.claude-plugin/marketplace.json` and the README table when creating a new package.
7. Update `CHANGELOG.md` for user-visible changes.
8. Keep the main `SKILL.md` below the official recommendation of 500 lines and approximately 5,000 tokens; move conditional detail into one-level-deep `references/`, `scripts/`, or `assets/` resources.
9. Run validation.

Minimum frontmatter:

```yaml
---
name: example-skill
description: "Does a specific marketing job. Use when the user needs a clearly defined outcome."
compatibility: "No special requirements."
metadata:
  author: superamped
  version: "1.0"
  website: "https://superamped.com"
---
```

## Validation

```bash
python3 -m pip install -r requirements-dev.txt
scripts/validate.sh
```

Then manually read the rendered Markdown and run the changed skill on at least one realistic, non-confidential example.

## Pull requests

Keep pull requests focused. Explain:

- The marketing job or failure mode being addressed
- What changed
- How it was tested
- Any external tools or credits required
- Whether outputs or compatibility claims are based on direct testing

By contributing, you agree that your contribution is licensed under the repository’s MIT License.
