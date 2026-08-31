# uv: Deduplicate all files in the wheel cache

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 196
- **Published (UTC):** 2026-08-31 06:03
- **Original:** https://github.com/astral-sh/uv/pull/21327

## Summary

Deduplicate all files in the wheel cache - #21327 Conversation | N.B. Slop comment for benchmark data. We benchmarked the optimization in 85c3f7485 against the binary-only cache at a3f977ece, with --preview-features content-addressed-cache enabled on both.

## Key Takeaways

- These are medians for the completeuv pip install process; positive changes mean slower.
- Before this optimization, the measured cold regressions were +4.02% for AnyIO 4.9.0, +19.41% for SymPy 1.14.0, +12.75% for NumPy 2.2.6, +15.30% for PyTorch 2.7.1+cpu.
- All eight median regressions are below 5%.

---
_Auto-generated daily digest entry._
