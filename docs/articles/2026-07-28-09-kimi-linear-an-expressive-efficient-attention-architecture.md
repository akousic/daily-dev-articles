# Kimi Linear: An Expressive, Efficient Attention Architecture

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 156
- **Published (UTC):** 2026-07-28 10:52
- **Original:** https://arxiv.org/abs/2510.26692

## Summary

Computer Science > Computation and Language [Submitted on 30 Oct 2025 (v1), last revised 1 Nov 2025 (this version, v2)] Title:Kimi Linear: An Expressive, Efficient Attention Architecture View PDFAbstract:We introduce Kimi Linear, a hybrid linear attention architecture that, for the first time, outperforms full attention under fair comparisons across various scenarios -- including short-context, long-context, and reinforcement learning (RL) scaling regimes. At its core lies Kimi Delta Attention (KDA), an expressive linear attention module that extends Gated DeltaNet with a finer-grained gating mechanism, enabling more effective use of limited finite-state RNN memory. Our bespoke chunkwise algorithm achieves high hardware efficiency through a specialized variant of the Diagonal-Plus-Low-Rank (DPLR) transition matrices, which substantially reduces computation compared to the general DPLR formulation while remaining more consistent with the classical delta rule.

## Key Takeaways

- We pretrain a Kimi Linear model with 3B activated parameters and 48B total parameters, based on a layerwise hybrid of KDA and Multi-Head Latent Attention (MLA).
- Our experiments show that with an identical training recipe, Kimi Linear outperforms full MLA with a sizeable margin across all evaluated tasks, while reducing KV cache usage by up to 75% and achieving up to 6 times decoding throughput for a 1M context.
- These results demonstrate that Kimi Linear can be a drop-in replacement for full attention architectures with superior performance and efficiency, including tasks with longer input and output lengths.

---
_Auto-generated daily digest entry._
