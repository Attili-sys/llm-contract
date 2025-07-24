#!/usr/bin/env python3
"""
Flask server for LLM Contracts Validator Frontend
Provides API endpoints to validate LLM outputs using the actual llm-contracts library
"""

import os
import json
import tempfile
import sys
from pathlib import Path
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import yaml

# Add the parent directory to sys.path to import llm_contracts
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Import llm-contracts library
from llm_contracts import contracts
from llm_contracts.core.validator import ValidationError

app = Flask(__name__, static_folder='.')
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    """Serve the index.html file"""
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    """Serve static files"""
    return send_from_directory('.', path)

@app.route('/api/validate', methods=['POST'])
def validate():
    """
    Validate LLM output against a schema
    
    Expects:
    - output: LLM output (string or JSON)
    - schema: Schema in YAML format
    
    Returns:
    - is_valid: Whether validation passed
    - errors: List of validation errors
    """
    try:
        data = request.json
        output = data.get('output')
        schema_yaml = data.get('schema')
        
        if not output or not schema_yaml:
            return jsonify({
                'success': False,
                'message': 'Missing output or schema'
            }), 400
        
        # Parse output as JSON if possible
        try:
            output_data = json.loads(output)
        except (json.JSONDecodeError, TypeError):
            output_data = output
        
        # Write schema to temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as temp_schema:
            temp_schema.write(schema_yaml)
            schema_path = temp_schema.name
        
        try:
            # Validate using the actual llm-contracts library
            result = contracts.validate(output_data, schema_path)
            
            return jsonify({
                'success': True,
                'is_valid': result.is_valid,
                'errors': result.errors
            })
        finally:
            # Clean up temporary file
            os.unlink(schema_path)
            
    except ValidationError as e:
        return jsonify({
            'success': False,
            'message': str(e),
            'errors': e.errors if hasattr(e, 'errors') else []
        }), 400
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error: {str(e)}'
        }), 500

@app.route('/api/generate-report', methods=['POST'])
def generate_report():
    """
    Generate a validation report
    
    Expects:
    - output: LLM output (string or JSON)
    - schema: Schema in YAML format
    - format: Report format ('html' or 'markdown')
    
    Returns:
    - report: Generated report content
    """
    try:
        data = request.json
        output = data.get('output')
        schema_yaml = data.get('schema')
        report_format = data.get('format', 'html')
        
        if not output or not schema_yaml:
            return jsonify({
                'success': False,
                'message': 'Missing output or schema'
            }), 400
        
        # Parse output as JSON if possible
        try:
            output_data = json.loads(output)
        except (json.JSONDecodeError, TypeError):
            output_data = output
        
        # Write schema to temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as temp_schema:
            temp_schema.write(schema_yaml)
            schema_path = temp_schema.name
        
        # Create temporary file for report
        with tempfile.NamedTemporaryFile(mode='w', suffix=f'.{"html" if report_format == "html" else "md"}', delete=False) as temp_report:
            report_path = temp_report.name
        
        try:
            # Generate report using the actual llm-contracts library
            result = contracts.validate_and_report(
                output_data, 
                schema_path, 
                report_path, 
                report_format
            )
            
            # Read the generated report
            with open(report_path, 'r', encoding='utf-8') as f:
                report_content = f.read()
            
            return jsonify({
                'success': True,
                'is_valid': result.is_valid,
                'report': report_content
            })
        finally:
            # Clean up temporary files
            os.unlink(schema_path)
            os.unlink(report_path)
            
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error: {str(e)}'
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000) 