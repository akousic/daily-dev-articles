# Spaghettifying DRAM

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 678
- **Published (UTC):** 2026-08-13 14:17
- **Original:** https://github.com/xoreaxeaxeax/skitter-creek-bath-salts

## Summary

Unlocking everything on the CPU with DRAM scrambling — PSP, C6, microcode, SMM, and anything else the specs left out. Poke the DRAM controller and an address can be made to land wherever you want in memory. skitter-creek-bath-salts modifies the bottom layers of the memory hierarchy to rewire the physical DRAM address translations.

## Key Takeaways

- This scrambles platform memory, exposing protected regions of DRAM — carveouts invisible even to the kernel.
- When the address translations break, so do the security primitives built on them, and we unlock everything.
- - Unlock your Platform Security Processor - Unlock System Management Mode - Unlock C6 DRAM - Unlock your CPU microcode Developed and tested on AMD Family 16h CPUs, the last generation whose datasheets document the DRAM controller's translation registers — and show that they can't be locked.

---
_Auto-generated daily digest entry._
