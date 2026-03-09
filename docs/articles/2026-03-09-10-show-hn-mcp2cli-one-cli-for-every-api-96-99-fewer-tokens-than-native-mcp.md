# Show HN: Mcp2cli – One CLI for every API, 96-99% fewer tokens than native MCP

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 129
- **Published (UTC):** 2026-03-09 05:18
- **Original:** https://github.com/knowsuchagency/mcp2cli

## Summary

Turn any MCP server or OpenAPI spec into a CLI — at runtime, with zero codegen. Save 96–99% of the tokens wasted on tool schemas every turn. pip install mcp2cli # Or run directly without installing uvx mcp2cli --help mcp2cli ships with an installable skill that teaches AI coding agents (Claude Code, Cursor, Codex) how to use it.

## Key Takeaways

- Once installed, your agent can discover and call any MCP server or OpenAPI endpoint — and even generate new skills from APIs.
- npx skills add knowsuchagency/mcp2cli --skill mcp2cli After installing, try prompts like: mcp2cli --mcp https://mcp.example.com/sse — interact with an MCP servermcp2cli create a skill for https://api.example.com/openapi.json — generate a skill from an API # Connect to an MCP server over HTTP mcp2cli --mcp https://mcp.example.com/sse --list # Call a tool mcp2cli --mcp https://mcp.example.com/sse search --query "test" # With auth header mcp2cli --mcp https://mcp.example.com/sse --auth-header "x-api-key:sk-..." \ query --sql "SELECT 1" # List tools from an MCP server mcp2cli --mcp-stdio "npx @modelcontextprotocol/server-filesystem /tmp" --list # Call a tool mcp2cli --mcp-stdio "npx @modelcontextprotocol/server-filesystem /tmp" \ read-file --path /tmp/hello.txt # Pass environment variables to the server process mcp2cli --mcp-stdio "node server.js" --env API_KEY=sk-...
- --env DEBUG=1 \ search --query "test" # List all commands from a remote spec mcp2cli --spec https://petstore3.swagger.io/api/v3/openapi.json --list # Call an endpoint mcp2cli --spec ./openapi.json --base-url https://api.example.com list-pets --status available # With auth mcp2cli --spec ./spec.json --auth-header "Authorization:Bearer tok_..." create-item --name "Test" # POST with JSON body from stdin echo '{"name": "Fido", "tag": "dog"}' | mcp2cli --spec ./spec.json create-pet --stdin # Local YAML spec mcp2cli --spec ./api.yaml --base-url http://localhost:8000 --list # Pretty-print JSON (also auto-enabled for TTY) mcp2cli --spec ./spec.json --pretty list-pets # Raw response body (no JSON parsing) mcp2cli --spec ./spec.json --raw get-data # Pipe-friendly (compact JSON when not a TTY) mcp2cli --spec ./spec.json list-pets | jq '.[] | .name' # TOON output — token-efficient encoding for LLM consumption # Best for large uniform arrays (40-60% fewer tokens than JSON) mcp2cli --mcp https://mcp.example.com/sse --toon list-tags Specs and MCP tool lists are cached in ~/.cache/mcp2cli/ with a 1-hour TTL by default.

---
_Auto-generated daily digest entry._
