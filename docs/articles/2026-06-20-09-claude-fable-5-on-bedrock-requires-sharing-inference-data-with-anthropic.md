# Claude Fable 5 on Bedrock Requires Sharing Inference Data with Anthropic

- **Source:** InfoQ
- **Rank (today):** #9
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-06-20 15:48
- **Original:** https://www.infoq.com/news/2026/06/bedrock-fable-5-data-sharing/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

Using Anthropic's Claude Fable 5 or Mythos 5 on Amazon Bedrock requires opting into provider_data_share, a data retention mode that sends prompts and outputs to Anthropic for 30-day retention with human review. There is no alternative mode. The allowed_modes field for these models contains exactly one value.

## Key Takeaways

- For every previous model on Bedrock, including Opus 4.8, Sonnet, and Haiku, inference data stayed inside the AWS boundary, and model providers never saw it.
- That guarantee is what got Bedrock through procurement, legal review, and the security questionnaires that sit between a proof of concept and production.
- Fable 5 changes the deal.

---
_Auto-generated daily digest entry._
