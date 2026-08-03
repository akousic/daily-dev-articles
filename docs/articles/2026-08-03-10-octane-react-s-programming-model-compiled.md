# Octane – React's programming model, compiled

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 97
- **Published (UTC):** 2026-08-03 08:04
- **Original:** https://octanejs.dev

## Summary

No rules of hooks No dependency arrays and no rules of hooks. The compiler tracks what your effects, memos and callbacks actually use, and hooks can sit behind conditions or early returns. The successor to Inferno, carrying its performance-first goal forward: React’s hooks, Suspense and actions, compiled ahead of time.

## Key Takeaways

- No hand-maintained dependency arrays — the compiler works out what your code captures for you.
- // Counter.tsrx — hooks next to output, no rules of hooks import { useState, useEffect } from 'octane'; export function Counter(props) @{ const [count, setCount] = useState(0); // A hook behind a condition is fine — slots are // assigned by call site, not call order.
- if (!props.paused) { useEffect(() => { console.log('count is now', count); }); // the compiler infers [count] } <button onClick={() => setCount(count + 1)}>{'Count: ' + count}</button> }// count is now 0 Independent use() calls start together instead of suspending one at a time down the tree.

---
_Auto-generated daily digest entry._
