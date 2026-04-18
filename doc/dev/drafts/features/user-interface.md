<!--Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)-->
<!--SPDX-License-Identifier: 0BSD-->
# User Interface


```{page-status} draft
:summary: created to support concept clarity (2024/04)
```

## Situation (UI)
The user interface of an applciation is a cross-cutting concern which is extremely
sensitive to customization. Different expectations start with *command-line interface
versus graphical user interface*, continued by *tkinter versus Qt* (plus others) and do
not end by the approaches and options within any UI library. This results in a conflict:
1) APPXC cannot ignore the user interface as cross-cutting concern while..
2) ..providing or supporting only one UI solution would render APPXC not suitable for a
   higher number of use cases.

+ localization

## Approach