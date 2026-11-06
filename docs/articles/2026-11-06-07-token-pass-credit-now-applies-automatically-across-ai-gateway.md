# Token Pass credit now applies automatically across AI Gateway

- **Source:** Vercel
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-11-06 20:20
- **Original:** https://vercel.com/changelog/token-pass-credit-now-applies-automatically-across-ai-gateway

## Summary

Token Pass credit now applies automatically to included model usage through AI Gateway, whether a request authenticates with an API key, OIDC token, or fx login. No dedicated Token Pass API key is required, though you can still create one from the dashboard or the CLI for keys scoped only to featured models and providers. When Token Pass credit runs out for the billing period, requests from a standard key or OIDC token fall back to your team's AI Gateway credits.

## Key Takeaways

- Token Pass keys still stop until the next billing period.
- Requests served through the Token Pass provider remain Zero Data Retention (ZDR).
- Fallback requests follow your team's setting.

---
_Auto-generated daily digest entry._
