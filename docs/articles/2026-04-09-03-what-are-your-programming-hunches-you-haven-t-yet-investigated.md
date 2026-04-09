# What are your programming "hunches" you haven't yet investigated?

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-04-09 03:55
- **Original:** https://lobste.rs/s/gns27z/what_are_your_programming_hunches_you

## Summary

Do other Lobsters have any hunches that certain aspects of problem could be better solved by doing x, or applying y, but haven't had the time to investigate them or the confidence to rubber duck them? Hunches often create room for interesting discussions or new ways to think about problems. Starting a cross-platform GUI toolkit project from accessibility instead of rendering would be much more practical and would result in a complete toolkit earlier than other way around.

## Key Takeaways

- I've had this exact idea and have made a few attempts at assembling one.
- Ideally it would be an a11y-only "invisible component tree" library that could be used alongside any existing graphics-only GUI library, like IMGUI.
- The problem is that there are 3 separate accessibility libraries (for Windows, Mac, Linux) and they're all archaic and poorly documented.

---
_Auto-generated daily digest entry._
