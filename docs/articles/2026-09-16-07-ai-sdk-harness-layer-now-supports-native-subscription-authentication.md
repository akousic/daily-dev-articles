# AI SDK harness layer now supports native subscription authentication

- **Source:** Vercel
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-09-16 18:06
- **Original:** https://vercel.com/changelog/ai-sdk-harness-native-subscription-authentication

## Summary

The AI SDK harness layer now supports authenticating harnesses through their native subscriptions, where the underlying harness supports them. The harness layer runs different coding agents through the same HarnessAgent interface, so you can switch agents without changing your application code. No code changes or new settings are required.

## Key Takeaways

- The direct authentication mode uses explicit provider environment credentials when they are present, and otherwise a native subscription found on the host.
- The default auto mode does the same when no AI Gateway credentials are set.
- The ai-gateway mode never reads native subscriptions.

---
_Auto-generated daily digest entry._
