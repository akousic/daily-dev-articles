# DeepSeek V4 Flash on a Single AMD MI300X

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 250
- **Published (UTC):** 2026-08-04 10:00
- **Original:** https://github.com/ryanzhou/deepseek-v4-flash-mi300x

## Summary

This repository contains the configuration and patches I use to run deepseek-ai/DeepSeek-V4-Flash-0731 on one AMD MI300X in production. It includes the Docker Compose stack, SHA-256-pinned file overlays, reference diffs against upstream, and tuning tables. The checkpoint runs as shipped, without additional weight quantization or offload.

## Key Takeaways

- Results from the pinned stack (vLLM ROCm nightly 0.26.1rc1.dev229+g124154a88.rocm723, AITER 0.1.19): | Metric | Result | |---|---| | Single-stream decode (median per-stream, DSpark-7) | 168.6 tok/s | | Prefill with tuned kernels | ≈ 7.9–8.5K tok/s (6,988–7,019 tok/s on fresh prompts in the shipping profile) | | 8 concurrent streams | 542 tok/s aggregate, 90.3 tok/s median per stream | | 64-stream burst | 830 tok/s aggregate, no OOM, no engine errors | | Context | 256K validated (the architecture supports 1M) | | Weights in HBM | 156.67 GiB — no additional quantization or weight offload | The official vLLM recipe targets NVIDIA and newer AMD hardware.
- Running the model reliably on MI300X required fixes for its FP8 format, MoE routing at high concurrency, causal speculative verification, CPU-KV synchronization, and several untuned kernel shapes.
- This repository collects those fixes and pins the versions used in production.

---
_Auto-generated daily digest entry._
