#!/usr/bin/env python

from setuptools import setup, find_packages

if __name__ == '__main__':
    setup(
        name='aiida_mul',
        author='Rico Haeuselmann',
        author_email='haeuselm@epfl.ch',
        classifiers=[
            'Programming Language :: Python'
        ],
        version='0.1',
        install_requires=[
            'aiida >= 0.7'
        ],
        packages=find_packages(),
        entry_points={
            'console_scripts': [
                'aiida_mul = aiida_mul.code:mul'
            ],
            'aiida.calculations': [
                'mul = aiida_mul.calcs:MultiplyCalculation'
            ],
            'aiida.parsers': [
                'mul = aiida_mul.parsers:MultiplyParsers'
            ]
        },
        scripts=['bin/submit_mul']
    )
