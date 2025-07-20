# <span style="font-family: 'Courier New', monospace; font-size: 20px;">llm//</span><span style="font-family: Georgia, serif; font-style: italic; font-size: 20px;">contracts</span>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

> **LLM Output Validation, Linting, and Assertion Layer**

`llm-contracts` is a developer-first framework for validating, linting, and asserting the correctness of LLM-generated outputs. Think of it as "ESLint + Pytest" for AI responses — without requiring a specific model or cloud API.

**Created by [Mohamed Jama](https://www.linkedin.com/in/mohamedjama/)**

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/Maxamed/llm-contract.git
cd llm-contracts

# Install in development mode
pip install -e .
```

### Basic Usage

```bash
# Validate a single file
llm-validate output.json --schema schema.yaml

# Generate HTML report
llm-validate output.json --schema schema.yaml --html-report report.html

# Generate Markdown report
llm-validate output.json --schema schema.yaml --md-report report.md

# Batch processing
llm-validate --batch outputs/ --schema schema.yaml
```

### Python SDK

```python
from llm_contracts import contracts

# Validate output
result = contracts.validate(data, 'schema.yaml')

# Generate HTML report
contracts.generate_report(result, 'report.html', 'schema.yaml', 'html')

# Generate Markdown report
contracts.generate_report(result, 'report.md', 'schema.yaml', 'markdown')

# Validate and report in one call
result = contracts.validate_and_report(data, 'schema.yaml', 'report.html', 'html')
```

## 🎯 What It Does

LLMs follow patterns, not instructions. What "looks right" can silently break apps. `llm-contracts` exists to:

- ✅ **Validate structure** (JSON, Markdown, text)
- ✅ **Lint content** (phrases, tone, repetition)
- ✅ **Assert semantic logic** (summaries, tool use)
- ✅ **Repair or reject** invalid outputs

This is a safety net between prompts and production.

## 🧰 Core Features

### Schema-Based Validation

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

### Text Linting Rules

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

### Professional Reports

Generate beautiful, detailed validation reports in multiple formats:

```bash
# HTML report
llm-validate output.json --schema schema.yaml --html-report validation_report.html

# Markdown report (perfect for CI/CD)
llm-validate output.json --schema schema.yaml --md-report validation_report.md
```

Reports include:
- Error categorization and highlighting
- Schema reference sections
- Success rate calculations
- Responsive design (HTML)
- Markdown formatting (MD)

## 📖 Examples

### Rule Bundles

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

### Product Description Validation

**Schema** (`product_description.yaml`):
```yaml
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
  - keyword_must_include: "warranty"
  - keyword_must_include: "return policy"
  - phrase_proximity:
      terms: ["warranty", "30"]
      max_distance: 20
```

**Valid Output**:
```json
{
  "title": "Premium Wireless Headphones",
  "description": "Experience superior sound quality with our premium wireless headphones. Built with durable materials and advanced audio technology, these headphones deliver crystal-clear sound. Features include noise cancellation, 30-hour battery life, and premium comfort. Our 30-day warranty and hassle-free return policy ensure your satisfaction. Buy now with free shipping!"
}
```

**Invalid Output** (fails validation):
```json
{
  "title": "Cheap Headphones",
  "description": "[YOUR_TEXT_HERE] These low quality headphones are defective and broken. [DESCRIPTION]"
}
```

### Markdown Blog Post Validation

**Schema** (`blog_post.yaml`):
```yaml
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

## 🛠️ Advanced Usage

### Custom Validators

```python
from llm_contracts import contracts

def custom_validator(content, schema):
    # Your custom validation logic
    if "spam" in content.lower():
        return False, ["Content contains spam"]
    return True, []

# Use in validation
result = contracts.validate(data, 'schema.yaml', custom_validator=custom_validator)
```

### Batch Processing

```bash
# Validate all JSON files in a directory
llm-validate --batch outputs/ --schema schema.yaml --html-report batch_report.html
```

### Integration with CI/CD

```yaml
# GitHub Actions example
- name: Validate LLM Outputs
  run: |
    git clone https://github.com/Maxamed/llm-contract.git
    cd llm-contracts
    pip install -e .
    llm-validate --batch outputs/ --schema schemas/ --html-report validation_report.html
```

## 📚 API Reference

### CLI Commands

```bash
llm-validate <file> --schema <schema> [options]

Options:
  --html-report <file>    Generate HTML report
  --md-report <file>      Generate Markdown report
  --output-format <format> Output format (text/json)
  --strict               Fail on any validation error
  --help                 Show help message
```

### Python SDK

```python
from llm_contracts import contracts

# Validate output against schema
result = contracts.validate(
    data,                    # Dict or JSON string
    schema_path,            # Path to YAML schema
    custom_validator=None   # Optional custom validator
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
    report_format="html",  # Report format
    custom_validator=None  # Optional custom validator
)
```

## 🧪 Testing

```bash
# Run all tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/test_schema.py

# Run with coverage
python -m pytest --cov=llm_contracts tests/
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup

```bash
# Clone repository
git clone https://github.com/Maxamed/llm-contract.git
cd llm-contracts

# Install in development mode
pip install -e .

# Run tests
python -m pytest tests/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Created by**: [Mohamed Jama](https://www.linkedin.com/in/mohamedjama/)
- **Inspired by**: The need for reliable LLM output validation
- **Built with**: Modern Python best practices
- **Designed for**: Developer productivity

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/Maxamed/llm-contract/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Maxamed/llm-contract/discussions)
- **LinkedIn**: [Mohamed Jama](https://www.linkedin.com/in/mohamedjama/)

---

**Made with ❤️ for the AI development community by Mohamed Jama** 