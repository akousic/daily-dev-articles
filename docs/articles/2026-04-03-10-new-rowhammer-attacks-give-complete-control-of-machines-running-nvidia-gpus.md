# New Rowhammer attacks give complete control of machines running Nvidia GPUs

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 99
- **Published (UTC):** 2026-04-03 08:15
- **Original:** https://arstechnica.com/security/2026/04/new-rowhammer-attacks-give-complete-control-of-machines-running-nvidia-gpus/

## Summary

The cost of high-performance GPUs, typically $8,000 or more, means they are frequently shared among dozens of users in cloud environments. Two new attacks demonstrate how a malicious user can gain full root control of a host machine by performing novel Rowhammer attacks on high-performance GPU cards made by Nvidia. The attacks exploit memory hardware’s increasing susceptibility to bit flips, in which 0s stored in memory switch to 1s and vice versa.

## Key Takeaways

- In 2014, researchers first demonstrated that repeated, rapid access—or “hammering”—of memory hardware known as DRAM creates electrical disturbances that flip bits.
- A year later, a different research team showed that by targeting specific DRAM rows storing sensitive data, an attacker could exploit the phenomenon to escalate an unprivileged user to root or evade security sandbox protections.
- Both attacks targeted DDR3 generations of DRAM.

---
_Auto-generated daily digest entry._
