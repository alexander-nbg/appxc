# Copyright 2024-2026 the contributors of APPXC (github.com/alexander-nbg/appxc)
# SPDX-License-Identifier: Apache-2.0
"""Storable user ID"""

from appxc.storage import Storable, Storage


class AppxcUserIdError(Exception):
    """Load/Store error for user ID"""


class UserId(Storable):
    """Storable user ID"""

    def __init__(self, storage_method: Storage, **kwargs):
        super().__init__(storage_method, **kwargs)
        self._id: int = -1

    @property
    def user_id(self):
        """The USER ID

        Will be loaded from file if not yet done. Throws error
        AppxcErrorUserId if file does not exist.
        """
        # error if still unloaded
        if self._id < 0 and not self._storage.exists():
            raise AppxcUserIdError("Cannot access USER ID: not yet written")
        # ensure loaded
        if self._id < 0:
            self.load()
        return self._id

    @user_id.setter
    def user_id(self, user_id: int):
        self._id = user_id
        self.store()

    def set_state(self, data: bytes):
        self._id = int.from_bytes(data, "big", signed=False)

    def get_state(self) -> bytes:
        return self._id.to_bytes(2, "big", signed=False)
