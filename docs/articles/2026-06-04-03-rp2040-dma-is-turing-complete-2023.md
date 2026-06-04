# RP2040 DMA is Turing Complete (2023)

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-06-04 06:02
- **Original:** https://people.ece.cornell.edu/land/courses/ece4760/RP2040/C_SDK_DMA_machine/DMA_machine_rp2040.html

## Summary

Cornell University ECE4760 Direct Memory Access computing machine RP2040 DMA on RP2040 DMA uses memory controllers separate from the CPU to accelerate data movment between memory locations, or between peripherials and memory. The RP2040 has 12 DMA channels which can stream an agregate of over 100 megabytes/sec without affecting CPU performance, in many cases. There are a huge number of options available to set up a DMA transfer.

## Key Takeaways

- You can think of a DMA channel controller as a separate, programmable, processor with the main job of moving data.
- Memory on the rp2040 is arranged as a bus matrix with separate memory bus control masters for each ARM core and for the DMA system, and several memory bus targets accessed by the masters.
- Each bus target can be accessed on each machine cycle.

---
_Auto-generated daily digest entry._
