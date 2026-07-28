# Regional inference now available on AI Gateway

- **Source:** Vercel
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-07-28 16:07
- **Original:** https://vercel.com/changelog/regional-inference-now-available-on-ai-gateway

## Summary

AI Gateway now supports regional inference. Set inferenceRegion on a request to pin it to the US or EU. Every model provider that supports the selected region handles it the same way.

## Key Takeaways

- Inference runs there, and any data the provider keeps is stored there.
- AI Gateway supports two pinned regions, plus global routing: If no model provider can serve it, the request fails rather than running somewhere else.
- Every response reports the region that served it, so you can confirm where each request ran.

---
_Auto-generated daily digest entry._
