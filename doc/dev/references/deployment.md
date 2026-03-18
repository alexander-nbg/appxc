<!--Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)-->
<!--SPDX-License-Identifier: 0BSD-->
# Deployment

```{page-status} usable
:summary: up to date (2026/03)
```

## Version
As of 2026/03, only versions 0.0.x and 0.0.x.devN are used.
 * APPXC requires general usability before entering a version 0.1.0. The additional
   efforts on enabling separate bugfix releases for unused code is avoided by this
   approach.
 * devN releases allow to access updates before the release milestone is reached. Quick
   reaction times are considered crucial in the current projcet state. Development
   releases may be deleted from pypi and the approach will be reconsidered, latest when
   reaching v0.1.0.

A version 1.0.0 will be planned when features can demonstrate maturity by being applied
in different projects. Otherwise, there is no evidence of having developed the right
features and efforts on maintaining interface stability are wasted.

Note that community feedback is affecting when a version 0.1.0 is created and a version
1.0.0 will never exist without positive feedback.

## Continuous Deployment
The deployment is automated via github actions. Enrty points to the procedure are
`pyproject.toml` and `.github/workflows/cd.yaml`. It has three top level steps:
1) The **package** is build and validated
1) Upload to **testpypi** and validation (same build)
1) Final upload to **pypi** and validation (same build)

The validation runs all tests on one python version with the package installed from
wheel/testpypy/pypi into a fresh virtual environment. Step (1) is also included in the
CI workflow.

The trigger is manual for .devN versions and automatic for releases. The deployment to
testpypi and pypi requires a review by a maintainer.

## Further References
Helpful pages:
* https://py-pkgs.org/welcome
* https://packaging.python.org/en/latest/tutorials/packaging-projects/
* https://drivendata.co/blog/python-packaging-2023
