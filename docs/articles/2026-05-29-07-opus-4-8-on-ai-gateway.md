# Opus 4.8 on AI Gateway

- **Source:** Vercel
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-05-29 17:37
- **Original:** https://vercel.com/changelog/opus-4-8-on-ai-gateway

## Summary

1 min read Claude Opus 4.8 is now available on Vercel AI Gateway. Claude Opus 4.8 is built for long-horizon agentic execution and handles complex, multi-step coding tasks like refactors that previously required human correction mid-task. The model also produces clearer, less hedgy prose for knowledge work like drafting documents, analyzing data, and building presentations.

## Key Takeaways

- To use Opus 4.8, set model to anthropic/claude-opus-4.8 in the AI SDK.
- import { streamText } from 'ai'; const result = streamText({ model: 'anthropic/claude-opus-4.8', prompt: 'Find and fix the root cause of these intermittent test failures.', providerOptions: { anthropic: { thinking: { type: 'adaptive' }, effort: 'high', }, },}); AI Gateway provides a unified API for calling models, tracking usage and cost, and configuring retries, failover, and performance optimizations for higher-than-provider uptime.
- It includes built-in custom reporting, Zero Data Retention support, dynamic provider sorting by latency & cost, and more.

---
_Auto-generated daily digest entry._
