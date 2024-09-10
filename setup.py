from setuptools import setup, find_packages

setup(
    name='assignment0',
    version='1.0',
    author='Bhanu Prakash Reddy Gundam',
    author_email='b.gundam@ufl.edu',
    packages=find_packages(exclude=('tests', 'docs')),
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)