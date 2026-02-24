# Code Mode: give agents an entire API in 1,000 tokens

- **Source:** Cloudflare
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-02-24 21:41
- **Original:** https://blog.cloudflare.com/code-mode-mcp/

## Summary

Model Context Protocol (MCP) has become the standard way for AI agents to use external tools. But there is a tension at its core: agents need many tools to do useful work, yet every tool added fills the model's context window, leaving less room for the actual task. Code Mode is a technique we first introduced for reducing context window usage during agent tool use.

## Key Takeaways

- Instead of describing every operation as a separate tool, let the model write code against a typed SDK and execute the code safely in a Dynamic Worker Loader.
- The code acts as a compact plan.
- The model can explore tool operations, compose multiple calls, and return just the data it needs.

---
_Auto-generated daily digest entry._
