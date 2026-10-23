# Vercel Connect adds managed Stripe API keys

- **Source:** Vercel
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-10-23 18:13
- **Original:** https://vercel.com/changelog/vercel-connect-adds-managed-stripe-api-keys

## Summary

Vercel Connect can now create a separate restricted Stripe API key for each agent or task. When you create a Stripe connector, you can now choose Managed API Key as the connection method. Vercel creates the key in your Stripe account, limited to the permissions you pick.

## Key Takeaways

- The existing MCP and bring-your-own API key methods are unchanged.
- Most apps and agents run on Stripe’s default secret key, which has full access to the account.
- With per-agent keys, each agent gets only the access its job needs.

---
_Auto-generated daily digest entry._
