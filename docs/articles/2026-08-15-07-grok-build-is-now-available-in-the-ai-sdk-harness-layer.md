# Grok Build is now available in the AI SDK harness layer

- **Source:** Vercel
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-08-15 14:30
- **Original:** https://vercel.com/changelog/grok-build-harness-adapter

## Summary

The AI SDK harness layer lets you run established coding-agent runtimes through one unified interface, so you can switch runtimes without changing your application code. Today we are adding Grok Build, which runs through the same HarnessAgent interface as every other supported harness. @ai-sdk/harness-grok-build is the official harness adapter for Grok Build, built on top of the ACP harness adapter (@ai-sdk/harness-acp).

## Key Takeaways

- import { HarnessAgent } from '@ai-sdk/harness/agent';import { grokBuild } from '@ai-sdk/harness-grok-build'; const agent = new HarnessAgent({ harness: grokBuild,}); Basic example for using Grok Build with HarnessAgent Read the Grok Build harness documentation to get started.
- The full supported list of harnesses is now: Claude Code, Codex, Deep Agents, Grok Build, OpenCode, Pi, with more coming soon.

---
_Auto-generated daily digest entry._
