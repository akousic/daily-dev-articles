# A tail-call interpreter in (nightly) Rust

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-04-05 08:19
- **Original:** https://www.mattkeeter.com/blog/2026-04-05-tailcall/

## Summary

A tail-call interpreter in (nightly) Rust Last week, I wrote a tail-call interpreter using the become keyword, which was recently added to nightly Rust (seven months ago is recent, right?). It was a surprisingly pleasant experience, and the resulting VM outperforms both my previous Rust implementation and my hand-coded ARM64 assembly. Tailcall-based techniques have been all the rage recently (see this overview); consider this my trip report implementing a simple but non-trivial system.

## Key Takeaways

- For those keeping track at home, this is the latest in my exploration of high-performance emulation of the Uxn CPU, which runs a bunch of applications in the Hundred Rabbits ecosystem.
- If you want to read the whole saga, here's the list: - Project writeup for Raven, my original Rust implementation - Beating the compiler, in which I write an ARM64 assembly implementation which outperforms my Rust code - Guided by the beauty of our test suite, in which I revisit the code a year later and improve its testing and CI - An x86-64 backend for raven-uxn , in which I port the assembly implementation from ARM64 to x86 (with the help of Claude Code) Experimenting with LLMs proved controversial, which wasn't a surprise; I'm pleased to declare that all of the tail-call code is human-written, and the new backend can be used as a substitute for the x86 assembly backend at a minor performance penalty.
- (This blog post is also entirely human-written, per my personal standards) The next few sections summarize previous work, so feel free to skim them if you've done the reading and jump straight to tailcalls in Rust.

---
_Auto-generated daily digest entry._
