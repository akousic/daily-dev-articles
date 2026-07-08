# Jim's TrueType QR Code Font

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-07-07 22:58
- **Original:** https://qr.jim.sh/

## Summary

Jim's TrueType QR Code Font This is a real TrueType/OpenType font that turns bracketed text into QR codes during text shaping. There is no separate image generation or preprocessing step: type text like [hello], apply the font, and the font's built-in OpenType rules render the QR code. Because the QR code is still text, you can copy and paste the rendered QR block as ordinary characters, store it in plain text, or mix it inline with regular Latin text.

## Key Takeaways

- Text outside brackets remains readable.
- Browser Line-Wrapping Note: Because layout engines perform line-breaking on the Unicode text before shaping, browsers may split a QR code across lines if it contains break opportunities (like spaces, dots, or slashes) and hits the edge of a text container.
- For reliable rendering in HTML, wrap the bracketed block in a container styled with white-space: nowrap; or display: inline-block;.

---
_Auto-generated daily digest entry._
