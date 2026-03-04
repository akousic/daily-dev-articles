# Rust zero-cost abstractions vs. SIMD

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-03-03 14:00
- **Original:** https://turbopuffer.com/blog/zero-cost

## Summary

We reduced the latency on a full-text search query from 220ms → 47ms by looking under the hood of Rust’s “zero-cost” iterators to find that they were silently preventing vectorization. This post serves as a reminder that zero-cost abstractions do not absolve you from practicing mechanical sympathy. avg latency, filtered BM25 query, 5 million documents ░░░░ 220 ms ░░░░ ░░░░ ░░░░ ░░░░ ░░░░ ░░░░ ░░░░ ░░░░ ░░░░ ░░░░ ▓▓▓▓ 47 ms ░░░░ ▓▓▓▓ ░░░░ ▓▓▓▓ ══════ ══════ before after Several months ago, one of our customers was struggling with high latency on a full-text (BM25) query that does a bunch of permissions checks, with up to thousands of permissions identifiers passed in a ContainsAny filter.

## Key Takeaways

- Something like this: { "filters": ["attribute", "ContainsAny", ["a", "c", "f", "j", "m", "o", "t", "x", "z", ...]], "rank_by": ["text", "BM25", "some query string"] } Filtered BM25 queries such as this are common on turbopuffer, routinely taking less than 50ms over millions of documents.
- This one seemed innocuous, yet it was taking over 4× that long.
- Examining the query profiles revealed something interesting: only about 10ms was being spent on the actual BM25 ranking; the rest (>200ms) was being spent evaluating filters.

---
_Auto-generated daily digest entry._
