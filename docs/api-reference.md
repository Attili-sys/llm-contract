---
layout: default
title: API Reference
nav_order: 6
description: "Complete API documentation for Python SDK and CLI"
---

# API Reference

This page documents the core APIs of the llm-contracts library.

## CLI Commands

```bash
llm-validate <file> --schema <schema> [options]
```

### Options

| Option | Description |
|--------|-------------|
| `--schema <file>` | Path to the YAML schema file |
| `--html-report <file>` | Generate HTML report |
| `--md-report <file>` | Generate Markdown report |
| `--output-format <format>` | Output format (text/json) |
| `--strict` | Fail on any validation error |
| `--help` | Show help message |

## Python SDK

### Validation

```python
from llm_contracts import contracts

# Validate output against schema
result = contracts.validate(
    data,                    # Dict or JSON string
    schema_path,            # Path to YAML schema
)
```

#### Parameters

- `data`: Dict or JSON string containing the data to validate
- `schema_path`: Path to the YAML schema file

#### Return Value

Returns a `ValidationResult` object with the following properties:

- `success`: Boolean indicating if validation passed
- `errors`: List of validation errors
- `warnings`: List of validation warnings
- `schema`: The parsed schema object

### Report Generation

```python
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
```

#### Parameters

- `result`: ValidationResult object from validate()
- `output_path`: Path to save the report
- `schema_path`: Path to the schema file
- `format`: Report format ("html" or "markdown")

### Combined Validation and Reporting

```python
# Validate and report in one call
result = contracts.validate_and_report(
    data,                  # Data to validate
    schema_path,           # Schema file path
    report_path,           # Optional report file path
    report_format="html"   # Report format
)
```

#### Parameters

- `data`: Dict or JSON string containing the data to validate
- `schema_path`: Path to the YAML schema file
- `report_path`: Path to save the report (optional)
- `report_format`: Report format ("html" or "markdown")

## Schema Format

### Basic Schema Structure

```yaml
schema:
  field_name:
    type: str|int|float|bool|list|dict
    # Other validation properties

rules:
  # Content validation rules
  - rule_type: rule_value
```

### Field Types and Properties

| Type | Properties |
|------|------------|
| `str` | `min_length`, `max_length`, `pattern`, `enum` |
| `int` | `min`, `max`, `enum` |
| `float` | `min`, `max`, `enum` |
| `bool` | N/A |
| `list` | `min_items`, `max_items`, `items` |
| `dict` | `properties`, `required` |

### Rule Types

| Rule | Description |
|------|-------------|
| `keyword_must_include` | Text must include specified keywords |
| `keyword_must_not_include` | Text must not include specified keywords |
| `no_placeholder_text` | Text must not include placeholder patterns |
| `word_count_min` | Minimum word count |
| `word_count_max` | Maximum word count |
| `regex_must_match` | Text must match specified regex pattern |
| `no_duplicate_sentences` | No duplicate sentences allowed |
| `min_list_items` | Minimum number of list items |
| `max_passive_voice_ratio` | Maximum ratio of passive voice |
| `phrase_proximity` | Maximum distance between specified terms |
| `phrase_order` | Terms must appear in specified order |

For a complete reference, see the [API.md](https://github.com/Maxamed/llm-contract/blob/main/API.md) file in the GitHub repository. 