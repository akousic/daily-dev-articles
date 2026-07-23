# Show HN: Cactus Hybrid: We taught Gemma 4 to know when it's wrong

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 176
- **Published (UTC):** 2026-07-22 17:56
- **Original:** https://github.com/cactus-compute/cactus-hybrid

## Summary

A small, on-device model is fast and private, but sometimes wrong. At Cactus we post-train models to know when they are wrong: we ship probes inside the checkpoint that score every answer with a confidence between 0 and 1, returned as structured data (never parsed out of the answer text). Answer on-device when confidence is high; you can re-route to a bigger model when it's low: if confidence < 0.85: answer = ask_a_bigger_model(prompt)We start the rollout with Gemma 4 E2B Hybrid, all builds live in the Cactus Hybrid collection on Hugging Face.

## Key Takeaways

- Gemma 4 E2B hybrid, the smallest Gemma model, matches Gemini 3.1 Flash-Lite on most benchmarks by routing only 15–35% of queries to the Gemini 3.1 Flash-Lite and running the remnant itself.
- | Benchmark | Handoff to match Flash-Lite (FP16) | At 4-bit | At 3-bit | |---|---|---|---| | ChartQA | 15–20% | 25–30% | 40–50% | | MMBench | 30–35% | 40–45% | 50–55% | | LibriSpeech | 25–30% | 35–40% | 55–65% | | GigaSpeech | 30–35% | 40–45% | 50–55% | | MMAU | 30–35% | 35–40% | 50–55% | | MMLU-Pro | 45–55% | ~90% | n/a | - N/B: Quantisation quality is measured on Cactus Quants which performs well at uniform quantization.
- - Developers are encouraged to benchmark for Unsloth, GGUF, and MLX quantization independently.

---
_Auto-generated daily digest entry._
