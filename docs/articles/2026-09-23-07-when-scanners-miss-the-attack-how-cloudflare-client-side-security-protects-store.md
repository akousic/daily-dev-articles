# When scanners miss the attack: how Cloudflare Client-Side Security protects storefronts

- **Source:** Cloudflare
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-09-23 18:21
- **Original:** https://blog.cloudflare.com/client-side-security-finds-4-malicious-campaigns/

## Summary

When scanners miss the attack: how Cloudflare Client-Side Security protects storefronts A modern storefront can look perfectly healthy while malicious JavaScript works underneath: siphoning affiliate revenue, hijacking searches and clicks, tampering with analytics, or asking a remote server what to execute next. Pages load, products appear, and checkout works — yet the browser may be quietly doing something the site owner never authorized. That is the blind spot our Client-Side Security machine learning (ML) model is built to expose.

## Key Takeaways

- This post follows four operations, spanning eight payloads, that our Page Shield ML uncovered in the wild.
- The detection of these malicious payloads was automated; humans verified each finding only after the system had flagged it.
- When we afterward reviewed the campaigns using security scanning tools, seven of the eight payloads were entirely absent from VirusTotal, and URLScan returned no malicious verdict for any of them.

---
_Auto-generated daily digest entry._
