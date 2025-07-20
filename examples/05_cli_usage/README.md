# CLI Usage Example

This example demonstrates all the command-line interface features of llm-contracts.

## 📋 Overview

The CLI usage example shows:
- ✅ **Basic CLI validation** - Simple file validation
- ✅ **Report generation** - HTML and Markdown reports
- ✅ **Strict mode** - Exit codes for automation
- ✅ **JSON output** - Machine-readable results
- ✅ **Error handling** - Comprehensive error reporting

## 🚀 Quick Start

```bash
# Run the example
python cli_examples.py
```

## 📁 Files

- `cli_examples.py` - Main example script
- `cli_report.html` - Generated HTML report
- `cli_report.md` - Generated Markdown report
- `cli_report_both.html` - Both formats HTML report
- `cli_report_both.md` - Both formats Markdown report

## 🔍 CLI Commands

### Basic Validation

```bash
# Validate a single file
llm-validate output.json --schema schema.yaml

# Validate with verbose output
llm-validate output.json --schema schema.yaml --output-format text
```

**Example Output**:
```
Validating output.json against schema.yaml

❌ Validation failed!

Errors:
  - Must include keyword: 'professional'
```

### Report Generation

```bash
# Generate HTML report
llm-validate output.json --schema schema.yaml --html-report report.html

# Generate Markdown report
llm-validate output.json --schema schema.yaml --md-report report.md

# Generate both reports
llm-validate output.json --schema schema.yaml --html-report report.html --md-report report.md
```

**Example Output**:
```
Validating output.json against schema.yaml

❌ Validation failed!

Errors:
  - Word count (43) below minimum (50)
📄 HTML report generated: cli_report.html
📝 Markdown report generated: cli_report.md
```

### Strict Mode

```bash
# Normal mode (exit code 0 regardless of validation result)
llm-validate output.json --schema schema.yaml

# Strict mode (exit code 1 if validation fails)
llm-validate output.json --schema schema.yaml --strict
```

**Example Output**:
```
# Without --strict (exit code 0)
Validating output.json against schema.yaml

❌ Validation failed!

Errors:
  - Schema validation failed: 'john' does not match '^[A-Z][a-z]+ [A-Z][a-z]+$'

Exit code: 0

# With --strict (exit code 1)
Validating output.json against schema.yaml

❌ Validation failed!

Errors:
  - Schema validation failed: 'john' does not match '^[A-Z][a-z]+ [A-Z][a-z]+$'

Exit code: 1
```

### JSON Output

```bash
# Get JSON output for automation
llm-validate output.json --schema schema.yaml --output-format json
```

**Example Output**:
```json
{
  "valid": true,
  "output_file": "output.json",
  "schema_file": "schema.yaml",
  "errors": [],
  "error_count": 0
}
```

## 🧪 Running the Example

### Step 1: Basic CLI Validation

```python
import subprocess
import tempfile
import json

# Create temporary test files
with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
    json.dump({"name": "john doe", "bio": "Software engineer."}, f)
    data_file = f.name

with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
    f.write("""
schema:
  name:
    type: str
    pattern: "^[A-Z][a-z]+ [A-Z][a-z]+$"
  bio:
    type: str

rules:
  - keyword_must_include: "professional"
""")
    schema_file = f.name

# Run CLI validation
result = subprocess.run([
    "llm-validate", data_file, "--schema", schema_file
], capture_output=True, text=True)

print("CLI Output:")
print(result.stdout)
print(f"Exit code: {result.returncode}")
```

**Output**:
```
🔧 CLI Basic Validation
========================================
CLI Output:
Validating /tmp/data.json against /tmp/schema.yaml

❌ Validation failed!

Errors:
  - Must include keyword: 'professional'

Exit code: 0
```

### Step 2: Report Generation

```python
# Generate HTML report
result = subprocess.run([
    "llm-validate", data_file, "--schema", schema_file, "--html-report", "cli_report.html"
], capture_output=True, text=True)

print("Generating HTML report...")
print("CLI Output:")
print(result.stdout)
print(f"📄 HTML report generated: cli_report.html")
```

**Output**:
```
📄 CLI with Report Generation
========================================
Generating HTML report...
CLI Output:
Validating /tmp/data.json against /tmp/schema.yaml

❌ Validation failed!

Errors:
  - Word count (43) below minimum (50)
📄 HTML report generated: cli_report.html

Exit code: 0
```

### Step 3: Strict Mode Testing

```python
# Test without strict mode
result = subprocess.run([
    "llm-validate", data_file, "--schema", schema_file
], capture_output=True, text=True)

print("Running without --strict (should not exit with error)...")
print(f"Exit code: {result.returncode}")

# Test with strict mode
result = subprocess.run([
    "llm-validate", data_file, "--schema", schema_file, "--strict"
], capture_output=True, text=True)

print("Running with --strict (should exit with error)...")
print(f"Exit code: {result.returncode}")
```

### Step 4: JSON Output

```python
# Get JSON output
result = subprocess.run([
    "llm-validate", data_file, "--schema", schema_file, "--output-format", "json"
], capture_output=True, text=True)

print("Running with JSON output format...")
print("CLI Output:")
print(result.stdout)
```

## 📊 CLI Options Reference

### Command Structure

```bash
llm-validate <file> --schema <schema> [options]
```

### Arguments

| Argument | Description | Example |
|----------|-------------|---------|
| `file` | Path to the file containing LLM output to validate | `output.json` |

### Options

| Option | Description | Example |
|--------|-------------|---------|
| `-s, --schema PATH` | Path to YAML schema file (required) | `--schema schema.yaml` |
| `-f, --output-format` | Output format: text or json (default: text) | `--output-format json` |
| `--strict` | Exit with error code 1 if validation fails | `--strict` |
| `--html-report PATH` | Generate HTML report file | `--html-report report.html` |
| `--md-report PATH` | Generate Markdown report file | `--md-report report.md` |
| `--help` | Show help message | `--help` |

### Exit Codes

| Code | Description |
|------|-------------|
| `0` | Validation passed or failed (non-strict mode) |
| `1` | Validation failed (strict mode) or error occurred |

## 🔧 Integration Examples

### Shell Scripts

```bash
#!/bin/bash

# Validate content and exit on failure
if ! llm-validate content.json --schema schema.yaml --strict; then
    echo "Content validation failed!"
    exit 1
fi

echo "Content validation passed!"
```

### Makefile Integration

```makefile
validate:
	llm-validate content.json --schema schema.yaml --html-report validation_report.html

validate-strict:
	llm-validate content.json --schema schema.yaml --strict

validate-json:
	llm-validate content.json --schema schema.yaml --output-format json
```

### Python Scripts

```python
import subprocess
import sys

def validate_content(data_file, schema_file, strict=False):
    """Validate content using CLI."""
    cmd = ["llm-validate", data_file, "--schema", schema_file]
    
    if strict:
        cmd.append("--strict")
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print("Validation failed:", file=sys.stderr)
        print(result.stdout, file=sys.stderr)
        return False
    
    print("Validation passed!")
    return True

# Usage
if not validate_content("content.json", "schema.yaml", strict=True):
    sys.exit(1)
```

## 🎯 Use Cases

### Development Workflows
- **Pre-commit hooks** - Validate content before committing
- **CI/CD pipelines** - Automated validation in build process
- **Quality gates** - Ensure content meets standards

### Content Management
- **Batch processing** - Validate multiple files
- **Report generation** - Create validation reports
- **Error tracking** - Monitor validation failures

### Automation
- **Scripts** - Integrate into existing workflows
- **Monitoring** - Track validation success rates
- **Alerts** - Notify on validation failures

## 🔗 Related Examples

- [Basic Validation](../01_basic_validation/) - Core validation functionality
- [Rule Bundles](../02_rule_bundles/) - Reusable rule sets
- [Advanced Rules](../03_advanced_rules/) - Advanced validation rules
- [Markdown Reports](../04_markdown_reports/) - CI/CD report generation

## 🤝 Next Steps

1. **Integrate CLI into your workflows** using the provided examples
2. **Set up automated validation** in your CI/CD pipeline
3. **Create custom scripts** for your specific needs
4. **Monitor validation results** over time
5. **Share CLI usage** with your team 