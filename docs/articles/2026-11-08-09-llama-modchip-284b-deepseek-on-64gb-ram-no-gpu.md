# Llama-modchip: 284B DeepSeek on 64GB RAM, no GPU

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 251
- **Published (UTC):** 2026-11-08 10:22
- **Original:** https://github.com/synchopate/llama-modchip

## Summary

Break the 64 GB RAM Wall: Run 284B DeepSeek-V4-Flash (< 59 GiB RAM) & 30B MoEs (up to 111 tok/s) at 256K Context on Pure CPU — Zero GPUs Required. ⚡ Quickstart · 🧩 Supported Models · 🖥️ Supported Chips & Platforms · 🏆 Leaderboard · 📄 Preprint PDF (paper/) · 📐 Architecture · ❓ FAQ | 284.33B Frontier MoE params | 56.56 GiB checkpoint on disk | 57.61 GiB peak VmRSS @ 256K ctx | 44.36 tok/s 284B CPU prefill | 60.4–111.6 tok/s 30B MoE CPU decode | 13.1 ms Claude Code restore | 0 GPUs required | Real-time Frontier & Agentic MoE inference on the CPU workstation you already own — 100% in RAM, zero NVMe swap: | the machine you have | RAM | recommended model | speed (0 GPUs) | what is going on | |---|---|---|---|---| | a developer laptop / mini-PC | 16–32 GB | Nemotron-3.5-30B-A3B ( 14.35 GiB) | 25.0–60.4 tok/s | 46 Mamba-2 SSM layers + 1.64 MB L3 Stockfish-PVS drafter; 256K ctx in 6 GiB KV | | a 64 GB desktop / server | 64 GB | DeepSeek-V4-Flash 284B ( 56.56 GiB) | 44.4 tok/s pp · 9.1–14.7 tok/s tg | SwiGLU-H2 shaves 20.31 GiB; entire 284B model + 256K ctx sits in RAM (57.61 GiB VmRSS) | | a hybrid desktop (CPU + 16 GB GPU) | 32–64 GB | Nemotron-30B / Qwen3-30B | 80.80 tok/s | hot attention trunk on GPU ( -ngl 99), cold routed MoE experts in CPU DDR5 | | an 8-channel workstation (Threadripper) | 128 GB+ | DeepSeek-284B / Nemotron-30B | 111.62 tok/s (30B) | 8-CCD AVX-512BW _1x8 register tiling saturates 8-channel DDR5 memory bandwidth | TL;DR — The 3 Paradigm-Breaking Pillars of llama-modchip: - 🐋 284.33B Frontier MoE in a 64 GB CPU Box: Shrinks DeepSeek-V4-Flash from 76.87 GiB (which crashes in OOM on 64 GB Linux) down to 56.56 GiB on disk / 57.61–58.9 GiB VmRSS at full 256K context (44.36 tok/s prefill, 9.06–10.74 tok/s pure CPU decode, 11.5–14.7 tok/s with PVS) using closed-form Analytical SwiGLU-H2 Second-Order Hessian Compression + Fractal-64 (Q2_0, 3.75 bpw) MLA transcoding + 4-Level Register (ZMM AVX-512BW) + L1D (32 KB) + L2 (1 MB) + L3 (64 MB) Whole-Model Tiling +$L_2$ -Quadrature MoE Pruning. - ⚡ 30B MoE at GPU Speeds on Pure CPU: Runs NVIDIA-Nemotron-3.5-30B-A3B in 14.35 GiB at 25.0–60.4 tok/s on 16-core Zen 5 (111.6 tok/s on Threadripper, 80.8 tok/s on AMD Vulkan Hybrid, 44.97 tok/s on AWS Graviton3 ARM64) via a 1.64 MB Stockfish-PVS v2 + RouteCrack L2/L3 Drafter (96.4% acceptance) and _MM_HINT_NTA L3 cache isolation (HARPCache).

## Key Takeaways

- - 🤖 Zero-API Claude Code (./modchip claude): Eliminates the 45-second CPU agent prompt re-evaluation bottleneck via /dev/shm Slot-0 KV Warm Restore (18.9 ms on Nemotron-30B / 13.1–32.6 ms on DeepSeek-284B) with all 40 Claude Code tools active.
- git clone https://github.com/synchopate/llama-modchip.git cd llama-modchip ./modchip chat ⚠️ Important Compatibility Note (GGML_TYPE_Q2_0 = 40): Our Fractal-64 models use custom block-64 BF16-scale Gray-coded tensors (GGML_TYPE_Q2_0, type ID 40) and custom deepseek4 / Stockfish-PVS kernels.
- Opening them in unpatched llama.cpp, Ollama, or LM Studio will fail with unknown tensor type 40.

---
_Auto-generated daily digest entry._
