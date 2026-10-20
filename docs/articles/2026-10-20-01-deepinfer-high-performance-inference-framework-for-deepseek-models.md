# DeepInfer: High-performance inference framework for DeepSeek models

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 1897
- **Published (UTC):** 2026-10-20 09:08
- **Original:** https://github.com/deepseek-ai/DeepInfer

## Summary

DeepInfer is the high-performance inference framework that powers DeepSeek's large-scale production services. This open-source release provides offline inference with the core features needed for serving at scale. Supported models: - DeepSeek-V4.1-Flash Supported features: - Optimized kernels, model and sampler runtime - Parallelism: Attention DP / balanced CP, MoE EP + EPLB - DSpark and confidence-scheduled verification - SWA bounded replay - Asynchronous scheduling (zero-overhead batch scheduler) - Batch-invariant inference - Deterministic sampling - Structured outputs Feature details and configuration - Optimized kernels: FlashMLA, DeepGEMM, DeepEP, TileKernels, DeepSelect, and custom TileLang kernels.

## Key Takeaways

- - DSpark and confidence-scheduled verification: accelerate decoding with draft tokens and use confidence estimates to schedule verification.
- Set DEEPINFER_ENABLE_MTP_VARLEN=1; DEEPINFER_USE_NEXTN_DECODE controls the maximum draft length (default: 5).
- - Decoder SWA bounded replay: reduce decoder prefill work by replaying only a bounded suffix.

---
_Auto-generated daily digest entry._
