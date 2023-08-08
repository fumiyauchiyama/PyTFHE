"""Minimal setup file for tasks project."""

from setuptools import setup, find_packages

setup(
    name='PyTFHE',
    version='0.0.1',
    license='proprietary',
    description='Module Experiment',

    author='FumyiaU',
    author_email='fumiyauchiyama.public@gmail.com',
    url='None.com',

    packages=find_packages(where='PyTFHE'),
    package_dir={'PyTFHE': 'PyTFHE'},
    install_requires=[
        'numpy',
        'typing',
    ],
)

