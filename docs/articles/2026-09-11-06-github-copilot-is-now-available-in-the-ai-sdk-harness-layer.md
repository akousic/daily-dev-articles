# GitHub Copilot is now available in the AI SDK harness layer

- **Source:** Vercel
- **Rank (today):** #6
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-09-11 17:42
- **Original:** https://vercel.com/changelog/github-copilot-ai-sdk-harness-adapter

## Summary

The AI SDK harness layer now supports GitHub Copilot through the official @ai-sdk/harness-github-copilot adapter. The harness layer lets your application run different coding agents through the same HarnessAgent interface, so you can switch agents without changing your application code. Pass githubCopilot to HarnessAgent: import { HarnessAgent } from '@ai-sdk/harness/agent';import { githubCopilot } from '@ai-sdk/harness-github-copilot'; const agent = new HarnessAgent({ harness: githubCopilot,}); Create a HarnessAgent that runs GitHub Copilot.

## Key Takeaways

- Under the hood, the adapter uses @ai-sdk/harness-acp to connect GitHub Copilot to HarnessAgent through the Agent Client Protocol (ACP).
- Supported harnesses now include, in addition to GitHub Copilot, Claude Code, Cline, Codex, Cursor, Deep Agents, fx, Grok Build, OpenCode, and Pi, with more coming soon.
- Read the GitHub Copilot harness documentation to get started.

---
_Auto-generated daily digest entry._
