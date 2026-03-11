# FFmpeg-over-IP – Connect to remote FFmpeg servers

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 215
- **Published (UTC):** 2026-03-10 18:26
- **Original:** https://github.com/steelbrain/ffmpeg-over-ip

## Summary

Use GPU-accelerated ffmpeg from anywhere — a Docker container, a VM, or a remote machine — without GPU passthrough or shared filesystems. GPU transcoding is powerful, but getting access to the GPU is painful: - Docker containers need --runtime=nvidia , device mounts, and driver version alignment between host and container - Virtual machines need PCIe passthrough or SR-IOV — complex setup that locks the GPU to one VM - Remote machines need shared filesystems (NFS/SMB) with all the path mapping, mount maintenance, and permission headaches that come with them You just want your media server to use the GPU for transcoding. You shouldn't need to restructure your infrastructure to make that happen.

## Key Takeaways

- Run the ffmpeg-over-ip server on the host (or any machine with a GPU).
- Point your app at the client binary instead of ffmpeg.
- Done — your app gets GPU-accelerated transcoding without needing direct GPU access.

---
_Auto-generated daily digest entry._
