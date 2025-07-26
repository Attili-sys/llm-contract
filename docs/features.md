---
layout: default
title: Core Features
nav_order: 3
description: "Complete validation toolkit for LLM outputs - schema validation, content linting, and professional reporting"
---

# Core Features

{: .fs-6 .fw-300 }
Complete validation toolkit for LLM outputs

llm-contracts provides everything you need to validate AI-generated content with confidence:

---

## 🔍 Schema-Based Validation

Define the exact structure your application expects:

```yaml
schema:
  type: object
  properties:
    title:
      type: string
      minLength: 10
      maxLength: 100
    price:
      type: number
      minimum: 0
    tags:
      type: array
      minItems: 1
      maxItems: 5
      items:
        type: string
  required: ["title", "price"]
```

**Catches:**
- Missing required fields
- Wrong data types
- Invalid value ranges
- Malformed JSON/YAML

---

## 📝 Content Linting Rules

Ensure content quality and compliance:

```yaml
rules:
  # Content requirements
  - keyword_must_include: ["warranty", "return policy"]
  - keyword_must_not_include: ["guarantee", "unlimited"]
  
  # Quality checks
  - no_placeholder_text: "\\[YOUR_TEXT_HERE\\]"
  - word_count_min: 50
  - word_count_max: 500
  - no_duplicate_sentences: true
  
  # Advanced validation
  - phrase_proximity:
      terms: ["30-day", "warranty"]
      max_distance: 10
  - regex_must_match: "\\$\\d+\\.\\d{2}"
```

**Catches:**
- Missing keywords
- Placeholder text
- Poor quality content
- Brand compliance issues
- Legal/regulatory violations

---

## 📊 Professional Reports

Generate detailed validation reports for stakeholders:

### HTML Reports
Beautiful, responsive reports with:
- ✅ Visual error highlighting
- 📈 Success rate metrics
- 🔍 Detailed error categorization
- 📱 Mobile-friendly design

### Markdown Reports
Perfect for CI/CD and documentation:
- ✅ Version control friendly
- 📝 Integration with pull requests
- 🤖 Automated compliance checking
- 📋 Audit trail documentation

```bash
# Generate both formats
llm-validate output.json --schema schema.yaml \
  --html-report validation.html \
  --md-report validation.md
```

---

## 🔧 Flexible Integration

### CLI Interface
```bash
# Basic validation
llm-validate content.json --schema rules.yaml

# With reporting
llm-validate content.json --schema rules.yaml --html-report report.html

# Strict mode (exit code 1 on failure)
llm-validate content.json --schema rules.yaml --strict
```

### Python API
```python
from llm_contracts import contracts

# Simple validation
result = contracts.validate(content, "schema.yaml")

# With custom error handling
try:
    result = contracts.validate(content, "schema.yaml") 
    if not result.is_valid:
        handle_validation_errors(result.errors)
except ValidationError as e:
    handle_critical_error(e)
```

### Web Interface
Interactive schema builder and testing interface:
- 🎨 Visual schema builder
- 🧪 Live validation testing
- 📚 Template library
- 🤖 AI integration for content generation

---

## 🚀 Advanced Features

### Rule Bundles
Create reusable validation rule sets:

```yaml
# common_rules.yaml
rules:
  - keyword_must_not_include: ["as an AI", "I cannot"]
  - no_placeholder_text: "\\[.*\\]"
  - word_count_min: 25

# product_rules.yaml  
rules:
  - include: "common_rules.yaml"  # Import shared rules
  - keyword_must_include: ["warranty", "specifications"]
  - price_format_valid: true
```

### Custom Validators
Extend with your own validation logic:

```python
from llm_contracts.custom_validators import BaseValidator

class BrandComplianceValidator(BaseValidator):
    def validate(self, content):
        # Your custom validation logic
        if "competitor_name" in content.lower():
            return False, "Competitor mention detected"
        return True, None

# Use in schema
validators:
  - BrandComplianceValidator
```

### Integration Patterns

#### CI/CD Pipeline
```yaml
# GitHub Actions
- name: Validate AI Content
  run: |
    llm-validate generated_content/ --schema content_rules.yaml --strict
```

#### Application Integration
```python
@app.route('/generate-content')
def generate_content():
    ai_output = llm.generate(prompt)
    
    # Validate before serving
    result = contracts.validate(ai_output, "content_schema.yaml")
    if not result.is_valid:
        return {"error": "Content validation failed", "issues": result.errors}
    
    return {"content": ai_output}
```

---

## 🎯 Why It Works

### Framework Agnostic
- ✅ Works with **any LLM** (OpenAI, Anthropic, local models)
- ✅ Compatible with **any framework** (LangChain, direct APIs)
- ✅ No vendor lock-in or API dependencies

### Production Ready
- ✅ Comprehensive error handling
- ✅ Performance optimized
- ✅ Extensive test coverage (84%)
- ✅ CI/CD integration support

### Developer Friendly
- ✅ Clear error messages
- ✅ Extensive documentation
- ✅ Rich examples library
- ✅ Active community support

---

[Get Started →](getting-started){: .btn .btn-primary }
[View Examples →](examples){: .btn .btn-outline } 