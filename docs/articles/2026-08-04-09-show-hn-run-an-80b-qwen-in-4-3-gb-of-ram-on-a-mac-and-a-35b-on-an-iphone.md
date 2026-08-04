# Show HN: Run an 80B Qwen in 4.3 GB of RAM on a Mac, and a 35B on an iPhone

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 271
- **Published (UTC):** 2026-08-03 16:54
- **Original:** https://github.com/leonickson1/Swiftlet

## Summary

Run 35B and 80B Qwen models on ordinary Apple devices, including iPhones. Swiftlet is a Swift + Metal runtime for the Qwen3-Next and Qwen3.5/3.6 MoE hybrid model family. It keeps only the small dense core of a model resident in memory and streams the routed Mixture-of-Experts weights from storage on demand.

## Key Takeaways

- The result: | Model | Disk | Peak RAM | Decode speed (M5 Mac) | |---|---|---|---| | Qwen3.6-35B-A3B, 4-bit | 18 GB | 2.6 GB | 7 to 11 tok/s | | Qwen3-Next-80B-A3B, 4-bit | 42 GB | 4.3 GB | 4.5 to 5 tok/s | The 35B also runs on an iPhone 17 in about 2.5 GB of RAM, at about 1 tok/s today.
- Credit where due: ANEMLL showed a 397B MoE streaming on an iPhone 17 Pro as a proof of concept in early 2026.
- Swiftlet's aim is the next step, making this class of model an installable app on a base iPhone, with an open runtime anyone can build on.

---
_Auto-generated daily digest entry._
