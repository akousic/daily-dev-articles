# Alibaba Open Sources OpenCodeReview for AI-Assisted Code Review

- **Source:** InfoQ
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-09-20 17:22
- **Original:** https://www.infoq.com/news/2026/09/alibaba-opencodereview/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

Alibaba recently open-sourced OpenCodeReview, an AI-powered code review CLI that combines deterministic pipelines for file selection, bundling, and rule matching with an LLM agent for dynamic code analysis. It supports built-in checks for issues such as null-pointer exceptions, thread safety, XSS, and SQL injection. Open-sourced under an Apache-2.0 license, OpenCodeReview is a Go-based CLI that avoids using AI for decisions that can be handled deterministically, such as selecting files, choosing tools, and validating review comments against the diff.

## Key Takeaways

- It therefore breaks the review process into multiple stages, each using a different level of determinism: deterministic components handle file selection, bundling, and rule matching, while AI agents perform code analysis.
- Reportedly used internally by tens of thousands of Alibaba developers for two years, OpenCodeReview works with OpenAI- and Anthropic-compatible models and can review Git diffs, branches, or entire files.
- Tom Rochette, Senior Developer at Shopify, reviews the project and writes: The architecture targets real agent failure modes: incomplete coverage, line-number drift, prompt instability, on large changesets.

---
_Auto-generated daily digest entry._
