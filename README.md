# Kind Cluster Setup

A tool for setting up Kind (Kubernetes in Docker) clusters with independent app deployments.

## Features

- Create and manage Kind clusters
- Deploy applications using Helm or Kubernetes manifests
- Support for different environments (dev, qa, staging, prod)
- Independent configuration for each application

## Prerequisites

- Python 3.7 or later
- Docker
- Kind
- kubectl
- Helm (for Helm-based deployments)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/kind-cluster-setup.git
   cd kind-cluster-setup
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the package in editable mode:
   ```sh
   pip install -e .
   ```

## Usage

### Creating a Kind cluster