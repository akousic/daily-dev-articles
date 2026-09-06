# Debian Code Search: Fast TurboPFor with Go SIMD

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-09-06 02:03
- **Original:** https://michael.stapelberg.ch/posts/2026-09-06-dcs-fast-turbopfor-go-simd/

## Summary

Table of contents This August, I accomplished what I wanted for many years: I deleted the last cgo dependency in Debian Code Search! This was made possible by Go’s recently introduced SIMD support, because now we can implement the TurboPFor integer compression format as efficiently — more efficiently, in fact, by using the newer AVX512 instruction set! — as the reference implementation.

## Key Takeaways

- Background: Why does DCS need a fast Integer Codec?
- Debian Code Search (DCS) is a search engine that allows searching all the Open Source source code within Debian, with either literal search expressions or regular expression search queries.
- A search engine uses an inverted index: a map from term to documents containing the term.

---
_Auto-generated daily digest entry._
