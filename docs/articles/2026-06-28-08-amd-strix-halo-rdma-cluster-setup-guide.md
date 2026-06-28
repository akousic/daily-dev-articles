# AMD Strix Halo RDMA Cluster Setup Guide

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 195
- **Published (UTC):** 2026-06-28 00:46
- **Original:** https://github.com/kyuz0/amd-strix-halo-vllm-toolboxes/blob/main/rdma_cluster/setup_guide.md

## Summary

This guide details how to configure a two-node AMD Strix Halo cluster linked via Intel E810 (RoCE v2) for distributed vLLM inference using Tensor Parallelism. - TL;DR (Quick Start) - Concepts & Architecture - Hardware Prerequisites - Host Configuration (Fedora) - Toolbox Installation & Network Verification - Running the Cluster - Troubleshooting - References & Acknowledgements On Both Nodes: - Preparation: - Install/Update Fedora 43 and the E810 NICs (Check firmware: ethtool -i <iface>). - BIOS/Kernel: Set iGPU to 512MB and apply kernel params (iommu=pt,pci=realloc, etc.).

## Key Takeaways

- - SSH: Configure passwordless SSH between nodes.
- - Install/Update Fedora 43 and the E810 NICs (Check firmware: - Networking: Assign static IPs (192.168.100.1&.2), set MTU 9000, and trust the interface in firewall.
- - Install Toolbox: Run ./refresh_toolbox.sh(this automatically installs the container with RDMA support and the customlibrccl.sopatch).

---
_Auto-generated daily digest entry._
