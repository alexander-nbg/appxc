<!--Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)-->
<!--SPDX-License-Identifier: 0BSD-->
# Application Test Harness

```{page-status} draft
:summary: see introduction (2026/03)
```

```{admonition} Draft Status
:class: attention
As long as there is no APPXC v0.1.0, backwards compatibility is not supported. This page is just a stub/draft to prepare concepts while reaching v0.1.0.
```

## Situation

### Application Harness
**Definition.** In APPXC context, an application harness aggregates objects for a basic
application. It ***does*** provide methods for operations on the aggregated objects
while it ***does not*** provide any user interface or enforce behavior more than
initialization.

The __AppHarness__ for testing is stored in `tests/fixtures/app_harness.py`. The
fixtures in `tests/fixtures/application.py` may combine several ApplicationMock
instances. They are prepared and used as follows:
1. The file structure is prepared once for the appxc library version at location:
   `.testing/app_\<context\>_\<appxc version\>`.
2. The prepared folder is copied for the specific test case. The dictionary of the
   fixture contains entries like `app_user` which return an ApplicationMock object. This
   ApplicationMock includes all objects and required paths in context of the
   ApplicationMock.
### Application Harness User Interface
**Definition.** In APPXC context, an application harness user interface just puts a
default user interface on top of an application harness.