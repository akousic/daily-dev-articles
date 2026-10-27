# Uber Moves Beyond CPU Cores with Performance-Aware Scheduling for Stateful Workloads

- **Source:** InfoQ
- **Rank (today):** #6
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-10-27 19:19
- **Original:** https://www.infoq.com/news/2026/10/uber-cpu-stateful-workloads/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

Uber has introduced Normalized Compute Units (NCUs) to make CPU allocation more consistent across its highly heterogeneous server fleet. The approach, implemented in Uber's Odin stateful orchestration platform, accounts for differences in processor performance rather than treating every CPU core as equivalent. Odin manages around 5 million CPU cores across on-premises data centres and public clouds, including multiple generations of x86 hardware and ARM processors.

## Key Takeaways

- Uber found that single-threaded performance can vary by almost a factor of two between the fastest and slowest cores.
- Consequently, the same workload can require significantly different numbers of physical CPU cores depending on where it runs.
- The problem creates two competing risks.

---
_Auto-generated daily digest entry._
