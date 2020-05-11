# =============================================================================
# setup.py for OpenOPC
# 2020-05-11
# John Ladasky
#
# Code refactoring guide:
# https://gehrcke.de/2014/02/distributing-a-python-command-line-application/
#
# Changes:
# - The OpenOPC version number master copy is placed here, and will be
#   copied to any other files in the package that need it.
# - Added SystemHealth to the py_modules list.  The initial search
#   for NT-type operating systems in OpenOPC.py never succeeded because
#   SystemHealth could not be found.  Was this a relic of Python2-style
#   imports?
#  - WORK IN PROGRESS: making opc.py into a script that installs
#   automatically (cross-platform, although for OpenOPC there may
#   be no functionality in a non-Windows environment?)  Reference: 
#   https://setuptools.readthedocs.io/en/latest/setuptools.html#automatic-script-creation
# - UNRESOLVED ISSUE: what to do with SystemHealth, which is treated as a
#   separate module and not as a component of OpenOPC?
# =============================================================================

OPENOPC_VERSION = "1.3.2.dev2"

# =============================================================================

from setuptools import setup

# =============================================================================

# Copy OPENOPC_VERSION from here to everywhere it needs to go
_openopc = ("src/OpenOPC.py", "__version__ = ", '"{}"\n')
_changes = ("./CHANGES.txt", "OpenOPC for Python ", "{}\n")
for path, pattern, fmt in (_openopc, _changes):
    with open(path, "r") as f:
        lines = f.readlines()
    with open(path, "w") as f:
        for line in lines:
            if line.startswith(pattern):
                line = pattern + fmt.format(OPENOPC_VERSION)
            f.write(line)

entry_points = {"console_scripts": ["opc = _opc:main"]}

setup(
    description = "OPC (OLE for Process Control) toolkit for Python 3.x",
    install_requires = ["Pyro4>=4.61"],
    keywords = "python, opc, openopc",
    license = "GPLv2",
    maintainer = "John Ladasky",
    maintainer_email = "john.ladasky@gmail.com",
    name = "OpenOPC-Python3x",
    package_dir = {"":"src"},
    py_modules = ["OpenOPC","SystemHealth","_opc"],
    url = "https://github.com/bwllc/openopc",
    version = OPENOPC_VERSION,
    entry_points = entry_points
    )