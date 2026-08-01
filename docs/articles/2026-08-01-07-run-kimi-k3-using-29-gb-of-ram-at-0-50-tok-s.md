# Run Kimi K3 using 29 GB of RAM at 0.50 tok/s

- **Source:** Hacker News
- **Rank (today):** #7
- **Ranking metrics:** HN score 289
- **Published (UTC):** 2026-07-31 14:12
- **Original:** https://github.com/sqliteai/waste

## Summary

Kimi K3 — 2.78 trillion parameters — running on a consumer laptop. $ waste run ~/models/k3.waste 'What is the capital of Italy?' waste: no --budget, using 46.24 GB of 64.00 GB (expert cache 17.56 GB) The capital of Italy is **Rome**. [16 tokens, 25.78 s, 0.62 tok/s | experts 9038 hit / 14514 miss = 38%] WASTE is an embeddable inference engine written in C, with no third-party runtime dependencies.

## Key Takeaways

- It keeps the model trunk in memory, streams selected experts directly from disk, and uses the remaining RAM as a bounded expert cache.
- Its current proof point is the complete open-weights Kimi K3 model: 2.78 trillion parameters, converted into a 982 GiB container and running on a 64 GB MacBook Pro at 0.45–0.62 tokens per second.
- This is not a distilled, pruned, or reduced variant.

---
_Auto-generated daily digest entry._
