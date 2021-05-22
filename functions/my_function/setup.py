import os
from setuptools import setup, find_packages

requirements = open(os.path.join(os.path.dirname(__file__), "requirements.txt"),
                    'r').readlines()

function_name = f"f_{os.path.basename(os.path.dirname(__file__))}"

setup(
    name=function_name,
    author="Some user",
    author_email="user@example.com",
    description="Python code for AWS function",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=requirements,
)
