# Copyright 2025-2026 the contributors of APPXC (github.com/alexander-nbg/appxc)
# SPDX-License-Identifier: Apache-2.0
"""Test utilities for projects using APPXC

Install with: pip install appxc[test]
"""

from appxc.testing.sandbox import (
    sandbox_for_caller_module,
    sandbox_from_fixture,
    sandbox_root,
)

__all__ = [
    "sandbox_for_caller_module",
    "sandbox_from_fixture",
    "sandbox_root",
]
