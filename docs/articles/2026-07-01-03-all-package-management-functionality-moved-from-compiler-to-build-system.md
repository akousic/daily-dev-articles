# All Package Management Functionality Moved from Compiler to Build System

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-07-01 06:29
- **Original:** https://ziglang.org/devlog/2026/?2026-06-30#2026-06-30

## Summary

Devlog This page contains a curated list of recent changes to main branch Zig. Also available as an RSS feed. This page contains entries for the year 2026.

## Key Takeaways

- Other years are available in the Devlog archive page.
- All Package Management Functionality Moved from Compiler to Build System Author: Andrew Kelley Now that there is a separate process for users’ build.zig scripts and the build system itself, it makes sense for that to be the place that package management logic lives.
- I moved these subcommands to the maker process: - zig build - zig fetch - zig init - zig libc This means that large parts of what used to be included in the compiler executable are now shipped in source form instead, including: - package fetching logic - HTTP client and networking - TLS (Transport Layer Security) and associated crypto - Git protocol - xz, gzip, zstd, flate, zip - parsing, validation, and otherwise dealing with build.zig.zonfiles Consequently, this functionality can now be patched without rebuilding the compiler, making it easier for users and contributors to tinker.

---
_Auto-generated daily digest entry._
