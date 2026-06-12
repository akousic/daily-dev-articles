# Scaling Security Insights: how we achieved a 10x increase in global scanning capacity

- **Source:** Cloudflare
- **Rank (today):** #6
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-06-12 16:51
- **Original:** https://blog.cloudflare.com/scaling-security-scans/

## Summary

Security Insights provides actionable security recommendations for every Cloudflare account. To find these insights, we perform regular scans for all accounts, zones, and DNS records, looking for potential security risks and misconfigurations. However, two key issues emerged.

## Key Takeaways

- First, our scans were too infrequent.
- Scans were only being performed every week or two, and therefore newly introduced security risks could remain undetected for up to two weeks.
- Second, automatic scanning was opt-in for many free plan accounts – meaning lots of accounts weren’t being scanned at all.

---
_Auto-generated daily digest entry._
