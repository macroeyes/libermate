from setuptools import setup
from pip.req import parse_requirements

setup(
    name='libermate',
    version='0.1.0',
    packages=[''],
    package_dir={
        '': 'libermate',
        'lib': 'pyclips'
    },
    install_requires=[str(ir.req) for ir in parse_requirements('requirements.txt')],
    url='https://github.com/macroeyes/libermate',
    license='',
    author='Eric C. Shug',
    entry_points = {
        'console_scripts': [
            'libermate = libermate.libermate:main'
        ]
    }
)
