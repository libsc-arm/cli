from setuptools import setup, find_packages
from interface.version import LIBSCARM_VERSION

setup(
    name="libscARM",
    version=LIBSCARM_VERSION,
    description="Command line interface for libscARM",
    url="http://github.com/libscARM/cli",
    author="Siva R",
    author_email="sivagrenganathan@protonmail.com",
    packages=find_packages(),
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'guineapig = interface.run:main',
            ],
    },
)
