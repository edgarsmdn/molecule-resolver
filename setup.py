from setuptools import setup

setup(
    name='moleculeresolver',
    version='0.1',
    author='Simon Müller',
    author_email='simon.mueller@tuhh.de',
    packages=['moleculeresolver'],
    url='https://collaborating.tuhh.de/v-8/moleculeresolver.git',
    license='LICENSE.txt',
    description='A package to use several web services to find molecule structures, synonyms and CAS.',
    long_description=open('README.md').read(),
    install_requires=['prompt_toolkit', 'regex', 'rdkit', 'tqdm', 'urllib3', 'xmltodict', 'xyz2mol']
)