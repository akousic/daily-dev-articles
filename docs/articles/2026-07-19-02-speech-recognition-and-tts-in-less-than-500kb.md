# Speech Recognition and TTS in less than 500kb

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 501
- **Published (UTC):** 2026-07-14 19:25
- **Original:** https://github.com/moonshine-ai/moonshine/tree/main/micro

## Summary

Moonshine Voice is an open source AI toolkit for developers building real-time voice agents and applications. Moonshine Micro is a version designed specifically for embedded system processors like microcontrollers and DSPs, and uses the Raspberry Pi RP2350, which retails for just 80 cents, as its reference platform. It includes voice-activity detection, command recognition, and neural speech synthesis and can run in as little as 470 KB of RAM.

## Key Takeaways

- You can see a full walkthrough in the video below: The memory and compute requirements are designed to fit resource-constrained systems.
- Figures below are for the RP2350 demo; the detailed memory budget breaks each one down: | Component | Flash | SRAM (arena peak) | Compute | |---|---|---|---| | VAD (Voice Activity Detection) | ~89 KiB | ~36 KiB | ~0.8 MMAC/frame (~25 MMAC/s) | | STT (SpellingCNN Speech-to-Text) | ~1.3 MiB | ~346 KiB | ~36 MMAC/s | | TTS (neural diphone synth @ 16 kHz) | ~1.8 MiB voice pack | ~340 KiB | ~37 MMAC typical reply (~65 MMAC/s out) | | TOTAL (Demo pipeline) | ~3.6 MiB | ~468 KiB provisioned* | classify + speak ~0.7–1.0 s | Notes: - Flash is .text+.rodatameasured witharm-none-eabi-sizeon the defaultmoonshine_micro_echofirmware (includes the embedded neural voice pack); SRAM is.bss+ heap + stacks.
- - *VAD, STT, and neural TTS run sequentially and time-share one ~384 KiB TFLM arena, so SRAM is not additive — ~468 KiB is the total RAM provisioned on the 520 KiB RP2350 (wifi_hardware~491 KiB).

---
_Auto-generated daily digest entry._
