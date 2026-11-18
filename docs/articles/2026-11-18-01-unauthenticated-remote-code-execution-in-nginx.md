# Unauthenticated remote code execution in Nginx

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 882
- **Published (UTC):** 2026-11-18 15:19
- **Original:** https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities

## Summary

Wiz Research, Ikotas Labs, Metnir, Rapid7, and Xint independently uncovered two critical remote code execution vulnerabilities in NGINX, software used to receive and route traffic to production applications and APIs. Successful exploitation could let attackers take control of affected NGINX servers, steal sensitive data, tamper with websites, or disrupt services. The vulnerabilities, tracked as CVE-2026-123633 and CVE-2026-123007, are both rated Critical, with a CVSS 4.0 score of 9.2.

## Key Takeaways

- The flaws are in NGINX itself.
- Websites and APIs can be exposed even when their own application code is secure.
- Both vulnerabilities require HTTP/2 to be enabled on the affected NGINX server.

---
_Auto-generated daily digest entry._
