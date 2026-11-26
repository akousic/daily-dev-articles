# I Built My First Multi-Agent System on AWS, and It Was Easier Than I Expected

- **Source:** Dev.to
- **Rank (today):** #5
- **Ranking metrics:** reactions 102, comments 46
- **Published (UTC):** 2026-11-25 15:26
- **Original:** https://dev.to/hemapriya_kanagala/i-built-my-first-multi-agent-system-on-aws-and-it-was-easier-than-i-expected-58c2

## Summary

TL;DR I recently completed the final project of Udacity's Future AWS Agent Engineer Nanodegree Program, which I had the opportunity to pursue through the AWS AI & ML Scholarship. And just like that, I've officially graduated from the Nanodegree 🎓 This was my third project working with AI agent systems, but my first time building a multi-agent system using Strands Agents and Amazon Bedrock AgentCore. The project was a fictional e-commerce customer support system for NovaMart.

## Key Takeaways

- Instead of having one agent handle everything, it used an Orchestrator and four specialized agents: Inventory, Policy, Refund, and Communication.
- They coordinated their work, shared information through a common WorkflowState in DynamoDB, and retrieved information from three separate Knowledge Bases covering Returns, Shipping, and Warranty.
- Along the way, I worked with Amazon Bedrock Guardrails, AgentCore Runtime and Memory, parallel retrieval using Python, CloudWatch, and AWS X-Ray.

---
_Auto-generated daily digest entry._
