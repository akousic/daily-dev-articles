# PgQue: Zero-Bloat Postgres Queue

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 131
- **Published (UTC):** 2026-04-18 16:50
- **Original:** https://github.com/NikolayS/pgque

## Summary

Zero-bloat Postgres queue. One SQL file to install, pg_cron to tick. Discussion on Hacker News.

## Key Takeaways

- For teams who want a durable event stream inside Postgres.
- The model is closer to Kafka (log) than to ActiveMQ or RabbitMQ (task message queue).
- Shared event log, independent per-consumer cursors, zero bloat under sustained load.

---
_Auto-generated daily digest entry._
