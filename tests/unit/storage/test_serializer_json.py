# Copyright 2025-2026 the contributors of APPXC (github.com/alexander-nbg/appxc)
# SPDX-License-Identifier: Apache-2.0
"""Test all serializer classes"""

from appxc.storage import JsonSerializer, Serializer
from tests.unit.storage.test_serializer_base import BaseSerializerTest


class TestJsonSerializer(BaseSerializerTest):
    def _get_serializer(self) -> Serializer:
        return JsonSerializer()
