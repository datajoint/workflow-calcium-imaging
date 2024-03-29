#!/usr/bin/env python
from os import path

from setuptools import find_packages, setup

pkg_name = "workflow_calcium_imaging"
here = path.abspath(path.dirname(__file__))

long_description = """"
# Workflow for calcium imaging data acquired with ScanImage, Scanbox, or Nikon NIS software and analyzed with Suite2p or CaImAn.

Build a complete imaging workflow using the DataJoint elements
+ [element-lab](https://github.com/datajoint/element-lab)
+ [element-animal](https://github.com/datajoint/element-animal)
+ [element-session](https://github.com/datajoint/element-session)
+ [element-event](https://github.com/datajoint/element-event)
+ [element-calcium-imaging](https://github.com/datajoint/element-calcium-imaging)
"""

with open(path.join(here, "requirements.txt")) as f:
    requirements = f.read().splitlines()

with open(path.join(here, pkg_name, "version.py")) as f:
    exec(f.read())

setup(
    name="workflow-calcium-imaging",
    version=__version__,  # noqa: F821
    description="Calcium imaging workflow using the DataJoint elements",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="DataJoint",
    author_email="info@datajoint.com",
    license="MIT",
    url="https://github.com/datajoint/workflow-calcium-imaging",
    keywords="neuroscience datajoint calcium-imaging",
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    install_requires=requirements,
)
