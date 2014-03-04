from setuptools import setup
from pip.req import parse_requirements

setup(
    name='libermate',
    version='0.1.0',
    packages=['libermate'],
    install_requires=[str(ir.req) for ir in parse_requirements('requirements.txt')],
    url='https://github.com/macroeyes/libermate',
    license='MIT',
    author='Eric C. Shug',
)
