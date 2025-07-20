#!/usr/bin/env python3
"""
Basic Validation Example

Demonstrates the core validation functionality using the new branded API.
"""

import json
from pathlib import Path

from llm_contracts import contracts


def basic_validation_example():
    """Demonstrate basic validation with the new contracts API."""
    
    print("🔍 Basic Validation Example")
    print("=" * 50)
    
    # Sample data
    user_data = {
        "name": "John Doe",
        "age": 25,
        "email": "john.doe@example.com",
        "bio": "Software engineer with 5 years of experience in Python and web development."
    }
    
    # Schema path
    schema_path = Path(__file__).parent / "user_profile.yaml"
    
    print(f"📋 Validating user profile...")
    print(f"Data: {json.dumps(user_data, indent=2)}")
    print(f"Schema: {schema_path}")
    print()
    
    # Validate using new branded API
    result = contracts.validate(user_data, schema_path)
    
    if result.is_valid:
        print("✅ Validation PASSED!")
        print("All schema requirements and rules passed.")
    else:
        print("❌ Validation FAILED!")
        print("Errors found:")
        for error in result.errors:
            print(f"  - {error}")
    
    print()
    return result


def validation_with_report():
    """Demonstrate validation with report generation."""
    
    print("📄 Validation with Report Generation")
    print("=" * 50)
    
    # Sample data
    product_data = {
        "product_id": "PROD-12345678",
        "title": "Premium Wireless Headphones",
        "description": "Experience superior sound quality with our premium wireless headphones. Built with durable materials and advanced audio technology, these headphones deliver crystal-clear sound. Features include noise cancellation, 30-hour battery life, and premium comfort. Our 30-day warranty and hassle-free return policy ensure your satisfaction. Buy now with free shipping!",
        "price": 199.99,
        "category": "electronics",
        "features": [
            "Noise cancellation technology",
            "30-hour battery life",
            "Premium comfort design",
            "Bluetooth 5.0 connectivity"
        ]
    }
    
    schema_path = Path(__file__).parent / "product_description.yaml"
    
    print(f"📋 Validating product description...")
    print(f"Schema: {schema_path}")
    print()
    
    # Validate and generate both HTML and Markdown reports
    result = contracts.validate_and_report(
        product_data, 
        schema_path,
        report_path="validation_report.html",
        report_format="html"
    )
    
    # Generate Markdown report separately
    contracts.generate_report(
        result,
        "validation_report.md",
        str(schema_path),
        format="markdown"
    )
    
    print(f"✅ Validation completed!")
    print(f"📊 Results: {'PASS' if result.is_valid else 'FAIL'}")
    print(f"📄 Reports generated:")
    print(f"  - HTML: validation_report.html")
    print(f"  - Markdown: validation_report.md")
    
    return result


if __name__ == "__main__":
    # Run basic validation
    basic_result = basic_validation_example()
    
    print("\n" + "="*60 + "\n")
    
    # Run validation with reports
    report_result = validation_with_report() 