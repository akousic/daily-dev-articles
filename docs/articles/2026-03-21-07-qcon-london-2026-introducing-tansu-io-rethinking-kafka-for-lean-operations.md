# QCon London 2026: Introducing Tansu.io — Rethinking Kafka for Lean Operations

- **Source:** InfoQ
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-03-21 14:35
- **Original:** https://www.infoq.com/news/2026/03/tansu-stateless-kafka-compatible/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

At QCon London 2026, Peter Morgan introduced Tansu, an open-source, Apache Kafka-compatible messaging broker he has been building solo for the past two years. The pitch was simple and deliberately provocative: what if you kept Kafka's protocol, however, threw out everything else, the replication, the leader elections, the permanent broker state, and replaced it with stateless brokers that delegate durability entirely to external storage? Morgan, who has spent over a decade building event-driven systems on top of Kafka, including platforms for Disney's MagicBand and large-scale betting systems, opened with the core assumption that separates Tansu from Kafka.

## Key Takeaways

- Kafka achieves resilience by replicating data between brokers.
- Tansu assumes that storage is already durable and resilient, and builds everything from that premise.
- The practical consequences are significant.

---
_Auto-generated daily digest entry._
