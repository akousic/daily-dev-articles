# Show HN: Needle2: 14MB agentic LLM for phones, wearables, smart home and robots

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 444
- **Published (UTC):** 2026-08-10 17:22
- **Original:** https://cactuscompute.com/needle

## Summary

Today we release Needle 2: an open 45M-parameter model for tool calling, device use and structured extraction. The whole model is a single 14MB binary that runs a full session in 28MB of RAM. It is built on our Simple Attention Network findings, compressed to CQ2-bit with Cactus Quants, and baked into its own engine.

## Key Takeaways

- On the tool call and mobile device use benchmarks, Needle 2 trades wins with other small models like FunctionGemma 270M, LFM2.5 230M and Apple FM, at 5× to 70× smaller, and 2 bits against their f16.
- Needle hits 500 tokens/sec decode speed on a Raspberry Pi 5, between 400–1,500 tokens/sec on VR devices like Meta Quest 3S and Apple Vision Pro, and ranges 300–700 on sub-$200 phones such as the Samsung A-Series.
- With a peak session RAM around 28MB, Needle runs on newer microcontrollers like ESP32-S3.

---
_Auto-generated daily digest entry._
