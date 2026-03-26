# A one-line Kubernetes fix that saved 600 hours a year

- **Source:** Cloudflare
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-03-26 15:15
- **Original:** https://blog.cloudflare.com/one-line-kubernetes-fix-saved-600-hours-a-year/

## Summary

Every time we restarted Atlantis, the tool we use to plan and apply Terraform changes, we’d be stuck for 30 minutes waiting for it to come back up. No plans, no applies, no infrastructure changes for any repository managed by Atlantis. With roughly 100 restarts a month for credential rotations and unboarding, that added up to over 50 hours of blocked engineering time every month, and paged the on-call engineer every time.

## Key Takeaways

- This was ultimately caused by a safe default in Kubernetes that had silently become a bottleneck as the persistent volume used by Atlantis grew to millions of files.
- Here’s how we tracked it down and fixed it with a one-line change.
- Mysteriously slow restarts We manage dozens of Terraform projects with GitLab merge requests (MRs) using Atlantis, which handles planning and applying.

---
_Auto-generated daily digest entry._
