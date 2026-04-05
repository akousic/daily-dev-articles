# AWS engineer reports PostgreSQL perf halved by Linux 7.0, fix may not be easy

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 355
- **Published (UTC):** 2026-04-05 00:13
- **Original:** https://www.phoronix.com/news/Linux-7.0-AWS-PostgreSQL-Drop

## Summary

AWS Engineer Reports PostgreSQL Performance Halved By Linux 7.0, But A Fix May Not Be Easy An Amazon/AWS engineer raised the alarms on Friday over the current Linux 7.0 development kernel leading to the throughput for the PostgreSQL database server being around half that of prior kernel versions. The culprit halving the PostgreSQL performance is known but a revert looks like it may not happen and currently suggesting that PostgreSQL may need to be adapted. Salvatore Dipietro of Amazon/AWS reported a throughput and latency regression for PostgreSQL.

## Key Takeaways

- They found Linux 7.0 in its near-final form delivering around 0.51x the throughputof prior kernels on a Graviton4 server due to now much more time being spent in a user-space spinlock.
- Bisecting the regression was traced back to the Linux 7.0 change of restricting the available preemption modes for the kernel.
- That change was previously covered on Phoronix within Linux 7.0 To Focus Just On Full & Lazy Preemption Models For Up-To-Date CPU Archs and in turn upstreamed with the Linux 7.0 scheduler updates.

---
_Auto-generated daily digest entry._
