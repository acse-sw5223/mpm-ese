from setuptools import setup, find_packages

setup(
    name="primes",
    version="0.1",
    packages=find_packages(),
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple package to work with prime numbers.",
    long_description="A longer description about the functions and \
        utilities provided by the primes package.",
    long_description_content_type="text/plain",
    url="https://github.com/yourusername/primes",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
