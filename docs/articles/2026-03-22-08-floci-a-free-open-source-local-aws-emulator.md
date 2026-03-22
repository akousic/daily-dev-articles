# Floci – A free, open-source local AWS emulator

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 232
- **Published (UTC):** 2026-03-21 21:49
- **Original:** https://github.com/hectorvent/floci

## Summary

Named after floccus — the cloud formation that looks exactly like popcorn. A free, open-source local AWS emulator. Just docker compose up .

## Key Takeaways

- LocalStack's community edition sunset in March 2026 — requiring auth tokens, dropping CI support, and freezing security updates.
- Floci is the no-strings-attached alternative.
- | Floci | LocalStack Community | | |---|---|---| | Auth token required | No | Yes (since March 2026) | | CI/CD support | Unlimited | Requires paid plan | | Security updates | Yes | Frozen | | Startup time | ~24 ms | ~3.3 s | | Idle memory | ~13 MiB | ~143 MiB | | Docker image size | ~90 MB | ~1.0 GB | | License | MIT | Restricted | | API Gateway v2 / HTTP API | ✅ | ❌ | | Cognito | ✅ | ❌ | | ElastiCache (Redis + IAM auth) | ✅ | ❌ | | RDS (PostgreSQL + MySQL + IAM auth) | ✅ | ❌ | | S3 Object Lock (COMPLIANCE / GOVERNANCE) | ✅ | | | DynamoDB Streams | ✅ | | | IAM (users, roles, policies, groups) | ✅ | | | STS (all 7 operations) | ✅ | | | Kinesis (streams, shards, fan-out) | ✅ | | | KMS (sign, verify, re-encrypt) | ✅ | | | Native binary | ✅ ~40 MB | ❌ | 20+ services.

---
_Auto-generated daily digest entry._
