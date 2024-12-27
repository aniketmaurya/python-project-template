<div align="center">
  <h1>Python Project Template 🐍</h1>
  <!-- A brief description of what this project does and who it's for -->
  <p>A template to kick-start your open-source Python project.</p>
</div>

<p align="center">
  <a href="https://github.com/aniketmaurya/python-project-template/actions/workflows/main.yml">
    <img src="https://github.com/aniketmaurya/python-project-template/actions/workflows/main.yml/badge.svg" alt="Tests">
  </a>
  <a href="https://codecov.io/gh/aniketmaurya/python-project-template">
    <img src="https://codecov.io/gh/aniketmaurya/python-project-template/branch/main/graph/badge.svg" alt="codecov">
  </a>
  <a href="https://github.com/psf/black">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="black">
  </a>
  <a href="https://github.com/aniketmaurya/python-project-template/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/aniketmaurya/python-project-template.svg" alt="license">
  </a>
</p>

<p align="center">
  <a href="https://github.com/codespaces/badge.svg)](https://codespaces.new/aniketmaurya/python-project-template?template=false">
    <img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces">
  </a>
</p>

# Features

- 🚀 Modern Python project structure
- 📦 Pre-configured [pyproject.toml](pyproject.toml)
- 🤖 ML server template with [LitServe](https://github.com/Lightning-AI/LitServe)
- 🧪 Testing setup with [pytest](https://docs.pytest.org/en/latest/)
- 👷 CI/CD with [GitHub Actions](https://github.com/aniketmaurya/python-project-template/blob/main/.github/workflows)
- 📝 Auto-generated documentation
- 🎯 Type hints and static type checking
- 🔍 Code formatting with ruff and isort
- 🐛 Linting with ruff

# Project Structure

```
python-project-template/
├── .github/
│   └── workflows/          # GitHub Actions workflows
├── docs/                   # Documentation
├── src/                    # Source code
│   └── python_project_template/
├── tests/                  # Test files
├── .gitignore
├── LICENSE
├── README.md
├── pyproject.toml         # Project metadata and dependencies
└── setup.py              # Package installation
```

# Installation

## From Source

```bash
git clone https://github.com/aniketmaurya/python-project-template.git
cd python-project-template
pip install .
```

## Development Installation

```bash
git clone https://github.com/aniketmaurya/python-project-template.git
cd python-project-template
pip install -e ".[dev]"
```

## Usage

```python
from python_project_template import do_something_awesome

print(do_something_awesome())
```

# Development

1. Clone the repository

```bash
git clone https://github.com/aniketmaurya/python-project-template.git
cd python-project-template
```

2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install development dependencies

```bash
pip install -e ".[dev]"
```

## Running Tests

```bash
pytest tests/
```

# Contributing

Contributions are always welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

Please make sure to update tests as appropriate and follow the existing coding style.

# License

[MIT](https://choosealicense.com/licenses/mit/) - Feel free to use this template for your projects!
