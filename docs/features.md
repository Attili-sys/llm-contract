---
layout: default
title: Core Features
nav_order: 4
description: "Core features of llm-contracts"
---

# Core Features

llm-contracts provides a comprehensive set of features for validating LLM outputs:

## Schema-Based Validation

Define the expected structure and data types of your LLM output:

```yaml
schema:
  name:
    type: str
    pattern: "^[A-Z][a-z]+ [A-Z][a-z]+$"
  age:
    type: int
    min: 18
    max: 65
  tags:
    type: list
    min_items: 1
    items:
      type: str
```

## Text Linting Rules

Apply content validation rules to ensure quality and consistency:

```yaml
rules:
  # Keyword requirements
  - keyword_must_include: ["quality", "premium"]
  - keyword_must_not_include: ["cheap", "defective"]
  
  # Content validation
  - no_placeholder_text: "\\[YOUR_TEXT_HERE\\]"
  - word_count_min: 100
  - word_count_max: 500
  
  # Advanced rules
  - regex_must_match: "\\b\\d{1,3}(?:\\.\\d{2})?\\s*USD\\b"
  - no_duplicate_sentences: true
  - min_list_items: 3
  - max_passive_voice_ratio: 0.2
  
  # Semantic rules
  - phrase_proximity:
      terms: ["warranty", "30"]
      max_distance: 20
  - phrase_order:
      first: "features"
      then: "buy now"
```

## Rule Bundles

Create reusable rule sets for teams:

```yaml
# common_rules.yaml
rules:
  - keyword_must_not_include: ["as an AI model", "I cannot"]
  - no_placeholder_text: "\\[YOUR_TEXT_HERE\\]"
  - word_count_min: 50
  - max_passive_voice_ratio: 0.3

# product_schema.yaml
rules:
  - include: "common_rules.yaml"
  - keyword_must_include: ["quality", "premium"]
  - min_list_items: 3
```

## Professional Reports

Generate detailed validation reports in multiple formats:

### HTML Reports

```bash
llm-validate output.json --schema schema.yaml --html-report validation_report.html
```

HTML reports include:
- Error categorization and highlighting
- Schema reference sections
- Success rate calculations
- Responsive design

### Markdown Reports

```bash
llm-validate output.json --schema schema.yaml --md-report validation_report.md
```

Markdown reports are perfect for CI/CD pipelines and GitHub integrations.

## CLI Integration

Integrate with your workflow using the command-line interface:

```bash
# Basic validation
llm-validate output.json --schema schema.yaml

# Strict mode (fail on any error)
llm-validate output.json --schema schema.yaml --strict

# JSON output for programmatic use
llm-validate output.json --schema schema.yaml --output-format json
```

## Python API

Use the Python API for programmatic validation:

```python
from llm_contracts import contracts

# Validate output against schema
result = contracts.validate(data, schema_path)

# Check if validation passed
if result.success:
    print("Validation passed!")
else:
    print(f"Validation failed with {len(result.errors)} errors")
    for error in result.errors:
        print(f"- {error.message}")
``` 