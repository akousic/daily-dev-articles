# How GitHub uses eBPF to improve deployment safety

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-04-18 04:17
- **Original:** https://github.blog/engineering/infrastructure/how-github-uses-ebpf-to-improve-deployment-safety/

## Summary

How GitHub uses eBPF to improve deployment safety Learn how Github uses eBPF to detect and prevent circular dependencies in its deployment tooling. Did you know that, at GitHub, we host all of our own source code on github.com? We do this because we’re our own biggest customer—testing out changes internally before they go to users.

## Key Takeaways

- However, there’s one downside: If github.com were ever to go down, we wouldn’t be able to access our own source code.
- This is what you’d call a very simple circular dependency: to deploy GitHub, we needed GitHub.
- If GitHub is down, then we wouldn’t be able to deploy something to fix it.

---
_Auto-generated daily digest entry._
