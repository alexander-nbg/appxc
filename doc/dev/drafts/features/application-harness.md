<!--Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)-->
<!--SPDX-License-Identifier: 0BSD-->
# Application Harness


```{page-status} draft
:summary: created to support concept clarity (2024/04)
```

## Situation (UI)
There are a number of APPXC objects involved to cover cross functional concerns leading
to ***repeated code patterns***:
1) the objects must be initialized in a ceratin order due to their dependencies
1) [login](/user/features/user-access/login) and
   [registration](/user/features/user-access/registration) are common procedures

To be refined:
 * (??) common procedures may not be good argument - why are those not included in the
   security or registry object??
   * login procedure includes user configuration - a dependency not wanted for security
     object
   * registration procedure may be different dependent on how registration requests and
     responses can be exchanged
   * most important: **procedure** implies **needing UI**

 * included: security, configuration, registry and/or storage locations.

## Approach