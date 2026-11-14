# Node.js Brings Debounce, Throttle, and PKCS#12 Parsing Into Core Modules

- **Source:** InfoQ
- **Rank (today):** #6
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-11-14 19:00
- **Original:** https://www.infoq.com/news/2026/11/nodejs-debounce-throttle/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

Node.js, the popular open-source JavaScript runtime, has pulled a handful of long-requested utilities directly into its standard library. Debounce and throttle helpers have landed in node:util, a new crypto.parsePKCS12() API now surfaces private keys and certificates from .p12 and .pfx bundles, and the experimental Virtual File System has been extended into node:ffi. The additions shipped as part of Node.js 26.10.0, one of a steady run of Current-line releases leading into the Node.js 26 LTS line that is now Active LTS under the codename "Lithium".

## Key Takeaways

- The headline change is the arrival of util.debounce() and util.throttle() in the core util module.
- Rate-limiting helpers have long been one of the most commonly vendored dependencies in the Node.js ecosystem, typically pulled from lodash or the throttle-debounce package.
- James M Snell landed both in a single pull request, with Matteo Collina noting that he uses these utilities in "essentially every app." Contributors ljharb and bakkot flagged the awkwardness of using an AbortSignal (which only transitions to aborted once) inside a function meant to be called repeatedly, so Snell reworked the signal to cancel every future invocation and added a leading-edge option so the first call can fire immediately.

---
_Auto-generated daily digest entry._
