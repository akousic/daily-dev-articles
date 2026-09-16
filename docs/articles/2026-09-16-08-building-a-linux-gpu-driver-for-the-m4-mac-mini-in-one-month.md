# Building a Linux GPU Driver for the M4 Mac Mini in One Month

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 397
- **Published (UTC):** 2026-09-15 19:30
- **Original:** https://codyho.dev/blog/gpu-driver/

## Summary

I Came, I Prompted, I Left Part 2: Building a GPU Driver From Scratch in One Month Previous blog post: https://codyho.dev/blog/hypervisor-macbook-neo/ What We Did TL;DR: Niklas and I built a fully OpenGL ES 3.0 compliant GPU driver for the M4 Mac Mini and MacBook Neo in about a month, a process which normally takes years. Here is Chrome and Firefox running WebGL on the M4 Mac Mini with working compositing: Most importantly, the driver is fast enough to run Minecraft at 200fps: Building this driver involved reverse engineering the AGX’s (Apple’s name for the GPU) incredibly complicated firmware ABI and user-space components. This was all done in a transparent, verifiably clean room manner using well established techniques.

## Key Takeaways

- The code is not yet ready for end users, but we are looking to get it to end users as soon as possible.
- How We Did It Previously, I built a hypervisor to reverse engineer macOS.
- Now the goal became to actually do something useful with it, and what better target than writing a GPU driver.

---
_Auto-generated daily digest entry._
