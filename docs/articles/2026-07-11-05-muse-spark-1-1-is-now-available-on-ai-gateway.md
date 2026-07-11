# Muse Spark 1.1 is now available on AI Gateway

- **Source:** Vercel
- **Rank (today):** #5
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-07-11 15:02
- **Original:** https://vercel.com/changelog/muse-spark-1-1-is-now-available-on-ai-gateway

## Summary

Muse Spark 1.1 from Meta is now available on AI Gateway. It is a multimodal reasoning model with a 1M token context window built for agentic tasks, accepting text, image, video, PDF, and audio inputs. Muse Spark 1.1 plans and orchestrates work across tools and services, operating as a main agent or as a subagent, and it works with new tools, MCP servers, and custom skills without examples.

## Key Takeaways

- The model supports parallel tool calling, structured output, and built-in search with citations.
- To use Muse Spark 1.1, set model to meta/muse-spark-1.1 in the AI SDK: import { streamText } from 'ai'; const result = streamText({ model: 'meta/muse-spark-1.1', prompt: 'Read this product spec PDF and implement the API it describes.',}); AI Gateway provides a unified API for calling models, tracking usage and cost, and configuring retries, failover, and performance optimizations for higher-than-provider uptime.
- It includes built-in custom reporting, Zero Data Retention support, budgets for API keys, routing rules, and more.

---
_Auto-generated daily digest entry._
