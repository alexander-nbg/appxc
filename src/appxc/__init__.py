# Copyright 2023-2026 the contributors of APPXC (github.com/alexander-nbg/appxc)
# SPDX-License-Identifier: Apache-2.0
"""Facade for APPXC basic classes"""
# Basic classes exposed here shall only have dependencies to python builtin
# modules. This facade shall not expose any object from sub-modules. Rationale:
# using APPXC shall not enforce loading of unnecessary dependencies which are
# typically present in sub-modules.

# try:
#     from ._version import __version__ as __version__
# except ImportError:
#     # Package was not installed; version metadata is unknown (e.g. running directly
#     # from source without hatch-vcs build hook execution).
#     __version__: str = "0.0.0.dev0+unknown"

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("package-name")
except PackageNotFoundError:
    # package is not installed
    __version__ = "0.0.0.dev0+unknown"

from .options import Options
from .stateful import Stateful
