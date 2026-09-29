# Pining for Arc Downcasting in Rust

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-09-29 10:35
- **Original:** https://wolfgirl.dev/blog/2026-09-29-pining-for-arc-downcasting-in-rust/

## Summary

In the course of writing my build driver, I came across a bit of an unusual problem, for which I made a bit of an usual solution. I think the solution is interesting and would like to talk about it, but to understand anything we must first understand the problem at hand. Consider The Case Of The Humble Concurrent Cache Suppose we have some expensive function we'd like to put a cache in front of.

## Key Takeaways

- Furthermore, suppose we'd like to access this cache from multiple threads.
- A simple example follows (playground link): enum JSON { F64(f64), String(String), Vec(Vec<JSON>), Object(HashMap<String, JSON>), } struct Proxy { client: HTTPClient, cache: RWLock<HashMap<String, JSON>>, } impl Proxy { fn get(&self, key: &str) -> JSON { // 1.
- { let cache = self.cache.read().unwrap(); if let Some(value) = cache.get(key) { return value.clone(); } } // 2.

---
_Auto-generated daily digest entry._
