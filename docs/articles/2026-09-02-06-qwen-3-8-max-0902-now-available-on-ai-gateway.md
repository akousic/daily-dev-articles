# Qwen 3.8 Max 0902 now available on AI Gateway

- **Source:** Vercel
- **Rank (today):** #6
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-09-02 17:49
- **Original:** https://vercel.com/changelog/qwen-3-8-max-0902-now-available-on-ai-gateway

## Summary

Qwen 3.8 Max 0902 from Alibaba is now available on AI Gateway. This is a new snapshot of Qwen 3.8 Max, with the gains concentrated in coding on larger projects, long-horizon work that runs without supervision, and agent runs. Vision handling is more accurate on charts and dense documents.

## Key Takeaways

- To use Qwen 3.8 Max 0902, set model to alibaba/qwen3.8-max-0902: import { streamText } from 'ai'; const result = streamText({ model: 'alibaba/qwen3.8-max-0902', prompt: 'Add pagination to the results endpoint.',}); The dated ID pins this snapshot, so a later release will not change what your requests run against.
- To move existing traffic onto it without a code change, add a rewrite routing rule.
- The gateway substitutes the destination transparently, so an application that still asks for alibaba/qwen3.8-max runs on the new snapshot: vercel ai-gateway rules add --type rewrite \ --source alibaba/qwen3.8-max \ --destination alibaba/qwen3.8-max-0902 To use it in a coding agent, see the coding agents guide, then run vercel ai-gateway coding-agents setup to connect agents like Claude Code, Codex, OpenCode, Cursor, Pi, and more and select alibaba/qwen3.8-max-0902.

---
_Auto-generated daily digest entry._
