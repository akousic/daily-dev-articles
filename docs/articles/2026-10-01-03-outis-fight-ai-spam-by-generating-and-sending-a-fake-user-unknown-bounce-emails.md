# outis: Fight AI spam by generating and sending a fake "user unknown" bounce emails

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-10-01 10:54
- **Original:** https://github.com/dtonon/outis

## Summary

Outis fights spam generating and sends a fake "user unknown" bounce for an email you received, so the sender believes your address does not exist. This should work well for the recent trend of AI-generated automated emails, where the sender may expect a reply; it helps to clean your email from their list. Outis (Οὖτις) is Greek for "nobody".

## Key Takeaways

- In the Odyssey, Odysseus gives it as his name to the Cyclops Polyphemus, so that when the blinded giant calls for help and shouts that "Nobody" is hurting him, the other Cyclopes leave.
- The tool does the same for your mailbox: it tells whoever is asking that there is nobody here.
- The bounce is an RFC 3464 delivery status notification modelled on Postfix: multipart/report with a human-readable part, a message/delivery-status part with status 5.1.1, and the original message attached as message/rfc822.

---
_Auto-generated daily digest entry._
