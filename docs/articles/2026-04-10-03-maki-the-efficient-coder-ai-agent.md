# maki - the efficient coder (AI agent)

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-04-10 02:35
- **Original:** https://maki.sh/

## Summary

Context efficiencyWhere tokens go Parses 15 languages into skeletons: imports, type defs, function signatures with their line ranges. Adds 59 tok/turn but saves 224 tok/turn on reads, netting 165 tok/turn saved. My usage indicated reads are ~65% of all tokens, so this optimization is big.

## Key Takeaways

- A sandboxed Python interpreter with memory and time limits.
- All tools are exposed as async functions, so the model can asyncio.gather() a bunch of reads, grep the results, and only return what matters.
- Intermediate data never reaches your context.

---
_Auto-generated daily digest entry._
