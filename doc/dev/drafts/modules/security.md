<!--Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)-->
<!--SPDX-License-Identifier: 0BSD-->
# Security

:::{page-status} draft
:summary: dropping old documentation parts for refinement (2026/04)
:::

## Old Security Documentation

:::{admonition} To be updated and refined
:class: warning

The samples in this section are old and likely not up to date. However, their intend is
valid. The conent should be refined.

:::

Usage can be as simple as the following. Note that login and registration both requiere
a appxc configuration object (see TBD):
```python
from appxc import config, login, registration

# You should always use your own salt for your tool but never change it, unless
# you want user passwords to become invalid.
security = Security(salt = 'PickYourOwnSaltForYourApplication!')

login = Login(security)
login.check()
# Note: If login procedure fails (password not correct), code will end here
# with an exception.

# Login is required before registration, but registration is optional.
registration = Registration(security)
registration.check()
# Note: Like with login, code will end with an Exception if registration check
# failed.

# After this step, securily stored data can be loaded (like Config section
# (see link TBD))
```
### Login
Without a gui, this could be like
```python
from appxc.security.local import Security

# You need to get the password input from somewhere, appxc does not support a
# command line helper.
pwd = ''

# You need to create a security context. You should define __your salt string__
# for __your application__. You __can__ change the storage for the security
# module.
security = Security(salt = 'PickYourOwnSaltForYourApplication!', storage = './data/security')

# If not yet initialized, you take the initial password to setup the security
# context. There won't be any data stored, so no further check needed.
if security.is_user_initialized():
	security.unlock_user(pwd)
# The above will throw an exception if the password is not correct.
else:
	security.init_user(pwd)
# There is no need to provide the password anymore. The user will be
# unlocked.
```

Dropping images:
`![login](securityLogin.png)`