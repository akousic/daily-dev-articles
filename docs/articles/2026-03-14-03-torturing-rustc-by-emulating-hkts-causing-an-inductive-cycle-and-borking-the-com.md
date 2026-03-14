# Torturing rustc by Emulating HKTs, Causing an Inductive Cycle and Borking the Compiler

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-03-14 00:51
- **Original:** https://www.harudagondi.space/blog/torturing-rustc-by-emulating-hkts/

## Summary

Torturing rustc by Emulating HKTs, Causing an Inductive Cycle and Borking the Compiler Table of Contents Prelude # On the 28th day of February of the year 2026, I was attempting to start writing an FP scripting language for fun. So I wrote up an Ast enum for a basic calculator to start: I realized that I wanted to add a way to include spans when I wanted or not. So here’s something I cooked up: Of course, since this is my project and I wanted to be a little bit silly, I went ahead and abstract this like a Java Enterprise Software Engineer but in an alternative universe where everything is Haskell.

## Key Takeaways

- So uh let’s add that to our Ast struct.
- That is… Rust does not have HKTs, kinda # Higher kinded types, or HKTs, is the notion that generics can have generics.
- That is, in something like struct Foo<T>(T<i32>); , T would be any specific type that hypothetically accepts one generic type.

---
_Auto-generated daily digest entry._
