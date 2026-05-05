# Bun (the js runtime) is being vibe-ported from zig to rust

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-05-04 22:07
- **Original:** https://github.com/oven-sh/bun/blob/claude/phase-a-port/docs/PORTING.md

## Summary

You are translating one Zig file to Rust. Read this whole document before writing any code. The goal of Phase A is a draft .rs next to the .zig that captures the logic faithfully — it does not need to compile.

## Key Takeaways

- Phase B makes it compile crate-by-crate.
- - Write the .rs in the same directory as the.zig , same basename.<area> is always the first path component undersrc/ (the crate root).
- If the.zig basename equals its immediate parent directory name (any depth), name itmod.rs ; if it equals the top-level<area> dir, name itlib.rs .

---
_Auto-generated daily digest entry._
