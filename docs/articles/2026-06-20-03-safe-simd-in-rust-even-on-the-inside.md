# Safe SIMD in Rust, even on the inside

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-06-19 23:16
- **Original:** https://shnatsel.medium.com/safe-simd-in-rust-even-on-the-inside-c6f1ff381828

## Summary

Safe SIMD in Rust, even on the inside Rust’s SIMD abstractions were not as safe as I’d like. It’s no secret that raw SIMD intrinsics are unpleasant to use. You want to write a + b, not this monstrosity: unsafe { #[cfg(all(any(target_arch = "x86", target_arch = "x86_64"), target_feature = "avx2"))] _mm256_add_ps(a, b) #[cfg(all(any(target_arch = "x86", target_arch = "x86_64"), target_feature = "sse", not(target_feature = "avx2")))] _mm_add_ps(a, b) #[cfg(all(target_arch = "aarch64", target_feature = "neon"))] vaddq_f32(a, b) }Look at it.

## Key Takeaways

- And the whole thing is wrapped in unsafe!
- And that’s a simplified example.
- It still doesn’t handle: - Other common platforms: AVX-512, 32-bit ARM, WebAssembly - Platforms without SIMD or obscure platforms like RISC-V - Actually loading data like &[f32]into a form that each intrinsic accepts - Selecting the best implementation for the CPU it’s running on Luckily, Rust provides many SIMD abstractions that handle all of that for you and let you simply write a + b.

---
_Auto-generated daily digest entry._
