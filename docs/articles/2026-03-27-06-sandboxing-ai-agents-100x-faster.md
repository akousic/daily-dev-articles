# Sandboxing AI agents, 100x faster

- **Source:** Cloudflare
- **Rank (today):** #6
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-03-27 14:59
- **Original:** https://blog.cloudflare.com/dynamic-workers/

## Summary

Last September we introduced Code Mode, the idea that agents should perform tasks not by making tool calls, but instead by writing code that calls APIs. We've shown that simply converting an MCP server into a TypeScript API can cut token usage by 81%. We demonstrated that Code Mode can also operate behind an MCP server instead of in front of it, creating the new Cloudflare MCP server that exposes the entire Cloudflare API with just two tools and under 1,000 tokens.

## Key Takeaways

- But if an agent (or an MCP server) is going to execute code generated on-the-fly by AI to perform tasks, that code needs to run somewhere, and that somewhere needs to be secure.
- You can't just eval() AI-generated code directly in your app: a malicious user could trivially prompt the AI to inject vulnerabilities.
- You need a sandbox: a place to execute code that is isolated from your application and from the rest of the world, except for the specific capabilities the code is meant to access.

---
_Auto-generated daily digest entry._
