#!/usr/bin/env bash
# Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)
# SPDX-License-Identifier: 0BSD

set -euo pipefail

# Ensure script is executed from APPXC root directory:
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Skip if .venv is already existing:
if [[ -d "${PROJECT_ROOT}/.venv" ]]; then
    echo ".venv already exists, skipping setup."
    exit 0
fi

echo "Creating .venv and upgrading pip..."
python3 -m venv "${PROJECT_ROOT}/.venv"
"${PROJECT_ROOT}/.venv/bin/pip" install --upgrade pip

echo "Installing APPXC and dev/doc/testing dependencies..."
"${PROJECT_ROOT}/.venv/bin/pip" install -e "${PROJECT_ROOT}"
# Also add dev, doc and testing dependencies:
"${PROJECT_ROOT}/.venv/bin/pip" install \
    -r "${PROJECT_ROOT}/doc/requirements.txt" \
    -r "${PROJECT_ROOT}/dev/requirements.txt" \
    -r "${PROJECT_ROOT}/tests/requirements.txt"

echo "Done. Activate with: source .venv/bin/activate"
