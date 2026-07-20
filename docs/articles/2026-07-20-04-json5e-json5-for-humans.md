# JSON5E - JSON5 for Humans

- **Source:** Lobsters
- **Rank (today):** #4
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-07-20 04:02
- **Original:** https://github.com/boris-kolpackov/libpdjson5/blob/master/JSON5E.md

## Summary

JSON5E is an extension of the JSON5 format that aims to be even more natural to write and maintain by hand. Where JSON5 retains the overall JSON shape and draws on ECMAScript 5 for inspiration, JSON5E tries harder to approximate the look and feel of a typical configuration file found in /etc while retaining the JSON object model. Specifically, JSON5E extends JSON5 with the following syntax: - Implied top-level objects.

## Key Takeaways

- JSON5: { delay: 10, timeout: 30 }JSON5E: delay: 10, timeout: 30Note that top-level arrays and simple values are still supported (but there are no implied top-level arrays).
- - Newline in addition to comma as a separator.
- JSON5: { delay: 10, timeout: 30 }JSON5E: { delay: 10 timeout: 30 }Note that it must be a newline, not just a whitespace.

---
_Auto-generated daily digest entry._
