# Show HN: Honker – Postgres NOTIFY/LISTEN Semantics for SQLite

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 126
- **Published (UTC):** 2026-04-23 11:53
- **Original:** https://github.com/russellromney/honker

## Summary

honker is a SQLite extension + language bindings that add Postgres-style NOTIFY /LISTEN semantics to SQLite, with built-in durable pub/sub, task queue, and event streams, without client polling or a daemon/broker. Any language that can SELECT load_extension('honker') gets the same features. honker ships as a Rust crate (honker , plus honker-core /honker-extension ), a SQLite loadable extension, and language packages: Python (honker ), Node (@russellthehippo/honker-node ), Bun (@russellthehippo/honker-bun ), Ruby (honker ), Go, Elixir, C++.

## Key Takeaways

- The on-disk layout is defined once in Rust; every binding is a thin wrapper around the loadable extension.
- honker works by replacing a polling interval with event notifications on SQLite's WAL file, achieving push semantics and enabling cross-process notifications with single-digit millisecond delivery.
- SQLite is increasingly the database for shipped projects.

---
_Auto-generated daily digest entry._
