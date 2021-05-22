from setuptools import setup, find_packages


function_name = f"common_local"

setup(
    name=function_name,
    author="Some user",
    author_email="user@example.com",
    description="Python code for AWS function",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        'python-dotenv'
    ],
)
