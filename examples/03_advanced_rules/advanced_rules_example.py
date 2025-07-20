#!/usr/bin/env python3
"""
Advanced Rules Example

Demonstrates all the new advanced validation rules.
"""

import json
import tempfile
import yaml
from pathlib import Path

from llm_contracts import contracts


def test_regex_must_match():
    """Test regex pattern matching rule."""
    
    print("🔍 Testing regex_must_match Rule")
    print("=" * 40)
    
    schema = {
        "rules": [
            {"regex_must_match": r"\b\d{1,3}(?:\.\d{2})?\s*USD\b"}
        ]
    }
    
    valid_text = "This product costs 99.99 USD"
    invalid_text = "This product costs 99.99 dollars"
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        yaml.dump(schema, f)
        schema_path = f.name
    
    try:
        result = contracts.validate(valid_text, schema_path)
        print(f"✅ Valid text: {'PASS' if result.is_valid else 'FAIL'}")
        
        result = contracts.validate(invalid_text, schema_path)
        print(f"❌ Invalid text: {'PASS' if result.is_valid else 'FAIL'}")
        if not result.is_valid:
            print(f"   Error: {result.errors[0]}")
    finally:
        import os
        os.unlink(schema_path)
    
    print()


def test_no_duplicate_sentences():
    """Test duplicate sentence detection rule."""
    
    print("🔄 Testing no_duplicate_sentences Rule")
    print("=" * 40)
    
    schema = {
        "rules": [
            {"no_duplicate_sentences": True}
        ]
    }
    
    valid_text = "This is sentence one. This is sentence two. This is sentence three."
    invalid_text = "This is a sentence. This is a sentence. This is another sentence."
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        yaml.dump(schema, f)
        schema_path = f.name
    
    try:
        result = contracts.validate(valid_text, schema_path)
        print(f"✅ Valid text: {'PASS' if result.is_valid else 'FAIL'}")
        
        result = contracts.validate(invalid_text, schema_path)
        print(f"❌ Invalid text: {'PASS' if result.is_valid else 'FAIL'}")
        if not result.is_valid:
            print(f"   Error: {result.errors[0]}")
    finally:
        import os
        os.unlink(schema_path)
    
    print()


def test_min_list_items():
    """Test minimum list items rule."""
    
    print("📝 Testing min_list_items Rule")
    print("=" * 40)
    
    schema = {
        "rules": [
            {"min_list_items": 3}
        ]
    }
    
    valid_text = """
    Features:
    - Feature one
    - Feature two  
    - Feature three
    """
    invalid_text = """
    Features:
    - Feature one
    - Feature two
    """
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        yaml.dump(schema, f)
        schema_path = f.name
    
    try:
        result = contracts.validate(valid_text, schema_path)
        print(f"✅ Valid text: {'PASS' if result.is_valid else 'FAIL'}")
        
        result = contracts.validate(invalid_text, schema_path)
        print(f"❌ Invalid text: {'PASS' if result.is_valid else 'FAIL'}")
        if not result.is_valid:
            print(f"   Error: {result.errors[0]}")
    finally:
        import os
        os.unlink(schema_path)
    
    print()


def test_max_passive_voice_ratio():
    """Test passive voice ratio rule."""
    
    print("🎭 Testing max_passive_voice_ratio Rule")
    print("=" * 40)
    
    schema = {
        "rules": [
            {"max_passive_voice_ratio": 0.2}
        ]
    }
    
    valid_text = "The product is designed for users. It works efficiently. Users love it."
    invalid_text = "The product is designed for users. It is used by many people. It is loved by users."
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        yaml.dump(schema, f)
        schema_path = f.name
    
    try:
        result = contracts.validate(valid_text, schema_path)
        print(f"✅ Valid text: {'PASS' if result.is_valid else 'FAIL'}")
        
        result = contracts.validate(invalid_text, schema_path)
        print(f"❌ Invalid text: {'PASS' if result.is_valid else 'FAIL'}")
        if not result.is_valid:
            print(f"   Error: {result.errors[0]}")
    finally:
        import os
        os.unlink(schema_path)
    
    print()


def test_combined_advanced_rules():
    """Test combining multiple advanced rules."""
    
    print("🎯 Testing Combined Advanced Rules")
    print("=" * 40)
    
    # Create a comprehensive schema with multiple advanced rules
    schema = {
        "schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "content": {"type": "string"}
            }
        },
        "rules": [
            # Basic rules
            {"keyword_must_include": "quality"},
            {"word_count_min": 50},
            
            # Advanced rules
            {"regex_must_match": r"\b\d{1,3}(?:\.\d{2})?\s*USD\b"},
            {"no_duplicate_sentences": True},
            {"min_list_items": 2},
            {"max_passive_voice_ratio": 0.3}
        ]
    }
    
    # Valid content that passes all rules
    valid_content = {
        "title": "Premium Product",
        "content": """
        This is a quality product that costs 99.99 USD. 
        It features excellent performance and durability.
        
        Key features:
        - Advanced technology
        - Premium materials
        - Long warranty
        
        Users love this product for its reliability.
        """
    }
    
    # Invalid content that fails multiple rules
    invalid_content = {
        "title": "Cheap Product",
        "content": """
        This product is designed for users. It is used by many people. 
        It is loved by users. This product is designed for users.
        
        Features:
        - Basic functionality
        """
    }
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        yaml.dump(schema, f)
        schema_path = f.name
    
    try:
        print("Testing valid content...")
        result = contracts.validate(valid_content, schema_path)
        print(f"✅ Valid content: {'PASS' if result.is_valid else 'FAIL'}")
        
        print("\nTesting invalid content...")
        result = contracts.validate(invalid_content, schema_path)
        print(f"❌ Invalid content: {'PASS' if result.is_valid else 'FAIL'}")
        if not result.is_valid:
            print("Errors found:")
            for error in result.errors:
                print(f"  - {error}")
    finally:
        import os
        os.unlink(schema_path)


if __name__ == "__main__":
    print("🧪 Advanced Rules Examples")
    print("=" * 60)
    print()
    
    # Test individual advanced rules
    test_regex_must_match()
    test_no_duplicate_sentences()
    test_min_list_items()
    test_max_passive_voice_ratio()
    
    print("=" * 60)
    print()
    
    # Test combined advanced rules
    test_combined_advanced_rules() 