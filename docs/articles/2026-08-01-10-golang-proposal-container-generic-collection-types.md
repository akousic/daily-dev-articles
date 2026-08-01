# Golang proposal: container/: generic collection types

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 170
- **Published (UTC):** 2026-07-31 18:39
- **Original:** https://github.com/golang/go/issues/80590

## Summary

- Notifications You must be signed in to change notification settings - Fork 19.2k proposal: container/...: generic collection types #80590 Description Background: The Go Collections working group was formed in late 2025 with the purpose of bringing common collection data structures to the standard library, guided by the familiar Go principles of pragmatism and simplicity. Alphabetically by last name, the group consists of Jonathan Amsterdam (@jba), Alan Donovan (@adonovan), Robert Griesemer (@griesemer), Daniel Martí (@mvdan), Roger Peppe (@rogpeppe), Keith Randall (@khr), and Ian Lance Taylor (@ianlancetaylor). We’ve now reached a point where we’re ready to share our results with the community.

## Key Takeaways

- This issue is an umbrella for discussing several related proposals for new collections APIs for Go 1.28.
- It presents a high level overview of the themes, and links to the various concrete proposals and associated implementation CLs.
- Go currently provides few collection types in its library, and from the outset we have emphasized the flexibility of the language’s built-in slice and map types.

---
_Auto-generated daily digest entry._
