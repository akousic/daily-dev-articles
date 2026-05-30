# Google Cloud Suspends Railway's Production Account, Causing Eight-Hour Platform-Wide Outage

- **Source:** InfoQ
- **Rank (today):** #6
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-05-30 15:15
- **Original:** https://www.infoq.com/news/2026/05/railway-gcp-account-outage/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

Google Cloud's automated systems suspended Railway's production account on May 19, triggering an eight-hour platform-wide outage that took down the dashboard, API, all deployments, and all databases for the platform's 3 million users. The suspension was not triggered by anything Railway did. Google applied it as part of a broader automated action affecting multiple accounts, with no advance notice to individual customers.

## Key Takeaways

- Chandrika Khanduri and Cody De Arkland from Railway's engineering team write: We take full responsibility for the architectural decisions that allowed a single upstream provider action to cascade into a platform-wide outage.
- The cascade mechanism is the architecturally interesting part.
- Railway runs a mesh network across Google Cloud, AWS, and its own bare-metal infrastructure (Railway Metal).

---
_Auto-generated daily digest entry._
