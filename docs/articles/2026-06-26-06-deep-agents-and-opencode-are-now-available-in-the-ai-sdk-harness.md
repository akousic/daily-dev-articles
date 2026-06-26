# Deep Agents and OpenCode are now available in the AI SDK Harness

- **Source:** Vercel
- **Rank (today):** #6
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-06-26 16:23
- **Original:** https://vercel.com/changelog/deepagents-and-opencode-harness-adapters

## Summary

The AI SDK Harness lets you run established coding-agent runtimes through one unified interface, so you can switch runtimes without changing your application code. Today we're adding two new adapters, Deep Agents and OpenCode, both running inside a Vercel Sandbox. Link to headingDeep Agents @ai-sdk/harness-deepagents adapts LangChain's deepagents runtime, with built-in file and shell tools, skills, host tools, multi-turn sessions, attach and resume, and built-in tool approvals.

## Key Takeaways

- import { HarnessAgent } from '@ai-sdk/harness/agent';import { deepAgents } from '@ai-sdk/harness-deepagents';const agent = new HarnessAgent({ harness: deepAgents,});Basic example for using Deep Agents with HarnessAgent Read the Deep Agents harness documentation to get started.
- Link to headingOpenCode @ai-sdk/harness-opencode boots a real OpenCode server inside the sandbox via @opencode-ai/sdk and streams its session events through the harness.
- It exposes OpenCode's built-in tools, supports both built-in and host tool approvals, and lets you pick the model, provider, and reasoning variant.

---
_Auto-generated daily digest entry._
