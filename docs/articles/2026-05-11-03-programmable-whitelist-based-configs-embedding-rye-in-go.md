# Programmable Whitelist-based Configs: Embedding Rye in Go

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-05-11 05:57
- **Original:** https://ryelang.org/blog/posts/whitelist-config-with-rye/

## Summary

Config spec feature creep Configuration starts simple. A few keys and values, then you want to group values, and nest them, somebody asks for simple expressions, conditionals, variables … Any sufficiently complicated configuration system contains an ad-hoc, informally-specified, bug-ridden, slow implementation of half of a programming language. Greenspun’s Tenth Rule, applied to config You gradually end up with a programming language that was never designed as one.

## Key Takeaways

- YAML added templating, Nginx added if .
- Terraform invented HCL.
- Helm is pretty bad, two languages, two escaping contexts, paired with sometimes conflicting indentation rules, and a preprocessor step.

---
_Auto-generated daily digest entry._
