# Dirtyfrag: Universal Linux LPE

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 727
- **Published (UTC):** 2026-05-07 19:21
- **Original:** https://www.openwall.com/lists/oss-security/2026/05/07/8

## Summary

| Message-ID: <afzgS2SCWNcZU3vU@v4bel> Date: Fri, 8 May 2026 03:56:11 +0900 From: Hyunwoo Kim <imv4bel@...il.com> To: oss-security@...ts.openwall.com Cc: imv4bel@...il.com Subject: Dirty Frag: Universal Linux LPE Hi, This is a report on "Dirty Frag", a universal LPE that allows obtaining root privileges on all major distributions. This vulnerability has a similar impact to the previous Copy Fail. Because the embargo has now been broken, no patches or CVEs exist for these vulnerabilities.

## Key Takeaways

- After consultation with the linux-distros@...openwall.org maintainers, and at the maintainers' request, I am publicly releasing this Dirty Frag document.
- As with the previous Copy Fail vulnerability, Dirty Frag likewise allows immediate root privilege escalation on all major distributions, and it chains two separate vulnerabilities: - https://git.kernel.org/pub/scm/linux/kernel/git/netdev/net.git/commit/?id=f4c50a4034e62ab75f1d5cdd191dd5f9c77fdff4 - https://lore.kernel.org/all/afKV2zGR6rrelPC7@v4bel/ Because the responsible disclosure schedule and embargo have been broken, no patches exist for any distribution.
- Use the following command to remove the modules in which the vulnerabilities occur: ``` sh -c "printf 'install esp4 /bin/false\ninstall esp6 /bin/false\ninstall rxrpc /bin/false\n' > /etc/modprobe.d/dirtyfrag.conf; rmmod esp4 esp6 rxrpc 2>/dev/null; true" ``` For detailed technical information about the vulnerabilities and the reason the embargo was broken, please check https://dirtyfrag.io.

---
_Auto-generated daily digest entry._
