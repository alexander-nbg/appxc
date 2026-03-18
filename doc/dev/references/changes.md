<!--Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)-->
<!--SPDX-License-Identifier: 0BSD-->
# Contribution Checklist

```{page-status} draft
:summary: Partly outdated and no clear seperation on what's usable (2026/03)
```

**Purpose.** Details to be considered before a pull request can be merged are
summarized, primarily, to support by providing an overview and including references or
code snippets. Secondarily, because the listings will not be duplicated, it serves as a *reference* for planning efforts or reviewing pull requests.

## Change Preparation

Every update shall enter via **pull request**s while each is linked to at least one
**ticket** (`resolves #42`, `relates to #42` or similar).

+ SMALL PR
+ deviation
+ minors direct
+ exceptions (ticket templates, deployment CI)

 * Developers ***with repo access*** can use `dev/branch_start.sh` to start
   working on a new branch and `dev/branch_close.sh` to initiate the PR.
   * branches must use the pattern `<issue-number>_<summary>` with `summary` in
     [snake_case](https://en.wikipedia.org/wiki/Snake_case). Example:
     "42_compute_answer".
 * Developers ***without repo access***.. ..let me know which details are missing, here.

## Code Changes



* `ruff check`, `ruff format`
* unit test coverage (see [[APPXC Test Strategy]])
* ToDo remarks for any known open topics (including planning tickets and referenced in ToDos `"ToDo #42"`)
* Ticket concluding remarks
	* Planning follow-up tickets
* Localization: MO/PO files are updated (all translations available)
* Functions are documented
	* How much depends on exposure
	* Minimum for public functions: Purpose (summary) and type annotation (including returns)
## Features on Application Level
If a feature is visible for final applications, it needs:
* documentation (updates) in the feature section
* automated BDD testing for behavior (application harness)
* manual test for user experience (application harness GUI)
* reference usage
	* documentation
	* testing the exact code in the testing
* All bullet points below since it is always also a feature for application developers
