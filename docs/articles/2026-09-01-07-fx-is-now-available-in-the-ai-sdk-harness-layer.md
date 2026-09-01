# fx is now available in the AI SDK harness layer

- **Source:** Vercel
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-09-01 17:46
- **Original:** https://vercel.com/changelog/fx-ai-sdk-harness-adapter

## Summary

The AI SDK harness layer now supports fx, Vercel's lightweight, open-source coding agent. The harness layer provides one API for running coding agents in your application, so you can add fx without building a separate integration. Configure HarnessAgent with the official @ai-sdk/harness-fx adapter: import { HarnessAgent } from '@ai-sdk/harness/agent';import { fx } from '@ai-sdk/harness-fx'; const agent = new HarnessAgent({ harness: fx,}); Run fx through the HarnessAgent interface.

## Key Takeaways

- The @ai-sdk/harness-fx adapter connects to fx over the Agent Client Protocol (ACP) using @ai-sdk/harness-acp.
- fx joins Claude Code, Cline, Codex, Cursor, Deep Agents, Grok Build, OpenCode, and Pi in the list of supported harnesses.
- Read the fx harness documentation to get started.

---
_Auto-generated daily digest entry._
