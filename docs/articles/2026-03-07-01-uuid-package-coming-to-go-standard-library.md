# UUID package coming to Go standard library

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 252
- **Published (UTC):** 2026-03-07 02:03
- **Original:** https://github.com/golang/go/issues/62026

## Summary

- Notifications You must be signed in to change notification settings - Fork 18.9k Open Labels ProposalProposal-CryptoProposal related to crypto packages or other security issuesProposal related to crypto packages or other security issuesProposal-FinalCommentPeriod Milestone Description I would like to suggest the addition to the standard library of a package to generate and parse UUID identifiers, specifically versions 3, 4 and 5. The main reason I see to include it is that the most popular 3rd-party package (github.com/google/uuid) is a staple import in every server/db based Go program, as confirmed by a quick Github code search. Additionally: - UUID is a standard; - The interface exposed by github.com/google/uuid has been stable for years.

## Key Takeaways

- Addendum Would like to point out how Go is rather the exception than the norm with regards to including UUID support in its standard library.
- Reactions are currently unavailable Pinned by neild Pinned comment options Updated proposal with more permissive Parse, Nil and Max as vars, and a reference to RFC 9562 in the Compare documentation: // Package uuid provides support for generating and manipulating UUIDs.
- // // See [RFC 9562] for details.

---
_Auto-generated daily digest entry._
