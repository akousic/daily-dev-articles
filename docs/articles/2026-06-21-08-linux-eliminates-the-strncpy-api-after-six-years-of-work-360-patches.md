# Linux eliminates the strncpy API after six years of work, 360 patches

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 259
- **Published (UTC):** 2026-06-20 20:59
- **Original:** https://www.phoronix.com/news/Linux-7.2-Drops-strncpy

## Summary

Linux Finally Eliminates The strncpy API After Six Years Of Work, 360+ Patches Linux 7.2 has finally eliminated the strncpy API from the Linux kernel. The strncpy() function for copying up to a specified number of bytes has long been deprecated and after six years of work and hundreds of patches, no more users of the strncpy interface within the Linux kernel remained that it has now been eliminated. The strncpy function within the Linux kernel has been a "persistent source of bugs" for years due to counter-intuitive semantics and behavior around NUL termination along with performance issues due to redundant zero-filling of the destination.

## Key Takeaways

- It took work over the last six years with around 362 commits to eliminate users of strncpy code within the kernel, but they are over the finish line for Linux 7.2.
- This merge on Friday eliminated the strncpy API and the last per CPU architecture strncpy implementations.
- In place of strncpy, Linux kernel code should use strscpy() for NUL terminated destinations, strscpy_pad() for NUl-terminated destinations with zero-padding, strtomem_pad() for non-NUL-terminated fixed-width fields, memcpy_and_pad() for bounded copies with explicit padding, or memcpy() for known-length memory copies.

---
_Auto-generated daily digest entry._
