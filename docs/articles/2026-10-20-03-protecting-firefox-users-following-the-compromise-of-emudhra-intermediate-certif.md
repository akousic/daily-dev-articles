# Protecting Firefox users following the compromise of eMudhra intermediate certificates

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-10-20 08:00
- **Original:** https://blog.mozilla.org/security/2026/10/20/protecting-firefox-users-following-the-compromise-of-emudhra-intermediate-certificates/

## Summary

On Saturday, October 17, at 20:06 UTC, Mozilla received a report that private keys associated with eight eMudhra intermediate certificates had been compromised. These keys could allow attackers to issue fraudulent HTTPS certificates for websites they do not control. An attacker who could intercept a user’s connection could use those certificates to impersonate websites and potentially read or modify traffic.

## Key Takeaways

- Mozilla engineers responded immediately, blocking the affected certificates in Firefox using OneCRL, Mozilla’s centralized list of revoked certificates.
- OneCRL delivers this protection without requiring users to update or restart Firefox.
- By 22:59 UTC that same day, in less than 3 hours after we received the report, the updated OneCRL distribution was complete for all Firefox users with standard configurations.

---
_Auto-generated daily digest entry._
