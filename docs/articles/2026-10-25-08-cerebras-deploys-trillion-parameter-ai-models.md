# Cerebras Deploys Trillion-Parameter AI Models

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 303
- **Published (UTC):** 2026-10-25 01:33
- **Original:** https://www.cerebras.ai/blog/how-we-deploy-trillion-parameter-frontier-models-on-cerebras

## Summary

One of the most frequently asked questions we get is how we deploy large models on Cerebras wafer-scale chips. A single Cerebras WSE-3T wafer has 44 GB of on-chip memory, and trillion-parameter frontier models need terabytes for their weights alone. In this post, we’ll explain how we split a large frontier model across multiple WSE-3T wafers, to run multi-trillion parameter models at 1000-2000+ tokens per second.

## Key Takeaways

- We’ll use the open source model Kimi K3, with ~3 trillion parameters, as an illustrative example.
- By the end, you'll understand: - How we fit the full model into on-chip memory - How we map the model across multiple chips - How we handle a high # of concurrent requests Breaking it down with Kimi K3 Kimi K3 is an open source, 3T parameter model with 69 linear-attention layers and 24 dense layers.
- It scores an impressive 88.3% on Terminal-Bench 2.1 (vs.

---
_Auto-generated daily digest entry._
