# Copyright 2025-2026 the contributors of APPXC (github.com/alexander-nbg/appxc)
# SPDX-License-Identifier: Apache-2.0
"""Manual Test Runner

Call via:  ./.venv/bin/python manual_tests.py

Virtual environment (venv) is required since, without, appxc would be unknown.
"""

from appxc_matema import CaseData, CmdHelper, Scanner

case_data = CaseData()

scanner = Scanner(case_data=case_data, path=["tests", "tests_features"])
scanner.scan()

cmd_helper = CmdHelper(database=case_data)
cmd_helper.run()
