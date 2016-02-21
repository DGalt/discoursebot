try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Twitter bot to combat online ignorance',
    'author': 'Kevin',
    'url': 'https://github.com/kevinpuj/discoursebot.',
    'download_url': 'https://github.com/kevinpuj/discoursebot',
    'author_email': 'kevinpuj at gmail',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)