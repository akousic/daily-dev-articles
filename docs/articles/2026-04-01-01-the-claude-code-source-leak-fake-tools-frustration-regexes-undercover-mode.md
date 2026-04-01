# The Claude Code Source Leak: fake tools, frustration regexes, undercover mode

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 1288
- **Published (UTC):** 2026-03-31 13:04
- **Original:** https://alex000kim.com/posts/2026-03-31-claude-code-source-leak/

## Summary

Update: see HN discussions about this post: https://news.ycombinator.com/item?id=47586778 I use Claude Code daily, so when Chaofan Shou noticed earlier today that Anthropic had shipped a .map file alongside their Claude Code npm package, one containing the full, readable source code of the CLI tool, I immediately wanted to look inside. The package has since been pulled, but not before the code was widely mirrored, including myself and picked apart on Hacker News. This is Anthropic’s second accidental exposure in a week (the model spec leak was just days ago), and some people on Twitter are starting to wonder if someone inside is doing this on purpose.

## Key Takeaways

- Probably not, but it’s a bad look either way.
- The timing is hard to ignore: just ten days ago, Anthropic sent legal threats to OpenCode, forcing them to remove built-in Claude authentication because third-party tools were using Claude Code’s internal APIs to access Opus at subscription rates instead of pay-per-token pricing.
- That whole saga makes some of the findings below more pointed.

---
_Auto-generated daily digest entry._
