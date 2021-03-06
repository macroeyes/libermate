from setuptools import setup, find_packages
from pip.req import parse_requirements

setup(
    name='libermate',
    version='0.1.0',
    packages=find_packages(),
    dependency_links = [
        "file://./lib/pyclips"
    ],
    install_requires=[
        'pyclips==1.0.7.348-clips-6.24'
    ],
    url='https://github.com/macroeyes/libermate',
    license='',
    author='Eric C. Shug',
    entry_points = {
        'console_scripts': [
            'libermate = libermate.libermate:main'
        ]
    }
)
