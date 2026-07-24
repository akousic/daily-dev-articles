# My security camera shipped a GitHub admin token in its login page

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 206
- **Published (UTC):** 2026-07-24 11:54
- **Original:** https://hhh.hn/hanwha-github-token/

## Summary

i have been thinking a bit more about security cameras again, because of AXIS starting to push more for every one of their cameras to be able to easily run linux applications on them, they're far more serious targets in an enterprise environment and need to be managed as such for vulnerabilities and credential management etc. someone brought up to me a company that sounded new to me, Hanwha (Vision.) I took a look at the site, and found that they had accessible firmware blobs for each model of camera, which is always a treat. poking and prodding i took the image and threw it at binwalk hoping it was just a rootfs or something, but inside there was a separate tarball with some AI stuff for the camera and a fwimage.tgz that binwalk was flagging as encrypted.

## Key Takeaways

- I was googling around and saw that Matt Brown has a writeup on these cameras that got me through.
- basically the passphrase is HTW + the model number so HTWXNP-9300RW worked.
- seems like they do some more stuff now, because inside of that tarball was another fwimage.tgz that was encrypted but it wasn't the same scheme, so we can't just re-use the same setup from Matt Brown.

---
_Auto-generated daily digest entry._
