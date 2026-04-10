<!--Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)-->
<!--SPDX-License-Identifier: 0BSD-->
# Configuration

```{page-status} incomplete
:summary: See section "approach".
```

## Situation
An application quickly has various sets of configuration settings, from user details and
server access to application-specific preferences. Adding them should just be a
definition of what is needed. However, several details typically increase the effort:
 * Protection from wrong entries to ensure valid values
 * A predictable way to find them in the application including ways to display and edit
   them (UI)
 * Storage and, eventually, secure storage of sensitive settings like passwords for
   server access (persistency, security)
 * Shipping configuration settings and maintaining them (data exchange)

**The bottom line**: a configuration setting is not a big thing on its own, but it grows
in complexity due to the impact from other concerns.

## Approach
APPXC introduces a `Setting` class to hold separate values with various predefined types
for integer, string, email or password. The class utilizes a conversion function to
convert an ***original entry*** to a ***valid value***. This separation enables:
 * validity checks
 * displaying the *original entry* in the UI
 * providing only valid values to functions using the setting

A class `SettingDict` is added to maintain sets of configuration settings and a class
`Config` is added to maintain all configuration settings in one object.

:::{admonition} Incomplete
:class: warning

A typical example to set up a configuration, given an application harness, still needs to
be added. Similarly, corresponding modules must be linked.

:::