# Inside Atlassian’s Forge Billing Architecture for Distributed Usage Tracking at Scale

- **Source:** InfoQ
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-06-20 15:48
- **Original:** https://www.infoq.com/news/2026/06/forge-billing-usage-platform/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

Atlassian has described the engineering behind its Forge billing platform, a system built to support usage-based pricing across its cloud application development ecosystem. Forge is Atlassian’s serverless extensibility platform used to build apps for products such as Jira and Confluence, and the billing system is responsible for translating distributed usage signals into accurate financial records at scale. The platform emerged as Forge evolved from a simple extension model into a usage-driven ecosystem where billing depends on fine-grained signals such as function invocations, storage consumption, and operational telemetry.

## Key Takeaways

- This shift required Atlassian to build a system capable of collecting high-volume events from independent services, ensuring they are consistently validated, attributed to the correct tenant context, and transformed into billing-ready records without duplication or loss, while still supporting near real-time visibility for developers.
- At a high level, the architecture consists of Forge services emitting usage events, a centralized ingestion and streaming layer, a usage tracking system, and downstream billing and commerce systems.
- Each Forge service produces structured events using a shared schema, ensuring consistent interpretation across downstream consumers regardless of origin.

---
_Auto-generated daily digest entry._
