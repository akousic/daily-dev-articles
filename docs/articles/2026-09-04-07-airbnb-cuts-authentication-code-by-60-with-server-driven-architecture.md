# Airbnb Cuts Authentication Code by 60% with Server Driven Architecture

- **Source:** InfoQ
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-09-04 17:32
- **Original:** https://www.infoq.com/news/2026/09/airbnb-server-driven-login/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

Airbnb has redesigned its authentication architecture to make login flows easier to change across Web, iOS, and Android. The new system moves authentication decisions from clients to a server-side policy engine that selects the most appropriate authentication challenge based on the user and session context. According to Airbnb, the redesign reduced authentication-related code by 60%, reduced the web client bundle by 100 KB, increased successful authentication by 2.6%, and reduced duplicate account creation by 27%.

## Key Takeaways

- Airbnb’s Identify-then-Challenge Architecture (Source: Airbnb Blog Post) The architecture separates authentication into two stages.
- First, users identify the account they want to access using an email address, phone number, or social login.
- The server then evaluates account and session information and uses a configurable policy engine to select the challenge most likely to succeed.

---
_Auto-generated daily digest entry._
