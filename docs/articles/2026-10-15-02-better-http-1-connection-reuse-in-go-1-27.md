# Better HTTP/1 connection reuse in Go 1.27

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 293
- **Published (UTC):** 2026-10-14 16:29
- **Original:** https://go.dev/blog/http-connection-reuse

## Summary

The Go Blog Better HTTP/1 connection reuse Take a look at the following function: func getStatus(url string) (int, error) { resp, err := http.Get(url) if err != nil { return 0, err } defer resp.Body.Close() return resp.StatusCode, nil } It sends a GET request to url and returns the HTTP status code. Using HTTP/1 (GODEBUG=http2client=0), calling this function 100 times against index.golang.org takes ~710 milliseconds on Go 1.26 on my machine. On Go 1.27, the same program takes ~150 milliseconds.

## Key Takeaways

- That is almost 5 times faster!
- How is such a drastic performance difference possible?
- The cost of establishing HTTP connections To understand the difference, consider what happens on the network when we make an HTTP request.

---
_Auto-generated daily digest entry._
