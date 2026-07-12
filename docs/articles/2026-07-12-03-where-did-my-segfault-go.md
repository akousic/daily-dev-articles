# Where did my segfault go?

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-07-11 16:05
- **Original:** https://rmpr.xyz/Where-did-my-segfault-go/

## Summary

Where did my segfault go? The other day I was iterating on a small C program with entr: ls hello.c | entr -s "gcc -o hello hello.c && ./hello" hello happened to segfault, but entr showed me… nothing. No Segmentation fault, no non-zero exit visible, just complete silence after the compile output.

## Key Takeaways

- Let’s prefix with bash -c: ls hello.c | entr -s "bash -c 'gcc -o hello hello.c && ./hello'" Still nothing.
- What about moving the command into a script: #!/bin/bash gcc -o hello hello.c && ./hello And point entr to it: ls hello.c | entr -s ./run.sh ./run.sh: line 2: 104465 Segmentation fault (core dumped) ./hello There’s my segmentation fault!
- The reason(s) Thanks to superuser (remember that site we used to use pre LLMs?) for pointing me in the right direction.

---
_Auto-generated daily digest entry._
