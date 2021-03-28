import os
import re

import setuptools


HERE = os.path.abspath(os.path.dirname(__file__))

VERSION_PY = ["src", "bpp_speech", "version.py"]


def read(*args):
    """Read complete file contents."""
    with open(os.path.join(HERE, *args)) as fh:
        return fh.read()


def get_version():
    """Parse version from the file."""
    version_file = read(*VERSION_PY)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file,
        re.M,
    )
    if version_match:
        return version_match.group(1)

    raise RuntimeError("Unable to find version string.")


setuptools.setup(
    version=get_version()
)
