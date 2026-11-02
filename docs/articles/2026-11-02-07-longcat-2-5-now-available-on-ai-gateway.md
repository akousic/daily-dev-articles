# LongCat 2.5 now available on AI Gateway

- **Source:** Vercel
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-11-02 22:41
- **Original:** https://vercel.com/changelog/longcat-2-5-now-available-on-ai-gateway

## Summary

LongCat 2.5 from Meituan is now available on AI Gateway. This model combines native visual understanding with coding and multi-step tool use for agents working across complex codebases and full-project builds. Meituan highlights improvements in visual programming, creative design, and 3D tasks, alongside longer agent workflows that carry engineering work from planning through execution.

## Key Takeaways

- The model supports text and image inputs with a 1M-token context window for code, documents, and extended task histories.
- Use meituan/longcat-2.5 as the model name: import { streamText } from 'ai';const result = streamText({ model: 'meituan/longcat-2.5', prompt: 'Outline a database migration in three brief steps.',});for await (const text of result.textStream) { process.stdout.write(text);} To use it in Claude Code, Codex, Cursor, and more, install the latest Vercel CLI and run setup: npx vercel ai-gateway setup Then select meituan/longcat-2.5 in the agent.
- See the coding agents guide for details.

---
_Auto-generated daily digest entry._
