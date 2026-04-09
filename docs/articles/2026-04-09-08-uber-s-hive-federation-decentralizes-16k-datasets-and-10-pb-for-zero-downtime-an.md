# Uber’s Hive Federation Decentralizes 16K Datasets and 10+ PB for Zero-Downtime Analytics at Scale

- **Source:** InfoQ
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-04-09 15:43
- **Original:** https://www.infoq.com/news/2026/04/uber-hive-decentralized-data/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

Uber has redesigned its Hive data warehouse to decentralize more than 16,000 datasets totaling over 10 petabytes, addressing scalability, operational, and security challenges. Previously, a monolithic Hive instance housed all delivery business datasets under a single namespace, creating risks of cascading outages, resource contention, and governance bottlenecks. By federating Hive databases, Uber aims to maintain high availability, enforce least-privilege access, and allow domain-specific datasets to scale independently, providing teams with operational autonomy.

## Key Takeaways

- The migration leverages a pointer-based approach within the Hive Metastore, enabling datasets to be redirected to new HDFS locations without duplicating petabytes of data.
- Each dataset is copied once to a decentralized target location, then the original pointer is updated, ensuring that queries continue to function during migration.
- Vijayant Soni, engineer at Uber, explained, Updating a dataset pointer in HMS is a split-second operation, ensuring continuous functioning for critical workloads.

---
_Auto-generated daily digest entry._
