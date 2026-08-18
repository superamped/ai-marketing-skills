# Keywords Everywhere

Keywords Everywhere is an MCP server that gives Claude native tool access to keyword data, traffic metrics, and backlink data. No curl commands or scripts needed — Claude calls the tools directly.

## Setup

### Claude Code and compatible MCP hosts

The repository includes a secret-free [`.mcp.json`](../.mcp.json) template using Streamable HTTP:

```json
{
  "mcpServers": {
    "keywords-everywhere": {
      "type": "http",
      "url": "https://mcp.keywordseverywhere.com/mcp",
      "headers": {
        "Authorization": "Bearer ${KEYWORDS_EVERYWHERE_API_KEY}"
      }
    }
  }
}
```

Supply `KEYWORDS_EVERYWHERE_API_KEY` to the host process from a secure secret store, then restart the host and verify the server is healthy. Do not replace the placeholder with a real key or commit an `.env` file.

For Claude Code, verify configured MCP servers with:

```bash
claude mcp list
```

MCP configuration and environment-variable interpolation vary by host and version. If your host does not read `.mcp.json`, follow its current documentation and use the same server URL and authorization header without saving the key in this repository.

## Authentication

Every call uses a bearer token supplied through the environment:

```
Authorization: Bearer ${KEYWORDS_EVERYWHERE_API_KEY}
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
