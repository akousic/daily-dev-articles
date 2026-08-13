# python's pre-declared constants are kinda weird

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-08-13 00:28
- **Original:** https://sebsite.pw/w/20260801-pythonconstants.html

## Summary

python has 6 pre-declared "constants": True, False, None, __debug__, Ellipsis (or equivalently ...), and NotImplemented. but they all behave slightly differently, for some reason. True, False, and None True, False, and None are keywords.

## Key Takeaways

- they aren't identifiers, they're just straight up their own lexical tokens.
- which is really weird; nothing else is like this in python.
- usually stuff is resolved during regular name resolution, not in the lexer itself.

---
_Auto-generated daily digest entry._
