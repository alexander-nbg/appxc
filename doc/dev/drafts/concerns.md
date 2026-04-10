<!--Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)-->
<!--SPDX-License-Identifier: 0BSD-->
# Concerns

```{page-status} draft
:summary: Documentation structure is still evolving (2026/03)
```

Planned intent of this page is to explain the cross-cutting nature of some concerns:
 * some have direct solutions (like logging or security)
 * Logging or error handling as concerns are well standardized in python with low
   friction.
 * Persistence, configuration or security influence each other.
   * Configuration must be persisted
   * Together with any data to be persisted, some of it should apply encryption
   * Data storage may need configuration, especially if it is a remote location like FTP


## Maintainability
Features:
 * need for logging
   * accessing logs from users
 * deploy updates

## Persistency
Features:
 * storing/loading settings and configuration
 * storing/loading general application data
 * synchronizing between instances

Aspects to the development procedure:
 * persistency triggers the need to consider backwards compatibility (old files)

## Security
Features:
 * storing and sharing passwords
 * user identity
 * role privileges, in particular user versus admin

Aspects to the development procedure:
 * testig may be affected if the applciation handles secrets
