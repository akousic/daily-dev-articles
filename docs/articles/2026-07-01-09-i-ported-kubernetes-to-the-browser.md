# I ported Kubernetes to the browser

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 320
- **Published (UTC):** 2026-06-30 20:48
- **Original:** https://ngrok.com/blog/i-ported-kubernetes-to-the-browser

## Summary

Jun 30, 2026 Latest PostJun 30, 2026 Latest PostLast week I released webernetes, a partial port of Kubernetes to TypeScript to make it possible to run clusters in the browser. I ended up generating almost 100,000 lines of code in 552 commits across 629 files. The demo below is a webernetes cluster.

## Key Takeaways

- It runs entirely in your browser, and it’s genuinely doing much of the same work a real Kubernetes cluster does: pod lifecycles, cluster DNS and networking, container garbage collection, IP allocation, Deployment and ReplicaSet tracking, and more.
- The blue dots represent pods sending requests to each other.
- Interactive Webernetes demo showing HTTP requests moving between three pods from a Deployment across three Kubernetes nodes.

---
_Auto-generated daily digest entry._
