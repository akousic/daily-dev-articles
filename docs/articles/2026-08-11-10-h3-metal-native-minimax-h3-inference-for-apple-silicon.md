# H3-metal – Native MiniMax-H3 inference for Apple Silicon

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 367
- **Published (UTC):** 2026-08-11 01:22
- **Original:** https://github.com/antirez/h3.c

## Summary

Native MiniMax-H3 inference for Apple Silicon. The project is being built as a sequence of working vertical slices: deterministic host/model metadata first, then portable Metal block parity, prompt encoding, prompt-to-video/audio, and first/last-frame conditioning and then ordered references. Prompt-to-video/audio, first/last-frame conditioning, and ordered Ref2VA image/video/audio references work end to end.

## Key Takeaways

- The current work is incremental H3-specific Metal performance and memory optimization on M3 Max and M5 Max.
- The examples assume that the Hugging Face snapshot is in ./MiniMax-H3 and that FFmpeg and FFprobe are available on PATH.
- make -j8 mkdir -p outputs ./h3 --info -d ./MiniMax-H3 --info checks the model layout and prints the selected Metal device without mapping all weights or generating media.

---
_Auto-generated daily digest entry._
