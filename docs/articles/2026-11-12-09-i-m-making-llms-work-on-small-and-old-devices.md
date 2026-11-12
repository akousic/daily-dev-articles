# I'm making LLMs work on small and old devices

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 206
- **Published (UTC):** 2026-11-12 15:23
- **Original:** https://github.com/hyperionaidev/smolmaxxing/

## Summary

Every device around you is more capable than it looks. TV boxes, old phones, single-board computers and routers all ship with CPUs, RAM and flash that sit idle most of the day. smolmaxxing is about unlocking that capability: finding the biggest language model each device can really run, then pushing it further with custom kernels, smarter memory use and weight streaming.

## Key Takeaways

- Every claim is measured on the hardware itself.
- Device #1 is a Xiaomi TV Box S (3rd Gen): Amlogic S7D, 4× Cortex-A55 @ 2.5 GHz, 1.9 GB of RAM (about 1 GB usable), eMMC flash, Android 14, no root.
- On it, this repo runs models from 260 K to 16 B parameters: - Qwen3.5-0.8B: 16.8 tok/s (2.2× the stock 7.5; measured in the evening of 11-05, see §17).

---
_Auto-generated daily digest entry._
