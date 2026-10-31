# OpenBSD 8.0 Brings Expanded Hardware Support, Security Enhancements, and Virtualization Improvements

- **Source:** InfoQ
- **Rank (today):** #6
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-10-31 18:24
- **Original:** https://www.infoq.com/news/2026/10/openbsd-8-released/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

OpenBSD 8.0 is a substantial upgrade bringing broader hardware compatibility, enhanced security, an expanded virtual address space, and support for modern architectures, including Intel Arc A-Series graphics support, ARM64 hibernation, RISC-V improvements, and enhanced virtual machine support. Key hardware and virtualization improvements in OpenBSD 8.0 include a larger virtual address space for the AMD64 kernel, expanded from 4 GB to 512 GB, enabling it to map graphics cards with more than 4 GB of VRAM; support for multi-processor virtual machines through vmm/vmd, with up to 64 virtual CPUs per guest and improvements to virtual hardware and guest compatibility; expanded RISC-V support, including the 'V' vector extension and Advanced Interrupt Architecture, improving compatibility with newer processors and platforms; and arm64 hibernation support, alongside faster swap encryption using AES instructions. Although OpenBSD 8.0 introduces support for the Intel Arc A-Series GPUs, based on the DG2/Alchemist architecture, NVIDIA GPUs remain unsupported, partially due to the fact that NVIDIA does not provide proprietary binary drivers for OpenBSD, unlike Linux and FreeBSD.

## Key Takeaways

- OpenBSD 8.0 also expands peripheral support, including the riscv64 K3 PCIe/USB3 combo PHY, the SpacemiT K3 SoC and PCIe controller, as well as the Intel E610 and Panther Lake and Wildcat Lake Ethernet devices.
- New drivers are now available for Samsung Advanced BIOS Interface (SABI), Rockchip OTP memory, and Samsung laptop battery monitor.
- Wireless adapters support has been significantly expanded as well, including support for the Qualcomm Technologies WCN7850 wireless network in the qwz driver.

---
_Auto-generated daily digest entry._
