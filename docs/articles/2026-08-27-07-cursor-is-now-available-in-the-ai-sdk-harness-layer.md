# Cursor is now available in the AI SDK harness layer

- **Source:** Vercel
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-08-27 23:42
- **Original:** https://vercel.com/changelog/cursor-ai-sdk-harness-adapter

## Summary

The AI SDK harness layer now supports Cursor through the official @ai-sdk/harness-cursor adapter. The harness layer lets your application run different coding agents through the same HarnessAgent interface, so you can switch agents without changing your application code. Pass cursor to HarnessAgent: import { HarnessAgent } from '@ai-sdk/harness/agent';import { cursor } from '@ai-sdk/harness-cursor'; const agent = new HarnessAgent({ harness: cursor,}); Create a HarnessAgent that runs Cursor.

## Key Takeaways

- Under the hood, the adapter uses @ai-sdk/harness-acp to connect Cursor to HarnessAgent through the Agent Client Protocol (ACP).
- Supported harnesses now include, in addition to Cursor, Claude Code, Cline, Codex, Deep Agents, Grok Build, OpenCode, and Pi, with more coming soon.
- Read the Cursor harness documentation to get started.

---
_Auto-generated daily digest entry._
