# Vue Router 5: File-Based Routing Into Core with No Breaking Changes

- **Source:** InfoQ
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-03-04 14:45
- **Original:** https://www.infoq.com/news/2026/03/vue-router-5/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

Vue Router, the official routing library for Vue.js, has released version 5.0, a transition release that merges the popular unplugin-vue-router plugin directly into the core package. The release, which maintainer Eduardo San Martin Morote (posva) has described as intentionally "boring", ships with no breaking changes for existing Vue Router 4 users. The headline change in Vue Router 5 is the absorption of unplugin-vue-router, a build-time plugin that provided file-based routing with full TypeScript support.

## Key Takeaways

- Previously maintained as a separate package, this functionality is now available directly from vue-router imports, eliminating the need for an additional dependency.
- For developers already using unplugin-vue-router, migration is primarily a matter of updating import paths.
- For those not using it, upgrading is a single command: pnpm update vue-router@5 Alongside the file-based routing integration, Vue Router 5 introduces several new features as experimental additions.

---
_Auto-generated daily digest entry._
