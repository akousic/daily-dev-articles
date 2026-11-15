# Show HN: DeepSeek V3 in ~200 lines of pure Jax

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 265
- **Published (UTC):** 2026-11-14 15:04
- **Original:** https://github.com/Vaibhaav-Tiwari/deepseek-v3-jax

## Summary

The architecture from the DeepSeek-V3 technical report in 190 lines of pure JAX, pretrained from scratch on a MacBook Air on public-domain detective fiction. No Flax, no Equinox, no PyTorch. Params are plain dicts of arrays and every part of the model is a function you can read top to bottom in deepseek_v3.py.

## Key Takeaways

- Read the write-up: DeepSeek V3 in 190 lines of pure JAX, with diagrams, the code explained piece by piece, and the results.
- | Idea from the paper | What it does | Where | |---|---|---| | Multi-head Latent Attention (MLA) | Caches one small latent per token instead of full keys and values: 480 → 144 numbers per token per layer here | mla, init_cache | | Decoupled RoPE | One rotary key shared by all heads, kept outside the compressed latent | rope, apply_rope, mla | | DeepSeekMoE | 1 shared expert that always runs + 16 routed experts, top-4 per token | route, moe | | Auxiliary-loss-free balancing | A per-expert bias nudges routing toward idle experts; it changes which experts are picked, not their weights | update_bias, route | | Sequence-wise balance loss | The small complementary loss from the paper (α = 1e-4) | seq_balance_loss | | Multi-token prediction (MTP) | An extra module also predicts the token after next, weighted λ = 0.3 in the loss | forward, loss_fn | | Training and generation | bf16 compute on f32 master weights; prefill + decode with the MLA cache | make_train_step, generate | One run of the default config on a MacBook Air M5 (24 GB): | Model | 36.2M parameters, 13.6M active per token | | Data | 207 books, 21.7M training tokens (Hammett repeated 3×); validation is held-out crime fiction | | Training | 12,000 steps, ~98M tokens (~4.5 epochs), ~2.6 h | | Speed | ~10.7k tokens/s (median) | | Validation loss | 5.02 (step 250) → 3.51 | | Expert load, with bias | 5.7–6.9% per expert (even is 6.25%), at step 2000 | | Expert load, without bias | 0.09–18.6% per expert, at step 2000 | With balancing on and off, validation loss at step 2000 was the same (3.921 vs 3.923).
- The bias evens out the experts without costing anything, which is the paper's claim.

---
_Auto-generated daily digest entry._
