<!--Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)-->
<!--SPDX-License-Identifier: 0BSD-->
# User Interface

:::{page-status} incomplete
:summary: to be updated for v0.0.4 for UI abstraction (2026/04)
:::

## Overview

### Situation

User interfaces are cross-cutting concerns that also cut across APPXC features such that
***a user interface must be provided***. However, user interfaces are susceptible to
***heavy customization*** conflicting with the APPXC scope to enable easy application
creation.

### Approach
The APPXC core will (feature is pending) realize features based on a command-line
interface (CLI) to enable lightweight executables and automated feature testing.

A GUI implementation based on [tkinter](https://docs.python.org/3/library/tkinter.html)
is provided for all features while adding a lightweight framework approach (feature is
pending) focusing on easy application creation.

To enable customization of user interfaces, features will define abstract UI classes as
interface contracts, separating feature function from UI (feature is pending) and enabling full UI customization.

## Notes
### Tkinter
Since APPXC aims for easy application creation, a quick learning curve is essential such
that [tkinter](https://docs.python.org/3/library/tkinter.html) was chosen as the basis
(see also: [pythonguis.com](https://www.pythonguis.com/faq/pyqt-vs-tkinter/)).