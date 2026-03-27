# $500 GPU outperforms Claude Sonnet on coding benchmarks

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 398
- **Published (UTC):** 2026-03-26 17:31
- **Original:** https://github.com/itigges22/ATLAS

## Summary

Adaptive Test-time Learning and Autonomous Specialization A.T.L.A.S achieves 74.6% LiveCodeBench pass@1-v(k=3) with a frozen 14B model on a single consumer GPU -- up from 36-41% in V2 -- through constraint-driven generation and self-verified iterative refinement. The premise: wrap a frozen smaller model in intelligent infrastructure -- structured generation, energy-based verification, self-verified repair -- and it can compete with frontier API models at a fraction of the cost. No fine-tuning, no API calls, no cloud.

## Key Takeaways

- Fully self-hosted -- no data leaves the machine, no API keys required, no usage metering.
- Hardware: RTX 5060 Ti 16GB | Model: Qwen3-14B-Q4_K_M (frozen) | Benchmark | Score | Tasks | Method | |---|---|---|---| | LiveCodeBench v5 | 74.6% pass@1-v(k=3)* | 599 | V3 pipeline: PlanSearch + self-verified PR-CoT repair, V3 Score | | GPQA Diamond | 47.0% | 198 | k=5, multiple-choice knowledge reasoning, V2 Score | | SciCode | 14.7% (sub-problems) | 341 | k=1, cross-domain scientific coding, V2 Score | *pass@k-v(k=3) = one solution submitted per task, but generated via best-of-3 candidates + Lens selection + iterative repair on failures.
- Not single-shot generation, it is not pass@1.

---
_Auto-generated daily digest entry._
