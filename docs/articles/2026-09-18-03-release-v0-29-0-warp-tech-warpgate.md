# Release v0.29.0 · warp-tech/warpgate

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-09-18 09:21
- **Original:** https://github.com/warp-tech/warpgate/releases/tag/v0.29.0

## Summary

Note Would you kindly spend 5 minutes to give your feedback on your deployment and what you'd like to see in Warpgate? Multiple changes in this release have been proposed by users like you through this survey. Warning This release contains breaking API changes, meaning that existing API clients might not work anymore.

## Key Takeaways

- Compatible Terraform provider version: v1.2.0, Kubernetes operator: v0.4.11 Major new features Session approvals (JIT access) - #2563 You can set up targets to require an admin to approve each session before the connection is allowed, with configurable timeout and approval caching MFA enforcement policy - #2555 A global setting to require or prompt enrollment of a second factor for all users, with an option to exempt SSO users Default credential policy setting for new users - #2557 Editable under Config → Policies, the new policy applies to all new users by default Changes - Support tickets for Kubernetes access by @LarsSven in #2562 - Sessions are now split into user sessions and target sessions, so a single HTTP session lists all its target connections together in the admin UI by @Eugeny in #2499 - Kubernetes exec ,attach ,port-forward and debug container usage is now logged in the structured audit log by @huguesgr in #2558 - SSH host keys are now stored in the database instead of the data directory.
- Existing key files are imported automatically.
- in #2570 Security fixes [Minor] GHSA-hrfx-fm67-gv64 - Kubernetes clients see detailed error messages Affected versions: up to 0.29.0 Kubernetes clients see exact reasons for certificate validation failures and possibly database errors.

---
_Auto-generated daily digest entry._
