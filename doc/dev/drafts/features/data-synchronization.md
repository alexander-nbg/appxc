<!--Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)-->
<!--SPDX-License-Identifier: 0BSD-->
# Data Synchronization

```{page-status} draft
created to drop thoughts on limitations (2026/04)
```

# Limitations
The following limitations should be reviewed and updated after feature creation and
potentially added to the user space documentation. The limitations represent a draft and
numbers are very variable.

**Data exchange** with other instances is based on one or a few (like 3) people having
writing rights while more (like 50) are just consuming the results.
* See security feature: you essentially give away your email or database passwords to
  the people with writing rights.
* **Update frequency** is expected to be around 20 times a week, and rare (once a month)
  peak reads are around 150 times/h.
* Methods provided to exchange data are not suited for continuous data exchange between
  instances.