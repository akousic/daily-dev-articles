# GLM 5.3 FlashX now available on AI Gateway

- **Source:** Vercel
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-09-19 17:08
- **Original:** https://vercel.com/changelog/glm-5-3-flashx-now-available-on-ai-gateway

## Summary

GLM 5.3 FlashX is now available on AI Gateway. GLM 5.3 FlashX is a high-speed serving option for Z.ai's multimodal coding model, delivering inference at ~200 tokens per second for faster streamed responses. The higher serving speed is useful for coding agents, tool loops, and interactive applications where users wait on generated output.

## Key Takeaways

- Use zai/glm-5.3-flashx across API formats and in coding agents: import { streamText } from 'ai'; const result = streamText({ model: 'zai/glm-5.3-flashx', prompt: 'Name three checks to run after deploying a latency-sensitive API',}); for await (const text of result.textStream) { process.stdout.write(text);} To use it in a coding agent, see the coding agents guide, then run vercel ai-gateway setup to create a key and configure your supported agents.
- Select zai/glm-5.3-flashx inside the agent.
- AI Gateway provides a unified API for calling models, tracking usage and cost, and configuring retries, failover, and performance optimizations for higher-than-provider uptime.

---
_Auto-generated daily digest entry._
