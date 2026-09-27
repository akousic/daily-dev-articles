# LuaRocks Security Incident September 2026

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-09-27 08:58
- **Original:** https://luarocks.org/security-incident-september-2026

## Summary

LuaRocks.org Security Incident, September 2026 On September 25th, 2026 we received a report of a remote code execution vulnerability in LuaRocks.org, coordinated through CISA. The vulnerability was fixed on September 26th. While investigating, we found that it had been exploited on the LuaRocks.org server several times between July 9th and August 20th, 2026.

## Key Takeaways

- Because an attacker was able to run code on the server, we are treating everything that server had access to as exposed.
- The site has been moved to a newly built server, and every credential the old server held has been revoked and replaced.
- We have not found any evidence that existing packages were modified.

---
_Auto-generated daily digest entry._
