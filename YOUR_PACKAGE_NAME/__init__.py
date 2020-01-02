"""
    ``$YOUR_PACKAGE_NAME`` module
    ============================

    Use it to import very important functions.

    This package was made for Lorem ipsum dolor sit amet, consectetur adipisicing
    elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
    aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in
    voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
    occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim
    id est laborum.

    :Example:

    >>> from YOUR_PACKAGE_NAME import add
    >>> add(1, 1)
    2

    Package structure
    -----------------

    (Use the tree commande to generate the structure)

    .
    ├── __init__.py
    ├── log  -> A directory that use to log everything in development
    │   └── main.log
    ├── __log.py -> Logger come from here
    ├── main.py -> Main functions care here
    └── tests -> All test file
        ├── __init__.py
        └── test_main.py

    LICENSE: GPLv3+
    For more info please go on <https://github.com/$YOUR_NAME/$YOUR_PACKAGE_NAME>

"""
from .__version__ import *
from .main import add

# All your function that need to be accessible
__all__ = ['add']


