# Etsy Migrates 1000-Shard, 425 TB MySQL Sharding Architecture to Vitess

- **Source:** InfoQ
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-04-12 14:49
- **Original:** https://www.infoq.com/news/2026/04/etsy-vitess-sharding-migration/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

The Etsy engineering team recently described how the company migrated its long-running MySQL sharding infrastructure to Vitess. The transition moved shard routing from Etsy’s internal systems to Vitess using vindexes, enabling capabilities such as resharding data and sharding previously unsharded tables. An open source database clustering system for horizontally scaling MySQL, Vitess was initially introduced as a layer between the ORM (Object-Relational Mapping) and the database, routing queries through it.

## Key Takeaways

- At the same time, the ORM continued to specify the target shard.
- In Vitess, vindexes define how application data maps to database shards and how queries are routed across them.
- Ella Yarmo-Gray, senior software engineer at Etsy, explains the challenge Etsy faced: With this new infrastructure in place, we were ready to start exploring vindexes, which define sharding strategies within Vitess (...) Since the ORM’s shard mappings are random and not algorithmic, using one of these out-of-the-box would require re-sharding all of our data – a process that would be manual and likely take years.

---
_Auto-generated daily digest entry._
