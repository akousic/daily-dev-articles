# The Physics of Memory (aka can Javascript ECS?)

- **Source:** Lobsters
- **Rank (today):** #4
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-07-01 23:23
- **Original:** https://www.dmurph.com/posts/2026/06/ecs_vs_oop_benchmark/ecs_vs_oop_benchmark.html

## Summary

The Physics of Memory I’ve heard that many algorithms, like sorting, are improved quite a bit when the accessed data has high memory-locality (e.g. the CPU can load all of the relevant information in it’s L1/L2 cache for processing, instead of hitting RAM). A common way to work with this is using the Entity Component System (ECS) software architecture.

## Key Takeaways

- However, it can be difficult to achieve this memory layout for interpreted or OOP languages (Java, Python, Javscript), as they often don’t offer the developer as much control over their object memory location.
- My question is: Is it possible to use an ECS-style architecture in Javascript?
- And for applicable operations, does that actually do better than objects + V8’s garbage collection?

---
_Auto-generated daily digest entry._
