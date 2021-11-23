"""
Module setup file
"""
from setuptools import setup, find_packages

with open('requirements.txt', encoding='utf-8') as f:
    REQUIRED = f.read().splitlines()


setup(
    name='the_arena',
    version='1.0',
    packages=find_packages(),
    description="Simple Arena game",
    install_requires=REQUIRED,
)
