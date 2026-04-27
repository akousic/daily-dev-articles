# Wasm is not quite a stack machine

- **Source:** Lobsters
- **Rank (today):** #4
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-04-27 01:20
- **Original:** https://purplesyringa.moe/blog/wasm-is-not-quite-a-stack-machine/

## Summary

Everyone knows Wasm is a stack machine. Wikipedia says so, the official Wasm design specification says so, you get it. That is, until I started writing Wasm code – not compiling for Wasm, but writing the instructions by hand.

## Key Takeaways

- And I found out that there exists a major difference between Wasm and all other stack-based languages, that makes this claim misleading.
- What is a stack machine, even?
- Say you write a program in a high-level language, and at some point you want to calculate 2 * 3 + 5 * 7 .

---
_Auto-generated daily digest entry._
