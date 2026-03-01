# Argo CD 3.3 Brings Safer GitOps Deletions and Smoother Day‑to‑Day Operations

- **Source:** InfoQ
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-03-01 14:32
- **Original:** https://www.infoq.com/news/2026/02/argocd-33/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

The application deployment and lifecycle management tool Argo CD has reached a new milestone with the release of version 3.3, extending the capabilities of the popular GitOps continuous delivery tool while addressing several long-standing pain points for operators. Argo CD 3.3 is presented as a practical release that closes several long-standing gaps in day-to-day GitOps operations rather than a major architectural change. The release candidate focuses on deletion safety, authentication experience, repository performance and more precise control for cluster and autoscaling resources.

## Key Takeaways

- In the announcement blog post, published at the time when the release candidate became available, software engineer Peter Jiang introduces PreDelete hooks as the most visible change in Argo CD 3.3, completing the existing lifecycle of PreSync , Sync and PostSync hooks.
- In the blog, Jiang explains that users have historically relied on external scripts, manual cleanup or Kubernetes finalisers to prepare for application deletion, which often proved fragile or opaque when teams needed a predictable teardown sequence.
- PreDelete hooks instead allow teams to define Kubernetes resources, such as Jobs that must run and succeed before Argo CD proceeds with deleting the rest of an application's resources, and a failing hook will block deletion.

---
_Auto-generated daily digest entry._
