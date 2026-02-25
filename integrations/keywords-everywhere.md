# Keywords Everywhere

Keywords Everywhere is an MCP server that gives Claude native tool access to keyword data, traffic metrics, and backlink data. No curl commands or scripts needed — Claude calls the tools directly.

## Setup

### Claude Code (recommended)

Streamable HTTP transport — one command:

```bash
claude mcp add --transport http keywords-everywhere \
  https://mcp.keywordseverywhere.com/mcp \
  -H "Authorization: Bearer <your-api-key>"
```

Or add to project scope (shared via `.mcp.json`):

```bash
claude mcp add -s project --transport http keywords-everywhere \
  https://mcp.keywordseverywhere.com/mcp \
  -H "Authorization: Bearer <your-api-key>"
```

Verify it's connected:

```bash
claude mcp list
```

Should show `keywords-everywhere` with status `✓ healthy`.

### Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "keywords-everywhere": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://mcp.keywordseverywhere.com/mcp",
        "--header",
        "Authorization: ${KEYWORDS_EVERYWHERE_AUTH_HEADER}"
      ],
      "env": {
        "KEYWORDS_EVERYWHERE_AUTH_HEADER": "Bearer <your-api-key>"
      }
    }
  }
}
```

Claude Desktop doesn't support streamable HTTP natively, so we use `mcp-remote` as a stdio wrapper.

## Authentication

Every call uses a bearer token:

```
Authorization: Bearer <your-api-key>
```

Get your API key from the [Keywords Everywhere dashboard](https://keywordseverywhere.com/).

## Available Tools

### Keyword Data

| Tool | Input | Returns |
|------|-------|---------|
| **Get Keyword Data** | List of keywords | Volume, CPC, competition, trend per keyword |
| **Get Related Keywords** | Seed keyword | Related keywords with volume, CPC, competition, trend |
| **Get "People Also Search For" Keywords** | Seed keyword | PASF keywords with volume, CPC, competition, trend |
| **Get Domain Keywords** | Domain name | Keywords the domain ranks for with positions |
| **Get URL Keywords** | URL | Keywords a specific URL ranks for |

### Traffic Metrics

| Tool | Input | Returns |
|------|-------|---------|
| **Get Domain Traffic Metrics** | Domain name | Traffic estimates, top pages |
| **Get URL Traffic Metrics** | URL | Traffic estimates for a specific page |

### Backlink Data

| Tool | Input | Returns |
|------|-------|---------|
| **Get Domain Backlinks** | Domain name | All backlinks pointing to the domain |
| **Get Unique Domain Backlinks** | Domain name | Deduplicated backlinks (one per referring domain) |
| **Get Page Backlinks** | URL | Backlinks pointing to a specific page |
| **Get Unique Page Backlinks** | URL | Deduplicated page backlinks |

### Utility

| Tool | Input | Returns |
|------|-------|---------|
| **Get Credit Balance** | — | Remaining API credits |
| **Get Countries** | — | Supported country codes |
| **Get Currencies** | — | Supported currencies |

## Credits & Costs

Keywords Everywhere uses a credit-based system. Different endpoints consume different amounts of credits. Check your balance with the **Get Credit Balance** tool before running large keyword expansions.

## Skills That Use This Integration

| Skill | Requirement |
|-------|-------------|
| **Keyword Research** | Required — primary data source for keyword expansion |
| **Competitor Keyword Analysis** | Required — maps competitor organic search presence |
| **Competitor Content Analysis** | Optional — enriches analysis with traffic metrics |

## Notes

- The MCP server exposes the `/mcp` endpoint (Streamable HTTP), not `/sse`
- All keyword data includes country-specific results — specify country code for localised volumes
- Rate limits apply — avoid sending thousands of keywords in a single batch; chunk if needed
