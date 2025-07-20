# llm-contracts API Documentation

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Core API](#core-api)
- [Schema Reference](#schema-reference)
- [Validation Rules](#validation-rules)
- [CLI Reference](#cli-reference)
- [Error Handling](#error-handling)
- [Examples](#examples)

## Installation

```bash
pip install llm-contracts
```

## Quick Start

```python
from llm_contracts import contracts

# Validate output
result = contracts.validate(data, 'schema.yaml')

# Generate HTML report
contracts.generate_report(result, 'report.html', 'schema.yaml', 'html')

# Validate and report in one call
result = contracts.validate_and_report(data, 'schema.yaml', 'report.html', 'html')
```

## Core API

### `contracts.validate(data, schema_path, custom_validator=None)`

Validates output data against a YAML schema.

**Parameters:**
- `data` (dict or str): JSON data to validate
- `schema_path` (str or Path): Path to YAML schema file
- `custom_validator` (callable, optional): Custom validation function

**Returns:**
- `ValidationResult`: Object containing validation status and errors

**Example:**
```python
from llm_contracts import contracts

data = {
    "name": "John Doe",
    "age": 25,
    "email": "john@example.com"
}

result = contracts.validate(data, 'schemas/user_profile.yaml')

if not result.is_valid:
    print("Validation errors:", result.errors)
```

### `contracts.lint(data, schema_path, custom_validator=None)`

Lints content for quality and style issues.

**Parameters:**
- `data` (dict or str): Content to lint
- `schema_path` (str or Path): Path to YAML schema file with linting rules
- `custom_validator` (callable, optional): Custom validation function

**Returns:**
- `ValidationResult`: Object containing linting status and issues

**Example:**
```python
from llm_contracts import contracts

content = "This is a sample content for linting."

result = contracts.lint(content, 'style_rules.yaml')

if not result.is_valid:
    print("Linting issues:", result.errors)
```

### `contracts.generate_report(result, output_path, schema_path, format="html", schema_content=None)`

Generates a validation report in the specified format.

**Parameters:**
- `result` (ValidationResult): Validation result from validate() or lint()
- `output_path` (str): Path for the report file
- `schema_path` (str): Path to schema file for reference
- `format` (str): Report format ("html" or "markdown")
- `schema_content` (dict, optional): Schema content for rule references

**Example:**
```python
from llm_contracts import contracts

result = contracts.validate(data, 'schema.yaml')

# Generate HTML report
contracts.generate_report(result, 'validation_report.html', 'schema.yaml', 'html')

# Generate Markdown report
contracts.generate_report(result, 'validation_report.md', 'schema.yaml', 'markdown')
```

### `contracts.validate_and_report(data, schema_path, report_path=None, report_format="html", custom_validator=None)`

Validates data and optionally generates a report in one call.

**Parameters:**
- `data` (dict or str): Data to validate
- `schema_path` (str or Path): Path to schema file
- `report_path` (str, optional): Path for report file
- `report_format` (str): Report format ("html" or "markdown")
- `custom_validator` (callable, optional): Custom validation function

**Returns:**
- `ValidationResult`: Validation result

**Example:**
```python
from llm_contracts import contracts

result = contracts.validate_and_report(
    data, 'schema.yaml', 'report.html', 'html'
)
```

## Schema Reference

### Basic Schema Structure

```yaml
schema:
  # JSON schema definition
  field_name:
    type: str|int|float|bool|list|dict
    # ... validation rules

rules:
  # Text linting rules
  - rule_type: rule_value
```

### Schema Field Types

#### String Fields

```yaml
schema:
  name:
    type: str
    min_length: 2
    max_length: 50
    pattern: "^[A-Z][a-z]+$"
    required: true
```

#### Numeric Fields

```yaml
schema:
  age:
    type: int
    min: 0
    max: 120
    required: true
  
  price:
    type: float
    min: 0.0
    max: 10000.0
```

#### List Fields

```yaml
schema:
  tags:
    type: list
    min_items: 1
    max_items: 10
    items:
      type: str
      min_length: 2
```

#### Object Fields

```yaml
schema:
  address:
    type: dict
    properties:
      street:
        type: str
        required: true
      city:
        type: str
        required: true
      zip_code:
        type: str
        pattern: "^\\d{5}$"
```

## Validation Rules

### Keyword Rules

#### `keyword_must_include`

Ensures specific keywords are present in text content.

```yaml
rules:
  - keyword_must_include: "quality"
  - keyword_must_include: ["premium", "durable", "warranty"]
```

#### `keyword_must_not_include`

Ensures specific keywords are NOT present in text content.

```yaml
rules:
  - keyword_must_not_include: "cheap"
  - keyword_must_not_include: ["defective", "broken", "low quality"]
```

### Content Validation Rules

#### `no_placeholder_text`

Detects placeholder text patterns.

```yaml
rules:
  - no_placeholder_text: "\\[YOUR_TEXT_HERE\\]"
  - no_placeholder_text: "\\[DESCRIPTION\\]"
```

#### `word_count_min` / `word_count_max`

Enforces minimum and maximum word counts.

```yaml
rules:
  - word_count_min: 100
  - word_count_max: 500
```

### Advanced Rules

#### `regex_must_match`

Validates content against regex patterns.

```yaml
rules:
  - regex_must_match: "\\b\\d{1,3}(?:\\.\\d{2})?\\s*USD\\b"
```

#### `no_duplicate_sentences`

Detects duplicate sentences in content.

```yaml
rules:
  - no_duplicate_sentences: true
```

#### `min_list_items`

Ensures minimum number of list items.

```yaml
rules:
  - min_list_items: 3
```

#### `max_passive_voice_ratio`

Limits passive voice usage.

```yaml
rules:
  - max_passive_voice_ratio: 0.2
```

### Semantic Rules

#### `phrase_proximity`

Ensures specific terms appear within a certain distance of each other.

```yaml
rules:
  - phrase_proximity:
      terms: ["warranty", "30"]
      max_distance: 20
```

#### `phrase_order`

Ensures phrases appear in a specific order.

```yaml
rules:
  - phrase_order:
      first: "features"
      then: "buy now"
```

### Markdown Rules

#### `section_must_start_with`

Validates that sections start with specific patterns.

```yaml
rules:
  - section_must_start_with: "^# Introduction"
```

#### `heading_max_depth`

Limits the maximum heading depth.

```yaml
rules:
  - heading_max_depth: 3
```

#### `list_item_pattern`

Validates list item formatting.

```yaml
rules:
  - list_item_pattern: "^\\d+\\. [A-Z].*"
```

## CLI Reference

### Basic Usage

```bash
# Validate a file against a schema
llm-validate output.json --schema schema.yaml

# Generate HTML report
llm-validate output.json --schema schema.yaml --html-report report.html

# Generate Markdown report
llm-validate output.json --schema schema.yaml --md-report report.md

# Both HTML and Markdown reports
llm-validate output.json --schema schema.yaml --html-report report.html --md-report report.md
```

### Command Options

```bash
llm-validate <file> --schema <schema> [options]

Arguments:
  file                    Path to the file containing LLM output to validate

Options:
  -s, --schema PATH       Path to YAML schema file (required)
  -f, --output-format     Output format: text or json (default: text)
  --strict                Exit with error code 1 if validation fails
  --html-report PATH      Generate HTML report file
  --md-report PATH        Generate Markdown report file
  --help                  Show help message
```

### Output Formats

#### Text Output (Default)
```
Validating output.json against schema.yaml

✅ Validation passed!
```

#### JSON Output
```json
{
  "valid": true,
  "output_file": "output.json",
  "schema_file": "schema.yaml",
  "errors": [],
  "error_count": 0
}
```

### Exit Codes

- `0`: Validation passed or failed (non-strict mode)
- `1`: Validation failed (strict mode) or error occurred

## Error Handling

### ValidationResult Object

```python
from llm_contracts import contracts

result = contracts.validate(data, 'schema.yaml')

print(f"Valid: {result.is_valid}")
print(f"Error count: {len(result.errors)}")
print(f"Errors: {result.errors}")
```

### Custom Error Handling

```python
from llm_contracts import contracts, ValidationError

try:
    result = contracts.validate(data, 'schema.yaml')
    
    if not result.is_valid:
        print("Validation failed:")
        for error in result.errors:
            print(f"  - {error}")
            
except ValidationError as e:
    print(f"Validation error: {e.message}")
    if e.errors:
        for error in e.errors:
            print(f"  - {error}")
```

## Examples

### Basic Validation

```python
from llm_contracts import contracts

# Sample data
data = {
    "name": "John Doe",
    "age": 25,
    "email": "john@example.com",
    "bio": "Software engineer with 5 years of experience."
}

# Validate against schema
result = contracts.validate(data, 'user_profile.yaml')

if result.is_valid:
    print("✅ Validation passed!")
else:
    print("❌ Validation failed!")
    for error in result.errors:
        print(f"  - {error}")
```

### Content Linting

```python
from llm_contracts import contracts

# Sample content
content = "This is a sample product description that needs quality validation."

# Lint content
result = contracts.lint(content, 'content_rules.yaml')

if result.is_valid:
    print("✅ Content passed linting!")
else:
    print("❌ Content failed linting!")
    for error in result.errors:
        print(f"  - {error}")
```

### Report Generation

```python
from llm_contracts import contracts

# Validate and generate reports
result = contracts.validate_and_report(
    data, 
    'schema.yaml', 
    'validation_report.html', 
    'html'
)

# Or generate reports separately
result = contracts.validate(data, 'schema.yaml')
contracts.generate_report(result, 'report.html', 'schema.yaml', 'html')
contracts.generate_report(result, 'report.md', 'schema.yaml', 'markdown')
```

### Rule Bundles

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

### CI/CD Integration

```yaml
# GitHub Actions example
name: Validate LLM Outputs

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
          
      - name: Install dependencies
        run: |
          pip install llm-contracts
          
      - name: Validate outputs
        run: |
          llm-validate --batch outputs/ --schema schemas/ --html-report validation_report.html
          
      - name: Upload report
        uses: actions/upload-artifact@v3
        with:
          name: validation-report
          path: validation_report.html
``` 