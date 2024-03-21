from setuptools import find_packages, setup

setup(
    name='DSMFileProcessorLib',
    pacakges=find_packages(include=['dsmFileProcessingLib'], exclude=['examples', 'tests']),
    version='0.1.1',
    description='DSM File Processor Library',
    author='Larry Welch - Foundation Technologies',
)