# From Minutes to Seconds: Uber Boosts MySQL Cluster Uptime with Consensus Architecture

- **Source:** InfoQ
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-03-11 14:56
- **Original:** https://www.infoq.com/news/2026/03/uber-mysql-uptime-consensus/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

Uber redesigned its MySQL infrastructure to improve cluster uptime, replacing external failover with MySQL Group Replication(MGR). Applied across thousands of clusters, the change reduces failover from minutes to seconds while maintaining strong consistency. The redesign began by introducing consensus replication to remove external dependencies, and was scaled fleet‑wide with automated onboarding, node management, rebalancing, and safeguards to ensure quorum and operational reliability.

## Key Takeaways

- Previously, Uber ran MySQL clusters in a single-primary, asynchronous replica model.
- External systems detected failures and promoted replicas, resulting in failover times measured in minutes.
- To reduce downtime and improve reliability, Uber adopted MySQL Group Replication, a Paxos-based consensus protocol.

---
_Auto-generated daily digest entry._
