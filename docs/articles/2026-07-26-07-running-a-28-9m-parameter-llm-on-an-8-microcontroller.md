# Running a 28.9M parameter LLM on an $8 microcontroller

- **Source:** Hacker News
- **Rank (today):** #7
- **Ranking metrics:** HN score 245
- **Published (UTC):** 2026-07-25 18:59
- **Original:** https://github.com/slvDev/esp32-ai

## Summary

Open to Work · 𝕏 slvDev · LinkedIn This is a 28.9 million parameter language model that generates text on an ESP32-S3, a microcontroller that costs about $8. It runs on the chip itself, with nothing sent to a server, and it writes each word to a small screen wired to the chip at roughly 9 tokens per second. The last language model people ran on a chip like this had 260 thousand parameters, so this one holds about a hundred times more.

## Key Takeaways

- It fits because most of the model lives in flash instead of RAM, using an idea from Google's Gemma models called Per-Layer Embeddings.
- | Parameters | 28.9M stored (25M of them in a flash lookup table) | | Chip | ESP32-S3, about $8, with 512KB SRAM, 8MB PSRAM and 16MB flash | | Speed | about 9.5 tok/s end to end (9.7 tok/s of pure compute) | | Connectivity | none, everything runs on the device | | Model size | 14.9MB at 4-bit | A microcontroller has very little fast memory.
- The ESP32-S3 gives you 512KB of SRAM.

---
_Auto-generated daily digest entry._
