# Copyright 2024-2026 the contributors of APPXF (github.com/alexander-nbg/appxf)
# SPDX-License-Identifier: Apache-2.0
"""Class definitions for storage handling."""

from abc import ABC, abstractmethod

# TODO: serializers have a usage problem. Typically, the data is serialized in one
# function and deserialized in another where the serializer returns generic objects as
# type, breaking type hints. In classes using the serializer directly, the class could
# hold a type-aware serializer. For situations of indirect usage, like in Storage, the
# pattern could apply likewise but to the storage class. -- While the above is only for
# type hints, actual type checks may also be appropriate.


class Serializer(ABC):
    """Provide serialize and deserialize functionality"""

    @classmethod
    @abstractmethod
    def serialize(cls, data: object) -> bytes:
        """Provide bytes from python object

        Consider include a version number in your object data in case
        you change your stored data format later.
        """

    @classmethod
    @abstractmethod
    def deserialize(cls, data: bytes) -> object:
        """Restore Python object from bytes

        Consider include a version number in your object data in case
        you change your stored data format later.
        """
