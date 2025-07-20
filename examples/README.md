# llm-contracts Examples

This directory contains comprehensive examples demonstrating all features of llm-contracts.

## 📁 Example Structure

```
examples/
├── 01_basic_validation/          # Core validation functionality
├── 02_rule_bundles/             # Reusable rule sets
├── 03_advanced_rules/           # Advanced validation rules
├── 04_markdown_reports/         # CI/CD report generation
├── 05_cli_usage/               # Command-line interface
├── schemas/                     # Shared schema files
├── rule_bundles/               # Shared rule bundles
└── README.md                   # This file
```

## 🚀 Quick Start

### Prerequisites

```bash
# Install llm-contracts
pip install -e .

# Navigate to examples
cd examples
```

### Run All Examples

```bash
# Run all examples
python 01_basic_validation/basic_validation.py
python 02_rule_bundles/rule_bundles_example.py
python 03_advanced_rules/advanced_rules_example.py
python 04_markdown_reports/markdown_reports_example.py
python 05_cli_usage/cli_examples.py
```

## 📖 Example Details

### 01_basic_validation/

**Purpose**: Demonstrate core validation functionality with the contracts API.

**Features**:
- ✅ Basic schema validation
- ✅ Text linting rules
- ✅ Report generation (HTML & Markdown)
- ✅ `contracts.validate()` API usage

**Files**:
- `basic_validation.py` - Main example script
- `user_profile.yaml` - User profile schema
- `product_description.yaml` - Product description schema

**Usage**:
```python
from llm_contracts import contracts

# Basic validation
result = contracts.validate(data, 'schema.yaml')

# Validation with reports
result = contracts.validate_and_report(
    data, 'schema.yaml', 'report.html', 'html'
)
```

**Expected Output**:
```
🔍 Basic Validation Example
==================================================
📋 Validating user profile...
❌ Validation FAILED!
Errors found:
  - Must include keyword: 'professional'

📄 Validation with Report Generation
==================================================
📋 Validating product description...
✅ Validation completed!
📊 Results: FAIL
📄 Reports generated:
  - HTML: validation_report.html
  - Markdown: validation_report.md
```

### 02_rule_bundles/

**Purpose**: Demonstrate reusable rule bundles for teams.

**Features**:
- ✅ Rule bundle creation and usage
- ✅ Team-specific rule sets
- ✅ Recursive includes
- ✅ Relative path resolution

**Files**:
- `rule_bundles_example.py` - Main example script
- `product_with_bundles.yaml` - Schema using bundles
- `rule_bundles/` - Rule bundle files
  - `common_rules.yaml` - Common validation rules
  - `ecommerce_rules.yaml` - E-commerce specific rules

**Usage**:
```yaml
# common_rules.yaml
rules:
  - keyword_must_not_include: ["as an AI model", "I cannot"]
  - no_placeholder_text: "\\[YOUR_TEXT_HERE\\]"

# product_schema.yaml
rules:
  - include: "common_rules.yaml"
  - keyword_must_include: ["quality", "premium"]
```

**Expected Output**:
```
📦 Rule Bundles Example
==================================================
📋 Validating product with rule bundles...
❌ Validation FAILED!
Errors found:
  - Must include keyword: 'quality'
  - Must have at least 3 list items, found 0
  - Content must match regex pattern: '\b\d{1,3}(?:\.\d{2})?\s*USD\b'
  - Content must start with pattern: '^# Product Description'
```

### 03_advanced_rules/

**Purpose**: Demonstrate all advanced validation rules.

**Features**:
- ✅ `regex_must_match` - Pattern validation
- ✅ `no_duplicate_sentences` - Content quality
- ✅ `min_list_items` - List validation
- ✅ `max_passive_voice_ratio` - Writing style

**Files**:
- `advanced_rules_example.py` - Main example script

**Usage**:
```yaml
rules:
  - regex_must_match: "\\b\\d{1,3}(?:\\.\\d{2})?\\s*USD\\b"
  - no_duplicate_sentences: true
  - min_list_items: 3
  - max_passive_voice_ratio: 0.2
```

**Expected Output**:
```
🧪 Advanced Rules Examples
============================================================

🔍 Testing regex_must_match Rule
========================================
✅ Valid text: PASS
❌ Invalid text: FAIL
   Error: Content must match regex pattern: '\b\d{1,3}(?:\.\d{2})?\s*USD\b'

🔄 Testing no_duplicate_sentences Rule
========================================
✅ Valid text: PASS
❌ Invalid text: FAIL
   Error: Duplicate sentences found: 1 instances
```

### 04_markdown_reports/

**Purpose**: Demonstrate markdown report generation for CI/CD.

**Features**:
- ✅ Markdown report generation
- ✅ CI/CD integration examples
- ✅ Batch processing
- ✅ Error categorization

**Files**:
- `markdown_reports_example.py` - Main example script

**Usage**:
```python
# Generate markdown report
contracts.generate_report(result, 'report.md', 'schema.yaml', 'markdown')

# CLI usage
llm-validate data.json --schema schema.yaml --md-report report.md
```

**Expected Output**:
```
📝 Markdown Reports Example
==================================================
📋 Validating content...
✅ Validation completed!
📊 Results: FAIL
📄 Markdown report generated: validation_report.md
📄 HTML report generated: validation_report.html

🔄 CI/CD Integration Example
==================================================
Running validation on multiple files...

📄 Validating product_announcement.md...
   ❌ FAIL
     - Word count (15) below minimum (20)
📄 Validating technical_specs.md...
   ❌ FAIL
     - Must include keyword: 'quality'
📄 Validating marketing_copy.md...
   ✅ PASS

📊 Summary Report
Files processed: 3
Passed: 1
Failed: 2
Success rate: 33.3%
```

### 05_cli_usage/

**Purpose**: Demonstrate all CLI features and options.

**Features**:
- ✅ Basic CLI validation
- ✅ Report generation (HTML & Markdown)
- ✅ Strict mode
- ✅ JSON output format
- ✅ Error handling

**Files**:
- `cli_examples.py` - Main example script

**Usage**:
```bash
# Basic validation
llm-validate data.json --schema schema.yaml

# With reports
llm-validate data.json --schema schema.yaml --html-report report.html --md-report report.md

# Strict mode
llm-validate data.json --schema schema.yaml --strict

# JSON output
llm-validate data.json --schema schema.yaml --output-format json
```

**Expected Output**:
```
🔧 CLI Usage Examples
============================================================

🔧 CLI Basic Validation
========================================
CLI Output:
Validating /tmp/data.json against /tmp/schema.yaml

❌ Validation failed!

Errors:
  - Must include keyword: 'professional'

Exit code: 0

📄 CLI with Report Generation
========================================
Generating HTML report...
CLI Output:
Validating /tmp/data.json against /tmp/schema.yaml

❌ Validation failed!

Errors:
  - Word count (43) below minimum (50)
📄 HTML report generated: cli_report.html
```

## 🧪 Testing Examples

### Run Individual Examples

```bash
# Basic validation
cd 01_basic_validation
python basic_validation.py

# Rule bundles
cd ../02_rule_bundles
python rule_bundles_example.py

# Advanced rules
cd ../03_advanced_rules
python advanced_rules_example.py

# Markdown reports
cd ../04_markdown_reports
python markdown_reports_example.py

# CLI usage
cd ../05_cli_usage
python cli_examples.py
```

### Expected Output

Each example will show:
- ✅ **PASS/FAIL** status for each test
- 📊 **Error details** when validation fails
- 📄 **Generated reports** (HTML/Markdown)
- 🔧 **CLI output** and exit codes

## 📊 Example Scenarios

### 1. User Profile Validation
- **Schema**: Name format, age range, email validation
- **Rules**: Professional keywords, word count, no placeholders
- **Result**: Validates user profile data

### 2. Product Description Validation
- **Schema**: Product ID format, price range, category enum
- **Rules**: Quality keywords, warranty requirements, SEO terms
- **Result**: Validates e-commerce product data

### 3. Team Rule Bundles
- **Marketing**: Call-to-action, limited time offers, word limits
- **Technical**: Specifications, performance metrics, technical terms
- **Result**: Reusable rules for different teams

### 4. Advanced Content Analysis
- **Regex**: Price formatting, email validation
- **Quality**: Duplicate detection, passive voice analysis
- **Structure**: List requirements, heading depth
- **Result**: Sophisticated content validation

### 5. CI/CD Integration
- **Batch Processing**: Multiple files validation
- **Report Generation**: HTML and Markdown reports
- **Error Handling**: Detailed error categorization
- **Result**: Production-ready validation pipeline

## 🎯 Use Cases

### Development Teams
- **Code Review**: Validate documentation and comments
- **Content Creation**: Ensure consistent writing style
- **API Documentation**: Validate OpenAPI descriptions

### Marketing Teams
- **Copy Validation**: Ensure brand guidelines
- **SEO Requirements**: Check keyword inclusion
- **Legal Compliance**: Verify required disclaimers

### Technical Teams
- **Specification Validation**: Check technical accuracy
- **Performance Requirements**: Validate metrics
- **Security Guidelines**: Ensure secure content

## 📁 Shared Resources

### schemas/
Contains shared schema files used across examples:
- `user_profile.yaml` - User profile validation schema
- `product_description.yaml` - Product description schema
- `blog_post.yaml` - Blog post validation schema

### rule_bundles/
Contains shared rule bundles:
- `common_rules.yaml` - Common validation rules
- `ecommerce_rules.yaml` - E-commerce specific rules

## 🔧 Troubleshooting

### Common Issues

1. **Missing Rule Bundles**
   ```bash
   # Copy rule bundles to example directories
   cp rule_bundles/*.yaml 02_rule_bundles/rule_bundles/
   ```

2. **Import Errors**
   ```bash
   # Ensure you're in the correct directory
   cd llm-contracts
   pip install -e .
   ```

3. **Schema Not Found**
   ```bash
   # Check file paths are correct
   ls -la examples/schemas/
   ```

### Debug Mode

Enable debug logging for detailed error information:

```python
import logging
logging.basicConfig(level=logging.DEBUG)

from llm_contracts import contracts
result = contracts.validate(data, 'schema.yaml')
```

## 📚 Next Steps

After running the examples:

1. **Explore the generated reports** in each example directory
2. **Modify the schemas** to test different validation rules
3. **Create your own rule bundles** for your specific use cases
4. **Integrate into your CI/CD pipeline** using the CLI examples
5. **Extend with custom validators** for business-specific logic

## 🤝 Contributing

Found an issue with the examples? Want to add a new example?

1. Check the [main contributing guide](../CONTRIBUTING.md)
2. Test your changes with the existing examples
3. Update this README if adding new examples
4. Submit a pull request with your improvements 