# Grok 4.5 now available on AI Gateway

- **Source:** Vercel
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-07-09 16:30
- **Original:** https://vercel.com/changelog/grok-4-5-now-available-on-ai-gateway

## Summary

Grok 4.5 from SpaceXAI is now available on AI Gateway. Built for coding, knowledge work, and STEM, the model accepts text and image inputs. Grok 4.5 supports low, medium, and high reasoning levels and defaults to high.

## Key Takeaways

- Set the level with reasoning to balance speed against depth.
- To use Grok 4.5, set model to xai/grok-4.5 in the AI SDK: import { streamText } from 'ai'; const result = streamText({ model: 'xai/grok-4.5', reasoning: 'high', prompt: 'Analyze this dataset and summarize the key trends.',});You can also set routing rules to switch to Grok 4.5 from other gateway models without touching your code.
- vercel ai-gateway rules add \ --type rewrite \ --source xai/grok-4.3 \ --destination xai/grok-4.5AI Gateway provides a unified API for calling models, tracking usage and cost, and configuring retries, failover, and performance optimizations for higher-than-provider uptime.

---
_Auto-generated daily digest entry._
