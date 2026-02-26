# Show HN: I ported Tree-sitter to Go

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 211
- **Published (UTC):** 2026-02-25 18:28
- **Original:** https://github.com/odvcencio/gotreesitter

## Summary

Pure-Go tree-sitter runtime — no CGo, no C toolchain, WASM-ready. go get github.com/odvcencio/gotreesitter Implements the same parse-table format tree-sitter uses, so existing grammars work without recompilation. Outperforms the CGo binding on every workload — incremental edits (the dominant operation in editors and language servers) are 90x faster than the C implementation.

## Key Takeaways

- Every existing Go tree-sitter binding requires CGo.
- That means: - Cross-compilation breaks ( GOOS=wasip1 ,GOARCH=arm64 from Linux, Windows without MSYS2) - CI pipelines need a C toolchain in every build image go install fails for end users withoutgcc - Race detector, fuzzing, and coverage tools work poorly across the CGo boundary gotreesitter is pure Go.
- go get and build — on any target, any platform.

---
_Auto-generated daily digest entry._
