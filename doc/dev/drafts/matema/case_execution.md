<!--Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)-->
<!--SPDX-License-Identifier: 0BSD-->
# Feature: Case Execution

```{page-status} draft
:summary: MaTeMa would be great but it's too much for now (2026/03)
```

```{admonition} Draft Status
:class: warning
Anything below is not well sorted into a structure and potentially outdated. See issue #62.
```

## Initialization Tree
* Doing nothing when: no command line arguments
* If command line arguments include any "process_*"
	* run the process (no file parsing required, this command should be at first place)
* If command line arguments include any matema commands (not yet defined)
	* parse commands
* Otherwise, arguments remain stored anyway and processing can wait until run()
* At run() or if there are command line arguments:
	* parse file and command line arguments

## Coverage Control
For application level testing, the test preparation steps *must be separated* for the
coverage. Example: even though the user data (login) preparation is executed for a test
case concerning registry, the login steps are not tested in such a test case. Hence, the
test case for registration should not be invalidated by changing the login
implementation. This is a trade-off.