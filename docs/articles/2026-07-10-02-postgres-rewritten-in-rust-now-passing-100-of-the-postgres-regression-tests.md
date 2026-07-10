# Postgres rewritten in Rust, now passing 100% of the Postgres regression tests

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 764
- **Published (UTC):** 2026-07-09 06:18
- **Original:** https://github.com/malisper/pgrust

## Summary

A Postgres rewrite in Rust. pgrust targets compatibility with Postgres 18.3 and matches Postgres's expected output across more than 46,000 regression queries. pgrust is disk compatible with Postgres and can boot from an existing Postgres 18.3 data directory.

## Key Takeaways

- The goal is to make Postgres easier to change from the inside: keep the behavior Postgres-shaped, keep the real Postgres tests as the oracle, and use Rust plus AI-assisted programming to explore deeper server changes.
- Update: We're working on a new not yet published version of pgrust that currently passes 100% of Postgres regression suite, has a thread per connection model instead of process per connection, is 50% faster than Postgres on transaction workloads, and is ~300x faster than Postgres on analytical workloads (2x slower than Clickhouse on clickbench and we think it can get faster than Clickhouse).
- Follow pgrust or join our Discord for updates!

---
_Auto-generated daily digest entry._
