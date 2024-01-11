from setuptools import find_packages, setup

setup(
    name='DSMPdfLib',
    packages=find_packages(include=['dsmPdfLib'], exclude=['tests','examples']),
    version='0.1.0',
    description='DSM PDF File Processing Library',
    author='Larry Welch - Foundation Technologies',
)