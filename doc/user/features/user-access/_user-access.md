<!--Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)-->
<!--SPDX-License-Identifier: 0BSD-->
# User Access

```{page-status} usable
Mostly usable but needs final review when pages are complete (2026/04)
```

User access focuses on the secure access to application data. The [login](login)
procedure is required to access locally stored data. The [registration](registration)
procedure is required to access data shared between applications.

The above-mentioned procedures are visible to the application user while the actual data
exchange between application instances remains seamless. It requires two more features.
The [data synchronization](data-synchronization) requires knowledge of users and their roles
from the [user registry](user-registry). To set up new users in the user registry, the
**registration** procedure is required and to store the database securely,
the **secure storage** enabled via **login** is required.

```{plantuml} user-access.puml
```

```{toctree}
:maxdepth: 1
:titlesonly:
:hidden:
:glob:

login
registration
data-synchronization
user-registry
security-limitations
```
