Overview
========

This repository was create to develop a python package.

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Mattherix/template-python-package/pulls)
[![codecov](https://codecov.io/gh/Mattherix/template-python-package/branch/master/graph/badge.svg)](https://codecov.io/gh/Mattherix/template-python-package)

Added:

* A README.md
* A HISTORY.md to follow the evolution of the project
* A smart setup.py
* A LICENCE (Default licence is GPLv3)
* Some functions/class/unitest templates
* A .gitignore
* Issue/PR templates
* Some github actions:
    * python_package.yml
        * Install dependencies from requiements.txt
        * Check the code with flake8
        * Run pytest
        * Publish the coverage result to [codecov.io](codecov.io)
    * python_publish.yml
        * Post your code to pypi when you release it
    * assignee_to_reviewer.yml
        * Automatically request a review from user A when you assign user A to a pull request
        * Automatically stop requesting a review from user A when you remove user A to the pull request

## How to use it
If you want to use this template just:

1. Click on 'use the template'.
2. Replace the $variable
   1. $project: The name of your project (README.md, HISTORY.md, docs/index.rst, docs/conf.py)
   2. $setup_date: The date of the creation of your project (HISTORY.md)
   3. $YOUR_NAME: Your github username, the one inside your github url (README.md, $YOUR_PACKAGE_NAME/__init__.py, docs/conf.py)
   4. $YOUR_PACKAGE_NAME: The name of your package/repository (README.md, codecov.yml, $YOUR_PACKAGE_NAME/, $YOUR_PACKAGE_NAME/__init__.py)
   5. request: Put the name of your package (README.md)
3. Add PYPI_USERNAME, PYPI_PASSWORD and CODECOV_TOKEN inside github secret (Setting -> Secret)
4. Fill the LICENCE
5. Fill the setup.py
6. Fill the README.md and remove the part before the ...

...
===


<div align="center">

$project
========

![PyPI](https://img.shields.io/pypi/v/request)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/request)
![PyPI - Downloads](https://img.shields.io/pypi/dm/request)
![PyPI - License](https://img.shields.io/pypi/l/request)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/request)
[![codecov](https://codecov.io/gh/$YOUR_NAME/YOUR_PACKAGE_NAME/branch/master/graph/badge.svg?token=7TyKhWhoVI)](https://codecov.io/gh/$YOUR_NAME/YOUR_PACKAGE_NAME)

</div>

A short description of your project

An image

Installation
------------
Using pip

```sh
pip3 install YOUR_PACKAGE_NAME
```

or from github

```sh
pip3 install -e git://github.com/$YOUR_NAME/YOUR_PACKAGE_NAME@latest
```

Usage example
-------------
How can I use your package

```python

```

For more examples and usage, please refer to the [documentation](https://github.com/$YOUR_NAME/YOUR_PACKAGE_NAME/wiki)

Contributor
-----------

- [@Mattherix](https://github.com/Mattherix)

How to contribute
-----------------

1. Fork the project
2. Create your feature branch
3. Commit your changes
4. Test carefully your code
5. Push to the branch
6. Create a new Pull Request
