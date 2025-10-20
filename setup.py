"""
Setup script for Unsloth to Brev Adapter.
"""

from pathlib import Path
from setuptools import setup, find_packages

# Read the README file
readme_file = Path(__file__).parent / "README.md"
if readme_file.exists():
    with open(readme_file, "r", encoding="utf-8") as f:
        long_description = f.read()
else:
    long_description = "Automatically convert Unsloth Colab notebooks to NVIDIA Brev launchables"

# Read requirements
requirements_file = Path(__file__).parent / "requirements.txt"
if requirements_file.exists():
    with open(requirements_file, "r", encoding="utf-8") as f:
        requirements = [
            line.strip() 
            for line in f 
            if line.strip() and not line.startswith("#")
        ]
else:
    requirements = []

setup(
    name="unsloth-brev-adapter",
    version="1.0.0",
    author="Brev Team",
    author_email="support@brev.dev",
    description="Convert Unsloth Colab notebooks to NVIDIA Brev launchables",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brevdev/unsloth-notebook-adaptor",
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "unsloth-convert=scripts.convert_notebook:main",
            "unsloth-compare=scripts.compare_notebooks:main",
            "unsloth-metadata=scripts.generate_metadata:main",
            "unsloth-summary=scripts.create_summary:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["templates/*.jinja2"],
    },
    zip_safe=False,
)

