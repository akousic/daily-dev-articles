# AI sandbox that runs on your homelab

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-02-27 05:47
- **Original:** https://github.com/deevus/pixels

## Summary

Disposable Linux containers for AI coding agents, powered by TrueNAS and Incus. Spin up sandboxed Linux containers pre-loaded with AI coding tools (Claude Code, Codex, OpenCode via mise). Each container gets SSH access, ZFS snapshot-based checkpoints, and network egress policies that control what the agent can reach.

## Key Takeaways

- Managed entirely from the CLI over TrueNAS WebSocket API.
- - Container lifecycle -- create, start, stop, destroy, and list Incus containers - SSH access -- interactive console and remote command execution - ZFS checkpoints -- snapshot, restore, delete, and clone containers from checkpoints - AI agent provisioning -- automatically installs mise, Claude Code, Codex, and OpenCode - Network egress policies -- restrict outbound traffic to AI APIs, package registries, and Git (or a custom allowlist) - Configuration -- TOML config file, PIXELS_* environment variables, and CLI flags - Local caching -- disk cache avoids WebSocket round-trips for console/exec - TrueNAS SCALE with Incus virtualization enabled - TrueNAS API key (create one in the TrueNAS web UI under Credentials > API Keys) - Go 1.25+ (for building from source) - SSH key pair (defaults to ~/.ssh/id_ed25519 ) go install github.com/deevus/pixels@latest Or build from source: git clone https://github.com/deevus/pixels.git cd pixels go build # Create a base container with agent egress restrictions pixels create base --egress agent --console # Set up your environment, install dependencies, etc.
- # Then save a checkpoint pixels checkpoint create base --label ready # Spin up new containers from the checkpoint pixels create task1 --from base:ready pixels create task2 --from base:ready # Or clone from a container's current state pixels create task3 --from base # Tear down when done pixels destroy task1 pixels destroy task2 | Command | Description | |---|---| pixels create <name> | Create a new container | pixels start <name> | Start a stopped container | pixels stop <name> | Stop a running container | pixels destroy <name> | Permanently destroy a container and all its checkpoints | pixels list | List all containers with status and IP | pixels console <name> | Open an interactive SSH session | pixels exec <name> -- <command...> | Run a command via SSH | pixels checkpoint create <name> | Create a ZFS snapshot | pixels checkpoint list <name> | List checkpoints with sizes | pixels checkpoint restore <name> <label> | Restore to a checkpoint | pixels checkpoint delete <name> <label> | Delete a checkpoint | pixels network show <name> | Show current egress rules | pixels network set <name> <mode> | Set egress mode | pixels network allow <name> <domain> | Add a domain to the allowlist | pixels network deny <name> <domain> | Remove a domain from the allowlist | Global flags: --host , --api-key , -u/--username , -v/--verbose # Create with custom resources pixels create mybox --image ubuntu/24.04 --cpu 4 --memory 4096 # Create with agent sandbox and open console when ready pixels create mybox --egress agent --console # Skip all provisioning (no SSH keys, devtools, or egress setup) pixels create mybox --no-provision # Clone from an existing container's checkpoint pixels create newbox --from mybox:ready # Clone from an existing container's current state pixels create newbox --from mybox All containers are prefixed px- internally.

---
_Auto-generated daily digest entry._
