# Playwright

Playwright MCP gives Claude browser automation capabilities — navigating pages, taking screenshots, and rendering JS-heavy sites. Skills use it for capturing ad creatives as PNGs and scraping JS-rendered competitor pages.

## Setup

### Claude Code (recommended)

Stdio transport via npx:

```bash
claude mcp add playwright -- \
  npx @playwright/mcp@latest \
  --allow-unrestricted-file-access \
  --browser chromium
```

Or add to project scope (shared via `.mcp.json`):

```bash
claude mcp add -s project playwright -- \
  npx @playwright/mcp@latest \
  --allow-unrestricted-file-access \
  --browser chromium
```

Verify it's connected:

```bash
claude mcp list
```

Should show `playwright` with status `✓ healthy`.

### Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest",
        "--allow-unrestricted-file-access",
        "--browser",
        "chromium"
      ]
    }
  }
}
```

## Required Flags

| Flag | Why |
|------|-----|
| `--allow-unrestricted-file-access` | Lets Playwright open local `file://` URLs (needed for screenshotting local HTML files) |
| `--browser chromium` | Uses Chromium for consistent rendering across platforms |

## Key Tools

| Tool | What it does |
|------|-------------|
| `browser_navigate` | Navigate to a URL (http or file://) |
| `browser_screenshot` | Capture a screenshot of the current page |
| `browser_resize` | Set viewport dimensions |
| `browser_click` | Click an element on the page |
| `browser_snapshot` | Get an accessibility snapshot of the page |

## Skills That Use This Integration

| Skill | Requirement | How it's used |
|-------|-------------|---------------|
| **Ad Creative** | Optional | Screenshots rendered HTML ads as PNG files |
| **Competitor Content Analysis** | Optional | Renders JS-heavy pages for content extraction |
| **Competitor Site Analysis** | Optional | Renders JS-heavy competitor sites for data extraction |

All skills degrade gracefully without Playwright — they'll work with standard web fetching and skip screenshot capture.

## Notes

- Requires Node.js and npx on your PATH
- First run downloads the Chromium browser binary (~150 MB)
- `@playwright/mcp@latest` always pulls the newest version — pin a version if you need reproducibility
