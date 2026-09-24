# Saving another 100TB of RAM with math (and Rust)

- **Source:** Cloudflare
- **Rank (today):** #5
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-09-24 18:22
- **Original:** https://blog.cloudflare.com/saving-100-tb-of-ram-with-math/

## Summary

Saving another 100TB of RAM with math (and Rust) Cloudflare operates at a scale so big that even after working here for years, it doesn’t seem real. We have thousands of servers all over the world with petabytes of RAM and millions of CPU cores, and all of it is pushed to the max. As vast as those resources feel, they are still finite, and when you need every service to run on every node, it doesn’t leave room for wasted space.

## Key Takeaways

- At this scale, small improvements are greatly magnified, so even 1%-at-a-time improvements are worth celebrating.
- And some tweaks add up to a lot more: in this post, we’ll look at how small changes to a single algorithm reduced the memory footprint of one of our Pingora-based services significantly.
- That allowed us to reclaim more than 100TB of RAM globally, on top of the 100TB of memory the DNS team was able to shed last month.

---
_Auto-generated daily digest entry._
