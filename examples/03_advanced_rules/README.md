# Advanced Rules Example

This example demonstrates all the advanced validation rules available in llm-contracts.

## 📋 Overview

The advanced rules example shows:
- ✅ **Regex pattern matching** - Complex pattern validation
- ✅ **Duplicate detection** - Content quality analysis
- ✅ **List validation** - Structure requirements
- ✅ **Writing style analysis** - Passive voice detection
- ✅ **Combined rules** - Multiple rule types together

## 🚀 Quick Start

```bash
# Run the example
python advanced_rules_example.py
```

## 📁 Files

- `advanced_rules_example.py` - Main example script

## 🔍 Advanced Rules

### 1. Regex Pattern Matching

**Rule**: `regex_must_match`
**Purpose**: Validate content against complex regex patterns

```yaml
rules:
  - regex_must_match: "\\b\\d{1,3}(?:\\.\\d{2})?\\s*USD\\b"
```

**Valid Content**:
```
This product costs 29.99 USD and is available now.
```

**Invalid Content**:
```
This product costs $30 and is available now.
```

### 2. Duplicate Sentence Detection

**Rule**: `no_duplicate_sentences`
**Purpose**: Detect and prevent duplicate sentences

```yaml
rules:
  - no_duplicate_sentences: true
```

**Valid Content**:
```
This is the first sentence. This is the second sentence. This is the third sentence.
```

**Invalid Content**:
```
This is the first sentence. This is the first sentence. This is the second sentence.
```

### 3. List Item Validation

**Rule**: `min_list_items`
**Purpose**: Ensure minimum number of list items

```yaml
rules:
  - min_list_items: 3
```

**Valid Content**:
```
Features:
1. High quality
2. Durable design
3. Long warranty
```

**Invalid Content**:
```
Features:
1. High quality
2. Durable design
```

### 4. Passive Voice Detection

**Rule**: `max_passive_voice_ratio`
**Purpose**: Limit passive voice usage

```yaml
rules:
  - max_passive_voice_ratio: 0.2
```

**Valid Content**:
```
The team developed the product. The engineers built the system. The designers created the interface.
```

**Invalid Content**:
```
The product was developed by the team. The system was built by engineers. The interface was created by designers.
```

## 🧪 Running the Example

### Individual Rule Testing

```python
from llm_contracts import contracts

# Test regex pattern matching
valid_text = "This product costs 29.99 USD and is available now."
invalid_text = "This product costs $30 and is available now."

result = contracts.lint(valid_text, 'regex_schema.yaml')
print(f"✅ Valid text: {'PASS' if result.is_valid else 'FAIL'}")

result = contracts.lint(invalid_text, 'regex_schema.yaml')
print(f"❌ Invalid text: {'PASS' if result.is_valid else 'FAIL'}")
if not result.is_valid:
    for error in result.errors:
        print(f"   Error: {error}")
```

**Output**:
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

### Combined Rules Testing

```python
# Test multiple advanced rules together
combined_schema = {
    "rules": [
        {"keyword_must_include": "quality"},
        {"word_count_min": 50},
        {"regex_must_match": "\\b\\d{1,3}(?:\\.\\d{2})?\\s*USD\\b"},
        {"min_list_items": 2},
        {"max_passive_voice_ratio": 0.3}
    ]
}

# Test valid content
valid_content = """# Product Description

This is a high quality product that costs 29.99 USD. 
It features excellent durability and comes with a comprehensive warranty.

Features:
1. Premium quality materials
2. Extended warranty coverage
3. Professional support

The product is designed for maximum performance."""
```

## 📊 Rule Examples

### Price Format Validation

```yaml
# price_schema.yaml
rules:
  - regex_must_match: "\\b\\d{1,3}(?:\\.\\d{2})?\\s*USD\\b"
```

**Pattern Explanation**:
- `\\b` - Word boundary
- `\\d{1,3}` - 1-3 digits
- `(?:\\.\\d{2})?` - Optional decimal with 2 digits
- `\\s*USD\\b` - Optional spaces followed by USD

### Email Validation

```yaml
# email_schema.yaml
rules:
  - regex_must_match: "^[^@]+@[^@]+\\.[^@]+$"
```

### Phone Number Validation

```yaml
# phone_schema.yaml
rules:
  - regex_must_match: "\\b\\d{3}-\\d{3}-\\d{4}\\b"
```

### Content Quality Rules

```yaml
# quality_schema.yaml
rules:
  - no_duplicate_sentences: true
  - max_passive_voice_ratio: 0.2
  - min_list_items: 3
  - word_count_min: 100
  - word_count_max: 1000
```

## 🔧 Custom Advanced Rules

### Custom Regex Patterns

```yaml
# Custom patterns for your domain
rules:
  - regex_must_match: "\\b[A-Z]{2}\\d{6}\\b"  # Product codes
  - regex_must_match: "\\b\\d{4}-\\d{2}-\\d{2}\\b"  # Date format
  - regex_must_match: "\\b[A-Z][a-z]+\\s+[A-Z][a-z]+\\b"  # Name format
```

### Content Structure Rules

```yaml
# Structured content requirements
rules:
  - section_must_start_with: "^# Introduction"
  - heading_max_depth: 3
  - list_item_pattern: "^\\d+\\. [A-Z].*"
  - min_list_items: 2
  - max_passive_voice_ratio: 0.3
```

## 🎯 Use Cases

### Technical Documentation

```yaml
# technical_docs.yaml
rules:
  - keyword_must_include: ["specifications", "requirements"]
  - regex_must_match: "\\b\\d+\\s*(?:GB|MB|TB)\\b"
  - min_list_items: 3
  - max_passive_voice_ratio: 0.1
```

### Marketing Content

```yaml
# marketing_content.yaml
rules:
  - keyword_must_include: ["call to action", "limited time"]
  - regex_must_match: "\\b\\d{1,3}(?:\\.\\d{2})?\\s*USD\\b"
  - word_count_min: 100
  - word_count_max: 500
  - max_passive_voice_ratio: 0.2
```

### Legal Documents

```yaml
# legal_docs.yaml
rules:
  - keyword_must_include: ["terms", "conditions", "liability"]
  - no_duplicate_sentences: true
  - section_must_start_with: "^# Legal Terms"
  - heading_max_depth: 2
```

## 🔗 Related Examples

- [Basic Validation](../01_basic_validation/) - Core validation functionality
- [Rule Bundles](../02_rule_bundles/) - Reusable rule sets
- [Markdown Reports](../04_markdown_reports/) - CI/CD report generation
- [CLI Usage](../05_cli_usage/) - Command-line interface

## 🤝 Next Steps

1. **Experiment with regex patterns** for your specific needs
2. **Create custom rule combinations** for your content types
3. **Test with real content** to fine-tune rules
4. **Integrate into your workflow** using the CLI examples
5. **Share rule bundles** with your team 