# Security incident on Hex.pm

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-11-24 08:52
- **Original:** https://hex.pm/blog/security-incident-on-hexpm

## Summary

On November 23, 2026, an unauthorized third party exploited a vulnerability in hex.pm that let them run commands on our web servers. We blocked the traffic and deployed a fix within 20 minutes. Shortly afterwards we received a report of this exact vulnerability.

## Key Takeaways

- We found no evidence of unauthorized package modifications, or database changes, or that the attacker maintained access to our systems.
- However, because database reads are not logged, we cannot rule out that the attacker accessed data stored in the database, including email addresses, password hashes, API key hashes, 2FA secrets, sessions, and audit logs.
- Because email addresses may have been exposed, be careful with emails that claim to come from Hex.

---
_Auto-generated daily digest entry._
