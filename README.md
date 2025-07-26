# llm-contracts

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://img.shields.io/badge/tests-84%25%20coverage-brightgreen.svg)](https://github.com/Maxamed/llm-contract)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/Maxamed/llm-contract)

> **Developer-first framework for validating LLM-generated outputs**

Think of it as "ESLint + Pytest" for AI responses — without requiring a specific model or cloud API.

**📖 [Full Documentation & Examples →](https://maxamed.github.io/llm-contract)**

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/Maxamed/llm-contract.git
cd llm-contracts

# Install in development mode
pip install -e .
```

### Basic Usage

#### CLI

```bash
# Validate a single file
llm-validate output.json --schema schema.yaml

# Generate reports
llm-validate output.json --schema schema.yaml --html-report report.html
llm-validate output.json --schema schema.yaml --md-report report.md
```

#### Python API

```python
from llm_contracts import contracts

# Validate output against schema
result = contracts.validate(data, "schema.yaml")

if not result.is_valid:
    print("Validation failed:")
    for error in result.errors:
        print(f"  - {error}")

# Generate reports
contracts.generate_report(result, "report.html", "schema.yaml", format="html")
contracts.generate_report(result, "report.md", "schema.yaml", format="markdown")
```

### Example Schema

```yaml
schema:
  title:
    type: str
    min_length: 10
  description:
    type: str
    min_length: 100

rules:
  - keyword_must_include: ["quality", "premium"]
  - keyword_must_not_include: ["cheap", "defective"]
  - no_placeholder_text: "\\[YOUR_TEXT_HERE\\]"
  - word_count_min: 100
  - word_count_max: 500
```

## Features

- **Schema-based validation** - JSON Schema validation for structure
- **Content linting rules** - Keyword requirements, patterns, quality checks
- **Professional reports** - HTML and Markdown validation reports
- **CLI and Python API** - Use in scripts or integrate into applications
- **Framework agnostic** - Works with any LLM or application

## Web Frontend (Optional)

Run a web interface for testing and building schemas:

```bash
cd frontend
pip install -r requirements.txt
python server.py
# Open index.html in your browser
```

## Documentation & Examples

- **[Complete Documentation](https://maxamed.github.io/llm-contract)** - Full guide and examples
- **[examples/](examples/)** - Ready-to-run examples
- **[API Reference](API.md)** - Complete API documentation
- **[Contributing](CONTRIBUTING.md)** - Development setup and guidelines

## Testing

```bash
# Run all tests
python -m pytest tests/

# Run with coverage
python -m pytest --cov=llm_contracts tests/
```

## Contributors

This project was created and is maintained by **[Mohamed Jama](https://www.linkedin.com/in/mohamedjama/)**.

**Major Contributors:**
- **[Abdirahman Attila](https://github.com/Attili-sys)** - Frontend web interface, comprehensive documentation website, enhanced testing suite, and Jekyll/GitHub Pages setup

See [CONTRIBUTORS.md](CONTRIBUTORS.md) for detailed contribution history.

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Created By

**[Mohamed Jama](https://www.linkedin.com/in/mohamedjama/)** - Built for developers shipping AI features in production.

---

*For detailed examples, use cases, and the complete whitepaper, visit [our documentation site](https://maxamed.github.io/llm-contract).* 