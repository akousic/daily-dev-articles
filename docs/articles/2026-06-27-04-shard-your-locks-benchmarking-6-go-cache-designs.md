# Shard your locks: benchmarking 6 Go cache designs

- **Source:** Lobsters
- **Rank (today):** #4
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-06-27 07:40
- **Original:** https://strebkov.dev/posts/shard-your-locks/

## Summary

I built the same in-memory string → string cache six ways, using nothing but the Go standard library, and benchmarked them under read-heavy, balanced, and write-heavy load across 1 to 8 cores. The rankings flip depending on the workload — and one of the “obvious” answers gets slower the more cores you give it. TL;DR: Shard your locks.

## Key Takeaways

- A 256-way striped map (sharded) was the all-around winner — up to 8× faster than a single sync.Mutex at 8 cores — and it’s about 15 lines of code.
- sync.RWMutex, the reflexive fix for “reads are contended,” is a trap: it barely helps reads past two cores and is slower than a plain mutex for writes.
- The contenders | Cache | Idea | One-liner | |---|---|---| | naive | Plain map, no locking | Not thread-safe — concurrent writes crash the process.

---
_Auto-generated daily digest entry._
