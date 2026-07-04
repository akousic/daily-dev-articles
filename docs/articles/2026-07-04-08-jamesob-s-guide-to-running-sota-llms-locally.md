# Jamesob's guide to running SOTA LLMs locally

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 377
- **Published (UTC):** 2026-07-03 15:03
- **Original:** https://github.com/jamesob/local-llm

## Summary

Note: nothing in this README aside from the tables was written by AI. Have $2k burning a hole in your pocket and want some local, state-of-the-art machine intelligence? If Dario and Altman are giving you heartburn (they should be), read on to figure out how to run this new kind of computing locally.

## Key Takeaways

- In this repo you'll find - the hardware I use to run SOTA locally, - why I bought what and little-known secrets for configuring it, - how I run speech-to-text (STT) locally, - ready-to-run configuration for running models I think are good within Docker containers.
- | Section | TL;DR | |---|---| | How much are you willing to spend?
- | $2k gets you Qwen and good STT (pretty far!); $40k gets you almost-Opus | | Base system | Last-gen EPYC + eBay DDR4 for $5.6k | | GPUs | 4× RTX PRO 6000, 384GB VRAM (where the money went) | | c-payne switch sub-BOM | Indie PCIe switching from c-payne.com so GPUs talk peer-to-peer | | GPU mount | A day of carpentry | | Making the switch behave | BIOS bifurcation, link speed, ASPM | | Kernel / GRUB params | iommu=offor NCCL hangs | | ACS disable | Keep P2P traffic inside the switch fabric | | GPU power limiting | Running $46k of silicon on a 110V circuit | | Result | Gen4 line rate: 27.5/50.4 GB/s, sub-µs latency | | runners/ | Ready-to-run serving configs: GLM-5.2-594B: vLLM docker-compose, DCP4+MTP5, ~80 t/s @ 460k ctx | | runners/stt | Ready-to-run speech-to-text config with whisper-large-v3 | | tools/ | measure-gpu-speed.sh: P2P bandwidth/latency benchmark | | Resources | rtx6kpro repo, c-payne | I was lucky/dumb enough to buy 4x RTX Pro 6000s back when they were cheaper.

---
_Auto-generated daily digest entry._
