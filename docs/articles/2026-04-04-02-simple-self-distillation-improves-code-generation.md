# Simple self-distillation improves code generation

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 236
- **Published (UTC):** 2026-04-04 10:26
- **Original:** https://arxiv.org/abs/2604.01193

## Summary

Computer Science > Computation and Language [Submitted on 1 Apr 2026] Title:Embarrassingly Simple Self-Distillation Improves Code Generation View PDF HTML (experimental)Abstract:Can a large language model (LLM) improve at code generation using only its own raw outputs, without a verifier, a teacher model, or reinforcement learning? We answer in the affirmative with simple self-distillation (SSD): sample solutions from the model with certain temperature and truncation configurations, then fine-tune on those samples with standard supervised fine-tuning. SSD improves Qwen3-30B-Instruct from 42.4% to 55.3% pass@1 on LiveCodeBench v6, with gains concentrating on harder problems, and it generalizes across Qwen and Llama models at 4B, 8B, and 30B scale, including both instruct and thinking variants.

## Key Takeaways

- To understand why such a simple method can work, we trace these gains to a precision-exploration conflict in LLM decoding and show that SSD reshapes token distributions in a context-dependent way, suppressing distractor tails where precision matters while preserving useful diversity where exploration matters.
- Taken together, SSD offers a complementary post-training direction for improving LLM code generation.
- References & Citations export BibTeX citation Loading...

---
_Auto-generated daily digest entry._
