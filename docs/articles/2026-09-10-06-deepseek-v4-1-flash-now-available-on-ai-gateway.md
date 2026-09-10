# DeepSeek V4.1 Flash now available on AI Gateway

- **Source:** Vercel
- **Rank (today):** #6
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-09-10 17:37
- **Original:** https://vercel.com/changelog/deepseek-v4-1-flash-now-available-on-ai-gateway

## Summary

DeepSeek V4.1 Flash is now available on AI Gateway with native image understanding. V4.1 Flash has vision support and accepts text and images in the same request, so you can ask questions about screenshots, read charts, and extract information from visual content. The model has a 1 million token context window and supports responses up to 384,000 tokens, along with reasoning, tool use, and prompt caching.

## Key Takeaways

- Its new architecture processes input and generates output with separate components, reducing the active computation needed for each stage.
- Use deepseek/deepseek-v4.1-flash as the model name: import { streamText } from 'ai'; const result = streamText({ model: 'deepseek/deepseek-v4.1-flash', prompt: 'Explain how to make a database migration safe to roll back.',}); To use it in Claude Code, Codex, Cursor, and more, install the latest Vercel CLI and run setup: npm i -g vercel@latestvercel ai-gateway setup Then select deepseek/deepseek-v4.1-flash in the agent.
- See the coding agents guide for details.

---
_Auto-generated daily digest entry._
