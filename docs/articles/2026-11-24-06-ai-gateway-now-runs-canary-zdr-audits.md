# AI Gateway now runs canary ZDR audits

- **Source:** Vercel
- **Rank (today):** #6
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-11-24 01:35
- **Original:** https://vercel.com/changelog/ai-gateway-now-runs-canary-zdr-audits

## Summary

AI Gateway now runs canary audits against inference providers to detect when prompt content is read outside the inference path. Contractual Zero Data Retention (ZDR) agreements and point-in-time security audits establish how a provider should handle your data, but production infrastructure changes continuously. Canary audits add a detection layer on top.

## Key Takeaways

- Each canary audit run: - Mints unique URLs that exist nowhere else, each mapped privately to a specific provider, model, and audit run.
- - Sends prompts containing those URLs through the normal inference path, with ZDR requested for covered providers and non-ZDR pairs included as positive controls.
- - Watches for traffic.

---
_Auto-generated daily digest entry._
