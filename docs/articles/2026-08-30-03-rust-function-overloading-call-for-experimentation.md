# Rust Function Overloading - Call for Experimentation

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-08-30 04:39
- **Original:** https://blog.rust-lang.org/inside-rust/2026/08/19/overloading-experiment/

## Summary

In partnership with the Rust Foundation's Rust-C++ Interop Initiative, the Rust Project has been experimenting with function overloading for FFI bindings. This experiment is now at a stage where compiler and interop tool developers can start exploring function overloading. Stable Rust already supports a form of overloading using tuples and traits, but calling these overloaded functions looks strange, because the overloaded arguments have to be passed as a single tuple argument, like this: hypot((2.0, 3.0, 6.0)).

## Key Takeaways

- Stable Rust also allows overloading of built-in operators with user-defined types, via traits like Add (the + operator) and Neg (the - value negation operator).
- We are running an unstable nightly Rust language experiment to answer questions like: - How much overloading can we do with Rust’s existing trait system?
- - Could this help us call C++ from Rust ergonomically?

---
_Auto-generated daily digest entry._
