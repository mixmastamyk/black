# Copyright (C) 2018 Łukasz Langa
from setuptools import setup
import sys

assert sys.version_info >= (3, 6, 0), "black requires Python 3.6+"
from pathlib import Path  # noqa E402

CURRENT_DIR = Path(__file__).parent


def get_long_description() -> str:
    readme_md = CURRENT_DIR / "README.md"
    with open(readme_md, encoding="utf8") as ld_file:
        return ld_file.read()


setup(
    name="nero",
    version="19.3b4",
    description="The uncompromising code formatter.  Single quotes version.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    keywords="automation formatter yapf autopep8 pyfmt gofmt rustfmt"
             "black single quotes",
    author="black authors",
    author_email="",
    url="https://github.com/mixmastamyk/nero",
    license="MIT",
    py_modules=["black", "blackd", "_version"],
    packages=["blib2to3", "blib2to3.pgen2"],
    package_data={"blib2to3": ["*.txt"]},
    python_requires=">=3.6",
    scripts=["nero"],
    zip_safe=False,
    install_requires=[
        "click>=6.5",
        "attrs>=18.1.0",
        "appdirs",
        "toml>=0.9.4",
        "typed-ast>=1.3.1",
        "regex",
    ],
    extras_require={"d": ["aiohttp>=3.3.2", "aiohttp-cors"]},
    test_suite="tests.test_black",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
    entry_points={
        "console_scripts": [
            "black=black:patched_main",
            "blackd=blackd:patched_main [d]",
        ]
    },
)
