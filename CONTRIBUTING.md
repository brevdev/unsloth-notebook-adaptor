# Contributing to Unsloth to Brev Adapter

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the project.

## 🚀 Quick Start

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone git@github.com:YOUR_USERNAME/unsloth-notebook-adaptor.git
cd unsloth-notebook-adaptor

# Add upstream remote
git remote add upstream git@github.com:brevdev/unsloth-notebook-adaptor.git
```

### 2. Set Up Development Environment

```bash
# Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -e .
```

### 3. Run Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=adapters --cov-report=term --cov-report=html

# Run specific test file
pytest tests/test_conversions.py -v
```

## 📝 Development Workflow

### 1. Create a Branch

```bash
# Sync with upstream
git fetch upstream
git checkout main
git merge upstream/main

# Create feature branch
git checkout -b feature/your-feature-name
```

### 2. Make Changes

- Write clean, documented code
- Follow PEP 8 style guidelines
- Add tests for new functionality
- Update documentation as needed

### 3. Test Your Changes

```bash
# Run tests
pytest tests/ -v

# Check code style (optional)
pip install flake8
flake8 adapters/ scripts/ --max-line-length=100
```

### 4. Commit Changes

Use [Conventional Commits](https://www.conventionalcommits.org/) format:

```bash
# Examples:
git commit -m "feat: add support for new model"
git commit -m "fix: correct path handling in storage conversion"
git commit -m "docs: update README with new examples"
git commit -m "test: add tests for magic command conversion"
```

Commit types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Test additions or changes
- `refactor`: Code refactoring
- `style`: Code style changes (formatting, etc.)
- `chore`: Maintenance tasks

### 5. Push and Create Pull Request

```bash
# Push to your fork
git push origin feature/your-feature-name

# Create a Pull Request on GitHub
```

## 🎯 Areas for Contribution

### 1. Add New Models

Update [`adapters/model_configs.py`](adapters/model_configs.py) to add support for new Unsloth models:

```python
"new-model-name": {
    "model_name": "New Model Name",
    "launchable_name": "new-model-name",
    "recommended_gpu": "L4",
    "min_vram_gb": 16,
    "recommended_batch_size": 4,
    "categories": ["text-generation", "fine-tuning"],
    "difficulty": "beginner",
    "upstream_notebook_url": "https://colab.research.google.com/...",
    "multi_gpu": False
}
```

### 2. Improve Conversions

Enhance conversion functions in [`adapters/colab_to_brev.py`](adapters/colab_to_brev.py):

- Better pattern matching
- Handle edge cases
- Optimize converted code
- Add new conversion types

### 3. Add Tests

Increase test coverage in [`tests/`](tests/):

- Unit tests for conversion functions
- Integration tests for full notebook conversions
- Edge case tests

### 4. Improve Templates

Enhance Jinja2 templates in [`templates/`](templates/):

- Better setup scripts
- More comprehensive READMEs
- Optimized Docker configurations

### 5. Fix Bugs

Check [GitHub Issues](https://github.com/brevdev/unsloth-notebook-adaptor/issues) for:

- Bug reports
- Feature requests
- Documentation improvements

## 🧪 Testing Guidelines

### Writing Tests

1. **Unit Tests** - Test individual functions in isolation
2. **Integration Tests** - Test full conversion workflows
3. **Use Fixtures** - Leverage pytest fixtures for reusable components
4. **Descriptive Names** - Use clear, descriptive test function names

Example test:

```python
def test_convert_installation(adapter, test_config):
    """Test installation conversion from Colab to Brev."""
    code = '!pip install "unsloth[colab-new]"'
    
    result = adapter.convert_installation(code, test_config)
    
    assert 'colab-new' not in result
    assert 'conda' in result
    assert 'subprocess.check_call' in result
```

### Running Tests

```bash
# All tests
pytest tests/ -v

# Specific test file
pytest tests/test_conversions.py -v

# Specific test function
pytest tests/test_conversions.py::test_convert_installation -v

# With coverage
pytest tests/ --cov=adapters --cov-report=html

# Stop on first failure
pytest tests/ -x

# Show print statements
pytest tests/ -s
```

## 📚 Code Style

### Python Style

- Follow PEP 8
- Use type hints where appropriate
- Write docstrings for functions and classes
- Maximum line length: 100 characters

### Documentation Style

- Use Google-style docstrings
- Include examples in docstrings when helpful
- Keep comments concise and meaningful

Example:

```python
def convert_magic_commands(self, code: str, config: Dict[str, Any]) -> str:
    """
    Convert Jupyter magic commands to subprocess calls.

    Args:
        code: Source code containing magic commands
        config: Configuration dictionary for the model

    Returns:
        Converted code with subprocess calls instead of magic commands

    Example:
        >>> adapter.convert_magic_commands('!pip install numpy', config)
        'subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy"])'
    """
```

## 🐛 Bug Reports

When reporting bugs, include:

1. **Description** - Clear description of the issue
2. **Steps to Reproduce** - Minimal steps to reproduce the bug
3. **Expected Behavior** - What you expected to happen
4. **Actual Behavior** - What actually happened
5. **Environment** - Python version, OS, etc.
6. **Logs** - Relevant error messages or logs

## 💡 Feature Requests

When requesting features, include:

1. **Use Case** - Describe the problem you're trying to solve
2. **Proposed Solution** - Your suggested implementation
3. **Alternatives** - Other solutions you've considered
4. **Impact** - Who would benefit from this feature

## 🔍 Code Review

All contributions go through code review. Reviewers will check:

- Code quality and style
- Test coverage
- Documentation
- Performance implications
- Backward compatibility

Be responsive to feedback and iterate on your PR as needed.

## 📄 License

By contributing, you agree that your contributions will be licensed under the LGPL-3.0 License.

## 🙏 Recognition

Contributors will be recognized in:

- GitHub contributors list
- Release notes (for significant contributions)

## 📞 Questions?

- Open a [GitHub Issue](https://github.com/brevdev/unsloth-notebook-adaptor/issues)
- Join discussions in Pull Requests
- Check existing Issues and PRs for similar questions

## 🎉 Thank You!

Your contributions help make this project better for everyone. We appreciate your time and effort!

---

**Happy Contributing!** 🚀

