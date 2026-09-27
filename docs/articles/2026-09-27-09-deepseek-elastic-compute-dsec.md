# DeepSeek Elastic Compute (DSec)

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 311
- **Published (UTC):** 2026-09-26 18:22
- **Original:** https://arxiv.org/abs/2609.22978

## Summary

Computer Science > Distributed, Parallel, and Cluster Computing [Submitted on 19 Sep 2026] Title:DeepSeek Elastic Compute (DSec): A Sandbox Infrastructure for Effective Agentic Training at Scale View PDF HTML (experimental) Abstract:Large-scale agentic training and evaluation with large language models (LLMs) rely on isolated, stateful execution environments in which models inspect repositories, invoke tools, execute commands, and interact with task-specific services. These workloads create sandboxes in large bursts, span heterogeneous functionality and isolation requirements, retain state across long interactions, and draw from large image corpora with limited reuse. Supporting them therefore requires an elastic execution platform rather than a single sandbox runtime.

## Key Takeaways

- This report presents DeepSeek Elastic Compute (DSec), a production sandbox platform that exposes FnCall, container, microVM, and full-VM sandbox backends through a unified SDK.
- DSec coordinates placement and lifecycle management across the cluster, composes environments from independently versioned layers, combines memory sharing, reclamation, and CPU scheduling for high-density execution, and loads image data on demand from Fire-Flyer File System (3FS), a cluster-wide distributed filesystem.
- DSec is co-designed with the reinforcement learning (RL) framework, decouples stateful rollout execution from preemptible GPU training, coordinates sandbox lifecycle with training to preserve rollout state while reclaiming idle resources, and mitigates agent misbehavior such as reward hacking.

---
_Auto-generated daily digest entry._
