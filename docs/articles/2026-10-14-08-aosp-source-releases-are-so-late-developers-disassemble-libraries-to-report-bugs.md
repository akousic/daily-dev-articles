# AOSP Source Releases Are So Late Developers Disassemble Libraries to Report Bugs

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 462
- **Published (UTC):** 2026-10-14 06:18
- **Original:** https://github.com/android/ndk/issues/2260

## Summary

Repository navigation [BUG] bionic: wcscspn()/wcspbrk() treat every wchar_t >= 0x100 as a match (Android 17, CP3A.260905.009) #2260 Description Description On Android 17 builds from September 2026, wcscspn() and wcspbrk() stop at the first character of the string that is >= U+0100 whenever the reject set has two or more characters that are all < U+0100. The character is reported as a match even though it is not in the set. wcsspn(), wcschr(), wcsrchr(), wmemchr() and wcsstr() are correct.

## Key Takeaways

- Any code that scans wide strings for ASCII delimiters, for example newline or wildcard characters, breaks as soon as the text contains an emoji, CJK, Cyrillic, Greek or Latin Extended character.
- Affected / unaffected | Device | Build | Result | |---|---|---| | Pixel 7 | google/panther/panther:17/CP3A.260905.009/16091614:user/release-keys | broken | | Pixel 8a | google/akita/akita:17/CP3A.260905.009/16091614:user/release-keys (patch 2026-09-05) | broken | | Nothing Phone 2 | Nothing/PongEEA/Pong:16/BQ2A.250721.001-BP2A.250605.031.A3 (patch 2026-08-01) | ok | The public android17-release sources (android-17.0.0_r1, June 2026) build wcscspn/wcspbrk from external/llvm-libc, which is a plain nested loop over wchar_t and is correct.
- The code on the September builds is different (see "Mechanism"), so the regression was introduced between the June and September releases.

---
_Auto-generated daily digest entry._
