# Stop MITM on the first SSH connection, on any VPS or cloud provider

- **Source:** Lobsters
- **Rank (today):** #4
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-05-08 06:26
- **Original:** https://www.joachimschipper.nl/Stop%20MITM%20on%20the%20first%20SSH%20connection,%20on%20any%20VPS%20or%20cloud%20provider.html

## Summary

Published on 8 May 2026 This little script stops attacks on the first SSH connection to a new VM, even on providers (like Hetzner Cloud) that don't offer a proprietary solution; we only need cloud-init, which is widely supported. Summary (for experts; read on for a longer explanation): inject a temporary SSH host (private) key via cloud-init, and trust that temporary SSH host key just long enough to generate and retrieve the "real" (long-term) SSH host keys. The script is a simple but hardened implementation of this technique; the comments in the script discuss implementation choices.

## Key Takeaways

- The technique appears to be new: I haven't found a proper write-up of this, nor of any other provider-independent solution (but I'd welcome a correction).
- This technique actually protects the first connection, whereas just answering "yes" when ssh asks "The authenticity of host [...] can't be established " (i.e.
- Trust On First Use) leaves you open to an attacker rerouting your traffic to a proxy, or to an attacker generously deciding to provide your VM (...

---
_Auto-generated daily digest entry._
