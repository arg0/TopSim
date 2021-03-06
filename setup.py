#! /usr/bin/env python3

from setuptools import setup

url = "https://github.com/chuanconggao/TopSim"
version = "0.1.5"

setup(
    name="TopSim",

    packages=["topsim"],
    scripts=["topsim-cli"],
    include_package_data=True,

    url=url,

    version=version,
    download_url=f"{url}/tarball/{version}",

    license="MIT",

    author="Chuancong Gao",
    author_email="chuancong@gmail.com",

    description="Search the most similar strings against the query in Python 3.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",

    keywords=[
        "similarity-search",
        "string-search"
    ],
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3"
    ],

    python_requires=">= 3",
    install_requires=[
        line.strip() for line in open("requirements.txt")
    ]
)
