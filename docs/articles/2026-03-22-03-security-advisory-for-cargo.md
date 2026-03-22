# Security advisory for Cargo

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-03-22 02:12
- **Original:** https://blog.rust-lang.org/2026/03/21/cve-2026-33056/

## Summary

The Rust Security Response Team was notified of a vulnerability in the third-party crate tar , used by Cargo to extract packages during a build. The vulnerability, tracked as CVE-2026-33056, allows a malicious crate to change the permissions on arbitrary directories on the filesystem when Cargo extracts it during a build. For users of the public crates.io registry, we deployed a change on March 13th to prevent uploading crates exploiting this vulnerability, and we audited all crates ever published.

## Key Takeaways

- We can confirm that no crates on crates.io are exploiting this.
- For users of alternate registries, please contact the vendor of your registry to verify whether you are affected by this.
- The Rust team will release Rust 1.94.1 on March 26th, 2026, updating to a patched version of the tar crate (along with other non-security fixes for the Rust toolchain), but that won't protect users of older versions of Cargo using alternate registries.

---
_Auto-generated daily digest entry._
