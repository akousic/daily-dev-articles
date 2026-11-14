# Formalizing US Tax Code (Using Lean)

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 81
- **Published (UTC):** 2026-11-14 15:41
- **Original:** https://lexifina.com/blog/formalizing-the-us-tax-code

## Summary

Formalizing the US tax code Yesterday, we verified that known tax loopholes could be identified using a Lean search. Today, we set out to formalize the entire Internal Revenue Code to hunt for unknown loopholes (bugs). Pointing a proof checker at statutes Lean is a programming language whose type checker can also check mathematical proofs: if Lean accepts a proof, every step follows from the definitions, with nothing taken on trust.

## Key Takeaways

- An earlier post discussed how far that kind of formalisation can reach in law,[1] and yesterday we used it on the retirement-account rules, where a blind search rediscovered the backdoor Roth.[2] This work is part of global-law, a CC0 repository of versioned legislation and case law.[3] Our argument is that pointing AI and a proof checker at a versioned record of the law finds the contradictions and mechanical mistakes that people miss.
- In particular, we can catch mistakes in the text, and see what the rules allow, including what they allow by accident.
- To do so, we translated each section of the law into Lean, staying close to the statute’s own words, and tested it against the worked examples the IRS prints in its forms and instructions.

---
_Auto-generated daily digest entry._
