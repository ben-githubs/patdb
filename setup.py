from pathlib import Path

from setuptools import find_packages, setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

PAT_VERSION = (this_directory / "VERSION").read_text().strip()

install_requires = [
    "gql",
    "aiohttp",
    "boto3",
    "dynaconf",
    "jsonpath-ng",
    "jsonschema",
    "nested_lookup",
    "packaging",
    "requests",
    "ruamel.yaml",
    "schema",
    "semver",
    "sqlfluff",
    "panther-core==0.8.1",
    "typing-extensions",
    "jsonlines",
    "setuptools"
]

setup(
    name="patdb",
    version=PAT_VERSION,
    packages=find_packages(),
    license="AGPL-3.0",
    description="Panther command line interface for writing, testing, and packaging policies/rules.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Panther Labs Inc",
    author_email="ben.airey@panther.com",
    url="https://github.com/ben-githubs/patdb",
    download_url=f"https://github.com/panther-labs/panther_analysis_tool/archive/v{PAT_VERSION}.tar.gz",
    keywords=["Security", "CLI"],
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Security",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Programming Language :: Python :: 3.9",
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'patdb = panther_analysis_tool.main:run'
        ]
    }
)
