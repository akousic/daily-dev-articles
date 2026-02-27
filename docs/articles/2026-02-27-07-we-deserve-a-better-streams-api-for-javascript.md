# We deserve a better streams API for JavaScript

- **Source:** Cloudflare
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-02-27 14:49
- **Original:** https://blog.cloudflare.com/a-better-web-streams-api/

## Summary

Handling data in streams is fundamental to how we build applications. To make streaming work everywhere, the WHATWG Streams Standard (informally known as "Web streams") was designed to establish a common API to work across browsers and servers. It shipped in browsers, was adopted by Cloudflare Workers, Node.js, Deno, and Bun, and became the foundation for APIs like fetch().

## Key Takeaways

- It's a significant undertaking, and the people who designed it were solving hard problems with the constraints and tools they had at the time.
- But after years of building on Web streams — implementing them in both Node.js and Cloudflare Workers, debugging production issues for customers and runtimes, and helping developers work through far too many common pitfalls — I've come to believe that the standard API has fundamental usability and performance issues that cannot be fixed easily with incremental improvements alone.
- The problems aren't bugs; they're consequences of design decisions that may have made sense a decade ago, but don't align with how JavaScript developers write code today.

---
_Auto-generated daily digest entry._
