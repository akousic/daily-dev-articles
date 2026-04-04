# Post Mortem: axios NPM supply chain compromise

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 271
- **Published (UTC):** 2026-04-03 00:00
- **Original:** https://github.com/axios/axios/issues/10636

## Summary

- - Notifications You must be signed in to change notification settings - Fork 11.6k Post Mortem: axios npm supply chain compromise #10636 Description Post Mortem: axios npm supply chain compromise Date: March 31, 2026 Author: Jason Saayman Status: Remediation in progress On March 31, 2026, two malicious versions of axios (1.14.1 and 0.30.4) were published to the npm registry through my compromised account. Both versions injected a dependency called plain-crypto-js@4.2.1 that installed a remote access trojan on macOS, Windows, and Linux. The malicious versions were live for about 3 hours before being removed.

## Key Takeaways

- Check your lockfile: grep -E "axios@(1\.14\.1|0\.30\.4)|plain-crypto-js" package-lock.json yarn.lock 2>/dev/null If anything comes back, treat that machine as compromised: - Downgrade to axios@1.14.0 (or0.30.3 for 0.x users) - Delete node_modules/plain-crypto-js/ - Rotate every secret, token, and credential on that machine - Check your network logs for connections to sfrclak[.]com or142.11.206.73 on port 8000 - If this happened on a CI runner, rotate any secrets that were injected during the affected build If you were already pinned to a clean version and didn't run a fresh install between 00:21 and 03:15 UTC on March 31, you're fine.
- For detailed remediation guidance, including CI/CD-specific steps, see: - StepSecurity: full technical analysis and remediation - Snyk: advisory and scanning guidance - Socket: Supply Chain Attack on Axios Pulls Malicious Dependency from npm What happened The attacker gained access to the lead maintainer's PC through a targeted social engineering campaign and RAT malware.
- This gave them access to the npm account credentials, which they used to publish the malicious versions.

---
_Auto-generated daily digest entry._
