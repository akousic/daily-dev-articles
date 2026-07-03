# crustc: entirety of `rustc`, translated to C

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 343
- **Published (UTC):** 2026-07-02 22:57
- **Original:** https://github.com/FractalFir/crustc

## Summary

This is a functional Rust compiler you can build with GCC & make. # We need to provide a path to LLVM(`libLLVM.so.22.1-rust-1.98.0-nightly`) # I *could* include pre-built LLVM in the project, but I'd rather not embed random binaries in the project. make -j20 LLVM_LIB_DIR=~/.rustup/toolchains/nightly-2026-06-16-aarch64-unknown-linux-gnu/libIt is just C code [1], which, when compiled, gives you a functional Rust compiler.

## Key Takeaways

- # It works - (library path to point to libLLVM.so.22.1-rust-1.98.0-nightly - rustc uses llvm) LD_LIBRARY_PATH=~/.rustup/toolchains/nightly-2026-06-16-aarch64-unknown-linux-gnu/lib:./rustc_driver ./rustc/rustc --version rustc 1.98.0-nightly (c712ea946 2026-06-16)That Rust compiler can compile code - build core, alloc, std - you name it!
- This is a demo/teaser for my new Rust to C compiler toolchain.
- The full cilly toolchain compiles your own Rust to C for arbitrary targets.

---
_Auto-generated daily digest entry._
