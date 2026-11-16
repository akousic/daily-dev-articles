# Hy4 Flash now available on AI Gateway for 50% off

- **Source:** Vercel
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-11-16 23:17
- **Original:** https://vercel.com/changelog/hy4-flash-now-available-on-ai-gateway-for-50-off

## Summary

Hy4 Flash from Tencent is now available on AI Gateway with an introductory 50% discount on input, cached input, and output tokens through November 29, 2026. Hy4 Flash is the new lower-cost model in the Hy4 family. It keeps the full Hy4 feature set at roughly a tenth of the price per token: reasoning with preserved thinking across turns, tool calling, structured outputs, prompt caching, and image input, with the same 1M-token context window.

## Key Takeaways

- Reasoning can be turned off for requests that don't need it, which suits high-volume coding, agent, and document workloads.
- Use tencent/hy4-flash as the model name: import { streamText } from 'ai'; const result = streamText({ model: 'tencent/hy4-flash', prompt: 'Summarize the tradeoffs of server-side rendering in three sentences.',}); for await (const text of result.textStream) { process.stdout.write(text);} To use it in Claude Code, Codex, Cursor, and more, install the latest Vercel CLI and run setup: npx vercel ai-gateway setup Then select tencent/hy4-flash in the agent.
- See the coding agents guide for details.

---
_Auto-generated daily digest entry._
