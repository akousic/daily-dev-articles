# We gave terabytes of CI logs to an LLM

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 203
- **Published (UTC):** 2026-02-27 15:41
- **Original:** https://www.mendral.com/blog/llms-are-good-at-sql

## Summary

Last week, our agent traced a flaky test to a dependency bump three weeks prior. It did this by writing its own SQL queries, scanning hundreds of millions of log lines across a dozen queries, and following a trail from job metadata to raw log output. The whole investigation took seconds.

## Key Takeaways

- To do this, the agent needs context: not one log file, but every build, every test, every log line, across months of history.
- Every week, about 1.5 billion CI log lines and 700K jobs flow through our system.
- All of it lands in ClickHouse, compressed at 35:1.

---
_Auto-generated daily digest entry._
