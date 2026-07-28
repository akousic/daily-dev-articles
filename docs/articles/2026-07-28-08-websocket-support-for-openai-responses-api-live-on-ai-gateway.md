# WebSocket support for OpenAI Responses API live on AI Gateway

- **Source:** Vercel
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-07-28 16:07
- **Original:** https://vercel.com/changelog/websocket-support-for-openai-responses-api-live-on-ai-gateway

## Summary

AI Gateway now supports WebSocket mode for the OpenAI Responses API. You can keep a persistent connection open and continue each turn by sending only new input items plus previous_response_id, instead of re-sending the full context over a fresh HTTP request every turn. OpenAI reports up to ~40% faster end-to-end execution on WebSockets for agentic rollouts with 20 or more tool calls.

## Key Takeaways

- Copy link to headingRoute Responses API traffic over WebSocket The Responses route opens at GET /v1/responses and accepts raw response.create frames over a persistent WebSocket connection.
- The mode is compatible with store=false and Zero Data Retention, and follows OpenAI's WebSocket mode specification upstream.
- import WebSocket from 'ws';const ws = new WebSocket('wss://ai-gateway.vercel.sh/v1/responses', { headers: { Authorization: `Bearer ${process.env.AI_GATEWAY_API_KEY}` },});ws.on('open', () => ws.send(JSON.stringify({ type: 'response.create', model: 'openai/gpt-5.6-sol', store: false, input: 'Pick a gemstone.',})));ws.on('message', (data) => { const event = JSON.parse(data); if (event.type === 'response.completed') { ws.send(JSON.stringify({ type: 'response.create', model: 'openai/gpt-5.6-sol', store: false, previous_response_id: event.response.id, input: 'Which gemstone did you pick?', })); }});See the AI Gateway documentation for setup and the full route list.

---
_Auto-generated daily digest entry._
