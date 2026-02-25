# Reducing the size of Go binaries by up to 77%

- **Source:** Lobsters
- **Rank (today):** #4
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-02-24 07:56
- **Original:** https://www.datadoghq.com/blog/engineering/agent-go-binaries/

## Summary

Pierre Gimalac Over the past few years, the Datadog Agent’s artifact size has grown significantly, from 428 MiB in version 7.16.0 to a peak of 1.22 GiB in version 7.60.0 on Linux. That growth reflected years of new capabilities, broader integrations, and support for more environments. But it also introduced real constraints in size-sensitive contexts like serverless platforms, IoT devices, and containerized workloads.

## Key Takeaways

- We didn’t want to stop adding functionality.
- Instead, we set out to bend the curve.
- Between versions 7.60.0 (December 2024) and 7.68.0 (July 2025), over the course of roughly 6 months, we reduced the size of our Go binaries by up to 77%, bringing artifacts close to where they were 5 years ago without removing features.

---
_Auto-generated daily digest entry._
