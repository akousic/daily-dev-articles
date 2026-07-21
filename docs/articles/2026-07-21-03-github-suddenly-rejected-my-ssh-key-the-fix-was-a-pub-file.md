# GitHub suddenly rejected my SSH key (the fix was a .pub file?!)

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-07-21 05:11
- **Original:** https://thorsell.io/2026/07/21/github-ssh-keys.html

## Summary

GitHub suddenly rejected my SSH key (the fix was a .pub file?!) Today, git pull stopped working on my main laptop. Permission denied (publickey), out of nowhere. I had changed nothing, the key was still registered on GitHub, and pulling the same repository from another laptop (with another key) worked fine.

## Key Takeaways

- The rabbit hole I’ll spare you the full troubleshooting session1.
- The key was mathematically sound (openssl rsa -check said RSA key ok), the signature algorithm was the modern rsa-sha2-512, my ~/.ssh/config was clean, and GitHub’s status page was all green.
- Still: Permission denied.

---
_Auto-generated daily digest entry._
