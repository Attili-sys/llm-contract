# Contributing to llm-contracts

Thank you for your interest in contributing to llm-contracts! This document provides guidelines and information for contributors.

**Created by [Mohamed Jama](https://www.linkedin.com/in/mohamedjama/)**

## Table of Contents

- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Code Style](#code-style)
- [Testing](#testing)
- [Pull Request Process](#pull-request-process)
- [Feature Requests](#feature-requests)
- [Bug Reports](#bug-reports)
- [Documentation](#documentation)

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip
- git

### Development Setup

1. **Fork the repository**
   ```bash
   git clone https://github.com/Maxamed/llm-contract.git
   cd llm-contracts
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install in development mode**
   ```bash
   pip install -e .
   ```

4. **Install development dependencies**
   ```bash
   pip install -r requirements-dev.txt
   ```

## Code Style

### Python Code Style

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with the following guidelines:

- **Line length**: 88 characters (Black default)
- **Indentation**: 4 spaces
- **Imports**: Grouped and sorted with isort
- **Type hints**: Required for public functions

### Code Formatting

We use automated tools to maintain consistent code style:

```bash
# Format code with Black
black src/ tests/

# Sort imports with isort
isort src/ tests/

# Check code style with flake8
flake8 src/ tests/

# Type checking with mypy
mypy src/
```

### Pre-commit Hooks

Install pre-commit hooks to automatically format code:

```bash
pip install pre-commit
pre-commit install
```

## Testing

### Running Tests

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=llm_contracts

# Run specific test file
python -m pytest tests/test_schema.py

# Run with verbose output
python -m pytest -v
```

### Writing Tests

- **Test files**: Place in `tests/` directory
- **Naming**: `test_<module_name>.py`
- **Coverage**: Aim for 90%+ coverage
- **Test cases**: Include positive and negative cases

### Example Test

```python
import pytest
from llm_contracts import contracts

def test_valid_user_profile():
    """Test that valid user profile passes validation."""
    data = {
        "name": "John Doe",
        "age": 25,
        "email": "john@example.com"
    }
    
    result = contracts.validate(data, 'tests/schemas/user_profile.yaml')
    
    assert result.is_valid
    assert len(result.errors) == 0

def test_invalid_user_profile():
    """Test that invalid user profile fails validation."""
    data = {
        "name": "john",  # Invalid format
        "age": "25",     # Wrong type
        "email": "invalid-email"  # Invalid email
    }
    
    result = contracts.validate(data, 'tests/schemas/user_profile.yaml')
    
    assert not result.is_valid
    assert len(result.errors) > 0
```

## Pull Request Process

### Before Submitting

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Follow the code style guidelines
   - Add tests for new functionality
   - Update documentation if needed

3. **Run tests and checks**
   ```bash
   # Run all tests
   python -m pytest
   
   # Check code style
   black --check src/ tests/
   isort --check-only src/ tests/
   flake8 src/ tests/
   mypy src/
   ```

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add new validation rule for email format"
   ```

### Pull Request Guidelines

1. **Title**: Use conventional commit format
   - `feat:` for new features
   - `fix:` for bug fixes
   - `docs:` for documentation
   - `test:` for test additions
   - `refactor:` for code refactoring

2. **Description**: Include
   - Summary of changes
   - Motivation for changes
   - Testing performed
   - Breaking changes (if any)

3. **Checklist**:
   - [ ] Code follows style guidelines
   - [ ] Tests pass
   - [ ] Documentation updated
   - [ ] No breaking changes (or documented)

### Example Pull Request

```markdown
## Description
Adds a new validation rule for email format checking.

## Motivation
Many LLM outputs contain invalid email formats. This rule helps ensure
email addresses follow proper RFC standards.

## Testing
- Added unit tests for email validation
- Tested with various email formats
- All existing tests pass

## Breaking Changes
None - this is a new feature that doesn't affect existing functionality.
```

## Feature Requests

### Before Submitting

1. **Check existing issues** - Your feature might already be requested
2. **Search documentation** - The feature might already exist
3. **Consider scope** - Is this within the project's goals?

### Feature Request Template

```markdown
## Feature Request: [Feature Name]

### Problem Statement
Describe the problem this feature would solve.

### Proposed Solution
Describe your proposed solution.

### Use Cases
Provide specific examples of how this would be used.

### Alternatives Considered
What other approaches did you consider?

### Additional Context
Any other relevant information.
```

## Bug Reports

### Before Submitting

1. **Check existing issues** - The bug might already be reported
2. **Test with latest version** - The bug might already be fixed
3. **Reproduce the issue** - Ensure it's a real bug

### Bug Report Template

```markdown
## Bug Report: [Brief Description]

### Environment
- OS: [e.g., macOS 12.0]
- Python version: [e.g., 3.9.7]
- llm-contracts version: [e.g., 0.1.0]

### Steps to Reproduce
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Expected Behavior
What you expected to happen.

### Actual Behavior
What actually happened.

### Additional Context
Any other relevant information (logs, screenshots, etc.).
```

## Documentation

### Contributing to Documentation

1. **Update README.md** for user-facing changes
2. **Update API.md** for API changes
3. **Add examples** for new features
4. **Update docstrings** for code changes

### Documentation Standards

- **Clear and concise** - Write for the target audience
- **Include examples** - Show real usage
- **Keep updated** - Documentation should match code
- **Use proper formatting** - Follow markdown conventions

## Code of Conduct

### Our Standards

- **Be respectful** - Treat everyone with respect
- **Be constructive** - Provide helpful feedback
- **Be inclusive** - Welcome contributors from all backgrounds
- **Be professional** - Maintain professional behavior

### Enforcement

- **Warning** - First violation gets a warning
- **Temporary ban** - Repeated violations may result in temporary ban
- **Permanent ban** - Severe violations may result in permanent ban

## Getting Help

### Questions and Support

- **GitHub Issues**: For bug reports and feature requests
- **GitHub Discussions**: For questions and general discussion
- **LinkedIn**: [Mohamed Jama](https://www.linkedin.com/in/mohamedjama/)

### Resources

- **Documentation**: [README.md](README.md) and [API.md](API.md)
- **Examples**: [examples/](examples/) directory
- **Tests**: [tests/](tests/) directory for usage examples

## Recognition

### Contributors

Contributors will be recognized in:
- **README.md** - For significant contributions
- **CHANGELOG.md** - For all contributions
- **GitHub contributors** - Automatic recognition

### Hall of Fame

Special recognition for:
- **Major features** - New validation rules, CLI features
- **Documentation** - Comprehensive guides, tutorials
- **Testing** - High coverage, edge cases
- **Community** - Helping others, answering questions

---

**Thank you for contributing to llm-contracts!**

**Created by [Mohamed Jama](https://www.linkedin.com/in/mohamedjama/)** 