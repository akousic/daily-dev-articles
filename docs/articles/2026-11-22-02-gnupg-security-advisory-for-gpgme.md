# GnuPG Security Advisory for GPGME

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 264
- **Published (UTC):** 2026-11-21 08:32
- **Original:** https://lists.gnupg.org/pipermail/gnupg-announce/2026q4/000517.html

## Summary

[Announce] GnuPG Security Advisory for GPGME (T8557,CVE-2026-129975) Werner Koch wk at gnupg.org Fri Nov 20 19:01:51 CET 2026 Hello! We are pleased to announce the availability of a new GPGME release: version 2.3.1. This version fixes a *critical security bug* found in all prior versions.

## Key Takeaways

- We also release a new Gpg4win versions and and GnuPG Desktop and GnuPG VS-Desktop versions which all make use of GPGME.
- Description =========== By using an OpenPGP key containing a crafted very long user id it is possible to trigger a double free.
- This double free can be used exfiltrate data from applications by sending for example signed data.

---
_Auto-generated daily digest entry._
