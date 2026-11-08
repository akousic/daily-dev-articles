# Show HN: Coldframe, a honeypot that poses as a supermarket fridge controller

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 268
- **Published (UTC):** 2026-11-07 17:27
- **Original:** https://github.com/hedgerow-dev/coldframe

## Summary

A honeypot for supermarket refrigeration controllers. In 2026, attackers broke into internet-facing refrigeration supervisors across Europe using default passwords and old, unpatched firmware, then forced defrost cycles. coldframe pretends to be one of those controllers.

## Key Takeaways

- It records who connects, what passwords they try and which public exploits they use, and it never gives them anything real.
- It is one Python file with no dependencies outside the standard library.
- | Persona | Pretends to be | What it serves | |---|---|---| | danfoss | Danfoss AK-SM 800A system manager | StoreView login, a fake store dashboard, the XML API at /html/xml.cgi and /xml.cgi, HTTP and HTTPS | | dixell | Copeland/Dixell XWEB EVO supervisor | Login page and the XWEB 500 CGI paths targeted by public exploits | The Danfoss persona copies what internet scanners record for real AK-SM 800A units: the nginx server header and header order, the Danfoss StoreView page title, TLS 1.2 only, and a 1-year certificate for CN=DanfossSM800A issued by a SelfSigned-DanfossSM800A authority.

---
_Auto-generated daily digest entry._
