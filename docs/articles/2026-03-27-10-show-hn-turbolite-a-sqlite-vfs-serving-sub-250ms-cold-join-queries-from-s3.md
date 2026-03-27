# Show HN: Turbolite – a SQLite VFS serving sub-250ms cold JOIN queries from S3

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 148
- **Published (UTC):** 2026-03-26 18:58
- **Original:** https://github.com/russellromney/turbolite

## Summary

turbolite is a SQLite VFS in Rust that serves point lookups and joins directly from S3 with sub-250ms cold latency. It also offers page-level compression (zstd) and encryption (AES-256) for efficiency and security at rests, which can be used separately from S3. turbolite is experimental.

## Key Takeaways

- It is new and contains bugs.
- It may corrupt your data.
- Object storage is getting fast.

---
_Auto-generated daily digest entry._
