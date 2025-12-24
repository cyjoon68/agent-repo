---
name: figma-mcp
description: Configure Figma MCP server connection. Use when the user provides a Figma API token and wants to set up or connect Figma MCP. Triggers on phrases like "Figma token", "Figma API key", "connect Figma MCP", "setup Figma MCP".
---

# Figma MCP Connector

Configure MCP server settings automatically when given a Figma API token.

## Workflow

When user provides a Figma API token:

### 1. Validate Token

Check token format (starts with figd\_ or fig)

### 2. Update MCP Settings

Add to `.claude/settings.json` or project MCP config file:

```json
{
  "mcpServers": {
    "figma-developer-mcp": {
      "command": "npx",
      "args": ["-y", "figma-developer-mcp", "--stdio"],
      "env": {
        "FIGMA_API_KEY": "<user-provided-token>"
      }
    }
  }
}
```

### 3. Confirm Setup

Inform user that Claude Code restart is required after configuration.

## Token Generation Guide

If user doesn't have a token:

1. Click profile icon in Figma app
2. Go to **Settings** > **Security**
3. Click **Generate New Token** in Personal Access Tokens section
4. Enter token name (e.g., "Claude_MCP")
5. Copy the generated token (shown only once)

## Security Notes

- Never hardcode tokens in source code
- Add `.env` files to `.gitignore`
- Revoke and regenerate immediately if token is leaked
