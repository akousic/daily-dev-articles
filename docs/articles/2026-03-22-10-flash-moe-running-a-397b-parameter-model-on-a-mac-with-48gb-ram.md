# Flash-Moe: Running a 397B Parameter Model on a Mac with 48GB RAM

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 134
- **Published (UTC):** 2026-03-22 11:30
- **Original:** https://github.com/danveloper/flash-moe

## Summary

Read the paper — Full technical details, 90+ experiments, and the story of how an AI and a human built this in 24 hours. Pure C/Metal inference engine that runs Qwen3.5-397B-A17B (a 397 billion parameter Mixture-of-Experts model) on a MacBook Pro with 48GB RAM at 4.4+ tokens/second with production-quality output including tool calling. The entire 209GB model streams from SSD through a custom Metal compute pipeline.

## Key Takeaways

- Just C, Objective-C, and hand-tuned Metal shaders.
- | Configuration | tok/s | Quality | Notes | |---|---|---|---| | 4-bit experts, FMA kernel | 4.36 | Excellent | Current best.
- | | 4-bit experts, baseline | 3.90 | Excellent | Before FMA kernel optimization.

---
_Auto-generated daily digest entry._
