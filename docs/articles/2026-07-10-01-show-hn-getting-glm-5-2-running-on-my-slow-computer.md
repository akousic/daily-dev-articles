# Show HN: Getting GLM 5.2 running on my slow computer

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 802
- **Published (UTC):** 2026-07-09 08:05
- **Original:** https://github.com/JustVugg/colibri

## Summary

Tiny engine, immense model. Run GLM-5.2 (744B-parameter MoE) on a consumer machine with ~25 GB of RAM — in pure C, with zero dependencies, by streaming experts from disk. $ ./coli chat 🐦 colibrì v1.0 — GLM-5.2 · 744B MoE · int4 · streaming CPU ✓ pronto in 32s · residente 9.9 GB › ciao!

## Key Takeaways

- 😊 Come posso aiutarti oggi?
- A 744B Mixture-of-Experts model activates only ~40B parameters per token — and only ~11 GB of those change from token to token (the routed experts).
- So: - the dense part (attention, shared experts, embeddings — ~17B params) stays resident in RAM at int4 (~9.9 GB); - the 21,504 routed experts (75 MoE layers × 256 experts + the MTP head, ~19 MB each at int4) live on disk (~370 GB) and are streamed on demand, with a per-layer LRU cache, an optional pinned hot-store, and the OS page cache as a free L2.

---
_Auto-generated daily digest entry._
