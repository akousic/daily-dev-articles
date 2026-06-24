# Qwen-AgentWorld: Language World Models for General Agents

- **Source:** Hacker News
- **Rank (today):** #7
- **Ranking metrics:** HN score 174
- **Published (UTC):** 2026-06-24 02:21
- **Original:** https://arxiv.org/abs/2606.24597

## Summary

Computer Science > Computation and Language [Submitted on 23 Jun 2026] Title:Qwen-AgentWorld: Language World Models for General Agents View PDF HTML (experimental)Abstract:A world model predicts environment dynamics based on current observations and actions, serving as a core cognitive mechanism for reasoning and planning. In this work, we investigate how world modeling based on language models can further push the boundaries of general agents. (i) We first focus on building foundation models for agentic environment simulation.

## Key Takeaways

- We introduce Qwen-AgentWorld-35B-A3B and Qwen-AgentWorld-397B-A17B, the first language world models capable of simulating agentic environments covering 7 domains via long chain-of-thought reasoning.
- Leveraging more than 10M environment interaction trajectories of 7 domains in real-world environments, we develop Qwen-AgentWorld through a three-stage training pipeline: CPT injects general-purpose world modeling capabilities from the state transition dynamics and augmented professional corpora, SFT activates next-state-prediction reasoning, and RL sharpens simulation fidelity through a tailored framework with hybrid rubric-and-rule rewards.
- To evaluate language world models, we present AgentWorldBench, a comprehensive benchmark constructed from real-world interactions of 5 frontier models on 9 established benchmarks.

---
_Auto-generated daily digest entry._
