# AI coding has made CI a bottleneck, so we reworked ours to keep up

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 303
- **Published (UTC):** 2026-09-21 19:23
- **Original:** https://linear.app/now/ci-bottleneck-reworked

## Summary

AI coding has made CI a bottleneck, so we reworked ours to keep up Earlier this year, I opened Linear to find that Tuomas, our CTO, had assigned an issue to me, titled “CI costs are high.” While I was at it, he also wanted me to make CI faster. Agents have made it exponentially faster to ship code, but validating those changes hasn’t quite kept up at the same rate. Every PR still has to pass through CI, so as development accelerates, CI becomes a bottleneck, driving up infrastructure costs and leaving developers and agents waiting longer for feedback.

## Key Takeaways

- In our pursuit to make CI more performant at Linear, we optimized for how long a PR waits on CI and how much runner time it consumes.
- Despite our test suites almost quadrupling since the start of the year, we brought pull request wait time down from more than 6 minutes to just over 5, while cutting runner time per test roughly in half.
- Broadly, we improved CI in four ways: - Upgraded infrastructure and tooling - Optimized the jobs that gate other work - Reduced repeated setup - Made test execution more efficient Linear’s codebase is primarily TypeScript, but many of these optimizations apply across languages and toolchains.

---
_Auto-generated daily digest entry._
