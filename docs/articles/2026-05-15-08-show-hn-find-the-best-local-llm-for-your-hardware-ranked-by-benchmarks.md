# Show HN: Find the best local LLM for your hardware, ranked by benchmarks

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 261
- **Published (UTC):** 2026-05-15 09:19
- **Original:** https://github.com/Andyyyy64/whichllm

## Summary

Find the best local LLM that actually runs on your hardware. Auto-detects your GPU/CPU/RAM and ranks the top models from HuggingFace that fit your system. $ whichllm --gpu "RTX 4090" #1 Qwen/Qwen3.6-27B 27.8B Q5_K_M score 92.8 27 t/s #2 Qwen/Qwen3-32B 32.0B Q4_K_M score 83.0 31 t/s #3 Qwen/Qwen3-30B-A3B 30.0B Q5_K_M score 82.7 102 t/s The 32B model fits your card fine — whichllm still ranks the 27B #1, because it scores higher on real benchmarks and is a newer generation.

## Key Takeaways

- A size-only "what fits?" tool would hand you the bigger one.
- That gap is the whole point of whichllm.
- (Note #3: a MoE model at 102 t/s — speed is ranked on active params, quality on total.) Real top picks (snapshot 2026-05 — your results track live HuggingFace data, this is not a static list): | Hardware | VRAM | Top pick | Speed | |---|---|---|---| | RTX 5090 | 32 GB | Qwen3.6-27B · Q6_K · score 94.7 | ~40 t/s | | RTX 4090 / 3090 | 24 GB | Qwen3.6-27B · Q5_K_M · score 92.8 | ~27 t/s | | RTX 4060 | 8 GB | Qwen3-14B · Q3_K_M · score 71.0 | ~22 t/s | | Apple M3 Max | 36 GB | Qwen3.6-27B · Q5_K_M · score 89.4 | ~9 t/s | | CPU only | — | gpt-oss-20b (MoE) · Q4_K_M · score 45.2 | ~6 t/s | whichllm --gpu "<your card>" to simulate any of these before you buy.

---
_Auto-generated daily digest entry._
