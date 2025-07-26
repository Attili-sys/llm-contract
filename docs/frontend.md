---
layout: default
title: Web Frontend
nav_order: 5
description: "Interactive web interface for testing and building validation schemas"
---

# Web Frontend

[![PyPI version](https://img.shields.io/pypi/v/llm-contracts)](https://pypi.org/project/llm-contracts/)

llm-contracts includes a web-based frontend for testing and validating LLM outputs.

## Features

- **API Key Management**: Securely store and test your Gemini API key
- **Schema Builder**: Create validation schemas using visual builder, AI generation, or YAML editor
- **Template Library**: Pre-built schemas for common use cases
- **LLM Integration**: Generate outputs using Gemini API
- **Validation**: Validate LLM outputs against your schemas using the llm-contracts library
- **Reports**: Generate HTML and Markdown validation reports

## Getting Started

### Prerequisites

- A modern web browser (Chrome, Firefox, Edge, Safari)
- Python 3.8+ with pip
- A Gemini API key (get one at https://makersuite.google.com/app/apikey)

### Setup

1. Install the backend dependencies:
   ```bash
   cd frontend
   pip install -r requirements.txt
   ```

2. Run the backend server:
   ```bash
   python server.py
   ```

3. Open `index.html` in your web browser

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

## Screenshots

(Screenshots will be added here)

## Technical Details

The frontend consists of:
- HTML/CSS/JavaScript frontend
- Flask backend that interfaces with the llm-contracts library
- Gemini API integration for LLM generation 