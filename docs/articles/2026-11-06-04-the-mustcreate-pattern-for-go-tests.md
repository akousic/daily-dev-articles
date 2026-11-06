# The MustCreate Pattern for Go Tests

- **Source:** Lobsters
- **Rank (today):** #4
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-11-06 09:37
- **Original:** https://mtlynch.io/notes/go-must-create-pattern/

## Summary

The MustCreate Pattern for Go Tests I recently discovered a handy way to make Go tests more readable and less repetitive. Suppose I have a constructor that can fail: func NewUsername(raw string) (Username, error) { ... } And I have another function that takes a Username as an argument: func (ds Datastore) ReadUser(username Username) (User, error) { ...

## Key Takeaways

- } When I write tests for ReadUser, I call NewUsername with a value I know is valid, but I still have to include a lot of verbose error-checking code to convince the compiler that everything is okay: username, err := NewUsername("joe123") // This is silly because *I* know joe123 is a valid username, so this should // never happen.
- if err != nil { t.Fatalf("failed to create username: %v", err) } // Perform the test assertion I actually care about.
- user, err := store.ReadUser(username) if got, want := user.Name.String(), "joe123"; got != want { t.Errorf("username=%v, want=%v", got, want) } My old solution: one new helper function per type 🔗︎ Until a few months ago, I avoided the verbose error checking by writing a helper function like MustCreateUsername that wraps NewUsername with the expectation that it never returns a non-nil error value: user, err := store.ReadUser(MustCreateUsername(t, "joe123")) if got, want := user.Name.String(), "joe123"; got != want { t.Errorf("username=%v, want=%v", got, want) } The implementation of MustCreateUsername looks how you’d expect: func MustCreateUsername(t testing.TB, raw string) Username { t.Helper() username, err := NewUsername(raw) if err != nil { t.Fatalf("invalid username: %s", raw) } } The helper function strategy worked fine, but it scales poorly.

---
_Auto-generated daily digest entry._
