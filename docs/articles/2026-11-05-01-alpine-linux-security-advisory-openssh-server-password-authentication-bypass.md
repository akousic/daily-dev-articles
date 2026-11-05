# Alpine Linux Security Advisory: OpenSSH-server password authentication bypass

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 473
- **Published (UTC):** 2026-11-05 14:44
- **Original:** https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/

## Summary

Security advisory: openssh-server password authentication bypass If you run sshd on Alpine Linux, update openssh now and restart sshd. Upgrading the package alone does not replace the running daemon. If you cannot update yet, at least disable password logins: set PasswordAuthentication no in your sshd configuration and restart sshd.

## Key Takeaways

- Either one closes the hole.
- An attacker who can reach your SSH port can log in without knowing any password.
- It takes one connection, works every time, and needs no retries.

---
_Auto-generated daily digest entry._
