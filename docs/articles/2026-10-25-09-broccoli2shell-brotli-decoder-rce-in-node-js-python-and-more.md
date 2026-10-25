# Broccoli2Shell: Brotli decoder RCE in Node.js, Python and more

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 375
- **Published (UTC):** 2026-10-24 08:06
- **Original:** https://broccoli2shell.com/

## Summary

Who's exposed You're at risk if your code, or any library it uses, decompresses Brotli data that someone else controls. That happens in more places than you'd think, because HTTP clients decompress Brotli responses on their own. - Your app fetches a URL Node's built-in fetch() decodes Content-Encoding: br responses automatically.

## Key Takeaways

- So do Python's requests/urllib3 and aiohttp whenever a Brotli package is installed.
- Any server you talk to can send the payload, whether through webhooks, link previews, crawlers or "import from URL" features.
- - Your app accepts uploads or request bodies Express 5.0.0–5.3.0 and body-parser 2.0.0–2.3.0 inflate Brotli request bodies in parsers such as raw() and json().

---
_Auto-generated daily digest entry._
