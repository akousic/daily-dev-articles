# Cloudflare Tests Cache Transcoding to Reduce Storage Requirements

- **Source:** InfoQ
- **Rank (today):** #6
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-09-13 17:22
- **Original:** https://www.infoq.com/news/2026/09/cloudflare-cache-transcoding/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

Cloudflare recently described a prototype called Cache Transcoding that compresses eligible cache content, mainly uncompressed text such as HTML, JSON, CSS, and JavaScript, using Zstandard before storing it on disk. The hyperscaler estimates that the approach could provide petabytes of additional effective cache capacity, although broader testing is still needed. According to the article, the additional processing required is relatively small, as the content is compressed once when it enters the cache and decompressed when served.

## Key Takeaways

- Compression reduced the size of eligible content by about 2.8 times, allowing existing servers to store more data and reducing the amount of data transferred between data centers.
- To achieve this, Cloudflare relies on Zstandard, the lossless compression algorithm developed by Facebook for real-time use, together with Pingora, its Rust-based proxy framework.
- Aashi Patel writes: A small increase in CPU gives Cloudflare petabytes of effective cache capacity and reduces the data transferred between our data centers.

---
_Auto-generated daily digest entry._
