import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='notacarioca',
    version='0.2.6',
    packages=['notacarioca'],
    include_package_data=True,
    license='Apache 2.0',
    description='NFSe for Rio de Janeiro city.',
    long_description=README,
    url='https://github.com/CatarinaPinheiro/py-notacarioca',
    author='Fabiano Moraes',
    author_email='catarina_pine@hotmail.com'
)
