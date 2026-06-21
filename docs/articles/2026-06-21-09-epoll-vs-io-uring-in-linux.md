# Epoll vs. io_uring in Linux

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 216
- **Published (UTC):** 2026-06-20 23:07
- **Original:** https://sibexi.co/posts/epoll-vs-io_uring/

## Summary

epoll vs io_uring in Linux First, I want to tell you how exactly I got to this point and why I started researching different options for handling asynchronous I/O on Linux… Last year, my students and I built a reverse proxy server called TinyGate. It was super simple, worker-based, and it basically worked well. Of course, I didn’t expect it to be very fast, but it was an educational project, and since we’d made a real, kind of production-ready tool, I was really proud of it.

## Key Takeaways

- But my students weren’t as happy as I was - they wanted to build something genuinely useful, and they were really disappointed that our “product” had strong architectural limits and couldn’t outperform titans like nginx and haproxy.
- So they literally forced me to research together how those tools work under the hood and how to handle asynchronous I/O to cut down on the heavy overhead… Long story short, we made a second version of TinyGate, based on epoll.
- It still lost to nginx/haproxy in benchmarks, but it had a dramatic performance boost compared to the first version.

---
_Auto-generated daily digest entry._
