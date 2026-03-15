# Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)
# SPDX-License-Identifier: 0BSD
#
# The page-status feature was added and is maintained by AI while added code is still
# reviewed by human developers.
"""Sphinx support for per-page documentation status.

Principles:
- `page-status` stores page metadata only; it renders via sidebar templates.
- Summary text can be explicit (`:summary:`) or directive body text.
- Defaults are status-specific and configured in ``conf.py``.

See also: doc/dev/concepts/page_status.md
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING, Any, cast

from docutils.parsers.rst import directives
from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective

if TYPE_CHECKING:
    from sphinx.application import Sphinx

LOGGER = logging.getLogger(__name__)

VALID_STATUSES = {
    "draft": "Draft",
    "stub": "Stub",
    "obsolete": "Obsolete",
    "usable": "Usable",
    "incomplete": "Incomplete",
}

DEFAULT_STATUS = "unknown"
DEFAULT_STATUS_LABEL = "Unknown"
DEFAULT_SUMMARIES = {
    "draft": "Draft documentation. Review details and behavior before relying on it.",
    "stub": "Stub page. Core details are still missing.",
    "obsolete": "Obsolete page. Content is outdated and must not be relied on.",
    "usable": "Usable overview. Check linked references for full behavior.",
    "incomplete": "Partly complete. Verify missing sections before usage.",
    "unknown": "Status not reviewed yet. See doc/dev/how-to for page-status usage.",
}


def _get_status_store(build_environment: Any) -> dict[str, dict[str, Any]]:
    existing_store = getattr(build_environment, "appxc_page_status", None)
    if not isinstance(existing_store, dict):
        existing_store = {}
        build_environment.appxc_page_status = existing_store
    return cast(
        "dict[str, dict[str, Any]]",
        existing_store,
    )


def _normalize_status(requested_status: str) -> tuple[str, str]:
    normalized_status = requested_status.strip().lower()
    canonical_status = normalized_status

    if canonical_status not in VALID_STATUSES:
        allowed_statuses = "draft, stub, obsolete, usable, incomplete"
        msg = (
            "Unsupported page-status value "
            f"'{requested_status}'. Allowed values are: {allowed_statuses}."
        )
        raise ValueError(msg)

    return canonical_status, VALID_STATUSES[canonical_status]


def _resolve_default_summary(app: Sphinx, status: str) -> str:
    defaults = app.config.page_status_default_summary
    if isinstance(defaults, dict):
        typed_defaults = cast("dict[str, str]", defaults)
        if status in defaults:
            return typed_defaults[status]
        if DEFAULT_STATUS in defaults:
            return typed_defaults[DEFAULT_STATUS]
    return "Review summary pending."


def _build_page_status(app: Sphinx, page_name: str) -> dict[str, Any]:
    status_store = getattr(app.env, "appxc_page_status", {})
    page_status = status_store.get(page_name, {})
    status = page_status.get("status", DEFAULT_STATUS)

    summary = page_status.get("summary") or _resolve_default_summary(app, status)

    return {
        "status": status,
        "label": page_status.get("label", DEFAULT_STATUS_LABEL),
        "summary": summary,
        "text": summary,
        "hidden": page_status.get("hidden", False),
    }


class DocStatusDirective(SphinxDirective):
    """Store a page-level documentation status without rendering inline output."""

    required_arguments = 1
    optional_arguments = 1
    has_content = True
    final_argument_whitespace = True
    option_spec = cast(
        "dict[str, Any]",
        MappingProxyType(
            {
                "summary": directives.unchanged,
            }
        ),
    )

    def run(self) -> list[Any]:
        try:
            canonical_status, display_label = _normalize_status(self.arguments[0])
        except ValueError as error:
            reporter = cast("Any", self.state.document.reporter)
            error_message = reporter.error(
                str(error),
                line=self.lineno,
            )
            return [error_message]

        # Parsing order:
        # 1) `:summary:` option, 2) directive body, 3) status-specific default.
        # ``hide`` is an optional positional argument on the same line as the status.
        summary_from_content = " ".join(
            line.strip() for line in self.content if line.strip()
        ).strip()

        hidden = len(self.arguments) > 1 and self.arguments[1].strip().lower() == "hide"

        summary = (
            self.options.get("summary", "").strip()
            or summary_from_content
            or _resolve_default_summary(self.env.app, canonical_status)
        )

        status_store = _get_status_store(self.env)
        if self.env.docname in status_store:
            LOGGER.warning(
                "Multiple 'page-status' directives found in %s; using the last one.",
                self.env.docname,
                location=(self.env.docname, self.lineno),
                type="appxc",
                subtype="page-status",
            )

        status_store[self.env.docname] = {
            "status": canonical_status,
            "label": display_label,
            "summary": summary,
            "hidden": hidden,
        }
        return []


def _add_page_context(
    app: Sphinx,
    page_name: str,
    template_name: str,
    context: dict[str, Any],
    doctree: Any,
) -> None:
    del template_name, doctree

    context["appxc_page_status"] = _build_page_status(app, page_name)
    context["appxc_page_status_show"] = (
        not app.config.page_status_hide_all
        and not context["appxc_page_status"].get("hidden", False)
    )
    context["appxc_page_status_linked_page"] = app.config.page_status_linked_page or ""


def _purge_doc_status(app: Sphinx, build_environment: Any, docname: str) -> None:
    del app
    _get_status_store(build_environment).pop(docname, None)


def _merge_doc_status(
    app: Sphinx,
    build_environment: Any,
    docnames: list[str],
    other: Any,
) -> None:
    del app, docnames
    _get_status_store(build_environment).update(getattr(other, "appxc_page_status", {}))


def setup(app: Sphinx) -> dict[str, bool]:
    app.add_config_value(
        "page_status_default_summary",
        DEFAULT_SUMMARIES,
        "env",
        [dict],
    )
    app.add_config_value(
        "page_status_linked_page",
        "",
        "env",
        [str],
    )
    app.add_config_value(
        "page_status_hide_all",
        False,
        "env",
        [bool],
    )
    app.add_directive("page-status", DocStatusDirective)
    app.connect("html-page-context", _add_page_context)
    app.connect("env-purge-doc", _purge_doc_status)
    app.connect("env-merge-info", _merge_doc_status)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
