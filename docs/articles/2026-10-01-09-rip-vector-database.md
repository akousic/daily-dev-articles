# RIP, vector database

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 180
- **Published (UTC):** 2026-10-01 16:01
- **Original:** https://turbopuffer.com/blog/rip-vector-database

## Summary

We are changing turbopuffer's storage architecture to take search to the next level. turbopuffer v3 changes how documents and indexes are laid out, written, compacted, and queried in turbopuffer. It will allow us to make search faster in every respect — including text, regex, and vector search — but it also lays the foundation to move many more SQL queries to turbopuffer and make them fast.

## Key Takeaways

- turbopuffer launched as a serverless vector database (v1), highly specialized to the task of serving extremely cheap and reasonably fast vector searches.
- Object storage as the source of truth gave the economics, and tiered NVMe SSD/memory caches gave the performance.
- The value of these particular tradeoffs was validated by our earliest customers, including Cursor and Notion.

---
_Auto-generated daily digest entry._
