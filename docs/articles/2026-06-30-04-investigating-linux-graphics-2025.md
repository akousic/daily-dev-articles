# Investigating Linux graphics (2025)

- **Source:** Lobsters
- **Rank (today):** #4
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-06-30 01:34
- **Original:** https://roscidus.com/blog/blog/2025/06/24/graphics/

## Summary

I learn how to draw a triangle with a GPU, and then trace the code to find out how the graphics system works (or doesn't), looking at Mesa3D, GLFW, OpenGL, Vulkan, Wayland and Linux DRM. Table of Contents - Introduction - Overview - OpenGL - Vulkan - Synchronisation - First attempt at tracing - Removing GLFW - Removing Vulkan's Wayland extension - Wayland walk-through - Kernel details with bpftrace - Re-examining the errors - Conclusions Introduction In the past, I've avoided graphics driver problems on Linux by using only Intel integrated graphics. But, due to a poor choice of motherboard, I ended up needing a separate graphics card.

## Key Takeaways

- Now my computer takes 14s to resume from suspend and dmesg is spewing this kind of thing: [59829.886009] [drm] Fence fallback timer expired on ring sdma0 [59830.390003] [drm] Fence fallback timer expired on ring sdma0 [59830.894002] [drm] Fence fallback timer expired on ring sdma0 [79622.739495] amdgpu 0000:01:00.0: [drm:amdgpu_ring_test_helper [amdgpu]] *ERROR* ring comp_1.0.1 test failed (-110) [79622.909019] amdgpu 0000:01:00.0: [drm:amdgpu_ring_test_helper [amdgpu]] *ERROR* ring comp_1.0.2 test failed (-110) [79623.075056] amdgpu 0000:01:00.0: [drm:amdgpu_ring_test_helper [amdgpu]] *ERROR* ring comp_1.0.3 test failed (-110) [79623.241971] amdgpu 0000:01:00.0: [drm:amdgpu_ring_test_helper [amdgpu]] *ERROR* ring comp_1.0.4 test failed (-110) [79623.408604] amdgpu 0000:01:00.0: [drm:amdgpu_ring_test_helper [amdgpu]] *ERROR* ring comp_1.0.6 test failed (-110) [80202.893020] [drm] scheduler comp_1.0.1 is not ready, skipping [80202.893023] [drm] scheduler comp_1.0.2 is not ready, skipping [80202.893024] [drm] scheduler comp_1.0.3 is not ready, skipping [80202.893025] [drm] scheduler comp_1.0.4 is not ready, skipping [80202.893025] [drm] scheduler comp_1.0.6 is not ready, skipping [80202.936910] [drm] scheduler comp_1.0.1 is not ready, skipping But what is a "fence" or an "sdma0" ring?
- What are these comp_ schedulers, and why does Linux Oops when enough of them aren't ready?
- And why does Firefox hang when playing videos since upgrading NixOS?

---
_Auto-generated daily digest entry._
