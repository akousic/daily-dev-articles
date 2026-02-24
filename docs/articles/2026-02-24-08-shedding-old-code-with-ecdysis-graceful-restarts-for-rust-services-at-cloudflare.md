# Shedding old code with ecdysis: graceful restarts for Rust services at Cloudflare

- **Source:** Cloudflare
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-02-24 21:38
- **Original:** https://blog.cloudflare.com/ecdysis-rust-graceful-restarts/

## Summary

ecdysis | ˈekdəsəs | noun the process of shedding the old skin (in reptiles) or casting off the outer cuticle (in insects and other arthropods). How do you upgrade a network service, handling millions of requests per second around the globe, without disrupting even a single connection? One of our solutions at Cloudflare to this massive challenge has long been ecdysis, a Rust library that implements graceful process restarts where no live connections are dropped, and no new connections are refused.

## Key Takeaways

- Last month, we open-sourced ecdysis, so now anyone can use it.
- After five years of production use at Cloudflare, ecdysis has proven itself by enabling zero-downtime upgrades across our critical Rust infrastructure, saving millions of requests with every restart across Cloudflare’s global network.
- It’s hard to overstate the importance of getting these upgrades right, especially at the scale of Cloudflare’s network.

---
_Auto-generated daily digest entry._
