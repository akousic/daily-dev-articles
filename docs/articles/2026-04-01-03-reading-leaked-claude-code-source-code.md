# Reading leaked Claude Code source code

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-03-31 17:55
- **Original:** https://lr0.org/blog/p/claude-code-source/

## Summary

Reading leaked Claude Code source code Interesting findings from reading 132,000 lines of TypeScript that power Claude Code. The post uses the repo at https://github.com/chatgptprojects/claude-code to reference code, note that it might go down by the time you are reading this. [2026-04-01 Wed 00:53]: after writing this, I found another interesting read by Alex Kim's blog Anthropic accidentally leaked a source map file (cli.js.map ) containing the full, unobfuscated TypeScript source code.

## Key Takeaways

- 1,897 files around 132,000 LOC.
- What I found is a piece of software that is surprisingly more opinionated and more paranoid than I expected.
- Here are some of things that I found worth talking about.

---
_Auto-generated daily digest entry._
