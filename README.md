# llm-contracts

![PyPI version](https://img.shields.io/pypi/v/llm-contracts)
![Python](https://img.shields.io/badge/python-3.8+-blue)
![License](https://img.shields.io/github/license/Maxamed/llm-contract)
![Tests](https://img.shields.io/badge/tests-84%25%20coverage-brightgreen)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)

> **"ESLint + Pytest" for AI responses** — Catch LLM mistakes before they reach production.  
> Schema validation, content linting, and professional reports for any LLM.

**Website:** https://maxamed.github.io/llm-contract/

---

## Install

```bash
pip install llm-contracts
```

---

## Why `llm-contracts`?

LLMs are **fluent, confident, and totally wrong** just often enough to break your app.

- **Air Canada's chatbot** promised non-existent bereavement fares → Legal action
- **CNET's AI** published financial advice with wrong interest rates → Public corrections  
- **ChatGPT lawyer** submitted fake legal citations in court → Professional sanctions

`llm-contracts` validates every AI response **before** it causes problems.

---

## Quick Start

### CLI
```bash
# Validate AI output against schema
llm-validate output.json --schema schema.yaml

# Generate professional reports
llm-validate output.json --schema schema.yaml --html-report report.html
```

### Python API
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

---

## Key Features

- **Schema-based validation** - Enforce structure, types, and constraints
- **Text linting rules** - Content quality, keywords, patterns, tone analysis
- **Professional reports** - HTML and Markdown validation reports
- **Framework-agnostic** - Works with any LLM (OpenAI, Anthropic, local models)
- **Zero dependencies** - No external API calls, runs anywhere Python runs
- **CLI + Python SDK** - Use from command line or integrate programmatically

---

## Example Schema

```yaml
schema:
  warranty_period:
    type: str
    pattern: "^(30|90|365) days?$"

rules:
  - keyword_must_include: ["warranty", "return policy"]  
  - keyword_must_not_include: ["guaranteed", "always", "never"]
  - no_placeholder_text: "\\[INSERT_.*\\]"
  - word_count_min: 100
  - phrase_proximity:
      terms: ["warranty", "30 days"]
      max_distance: 20
```

---

## Documentation & Links

* [Complete Documentation & Whitepaper](https://maxamed.github.io/llm-contract/)
* [Getting Started Guide](https://maxamed.github.io/llm-contract/getting-started)
* [Real-World Examples](https://maxamed.github.io/llm-contract/examples)
* [API Reference](https://maxamed.github.io/llm-contract/api-reference)
* [Web Interface](https://maxamed.github.io/llm-contract/frontend)

---

## Contributors

This project was created and is maintained by **[Mohamed Jama](https://www.linkedin.com/in/mohamedjama/)**.

**Major Contributors:**
- **[Abdirahman Attila](https://github.com/Attili-sys)** - Frontend web interface, comprehensive documentation website, enhanced testing suite, and Jekyll/GitHub Pages setup

See [CONTRIBUTORS.md](CONTRIBUTORS.md) for detailed contribution history.

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

**Built by developers who ship AI features that actually work.** 