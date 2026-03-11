# Copyright 2023-2026 the contributors of APPXC (github.com/alexander-nbg/appxc)
# SPDX-License-Identifier: Apache-2.0
from appxc import logging
from appxc.storage import Storage


def pytest_configure(config):
    logging.activate_logging("appxc", directory="./.testing")


def pytest_runtest_teardown(item, nextitem):
    # need to reset storage context switching
    Storage.reset()


# Add logging for feature execution:
def pytest_bdd_before_step_call(request, feature, scenario, step, step_func):
    print(f"[BDD] {feature.filename}:{step.line_number} - {step.name}")
