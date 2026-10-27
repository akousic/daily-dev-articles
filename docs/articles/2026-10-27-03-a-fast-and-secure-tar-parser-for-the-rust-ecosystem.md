# A fast and secure tar parser for the Rust ecosystem

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-10-27 11:59
- **Original:** https://astral.sh/blog/tar-codec

## Summary

Starting with 0.131, uv uses tar-codec to parse source distributions. tar-codec is roughly twice as fast as our previous tar implementation (astral-tokio-tar) while also reducing uv's exposure to parser differentials and other security risks. This blog post is about tar-codec itself: what it is, and what compelled us to build and optimize it.

## Key Takeaways

- Read on if you, too, would like to know too much about tar archives.
- Background: uv and tar # What follows is an extended digression on the tar format.
- If all you care about is tar-codec, skip to it.

---
_Auto-generated daily digest entry._
