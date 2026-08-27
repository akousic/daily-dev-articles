# Show HN: We built open OpenRouter that turns usage into a better model

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 65
- **Published (UTC):** 2026-08-27 21:18
- **Original:** https://github.com/experientiallabs/experiential

## Summary

Experiential is an open source gateway and router for agent workflows: - Use hosted, BYOK, and local models through one OpenAI-compatible API. - Control which users and agents can use which models, for which use cases, and how much they can spend. - Turn production traffic into a custom router or model optimized for quality, speed, and cost.

## Key Takeaways

- Start a local OpenAI-compatible gateway.
- On first run, the setup wizard uses the shared provider, model, and reasoning-effort selectors, persists every selected provider connection, then shows defaults for the public alias, identity, and $50.00 command budget before printing a one-time key: pip install experiential exp Choose a public alias such as opus-5, capture the issued key, and send a request: export EXP_GATEWAY_KEY=...
- curl http://127.0.0.1:8000/v1/chat/completions \ -H "Authorization: Bearer $EXP_GATEWAY_KEY" \ -H 'Content-Type: application/json' \ -d '{"model":"opus-5","messages":[{"role":"user","content":"Help me"}]}' Prefer a managed gateway to running one locally?

---
_Auto-generated daily digest entry._
