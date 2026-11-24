# GitHub Actions accepts invalid YAML

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-11-22 15:49
- **Original:** https://yossarian.net/til/post/github-actions-accepts-invalid-yaml/

## Summary

TL;DR: GitHub Actions accepts several invalid YAML productions, making it difficult (read: impossible) to parse some real-world action and workflow definitions with a properly conforming YAML parser. This is related to zizmor#1116, which has been bugging me for a year and a half. Last April, a user reported that zizmor was rejecting a workflow containing a step that looks like this: - name: Create NPM Remote Repository JSON uses: jsdaniell/create-json@v1.2.3 with: name: "npm-remote-template.json" json: '{ "key": "npm-remote", "rclass": "remote", "packageType": "npm", "url": "https://registry.npmjs.org" }' Apart from the use of a multi-line flow-style string for the json: key, nothing particularly stands out about this step.

## Key Takeaways

- Except: it isn't valid YAML!
- YAML says this about flow-style nodes that are nested inside of a block-style parent collection (read: map or array): Flow nodes must be indented by at least one more space than the parent block collection.
- Note that flow nodes may begin on a following line.

---
_Auto-generated daily digest entry._
