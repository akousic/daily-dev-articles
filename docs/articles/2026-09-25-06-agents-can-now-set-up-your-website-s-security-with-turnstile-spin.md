# Agents can now set up your website’s security with Turnstile Spin

- **Source:** Cloudflare
- **Rank (today):** #6
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-09-25 18:27
- **Original:** https://blog.cloudflare.com/turnstile-spin/

## Summary

Agents can now set up your website’s security with Turnstile Spin In 2023, Cloudflare declared itself free from CAPTCHAs with the launch of Turnstile, our privacy-first client-side challenge. Turnstile is free to use, works on any site (no need to proxy traffic through Cloudflare), and never asks a visitor to solve a puzzle. Now, we are launching Turnstile Spin, an agent-mediated end-to-end implementation of Turnstile.

## Key Takeaways

- Initially built with developers in mind, Turnstile requires a basic two-step implementation and understanding of frontend and backend development.
- First, you modify your frontend code to render the Turnstile widget; this allows Cloudflare to run the client-side challenges and issue a token.
- Second, you POST the token to our Siteverify API, which verifies the token and returns metadata about whether the visitor passed or failed the challenge.

---
_Auto-generated daily digest entry._
