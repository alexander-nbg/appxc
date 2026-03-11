# Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)
# SPDX-License-Identifier: Apache-2.0
"""Translation setup for APPXC GUI modules"""

import gettext
import importlib.resources

# Translation setup. No language is defined in translation() to apply the
# system language by default.
_translation = gettext.translation(
    domain="appxc-gui",
    localedir=str(importlib.resources.files("appxc") / "locale"),
    fallback=True,
)

# Export the pgettext function as _ for context-aware translations
_ = _translation.pgettext
# Also export other useful translation functions if needed
ngettext = _translation.ngettext
