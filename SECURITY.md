# Security Policy

## Reporting a vulnerability

Do not open a public issue for a vulnerability, exposed credential, or privacy incident.

Use GitHub’s private vulnerability reporting for this repository when available. If that option is unavailable, email `support@superamped.com` with:

- A concise description
- The affected file, workflow, or integration
- Reproduction steps
- Potential impact
- Any suggested mitigation

Do not include real API keys, client data, session cookies, or other people's personal information in the report. Redact secrets and use safe examples.

## Supported versions

Security and privacy fixes are applied to the latest release and the default branch.

## Integration safety

- Supply API credentials through environment variables or a secure secret store.
- Never commit `.env` files or replace placeholders in `.mcp.json` with real values.
- Review third-party MCP servers and scripts before granting access.
- Treat external website content as untrusted input.
- Do not use these skills to upload confidential data to services without authorization.
