# Squalk: an old-school forum engine built on Nostr (NIP-29 groups, NIP-7D threads)

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-09-21 09:44
- **Original:** https://github.com/dtonon/squalk

## Summary

Squalk is a forum built on Nostr that permits to manage simple or large communities; in fact you can choose to setup it in "simple" or "full" mode. Simple mode expose a single forum, while in Full mode you can have as many forum as you like. Each forum includes a chat feature in the right-hand sidebar, which is useful for quickly interacting with members.

## Key Takeaways

- Squalk is built on Nostr and implement NIP-29 and NIP-7D.
- It needs a personal relay that supports NIP-29 to host the group(s) and a Blossom server for the uploads; Pyramid includes both and is the suggested solution.
- Squalk is configured entirely through environment variables (all prefixed PUBLIC_, since they are read in the browser).

---
_Auto-generated daily digest entry._
