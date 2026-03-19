<!--Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)-->
<!--SPDX-License-Identifier: 0BSD-->
# **MaTeMa** - **Ma**nual **Te**st **Ma**nager

```{page-status} draft
:summary: only the situation is usable, the rest needs review and update (2026/03)
```

## Situation
Assume you are a developer or tester in a reasonably complex project running on low budget
that needs manual test cases because it has GUI elements to test. You already have some
test cases but fear to add more because you have no means to maintain an overview nor do
you have time to run all tests for every code change you do. But you also do not want to
sacrifice quality.

Let's look at some typical development steps:
1. You added new functionality and need to identify which test cases to re-run and if
   you require new ones.
   * The test manager marks any test execution invalid if you changed files on which the
	 execution depended on.
   * Since the manual test case coverage results are merged with the overall coverage,
	 you can identify if any new manual test case is required.
2. You want to execute the (new) test cases and add test results.
   * The test case manager automatically identifies new test cases and you can start and
     run the test cases directly from the manager.
   * The test case description will be available during execution and you will be able
     to comment on the test case execution.
3. In several files, you only corrected spelling and documentation or the changes you
   did are minor and do not want to re-execute the test case.
   * The case manager maintains a code history and you can add a rationale why certain
     file changes are not relevant.
   * The case manager will apply this rationale in the execution history
4. You want to wrap up your implementation, reacting on minor findings from past test
   case executions.
   * You can filter test case results accordingly

```{admonition} Draft Status
:class: warning
Anything below is not well sorted into a structure and potentially outdated. See issue #62.
```

## Approach

The idea comprises steps in the test case execution:
* update the manual test case database (validity of test cases based on code changes and
  scanning for existing manual test cases)
* an automatic test case that is FAILING if any manual test case has no valid test
  execution
* merging the coverage of valid manual test case executions with the automated unit
  tests

Additionally, scripting or an application is required, assisting with:
* listing invalid test cases
* triggering test case execution including adding results to database

During manual test case execution:
* the tester has one window with the test descriptions (things to check) and commenting
  results with OK/FAILED
* the tester gets the window or frame in a second window to play around
* the test execution may include additional checks after test execution

## Dumped Development Notes
### Dependencies
When rolling out the overall dependency shall be APPXC-ManualTests depending on APPXC-Gui which depends on APPXC. APPXC-GUI still uses APPXC-ManualTests but this dependency is only required during testing, not for the module itself.

But the above has a severe flaw: when executing GUI tests in APPXC-GUI, the python environment running the ManualTestHelpers will have APPXC-GUI installed.
* The test cases MUST be executed within a separate environment that DOES NOT have APPXC-GUI installed such that it uses the local sources.
### Further Top-Level tasks for test application
Current culprits after cases can be run with coverage stored:
* I would like to see a coverage summary after execution
* I would like to see a coverage summary for specific folders
* I need a mechanism that some configuration can tell which files to cover. Some subset of appxc - but due to invalidation via dependencies (unit tests), this should be stripped down much further and potentially on a per-file basis. For feature-tests, this should not be the case (any coverage is reasonable).
* Test results (comments and status) should be collected after execution. But how does the separate system call know where to put such information? >> Script arguments would work.
* From the above: the test case helper needs to write a separate file with execution results (tester comments, status). At some point, we also need to collect testing instructions which could also be collected in this way. An even better way would be if the case helper would directly act upon the database. This would also allow to display "recent execution results".
* CAREFUL HERE - there are two applications running that act on database. STORE before running and LOAD afterwards.
* Note to above: this idea is like the test case execution being initialized by the test case implementation. A different paradigm would be the execution being initialized by the handler and the test case path/name being an argument to this. >Dependency Inversion< >> The test case script may not need to know the handler anymore.
* Note to above dependency inversion: this may be good for the new way of running such cases. But it may become cumbersome to run such cases completely manually. Also: due to the test case helper, a bit more code may be executed and covered. >> Not a problem (unit tests are stripped down to a minimum; feature tests are allowed to cover more)

CaseRunner is called: The database runner is calling the case runner with one argument reflecting the database and another the case to run.
+ Argument handling would be done within the case runner
+ The case would be dynamically loaded as a module, accessing the variables from the case
- Since module variables are accessed, there is no type hinting or assistance in what features the test helper would support (via auto completion)/ When running the test case manually (calling the guitest_\*.py), I would need to call "guitest.py run case_name" >> acceptable

Test case is called: The test case is called directly. Within the guitest case, the case runner is constructed with test description and finally calling some run(). / Arguments to this call need to be forwarded to the handler. But this is as simple as sys.argv. This actually could be called from the case runner BUT it would complicate potential testing.
+ Since script is implemented, interacting with the case runner, its implementation is assisted by type hints and auto completion.
+ If there would be different guitest types (frame and toplevel already existing, different GUI may be another use case or something else requiring manual testing) - a different class could be added WITHOUT affecting existing test cases. In the other solution, this case would imply making the case runner arbitrarily more complex.
+ The case above can be supported by some "basic test runner" that handles common parts and from which more specific case runners are derived.
Conclusion: Call the case and let case implementation load the case runner. Just ensure that any later testing can OVERRIDE what comes from sys.argv.
* test helper assists in running test cases (collecting test result, marking valid, collecting coverage)
* TOX considers (valid) guitest results in coverage