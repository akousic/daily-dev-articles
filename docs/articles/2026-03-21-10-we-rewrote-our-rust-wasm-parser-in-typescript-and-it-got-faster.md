# We rewrote our Rust WASM parser in TypeScript and it got faster

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 246
- **Published (UTC):** 2026-03-20 21:48
- **Original:** https://www.openui.com/blog/rust-wasm-parser

## Summary

We built the openui-lang parser in Rust and compiled it to WASM. The logic was sound: Rust is fast, WASM gives you near-native speed in the browser, and our parser is a reasonably complex multi-stage pipeline. Why wouldn't you want that in Rust?

## Key Takeaways

- Turns out we were optimising the wrong thing.
- The Pipeline The openui-lang parser converts a custom DSL emitted by an LLM into a React component tree.
- It runs on every streaming chunk — so latency matters a lot.

---
_Auto-generated daily digest entry._
