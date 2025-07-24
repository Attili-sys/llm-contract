# LLM Contracts Validator Frontend

A web-based frontend for testing and validating LLM outputs using the llm-contracts library.

## Features

- **API Key Management**: Securely store and test your Gemini API key
- **Schema Builder**: Create validation schemas using visual builder, AI generation, or YAML editor
- **Template Library**: Pre-built schemas for common use cases
- **LLM Integration**: Generate outputs using Gemini API
- **Validation**: Validate LLM outputs against your schemas using the actual llm-contracts library
- **Reports**: Generate HTML and Markdown validation reports

## Getting Started

### Prerequisites

- A modern web browser (Chrome, Firefox, Edge, Safari)
- Python 3.8+ with pip
- A Gemini API key (get one at https://makersuite.google.com/app/apikey)

### Setup

1. Install the backend dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the backend server:
   ```bash
   python server.py
   ```

3. Open `index.html` in your web browser

### Running the Frontend

1. Enter your Gemini API key and click "Test API Key"
2. Create or select a validation schema
3. Enter a prompt and click "Generate & Validate"
4. View validation results and download reports

## Usage Guide

### API Configuration

1. Enter your Gemini API key in the input field
2. Click "Test API Key" to verify it works
3. The key is stored in your browser's local storage for convenience

### Creating Schemas

#### Visual Builder

1. Click "Add Field" to add schema fields
2. Configure field properties (name, type, constraints)
3. Click "Add Rule" to add validation rules
4. Configure rule properties

#### AI Builder

1. Describe your validation requirements in natural language
2. Click "Generate Schema" to create a schema using AI
3. Review and adjust the generated schema as needed

#### YAML Editor

1. Write or paste YAML schema directly
2. Changes are automatically parsed and validated

#### Templates

1. Click on a template to load a pre-built schema
2. Customize the template as needed

### Validation

1. Enter a prompt in the "Prompt" field
2. Click "Generate & Validate" to generate LLM output and validate it
3. View validation results in the "Validation Results" section
4. Download HTML or Markdown reports for documentation

## Schema Format

```yaml
schema:
  # Field definitions with types and validation rules
  field_name:
    type: str|int|float|bool|list|dict
    # Other validation properties

rules:
  # Content validation rules
  - rule_type: rule_value
```

## Backend API

The frontend communicates with a Flask backend that uses the actual llm-contracts library for validation:

- `/api/validate` - Validates LLM output against a schema
- `/api/generate-report` - Generates HTML or Markdown validation reports

## Troubleshooting

- If you see CORS errors, make sure the backend server is running on port 5000
- If validation fails, check the error messages for details
- If the API key test fails, verify your Gemini API key is correct 