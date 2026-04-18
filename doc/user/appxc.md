<!--Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)-->
<!--SPDX-License-Identifier: 0BSD-->
# APPXC

```{page-status} usable
```

The mission of APPXC is to ***resolve cross-cutting concerns*** like configuration,
data persistence, and security for ***desktop applications*** while
***reducing overhead***. Features and modules are designed to work ***without dedicated
IT operations***.

The sections below explain what APPXC covers, how those concerns interact and further
refines the scope.

:::{admonition} work in progress
:class: info

As of 2026/04, this project is a work in progress. The current focus for `v0.0.4` is
concept clarity. Adding the documentation needed to make available modules easy to use
is pending.

:::
## Cross-Cutting Concerns

APPXC addresses a specific imbalance: in many applications, the effort required to
implement cross-cutting concerns can exceed the effort spent on domain logic. For most
cross-cutting concerns, there are strong existing solutions, and APPXC builds on them.
Examples:
 * logging via [built-in logging](https://docs.python.org/3/library/logging.html)
 * security via [Cryptography](https://cryptography.io/en/latest/)

If these concerns were isolated, handling them early would be enough. In practice, they
interact and create unexpected effort, often dsicovered when the development already
started. The table below shows three concerns and how they can affect each other.

:::{list-table} Concerns (columns) are cutting across concerns (rows)
:widths: 5 15 15 15
:header-rows: 1

*   -
    - Configuration
    - Persistence
    - Security

*   - Configuration
    - Configuration settings may have options. For example, a password may have a
      configurable minimum length.
    - A configuration should be persisted.
    - Passwords should not be displayed in plain text and should only be stored
      securely.

*   - Persistence
    - The application may allow configurable storage locations. If an FTP server is used
      as storage, access must be configured.
    - Persistence can impact itself when additional metadata must be stored with the
      actual data. Examples: timestamps, versions, or author.
    - Storage may have to consider confidentiality via encryption and/or authenticity
      via signing.

*   - Security
    - The configuration may maintain the passwords for services. This includes a secure
      provisioning of passwords to application users.
    - Maintained keys must be persisted, but this cannot rely on the same secure storage
      solution used for any other data (cyclic dependency).
    - As with persistence: maintained cryptographic keys must be persisted *securely*.
:::

APPXC derives an internal architecture to resolve these interdependencies while keeping
the interface to domain logic simple and flexible. Because you can use these components
out of the box, application development can:
* consume less initial effort
* reduce the risk of unexpected effort when discovering one of the
  interdependencies
* improve quality by including cross-cutting concerns from the start

Future options on the advanced side of cross-cutting concerns include:
* given a persistence model that gives APPXC a complete overview of data
  assets, it could realize **backup** functionality.
* given APPXC knows the log files, provides basic email functionality, and can integrate
  into the user interface, it could enable **error reporting**.
* given defined assumptions on application build and runtime in addition to
  security concerns (authenticity) and some remote data access, it could realize the
  **deployment of application updates**.


## Scope

Optimization fails when the target is ambiguous.

APPXC focuses on applications that are not supported by dedicated IT infrastructure,
IT operations, and/or a development team. Typical target users include:
* hobbyist developers, researchers and lecturers
* IT support for associations or small organizations
* (possibly even) departments of large companies where the built application is just an
  internal tool

As a result, APPXC prioritizes:
* **ease of use**, affecting interfaces and documentation
* **compatibility** with commonly available IT infrastructure
* **reliability**, since APPXC may be used as a basis for various applications

APPXC does not exclude professional Python applications. However, these applications are
typically exposed to a competitive environment with higher expectations. Shifting focus
there would:
1. consume effort that would no longer be available for other features
2. significantly change target quality characteristics, potentially creating conflicts

:::{list-table} Differences in quality characteristics for applications within and not within APPXC scope
:widths: 10 15 15
:header-rows: 1

*   - Aspect
    - Application in APPXC Scope
    - Professional Application

*   - IT infrastructure
    - Relying on widely available resources like files, web hosting or email providers
    - Hosting dedicated servers and specialized services

*   - Security
    - Encryption and signing via software modules
    - Single sign-on, isolation via web services and/or enforcing the use of hardware
      security modules

*   - Efficiency
    - Focus on a broad spectrum of use cases with very limited capacity
    - Optimized performance efficiency by reduced scope, stricter assumptions on IT
      infrastructure and high investment in optimization

:::
