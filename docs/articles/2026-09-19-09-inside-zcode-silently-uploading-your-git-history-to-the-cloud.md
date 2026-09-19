# Inside ZCode: Silently uploading your Git history to the cloud

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 322
- **Published (UTC):** 2026-09-18 06:11
- **Original:** https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/

## Summary

I am not a native English speaker; this article was translated by AI. It started with a routine check while freeing up disk space: ~/.zcode was taking up over 700MB. After digging into it intermittently, I confirmed something pretty wild: Whenever you are logged in, ZCode (Zhipu’s official AI coding desktop app) silently packages your entire workspace — complete .git history, LFS asset cache, reflogs, and global app configs — encrypts it, and uploads it directly to Aliyun OSS.

## Key Takeaways

- Even more ironic: the RSA public key used for encryption is delivered on the fly by the server, while the private key lives exclusively in the cloud.
- You cannot decrypt that multi-hundred-megabyte ciphertext sitting right on your own disk, and neither can the ZCode client itself.
- Here is the complete record of the investigation, the evidence chain, and a one-liner defense that permanently shuts it down.

---
_Auto-generated daily digest entry._
