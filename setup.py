# ======================================================================
# setup.py for OpenOPC
# 2020-05-08
# John Ladasky
# ======================================================================

from setuptools import setup

setup(
    description = "OPC (OLE for Process Control) toolkit for Python 3.x",
    install_requires = ["Pyro4>=4.61"],
    keywords = "python, opc, openopc",
    license = "GPLv2",
    maintainer = "John Ladasky",
    maintainer_email = "john.ladasky@gmail.com",
    name = "OpenOPC-Python3x",
    package_dir = {"":"src"},
    py_modules = ["OpenOPC","SystemHealth"],
    url = "https://github.com/bwllc/openopc",
    version = "1.3.2.dev1"
    )