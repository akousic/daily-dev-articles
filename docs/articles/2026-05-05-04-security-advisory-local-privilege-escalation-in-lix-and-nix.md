# Security Advisory: Local privilege escalation in Lix and Nix

- **Source:** Lobsters
- **Rank (today):** #4
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-05-04 15:17
- **Original:** https://discourse.nixos.org/t/security-advisory-local-privilege-escalation-in-lix-and-nix/77407

## Summary

Summary Nix and Lix daemon implementations are affected by buffer overflows vulnerabilities that allow a local attacker to gain arbitrary code execution as the daemon user (root in multi-user installations). The vulnerabilities are identified as: - Nix: GHSA-vh5x-56v6-4368, CVE ID pending attribution by MITRE. - Lix: NVD - CVE-2026-44028 .

## Key Takeaways

- This is a coordinated disclosure between the Nix and Lix projects.
- Guix is NOT affected by this vulnerability.
- To exploit this issue, a local attacker needs access to talk to the Nix daemon.

---
_Auto-generated daily digest entry._
