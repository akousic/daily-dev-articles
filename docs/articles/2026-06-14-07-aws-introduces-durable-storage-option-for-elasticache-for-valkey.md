# AWS Introduces Durable Storage Option for ElastiCache for Valkey

- **Source:** InfoQ
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-06-14 15:51
- **Original:** https://www.infoq.com/news/2026/06/elasticache-valkey-durability/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

AWS has recently introduced durability for Amazon ElastiCache for Valkey, enabling reliable data retention across failures and expanding support beyond caching to persistent workloads. The feature offers new options that prioritize either minimizing data loss or maintaining lower write latency, expanding the range of use cases supported by the Redis fork, including AI memory, session storage, and real-time applications. ElastiCache for Valkey now supports both caching and persistent data workloads.

## Key Takeaways

- Developers can choose synchronous durability to minimize data loss during failures, or asynchronous durability for lower latency.
- Traditional ElastiCache without durability remains the default and cheapest option for caching scenarios where data can be rebuilt from source.
- Jules Lasarte, software engineer at AWS, and Karthik Konaparthi, principal product manager at AWS, explain: Many organizations find that Multi-AZ replication and automatic failover in ElastiCache meet their resilience requirements, but as customers increasingly adopt ElastiCache as a persistent data store, as well as a cache, data loss becomes a primary concern.

---
_Auto-generated daily digest entry._
