# Dropbox Collaborates with GitHub to Reduce Monorepo Size from 87GB to 20GB

- **Source:** InfoQ
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-04-22 15:20
- **Original:** https://www.infoq.com/news/2026/04/dropbox-reduces-git-optimization/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

Dropbox engineers have reduced the size of their backend monorepo from 87GB to 20GB by addressing inefficiencies in Git’s storage and delta compression model, improving developer productivity and continuous integration performance. The effort was driven by scaling challenges in a repository that serves as a central integration point for backend services and shared libraries across teams at Dropbox. As the monorepo grew, engineering teams began experiencing slow clone operations that could take over an hour, along with degraded CI pipeline performance due to repeated fetch and build overhead.

## Key Takeaways

- The expansion also increased the risk of reaching repository hosting limits.
- According to Dropbox engineering findings, the issue was not primarily caused by large binaries or accidental commits, but by how Git’s internal compression heuristics handled large sets of related files.
- Git uses delta compression to reduce storage by identifying similarities between files and storing differences efficiently.

---
_Auto-generated daily digest entry._
