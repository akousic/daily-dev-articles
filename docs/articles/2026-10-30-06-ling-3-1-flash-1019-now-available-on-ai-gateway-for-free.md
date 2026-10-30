# Ling 3.1 Flash 1019 now available on AI Gateway for free

- **Source:** Vercel
- **Rank (today):** #6
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-10-30 19:06
- **Original:** https://vercel.com/changelog/ling-3-1-flash-1019-now-available-on-ai-gateway-for-free

## Summary

Ling 3.1 Flash 1019 from InclusionAI is now available on AI Gateway, free until November 3, 2026. The updated model is designed for coding, multi-step reasoning, and agents that use tools. Its 1M-token context window supports workflows involving long documents, code, and extended task histories.

## Key Takeaways

- Use inclusionai/ling-3.1-flash-1019 as the model name: import { streamText } from 'ai'; const result = streamText({ model: 'inclusionai/ling-3.1-flash-1019', prompt: 'Suggest three ways to make an AI agent more reliable.',}); for await (const text of result.textStream) { process.stdout.write(text);} Free requests still appear in your spend dashboard with a full request trace, they just cost nothing.
- On November 3, requests will begin charging at the published rate.
- To use it in Claude Code, Codex, Cursor, and more, install the latest Vercel CLI and run setup: npx vercel ai-gateway setup Then select inclusionai/ling-3.1-flash-1019 in the agent.

---
_Auto-generated daily digest entry._
