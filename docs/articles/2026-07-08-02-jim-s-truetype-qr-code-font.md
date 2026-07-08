# Jim's TrueType QR Code Font

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 205
- **Published (UTC):** 2026-07-07 16:30
- **Original:** https://github.com/jimparis/qr-font

## Summary

Live Demo: https://qr.jim.sh/ Downloads: - qrfont-1L.ttf (21x21 modules, up to 17 characters) - qrfont-2L.ttf (25x25 modules, up to 32 characters) - qrfont-3L.ttf (29x29 modules, up to 53 characters) This repo generates an experimental OpenType font that turns bracket-delimited text into a QR Code symbol while leaving surrounding text readable. abc[hello]ghi All fonts use: - Byte mode - Printable ASCII input - Fixed mask pattern 0 - [and- ]as delimiters The fonts are generated rather than hand-authored. The build script emits glyph outlines and GSUB feature logic, then compiles them into dist/qrfont-*.ttf.

## Key Takeaways

- The default build compiles the delimiter parser, byte expansion, Reed-Solomon parity circuit, QR module placement, and fixed mask rendering.
- Printable ASCII glyphs are copied from Liberation Sans Regular, scaled into the QR Font em square, so text outside bracketed QR blocks renders as ordinary text in the same font.
- Liberation is a reserved font name under the source font license, so the generated families are named QR Font 1-L, QR Font 2-L, and QR Font 3-L.

---
_Auto-generated daily digest entry._
