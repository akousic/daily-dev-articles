# tropius: detect AI tropes in prose

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-06-25 04:23
- **Original:** https://tangled.org/desertthunder.dev/tropius

## Summary

tropius# tropius is a CLI to detect AI tropes in prose. How# We use a pattern dictionary in TOML based on a trope list from Tropes.fyi Text ↓ Aho-Corasick phrase matcher ↓ Structural, repetition, and character-class detectors ↓ Findings report Usage# Scan text from stdin: printf 'Let us delve into this robust ecosystem.' | cargo run -q -p tropius-cli Scan article text extracted from a live URL with lectito: # Install lectito cargo install lectito-cli lectito 'https://www.solo.io/blog/what-is-agent-identity-human-workload-a-new-layer' \ --format text \ | cargo run -q -p tropius-cli The CLI exits 0 when no findings are found and 1 when it finds trope signals. It exits 2 for usage or configuration errors.

## Key Takeaways

- Color output respects NO_COLOR.
- Coverage# - an implementation path for every source section in tropes.md - phrase patterns for literal trope signals - structural detectors for sentence and paragraph shape - repetition detectors for repeated metaphor terms and duplicated content - markdown-aware detection for bold-first bullets - character-class detection for Unicode decoration Inspiration# I got nerd-sniped on BlueSky Samuel - @samuel.fm 2026-06-25 04:16 “Claudesmell” labeller for standard.site records wen owais - @desertthunder.dev 2026-06-25 04:18 what does claudesmell mean here Samuel - @samuel.fm 2026-06-25 04:22 smells of claude, e.g.
- short, punchy yet needlessly florid prose, excessive claudeisms, it’s not just x it’s y etc owais - @desertthunder.dev 2026-06-25 04:26 You know that feeling of nerd-sniping about to happen?

---
_Auto-generated daily digest entry._
