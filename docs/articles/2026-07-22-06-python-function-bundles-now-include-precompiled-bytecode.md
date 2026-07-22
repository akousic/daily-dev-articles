# Python function bundles now include precompiled bytecode

- **Source:** Vercel
- **Rank (today):** #6
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-07-22 15:45
- **Original:** https://vercel.com/changelog/python-function-bundles-now-include-precompiled-bytecode

## Summary

Vercel now compiles Python functions to bytecode at build time. In our benchmarks, cold starts for the median-sized function dropped from 2.8s to 1.3s. Cold starts are already rare in practice.

## Key Takeaways

- Pre-warmed instances keep at least one function instance active for production deployments on paid plans, and automatic concurrency scaling reduces how often new instances start cold.
- Precompiling to bytecode makes starts faster across the board, so proactive initialization finishes sooner and fewer requests ever hit a cold start.
- When Python imports a module without cached bytecode, it parses and compiles the source before executing it.

---
_Auto-generated daily digest entry._
