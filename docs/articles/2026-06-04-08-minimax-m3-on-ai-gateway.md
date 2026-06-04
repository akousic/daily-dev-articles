# MiniMax M3 on AI Gateway

- **Source:** Vercel
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-06-04 17:15
- **Original:** https://vercel.com/changelog/minimax-m3-on-ai-gateway

## Summary

1 min read MiniMax M3 is now available on Vercel AI Gateway. M3 is MiniMax's first model with a 1M-token context window and native multimodality, built around MiniMax Sparse Attention (MSA). M3 improves on software engineering, terminal-based tool use, and agentic web browsing, and is tuned for multi-turn collaboration.

## Key Takeaways

- To use MiniMax M3, set model to minimax/minimax-m3 in the AI SDK.
- import { streamText } from 'ai'; const result = streamText({ model: 'minimax/minimax-m3', prompt: 'Reproduce the bug in this GitHub issue and submit a fix.',}); Pass an image alongside a prompt to use M3's multimodal input: import { streamText } from 'ai'; const result = streamText({ model: 'minimax/minimax-m3', messages: [ { role: 'user', content: [ { type: 'text', text: 'This is a screenshot of a failing test.
- Identify the root cause and write the patch.', }, { type: 'image', image: 'https://example.com/failing-test.png', }, ], }, ],}); AI Gateway provides a unified API for calling models, tracking usage and cost, and configuring retries, failover, and performance optimizations for higher-than-provider uptime.

---
_Auto-generated daily digest entry._
