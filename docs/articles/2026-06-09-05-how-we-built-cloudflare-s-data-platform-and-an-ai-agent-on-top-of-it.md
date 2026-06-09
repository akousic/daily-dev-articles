# How we built Cloudflare's data platform and an AI agent on top of it

- **Source:** Cloudflare
- **Rank (today):** #5
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-06-09 16:34
- **Original:** https://blog.cloudflare.com/our-unified-data-platform/

## Summary

Cloudflare processes more than a billion events every second. Our network spans 330+ cities in 120+ countries. Behind every HTTP request, every Worker invocation, every R2 read operation, there is data, and a lot of it.

## Key Takeaways

- For years, that data was not very easy to access.
- It lived in dozens of production databases, ClickHouse clusters, Kafka streams, Google Cloud buckets, BigQuery datasets, and a long tail of pipelines.
- To answer a simple question like "How many domains that signed up today are in the Top 100 by traffic?", an analyst at Cloudflare had to know which system to ask, what credentials to use, what query language to write, and whether the data they were looking at was sampled, fresh, or seven-days stale.

---
_Auto-generated daily digest entry._
