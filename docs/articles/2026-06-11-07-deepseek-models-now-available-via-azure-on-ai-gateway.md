# DeepSeek models now available via Azure on AI Gateway

- **Source:** Vercel
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-06-11 17:38
- **Original:** https://vercel.com/changelog/deepseek-models-now-available-via-azure-on-ai-gateway

## Summary

1 min read Azure is now a provider for DeepSeek V4 Pro and V4 Flash on AI Gateway. Requests to either model can route through Azure alongside the existing providers for another failover path. No code changes are required: default routing considers Azure automatically, and if a provider fails the gateway falls back through the remaining list.

## Key Takeaways

- If you want requests to try Azure first, use order in the gateway provider options to prefer Azure while keeping the other providers as fallback for deepseek/deepseek-v4-pro or deepseek/deepseek-v4-flash in the AI SDK: import { streamText } from 'ai'; const result = streamText({ model: 'deepseek/deepseek-v4-pro', prompt: 'Refactor this function to use async/await.', providerOptions: { gateway: { order: ['azure'], }, },});If you have existing Azure credentials, you can bring your own key and AI Gateway will use it for requests routed to Azure.
- See API key authentication and BYOK for setup.
- AI Gateway provides a unified API for calling models, tracking usage and cost, and configuring retries, failover, and performance optimizations for higher-than-provider uptime.

---
_Auto-generated daily digest entry._
