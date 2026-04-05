# Roogle: A Rust API search engine

- **Source:** Lobsters
- **Rank (today):** #4
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-04-05 04:42
- **Original:** https://github.com/roogle-rs/roogle

## Summary

Roogle is a Rust API search engine, which allows you to search functions by names and type signatures. - Function queries - Method queries - Primitive types - Generic types - Without bounds and where predicates (e.g., <T> ) - With bounds (e.g., <T: Copy> ) - With where predicates - Without bounds and where predicates (e.g., - Custom types - Without generic args (e.g., IpAddr ) - With generic args (e.g., Vec<T> ,Option<T> ) - Without generic args (e.g., - Other types $ cargo r --release # Then, on another shell session, run: $ curl -X GET \ -d "fn (Option<Result<T, E>>) -> Result<Option<T>, E>>" \ "localhost:8000/search?scope=set:libstd" $ docker-compose up # Then, on another shell session, run: $ curl -X GET \ -d "fn (Option<Result<T, E>>) -> Result<Option<T>, E>>" \ "localhost:8000/search?scope=set:libstd" fn f(type) -> type fn (type) -> type fn(type) -> type (type) -> type

## Key Takeaways

- Read full article for details.

---
_Auto-generated daily digest entry._
