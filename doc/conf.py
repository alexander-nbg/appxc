# Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)
# SPDX-License-Identifier: 0BSD
from datetime import date
from pathlib import Path

project = "APPXC"
html_title = "APPXC"
author = "the contributors of APPXC (github.com/alexander-nbg/appxc)"
copyright_year = date.today().year  # noqa: DTZ011 no timezone for correct year
copyright = (  # noqa: A001
    f"{copyright_year} the contributors of APPXC (github.com/alexander-nbg/appxc)"
)

extensions = [
    "myst_parser",
    "sphinxcontrib.plantuml",
    "sphinx.ext.duration",
]

myst_enable_extensions = [
    "colon_fence",
    #'linkify',
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

source_suffix = {
    ".md": "markdown",
}

master_doc = "index"

html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "github_url": "https://github.com/alexander-nbg/appxc",
    "announcement": (
        "<b>Documentation is not usable</b>: "
        "APPXC is currently transitioning from private repo. "
        'See <a href="https://github.com/alexander-nbg/appxc/issues/48" '
        'target="_blank">issue #48</a>.'
    ),
}

project_root = Path(__file__).resolve().parent.parent
plantuml_jar = project_root / "doc" / "plantuml.jar"
plantuml = f"java -jar {plantuml_jar}"
plantuml_args = ["-I", project_root / "doc"]
plantuml_output_format = "svg"
plantuml_syntax_error_image = True
