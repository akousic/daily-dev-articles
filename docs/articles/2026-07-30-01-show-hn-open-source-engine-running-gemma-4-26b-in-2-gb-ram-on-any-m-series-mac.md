# Show HN: Open-source engine running Gemma 4 26B in 2 GB RAM on any M-series Mac

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 861
- **Published (UTC):** 2026-07-29 15:05
- **Original:** https://github.com/drumih/turbo-fieldfare

## Summary

Gemma 4 26B-A4B inference in about 2 GB of RAM A custom Swift + Metal runtime for any Apple Silicon Mac, even the 8 GB ones. Quick start · Local server · Benchmarks · Contribute results · How it works · Experiments · References Memory got expensive. So I gave a 26-billion-parameter model a ~2 GB budget.

## Key Takeaways

- TurboFieldfare runs the instruction-tuned Gemma 4 26B-A4B without loading the entire 14.3 GB model into memory.
- It keeps the shared 1.35 GB core and FP16 KV cache in memory, then streams only the experts needed for each token from SSD.
- This is what lets the model run on Macs with 8 GB of RAM.

---
_Auto-generated daily digest entry._
