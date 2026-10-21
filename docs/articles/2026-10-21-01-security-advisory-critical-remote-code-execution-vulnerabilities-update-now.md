# Security advisory: Critical remote code execution vulnerabilities, update now

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 1471
- **Published (UTC):** 2026-10-20 20:15
- **Original:** https://www.php.net/archive/2026.php#2026-10-21-5

## Summary

Security advisory: Critical remote code execution vulnerabilities, update now PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35 fix two critical vulnerabilities that can allow unauthenticated remote code execution. All PHP users are strongly encouraged to update immediately. Who is at risk: all PHP installations serving web requests, including PHP-FPM, Apache with mod_php, php-cgi, FrankenPHP and LiteSpeed.

## Key Takeaways

- We consider the risk highest for mod_php, with a demonstrated exploit where an unauthenticated request can trigger the attack before any application code runs.
- The vulnerabilities: - RCE via OOM corruption, CVE-2026-109618 (GHSA-w8hw-w9fx-j79w): out-of-memory handling can interrupt PHP while internal request data is only partially initialized.
- Request cleanup may then treat the invalid data as valid.

---
_Auto-generated daily digest entry._
