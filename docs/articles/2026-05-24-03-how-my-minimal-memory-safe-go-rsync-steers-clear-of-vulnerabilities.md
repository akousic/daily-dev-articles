# How my minimal, memory-safe Go rsync steers clear of vulnerabilities

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-05-24 09:38
- **Original:** https://michael.stapelberg.ch/posts/2026-05-24-minimal-memory-safe-go-rsync-vulns/

## Summary

Table of contents Back in January 2025, multiple different security researchers published a total of 6 security vulnerabilities in rsync, some of which allow arbitrary code execution and file leaks, so naturally I was wondering whether/how my gokrazy/rsync implementation was affected. Did implementing my own (compatible, but minimal) rsync in Go, a modern and memory-safe programming language, really rule out entire classes of security vulnerabilities? This deep dive article was in the making since January 2025, but was delayed because we uncovered more unpublished vulnerabilities in the process!

## Key Takeaways

- The “Security Vulnerabilities” section now covers all 12 vulnerabilities from the January 2025 batch and the May 2026 batch.
- If you are running (upstream, samba) rsync in production, upgrade to version 3.4.3 or newer.
- If you are running gokrazy/rsync in production, upgrade to version v0.3.3 or newer.

---
_Auto-generated daily digest entry._
