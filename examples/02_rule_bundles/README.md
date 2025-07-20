# Rule Bundles Example

This example demonstrates how to create and use reusable rule bundles for teams and organizations.

## 📋 Overview

The rule bundles example shows:
- ✅ **Rule bundle creation** - Reusable rule sets
- ✅ **Team-specific rules** - Different rules for different teams
- ✅ **Recursive includes** - Bundles can include other bundles
- ✅ **Relative path resolution** - Automatic path handling

## 🚀 Quick Start

```bash
# Run the example
python rule_bundles_example.py
```

## 📁 Files

- `rule_bundles_example.py` - Main example script
- `product_with_bundles.yaml` - Schema using rule bundles
- `rule_bundles/` - Rule bundle files
  - `common_rules.yaml` - Common validation rules
  - `ecommerce_rules.yaml` - E-commerce specific rules
- `team_rules/` - Team-specific rule bundles (generated)
  - `marketing_rules.yaml` - Marketing team rules
  - `technical_rules.yaml` - Technical team rules

## 🔍 Example Details

### Common Rules Bundle

**File**: `rule_bundles/common_rules.yaml`
```yaml
rules:
  - keyword_must_not_include: ["as an AI model", "I cannot", "I am an AI"]
  - no_placeholder_text: "\\[YOUR_TEXT_HERE\\]"
  - no_placeholder_text: "\\[DESCRIPTION\\]"
  - word_count_min: 50
  - max_passive_voice_ratio: 0.3
  - no_duplicate_sentences: true
```

### E-commerce Rules Bundle

**File**: `rule_bundles/ecommerce_rules.yaml`
```yaml
rules:
  - keyword_must_include: ["quality", "premium", "durable"]
  - keyword_must_not_include: ["cheap", "low quality", "defective"]
  - regex_must_match: "\\b\\d{1,3}(?:\\.\\d{2})?\\s*USD\\b"
  - min_list_items: 3
  - phrase_proximity:
      terms: ["warranty", "30"]
      max_distance: 20
```

### Product Schema with Bundles

**File**: `product_with_bundles.yaml`
```yaml
schema:
  title:
    type: str
    min_length: 10
    max_length: 100
    required: true
  description:
    type: str
    min_length: 100
    max_length: 1000
    required: true
  price:
    type: float
    min: 0.0
    required: true
  features:
    type: list
    min_items: 1
    items:
      type: str
      min_length: 5

rules:
  - include: "rule_bundles/common_rules.yaml"
  - include: "rule_bundles/ecommerce_rules.yaml"
  - section_must_start_with: "^# Product Description"
  - keyword_must_include: "warranty"
  - keyword_must_include: "return policy"
```

## 🧪 Running the Example

### Step 1: Product Validation with Bundles

```python
from llm_contracts import contracts

# Test data that will fail validation
product_data = {
    "title": "Basic Headphones",
    "description": "These headphones are cheap and low quality. They might be defective. [YOUR_TEXT_HERE]",
    "price": 19.99,
    "features": []
}

# Validate with rule bundles
result = contracts.validate(product_data, 'product_with_bundles.yaml')

print(f"Valid: {result.is_valid}")
if not result.is_valid:
    print("Errors:")
    for error in result.errors:
        print(f"  - {error}")
```

**Output**:
```
📦 Rule Bundles Example
==================================================
📋 Validating product with rule bundles...
Schema: /path/to/product_with_bundles.yaml
Schema includes:
  - common_rules.yaml (basic quality rules)
  - ecommerce_rules.yaml (e-commerce specific rules)

❌ Validation FAILED!
Errors found:
  - Must include keyword: 'quality'
  - Must have at least 3 list items, found 0
  - Content must match regex pattern: '\b\d{1,3}(?:\.\d{2})?\s*USD\b'
  - Content must start with pattern: '^# Product Description'
```

### Step 2: Team Rule Bundles

```python
# Create team-specific rule bundles
marketing_rules = {
    "rules": [
        {"keyword_must_include": ["call to action", "limited time"]},
        {"word_count_min": 100},
        {"word_count_max": 500},
        {"max_passive_voice_ratio": 0.2}
    ]
}

technical_rules = {
    "rules": [
        {"keyword_must_include": ["specifications", "performance"]},
        {"regex_must_match": "\\b\\d+\\s*(?:GB|MB|TB)\\b"},
        {"min_list_items": 2},
        {"section_must_start_with": "^# Technical Specifications"}
    ]
}

# Test marketing content
marketing_content = "This is a basic product description without call to action."
result = contracts.lint(marketing_content, 'marketing_rules.yaml')

print(f"Marketing validation: {'✅ PASS' if result.is_valid else '❌ FAIL'}")
```

## 📊 Rule Bundle Structure

### Bundle Hierarchy

```
rule_bundles/
├── common_rules.yaml          # Base rules for all content
├── ecommerce_rules.yaml       # E-commerce specific rules
└── team_rules/
    ├── marketing_rules.yaml   # Marketing team rules
    └── technical_rules.yaml   # Technical team rules
```

### Include Chain

```yaml
# product_schema.yaml
rules:
  - include: "rule_bundles/common_rules.yaml"      # Base rules
  - include: "rule_bundles/ecommerce_rules.yaml"   # E-commerce rules
  - keyword_must_include: "warranty"               # Product-specific rules
  - keyword_must_include: "return policy"          # Product-specific rules
```

## 🔧 Creating Your Own Bundles

### 1. Create Base Rules

```yaml
# base_rules.yaml
rules:
  - keyword_must_not_include: ["placeholder", "template"]
  - no_placeholder_text: "\\[YOUR_TEXT_HERE\\]"
  - word_count_min: 50
```

### 2. Create Team-Specific Rules

```yaml
# marketing_rules.yaml
rules:
  - include: "base_rules.yaml"
  - keyword_must_include: ["call to action", "limited time"]
  - word_count_max: 300
  - max_passive_voice_ratio: 0.2
```

### 3. Use in Schemas

```yaml
# content_schema.yaml
schema:
  title:
    type: str
    required: true
  content:
    type: str
    required: true

rules:
  - include: "marketing_rules.yaml"
  - keyword_must_include: "brand name"
```

## 🎯 Best Practices

### 1. Bundle Organization

- **Base rules**: Common rules for all content
- **Domain rules**: Industry-specific rules (e-commerce, healthcare, etc.)
- **Team rules**: Role-specific rules (marketing, technical, legal)
- **Project rules**: Project-specific rules

### 2. Rule Naming

```yaml
# Use descriptive names
rules:
  - keyword_must_include: ["quality", "premium"]  # Good
  - keyword_must_include: ["q", "p"]              # Avoid
```

### 3. Bundle Reusability

```yaml
# Create modular bundles
# common_rules.yaml - Base quality rules
# content_rules.yaml - Content-specific rules
# legal_rules.yaml - Legal compliance rules

# Combine in schemas
rules:
  - include: "common_rules.yaml"
  - include: "content_rules.yaml"
  - include: "legal_rules.yaml"
```

## 🔗 Related Examples

- [Basic Validation](../01_basic_validation/) - Core validation functionality
- [Advanced Rules](../03_advanced_rules/) - Advanced validation rules
- [Markdown Reports](../04_markdown_reports/) - CI/CD report generation
- [CLI Usage](../05_cli_usage/) - Command-line interface

## 🤝 Next Steps

1. **Create your own rule bundles** for your organization
2. **Organize rules by team** (marketing, technical, legal)
3. **Test bundle combinations** to ensure they work together
4. **Document your bundles** for team members
5. **Integrate into CI/CD** using the CLI examples 