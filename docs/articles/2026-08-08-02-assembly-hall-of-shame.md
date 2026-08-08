# Assembly Hall of Shame

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 379
- **Published (UTC):** 2026-08-07 18:01
- **Original:** https://github.com/xoreaxeaxeax/asm-hall-of-shame

## Summary

Instruction latency analysis usually focuses on performance optimization—making code run as fast as possible. The Assembly Hall of Shame takes the opposite approach: searching for the absolute floor of single-instruction performance. x86: fxrstor64 Strategy: Use fxrstor64 to load 512-byte FPU/MMX/XMM state from a high-latency MMIO region in the PCIe fabric, then starve the fabric while the load is in flight — a fleet of hammer cores pounds a different high-latency MMIO register with tight 4-byte reads, saturating the PCIe root complex and endpoint with non-posted transactions, so CPU 0's 512-byte fxrstor64 must queue behind all that contending traffic.

## Key Takeaways

- Contender: AMD Ryzen 7 5800H ; CPU 0 — timed instruction movl $0xfcc68830, %rsi fxrstor64 %rsi ; CPUs 1..N — hammer loop against a different high-latency location movl 0xfcc68858, %eax 🏆 Score: 198,002,498,236 cycles 🏆 Time: 62 seconds A spec-violating unaligned ymm0 load that forced non-posted dword transactions from stalled GPU registers was used to break the fundamental design of System Management Mode in smiiiiiiiiiiiiiiii.
- vmovdqu 0xfcc003b1, %ymm0 - Instructions may use whatever setup is necessary, but only a single instruction is eligible to be scored.
- - Trapped/emulated/virtualized instructions may only time the trap, not the handler.

---
_Auto-generated daily digest entry._
