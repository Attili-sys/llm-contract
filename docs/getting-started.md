---
layout: default
title: Getting Started
nav_order: 2
description: "Quick start guide - install llm-contracts and validate your first LLM output"
---

# Getting Started with llm-contracts

This guide will walk you through the basic usage of llm-contracts to validate LLM outputs.

## Basic Concepts

llm-contracts works by validating LLM outputs against predefined schemas and rules:

- **Schemas** define the structure and data types of your LLM output
- **Rules** define content requirements and constraints
- **Reports** provide detailed validation results

## Basic Usage

### Using the CLI

The command-line interface is the quickest way to validate outputs:

```bash
# Validate a single file
llm-validate output.json --schema schema.yaml

# Generate HTML report
llm-validate output.json --schema schema.yaml --html-report report.html

# Generate Markdown report
llm-validate output.json --schema schema.yaml --md-report report.md
```

### Using the Python SDK

For more flexibility, use the Python SDK:

```python
from llm_contracts import contracts

# Validate output against schema
result = contracts.validate(
    data,                    # Dict or JSON string
    schema_path,            # Path to YAML schema
)

# Generate HTML report
contracts.generate_report(
    result,                 # Validation result
    output_path,           # HTML file path
    schema_path,           # Schema file path
    format="html"          # Report format
)

# Generate Markdown report
contracts.generate_report(
    result,                 # Validation result
    output_path,           # Markdown file path
    schema_path,           # Schema file path
    format="markdown"      # Report format
)

# Validate and report in one call
result = contracts.validate_and_report(
    data,                  # Data to validate
    schema_path,           # Schema file path
    report_path,           # Optional report file path
    report_format="html"   # Report format
)
```

## Creating a Schema

Schemas are defined in YAML format:

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

rules:
  - keyword_must_include: ["quality", "premium"]
  - keyword_must_not_include: ["cheap", "defective"]
  - word_count_min: 100
```

## Next Steps

- Check out the [Examples](examples) for more use cases
- Learn about [Core Features](features) for advanced usage
- Try the [Web Frontend](frontend) for a visual interface 