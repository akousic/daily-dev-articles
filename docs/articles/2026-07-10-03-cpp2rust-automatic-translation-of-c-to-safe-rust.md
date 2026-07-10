# Cpp2Rust: Automatic Translation of C++ to Safe Rust

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-07-09 22:24
- **Original:** https://github.com/Cpp2Rust/cpp2rust

## Summary

Cpp2Rust translates C++ to fully safe Rust automatically. It is a syntax-driven translator based on clang's AST. Cpp2Rust's algorithm is described in the paper Cpp2Rust: Automatic Translation of C++ to Safe Rust published at PLDI 2026.

## Key Takeaways

- Cpp2Rust first parses the input C++ file(s) with clang and produces an AST.
- It then traverses the AST and emits Rust code as strings, inserting calls to the libcc2rs runtime library where needed (e.g., for raw pointer semantics).
- Finally, the Rust code is pretty-printed using rustfmt to a single .rs file.

---
_Auto-generated daily digest entry._
