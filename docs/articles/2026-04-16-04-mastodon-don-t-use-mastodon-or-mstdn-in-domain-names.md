# Mastodon: Don't use "mastodon" or "mstdn" in domain names

- **Source:** Lobsters
- **Rank (today):** #4
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-04-16 04:57
- **Original:** https://github.com/mastodon/mastodon/commit/d6f8ac97e808821180e9ae0c66879b7a2d64e690

## Summary

We read every piece of feedback, and take your input very seriously. To see all available qualifiers, see our documentation. There was an error while loading.

## Key Takeaways

- Please reload this page.
- mastodon:setup 1 parent 19ef4e5 commit d6f8ac9Copy full SHA for d6f8ac9 lib/tasks/mastodon.rake @@ -27,6 +27,12 @@ namespace :mastodon do 27 q.messages[:valid?] = 'Invalid domain.
- If you intend to use unicode characters, enter punycode here' 28 end 29 30 + if env['LOCAL_DOMAIN'].include?('mastodon') || env['LOCAL_DOMAIN'].include?('mstdn') 31 + prompt.warn 'The Mastodon name is a trademark and its use is restricted.' 32 + prompt.warn 'You can read the trademark policy at https://joinmastodon.org/trademark' 33 + next prompt.warn 'Nothing saved.

---
_Auto-generated daily digest entry._
