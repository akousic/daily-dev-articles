# Google and Meta Open-source TorchTPU to Bring Native PyTorch Support to Google TPUs

- **Source:** InfoQ
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-11-02 22:41
- **Original:** https://www.infoq.com/news/2026/11/torchtpu-native-pythorch-tpu/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

TorchTPU is an open-source project developed by Google in collaboration with Meta that provides a native PyTorch backend for Google TPUs. It enables PyTorch workloads to execute on TPU hardware with minimal code modifications, supporting eager and compiled execution, distributed computing, and hardware-specific optimizations. Google began enabling PyTorch workloads to run on TPUs in 2020 through PyTorch/XLA, which leveraged JAX, XLA, and lazy tensors.

## Key Takeaways

- According to Google, this approach had significant shortcomings: Crucially, PyTorch/XLA required intrusive source-code modifications to explicitly define compilable regions, suffered from severe compile-time latency, lacked support for PyTorch's native imperative (“eager”) execution mode, and lagged in supporting emerging distributed computing primitives within the PyTorch ecosystem.
- TorchTPU takes a fundamentally different approach, making eager execution a top priority, and enabling existing PyTorch workloads to run out with minor code modifications.
- Specifically, migrating from GPUs to TPUs involves replacing the cuda device with tpu and the nccl distributed backend with tpu_dist.

---
_Auto-generated daily digest entry._
