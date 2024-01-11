from setuptools import find_packages, setup

setup(
    name='DSMAzureLib',
    packages=find_packages(include=['dsmAzureLib'], exclude=['tests','examples']),
    version='0.1.0',
    description='DSM Azure File Processing Library',
    author='Larry Welch - Foundation Technologies',
)