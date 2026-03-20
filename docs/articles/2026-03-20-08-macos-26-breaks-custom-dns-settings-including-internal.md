# macOS 26 breaks custom DNS settings including .internal

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 365
- **Published (UTC):** 2026-03-19 15:06
- **Original:** https://gist.github.com/adamamyl/81b78eced40feae50eae7c4f3bec1f5a

## Summary

Ah, the joys of waking up to find the Mac's done an overnight upgrade… and erm, suddenly things stop working. Thankfully, me and Claude managed to work out what the fuck is going on… I'm sharing here, as well as having raised in on https://feedbackassistant.apple.com/feedback/22280434 (that seems to need a login?). Product: macOS 26.3.1 (Darwin 25.3.0, Build 25D771280a) Component: Networking → DNS / mDNSResponder Regression from: macOS 25.x 26.3.0 (working immediately prior to overnight update) The /etc/resolver/ per-domain DNS resolver mechanism — an Apple-documented, long-standing macOS feature — is silently broken in macOS 26 for any TLD that is not present in the IANA root zone.

## Key Takeaways

- mDNSResponder intercepts queries for custom/private TLDs and handles them as mDNS (multicast DNS), never consulting the unicast nameserver specified in the resolver file.
- This breaks an entire class of local development and private network DNS workflows that previously worked correctly on macOS 25 and earlier.
- macOS supports per-domain DNS resolver configuration via files placed in /etc/resolver/ .

---
_Auto-generated daily digest entry._
