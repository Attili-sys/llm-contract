#!/usr/bin/env python3
"""
Markdown Reports Example

Demonstrates markdown report generation for CI/CD pipelines.
"""

import json
import tempfile
import yaml
from pathlib import Path

from llm_contracts import contracts


def markdown_reports_example():
    """Demonstrate markdown report generation."""
    
    print("📝 Markdown Reports Example")
    print("=" * 50)
    
    # Sample content to validate
    content_data = {
        "title": "Product Launch Announcement",
        "content": """
        # Product Launch Announcement
        
        We are excited to announce the launch of our premium wireless headphones!
        
        ## Key Features
        
        1. Advanced noise cancellation technology
        2. 30-hour battery life
        3. Premium comfort design
        4. Bluetooth 5.0 connectivity
        
        ## Pricing
        
        The headphones are priced at 299.99 USD and include free shipping.
        
        ## Call to Action
        
        Don't miss out on this amazing opportunity! Buy now and experience premium sound quality.
        """
    }
    
    # Create a comprehensive schema
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
            # Content quality
            {"keyword_must_include": ["premium", "quality"]},
            {"keyword_must_not_include": ["cheap", "low quality"]},
            {"no_placeholder_text": "\\[YOUR_TEXT_HERE\\]"},
            
            # Structure requirements
            {"section_must_start_with": "^# "},
            {"heading_max_depth": 3},
            {"min_list_items": 3},
            
            # Content requirements
            {"word_count_min": 50},
            {"keyword_must_include": "call to action"},
            {"phrase_order": {"first": "features", "then": "call to action"}},
            
            # Advanced rules
            {"regex_must_match": "\\b\\d{1,3}(?:\\.\\d{2})?\\s*USD\\b"},
            {"no_duplicate_sentences": True},
            {"max_passive_voice_ratio": 0.3}
        ]
    }
    
    # Write schema to temporary file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        yaml.dump(schema, f)
        schema_path = f.name
    
    try:
        print(f"📋 Validating content...")
        print(f"Schema: {schema_path}")
        print()
        
        # Validate and generate markdown report
        result = contracts.validate_and_report(
            content_data,
            schema_path,
            report_path="validation_report.md",
            report_format="markdown"
        )
        
        print(f"✅ Validation completed!")
        print(f"📊 Results: {'PASS' if result.is_valid else 'FAIL'}")
        print(f"📄 Markdown report generated: validation_report.md")
        
        # Also generate HTML report for comparison
        contracts.generate_report(
            result,
            "validation_report.html",
            schema_path,
            format="html"
        )
        print(f"📄 HTML report generated: validation_report.html")
        
        return result
        
    finally:
        import os
        os.unlink(schema_path)


def ci_cd_integration_example():
    """Demonstrate CI/CD integration with markdown reports."""
    
    print("\n🔄 CI/CD Integration Example")
    print("=" * 50)
    
    # Simulate multiple content files
    content_files = [
        {
            "name": "product_announcement.md",
            "content": {
                "title": "New Product Launch",
                "content": "Premium product with quality features. Buy now for 199.99 USD!"
            }
        },
        {
            "name": "technical_specs.md", 
            "content": {
                "title": "Technical Specifications",
                "content": "This product is designed for users. It is used by many people. It is loved by users."
            }
        },
        {
            "name": "marketing_copy.md",
            "content": {
                "title": "Marketing Copy",
                "content": "Discover our amazing product with premium quality and excellent features. Limited time offer - buy now for 299.99 USD!"
            }
        }
    ]
    
    # Create a simple validation schema
    schema = {
        "rules": [
            {"keyword_must_include": "quality"},
            {"word_count_min": 20},
            {"no_duplicate_sentences": True},
            {"regex_must_match": "\\b\\d{1,3}(?:\\.\\d{2})?\\s*USD\\b"}
        ]
    }
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        yaml.dump(schema, f)
        schema_path = f.name
    
    try:
        print("Running validation on multiple files...")
        print()
        
        all_results = []
        
        for file_info in content_files:
            print(f"📄 Validating {file_info['name']}...")
            
            result = contracts.validate(file_info['content'], schema_path)
            all_results.append({
                'file': file_info['name'],
                'result': result
            })
            
            status = "✅ PASS" if result.is_valid else "❌ FAIL"
            print(f"   {status}")
            
            if not result.is_valid:
                for error in result.errors[:2]:  # Show first 2 errors
                    print(f"     - {error}")
                if len(result.errors) > 2:
                    print(f"     ... and {len(result.errors) - 2} more errors")
        
        # Generate summary report
        print(f"\n📊 Summary Report")
        print(f"Files processed: {len(all_results)}")
        
        passed = sum(1 for r in all_results if r['result'].is_valid)
        failed = len(all_results) - passed
        
        print(f"Passed: {passed}")
        print(f"Failed: {failed}")
        print(f"Success rate: {(passed/len(all_results)*100):.1f}%")
        
        # Generate detailed markdown report
        with open("ci_cd_summary.md", "w") as f:
            f.write("# CI/CD Validation Summary\n\n")
            f.write(f"**Generated**: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"**Files Processed**: {len(all_results)}\n")
            f.write(f"**Passed**: {passed}\n")
            f.write(f"**Failed**: {failed}\n")
            f.write(f"**Success Rate**: {(passed/len(all_results)*100):.1f}%\n\n")
            
            f.write("## Results\n\n")
            for item in all_results:
                status = "✅ PASS" if item['result'].is_valid else "❌ FAIL"
                f.write(f"### {item['file']} - {status}\n")
                
                if not item['result'].is_valid:
                    f.write("**Errors:**\n")
                    for error in item['result'].errors:
                        f.write(f"- {error}\n")
                f.write("\n")
        
        print(f"📄 Detailed report generated: ci_cd_summary.md")
        
        return all_results
        
    finally:
        import os
        os.unlink(schema_path)


if __name__ == "__main__":
    # Run markdown reports example
    report_result = markdown_reports_example()
    
    print("\n" + "="*60 + "\n")
    
    # Run CI/CD integration example
    ci_results = ci_cd_integration_example() 