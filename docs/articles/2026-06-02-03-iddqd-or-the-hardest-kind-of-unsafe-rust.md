# iddqd, or the hardest kind of unsafe Rust

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-06-02 11:20
- **Original:** https://oxide.computer/blog/iddqd-unsafe

## Summary

I’m the main author of iddqd , a Rust library for maps (named after the Doom cheat code) where keys are borrowed from values. At Oxide we use it extensively in Omicron, our control plane—the software that sits at the heart of every Oxide rack, provisions resources like compute and storage for our customers, and ensures the rack stays up and running over time. iddqd maintains in-memory indexes of the kinds of large records that show up everywhere in a system like that, such as disks or sled inventories.

## Key Takeaways

- As a result, it must be correct: if it misbehaves, our control plane can malfunction in ways that are unpredictable and hard to diagnose.
- iddqd consists of a fair amount of unsafe code underneath.
- There’s been some recent concern over the amount of unsafe code in Rust rewrites, so I thought I’d write about some of the unsafe code in iddqd and how we try to tame it.

---
_Auto-generated daily digest entry._
