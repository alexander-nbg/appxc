<!--Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)-->
<!--SPDX-License-Identifier: 0BSD-->
# CI: License Header Checks

```{page-status} usable
```

The script [dev/check_license_headers.sh](gh) ensures that all checked-in files contain
appropriate copyright and license headers.

## Situation
Simply adding a license file to the project has two potential flaws:
  1) When the file is copied elsewhere, copyright and license information would be lost.
  2) APPXC uses two licenses and it may not be clear which one applies for which file.

As a consequence, each file must include the copyright and license information in its
header. The remaining problem is that adding this information is easy to forget.

## Approach
The script [dev/check_license_headers.sh](gh) wraps the Python script
[src/appxc_dev/check_license_headers.py](gh) which:
 * scans all files which are checked in
 * defines expected licenses per file type (and folder)
 * ignores explicit mentions from [LICENSE](gh)

The script is used as part of the [static checks](../references/static-checks).