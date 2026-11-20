# GPT-Live 1.1 now available on AI Gateway

- **Source:** Vercel
- **Rank (today):** #5
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-11-20 21:44
- **Original:** https://vercel.com/changelog/gpt-live-1-1-now-available-on-ai-gateway

## Summary

GPT-Live 1.1 from OpenAI is now available on AI Gateway. GPT-Live 1.1 is a full-duplex voice model, so it listens while it speaks and a caller can pause, interrupt, or add detail mid-reply. Compared with the previous GPT-Live model, it transcribes speech more accurately and keeps a more consistent accent and voice across languages.

## Key Takeaways

- It uses the same Live endpoint and client delegation, so an existing GPT-Live integration only needs the new model ID.
- Copy link to headingSimple example without delegation Run openai/gpt-live-1.1 by itself: import { createOpenAI } from '@ai-sdk/openai'; const live = createOpenAI({ apiKey: process.env.AI_GATEWAY_API_KEY, baseURL: 'https://ai-gateway.vercel.sh/v1',}).experimental_realtime('openai/gpt-live-1.1', { api: 'live' }); const { url, headers } = await live.getServerWebSocketConfig(); send(live.serializeClientEvent({ type: 'session-start', config: { instructions: 'You are a helpful voice assistant.' },})); Copy link to headingDelegate work and keep talking Turn on client delegation, and use the session instructions to tell GPT-Live 1.1 when to ask for help.
- It asks by sending delegation-created.

---
_Auto-generated daily digest entry._
