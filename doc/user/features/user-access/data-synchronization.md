<!--Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)-->
<!--SPDX-License-Identifier: 0BSD-->
# Data Synchronization

```{page-status} incomplete
The feature is outlined but cannot be detailed without implementation (2026/04)
```

## Situation
You collaborate with others via an application and just updated some data for them. Now,
it needs to be synchronized securely. They may currently not be online to receive data
directly.

This situation has a few more considerations, some of them originating from security
concerns:
* There may be groups of users which do not need the data and you don't want to
  synchronize with everyone.
* New incoming data should be trustworthy.
* When to synchronize and which storage to use as an exchange is decided by the
  application.

## Approach
The synchronization is set up against two storage locations (see [storage
concept](../storage-concept)). Each storage location has a default setting on which
roles are permitted to write and read data which can be overwritten by each storage
within the location. The role definitions are according to the [user
registry](user-registry).

:::{admonition} No Implementation
:class: attention
This feature is not yet implemented.
:::