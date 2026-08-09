# Who Should Pay For Source Code Availability?

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-08-09 08:42
- **Original:** https://kristoff.it/blog/source-code-availability/

## Summary

Who Should Pay For Source Code Availability? I have a project (Zine, a static site generator) that has 11 dependencies hosted across GitHub, Codeberg, and self-hosted Forgejo instances. Whenever GitHub or Codeberg is down, fresh builds of my project will fail.

## Key Takeaways

- While self-hosted Forgejo instances have significantly better uptime than GitHub, they are at greater risk of eventually going down for good and breaking my project permanently.
- The most direct and practical solution to this problem is to fork/vendor everything.
- Forking means moving all dependencies to the same host where Zine is.

---
_Auto-generated daily digest entry._
