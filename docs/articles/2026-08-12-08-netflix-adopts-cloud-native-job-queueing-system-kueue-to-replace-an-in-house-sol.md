# Netflix Adopts Cloud-Native Job Queueing System Kueue to Replace an In-House Solution

- **Source:** InfoQ
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-08-12 15:04
- **Original:** https://www.infoq.com/news/2026/08/netflix-kueue-kubernetes-batch/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

Netflix migrated most of its batch workloads onto Kueue, an open-source cloud-native batch job execution system that has outgrown its homegrown solution over the years. The company mapped the capabilities previously created in-house to Kueue’s functionality and also benefited from new features that would have been costly to incorporate into its homegrown solution. Engineers used API parity with the existing system to derisk the project and allow for a gradual and seamless migration.

## Key Takeaways

- Over the years, Netflix created a range of bespoke solutions for Titus, its container platform, including Compute Managed Batch (CMB) for managing and executing batch jobs on top of containerized compute.
- CMB managed capacity using tenant hierarchies and was able to federate workloads across multiple cells (Kubernetes clusters), leveraging Titus’ control plane APIs.
- The company observed that since CMB’s creation in 2018, many of its key features have been incorporated into open-source projects that evolved within the Kubernetes ecosystem.

---
_Auto-generated daily digest entry._
