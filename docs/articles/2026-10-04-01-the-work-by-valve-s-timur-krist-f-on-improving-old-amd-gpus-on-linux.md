# The work by Valve's Timur Kristóf on improving old AMD GPUs on Linux

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 411
- **Published (UTC):** 2026-10-03 19:14
- **Original:** https://www.phoronix.com/news/XDC-2026-Valve-Timur-AMDGPU

## Summary

The Amazing Work By Valve's Timur Kristóf On Improving Old AMD GPUs On Linux Over the past year Timur Kristóf of Valve's Linux graphics driver team has made multiple very nice improvements to the AMDGPU kernel driver for enhancing support for old (GCN 1.0/1.1 era from a decade ago) graphics cards so that they can better handle Linux gaming and other tasks. This week in Toronto, Kristóf presented on this AMDGPU work that he initially began as a kernel driver development exercise after initially spending years in user-space focused on the Mesa 3D driver code. Timur Kristóf has become a legend for those with old AMD GCN 1.0/1.1 graphics cards and APUs for transitioning them from the legacy Radeon driver over to the modern AMDGPU kernel driver, which unlocks being able to use the RADV Vulkan driver, better performance, and all-around better functionality than the legacy Radeon code.

## Key Takeaways

- In the process he had to address defects in the AMDGPU display code for these legacy graphics cards along with various power management issues and more.
- Then he went on to improve these graphics cards further with soft reset support and other enhancements all to make these aging graphics cards more viable for Linux gaming use in 2026 and beyond.
- For getting an idea of the impact of transitioning the old Radeon graphics cards to AMDGPU, see last year's Linux 6.19's Significant ~30% Performance Boost For Old AMD Radeon GPUs.

---
_Auto-generated daily digest entry._
