#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path
import subprocess

pkg_name = "workflow_calcium_imaging"
here = path.abspath(path.dirname(__file__))

long_description = """"
# Calcium Imaging Workflow with CaImAn for CCN2023.

Build a complete imaging workflow using the DataJoint elements
+ [element-lab](https://github.com/datajoint/element-lab)
+ [element-animal](https://github.com/datajoint/element-animal)
+ [element-session](https://github.com/datajoint/element-session)
+ [element-calcium-imaging](https://github.com/datajoint/element-calcium-imaging)
"""

with open(path.join(here, "requirements.txt")) as f:
    requirements = f.read().splitlines()

with open(path.join(here, pkg_name, "version.py")) as f:
    exec(f.read())

subprocess.call(["pip", "install", "numpy", "Cython"])
extras_require = {
    "caiman": "caiman @ git+https://github.com/datajoint-company/CaImAn.git"
}

setup(
    name="workflow-calcium-imaging",
    version=__version__,
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
    extras_require=extras_require,
)
