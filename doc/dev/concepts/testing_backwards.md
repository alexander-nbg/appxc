# Testing: Backwards Compatibility

```{page-status} draft
:summary: see situation section (2026/03)
```

## Situation
**In a short draft:** As soon as [persistency](/user/concerns/persistency) is supported,
application updates may break with previously persisted data.

```{admonition} Draft Status
:class: attention
As long as there is no APPXC v0.1.0, backwards compatibility is not supported. This page is just a stub/draft to prepare concepts while reaching v0.1.0.
```

## General Idea

* Selected tests generate version-specific workspaces in `/.testing/v0.1.0` by the same
  methods used to generate any other test-case workspace.
* At release, the workspaces from above are checked in.
* Missing is the approach how "marked test cases" would split "workspace generation"
  which skips for the regression test, relying on the existing workspace and the actual
  testing. The approach should also automatically look for existing version workspaces.

Further notes:
* The approach will be prone to test case renaming
