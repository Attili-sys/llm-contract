"""Basic validation example for llm-contracts."""

import json
from pathlib import Path

from llm_contracts import validate_output


def main():
    """Demonstrate basic validation functionality."""
    
    # Example 1: Validate JSON output
    print("=== Example 1: JSON Validation ===")
    
    user_data = {
        "name": "John Doe",
        "age": 30,
        "email": "john.doe@example.com",
        "bio": "I am a professional software developer with 5 years of experience."
    }
    
    schema_path = Path(__file__).parent / "schemas" / "user_profile.yaml"
    
    result = validate_output(user_data, schema_path)
    
    if result.is_valid:
        print("✅ JSON validation passed!")
    else:
        print("❌ JSON validation failed!")
        for error in result.errors:
            print(f"  - {error}")
    
    print()
    
    # Example 2: Validate text output
    print("=== Example 2: Text Validation ===")
    
    blog_post = """
    # Introduction to AI
    
    Artificial Intelligence is transforming the way we work and live. 
    This technology offers incredible opportunities for innovation and growth.
    
    ## Key Features
    
    - Machine Learning capabilities
    - Natural Language Processing
    - Computer Vision applications
    
    ## Call to Action
    
    Start exploring AI today to unlock new possibilities for your business!
    """
    
    # Create a simple text validation schema
    text_schema = {
        "rules": [
            {"keyword_must_include": "AI"},
            {"keyword_must_include": "features"},
            {"keyword_must_include": "call to action"},
            {"phrase_order": {"first": "features", "then": "call to action"}},
            {"word_count_min": 20},
            {"no_placeholder_text": "\\[YOUR_TEXT_HERE\\]"}
        ]
    }
    
    # Write schema to temporary file
    import yaml
    import tempfile
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        yaml.dump(text_schema, f)
        temp_schema_path = f.name
    
    try:
        result = validate_output(blog_post, temp_schema_path)
        
        if result.is_valid:
            print("✅ Text validation passed!")
        else:
            print("❌ Text validation failed!")
            for error in result.errors:
                print(f"  - {error}")
    finally:
        Path(temp_schema_path).unlink()
    
    print()
    
    # Example 3: Failed validation
    print("=== Example 3: Failed Validation ===")
    
    invalid_data = {
        "name": "john doe",  # Doesn't match pattern
        "age": 15,  # Too young
        "email": "invalid-email",  # Invalid email
        "bio": "Short."  # Too short
    }
    
    result = validate_output(invalid_data, schema_path)
    
    if result.is_valid:
        print("✅ Validation passed!")
    else:
        print("❌ Validation failed!")
        for error in result.errors:
            print(f"  - {error}")


if __name__ == "__main__":
    main() 