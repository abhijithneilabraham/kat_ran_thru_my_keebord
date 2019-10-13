#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 19:36:29 2019

@author: abhijithneilabraham
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="katran",
    version="0.0.5",
    author="Abhijith Neil Abraham",
    author_email="abhijithneilabrahampk@gmail.com",
    description="Cat running experience through ya keeboooaard",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abhijithneilabraham/kat_ran_thru_my_keebord/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)