# Show HN: Needle: We Distilled Gemini Tool Calling into a 26M Model

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 575
- **Published (UTC):** 2026-05-12 18:03
- **Original:** https://github.com/cactus-compute/needle

## Summary

We distilled Gemini 3.1 into a 26m parameter "Simple Attention Network" that you can even finetune locally on your Mac/PC. In production, Needle runs on Cactus at 6000 toks/sec prefill and 1200 decode speed. Weights are fully open on Cactus-Compute/needle, as well as the dataset generation.

## Key Takeaways

- d=512, 8H/4KV, BPE=8192 ┌──────────────┐ │ Tool Call │ └──────┬───────┘ ┌┴──────────┐ │ Softmax │ └─────┬─────┘ ┌─────┴─────┐ │ Linear (T)│ ← tied └─────┬─────┘ ┌─────┴─────┐ │ ZCRMSNorm │ └─────┬─────┘ ┌────────┴────────┐ │ Decoder x 8 │ │┌───────────────┐│ ││ ZCRMSNorm ││ ││ Masked Self ││ ││ Attn + RoPE ││ ││ Gated Residual││ │├───────────────┤│ ┌──────────────┐ ││ ZCRMSNorm ││ │ Encoder x 12 │──────────────────────▶Cross Attn ││ │ │ ││ Gated Residual││ │ ┌──────────┐ │ │└───────────────┘│ │ │ZCRMSNorm │ │ └────────┬────────┘ │ │Self Attn │ │ ┌─────┴─────┐ │ │ GQA+RoPE │ │ │ Embedding │ ← shared │ │Gated Res │ │ └─────┬─────┘ │ │ │ │ ┌───────┴───────-┐ │ │ (no FFN) │ │ │[EOS]<tool_call>│ │ └──────────┘ │ │ + answer │ │ │ └───────────────-┘ └──────┬───────┘ │ ┌────┴──────┐ │ Embedding │ └────┬──────┘ │ ┌────┴──────┐ │ Text │ │ query │ └───────────┘ - Pretrained on 16 TPU v6e for 200B tokens (27hrs).
- - Post-trained on 2B tokens of single-shot function call dataset (45mins).
- Needle is an experimental run for Simple Attention Networks, geared at redefining tiny AI for consumer devies (phones, watches, glasses...).

---
_Auto-generated daily digest entry._
