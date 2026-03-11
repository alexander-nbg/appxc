# Copyright 2023-2026 the contributors of APPXC (github.com/alexander-nbg/appxc)
# SPDX-License-Identifier: Apache-2.0
"""
__Resizing:__ should only affect the right entry part.

__Validation:__ This entry is for a boolean. Latest after loosing focus on
entry, wrong values *must* turn the entry red.
"""

from appxc.gui import SettingFrameDefault
from appxc.setting import SettingBool
from appxc_matema.case_runner import ManualCaseRunner

prop = SettingBool(name="bool")

ManualCaseRunner().run(SettingFrameDefault, prop)
