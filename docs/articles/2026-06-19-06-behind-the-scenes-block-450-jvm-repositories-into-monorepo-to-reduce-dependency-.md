# Behind the Scenes:  Block 450 JVM Repositories Into Monorepo to Reduce Dependency Drift

- **Source:** InfoQ
- **Rank (today):** #6
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-06-19 16:35
- **Original:** https://www.infoq.com/news/2026/06/block-450-jvm-monorepo-migration/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

has described a large-scale migration from a polyrepo architecture to a monorepo across its Cash App and Square engineering organizations to address growing coordination and dependency management challenges across backend systems. The initiative consolidated approximately 450 JVM-based repositories into a single codebase to simplify cross-service development, improve dependency visibility, and reduce operational friction across distributed systems. According to the Block engineering team, the monorepo now supports approximately 8,800 builds per week, with p90 CI times of around 10 minutes on a reliably green main branch.

## Key Takeaways

- Under the previous polyrepo model, services and shared libraries were maintained in separate repositories, allowing teams to operate independently while introducing increasing coordination complexity over time.
- The model led to dependency version drift, duplicated upgrade efforts, and an increased risk of runtime incompatibilities across JVM services, including classic diamond dependency surprises.
- Gabor Pap, Senior Engineering Manager at Block, mentioned, What started as a complex, large-scale migration became a step-change in developer experience: a modern, cohesive codebase with an optimized IDE workflow, dramatically faster CI, and a foundation built for long-term velocity.

---
_Auto-generated daily digest entry._
