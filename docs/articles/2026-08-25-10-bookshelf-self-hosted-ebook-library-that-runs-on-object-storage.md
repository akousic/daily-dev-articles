# Bookshelf – Self-hosted eBook library that runs on object storage

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 142
- **Published (UTC):** 2026-08-24 23:00
- **Original:** https://github.com/murerkinn/bookshelf

## Summary

A self-hosted library for the ebooks you already own. One server-rendered page lists them, filters them with a search box, serves downloads, and reads them in the browser — EPUB and PDF, each with its own reader — as a Cloudflare Worker over R2, or as a Node server over a directory on disk. Everything above is npm run demo — a generated shelf of public-domain titles, so the screenshots can be reproduced without finding books first.

## Key Takeaways

- Node 24 or newer, and a Unix-like system: the sync tool finds its image tools with which, so Windows is not supported.
- Covers come out better with cwebp and pdftoppm installed — see publishing, or use Docker, which ships both.
- git clone https://github.com/murerkinn/bookshelf.git cd bookshelf npm install Put some books — EPUB or PDF — in books/, then choose where the library should live.

---
_Auto-generated daily digest entry._
