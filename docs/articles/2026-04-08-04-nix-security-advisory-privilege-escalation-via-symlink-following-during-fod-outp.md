# Nix security advisory: Privilege escalation via symlink following during FOD output registration

- **Source:** Lobsters
- **Rank (today):** #4
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-04-07 17:41
- **Original:** https://discourse.nixos.org/t/nix-security-advisory-privilege-escalation-via-symlink-following-during-fod-output-registration/76900

## Summary

Nix daemon is vulnerable to arbitrary file overwrites as the daemon user (root on NixOS and in multi-user installations). The issue is identified as GHSA-g3g9-5vj6-r3gj and CVE-2026-39860. All users allowed to submit builds to the Nix daemon (allowed-users, everyone by default) can achieve arbitrary file writes as root and subsequent privilege escalation.

## Key Takeaways

- All Nix versions since 2.21 and patch releases >=2.18.2,>=2.19.4,>=2.20.5 prior to 2.34.5, 2.33.4, 2.32.7, 2.31.4, 2.30.4, 2.29.3, 2.28.6 are vulnerable.
- This affects sandboxed Linux configurations, sandboxed macOS configurations are unaffected.
- All default configurations of NixOS and systems building untrusted derivations are impacted.

---
_Auto-generated daily digest entry._
