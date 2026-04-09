# Open Source Security at Astral

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 291
- **Published (UTC):** 2026-04-09 04:11
- **Original:** https://astral.sh/blog/open-source-security-at-astral

## Summary

Astral builds tools that millions of developers around the world depend on and trust. That trust includes confidence in our security posture: developers reasonably expect that our tools (and the processes that build, test, and release them) are secure. The rise of supply chain attacks, typified by the recent Trivy and LiteLLM hacks, has developers questioning whether they can trust their tools.

## Key Takeaways

- To that end, we want to share some of the techniques we use to secure our tools in the hope that they're useful to: - Our users, who want to understand what we do to keep their systems secure; - Other maintainers, projects, and companies, who may benefit from some of the techniques we use; - Developers of CI/CD systems, so that projects do not need to follow non-obvious paths or avoid useful features to maintain secure and robust processes.
- CI/CD security # We sustain our development velocity on Ruff, uv, and ty through extensive CI/CD workflows that run on GitHub Actions.
- Without these workflows we would struggle to review, test, and release our tools at the pace and to the degree of confidence that we demand.

---
_Auto-generated daily digest entry._
