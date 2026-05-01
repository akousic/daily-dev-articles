# For Linux kernel vulnerabilities, there is no heads-up to distributions

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 560
- **Published (UTC):** 2026-04-30 16:43
- **Original:** https://www.openwall.com/lists/oss-security/2026/04/30/10

## Summary

| Message-ID: <87se8dgicq.fsf@gentoo.org> Date: Thu, 30 Apr 2026 05:52:37 +0100 From: Sam James <sam@...too.org> To: oss-security@...ts.openwall.com Cc: Jan Schaumann <jschauma@...meister.org> Subject: Re: CVE-2026-31431: CopyFail: linux local privilege scalation Eddie Chapman <eddie@...k.net> writes: > On 29/04/2026 21:23, Jan Schaumann wrote: >> Affected and fixed versions >> =========================== >> Issue introduced in 4.14 with commit >> 72548b093ee38a6d4f2a19e6ef1948ae05c181f7 and fixed in >> 6.18.22 with commit >> fafe0fa2995a0f7073c1c358d7d3145bcc9aedd8 >> Issue introduced in 4.14 with commit >> 72548b093ee38a6d4f2a19e6ef1948ae05c181f7 and fixed in >> 6.19.12 with commit >> ce42ee423e58dffa5ec03524054c9d8bfd4f6237 >> Issue introduced in 4.14 with commit >> 72548b093ee38a6d4f2a19e6ef1948ae05c181f7 and fixed in >> 7.0 with commit >> a664bf3d603dc3bdcf9ae47cc21e0daec706d7a5 >> https://git.kernel.org/stable/c/fafe0fa2995a0f7073c1c358d7d3145bcc9aedd8 >> https://git.kernel.org/stable/c/ce42ee423e58dffa5ec03524054c9d8bfd4f6237 >> https://git.kernel.org/stable/c/a664bf3d603dc3bdcf9ae47cc21e0daec706d7a5 > > So this is one of the worst make-me-root vulnerabilities in the kernel > in recent times. I see that on the 11th of April 6.19.12 & 6.18.22 > were released with the fix backported. > > Longterm 6.12, 6.6, 6.1, 5.15, 5.10 have not received the fix and I > don't see anything in the upstream stable queues yet as I write.

## Key Takeaways

- My > guess is backporting that far back is not as straightforward.
- As this > was introduced in 2017 all those older kernels are affected, right?
- Or > am I missing something?

---
_Auto-generated daily digest entry._
