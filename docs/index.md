---
layout: default
title: Home
nav_order: 1
description: "Stop trusting LLM output. Start validating it. Developer-first framework for catching AI mistakes before they reach production."
---

# LLMs Are Fluent, Confident, and **Totally Wrong**

## Until Now.

**llm-contracts** is the first developer-first framework for validating, linting, and asserting the correctness of LLM-generated outputs. Think of it as **ESLint + Pytest for AI responses** — without requiring a specific model or cloud API.

[Get Started on GitHub](https://github.com/Maxamed/llm-contract){: .btn}
[Read the Whitepaper](whitepaper){: .btn}

---

## The Problem That Keeps You Up At Night

> **You deployed an AI feature last week. It's working perfectly.**  
> **Except when it confidently tells customers about warranty policies that don't exist.**  
> **Or invents product specifications.**  
> **Or promises shipping to countries you don't serve.**

**Sound familiar?**

### Real-World AI Failures:
- ✈️ **Air Canada's chatbot** promised non-existent bereavement fares → Legal action
- 💰 **CNET's AI writer** published financial advice with wrong interest rates → Public corrections
- ⚖️ **ChatGPT lawyer** submitted fake legal citations in court → Professional sanctions
- 🛒 **E-commerce AI** invented product features that didn't exist → Customer complaints

**The pattern:** LLMs generate responses that **look perfect** but **break everything.**

---

## The Solution: Contracts for AI Output

Instead of hoping your AI "gets it right," **llm-contracts** lets you define exactly what "right" looks like:

```yaml
# Your contract with the AI
schema:
  warranty_period:
    type: str
    pattern: "^(30|90|365) days?$"  # Only valid warranty periods
  
rules:
  - keyword_must_include: ["warranty", "return policy"]
  - keyword_must_not_include: ["guaranteed", "always", "never"]
  - no_placeholder_text: "\\[INSERT_.*\\]"
  - word_count_min: 100
  - phrase_proximity:
      terms: ["warranty", "30 days"]
      max_distance: 20  # Warranty details must be close together
```

**Result:** Every AI response gets validated before reaching your users. **No more silent failures.**

---

## See It In Action

### ❌ **Before llm-contracts:**
```json
{
  "product_description": "[INSERT_PRODUCT_NAME] is the best quality item you'll ever buy! We guarantee 100% satisfaction always and forever. Our unlimited warranty covers everything!"
}
```
*Passes the "looks good" test. Breaks everything else.*

### ✅ **After llm-contracts:**
```yaml
✅ Schema validation: PASSED
❌ Placeholder text detected: "[INSERT_PRODUCT_NAME]"
❌ Forbidden keywords: "guarantee", "always", "unlimited"
❌ Missing required: "30-day warranty", "return policy"

VALIDATION FAILED - Output rejected
```
*Catches the problems **before** they reach production.*

---

## Why Developers Choose llm-contracts

### 🚀 **Framework-Agnostic**
Works with **any LLM** (OpenAI, Anthropic, local models) and **any framework** (LangChain, direct API calls, custom implementations).

### 🛡️ **Production-Ready**
Built by developers who've shipped AI features at scale. Handles edge cases, provides detailed error reporting, and integrates with your existing CI/CD.

### 🎯 **Zero Vendor Lock-in**
No API calls to external services. No model-specific prompting tricks. Just pure validation logic that runs anywhere Python runs.

### 📊 **Professional Reports**
Generate beautiful HTML and Markdown validation reports for stakeholders, compliance, and debugging.

---

## How Is This Different?

**Validate AI like you validate code — enforce rules, not hope for the best.**

| Tool | Approach | llm-contracts Difference |
|------|----------|--------------------------|
| **Guardrails** | Tries to fix bad output | We **fail fast** — no magic repairs |
| **LangChain** | Orchestrates AI pipelines | We're a **QA layer**, not orchestration |
| **Pydantic** | Python type validation | We validate **content quality**, not just types |
| **Manual Review** | Human checks everything | We **automate validation** at machine speed |

> **Other tools try to fix LLM output.**  
> **llm-contracts asks:** "Did the AI follow the rules?"  
> **If not, we fail it — no excuses.**

---

## Get Started Today

### Installation
```bash
# Clone the repository
git clone https://github.com/Maxamed/llm-contract.git
cd llm-contracts

# Install the package
pip install -e .
```

### Quick Validation
```bash
# Validate AI output against your rules
llm-validate output.json --schema schema.yaml --html-report report.html
```

### Python API
```python
from llm_contracts import contracts

# Validate and get detailed results
result = contracts.validate(ai_output, "schema.yaml")
if not result.is_valid:
    print(f"AI failed validation: {result.errors}")
```

[View Full Documentation](getting-started)
[Try the Web Interface](frontend)

---

## Learn More

- **[🎯 The Problem](whitepaper#the-problem-with-trusting-llms)** - Why LLM validation matters
- **[⚡ Core Features](features)** - Schema validation, content linting, and reporting
- **[📚 Real Use Cases](examples)** - E-commerce, support, marketing, and more
- **[🌐 Web Interface](frontend)** - Try validation in your browser
- **[📄 Complete Whitepaper](whitepaper)** - Deep dive into the business case

---

**Stop hoping your AI gets it right.**
**Start knowing it does.**

[Get Started on GitHub →](https://github.com/Maxamed/llm-contract)

---

**Created by [Mohamed Jama](https://www.linkedin.com/in/mohamedjama/) for developers who ship AI features that actually work.**

*Major contributions by [Abdirahman Attila](https://github.com/Attili-sys) - Frontend interface, documentation website, and testing infrastructure.* 