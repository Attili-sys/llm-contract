---
layout: default
title: Whitepaper
description: "Deep dive: Why LLM validation matters and how llm-contracts solves production AI challenges"
---

# llm-contracts: Fluent, Confident, and Totally Wrong, Until Now

*A white paper by Mohamed Jama, July 2025*

*Implementation support and web interface by [Abdirahman Attila](https://github.com/Attili-sys)*

## Executive Summary

AI is already writing your product descriptions, responding to customer queries, summarizing your meetings, and generating your marketing content. But do you actually know what it's saying?

While these systems are impressive, they're often unreliable - and the risks they introduce are invisible until it's too late. AI-generated outputs can be grammatically perfect, confident in tone, and still factually wrong, legally noncompliant, or off-brand.

Over the past year, building GenAI apps across industries, I've seen firsthand that most teams trust model output without safeguards. We assume because the model returns a string in the correct format, it understood the task. But LLMs don't follow instructions - they follow patterns that sound like instructions were followed.

**llm-contracts fixes this by introducing a contract layer.** Think of it as schema validation, rule enforcement, and output QA - for everything your AI says. It lets you:

- Define strict rules for AI output (structure, tone, keywords, etc.)
- Automatically validate every LLM response before it hits production
- Fail fast when the output doesn't meet expectations

In short:
- Your team defines the standards
- The contract checks every output
- Bad content gets caught before it causes harm

This paper outlines the business and engineering risks of unvalidated AI content, the gaps in current tooling, and how llm-contracts introduces a reliable new enforcement layer for teams deploying LLMs at scale.

## The Problem with Trusting LLMs

LLMs are pattern generators, not rule followers. They don't "understand" - they autocomplete plausible answers. And when you say:

- "Return JSON with these fields."
- "Use this exact format."
- "Don't hallucinate."

...they will try. But they'll get it wrong just often enough to quietly break your feature, mislead your user, or undermine trust in your product.

### Hidden Failure Modes

- A chatbot promises a bereavement fare policy the company doesn't offer - resulting in legal action and reimbursement (Air Canada, 2024)
- A media site publishes AI-generated financial advice with interest rate errors - leading to corrections and public backlash (CNET, 2023)
- A lawyer submits fake legal citations in court - written by ChatGPT - and faces sanctions for misinformation (Mata v. Avianca, 2023)
- A support bot quietly omits refund eligibility because of a misparsed prompt template

And I've seen it in practice - at startups and tech giants alike - where raw LLM output is piped directly into user-facing apps with no validation at all.

> A virtual assistant for a food delivery app confidently explained that pineapple is banned from delivery in all EU countries - citing a "EU Ingredient Code 91.4" regulation. The company received confused emails from customers and temporarily pulled the feature.
> 
> (Just kidding - last one's fake. But you didn't question it, did you? That's the point. It could've been real, and you wouldn't have known. That's how easy it is for confident nonsense to slip into production.)

Just pure, uncut trust.

### Why Traditional Testing Doesn't Work

Software developers have linters, test cases, and schema validation. But LLM outputs are natural language - they can be mostly right and still cause harm. There's no unit test for "Does this paragraph reflect company policy?" or "Is this answer legally compliant?" You can't assert correctness with a test case. That's where llm-contracts steps in.

### Not Hallucinations. Pattern Illusions.

The industry calls these errors "hallucinations." But that implies randomness. The truth is: they're statistical illusions. The model is doing what it was trained to do - output the most likely-seeming response. Whether it's correct, compliant, or complete is not part of its process.

### The Clock Tower Analogy

A child asks, "Why are clock towers built so high?" Another answers:

"So other kids can't break them." It's confidently stated. It sounds logical. But it's completely wrong. That's what LLMs do every day. Answers that look right but aren't. Structured, fluent, wrong. You can't prompt your way out of this. You need to validate the output.

These aren't random errors; they're byproducts of models trained to predict likely continuations - not truth, intent, or instruction. The result? Outputs that pass the eye test but fail the reality test.

## The llm-contracts Solution

llm-contracts treat AI like a subcontractor. It provides the output with a strict contract - and checks whether it kept its side of the deal.

Here's how it works:

1. You define what "acceptable output" looks like - structure, phrasing, tone, required fields.
2. The LLM generates a response.
3. llm-contracts intercepts and validates the output against your rules.
4. If it passes - it's delivered. If not - it's flagged, blocked, or corrected.

### Types of Rules

**Structural Rules**: These ensure the AI's output looks exactly like what your app expects - whether that's a JSON object, Markdown snippet, or structured paragraph. It prevents runtime errors and unexpected behaviors.

**Required Content**: You can specify phrases, numbers, or facts that must be present. For example: a warranty message, a legal disclaimer, or a product spec line.

**Tone/Style Constraints**: You can block passive voice, overly promotional language, or anything that doesn't sound like your brand.

**Semantic Checks**: These rules look deeper - like making sure there are exactly 5 list items or that dates follow a specific format.

Every output is validated automatically. If it breaks the rules - you catch it before it reaches your user. This isn't just syntax checking. It's brand protection, trust enforcement, and automated QA for AI.

## Real-World Use Cases

### E-commerce

Ensure AI-generated product pages include required spec lines, exclude risky terms, and match tone. A major retailer cut return-related complaints by validating all copy before publishing.

### Customer Support

Prevent drift in chatbot responses. After one model update, a support assistant began offering unauthorized discounts. llm-contracts caught and blocked 97 invalid replies in the first week.

### Marketing

A content team using LLMs to write landing pages added contracts requiring every post to include CTAs and product names. Validation caught template errors and placeholder text before publishing.

### Legal & Policy

A compliance department used llm-contracts to ensure disclaimers were included in all AI-generated FAQs and summaries. Zero omission errors after adoption.

### GenAI QA Teams

Internal prompt engineers now wrap every test run with output validation. Saves hours of manual review - and surfaces consistent model bugs that were previously missed.

## Why This Matters Now

Based on months of hard-won lessons building GenAI systems, I've seen these truths play out:

- Hallucinations aren't bugs - they're the default
- Prompting alone isn't enough
- You need structure, validation, logging, and QA - like with any other system

As teams race to production, they're skipping safety steps. They're not defining "correct." They're not logging failures. And they're definitely not validating outputs. You don't need another wrapper. You need enforcement. llm-contracts gives you that - without rewriting your stack, changing your model, or adding latency.

## Summary of Benefits

Teams that adopt llm-contracts will see measurable improvements in safety, efficiency, and confidence when deploying AI at scale. Key benefits include:

- **Increased Brand Safety**: Ensure that all AI-generated content aligns with tone, terminology, and approved messaging.
- **Reduced Legal and Compliance Risk**: Catch missing disclaimers, hallucinated claims, or improper formatting before users see them.
- **Faster Time to Market**: Automate QA and eliminate manual review cycles, allowing faster deployment of GenAI features.
- **Improved Customer Trust**: Prevent factual or structural errors that erode credibility and damage user confidence.
- **Scalable AI Governance**: Bring engineering-grade validation and observability to AI-generated content workflows.

## Where It's Going

llm-contracts is just getting started. We're working toward:

- Community-shared rule libraries for common use cases
- Better error reporting and logging
- IDE/editor plugins for live rule previews
- Integration with CI pipelines for prompt validation before deployment

The goal? To make validation as common as prompting.

## What to Do Next

llm-contracts is open-source and production-ready. If you:

- Use LLMs in customer-facing features
- Care about trust, tone, and structure
- Want to reduce hallucination risk
- Need to move faster without QA debt

Then you should:

- Explore the GitHub project: [github.com/Maxamed/llm-contract](https://github.com/Maxamed/llm-contract) - read the overview, browse examples, and understand the structure
- Try it out: Follow the [quickstart guide](getting-started) to define your first validation contract
- Fork or adapt the repo (optional): For customization or contribution
- Contact us: For walkthroughs, integration help, or enterprise support

**You wouldn't ship an app without tests.**

**Why ship AI without contracts?** llm-contracts brings quality control to LLMs - and peace of mind to the teams who use them.

*Written by Mohamed Jama - software engineer, GenAI practitioner, and creator of llm-contracts.* 