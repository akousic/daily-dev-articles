# How to Bypass Rust's Orphan Rule

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-11-17 09:35
- **Original:** https://edvong.com/bypass-orphan-rule/

## Summary

How to Bypass Rust's Orphan Rule Write Rust for long enough, and you are bound to run into error[E0117]. Take a simple, everyday scenario. You pull in a serialization library that defines a ToJson trait, along with a third-party type library like uuid.

## Key Takeaways

- You want to turn a uuid::Uuid into JSON, so you naturally write: impl ToJson for uuid::Uuid { fn to_json(&self) -> String { format!("\"{}\"", self) } } And the compiler immediately stops you: error[E0117]: only traits defined in the current crate can be implemented for types defined outside of the crate This is Rust's well-known Orphan Rule.
- Once people hit this wall, they usually either complain that the compiler is too rigid or dutifully wrap the type in a NewType.
- But if you look closely at how the Orphan Rule actually works, it is not a dead end.

---
_Auto-generated daily digest entry._
