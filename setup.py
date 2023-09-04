#  Created by Martin Strohalm

from setuptools import setup, find_packages

# get version
version = '0.4.0'

# get description
with open("README.md", "r") as fh:
    long_description = fh.read()

# include additional files
package_data = {}

# set classifiers
classifiers = [
    'Development Status :: 3 - Alpha',
    'Programming Language :: Python :: 3 :: Only',
    'Operating System :: OS Independent',
    'Topic :: Utilities',
    'Intended Audience :: Other Audience']

# main setup
setup(
    name = 'rebrick',
    version = version,
    description = 'Python access to Rebrickable API.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/xxao/rebrick',
    author = 'Martin Strohalm',
    author_email = '',
    license = 'MIT',
    packages = find_packages(),
    package_data = package_data,
    classifiers = classifiers,
    install_requires = [],
    zip_safe = False)
