# yet another place where a linux man page is inaccurate

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-10-14 06:18
- **Original:** https://sebsite.pw/w/20261014-initstate.html

## Summary

ok hi so a couple days ago i put out your c is not standard c. and it originally had a section that looked like this (entire section pasted here, since it's now gone from the original post): this one is a posix extension, so not necessarily "standard c", more like "posix c", but it's still a documented incompatibility with a standard: in glibc, initstate doesn't return NULL on error, despite posix requiring that it does: // EINVAL: state array less than 8 bytes char *state = initstate(67, (char [1]){}, 1); assert(errno == EINVAL); // ok assert(state == NULL); // fails, despite posix requiring it to succeed the man page initstate(3) very unhelpfully first describes the posix behavior in the RETURN VALUE section, as though it's the actual behavior: Theinitstate() function returns a pointer to the previous state array. On failure, it returns NULL, and errno is set to indicate the error.

## Key Takeaways

- only at the very bottom in the BUGS section does it say that glibc behaves differently: According to POSIX,initstate() should return NULL on error.
- In the glibc implementation, errno is (as specified) set on error, but the function does not return NULL.
- however, i just got an email: Hi, I read " your c is not standard c" and I think there's a small mistake about initstate() in glibc.

---
_Auto-generated daily digest entry._
