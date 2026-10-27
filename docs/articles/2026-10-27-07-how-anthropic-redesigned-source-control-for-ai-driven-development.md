# How Anthropic Redesigned Source Control for AI-Driven Development

- **Source:** InfoQ
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-10-27 19:19
- **Original:** https://www.infoq.com/news/2026/10/anthropic-source-control/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

Anthropic recently detailed how it migrated its monorepo from Git to Scion. Scion is a source control system that moves repository operations to the server side and uses content-addressed storage and tiered caches for agent and CI workloads. The design sacrifices offline independence for less local data and shared infrastructure.

## Key Takeaways

- In its 13 October engineering post, Anthropic reported that daily merged changes rose from around 2,500 in May to more than 30,000 in September.
- Its CI systems perform approximately 25 million checkouts daily, against a monorepo with nearly 100 GB of main-branch history and a compressed working copy exceeding 25 GB.
- The company had used shallow clones, sparse checkouts, promisor remotes, repository snapshots and several hundred Git mirrors, but said these became harder to operate as merge rates increased.

---
_Auto-generated daily digest entry._
