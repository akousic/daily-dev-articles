# What's in a tag name? JavaScript, apparently

- **Source:** Lobsters
- **Rank (today):** #4
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-08-26 01:36
- **Original:** https://portswigger.net/research/whats-in-a-tag-name-javascript-apparently

## Summary

Published: Tuesday, 25 August 2026 at 14:24 UTC Updated: Tuesday, 25 August 2026 at 14:24 UTC I was on my laptop, as I often am when there's rubbish on telly, and found myself wondering what characters are allowed in a tag. I knew they had to begin with "a-zA-Z", but what about after that? I tried placing alert(1) in the tag name and remembered that the browser converts everything to uppercase.

## Key Takeaways

- Then I wondered whether another property existed that didn't do that.
- I gave my tag an id attribute and inspected it in DevTools using console.dir(x).
- Carefully inspecting each property, I saw that "localName" contained a lowercase version of the tag name.

---
_Auto-generated daily digest entry._
