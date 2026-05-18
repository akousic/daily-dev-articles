# Show HN: Auto-identity-remove – Automated data broker opt-out runner for macOS

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 301
- **Published (UTC):** 2026-05-18 11:32
- **Original:** https://github.com/stephenlthorn/auto-identity-remove

## Summary

Automated data broker opt-out runner for macOS. Removes your personal information from 500+ people-search sites and data broker databases on a monthly schedule — with CAPTCHA solving, persistent state tracking (so completed opt-outs aren't resubmitted every run), and an iMessage notification when done. Each month, the script: - Searches each data broker site for your name + state - Finds your specific listing (for sites that need a profile URL) - Fills and submits the opt-out form automatically - Solves CAPTCHAs via CapSolver (AI-powered, ~$0.001/solve) - Skips brokers you were already removed from recently (90-day re-check window) - Sends you an iMessage with the results summary - Opens any sites that require manual action in your browser - macOS (uses launchd for scheduling and Messages for iMessage) - Node.js 18+ - Playwright browsers installed npx playwright install chromium # 1.

## Key Takeaways

- Clone the repo git clone https://github.com/stephenlthorn/auto-identity-remove.git cd auto-identity-remove # 2.
- Install dependencies npm install # 3.
- Run interactive setup (creates config.json and schedules the monthly job) node setup.js # 4.

---
_Auto-generated daily digest entry._
