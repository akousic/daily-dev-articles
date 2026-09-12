# How Tailscale built a customer-facing model router on AI Gateway

- **Source:** Vercel
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-09-12 16:55
- **Original:** https://vercel.com/blog/how-tailscale-built-a-customer-facing-model-router-on-ai-gateway

## Summary

Copy link to headingTailscale on Vercel - Hundreds of AI models shipped to customers in-product - Model access granted and revoked by tailnet network identity - Went from model routing prototype to paying customers in months Tailscale connects a company's laptops, servers, cloud instances, and personal devices into one private network called a tailnet. Remy Guercio, who leads product for Aperture by Tailscale, describes it simply: "It's basically like a VPC that can span any cloud, on-prem, your house, and your phone." Aperture takes that same idea and applies it to AI. Instead of giving every employee, agent, or tool a separate provider API key, Aperture lets companies control model access through the tailnet itself.

## Key Takeaways

- Add someone to the network, and they can immediately use approved models.
- Remove them, and access disappears.
- Under the hood, Aperture is built on Vercel AI Gateway and Vercel Sandbox.

---
_Auto-generated daily digest entry._
