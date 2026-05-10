# Replacing a 3 GB SQLite database with a 10 MB FST (finite state transducer) binary

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-05-10 06:42
- **Original:** https://til.andrew-quinn.me/posts/replacing-a-3-gb-sqlite-database-with-a-7-mb-fst-finite-state-trandsucer-binary/

## Summary

Note for numberphiles: all numbers have been rounded to their first significant digit, because I’m a fan of Rob Eastaway’s “zequals” method of getting to the point when it comes to estimation. It’s much more valuable to walk away with the heuristic “some dude got a 300x memory reduction by swapping out a database he hacked together for a tiny, static, specialized data structure that does exactly what he needs it to and no more.” I found myself with an increasingly rare opportunity to work this weekend on Taskusanakirja, also often called tsk , a Finnish-English dictionary with incremental search-as-you-type.1 Fundamentally this problem reduces down to prefix search, and the canonical solution for prefix search with autocomplete is to implement a trie. And this worked wonderfully for the first implementation of tsk , which was in Go (and which I have written about elsewhere and elsewhere and elsewhere).

## Key Takeaways

- With a few basic optimizations.
- To prevent matching on some single-digit percentage of the mid-six-figures number of words we were baking into the binary (it’s been a design goal from the start to ship the entire program as one .exe , one .app , or one statically linked binary), we set some limit of e.g.
- only the first 50 or 100 matches or so and then just memoized all of the 1-, 2-, and 3-character combinations, after which I’ve never noticed a perceptible delay in the program again after a year of heavy personal use.

---
_Auto-generated daily digest entry._
