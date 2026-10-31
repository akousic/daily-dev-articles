# Show HN: A working Nintendo in ~1GB of Qwen weights

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 278
- **Published (UTC):** 2026-10-30 16:40
- **Original:** https://github.com/dbreunig/nesformer

## Summary

An NES CPU compiled into the weights of a stock Qwen3.5 model. The NES's 6502 CPU (the core of its 2A03 chip), its 2 KB of work RAM, and a cartridge's program ROM run inside a standard Qwen3_5ForCausalLM checkpoint. Nobody trained these weights; a compiler computed every one.

## Key Takeaways

- When you play a game, the model predicts the CPU's execution log one token at a time.
- A small host program plays the rest of the console around it: it draws the picture, reads the controller, and fires the vblank interrupt.
- nesformer builds on Qwenputer by Divyansh Agrawal, which compiled a CHIP-8 and then a RISC-V CPU into Qwen3.5-4B.

---
_Auto-generated daily digest entry._
