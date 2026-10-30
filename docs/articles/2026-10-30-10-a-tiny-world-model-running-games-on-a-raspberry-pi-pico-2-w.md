# A tiny world model running games on a Raspberry Pi Pico 2 W

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 267
- **Published (UTC):** 2026-10-29 20:32
- **Original:** https://github.com/SheepSeb/tinyworldformer

## Summary

Using 2 small neural networks to generate and play the game at the same time on a Raspberry Pi Pico 2 W. The first one creates the game: given the current frame and the action, it predicts the next frame and the reward. The second one plays that game: it uses the generated frame and picks an action.

## Key Takeaways

- Every frame above was sampled by the world model network, and the actions were taken by the actor network.
- I got interested in looped transformers, where one transformer block is applied several times with the same weights instead of stacking different layers.
- Reusing weights is cheap on memory, so I wanted to see if a looped world model could be small enough to run on a microcontroller.

---
_Auto-generated daily digest entry._
