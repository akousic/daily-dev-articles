# Memdoor: A team of 5 Qwen3.8-27B models beats Fable 5 on LiveCodeBench Hard

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 385
- **Published (UTC):** 2026-10-31 22:46
- **Original:** https://github.com/guregodevo/memdoor/tree/main/examples/workflows/team-solve

## Summary

Five small models solve a programming problem together: a planner, two ideators, a solver and a manager, plus a repair worker. Each starts from a fresh context and talks only through files on disk. A script that runs the samples decides success, not a model.

## Key Takeaways

- It is the method of GVS5H (Lee, 2026), written as a Memdoor workflow: eight YAML files, no code, no model named.
- The authors' harness rebuilt on the same model, Qwen3.8-27B, with their prompts, loop and 128K reply cap.
- The first ten problems of their LiveCodeBench Hard list, five passes each, graded on every hidden test with their corrected grader: | pass | this workflow | authors' harness | Fable 5, one call | |---|---|---|---| | 1 | 10 / 10 | 9 | 7 | | 2 | 10 / 10 | 10 | 8 | | 3 | 10 / 10 | 10 | 10 | | 4 | 10 / 10 | 9 | 8 | | 5 | 9 / 10 | 10 | 7 | | mean | 9.8 | 9.6 | 8.0 | The authors' two columns are the regraded result files in their repository, the numbers in their paper.

---
_Auto-generated daily digest entry._
