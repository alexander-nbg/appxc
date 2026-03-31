<!--Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)-->
<!--SPDX-License-Identifier: 0BSD-->
# Static Checks

```{page-status} usable
:summary: page is up to date but see ruff and basedpyright details (2026/03)
```

APPXC applies the following static checks as part of the continuous integration
([.github/workflows/ci-entry.yml](gh)). Given, the dependencies are installed
([dev/requirements.txt](gh)), the commands can be executed on the command line:
 * `dev/check_license_headers.sh` (see [CI: License Headers](../concepts/ci-license-headers))
 * `ruff format --check` (see below)
 * `ruff check` (see below)
 * `basedpyright` (see below)

## Ruff Formatting
APPXC uses `ruff format` to keep the code base consistent. Consistency of the code base
and the tremendously low effort using this approach had quite some weight in adding this
check.

Consider adding the ruff formatter in your IDE.

## Ruff Checker
The rules were selected *all in* with arguments being required before ignoring rules.
See the configuration in [pyproject.toml](gh) for details. The following applies:
 * As of 2026/03, a large set of rules are ignored because there was no time to fix them
   right-away. They must be ramped down when a module/feature becomes mature. Very
   likely, configuration and CI checks will be adapted to *ensure* the ramp down.
 * You're welcome to discuss the set of ignored rules! The current state was only
   reviewed by one person to get things running.

## Basedpyright
While it is recommended to keep [pyright](https://microsoft.github.io/pyright) (part of
Pylance in VS code) active to catch warnings early,
[basedpyright](https://docs.basedpyright.com) was selected because it supports CI and
project aspects: baselining the warnings to enable a ramp-down and fixing versions for
stable CI. See also this [mypy/pyright
comparison](https://github.com/microsoft/pyright/blob/main/docs/mypy-comparison.md)
summarizing arguments for pyright instead of mypy.

As of 2026/03, the rule set of for basedpyright is ***not*** reviewed. The aim 2026/03
was to enable the checker to stop further violations. With the baselining feature, no
more time was spent to review and triage the rule set. The approach will evolve while
getting modules mature.
