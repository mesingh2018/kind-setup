# Contributing to Kind Cluster Setup

We welcome contributions to the Kind Cluster Setup project! This document provides guidelines for contributing to the project.

## Getting Started

1. Fork the repository on GitHub.
2. Clone your fork locally: `git clone https://github.com/yourusername/kind-cluster-setup.git`
3. Create a new branch for your feature or bug fix: `git checkout -b feature-or-bugfix-name`
4. Make your changes and commit them with a clear commit message.
5. Push your changes to your fork: `git push origin feature-or-bugfix-name`
6. Create a pull request from your fork to the main repository.

## Development Setup

1. Ensure you have Python 3.7 or later installed.
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
4. Install the project in editable mode: `pip install -e .`
5. Install development dependencies: `pip install -r requirements-dev.txt`

## Code Style

We follow the PEP 8 style guide for Python code. Please ensure your code adheres to this standard.

## Testing

1. Write tests for your changes.
2. Run tests: `pytest tests/`
3. Ensure all tests pass before submitting a pull request.

## Code of Conduct

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) for guidelines on how to interact with the community.
