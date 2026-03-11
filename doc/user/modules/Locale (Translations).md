<!--Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)-->
<!--SPDX-License-Identifier: 0BSD-->
# Locale (Translations)

* General concept explained: https://phrase.com/blog/posts/translate-python-gnu-gettext/
* Context sensitive translations are used: `_(<context>, <string>)`
* GUI (appxc-gui) and normal appxc (if any) should be separated since they will go in different packages
* For testing, LANGUAGE can be set before calling python like:
  `PYTHONPATH=. LANGUAGE=en python tests_features/full_application/manual_user_s2r0.py`