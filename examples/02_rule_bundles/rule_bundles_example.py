#!/usr/bin/env python3
"""
Rule Bundles Example

Demonstrates how to create and use reusable rule bundles for teams.
"""

import json
from pathlib import Path

from llm_contracts import contracts


def rule_bundles_example():
    """Demonstrate rule bundles functionality."""
    
    print("📦 Rule Bundles Example")
    print("=" * 50)
    
    # Sample product data
    product_data = {
        "product_id": "PROD-87654321",
        "title": "Premium Coffee Maker",
        "description": "Experience the perfect cup of coffee with our premium coffee maker. Built with durable stainless steel and advanced brewing technology, this coffee maker delivers rich, flavorful coffee every time. Features include programmable brewing, 12-cup capacity, and auto-shutoff. Our 30-day warranty and hassle-free return policy ensure your satisfaction. Buy now with free shipping!",
        "price": 299.99,
        "category": "home",
        "features": [
            "Programmable brewing",
            "12-cup capacity",
            "Auto-shutoff feature",
            "Stainless steel construction"
        ]
    }
    
    # Schema that uses rule bundles
    schema_path = Path(__file__).parent / "product_with_bundles.yaml"
    
    print(f"📋 Validating product with rule bundles...")
    print(f"Schema: {schema_path}")
    print(f"Schema includes:")
    print(f"  - common_rules.yaml (basic quality rules)")
    print(f"  - ecommerce_rules.yaml (e-commerce specific rules)")
    print()
    
    # Validate using rule bundles
    result = contracts.validate(product_data, schema_path)
    
    if result.is_valid:
        print("✅ Validation PASSED!")
        print("All bundled rules and schema requirements passed.")
    else:
        print("❌ Validation FAILED!")
        print("Errors found:")
        for error in result.errors:
            print(f"  - {error}")
    
    print()
    return result


def create_team_rules():
    """Demonstrate creating team-specific rule bundles."""
    
    print("👥 Team Rules Example")
    print("=" * 50)
    
    # Create a marketing team rule bundle
    marketing_rules = {
        "rules": [
            {"keyword_must_include": ["call to action", "limited time", "exclusive"]},
            {"keyword_must_not_include": ["technical jargon", "complex terms"]},
            {"word_count_min": 50},
            {"word_count_max": 300},
            {"max_passive_voice_ratio": 0.1},
            {"phrase_order": {"first": "benefits", "then": "call to action"}}
        ]
    }
    
    # Create a technical team rule bundle
    technical_rules = {
        "rules": [
            {"keyword_must_include": ["specifications", "technical", "performance"]},
            {"keyword_must_not_include": ["marketing buzzwords", "hype"]},
            {"word_count_min": 100},
            {"word_count_max": 1000},
            {"min_list_items": 3},
            {"regex_must_match": "\\b\\d+\\s*(?:GB|MB|GHz|W)\\b"}
        ]
    }
    
    # Write team rule bundles
    marketing_path = Path(__file__).parent / "team_rules" / "marketing_rules.yaml"
    technical_path = Path(__file__).parent / "team_rules" / "technical_rules.yaml"
    
    marketing_path.parent.mkdir(exist_ok=True)
    
    import yaml
    with open(marketing_path, 'w') as f:
        yaml.dump(marketing_rules, f)
    
    with open(technical_path, 'w') as f:
        yaml.dump(technical_rules, f)
    
    print(f"✅ Created team rule bundles:")
    print(f"  - Marketing: {marketing_path}")
    print(f"  - Technical: {technical_path}")
    
    # Test marketing content
    marketing_content = {
        "title": "Amazing Product Launch",
        "description": "Discover the incredible benefits of our revolutionary product. Limited time offer - exclusive access for early adopters. Don't miss out on this amazing opportunity! Call to action: Buy now and save 50%!"
    }
    
    # Test technical content
    technical_content = {
        "title": "Product Specifications",
        "description": "Technical specifications include 8GB RAM, 256GB SSD storage, 2.4GHz processor, and 45W power consumption. Performance metrics show 99.9% uptime and sub-100ms response times. Additional features include advanced cooling system and modular design."
    }
    
    # Create schemas that use team rules
    marketing_schema = {
        "schema": {"type": "object"},
        "rules": [
            {"include": "team_rules/marketing_rules.yaml"}
        ]
    }
    
    technical_schema = {
        "schema": {"type": "object"},
        "rules": [
            {"include": "team_rules/technical_rules.yaml"}
        ]
    }
    
    # Test marketing content
    marketing_schema_path = Path(__file__).parent / "marketing_schema.yaml"
    with open(marketing_schema_path, 'w') as f:
        yaml.dump(marketing_schema, f)
    
    print(f"\n📋 Testing marketing content...")
    marketing_result = contracts.validate(marketing_content, marketing_schema_path)
    print(f"Marketing validation: {'✅ PASS' if marketing_result.is_valid else '❌ FAIL'}")
    
    # Test technical content
    technical_schema_path = Path(__file__).parent / "technical_schema.yaml"
    with open(technical_schema_path, 'w') as f:
        yaml.dump(technical_schema, f)
    
    print(f"📋 Testing technical content...")
    technical_result = contracts.validate(technical_content, technical_schema_path)
    print(f"Technical validation: {'✅ PASS' if technical_result.is_valid else '❌ FAIL'}")
    
    return marketing_result, technical_result


if __name__ == "__main__":
    # Run rule bundles example
    bundles_result = rule_bundles_example()
    
    print("\n" + "="*60 + "\n")
    
    # Run team rules example
    marketing_result, technical_result = create_team_rules() 