# Go: Support for Generic Methods

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 292
- **Published (UTC):** 2026-05-27 09:02
- **Original:** https://github.com/golang/go/issues/77273

## Summary

Proposal: Generic Methods for Go A change of view. Background For clarity, in the following we use the term concrete method (or just method when the context is clear) to describe a non-interface method declared like a function but with a receiver; and we use the term interface method to describe the name and signature of a method of an interface. Per the current spec, a concrete method is a function with a receiver.

## Key Takeaways

- Syntactically this is not quite true: while functions can be generic, methods cannot.
- They cannot declare new type parameters themselves; but they can have a receiver of a generic type (and thus have method-local names for the type parameters of the receiver type).
- A reason for this discrepancy is that we have historically viewed the primary role of methods as a means to implement an interface: permitting type parameters on concrete methods would imply that we must also permit type parameters on interface methods.

---
_Auto-generated daily digest entry._
