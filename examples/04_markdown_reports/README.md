# Markdown Reports Example

This example demonstrates how to generate markdown reports for CI/CD integration and team communication.

## 📋 Overview

The markdown reports example shows:
- ✅ **Markdown report generation** - Clean, readable reports
- ✅ **CI/CD integration** - Batch processing workflows
- ✅ **Error categorization** - Organized error reporting
- ✅ **Success rate calculation** - Statistical summaries
- ✅ **Multiple file validation** - Batch validation workflows

## 🚀 Quick Start

```bash
# Run the example
python markdown_reports_example.py
```

## 📁 Files

- `markdown_reports_example.py` - Main example script
- `validation_report.md` - Generated markdown report
- `validation_report.html` - Generated HTML report
- `ci_cd_summary.md` - CI/CD summary report

## 🔍 Example Details

### Individual Report Generation

**Purpose**: Generate detailed markdown reports for individual validations

```python
from llm_contracts import contracts

# Sample content for validation
content = """# Product Description

This is a high quality product that costs 29.99 USD. 
It features excellent durability and comes with a comprehensive warranty.

Features:
1. Premium quality materials
2. Extended warranty coverage
3. Professional support

The product is designed for maximum performance."""

# Validate and generate markdown report
result = contracts.validate_and_report(
    content, 
    'product_schema.yaml', 
    'validation_report.md', 
    'markdown'
)
```

**Generated Report** (`validation_report.md`):
```markdown
# Validation Report

**Status**: ❌ FAIL  
**Schema**: product_schema.yaml  
**Timestamp**: 2024-01-15 10:30:00  

## Summary
- **Total Errors**: 2
- **Validation Status**: Failed

## Errors
1. **Must include keyword**: 'quality'
2. **Word count (35) below minimum (50)**

## Schema Information
- **Schema File**: product_schema.yaml
- **Rules Applied**: 5
- **Validation Type**: Content + Structure

## Recommendations
- Add required keywords to content
- Increase word count to meet minimum requirements
```

### CI/CD Batch Processing

**Purpose**: Process multiple files and generate summary reports

```python
# Sample files for batch processing
files_to_validate = [
    {
        "name": "product_announcement.md",
        "content": "New product launch with amazing features.",
        "schema": "marketing_schema.yaml"
    },
    {
        "name": "technical_specs.md", 
        "content": "Technical specifications for the product.",
        "schema": "technical_schema.yaml"
    },
    {
        "name": "marketing_copy.md",
        "content": "High quality marketing copy with call to action and limited time offer.",
        "schema": "marketing_schema.yaml"
    }
]

# Process all files
results = []
for file_info in files_to_validate:
    result = contracts.validate(file_info["content"], file_info["schema"])
    results.append({
        "file": file_info["name"],
        "result": result,
        "schema": file_info["schema"]
    })

# Generate summary report
generate_summary_report(results, "ci_cd_summary.md")
```

**Generated Summary Report** (`ci_cd_summary.md`):
```markdown
# CI/CD Validation Summary

**Date**: 2024-01-15  
**Time**: 10:30:00  
**Total Files**: 3  

## Summary Statistics
- **Passed**: 1
- **Failed**: 2
- **Success Rate**: 33.3%

## File Results

### ✅ product_announcement.md
- **Status**: PASS
- **Schema**: marketing_schema.yaml
- **Errors**: 0

### ❌ technical_specs.md
- **Status**: FAIL
- **Schema**: technical_schema.yaml
- **Errors**: 2
  - Must include keyword: 'quality'
  - Content must match regex pattern: '\b\d{1,3}(?:\.\d{2})?\s*USD\b'

### ❌ marketing_copy.md
- **Status**: FAIL
- **Schema**: marketing_schema.yaml
- **Errors**: 1
  - Word count (15) below minimum (20)

## Recommendations
- Review failed files and fix validation errors
- Consider updating schemas if rules are too strict
- Monitor success rate trends over time
```

## 🧪 Running the Example

### Step 1: Individual Report Generation

```python
from llm_contracts import contracts

# Test content
content = "This is a sample content for validation."

# Generate markdown report
result = contracts.validate_and_report(
    content, 
    'content_schema.yaml', 
    'validation_report.md', 
    'markdown'
)

print(f"✅ Validation completed!")
print(f"📊 Results: {'PASS' if result.is_valid else 'FAIL'}")
print(f"📄 Markdown report generated: validation_report.md")
```

**Output**:
```
📝 Markdown Reports Example
==================================================
📋 Validating content...
✅ Validation completed!
📊 Results: FAIL
📄 Markdown report generated: validation_report.md
📄 HTML report generated: validation_report.html
```

### Step 2: CI/CD Integration

```python
# Simulate CI/CD batch processing
files = [
    {"name": "product_announcement.md", "content": "New product launch.", "schema": "marketing.yaml"},
    {"name": "technical_specs.md", "content": "Technical specs.", "schema": "technical.yaml"},
    {"name": "marketing_copy.md", "content": "High quality marketing copy.", "schema": "marketing.yaml"}
]

print("🔄 CI/CD Integration Example")
print("==================================================")
print("Running validation on multiple files...\n")

for file_info in files:
    result = contracts.validate(file_info["content"], file_info["schema"])
    status = "✅ PASS" if result.is_valid else "❌ FAIL"
    print(f"📄 Validating {file_info['name']}...")
    print(f"   {status}")
    if not result.is_valid:
        for error in result.errors:
            print(f"     - {error}")
    print()
```

## 📊 Report Formats

### Markdown Report Features

- ✅ **Clean formatting** - Easy to read in any markdown viewer
- 📋 **Detailed error information** - Specific error messages
- 📊 **Statistics** - Success rates and error counts
- 📄 **Schema references** - Links to schema files
- 🎯 **Recommendations** - Actionable improvement suggestions

### HTML Report Features

- 🎨 **Responsive design** - Works on all devices
- 📊 **Interactive elements** - Expandable error details
- 🎯 **Color coding** - Visual status indicators
- 📋 **Search functionality** - Find specific errors quickly
- 📄 **Print-friendly** - Optimized for printing

## 🔧 CI/CD Integration

### GitHub Actions Example

```yaml
name: Validate Content

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
          
      - name: Validate content
        run: |
          llm-validate --batch content/ --schema schemas/ --md-report validation_report.md
          
      - name: Upload report
        uses: actions/upload-artifact@v3
        with:
          name: validation-report
          path: validation_report.md
          
      - name: Comment on PR
        if: github.event_name == 'pull_request'
        uses: actions/github-script@v6
        with:
          script: |
            const fs = require('fs');
            const report = fs.readFileSync('validation_report.md', 'utf8');
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: `## Content Validation Report\n\n${report}`
            });
```

### GitLab CI Example

```yaml
validate_content:
  stage: test
  image: python:3.9
  script:
    - pip install llm-contracts
    - llm-validate --batch content/ --schema schemas/ --md-report validation_report.md
  artifacts:
    reports:
      markdown: validation_report.md
    paths:
      - validation_report.md
```

## 🎯 Use Cases

### Content Teams
- **Pre-publication validation** - Ensure content meets standards
- **Quality assurance** - Catch errors before publishing
- **Team communication** - Share validation results

### Development Teams
- **Documentation validation** - Ensure docs meet requirements
- **API documentation** - Validate OpenAPI descriptions
- **Code comments** - Ensure consistent commenting style

### Marketing Teams
- **Copy validation** - Ensure brand guidelines
- **Campaign content** - Validate marketing materials
- **SEO requirements** - Check keyword inclusion

## 🔗 Related Examples

- [Basic Validation](../01_basic_validation/) - Core validation functionality
- [Rule Bundles](../02_rule_bundles/) - Reusable rule sets
- [Advanced Rules](../03_advanced_rules/) - Advanced validation rules
- [CLI Usage](../05_cli_usage/) - Command-line interface

## 🤝 Next Steps

1. **Integrate into your CI/CD pipeline** using the provided examples
2. **Customize report formats** for your team's needs
3. **Set up automated validation** for your content workflows
4. **Monitor validation trends** over time
5. **Share reports with stakeholders** for transparency 