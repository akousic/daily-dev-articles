# Bun Rust rewrite: "codebase fails basic miri checks, allows for UB in safe rust"

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 438
- **Published (UTC):** 2026-05-15 16:51
- **Original:** https://github.com/oven-sh/bun/issues/30719

## Summary

error: Undefined Behavior: constructing invalid value of type &[u8]: encountered a dangling reference (0x20933[noalloc] has no provenance) --> src/main.rs:97:18 | 97 | unsafe { core::slice::from_raw_parts(ptr as *const u8, self.len()) } | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ Undefined Behavior occurred here | = help: this indicates a bug in the program: it performed an invalid operation, and caused Undefined Behavior = help: see https://doc.rust-lang.org/nightly/reference/behavior-considered-undefined.html for further information = note: stack backtrace: 0: PathString::slice at src/main.rs:97:18: 97:75 1: main at src/main.rs:130:22: 130:34 code: fn main() { let test = Box::new(*b"Hello World"); let init = PathString::init(&*test); drop(test); println!("{:?}", init.slice()); } Please consider not vibe coding rust as AIs are not good at writing Rust and also hire a real rust dev code: Please consider not vibe coding rust as AIs are not good at writing Rust and also hire a real rust dev

## Key Takeaways

- Read full article for details.

---
_Auto-generated daily digest entry._
