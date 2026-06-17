# TIL: You can make HTTP requests without curl using Bash /dev/TCP

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 512
- **Published (UTC):** 2026-06-16 16:40
- **Original:** https://mareksuppa.com/til/bash-dev-tcp-http-without-curl/

## Summary

Edit: This has generated a nice discussion on Hacker News – check it out too! I needed to check that one container could reach another over an internal Docker network: a plain GET /health against a service on a shared network. The obvious move is curl http://service:8642/health.

## Key Takeaways

- But this app image was stripped right down, with no curl or wget and nothing else around that I could use to open a socket.
- As it turns out, bash can speak HTTP by itselfbash can open a TCP socket, and you can write a small HTTP request to it by hand.
- Opening a connection to a host and port and writing the request needs nothing beyond the shell that’s already there: exec 3<>/dev/tcp/service/8642 printf 'GET /health HTTP/1.1\r\nHost: service\r\nConnection: close\r\n\r\n' >&3 cat <&3service here is just the hostname of whatever you’re talking to.

---
_Auto-generated daily digest entry._
