# PostgreSQL 19 Released with Online Table Repacking and Query Planning Controls

- **Source:** InfoQ
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-11-22 20:38
- **Original:** https://www.infoq.com/news/2026/11/postgresql-19-released/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

The PostgreSQL Global Development Group released PostgreSQL 19, introducing changes to database maintenance, query planning, replication, and application development. The release focuses on reducing administrative overhead and improving performance, with new tools for reorganizing tables without downtime and controlling query plans. One of the main additions is REPACK, which reclaims unused table space and can reorder data to match an index.

## Key Takeaways

- Its CONCURRENTLY option allows the operation to run without blocking reads or writes, making it a potential replacement for common uses of VACUUM FULL and CLUSTER.
- PostgreSQL 19 also introduces pg_plan_advice and pg_stash_advice, extensions that let administrators influence query plan selection and apply stored advice to queries by identifier, without changing application code.
- Other maintenance improvements include parallel index vacuuming, changes to autovacuum prioritization, and additional monitoring views.

---
_Auto-generated daily digest entry._
