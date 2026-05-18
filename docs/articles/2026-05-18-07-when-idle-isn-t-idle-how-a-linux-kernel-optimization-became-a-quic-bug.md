# When "idle" isn't idle: how a Linux kernel optimization became a QUIC bug

- **Source:** Cloudflare
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-05-18 16:50
- **Original:** https://blog.cloudflare.com/quic-death-spiral-fix/

## Summary

CUBIC, standardized in RFC 9438, is the default congestion controller in Linux, and as a result governs how most TCP and QUIC connections on the public Internet probe for available bandwidth, back off when they detect loss, and recover afterward. At Cloudflare, our open-source implementation of QUIC, quiche, uses CUBIC as its default congestion controller, meaning this code is in the critical path for a significant share of the traffic we serve. In this post, we’ll tell the story of a bug in which CUBIC's congestion window (cwnd) gets permanently pinned at its minimum and never recovers from a congestion collapse event.

## Key Takeaways

- The story starts with a Linux kernel change aimed at bringing CUBIC into line with the app-limited exclusion described in RFC 9438 §4.2-12 — a fix to a real problem in TCP that, when ported to our QUIC implementation, surfaced unexpected behaviors in quiche.
- It has a happy ending: an elegant (near-)one-line fix that broke the cycle.
- CUBIC's logic in a nutshell Before we dive into the core problem, a quick refresher on Congestion Control Algorithms (CCAs) may help to set the stage.

---
_Auto-generated daily digest entry._
