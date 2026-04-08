# MegaTrain: Full Precision Training of 100B+ Parameter LLMs on a Single GPU

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 122
- **Published (UTC):** 2026-04-08 12:19
- **Original:** https://arxiv.org/abs/2604.05091

## Summary

Computer Science > Computation and Language [Submitted on 6 Apr 2026] Title:MegaTrain: Full Precision Training of 100B+ Parameter Large Language Models on a Single GPU View PDF HTML (experimental)Abstract:We present MegaTrain, a memory-centric system that efficiently trains 100B+ parameter large language models at full precision on a single GPU. Unlike traditional GPU-centric systems, MegaTrain stores parameters and optimizer states in host memory (CPU memory) and treats GPUs as transient compute engines. For each layer, we stream parameters in and compute gradients out, minimizing persistent device state.

## Key Takeaways

- To battle the CPU-GPU bandwidth bottleneck, we adopt two key optimizations.
- 1) We introduce a pipelined double-buffered execution engine that overlaps parameter prefetching, computation, and gradient offloading across multiple CUDA streams, enabling continuous GPU execution.
- 2) We replace persistent autograd graphs with stateless layer templates, binding weights dynamically as they stream in, eliminating persistent graph metadata while providing flexibility in scheduling.

---
_Auto-generated daily digest entry._
