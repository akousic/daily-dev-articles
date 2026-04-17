# Unweight: how we compressed an LLM 22% without sacrificing quality

- **Source:** Cloudflare
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-04-17 15:03
- **Original:** https://blog.cloudflare.com/unweight-tensor-compression/

## Summary

Running inference within 50ms of 95% of the world's Internet-connected population means being ruthlessly efficient with GPU memory. Last year we improved memory utilization with Infire, our Rust-based inference engine, and eliminated cold-starts with Omni, our model scheduling platform. Now we are tackling the next big bottleneck in our inference platform: model weights.

## Key Takeaways

- Generating a single token from an LLM requires reading every model weight from GPU memory.
- On the NVIDIA H100 GPUs we use in many of our datacenters, the tensor cores can process data nearly 600 times faster than memory can deliver it, leading to a bottleneck not in compute, but memory bandwidth.
- Every byte that crosses the memory bus is a byte that could have been avoided if the weights were smaller.

---
_Auto-generated daily digest entry._
