from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="kind-cluster-setup",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "PyYAML>=5.4.1",
        "kubernetes>=17.17.0",
        "click>=8.0.1",
    ],
    entry_points={
        "console_scripts": [
            "kind-cluster-setup=kind_cluster_setup.main:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool for setting up Kind clusters with independent app deployments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/kind-cluster-setup",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
)