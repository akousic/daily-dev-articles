# pg_durable: Microsoft open sources in-database durable execution

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 437
- **Published (UTC):** 2026-06-05 15:59
- **Original:** https://github.com/microsoft/pg_durable

## Summary

Long-running, fault-tolerant SQL functions for teams that already keep their state in Postgres and want to stop stitching together cron jobs, workers, queues, and status tables to make background work reliable. Define the workflow in SQL, let pg_durable checkpoint each step, and resume after crashes, restarts, or failed steps. Durable execution is now a standard industry pattern, and pg_durable brings it inside Postgres with no extra service infrastructure required.

## Key Takeaways

- Part of our mission to bring compute close to data.
- Try pg_durable now in Azure HorizonDB, Microsoft's new PostgreSQL cloud service engineered for performance and built with pg_durable inside - Backend and data engineers who want workflows to live next to the data they touch.
- - DBAs and SREs automating runbooks that must survive restarts and be auditable in SQL.

---
_Auto-generated daily digest entry._
