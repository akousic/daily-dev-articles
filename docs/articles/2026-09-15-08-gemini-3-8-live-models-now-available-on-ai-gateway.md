# Gemini 3.8 Live models now available on AI Gateway

- **Source:** Vercel
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-09-15 18:05
- **Original:** https://vercel.com/changelog/gemini-3-8-live-models-now-available-on-ai-gateway

## Summary

Gemini 3.8 Live and Gemini 3.8 Live Extended Thinking from Google are now available on AI Gateway. Both models support real-time spoken interactions for voice assistants, conversational experiences, and applications that respond through audio. - google/gemini-3.8-live supports real-time audio, visual grounding, automatic switching across 97 languages, and background tool calls while the conversation continues.

## Key Takeaways

- - google/gemini-3.8-live-extended-thinking adds multi-step reasoning that runs in parallel with speech, allowing it to acknowledge requests and narrate progress without interrupting the conversation.
- Use either model through the AI SDK's realtime API.
- Install the Gateway provider and a WebSocket client: pnpm add @ai-sdk/gateway@latest ws Mint a short-lived token, open the WebSocket, and use the model adapter to serialize and parse realtime events: import { gateway } from '@ai-sdk/gateway';import WebSocket from 'ws'; const modelId = 'google/gemini-3.8-live';const { token, url } = await gateway.experimental_realtime.getToken({ model: modelId,}); const model = gateway.experimental_realtime(modelId);const config = model.getWebSocketConfig({ token, url });const ws = new WebSocket(config.url, config.protocols); const send = async ( event: Parameters<typeof model.serializeClientEvent>[0],) => ws.send(JSON.stringify(await model.serializeClientEvent(event))); ws.on('open', async () => { await send({ type: 'session-update', config: { outputModalities: ['audio'], outputAudioTranscription: {}, // Extended Thinking only.

---
_Auto-generated daily digest entry._
