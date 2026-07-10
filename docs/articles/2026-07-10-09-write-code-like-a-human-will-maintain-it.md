# Write code like a human will maintain it

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 197
- **Published (UTC):** 2026-07-10 13:33
- **Original:** https://unstack.io/write-code-like-a-human-will-maintain-it

## Summary

One of the best things about LLMs is that they'll write code for you, all day long. You don't have to be the one updating the same long conditional in four different files - the AI will just do it for you! I've noticed myself letting it slide recently on a project I'd been building with AI.

## Key Takeaways

- I needed the same access check in a handful of places: a route handler, a background job, an API endpoint, a webhook, etc.
- Each time, I'd describe what I needed, the model would generate something that worked, and I'd merge it.
- Each version looked roughly like this: if (user.isActive && user.hasPermission('read') && !user.isSuspended && account.status === 'open') { // do a thing } Essentially the same conditionals every time.

---
_Auto-generated daily digest entry._
