#!/bin/bash
# Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)
# SPDX-License-Identifier: 0BSD

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

export PYTHONPATH="$REPO_ROOT/src${PYTHONPATH:+:$PYTHONPATH}"

python3 -m appxc_dev.check_license_headers "$@"
