# Step 5 Preview now available on AI Gateway

- **Source:** Vercel
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-10-08 19:47
- **Original:** https://vercel.com/changelog/step-5-preview-now-available-on-ai-gateway

## Summary

Step 5 Preview, StepFun's flagship model, is now available on AI Gateway. It's built for agentic coding, professional knowledge work, and financial analysis, from building apps and debugging code to research and analytical reports. Step 5 Preview supports text and image input with a 1M-token context window, allowing you to work with large codebases, a stack of documents, or screenshots and charts in a single request.

## Key Takeaways

- Use stepfun/step-5-preview as the model name: import { streamText } from 'ai'; const result = streamText({ model: 'stepfun/step-5-preview', prompt: 'Plan a dashboard for analyzing quarterly financial results.',}); for await (const text of result.textStream) { process.stdout.write(text);} For other coding agents such as Claude Code, Codex, Cursor, and more, install the latest Vercel CLI and run setup: npm i -g vercel@latestvercel ai-gateway setup Then select stepfun/step-5-preview in the agent.
- See the coding agents guide for details.
- Try Step 5 Preview in the model playground.

---
_Auto-generated daily digest entry._
