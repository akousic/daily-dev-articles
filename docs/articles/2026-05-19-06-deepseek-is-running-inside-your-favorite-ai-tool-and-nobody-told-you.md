# DeepSeek Is Running Inside Your Favorite AI Tool – And Nobody Told You

- **Source:** Dev.to
- **Rank (today):** #6
- **Ranking metrics:** reactions 42, comments 21
- **Published (UTC):** 2026-05-18 11:21
- **Original:** https://dev.to/harsh2644/deepseek-is-running-inside-your-favorite-ai-tool-and-nobody-told-you-5g47

## Summary

I was debugging a slow response in HuggingChat last Tuesday. Standard stuff Open DevTools, check the Network tab, filter by Fetch/XHR, look at the API responses. And then I saw this right there in the chat UI: agentic with Kimi-K2.6 via 🤗 together HuggingChat showing exactly which model it's using - Kimi-K2.6 via Together AI No hiding This is what transparency looks like.

## Key Takeaways

- I stared at the screen for a second Kimi-K2.6 That's a model from Moonshot AI a Chinese AI company Not something HuggingChat built from scratch Just a third-party API call, right there in plain sight.
- But here's the thing HuggingChat was being honest They show you the model name They show you the inference provider Right in the UI.
- Then I checked some of the other tools I use every day.

---
_Auto-generated daily digest entry._
