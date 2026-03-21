<!--Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)-->
<!--SPDX-License-Identifier: 0BSD-->
# Documentation: GitHub Links

```{page-status} usable
:summary: initial version (2026/03)
```

The **GitHub link shorthand** allows compact Markdown links such as `[#42](gh)`,
`[v1.2.3](gh)`, or `[src/appxc](gh)`. During the documentation build, these
links resolve to full GitHub URLs.

## Situation
Documentation often references source files, issues, and versions but accessing the details of those references would require an actual link to the referenced source. Some examples:
* Development documentation is kept concise, with more detail added to source files. The
  same can apply to user-facing module documentation which will not repeat docstring
  details.
* Issue numbers and versions are often referenced for open topics while new features are
  being developed.

Another common situation affecting doucumented source code references is refactoring.
When file names or paths change, links in the documentation can become invalid without
being noticed and then cause confusion.

## Status Quo
Built-in Markdown links would require something like
`[#42](<project URL>/issues/42)`. Even this is a short example, and `<project URL>`
shortens it further. In Markdown files, these links are verbose and require redundant
information because the link text is repeated in the URL. As a result, references may
still be mentioned, but the link itself is often omitted, creating a barrier to the
additional information.

## Approach
A Sphinx extension, [doc/_ext/github_links.py](gh), supports links to:
* the **project** via `[APPXC](gh)`, resulting in [APPXC](gh)
* **issues** or **PRs** via `[#61](gh)`, resulting in [#61](gh)
* **source folders** via `[doc/dev](gh)`, resulting in [doc/dev](gh)
* **source files** via `[doc/dev/concepts/doc_github_links.md](gh)`, resulting in
  [doc/dev/concepts/doc_github_links.md](gh)
* **versions**, either explicitly via `[v0.0.2](gh)`, resulting in [v0.0.2](gh) or the
  **current version** via `[gh:version](gh)`, resulting in [gh:version](gh)

The syntax also supports the following alternatives:
* **explicit targets** with arbitrary link text via
  `[workflow](gh:.github/workflows/cd.yml)`, resulting in
  [workflow](gh:.github/workflows/cd.yml)
* a file name as the link text while providing only the path as additional
  information, such as
  `[doc_github_links.md](gh:path:doc/dev/concepts)`, resulting in
  [doc_github_links.md](gh:path:doc/dev/concepts)

The extension uses the `release` variable in [conf.py](gh:doc/conf.py) and links to
files and paths for the version that matches the documentation build. Development
builds and local builds that do not have a tagged release use the current checkout
commit ID.

### File and Path Checks
Links to files and paths are verified against the file system. If a file or path does
not exist, the build raises an error. This helps ensure that the documentation links
only to files and paths that actually exist, provided this extension is used.

## Additional Considerations
### Alternative Hooks
* The link syntax `[]()` was selected as a hook because it is the default for links and
  supports natural reading of the markdown source. You read the text in `[]` and jump
  over the implementation detail in `()`.
  * There are probably many alternatives but a role may be a very common approach to add
    behavior. A role based syntax, however, would make you read some implementation
    detail first before the actual text is found and `:gh:#15` is hard to read.
* There were many experiments before ending up with just `(gh)`. `(@gh)` provided more
  awareness on the special handling