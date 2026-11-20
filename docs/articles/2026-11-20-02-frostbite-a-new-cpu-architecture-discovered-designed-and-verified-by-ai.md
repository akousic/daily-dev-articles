# Frostbite: A new CPU architecture discovered, designed and verified by AI

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 574
- **Published (UTC):** 2026-11-20 10:01
- **Original:** https://architectlabs.com/blog/frostbite

## Summary

Introducing Frostbite: A new CPU architecture discovered, designed, and verified end-to-end by AI Abstract In our previous post, Redwood, we showed that given an architecture, our AI systems could implement, verify, and deploy an inference accelerator in record time. However, similar to other scientific domains, we believe that AI systems, given the correct freedom and guardrails, can co-design software and hardware together, making optimizations across the stack and opening a design space so large it was previously inaccessible. We set out to answer the question: “Could our AI systems & tools lead to a novel hardware discovery that radically outperforms human-made designs?” Today, we're introducing Frostbite, a general-purpose CPU with a new instruction set built from the ground up.

## Key Takeaways

- Frostbite exploits the properties of interaction nets, namely that every step is local, every dependency is explicit, and every value has exactly one owner, to reach a step-function gain in CPU performance that has long stagnated.
- On a set of 25 initially chosen workloads, including 15 held out until the final evaluation, we achieved a 4.59x performance-per-watt multiple when compared to a modern, silicon-proven superscalar (dual-issue, in-order) CPU core.
- Our AI systems autonomously iterated over the compiler, ISA, architecture, microarchitecture, RTL, verification, and final GDS.

---
_Auto-generated daily digest entry._
