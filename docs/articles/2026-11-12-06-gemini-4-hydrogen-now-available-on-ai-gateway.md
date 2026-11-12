# Gemini 4 Hydrogen now available on AI Gateway

- **Source:** Vercel
- **Rank (today):** #6
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-11-12 21:23
- **Original:** https://vercel.com/changelog/gemini-4-hydrogen-now-available-on-ai-gateway

## Summary

Gemini 4 Hydrogen from Google is now available on AI Gateway. Gemini 4 Hydrogen succeeds Gemini 3.8 Flash, improving agentic coding, knowledge work, and tool use while staying in the same latency class. It handles longer engineering tasks and produces better-researched documents, spreadsheets, and presentations in fewer agent steps.

## Key Takeaways

- Hydrogen follows system instructions, formatting requirements, and task boundaries more closely, with more reliable tool orchestration across long conversations.
- Improvements in visual reasoning and technical problem-solving support multimodal workflows, while stronger grounding reduces unsupported claims in search-backed answers and invented tool or test results in coding reports.
- Use google/gemini-4-hydrogen as the model name: import { streamText } from 'ai'; const result = streamText({ model: 'google/gemini-4-hydrogen', prompt: 'Write a TypeScript retry helper with exponential backoff and jitter.',}); for await (const text of result.textStream) { process.stdout.write(text);} To use it in Claude Code, Codex, Cursor, and more, install the latest Vercel CLI and run setup: npx vercel ai-gateway setup Then select google/gemini-4-hydrogen in the agent.

---
_Auto-generated daily digest entry._
