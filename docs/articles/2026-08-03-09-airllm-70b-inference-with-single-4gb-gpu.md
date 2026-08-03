# AirLLM 70B inference with single 4GB GPU

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 106
- **Published (UTC):** 2026-08-03 11:15
- **Original:** https://github.com/lyogavin/airllm

## Summary

Quickstart | Configurations | MacOS | Example notebooks | FAQ AirLLM dramatically reduces inference memory usage, letting 70B large language models run on a single 4GB GPU card — without quantization, distillation, or pruning. You can even run 405B Llama 3.1 on 8GB, DeepSeek-V3 (671B) on ~12GB, and Kimi K3 (2.8T) — the largest open-source model released to date — on under 4GB, because sparse MoE models stream one expert at a time rather than a whole layer. - Best AI Game Sprite Generator - Best AI Facial Expression Editor - Bloome — build & run AI agent teams in the cloud, zero setup [2026/07] Kimi K3 (2.8T) support: the largest open-source model runs on a single card in 3.72GB of VRAM, measured end to end on one RTX 6000 Ada.

## Key Takeaways

- Per-expert streaming loads only the experts a token actually routes to.
- K3 brings three requirements of its own: pip install compressed-tensors flash-attn (its model code mandates flash attention regardless of what you request), a CUDA 12 build of torch, since no prebuilt flash-attn wheel exists for CUDA 13 yet, and transformers 4.56.x, as its remote code does not load on 5.x.
- [2026/06] v3.0: FP8 model support + the latest models.

---
_Auto-generated daily digest entry._
