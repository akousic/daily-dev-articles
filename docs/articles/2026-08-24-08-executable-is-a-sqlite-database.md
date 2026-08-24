# Executable Is a SQLite Database

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 261
- **Published (UTC):** 2026-08-24 04:48
- **Original:** https://fzakaria.com/2026/08/23/your-executable-is-a-sqlite-database

## Summary

I have been probably obsessed with two things in the last few years: Nix as a tool to explore innovative ideas that require the capability to rebuild the world and replacing ELF with SQLite as an executable format. You might have noticed that these two ideas are well suited to each other. I explored the idea during my PhD thesis but found feedback from others unmotivating.

## Key Takeaways

- Radical ideas are hard to sell, as you are working against the inertia of the established solution.
- One of the end results of that exploration was sqlelf, a tool that lets you explore an ELF file declaratively using SQL.11I wrote a paper, arXiv:2405.03883, that I failed to get published and a follow-up post on querying with it.
- SELECT name FROM elf_symbols instead of fiddling with readelf and grep.

---
_Auto-generated daily digest entry._
