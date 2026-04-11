<!--Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)-->
<!--SPDX-License-Identifier: 0BSD-->
# Documentation: User Pages

```{page-status} incomplete
:summary: page reflects current clarity on feature and module pages (2026/04)
```

## Feature Pages
The intent of feature pages is to raise awareness on the concerns which typically arise
for applications and ***explain*** the *general* approach taken in APPXC. The pages
***must be concise*** and ***must not be technical***.

### Header
:::{admonition} to be refined
:class: warning

Despite the page status, we may use sphinx needs to model feature data elements with
reusable short descriptions, a status and links to required modules. The feature status
shall be clearly visible.

:::

### Situation (mandatory)
Highlighting a typical problem arising for application development. The first paragraph
should focus on the core of the problem, further details may be added to a listing in a
further paragraph, if needed.

### Approach (mandatory)
Outlining the approach from a top level and linking to related modules.

:::{admonition} not yet realized
:class: warning


As of 2026/04, no feature is referencing any implementation module since no
implementation module page is added, yet.

:::

### Alternatives (optional)
If there are typical alternatives to the approach, they can be outlined and commented
here. The [Login](/user/features/user-access/login) is using this subsection.

### FAQ (optional)
Especially, if the approach is complex, it is reasonable to add this FAQ section to
clarify potentially open questions while keepting the **approach** section concise. The
[Registration](/user/features/user-access/registration) page uses an FAQ section.

### References

:::{admonition} idea
:class: info

As of 2026/04, this section is just an idea based on sphinx-need capabilities. Given
linkage between features and modules and corresponding state information, this section
could easily list all relevant modules including their state and short description.
Furthermore, this section could list corresponding draft pages (feature+module).

:::


## Module Pages

:::{admonition} to be refined
:class: warning

As of 2026/04, there is no serious module page existing to condense a general guideline.

:::