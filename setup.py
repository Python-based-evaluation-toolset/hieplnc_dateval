from setuptools import setup, find_packages

from hieplnc_dateval import __version__

setup(
    name='hieplnc_dateval',
    version=__version__,

    url=None,
    author='LE Nhu Chu Hiep',
    author_email='lenhuchuhiep99@gmail.com',

    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'txt2csv=hieplnc_dateval.txt2csv:txt2csv',
        ],
    },
)