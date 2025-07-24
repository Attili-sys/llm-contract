---
layout: default
title: Home
nav_order: 1
description: "LLM Contracts - Developer-first framework for validating, linting, and asserting the correctness of LLM-generated outputs."
permalink: /
---

# llm//contracts

> **LLM Output Validation, Linting, and Assertion Layer**

`llm-contracts` is a developer-first framework for validating, linting, and asserting the correctness of LLM-generated outputs. Think of it as "ESLint + Pytest" for AI responses — without requiring a specific model or cloud API.

If you're building with LLMs, this was made for you — by someone who actually uses them in production.

**Created by [Mohamed Jama](https://www.linkedin.com/in/mohamedjama/)**

## What It Does

We got burned too many times by "looks right" AI responses that quietly broke apps. This isn't another GPT wrapper — it's your test suite for machine output.

LLMs follow patterns, not instructions. What "looks right" can silently break apps. `llm-contracts` exists to:

- **Validate structure** (JSON, Markdown, text)
- **Lint content** (phrases, tone, repetition)
- **Assert semantic logic** (summaries, tool use)
- **Repair or reject** invalid outputs

This is a safety net between prompts and production.

## Quick Links

- [Installation Guide](installation.html)
- [Getting Started](getting-started.html)
- [Core Features](features.html)
- [Web Frontend](frontend.html)
- [Examples](examples.html)
- [API Reference](api-reference.html)
- [White Paper: Fluent, Confident, and Totally Wrong, Until Now](whitepaper.html)
- [GitHub Repository](https://github.com/Maxamed/llm-contract)

## How Is This Different?

**Validate AI like you validate code — enforce rules, not hope for the best.**

`llm-contracts` is not a model orchestration library. It doesn't reroute, repair, or retry outputs — it asserts correctness after the generation step.

| Tool / Library | Focus | llm-contracts Difference |
|---|---|---|
| **Guardrails** | Validates and rewrites model output | We validate and fail fast — no magic fixes |
| **Unstructured** | Parses messy documents into structure | We expect structure and enforce contracts |
| **Pydantic** | Python runtime type validation | We support language-level rules, not just types |
| **LLM-as-a-Judge** | Uses models to rate themselves | We use rules, not opinions |
| **LangChain** | Pipeline and toolchain orchestration | We're a QA layer, not orchestration |

**Think of this as the unit test framework for AI-generated content — not a controller, not a wrapper, not another GPT tool.**

> **Other tools try to fix LLM output.**  
> **llm-contracts asks:** "Did the AI follow the rules?"  
> **If not, we fail it — no excuses.**

Will this prevent GPT from inventing Martian presidents? No. But it will tell you when it does. 