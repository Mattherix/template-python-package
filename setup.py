"""Setup file"""
from typing import Tuple, List

from setuptools import setup, find_packages
import glob

package_name = glob.glob('./*/__init__.py')[0]
package_name = package_name.replace('./', '')
package_name = package_name.replace('/__init__.py', '')

PACKAGE_NAME = package_name  # The name of the package
VERSION = '0.0.1'
PYTHON_VERSION = '~=3.6'  # Any python 3 version since python3.6
SHORT_DESCRIPTION = ''
DESCRIPTION = open('README.md').read()
AUTHOR = ''
MAIL = ''
PROJECT_URL = 'https://github.com/$url_name/$project@latest'
LICENCE = 'GPLv3+'
DEVELOPMENT_STATUS = 'Planning'
ENVIRONMENT = []
FRAMEWORK = []
AUDIENCE = ['Developers']
PROGRAMMING_LANGUAGE = ['Pythonv3.6', 'Pythonv3.7', 'Pythonv3.8']
KEYWORDS = ['test', 'test2']

# To add more classifier, like topic go on <https://pypi.org/pypi?action=list_classifiers>
classifiers = []

LICENCE_CLASSIFIER = {
    'GPLv3+': 'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Apache': 'License :: OSI Approved :: Apache Software License',
    'MIT': 'License :: OSI Approved :: MIT License',

    'GPL': 'License :: OSI Approved :: GNU General Public License (GPL)',
    'GPLv2': 'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
    'GPLv2+': 'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
    'GPLv3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
}

DEVELOPMENT_STATUS_CLASSIFIER = {
    'Planning': 'Development Status :: 1 - Planning',
    'Pre-Alpha': 'Development Status :: 2 - Pre-Alpha',
    'Alpha': 'Development Status :: 3 - Alpha',
    'Beta': 'Development Status :: 4 - Beta',
    'Production/Stable': 'Development Status :: 5 - Production/Stable',
    'Mature': 'Development Status :: 6 - Mature',
    'Inactive': 'Development Status :: 7 - Inactive'
}

ENVIRONMENT_CLASSIFIER = {
    'Console': 'Environment :: Console',
    'MacOS X': 'Environment :: MacOS X',
    'Daemon': 'Environment :: No Input/Output',
    'Other Environment': 'Environment :: Other Environment',
    'Plugins': 'Environment :: Plugins',
    'Web': 'Environment :: Web Environment',
    'Windows': 'Environment :: Win32 (MS Windows)',
    'Gnome': 'Environment :: X11 Applications :: Gnome',
    'GTK': 'Environment :: X11 Applications :: GTK',
    'KDE': 'Environment :: X11 Applications :: KDE',
    'Qt': 'Environment :: X11 Applications :: Qt'
}

FRAMEWORK_CLASSIFIER = {
    'AiiDA': 'Framework :: AiiDA',
    'AsyncIO': 'Framework :: AsyncIO',
    'BEAT': 'Framework :: BEAT',
    'BFG': 'Framework :: BFG',
    'Bob': 'Framework :: Bob',
    'Bottle': 'Framework :: Bottle',
    'CastleCMS': 'Framework :: CastleCMS',
    'Chandler': 'Framework :: Chandler',
    'CherryPy': 'Framework :: CherryPy',
    'CubicWeb': 'Framework :: CubicWeb',
    'Dash': 'Framework :: Dash',
    'Django': 'Framework :: Django',
    'Djangov1.10': 'Framework :: Django :: 1.10',
    'Djangov1.11': 'Framework :: Django :: 1.11',
    'Djangov1.4': 'Framework :: Django :: 1.4',
    'Djangov1.5': 'Framework :: Django :: 1.5',
    'Djangov1.6': 'Framework :: Django :: 1.6',
    'Djangov1.7': 'Framework :: Django :: 1.7',
    'Djangov1.8': 'Framework :: Django :: 1.8',
    'Djangov1.9': 'Framework :: Django :: 1.9',
    'Djangov2.0': 'Framework :: Django :: 2.0',
    'Djangov2.1': 'Framework :: Django :: 2.1',
    'Djangov2.2': 'Framework :: Django :: 2.2',
    'Djangov3.0': 'Framework :: Django :: 3.0',
    'Django CMS': 'Framework :: Django CMS',
    'Django CMSv3.4': 'Framework :: Django CMS :: 3.4',
    'Django CMSv3.5': 'Framework :: Django CMS :: 3.5',
    'Django CMSv3.6': 'Framework :: Django CMS :: 3.6',
    'Django CMSv3.7': 'Framework :: Django CMS :: 3.7',
    'Flake8': 'Framework :: Flake8',
    'Flask': 'Framework :: Flask',
    'Hypothesis': 'Framework :: Hypothesis',
    'IDLE': 'Framework :: IDLE',
    'IPython': 'Framework :: IPython',
    'Jupyter': 'Framework :: Jupyter',
    'Lektor': 'Framework :: Lektor',
    'Masonite': 'Framework :: Masonite',
    'Nengo': 'Framework :: Nengo',
    'Odoo': 'Framework :: Odoo',
    'Opps': 'Framework :: Opps',
    'Paste': 'Framework :: Paste',
    'Pelican': 'Framework :: Pelican',
    'Plone': 'Framework :: Plone',
    'Plonev3.2': 'Framework :: Plone :: 3.2',
    'Plonev3.3': 'Framework :: Plone :: 3.3',
    'Plonev4.0': 'Framework :: Plone :: 4.0',
    'Plonev4.1': 'Framework :: Plone :: 4.1',
    'Plonev4.2': 'Framework :: Plone :: 4.2',
    'Plonev4.3': 'Framework :: Plone :: 4.3',
    'Plonev5.0': 'Framework :: Plone :: 5.0',
    'Plonev5.1': 'Framework :: Plone :: 5.1',
    'Plonev5.2': 'Framework :: Plone :: 5.2',
    'Plonev5.3': 'Framework :: Plone :: 5.3',
    'Plone Addon': 'Framework :: Plone :: Addon',
    'Plone Core': 'Framework :: Plone :: Core',
    'Plone Theme': 'Framework :: Plone :: Theme',
    'Pylons': 'Framework :: Pylons',
    'Pyramid': 'Framework :: Pyramid',
    'Pytest': 'Framework :: Pytest',
    'Review Board': 'Framework :: Review Board',
    'Scrapy': 'Framework :: Scrapy',
    'Setuptools Plugin': 'Framework :: Setuptools Plugin',
    'Sphinx': 'Framework :: Sphinx',
    'Sphinx Extension': 'Framework :: Sphinx :: Extension',
    'Sphinx Theme': 'Framework :: Sphinx :: Theme',
    'tox': 'Framework :: tox',
    'Trac': 'Framework :: Trac',
    'Trio': 'Framework :: Trio',
    'Tryton': 'Framework :: Tryton',
    'TurboGears': 'Framework :: TurboGears',
    'TurboGears Applications': 'Framework :: TurboGears :: Applications',
    'Wagtail': 'Framework :: Wagtail',
    'Wagtailv1': 'Framework :: Wagtail :: 1',
    'Wagtailv2': 'Framework :: Wagtail :: 2'
}

AUDIENCE_CLASSIFIER = {
    'Customer Service': 'Intended Audience :: Customer Service',
    'Developers': 'Intended Audience :: Developers',
    'Education': 'Intended Audience :: Education',
    'End Users/Desktop': 'Intended Audience :: End Users/Desktop',
    'Financial and Insurance Industry': 'Intended Audience :: Financial and Insurance Industry',
    'Healthcare Industry': 'Intended Audience :: Healthcare Industry',
    'Information Technology': 'Intended Audience :: Information Technology',
    'Legal Industry': 'Intended Audience :: Legal Industry',
    'Manufacturing': 'Intended Audience :: Manufacturing',
    'Religion': 'Intended Audience :: Religion',
    'Science/Research': 'Intended Audience :: Science/Research',
    'System Administrators': 'Intended Audience :: System Administrators',
    'Telecommunications Industry': 'Intended Audience :: Telecommunications Industry',
    'Other Audience': 'Intended Audience :: Other Audience'
}

PROGRAMMING_LANGUAGE_CLASSIFIER = {
    'Assembly': 'Programming Language :: Assembly',
    'C': 'Programming Language :: C',
    'C#': 'Programming Language :: C#',
    'C++': 'Programming Language :: C++',
    'Cython': 'Programming Language :: Cython',
    'Java': 'Programming Language :: Java',
    'JavaScript': 'Programming Language :: JavaScript',
    'Objective C': 'Programming Language :: Objective C',
    'Pascal': 'Programming Language :: Pascal',
    'Perl': 'Programming Language :: Perl',
    'PHP': 'Programming Language :: PHP',
    'Python': 'Programming Language :: Python',
    'Pythonv2': 'Programming Language :: Python :: 2',
    'Pythonv2.3': 'Programming Language :: Python :: 2.3',
    'Pythonv2.4': 'Programming Language :: Python :: 2.4',
    'Pythonv2.5': 'Programming Language :: Python :: 2.5',
    'Pythonv2.6': 'Programming Language :: Python :: 2.6',
    'Pythonv2.7': 'Programming Language :: Python :: 2.7',
    'Pythonv2 Only': 'Programming Language :: Python :: 2 :: Only',
    'Pythonv3': 'Programming Language :: Python :: 3',
    'Pythonv3.0': 'Programming Language :: Python :: 3.0',
    'Pythonv3.1': 'Programming Language :: Python :: 3.1',
    'Pythonv3.2': 'Programming Language :: Python :: 3.2',
    'Pythonv3.3': 'Programming Language :: Python :: 3.3',
    'Pythonv3.4': 'Programming Language :: Python :: 3.4',
    'Pythonv3.5': 'Programming Language :: Python :: 3.5',
    'Pythonv3.6': 'Programming Language :: Python :: 3.6',
    'Pythonv3.7': 'Programming Language :: Python :: 3.7',
    'Pythonv3.8': 'Programming Language :: Python :: 3.8',
    'Pythonv3.9': 'Programming Language :: Python :: 3.9',
    'Pythonv3 Only': 'Programming Language :: Python :: 3 :: Only',
    'IronPython': 'Programming Language :: Python :: Implementation :: IronPython',
    'Jython': 'Programming Language :: Python :: Implementation :: Jython',
    'MicroPython': 'Programming Language :: Python :: Implementation :: MicroPython',
    'PyPy': 'Programming Language :: Python :: Implementation :: PyPy',
    'Stackless': 'Programming Language :: Python :: Implementation :: Stackless',
    'R': 'Programming Language :: R',
    'Ruby': 'Programming Language :: Ruby',
    'Rust': 'Programming Language :: Rust',
    'SQL': 'Programming Language :: SQL',
    'Unix Shell': 'Programming Language :: Unix Shell',
    'Visual Basic': 'Programming Language :: Visual Basic'
}

classifiers.append(LICENCE_CLASSIFIER[LICENCE])
classifiers.append(DEVELOPMENT_STATUS_CLASSIFIER[DEVELOPMENT_STATUS])
classifiers = classifiers + [ENVIRONMENT_CLASSIFIER[classifier] for classifier in ENVIRONMENT]
classifiers = classifiers + [FRAMEWORK_CLASSIFIER[classifier] for classifier in FRAMEWORK]
classifiers = classifiers + [AUDIENCE_CLASSIFIER[classifier] for classifier in AUDIENCE]
classifiers = classifiers + [PROGRAMMING_LANGUAGE_CLASSIFIER[classifier] for classifier in PROGRAMMING_LANGUAGE]

while '' in classifiers:
    classifiers.remove('')


def get_requirements(filename: str) -> Tuple[List[str], List[str]]:
    """Get requirements and dependency from a file (like 'requirements.txt')

    This return the requirement and link to python package from a file formats for pip.
    You will want to use this function to make a bridge between a requirements.txt and
    setup.py

    :Example:

    >>> get_requirements('requirements.txt')
    (['test', 'nine'], ['git://github.com/psf/request/#egg=request'])

    :param filename: The path to the file
    :type filename: str
    :return: The list of requirements and a list of dependency
    :rtype: Tuple[List[str], List[str]]
    """
    requirements = open(filename, 'r').read().splitlines()

    install_requires = []
    dependency_links = []
    for requirement in requirements:
        if requirements[0] == '#':
            # It's a comment
            pass
        elif requirement[0:11] == '--index-url':
            # We are on a private pypi
            dependency_links.append(requirement[12:])
        elif requirement[0:2] == '-e':
            # The requirement use a version control systems
            dependency_links.append(requirement[3:])
        elif requirement[0:2] == '-r':
            # A link to an other file
            new_install_requires, new_dependency_links = get_requirements(requirement[3:])
            install_requires = install_requires + new_install_requires
            dependency_links = dependency_links + new_dependency_links
        else:
            install_requires.append(requirement)
    return install_requires, dependency_links


install_requires, dependency_links = get_requirements('requirements.txt')

# For more info see <https://python-packaging.readthedocs.io/en/latest/metadata.html>
setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=SHORT_DESCRIPTION,
    long_description=DESCRIPTION,
    long_description_content_type='text/markdown',
    classifiers=classifiers,
    keywords=' '.join(KEYWORDS),
    url=PROJECT_URL,
    author=AUTHOR,
    author_email=MAIL,
    license=LICENCE,
    python_requires=PYTHON_VERSION,
    packages=find_packages(),
    install_requires=install_requires,
    dependency_links=dependency_links,
    include_package_data=True,
    zip_safe=False
)
