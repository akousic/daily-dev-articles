# GLM-5.3 is 50% off through DigitalOcean on AI Gateway

- **Source:** Vercel
- **Rank (today):** #9
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-09-03 17:46
- **Original:** https://vercel.com/changelog/glm-5-3-is-50-off-through-digitalocean-on-ai-gateway

## Summary

GLM-5.3 is 50% off on AI Gateway through Tuesday, September 8, in partnership with DigitalOcean. Copy link to headingHow to use the model during the offer period - Using the promo name ( zai/glm-5.3-promo-50 ) gets the discounted rate. It routes only to DigitalOcean, with no fallback to another provider, and it stops serving when the offer ends.

## Key Takeaways

- - Using the standard name (i.e., zai/glm-5.3 ) with provider options to sort DigitalOcean as the preferred provider keeps working after September 8 and routes across every provider that serves the model, at their usual rates.
- import { streamText } from 'ai'; const result = streamText({ model: 'zai/glm-5.3-promo-50', prompt: 'Add error recovery to the data ingestion pipeline.',}); Because the promo name goes away when the offer ends, treat it as something you switch on for the window rather than hardcode.
- To keep the standard name in your code instead, pin the provider with order: ['digitalocean'] under providerOptions.gateway, which prefers DigitalOcean and falls back to the others if it cannot serve the request.

---
_Auto-generated daily digest entry._
