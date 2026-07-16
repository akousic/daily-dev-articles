# Improving Smart Tiered Cache for Public Cloud Regions

- **Source:** Cloudflare
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-07-16 15:41
- **Original:** https://blog.cloudflare.com/smart-tiered-cache-for-public-clouds/

## Summary

Improving Smart Tiered Cache for Public Cloud Regions In 2021, we shipped Smart Tiered Cache. The idea: for each origin behind your site, Cloudflare picks the single best upper-tier data center to route through, based on real-time latency. Flip one switch, and we find the fastest path from our network to your origin.

## Key Takeaways

- That works as long as an origin IP lives in one fixed place.
- Public cloud origins usually don't.
- They sit behind anycast or regional unicast front ends, so one origin IP can look equally close to a dozen Cloudflare data centers at once — and the latency probes have nothing to lock onto.

---
_Auto-generated daily digest entry._
