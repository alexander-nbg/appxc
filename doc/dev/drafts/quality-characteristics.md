<!--Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)-->
<!--SPDX-License-Identifier: 0BSD-->
 # Quality Characteristics

 ```{page-status} incomplete
:summary: incomplete and not fully reviewed, but usable (2026/04)
```

Intent of this page is to clarify the mission of APPXC as a solution for small to medium
scale associations (and eventual businesses) by highlighting differences in targeted
quality characteristics. At a second level, the page defines the basis for design
decisions.
 * architecture is often about compromises between non-functional requirements (speed
   versus memory consumption; lots of options (modifiability) versus easy to
   use (usability))
 * possible general motivation via [ISO/IEC
   9126](https://en.wikipedia.org/wiki/ISO/IEC_9126) or, better, ISO 25010


## Analysis (Incomplete)

Considering product quality, two things will always be true:
 * Quality needs time while time is limited
 * Constraints that include quality expectations will occasionally conflict with
   each other requiring a compromise

The table below lists remarks on product quality characteristics to (1) clarify product
goals and (2) to provide guidance in case of required compromises. Expectations which
are common sense like "modules behave like described" are not listed. Rows are marked
with decreased (`-`) or increased (`+`) importance compared to a subjective baseline to
emphasize the characteristics where APPXC may differ most from common expectations.

:::{list-table}
:widths: 5 3 20
:header-rows: 1

*   - Quality Characteristic
    - Rating
    - Comment

*   - functional suitability
    -
    - ***delivering value early is prioritized*** against covering all use cases before
      a release\
      the module and feature status shall be transparent in the documentation to
  mitigate irritation due to feature completeness

*   - reliability
    - ++
    - * APPXC provides a basis for desktop applications which must not be brittle
      * resulting is a ***high priority on bugfixes*** including documentation and
        interface updates if unexpected behavior emerges from unintended use cases
      * transparent documentation on completeness and maturity still enables delivery of
        partial solutions

*   - maintainability
    - ++
    - * high priority since APPXC can only work with community support
      * maintainability is an enabler for reliability which also has high priority

*   - performance efficiency
    - \-\-
    - architecture decisions shall prioritize reliability, compatibility and early
      availability of resolved concerns higher than performance efficiency\
  relevant limitations to feature suitability shall be documented on the feature
      pages\
      efficiency increase will be planned where it can be improved by higher development
      efforts

*   - usability
    -
    - scope library, scope application

*   - compatibility
    -
    - compatibility shall focus on applying low expectations on the IT infrastructure.
      Examples: no solution which only runs on one operating system ***or*** not relying
  on a particular server infrastructure.\
      beginning with `v0.1.0`, backwards compatibility must be considered for
  testing, release notes and documentation for more complex changes

*   - security
    -
    - * strictly aiming for a security level which is significantly better than handling
        office documents and collaborating via email and file shares
      * aiming for very high security levels is not in scope for APPXC since target
        users cannot provide the necessary capacity in IT operations

*   - flexibility
    -
    - TBD

:::
