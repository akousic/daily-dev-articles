# Replace IBM Quantum back end with /dev/urandom

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 230
- **Published (UTC):** 2026-04-25 00:58
- **Original:** https://github.com/yuvadm/quantumslop/blob/25ad2e76ae58baa96f6219742459407db9dd17f5/URANDOM_DEMO.md

## Summary

Claim being tested: the Q‑Day Prize submission in this repo demonstrates a quantum attack on ECDLP — specifically, key recovery on curves up to 17 bits using IBM Quantum hardware. This branch applies a single surgical patch (−29 / +30 lines) to projecteleven.py . The patch replaces the IBM Quantum backend inside solve_ecdlp() with os.urandom .

## Key Takeaways

- Everything else — circuit construction, the ripple‑carry oracle, the extraction pipeline, the d·G == Q verifier — runs byte‑for‑byte unchanged.
- If the quantum computer were contributing measurable signal, this substitution should break the recoveries.
- The author's own CLI recovers every reported private key at statistically indistinguishable rates from the IBM hardware runs.

---
_Auto-generated daily digest entry._
