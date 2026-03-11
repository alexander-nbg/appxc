# Copyright 2023-2026 the contributors of APPXC (github.com/alexander-nbg/appxc)
# SPDX-License-Identifier: Apache-2.0
"""Facade for APPXC storage module"""
# TODO: See also the TODO remark in pyproject.toml on unused imports.

# isort: skip_file

# Abstract/General Classes
from .serializer import Serializer
from .storable import Storable, AppxcStorableError
from .storage import Storage
from .storage import AppxcStorageError, AppxcStorageWarning

# Serializer Implementations:
from .serializer_raw import RawSerializer
from .serializer_compact import CompactSerializer
from .serializer_json import JsonSerializer
from .storage_to_bytes import StorageToBytes

# Storage Implementations
from .local import LocalStorage

# from .ftp import FtpStorage
from .ram import RamStorage

# Buffer
from .buffer import Buffer, buffered

# Helpers
from .meta_data import MetaData

# Synchronization
from .sync import sync
