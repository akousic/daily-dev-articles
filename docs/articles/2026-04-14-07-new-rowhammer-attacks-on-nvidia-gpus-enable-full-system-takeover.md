# New Rowhammer Attacks on NVIDIA GPUs Enable Full System Takeover

- **Source:** InfoQ
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-04-14 15:18
- **Original:** https://www.infoq.com/news/2026/04/rowhammer-attacks-nvidia/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

Security researchers have demonstrated a new class of Rowhammer attacks targeting NVIDIA GPUs that can escalate from memory corruption to full system compromise, marking a significant shift in hardware-level security risks. Detailed in recent academic research and highlighted by Ars Technica, the attacks, known as GDDRHammer and GeForce/GeForge, exploit vulnerabilities in GDDR6 GPU memory to gain arbitrary read and write access, ultimately allowing attackers to take control of the host CPU and system memory. The findings build on earlier research into Rowhammer, a long-known hardware flaw in DRAM where repeatedly accessing ("hammering") memory rows induces bit flips in adjacent memory cells, bypassing traditional isolation mechanisms.

## Key Takeaways

- While historically associated with system RAM, researchers have now shown that similar techniques can be applied to GPU memory, dramatically expanding the attack surface, particularly in environments where GPUs are shared, such as cloud infrastructure and AI training platforms.
- Unlike earlier GPU-focused attacks that primarily impacted application behavior (such as degrading AI model accuracy), these new techniques demonstrate end-to-end compromise capabilities.
- By carefully inducing bit flips in GPU memory, attackers can manipulate page tables and memory mappings, effectively bridging the gap between GPU and CPU memory spaces.

---
_Auto-generated daily digest entry._
