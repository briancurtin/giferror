#! /usr/bin/env python

from setuptools import setup

setup(name="giferror",
      version="1.0.0",
      description="Open GIFs in exception messages in a web browser.",
      long_description=open("README.rst", "r").read(),
      author="Brian Curtin",
      author_email="brian@python.org",
      url="https://github.com/briancurtin/giferror",
      py_modules=["giferror"],
      classifiers=[
        "Development Status :: 6 - Mature",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        ]
     )
