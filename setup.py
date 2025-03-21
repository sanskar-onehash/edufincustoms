from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in edufincustoms/__init__.py
from edufincustoms import __version__ as version

setup(
	name="edufincustoms",
	version=version,
	description="customs",
	author="Abhi",
	author_email="abhishek.c@onehash.ai",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
