import setuptools

import sample_package

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

setuptools.setup(
    name='sample_package',
    version=sample_package.__version__,
    packages=setuptools.find_packages(),
    install_requires=install_requires
 )
