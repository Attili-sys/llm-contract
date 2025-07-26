---
layout: default
title: Examples
nav_order: 4
description: "Real-world examples - e-commerce, support, marketing, and more"
---

# Examples

[![PyPI version](https://img.shields.io/pypi/v/llm-contracts)](https://pypi.org/project/llm-contracts/) 

Here are some practical examples of using llm-contracts in different scenarios.

## Installation

```bash
pip install llm-contracts
```

## Basic Validation Example

### Schema Definition

```yaml
# product_description.yaml
schema:
  title:
    type: str
    min_length: 10
  description:
    type: str
    min_length: 100

rules:
  - keyword_must_include: ["quality", "premium", "durable"]
  - keyword_must_not_include: ["cheap", "low quality", "defective"]
  - no_placeholder_text: "\\[YOUR_TEXT_HERE\\]"
  - word_count_min: 100
  - word_count_max: 500
```

### Valid Output

```json
{
  "title": "Premium Wireless Headphones",
  "description": "Experience superior sound quality with our premium wireless headphones. Built with durable materials and advanced audio technology, these headphones deliver crystal-clear sound. Features include noise cancellation, 30-hour battery life, and premium comfort. Our 30-day warranty and hassle-free return policy ensure your satisfaction. Buy now with free shipping!"
}
```

### Python Code

```python
from llm_contracts import contracts

# Load data (could be from an LLM API)
data = {
  "title": "Premium Wireless Headphones",
  "description": "Experience superior sound quality with our premium wireless headphones..."
}

# Validate against schema
result = contracts.validate(
    data,
    "product_description.yaml"
)

# Check results
if result.success:
    print("Validation passed!")
else:
    print(f"Validation failed with {len(result.errors)} errors")
    for error in result.errors:
        print(f"- {error.message}")

# Generate a report
contracts.generate_report(
    result,
    "validation_report.html",
    "product_description.yaml",
    format="html"
)
```

## Rule Bundles Example

Rule bundles let you create reusable rule sets:

### Common Rules

```yaml
# common_rules.yaml
rules:
  - keyword_must_not_include: ["as an AI model", "I cannot"]
  - no_placeholder_text: "\\[YOUR_TEXT_HERE\\]"
  - word_count_min: 50
  - max_passive_voice_ratio: 0.3
```

### Team-Specific Rules

```yaml
# marketing_rules.yaml
rules:
  - include: "common_rules.yaml"
  - keyword_must_include: ["quality", "premium"]
  - min_list_items: 3

# technical_rules.yaml
rules:
  - include: "common_rules.yaml"
  - keyword_must_include: ["specifications", "requirements"]
  - regex_must_match: "\\b\\d+(?:\\.\\d+)?\\s*(?:GB|MB|TB)\\b"
```

### Usage

```python
from llm_contracts import contracts

# Marketing content validation
marketing_result = contracts.validate(
    marketing_data,
    "marketing_rules.yaml"
)

# Technical content validation
technical_result = contracts.validate(
    technical_data,
    "technical_rules.yaml"
)
```

## Markdown Validation Example

Validate structured Markdown content:

```yaml
# blog_post.yaml
schema:
  title:
    type: str
  content:
    type: str

rules:
  - section_must_start_with: "^# Introduction"
  - heading_max_depth: 3
  - list_item_pattern: "^\\d+\\. [A-Z].*"
  - keyword_must_include: "call to action"
  - no_placeholder_text: "\\[YOUR_TEXT_HERE\\]"
```

## CLI Usage Example

```bash
# Basic validation
llm-validate output.json --schema schema.yaml

# Generate HTML report
llm-validate output.json --schema schema.yaml --html-report report.html

# Generate Markdown report
llm-validate output.json --schema schema.yaml --md-report report.md

# Strict mode (fail on any error)
llm-validate output.json --schema schema.yaml --strict
```

## More Examples

For more examples, check out the [examples directory](https://github.com/Maxamed/llm-contract/tree/main/examples) in the GitHub repository. 