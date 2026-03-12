# Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)
# SPDX-License-Identifier: Apache-2.0
import inspect
import os
import subprocess
import sys
import textwrap
from collections.abc import Callable
from pathlib import Path

from appxc import __version__, fileversions, logging
from tests.fixtures.test_sandbox import init_test_sandbox_from_fixture


def _log_default_usage(directory: str) -> None:
    # default reduces number of log files for the file rotation test
    logging.activate_logging(directory=directory, n_files=3)


def _run_activate_logging(
    log_directory: str,
    callback: Callable[[str], None] | None = None,
) -> None:
    if callback is None:
        callback = _log_default_usage
    callback_source = textwrap.dedent(inspect.getsource(callback))
    callback_name = callback.__name__

    script = (
        "from appxc import fileversions, logging\n"
        f"exec({callback_source!r}, globals())\n"
        f"globals()[{callback_name!r}]({log_directory!r})\n"
    )

    command = [
        sys.executable,
        "-c",
        script,
    ]

    subprocess.run(command, check=True)


def test_activate_logging_multiple_files(request):
    test_path = init_test_sandbox_from_fixture(request)

    # Initialize a logged program 3 times:
    _run_activate_logging(test_path)
    _run_activate_logging(test_path)
    _run_activate_logging(test_path)

    created_files = [
        file_name
        for file_name in os.listdir(test_path)
        if file_name.startswith("logging_") and file_name.endswith(".log")
    ]
    assert len(created_files) == 3, "Expected exactly 3 log files"

    # get todays data in format YYYYMMDD
    today = fileversions.format_date(date=None, format="yyyyMMdd")
    assert f"logging_{today}_00.log" in created_files
    assert f"logging_{today}_01.log" in created_files
    assert f"logging_{today}_02.log" in created_files


def test_activate_logging_file_rotation(request):
    test_path = init_test_sandbox_from_fixture(request)

    # Initialize a logged program 5 times:
    _run_activate_logging(test_path)
    _run_activate_logging(test_path)
    _run_activate_logging(test_path)
    _run_activate_logging(test_path)
    _run_activate_logging(test_path)

    # ..then expecting log files 2, 3 and 4:
    created_files = [
        file_name
        for file_name in os.listdir(test_path)
        if file_name.startswith("logging_") and file_name.endswith(".log")
    ]
    assert len(created_files) == 3, "Expected exactly 3 log files"

    # get todays data in format YYYYMMDD
    today = fileversions.format_date(date=None, format="yyyyMMdd")
    assert f"logging_{today}_02.log" in created_files
    assert f"logging_{today}_03.log" in created_files
    assert f"logging_{today}_04.log" in created_files


def test_activate_logging_content(request):
    test_path = init_test_sandbox_from_fixture(request)

    _run_activate_logging(test_path)

    log_files = sorted(Path(test_path).glob("logging_*.log"))
    assert log_files
    log_lines = log_files[-1].read_text(encoding="utf-8").splitlines()

    assert len(log_lines) == 1, "Exactly one log line expected"
    assert "INFO appxc.activate_logging" in log_lines[0]
    assert f"v{__version__}" in log_lines[0]


def test_typical_usage_in_order(request):
    test_path = init_test_sandbox_from_fixture(request)

    def run_logging(directory: str):
        logging.activate_logging(directory=directory, app_scope=["test"])
        logging.get_logger("test.").info("test scope log")
        # just produce some APPXF logging:
        fileversions.set_locale("DE")

    _run_activate_logging(test_path, callback=run_logging)

    log_files = sorted(Path(test_path).glob("logging_*.log"))
    assert log_files
    log_content = log_files[-1].read_text(encoding="utf-8")

    expected_order = [
        "APPXC v",
        "test",
        "test scope log",
        "appxc.fileversions.set_locale",
    ]

    current_position = -1
    for expected_line in expected_order:
        next_position = log_content.find(expected_line, current_position + 1)
        assert next_position >= 0
        current_position = next_position
