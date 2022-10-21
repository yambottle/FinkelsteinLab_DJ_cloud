from setuptools import setup, find_packages
from os import path

pkg_name = 'workflow'
here = path.abspath(path.dirname(__file__))

long_description = """"
DataJoint data workflow for ArsenyFinkelstein Lab
"""

with open(path.join(here, 'requirements.txt')) as f:
    requirements = f.read().splitlines()

with open(path.join(here, pkg_name, 'version.py')) as f:
    exec(f.read())

setup(
    name='',
    version=__version__,
    description="DataJoint data workflow for ArsenyFinkelsteinLab",
    long_description=long_description,
    author='Arseny Finkelstein Lab',
    author_email='info@datajoint.com',
    license='MIT',
    url='https://github.com/ArsenyFinkelsteinLab/DJ_cloud',
    keywords='neuroscience datajoint',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=requirements,
    entry_points={
        'console_scripts': ['run_workflow=workflow.populate.process:cli'],
    }
)
