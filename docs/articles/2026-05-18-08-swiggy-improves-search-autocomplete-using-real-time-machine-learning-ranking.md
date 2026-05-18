# Swiggy Improves Search Autocomplete Using Real Time Machine Learning Ranking

- **Source:** InfoQ
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-05-18 16:50
- **Original:** https://www.infoq.com/news/2026/05/swiggy-autocomplete-rt-ranking/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

Swiggy detailed the architecture of the company's real-time machine-learning ranking system for autocomplete search suggestions, describing how the platform combines OpenSearch retrieval, feature stores, and learning-to-rank models while operating under strict latency requirements. The system replaced a hand-tuned heuristic ranking approach with a learned ranking model running directly inside OpenSearch, avoiding additional services or network hops while improving autocomplete relevance. According to the company, autocomplete requests are particularly sensitive to latency because every keystroke can trigger a new search query.

## Key Takeaways

- Traditional autocomplete systems, therefore, tend to rely on lexical matching and static ranking rules optimized for speed.
- Swiggy's newer approach separates the workflow into two stages: candidate generation and ranking.
- When a user begins typing, the system first retrieves a broad set of candidate suggestions using OpenSearch lexical retrieval combined with embedding-based similarity search.

---
_Auto-generated daily digest entry._
