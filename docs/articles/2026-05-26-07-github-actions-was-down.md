# GitHub Actions was down

- **Source:** Hacker News
- **Rank (today):** #7
- **Ranking metrics:** HN score 634
- **Published (UTC):** 2026-05-26 11:42
- **Original:** https://www.githubstatus.com/?today

## Summary

Resolved - On May 12, 2026, between 13:41 and 17:43 UTC, some services experienced delays in processing. For the Code Scanning service, 53% of check runs took over 15 minutes to complete. Additionally, notifications took an average of 22 minutes to be delivered and Slack integration webhooks took an average of 20 minutes to be delivered.

## Key Takeaways

- The delays were caused by replication lag due to an internal database migration, resulting in insufficient worker capacity for our high rate of job enqueues.
- We mitigated the impact by scaling our processing workers to handle the increased load.
- All services returned to normal processing times after the mitigation was applied.

---
_Auto-generated daily digest entry._
