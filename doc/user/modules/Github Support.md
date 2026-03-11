<!--Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)-->
<!--SPDX-License-Identifier: 0BSD-->
# Testing
```{plantuml} github-support-testing.puml
```

## Current Setup
* Entry point: **.github/workflows/test.yml**
	* Calls: **appxc/github/test**@main (os, python version)
		* checkout repo
		* checkout appxc (if not running on appxc)
		* Calls: **./.github/actions/setup** (only if on appxc)
		* Calls: **appxc/.github/actions/setup** (if not on appxc)
		* install appxc
		* tox preparation
		* run tox (if not appxc) << wrong

# TODO:
* User RUNNER_OS instead of passing the os as argument.