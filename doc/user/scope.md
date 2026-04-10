<!--Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)-->
<!--SPDX-License-Identifier: 0BSD-->
# Scope

```{page-status} draft
:summary: text just taken over from an old README (2026/03)
```

The APPXC library covers cross-cutting concerns like configuration, data persistence,
logging, and security to limit the effort of writing simple applications.

Solutions to cross-cutting concerns have a strong impact on non-functional
requirements, and vice versa. The following list was compiled to allow a quick
decision on whether this toolbox is for you and to guide its development.
Provided numbers only provide a rough idea.
 * The toolbox aims for **easy application creation**. This includes simple to use
   interfaces and the need for documentation and examples.
 * Supported are **desktop applications** which are **shared with a limited number of
   people** (like: 50).
   * Not suited for online applications.
   * Does not aim to scale for 1000 or more users.
 * **Data exchange** with other instances is based on one or a few (like 3) people
   having writing rights while more (like 50) are just consuming the results.
   * See security section: you essentially give away your email or database passwords to the people with writing rights.
   * **Update frequency** is expected to be around 20 times a week, and rare (once a month) peak reads are around 150 times/h.
   * Methods provided to exchange data are not suited for continuous data exchange between instances.