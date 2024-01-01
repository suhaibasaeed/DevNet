from setuptools import setup, find_packages
import os
import re

with open("requirements.txt", "r") as fs:
    requirements = [r for r in fs.read().splitlines() if (len(r) > 0 and not r.startswith("#"))]


def find_version(*file_paths):
    """
    This pattern was modeled on a method from the Python Packaging User Guide:
        https://packaging.python.org/en/latest/single_source_version.html
    We read instead of importing so we don't get import errors if our code
    imports from dependencies listed in install_requires.
    """
    base_module_file = os.path.join(*file_paths)
    with open(base_module_file) as f:
        base_module_data = f.read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", base_module_data, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="net-inventory",
    version=find_version("net_inventory", "__init__.py"),
    description="A Flask framework, made for quickly deploying flask applications within Network to Code",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        "Topic :: Utilities",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: POSIX :: Linux",
    ],
    keywords=["flask", "framework"],
)
