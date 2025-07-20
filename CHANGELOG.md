# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Custom validator support for user-defined validation functions
- Batch processing capabilities for multiple files
- Strict mode for immediate failure on validation errors
- Enhanced error messages with more context

### Changed
- Improved HTML report styling and responsiveness
- Better schema reference highlighting in reports
- More detailed error categorization

### Fixed
- Placeholder text detection edge cases
- Schema validation for nested objects
- CLI argument parsing improvements

## [0.1.0] - 2025-07-20

### Added
- **Core validation engine** with JSON schema support
- **Text linting rules** for keyword validation, placeholder detection, and content analysis
- **CLI interface** (`llm-validate`) for command-line usage
- **Python SDK** with `validate_output()` and `generate_html_report()` functions
- **HTML report generation** with professional styling and error categorization
- **YAML-based schemas** for easy configuration
- **Comprehensive test suite** with unit and integration tests
- **Documentation** including README, API docs, and contributing guidelines

### Features
- **Schema Validation**
  - JSON schema validation using jsonschema
  - Field type checking (str, int, float, bool, list, dict)
  - Pattern matching with regex support
  - Min/max value constraints
  - Required field validation
  - Nested object validation

- **Text Linting Rules**
  - `keyword_must_include`: Ensure specific keywords are present
  - `keyword_must_not_include`: Ensure specific keywords are absent
  - `no_placeholder_text`: Detect placeholder patterns like `[YOUR_TEXT_HERE]`
  - `word_count_min` / `word_count_max`: Enforce word count limits
  - `phrase_proximity`: Ensure terms appear within specified distance
  - `phrase_order`: Enforce phrase ordering (e.g., "features" before "buy now")
  - `section_must_start_with`: Validate section headers
  - `heading_max_depth`: Limit heading depth in Markdown
  - `list_item_pattern`: Validate list item formatting

- **CLI Features**
  - Single file validation: `llm-validate file.json --schema schema.yaml`
  - HTML report generation: `--html-report report.html`
  - Batch processing: `--batch directory/`
  - Help and usage information: `--help`

- **HTML Reports**
  - Professional styling with CSS
  - Error categorization (Pass/Fail/Warning)
  - Schema reference sections
  - Success rate calculations
  - Responsive design

- **Python SDK**
  - `validate_output(data, schema_path)` → (valid, errors)
  - `generate_html_report(result, output_path, schema_path)`
  - Easy integration into existing workflows

### Documentation
- **README.md**: Comprehensive project overview and quick start guide
- **API.md**: Detailed API documentation with examples
- **CONTRIBUTING.md**: Guidelines for contributors
- **CHANGELOG.md**: Version history and changes
- **result-dev.md**: Development summary for code review

### Examples
- **Product description validation** with quality keywords and placeholder detection
- **User profile validation** with field type checking and format validation
- **Blog post validation** with Markdown structure and content rules
- **Batch processing** for multiple files
- **Custom validators** for specific business logic

### Testing
- **Unit tests** for all core functionality
- **Integration tests** for end-to-end workflows
- **Example tests** demonstrating real-world usage
- **Test coverage** for schema validation, text linting, and HTML generation

### Package Configuration
- **pyproject.toml** with proper metadata and dependencies
- **Entry points** for CLI commands
- **MIT License** for open source distribution
- **Development setup** with editable install

---

## Version History

### v0.1.0 (Initial Release)
- Complete core functionality
- CLI and Python SDK
- HTML report generation
- Comprehensive documentation
- Test suite
- Example schemas and outputs

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on contributing to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 