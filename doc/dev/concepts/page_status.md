<!--Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)-->
<!--SPDX-License-Identifier: 0BSD-->
# Documentation: Page Status

```{page-status} usable
:summary: ""
```

The **page status** is the prominent block on the right, raising awareness on incomplete
or incorrect information.

## Situation

With APPXC constantly evolving, the ***documentation is having different maturity***
because ***publishing partial value is prioritized*** over publishing only fully mature
features. This approach poses ***risk to applying projects*** by using incorrect information.

## Status Quo

The situation would not require a special approach if the documentation text could
contain remarks on incomplete or inaccurate information wherever needed. A few issues to
consider:
1) Polluting a draft with mentions *wherever needed* distracts from a draft's purpose of
   conveying current ideas by highlighting the missing/inaccurate details.
1) It is high effort to get a rough idea on a page's maturity if all documentation text
   must be scanned. With just remarks in arbitrary text, readers need to classify
   maturity themselves.
1) Remarks on an incomplete or outdated status in the introduction of a page are
   explicit mentions of flaws but will likely be missed when reading a subsection.
1) It is and will remain hard to catch up documenting *everything* in high quality. As
   of 2026/03, this is particularly true after taking over of the privatly maintainted
   library into v0.0.3.

## Approach

Each page prominently classifies it's maturity as **page status** on the right side. The
possible page status are:

|status|use case|
|---|---|
|stub|page created to link and/or drop information|
|draft|refinement and preparation|
|incomplete|partly usable, other parts: in draft, outdated or missing|
|usable|fully usable up to minor flaws mentioned in text|
|obsolete|outdated information
|unknown|Should not be visible: the page did not define it's status|

Each page adds a directive at the top:
````{code-block} markdown
```{page-status} draft
:summary: In preparation, last updated on 2026/03
```
````

The directive **page-status** is configured in `conf.py` and further details entry point
is `doc/_ext/doc_status.py`.


<!-- Could be added later: In contrast to module or feature status, there is no ***mature*** page status.-->

## Further Considerations

### Limitations
* The page status is not prominent when viewing pages on the mobile phone. This is
  accepted, assuming developers using APPXC will reguarly *also* view the docs on a
  desktop browser

### Future Ideas
* Adding a CI check to avoid **unknown** status
* Pages on features/moduels may indicate feature/module maturity analogously to the
  documentation status. The status may also be merged or substituted on those pages.
* The page status for features and modules *may become a dependency* when promoting
  feature/module maturity. A mature feature/module should have a usable documentation.
