# HashiCorp Vault 1.21 Brings SPIFFE Authentication, Granular Secret Recovery, and More

- **Source:** InfoQ
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-03-28 14:40
- **Original:** https://www.infoq.com/news/2026/03/hashicorp-vault-1-21/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

HashiCorp has released Vault 1.21. This version introduces native SPIFFE authentication for non-human workloads, expands the granular secret recovery model introduced in Vault 1.20, and adds KV v2 secret attribution, MFA TOTP self-enrollment, a Vault Secrets Operator CSI driver that mounts secrets directly into pods without persisting them in etcd, and more. Vault Enterprise 1.21 adds native support for SPIFFE (Secure Production Identity Framework For Everyone), an open standard for assigning cryptographically verifiable identities to workloads in dynamic environments.

## Key Takeaways

- With SPIFFE, non-human identities like microservices, containers, and serverless functions can authenticate to Vault using X509 or JWT-based SVIDs (SPIFFE Verifiable Identity Documents) without relying on static credentials or manual configuration.
- Beyond authentication, Vault can now issue X509-SVIDs to workloads that already authenticate through methods like AppRole or AWS auth, enabling them to participate in SPIFFE-based service-to-service communication without additional tooling.
- This makes Vault both a consumer and issuer of SPIFFE identities, useful for organizations building zero-trust architectures across Kubernetes, hybrid, and multi-cloud environments.

---
_Auto-generated daily digest entry._
