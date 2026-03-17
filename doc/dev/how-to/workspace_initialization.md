<!--Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)-->
<!--SPDX-License-Identifier: 0BSD-->
# Workspace Initialization

```{page-status} incomplete
:summary: see page introduction (2026/03)
```

The page content is collected only during setup of my own environment which is basically
never repeated and did include some back and forth. I currenlty use Ubuntu 24.04 with VS
Code and Python 3.12 as default. As a consequence:
 * setup is almost certainly incomplete
 * superflous steps are also likely
 * it is not considering other OSes, yet

If this works out well for you, let me know. For any updates, just modify yourself or
notify me directly for small additions.

## Ubuntu installations

```bash
sudo apt-get install tox
sudo apt install python3.12-venv
sudo apt install gettext
```
## Virtual Environment Setup

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e . -r tests/requirements.txt -r dev/requirements.txt -r doc/requirements.txt
```


```{admonition} Always .venv
:class: warning

Ensure to run ***all commands always*** from the virtual environment.
```

## Check Setup

### CI Checks
```bash
ruff check
ruff format --check
basedpyright
./dev/check_license_headers.sh
pytest -rA
tox
```

### Package and Documentation Builds
```bash
python -m build
./dev/build_doc.sh
```
Open documentation and check the version next to "APPXC" in the top left (verify
hatch-vcs is working properly). To serve the HTML pages locally while having your
browser as protected ubuntu snap, you may use `python3 -m http.server 8000` and open `http://127.0.0.1:8000/doc/_build/html/index.html`.

### Manual Test Cases
Despite the manual test case runner infrastructure, running any manual test case will
verify the GUI is working. The first command is some tool helper, not yet being
productive, the third and second are two random manual test cases.
```bash
python manual_test.py
python tests/unit/gui/manual_setting_frame.py
python PYTHONPATH=. python tests/acceptance/full_application/manual_user_s0.py
```

Note the `PYTHONPATH=.` in the last line which is required to find module imports currently still located in `tests`.

## Optional: VS Code Extensions
Recommended are:
 * Ruff by Astral Software (Ruff formating on save and inline issue highlighting)
 * Pylance (for inline highlighting even if final checks are basedpyright)
 * Rewrap Revived by Drew Nutter (`[Alt]+[Q]` auto wrapping lines)

## Journal
### 15.06.2025
Problems with pip after changing from Ubuntu 22.04 to 24.04 (pip needs venv or packages must be installed via apt-get). This topic has two aspects:
 * venv is now mandatory when developing python
 * I did not yet resolve preparing for multiple python versions. 3.10 was not available via apt-get and I stopped digging deeper into pyenv.
Via apt-get: https://askubuntu.com/questions/682869/how-do-i-install-a-different-python-version-using-apt-get
Via pyenv: https://help.clouding.io/hc/en-us/articles/13555555842588-How-to-install-different-versions-of-Python-on-Ubuntu
