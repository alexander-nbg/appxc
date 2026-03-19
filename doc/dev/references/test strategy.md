<!--Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)-->
<!--SPDX-License-Identifier: 0BSD-->
# Test Strategy

```{page-status} usable
:summary: content is up to date while there are gaps in realizing the strategy (2026/03)
```

The test strategy applies to all [features](/user/features/_features) in the user area
and to all modules in `src/appxc`. It does not cover development tools in
`src/appxc-dev`, the scripts in `dev` or documentation related extensions in `doc/**`.

## Test Levels
Considered are the following two test levels:
* __Unit Tests__ are driven by code coverage of the individual ***modules*** and *should
  cover 100%* (lines and branches) while *80% branch coverage is acceptable for initial
  versions*.
* __Acceptance Tests__ are driven by the APPXC supported ***features*** and *appropriate
  coverage is determined by review*.

**Integration test**. The term *integration test* will not be used because neither unit
tests nor acceptance tests *focus* on validating the interfaces between modules.
Validating those interactions in acceptance tests is intended, but remains implicit.

### Unit Tests
**Purity of *unit***. While unit tests focus on a single module (python file), unit
tests may or may not cut free interfaces to other modules by mocks with following consequences:
* Not isolating a unit's behavior increases the complexity of the object under test.
  There are no rules applied to triage this risk.
* Other units which are called may be implicitly covered, reaching coverage goals
  without having their own dedicated test cases. This is accepted and intended for
  abstract classes and (base) classes which are not used outside of the module's scope.
  A module in this item means any set of python files in a folder `src/appxc/*`. It is
  not acceptable for any class or function which is used by another module or by users
  of the APPXC package.

**Manual GUI tests.** GUI modules need manual tests but they are no exception from needing
unit tests. However, as of 2026/03, there are no means to effectively collect the test
coverage or results from manual test cases.

### Acceptance Tests
**No duplication**. If feature use cases are well covered by unit tests, they do not
need to be repeated as acceptance test. A corresponding file shall still be present, the unit test references shall be listed and some explanation should be provided.

**User perspective**. Acceptance tests shall use the APPXC implementation as-is wherever
possible to cover all user aspects. A rationale is required when deviating from this
expectation.

## Test Methods
All methods in this section may be combined.

### Pytest
The default approach is straightforward pytest test cases. Pytest is preferred, but not
mandated, for automated unit tests because BDD tests would add the complexity of
two files, a more abstract implementation and the abstraction of the Gherkin language.

### Behavior Driven Tests (bdd)
They are included in a pytest run and just use the capabilities of python-bdd with
Gherkin syntax. They are preferred for acceptance testing because the feature files are
easily readable functional requirements.

```{admonition} concept maturity
:class: attention
As of 2026/03, acceptance test implementation has various implementation attempts which are not yet consolidated. It should be consolidated with the features being lifted into
a usable maturity.
```

### Manual Tests (GUI)

As of 2026/03, parts of the concept are realized, but not well documented. This section will be updated at a later point. See also [MaTeMa](../drafts/matema/_matema.md).

## Folder Structure
### Unit tests
Unit tests are in `tests/unit` and in subfolders according to the modules in `src`.
Different test files exist (see test methods):
* normal unit tests should use the naming of the `src` file with the prefix `test_`.
* manual test cases for GUI elements also use the naming of the `src` file with the
  prefix `manual_` but need to add further details into the file name since each file
  represents one test case.
* behavior driven tests (bdd) need to use the prefix `test_bdd` and come along with a
  second `*.feature` file.

Examples:
* `tests/unit/test_buffer.py`
* `tests/unit/storage/test_ram.py`
* `tests/unit/gui/manual_setting_dict_column_frame.py`


### Acceptance tests
Acceptance tests are all stored in `tests/acceptance` while following the same folder
and file naming conventions.

Examples:
* `tests/acceptance/sync/test_bdd_sync.py` and
* `tests/acceptance/sync/test_bdd_sync.feature`

<!--
TODO: file guideline should include the fixtures folder. However, there is some refactoring required based on one core aspect: if APPXC needs additions for test case execution, may deriving projects need the same additions? This would mean, moving fixtures and testing into an implementation module of APPXC.
-->