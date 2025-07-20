# Basic Validation Example

This example demonstrates the core validation functionality of llm-contracts using the `contracts.validate()` API.

## 📋 Overview

The basic validation example shows:
- ✅ **Schema validation** - JSON structure validation
- ✅ **Text linting** - Content quality rules
- ✅ **Report generation** - HTML and Markdown reports
- ✅ **Error handling** - Detailed error messages

## 🚀 Quick Start

```bash
# Run the example
python basic_validation.py
```

## 📁 Files

- `basic_validation.py` - Main example script
- `user_profile.yaml` - User profile validation schema
- `product_description.yaml` - Product description validation schema
- `validation_report.html` - Generated HTML report
- `validation_report.md` - Generated Markdown report

## 🔍 Example Details

### User Profile Validation

**Schema** (`user_profile.yaml`):
```yaml
schema:
  name:
    type: str
    pattern: "^[A-Z][a-z]+ [A-Z][a-z]+$"
    required: true
  age:
    type: int
    min: 18
    max: 65
    required: true
  email:
    type: str
    pattern: "^[^@]+@[^@]+\\.[^@]+$"
    required: true
  bio:
    type: str
    min_length: 10
    max_length: 500

rules:
  - keyword_must_include: "professional"
  - no_placeholder_text: "\\[YOUR_BIO\\]"
  - word_count_min: 5
```

**Test Data**:
```python
user_data = {
    "name": "John Doe",
    "age": 25,
    "email": "john.doe@example.com",
    "bio": "Software engineer with 5 years of experience in Python and web development."
}
```

**Expected Result**: ❌ FAIL (missing "professional" keyword)

### Product Description Validation

**Schema** (`product_description.yaml`):
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

**Test Data**:
```python
product_data = {
    "title": "Premium Wireless Headphones",
    "description": "Experience superior sound quality with our premium wireless headphones. Built with durable materials and advanced audio technology, these headphones deliver crystal-clear sound. Features include noise cancellation, 30-hour battery life, and premium comfort. Our 30-day warranty and hassle-free return policy ensure your satisfaction. Buy now with free shipping!",
    "price": 199.99,
    "features": [
        "Noise cancellation technology",
        "30-hour battery life",
        "Premium comfort design",
        "Bluetooth 5.0 connectivity"
    ]
}
```

**Expected Result**: ✅ PASS

## 🧪 Running the Example

### Step 1: User Profile Validation

```python
from llm_contracts import contracts

# Load test data
user_data = {
    "name": "John Doe",
    "age": 25,
    "email": "john.doe@example.com",
    "bio": "Software engineer with 5 years of experience in Python and web development."
}

# Validate user profile
result = contracts.validate(user_data, 'user_profile.yaml')

print(f"Valid: {result.is_valid}")
if not result.is_valid:
    print("Errors:")
    for error in result.errors:
        print(f"  - {error}")
```

**Output**:
```
🔍 Basic Validation Example
==================================================
📋 Validating user profile...
Data: {
  "name": "John Doe",
  "age": 25,
  "email": "john.doe@example.com",
  "bio": "Software engineer with 5 years of experience in Python and web development."
}
Schema: /path/to/user_profile.yaml

❌ Validation FAILED!
Errors found:
  - Must include keyword: 'professional'
```

### Step 2: Product Description with Reports

```python
# Validate product description and generate reports
result = contracts.validate_and_report(
    product_data, 
    'product_description.yaml', 
    'validation_report.html', 
    'html'
)

print(f"Validation completed!")
print(f"Results: {'PASS' if result.is_valid else 'FAIL'}")
print(f"Reports generated:")
print(f"  - HTML: validation_report.html")
print(f"  - Markdown: validation_report.md")
```

**Output**:
```
📄 Validation with Report Generation
==================================================
📋 Validating product description...
Schema: /path/to/product_description.yaml

✅ Validation completed!
📊 Results: PASS
📄 Reports generated:
  - HTML: validation_report.html
  - Markdown: validation_report.md
```

## 📊 Generated Reports

### HTML Report
The HTML report includes:
- ✅/❌ Validation status
- 📋 Detailed error messages
- 📄 Schema reference
- 🎨 Responsive design
- 📊 Error categorization

### Markdown Report
The Markdown report includes:
- 📋 Validation summary
- ❌ Error details
- 📄 Schema information
- 📊 Statistics

## 🔧 Customization

### Adding Custom Rules

```yaml
# Add to your schema
rules:
  - keyword_must_include: ["your", "custom", "keywords"]
  - word_count_min: 50
  - max_passive_voice_ratio: 0.3
```

### Custom Validation Logic

```python
def custom_validator(content, schema):
    # Your custom validation logic
    if "spam" in content.lower():
        return False, ["Content contains spam"]
    return True, []

# Use custom validator
result = contracts.validate(data, 'schema.yaml', custom_validator=custom_validator)
```

## 🎯 Key Learning Points

1. **Schema Validation**: JSON structure validation with type checking
2. **Text Linting**: Content quality rules for better output
3. **Error Handling**: Clear error messages for debugging
4. **Report Generation**: Professional reports for stakeholders
5. **API Usage**: Simple and intuitive contracts API

## 🔗 Related Examples

- [Rule Bundles](../02_rule_bundles/) - Reusable rule sets
- [Advanced Rules](../03_advanced_rules/) - Advanced validation rules
- [Markdown Reports](../04_markdown_reports/) - CI/CD report generation
- [CLI Usage](../05_cli_usage/) - Command-line interface

## 🤝 Next Steps

1. **Modify the schemas** to test different validation rules
2. **Add custom rules** for your specific use cases
3. **Explore the generated reports** to understand the format
4. **Try the other examples** to learn more features 