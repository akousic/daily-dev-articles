# AWS Introduces Nested Virtualization on EC2 Instances

- **Source:** InfoQ
- **Rank (today):** #6
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-03-07 14:32
- **Original:** https://www.infoq.com/news/2026/03/aws-ec2-nested-virtualization/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

AWS recently announced support for nested virtual machines within virtualized EC2 instances running KVM or Hyper-V. A long-awaited feature by the community, the new option enables use cases such as app emulation and hardware simulation on supported C8i, M8i, and R8i instances. Developers can use this feature to run mobile app emulators, simulate in-car automotive hardware, and use Windows Subsystem for Linux (WSL) on Windows workstations.

## Key Takeaways

- According to the documentation, the Nitro System exposes processor features such as Intel VT-x to the instance, allowing it to run virtual machines inside it.
- The architecture for nested virtualization has three layers: the physical AWS infrastructure and Nitro hypervisor (L0), your EC2 instance running its own hypervisor (L1), and the virtual machines running inside that instance (L2).
- The new feature supports KVM and Hyper-V on C8i, M8i, and R8i instances.

---
_Auto-generated daily digest entry._
