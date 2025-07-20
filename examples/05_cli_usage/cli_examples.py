#!/usr/bin/env python3
"""
CLI Usage Examples

Demonstrates all CLI features and options.
"""

import json
import subprocess
import tempfile
import yaml
from pathlib import Path

from llm_contracts import contracts


def cli_basic_validation():
    """Demonstrate basic CLI validation."""
    
    print("🔧 CLI Basic Validation")
    print("=" * 40)
    
    # Create sample data
    data = {
        "name": "Jane Smith",
        "age": 30,
        "email": "jane.smith@example.com",
        "bio": "Experienced software engineer with expertise in Python and web development."
    }
    
    # Create schema
    schema = {
        "schema": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "pattern": "^[A-Z][a-z]+ [A-Z][a-z]+$"},
                "age": {"type": "integer", "minimum": 18, "maximum": 65},
                "email": {"type": "string", "pattern": "^[^@]+@[^@]+\\.[^@]+$"},
                "bio": {"type": "string", "minLength": 10}
            },
            "required": ["name", "age", "email"]
        },
        "rules": [
            {"keyword_must_include": "professional"},
            {"word_count_min": 5}
        ]
    }
    
    # Write files
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump(data, f, indent=2)
        data_file = f.name
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        yaml.dump(schema, f)
        schema_file = f.name
    
    try:
        print(f"📄 Data file: {data_file}")
        print(f"📋 Schema file: {schema_file}")
        print()
        
        # Run CLI validation
        result = subprocess.run([
            "llm-validate", data_file, "--schema", schema_file
        ], capture_output=True, text=True)
        
        print("CLI Output:")
        print(result.stdout)
        
        if result.stderr:
            print("CLI Errors:")
            print(result.stderr)
        
        print(f"Exit code: {result.returncode}")
        
        return result.returncode == 0
        
    finally:
        import os
        os.unlink(data_file)
        os.unlink(schema_file)


def cli_with_reports():
    """Demonstrate CLI with report generation."""
    
    print("\n📄 CLI with Report Generation")
    print("=" * 40)
    
    # Create sample data
    data = {
        "title": "Premium Product Launch",
        "content": "Experience superior quality with our premium product. Built with durable materials and advanced technology. Features include innovative design, long-lasting performance, and premium comfort. Our 30-day warranty and hassle-free return policy ensure your satisfaction. Buy now with free shipping!"
    }
    
    # Create schema
    schema = {
        "schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string", "minLength": 10},
                "content": {"type": "string", "minLength": 100}
            },
            "required": ["title", "content"]
        },
        "rules": [
            {"keyword_must_include": ["quality", "premium"]},
            {"keyword_must_not_include": ["cheap", "low quality"]},
            {"word_count_min": 50},
            {"keyword_must_include": "warranty"},
            {"phrase_proximity": {"terms": ["warranty", "30"], "max_distance": 20}}
        ]
    }
    
    # Write files
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump(data, f, indent=2)
        data_file = f.name
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        yaml.dump(schema, f)
        schema_file = f.name
    
    try:
        print(f"📄 Data file: {data_file}")
        print(f"📋 Schema file: {schema_file}")
        print()
        
        # Run CLI with HTML report
        print("Generating HTML report...")
        result = subprocess.run([
            "llm-validate", data_file, "--schema", schema_file, "--html-report", "cli_report.html"
        ], capture_output=True, text=True)
        
        print("CLI Output:")
        print(result.stdout)
        print(f"Exit code: {result.returncode}")
        
        # Run CLI with Markdown report
        print("\nGenerating Markdown report...")
        result = subprocess.run([
            "llm-validate", data_file, "--schema", schema_file, "--md-report", "cli_report.md"
        ], capture_output=True, text=True)
        
        print("CLI Output:")
        print(result.stdout)
        print(f"Exit code: {result.returncode}")
        
        # Run CLI with both reports
        print("\nGenerating both reports...")
        result = subprocess.run([
            "llm-validate", data_file, "--schema", schema_file, 
            "--html-report", "cli_report_both.html", "--md-report", "cli_report_both.md"
        ], capture_output=True, text=True)
        
        print("CLI Output:")
        print(result.stdout)
        print(f"Exit code: {result.returncode}")
        
        return result.returncode == 0
        
    finally:
        import os
        os.unlink(data_file)
        os.unlink(schema_file)


def cli_strict_mode():
    """Demonstrate CLI strict mode."""
    
    print("\n🚨 CLI Strict Mode")
    print("=" * 40)
    
    # Create invalid data
    data = {
        "name": "john",  # Invalid format
        "age": "25",     # Wrong type
        "email": "invalid-email"  # Invalid email
    }
    
    # Create schema
    schema = {
        "schema": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "pattern": "^[A-Z][a-z]+ [A-Z][a-z]+$"},
                "age": {"type": "integer", "minimum": 18, "maximum": 65},
                "email": {"type": "string", "pattern": "^[^@]+@[^@]+\\.[^@]+$"}
            },
            "required": ["name", "age", "email"]
        }
    }
    
    # Write files
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump(data, f, indent=2)
        data_file = f.name
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        yaml.dump(schema, f)
        schema_file = f.name
    
    try:
        print(f"📄 Invalid data file: {data_file}")
        print(f"📋 Schema file: {schema_file}")
        print()
        
        # Run CLI without strict mode (should not exit with error)
        print("Running without --strict (should not exit with error)...")
        result = subprocess.run([
            "llm-validate", data_file, "--schema", schema_file
        ], capture_output=True, text=True)
        
        print(f"Exit code: {result.returncode}")
        print("Output:")
        print(result.stdout)
        
        # Run CLI with strict mode (should exit with error)
        print("\nRunning with --strict (should exit with error)...")
        result = subprocess.run([
            "llm-validate", data_file, "--schema", schema_file, "--strict"
        ], capture_output=True, text=True)
        
        print(f"Exit code: {result.returncode}")
        print("Output:")
        print(result.stdout)
        
        return result.returncode != 0  # Should fail in strict mode
        
    finally:
        import os
        os.unlink(data_file)
        os.unlink(schema_file)


def cli_json_output():
    """Demonstrate CLI JSON output format."""
    
    print("\n📊 CLI JSON Output")
    print("=" * 40)
    
    # Create sample data
    data = {
        "name": "Alice Johnson",
        "age": 28,
        "email": "alice.johnson@example.com"
    }
    
    # Create schema
    schema = {
        "schema": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "pattern": "^[A-Z][a-z]+ [A-Z][a-z]+$"},
                "age": {"type": "integer", "minimum": 18, "maximum": 65},
                "email": {"type": "string", "pattern": "^[^@]+@[^@]+\\.[^@]+$"}
            },
            "required": ["name", "age", "email"]
        }
    }
    
    # Write files
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump(data, f, indent=2)
        data_file = f.name
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        yaml.dump(schema, f)
        schema_file = f.name
    
    try:
        print(f"📄 Data file: {data_file}")
        print(f"📋 Schema file: {schema_file}")
        print()
        
        # Run CLI with JSON output
        print("Running with JSON output format...")
        result = subprocess.run([
            "llm-validate", data_file, "--schema", schema_file, "--output-format", "json"
        ], capture_output=True, text=True)
        
        print("CLI Output:")
        print(result.stdout)
        print(f"Exit code: {result.returncode}")
        
        return result.returncode == 0
        
    finally:
        import os
        os.unlink(data_file)
        os.unlink(schema_file)


if __name__ == "__main__":
    print("🔧 CLI Usage Examples")
    print("=" * 60)
    print()
    
    # Run all CLI examples
    basic_success = cli_basic_validation()
    reports_success = cli_with_reports()
    strict_success = cli_strict_mode()
    json_success = cli_json_output()
    
    print("\n" + "=" * 60)
    print("📊 CLI Examples Summary:")
    print(f"✅ Basic validation: {'PASS' if basic_success else 'FAIL'}")
    print(f"✅ Report generation: {'PASS' if reports_success else 'FAIL'}")
    print(f"✅ Strict mode: {'PASS' if strict_success else 'FAIL'}")
    print(f"✅ JSON output: {'PASS' if json_success else 'FAIL'}") 