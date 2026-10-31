# Cloudflare Turnstile solver library (no headless browser required)

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 287
- **Published (UTC):** 2026-10-28 17:29
- **Original:** https://github.com/chris124567/cfsolve

## Summary

cfsolve is a Rust library and command line tool that solves Cloudflare Turnstile widgets and challenge pages without a headless browser. It returns a Turnstile token for widgets or a cf_clearance cookie for challenge pages. Turnstile widgets can be solved using the page URL, the sitekey, and optionally the page's HTML (this should not be required in most cases).

## Key Takeaways

- Challenge pages require a direct fetch or the HTML of the page.
- cfsolve impersonates a specific browser, described by a profile file.
- One is included: profiles/safari-26-ios.json (Safari on iPhone).

---
_Auto-generated daily digest entry._
