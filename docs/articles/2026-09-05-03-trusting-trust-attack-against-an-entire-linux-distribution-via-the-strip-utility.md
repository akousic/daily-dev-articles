# Trusting-Trust Attack against an Entire Linux Distribution (via the strip utility)

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-09-05 05:58
- **Original:** https://arxiv.org/abs/2607.24888

## Summary

Computer Science > Cryptography and Security [Submitted on 27 Jul 2026] Title:Trusting-Trust Attack against an Entire Linux Distribution through Binary Manipulation View PDF HTML (experimental) Abstract:Ken Thompson's trusting-trust attack, in which a compromised compiler backdoors the programs it builds and reproduces the backdoor in subsequent rebuilds of itself, is widely regarded as a threat specific to compilers. We show that it is not. We construct a complete trusting-trust attack around GNU strip, an ordinary build utility that neither inspects nor generates source code, using only manipulations of finished ELF files.

## Key Takeaways

- In the bootstrap of the NixOS Linux distribution, a single tampered strip in the binary seed implants a payload that propagates from one generation of strip to the next and survives into the final standard environment after the seed leaves the dependency closure.
- On a real nixpkgs revision, the attack builds a complete graphical installer without failures and backdoors almost every one of its binaries, enabling arbitrary malicious behavior of the subverted packages.
- References & Citations Loading...

---
_Auto-generated daily digest entry._
