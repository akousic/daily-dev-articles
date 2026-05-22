# C Programming Language Quiz

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-05-22 01:49
- **Original:** https://stefansf.de/c-quiz/

## Summary

C Programming Language Quiz This quiz is about quirks of the programming language C and intended for fun and educational purpose. The one or the other question is more academic, i.e., it should make you think ;-) Unless otherwise stated, the questions and corresponding answers are independent of a specific version of the C standard. Thus the answers are the same considering C89 up to and including C17 and probably future releases.

## Key Takeaways

- - If two pointers p andq of the same type point to the same address, thenp == q must evaluate to true.YesNoShort answer: Comparing two pointers which are derived from two different objects which are not part of the same aggregate or union object invokes undefined behavior.
- Have a look at this post for a detailed discussion.
- - Consider the following code snippet where an object of type int is accessed through lvalues of typeshort andunsigned char :(A) and(B) invoke undefined behavior(A) invokes undefined behavior but(B) is legal(B) invokes undefined behavior but(A) is legal(A) and(B) are legalThe rule of thumb is: accessing an object of type T through an lvalue of typeU whereT andU are not compatible (modulo few exceptions) invokes undefined behavior—according to the strict aliasing rules.

---
_Auto-generated daily digest entry._
