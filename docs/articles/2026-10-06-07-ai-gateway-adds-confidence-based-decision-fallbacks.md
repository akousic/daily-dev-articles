# AI Gateway adds confidence-based decision fallbacks

- **Source:** Vercel
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-10-06 19:24
- **Original:** https://vercel.com/changelog/confidence-based-decision-fallbacks

## Summary

AI Gateway can now escalate a decision request to a fallback model when the primary model's answer trips a confidence condition you set. Conditions can be combined, so an escalation can depend on more than one signal. The plain model names you already list in models keep catching outright errors, so existing fallbacks are unaffected.

## Key Takeaways

- Confidence conditions cover Choice and Score questions.
- Boolean questions escalate on a probability range instead.
- Set the fallback by adding one conditional object to providerOptions.gateway.models.

---
_Auto-generated daily digest entry._
