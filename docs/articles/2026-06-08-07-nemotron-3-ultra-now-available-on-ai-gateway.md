# Nemotron 3 Ultra now available on AI Gateway

- **Source:** Vercel
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-06-08 17:25
- **Original:** https://vercel.com/changelog/nemotron-3-ultra-now-available-on-ai-gateway

## Summary

1 min read Nemotron 3 Ultra from Nvidia is now available on Vercel AI Gateway. Nemotron 3 Ultra is an open Mixture-of-Experts reasoning model built for orchestrating long-running agent workflows, with a 1M token context window. The model targets multi-turn agent workflows: planning, tool use, sub-agent delegation, and error recovery.

## Key Takeaways

- Throughput reaches up to 350 tokens per second, with up to 30% lower cost on agentic tasks.
- To use Nemotron 3 Ultra, set model to nvidia/nemotron-3-ultra-550b-a55b in the AI SDK.
- import { streamText } from 'ai'; const result = streamText({ model: 'nvidia/nemotron-3-ultra-550b-a55b', prompt: 'Plan and run a multi-step research task and synthesize a report.',});AI Gateway provides a unified API for calling models, tracking usage and cost, and configuring retries, failover, and performance optimizations for higher-than-provider uptime.

---
_Auto-generated daily digest entry._
