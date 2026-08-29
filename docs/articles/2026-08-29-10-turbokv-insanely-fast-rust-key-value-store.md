# TurboKV: Insanely fast Rust key-value store

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 158
- **Published (UTC):** 2026-08-29 02:23
- **Original:** https://github.com/kingroryg/turbokv

## Summary

TurboKV is an async embedded key-value database with atomic batches, ordered range scans, configurable durability, compression, and background compaction. cargo add turbokv cargo add tokio --features full Or add the dependencies directly: [dependencies] turbokv = "0.6" tokio = { version = "1", features = ["full"] } TurboKV's persisted Bloom-filter format uses hardware AES. Build x86/x86_64 targets with RUSTFLAGS="-C target-feature=+aes,+sse2", and ARM/AArch64 targets with RUSTFLAGS="-C target-feature=+aes,+neon".

## Key Takeaways

- You may instead use -C target-cpu=native when the binary will run only on the same CPU model or a feature superset.
- use turbokv::{Db, DbOptions, WriteBatch}; #[tokio::main] async fn main() -> Result<(), Box<dyn std::error::Error>> { let db = Db::open_with_options("./my-database", DbOptions::durable()).await?; db.insert(b"user:1", b"Ada").await?; assert_eq!(db.get(b"user:1").await?, Some(b"Ada".to_vec())); let mut batch = WriteBatch::new(); batch.put(b"user:2", b"Grace"); batch.put(b"user:3", b"Linus"); batch.delete(b"user:1"); db.write_batch(&batch).await?; for (key, value) in db.scan_prefix(b"user:").await?
- { println!( "{} = {}", String::from_utf8_lossy(&key), String::from_utf8_lossy(&value) ); } db.close().await?; Ok(()) } Runnable examples: - basic : insert, get, update, and remove - batch_writes : atomic puts and deletes - range_queries : ordered range and prefix scans - concurrent : shared access from Tokio tasks - persistence : paranoid WAL recovery - configuration : cache, memtable, and compression options | Preset | Acknowledgement boundary | Use case | |---|---|---| | DbOptions::fast() | In-memory visibility; no WAL | Caches and reproducible data | | DbOptions::durable() | Appended to the WAL without a per-write sync | Process-crash recovery with periodic power-loss checkpoints; recommended default | | DbOptions::paranoid() | WAL group completed sync_all before return | Strongest mode, subject to filesystem/device guarantees | Durable does not leave the WAL unsynchronized forever.

---
_Auto-generated daily digest entry._
