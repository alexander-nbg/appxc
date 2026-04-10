<!--Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)-->
<!--SPDX-License-Identifier: 0BSD-->
# User Registry

```{page-status} incomplete
The feature is outlined but cannot be detailed without complete implementation (2026/04)
```

The user registry maintains users, their roles, and user details.

## Situation
If an application shares information with other instances, it must know which *others*
exist. To maintain security, *others* should authenticate themselves and data should only
be provided to authorized *others*. Additionally, users *may* want to know details
about the others.

Connected features:
* The [registration procedure](registration) is required to set up new users.
* [Data synchronization](data-synchronization) is handled separately.

## Approach

To be described.

:::{admonition} Implementation Incomplete
:class: warning

The current implementation only maintains user public keys for signing and encryption.
No user details are shared. Maintaining roles is very limited. In particular, due to the
missing data synchronization, there is ***no automatic synchronization of the use
registry***.

:::

## FAQ
### How is the user registry updated?
If the admin removes a user or changes roles, the user registry will be uploaded to the
remote location automatically. During startup of the application, as part of the user
registration check, the user registry will be updated before this check.
### Can users' rights be revoked?
You can remove a user. Without cleanup, the user-id will remain blocked. You can add or
remove roles from a user. At least one role must remain. Access permissions will be
forwarded accordingly. Please be aware of the [security
limitations](security-limitations).
### What happens if a user loses their data?
If the application data is lost or corrupted, the user just needs to re-register with a
fresh application. Shared data will be available again after registration. Since APPXC
defines the user-id and the user's public key as identification data, the user will get a
*new* entry in the user registry.

A manual mapping to the old user ID is not supported since the added complexity does not
seem to match the benefit.