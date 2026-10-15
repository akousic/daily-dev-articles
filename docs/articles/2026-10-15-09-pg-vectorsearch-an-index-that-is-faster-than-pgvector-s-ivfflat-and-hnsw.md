# Pg_vectorsearch: An index that is faster than pgvector's IVFFlat and HNSW

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 206
- **Published (UTC):** 2026-10-14 11:47
- **Original:** https://github.com/timescale/pg_vectorsearch

## Summary

A PostgreSQL extension for high-performance approximate nearest neighbor (ANN) search. Meant for testing, not production. Upgrading between prereleases may not be possible; plan to drop and recreate the extension and its indexes.

## Key Takeaways

- See the changelog for known issues.
- - PRISM index (100M+ vectors) — IVF-style, with hierarchical routing - RaBitQ quantization with theoretical error bounds for two-stage search - SIMD-optimized distance computation (AVX2, AVX512, NEON) - Dynamic updates — inserts, updates and deletes, with posting-list splits via prism_rebalance (see Maintenance) - pgvector compatible — index existing vector and halfvec columns as-is (see Existing pgvector tables) PRISM (Partitioned Routing Index for Similarity Matching) is a PostgreSQL-native index access method that is conceptually similar to pgvector's IVFFlat, but it is built around state-of-the-art quantization, routing, and partitioning techniques.
- It is implemented in C for high performance and seamless integration with PostgreSQL.

---
_Auto-generated daily digest entry._
