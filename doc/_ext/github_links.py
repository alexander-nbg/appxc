# Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)
# SPDX-License-Identifier: 0BSD
"""Resolve compact GitHub links written in MyST markdown link targets.

See doc/dev/concepts/doc-github-links.md for a top level introduction of the feature.

This extension operates on MyST markdown link syntax ``[text](target)`` during the
Sphinx doctree stage. It is therefore intentionally markdown-focused and does not try
to provide equivalent reStructuredText role syntax.

Terminology used in this module follows markdown syntax:
* ``label_text`` is the displayed link text inside ``[]``.
* ``target_text`` is the link target inside ``()``.
* MyST ``pending_xref`` stores ``target_text`` in its ``reftarget`` attribute.

Primary syntax:
* ``[label](gh)`` keeps the common case short and derives the target from ``label``.
* ``[label](gh:some/value)`` overrides the inferred target completely.
* ``[file.ext](gh:path:some/folder)`` joins the displayed file name with the path
    prefix, allowing short authoring without repeating the file name in both places.

Bare-marker inference is intentionally small in scope:
* ``#42`` -> issue page
* ``gh:version`` -> current build version target
* ``v1.2`` or ``v1.2.3`` with optional missing leading ``v`` -> release tag
* text equal to the configured project name -> repository root
* otherwise -> repository source object lookup

Source validation checks the local repository and supports both files and directories.
If the configured release is unstable, source links use the commit hash when available,
otherwise ``main``.

After hooking into Sphinx, ``_resolve_doctree_links()`` is the main entry point.
"""

from __future__ import annotations

import posixpath
import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import TYPE_CHECKING

from docutils import nodes
from sphinx import addnodes
from sphinx.errors import SphinxError
from sphinx.util import logging

if TYPE_CHECKING:
    from sphinx.application import Sphinx

LOGGER = logging.getLogger(__name__)

MARKER = "gh"
ISSUE_PATTERN = re.compile(r"^#(\d+)$")
VERSION_PATTERN = re.compile(r"^v?\d+\.\d+(?:\.\d+)?$")
COMMIT_HASH_PATTERN = re.compile(r"(?i)g?([0-9a-f]{7,40})")


# ---------------------------------------------------------------------------
# Context model and release interpretation
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class GithubLinkContext:
    repo_url: str
    release: GithubReleaseContext
    project_name: str
    repo_root: Path
    docname: str


# ---------------------------------------------------------------------------
# Release interpretation
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class GithubReleaseContext:
    full_name: str
    tag_name: str
    base_version: str
    is_dev: bool
    is_local: bool
    commit_hash: str

    @property
    def is_unstable(self) -> bool:
        """Return whether source links must avoid release tags."""
        return self.is_dev or self.is_local


def _release_context(full_name: str) -> GithubReleaseContext:
    """Interpret the configured release string into consistent derived attributes."""
    tag_name = full_name.split("+", maxsplit=1)[0]
    is_local = "+" in full_name
    is_dev = ".dev" in tag_name
    base_version = tag_name.split(".dev", maxsplit=1)[0]

    if not is_local:
        commit_hash = ""
    else:
        local_part = full_name.split("+", maxsplit=1)[1]
        commit_match = COMMIT_HASH_PATTERN.search(local_part)
        commit_hash = "" if commit_match is None else commit_match.group(1)

    return GithubReleaseContext(
        full_name=full_name,
        tag_name=tag_name,
        base_version=base_version,
        is_dev=is_dev,
        is_local=is_local,
        commit_hash=commit_hash,
    )


# ---------------------------------------------------------------------------
# Resolving Links
# ---------------------------------------------------------------------------


def _classify_target(
    target_text: str,
    label_text: str,
    project_name: str,
) -> tuple[str, str] | None:
    """Decode marker syntax and classify the resulting GitHub target."""
    normalized_target = target_text.strip()
    inferred_text: str | None

    # Keep the common case short by deriving the target from the link label.
    if normalized_target == MARKER:
        inferred_text = label_text
    # Support path-prefix composition to avoid repeating the file name in the target.
    elif normalized_target.startswith(f"{MARKER}:path:"):
        if not label_text:
            return None
        base_path = normalized_target[len(f"{MARKER}:path:") :].strip()
        if not base_path:
            inferred_text = label_text
        else:
            inferred_text = posixpath.join(base_path.rstrip("/"), label_text)
    # Allow explicit targets when the link text is only display text.
    elif normalized_target.startswith(f"{MARKER}:"):
        inferred_text = normalized_target[len(f"{MARKER}:") :]
    else:
        return None

    text = inferred_text.strip()
    if not text:
        return None

    issue_match = ISSUE_PATTERN.match(text)
    if issue_match is not None:
        return "issue", issue_match.group(1)

    if text.lower() == "gh:version":
        return "current-version", ""

    if VERSION_PATTERN.match(text):
        return "specific-version", text

    if text == project_name:
        return "project-root", ""

    return "source", text


@lru_cache(maxsize=2048)
def _resolve_repo_object(repo_root: Path, path_text: str) -> tuple[str, str] | None:
    """Resolve a repository file or directory from an explicit repository path."""
    # Normalize the provided path-like text before looking at the local repository.
    normalized_path = posixpath.normpath(
        path_text.strip().replace("\\", "/").lstrip("/")
    )
    if not normalized_path or normalized_path == ".":
        return None

    # Prefer an exact repository-relative match for deterministic resolution.
    repo_root_resolved = repo_root.resolve()
    exact_path = (repo_root / normalized_path).resolve()
    if exact_path.is_relative_to(repo_root_resolved):
        relative_path = exact_path.relative_to(repo_root_resolved).as_posix()
        if exact_path.is_file():
            return "file", relative_path
        if exact_path.is_dir():
            return "dir", relative_path

    return None


def _current_version_url(context: GithubLinkContext) -> str:
    """Return the repository URL representing the current configured version."""
    if context.release.is_unstable:
        if context.release.commit_hash:
            return f"{context.repo_url}/tree/{context.release.commit_hash}"
        return f"{context.repo_url}/tree/main"
    return f"{context.repo_url}/releases/tag/{context.release.tag_name}"


def _resolve_source_url(
    source_path_text: str,
    marker_text: str,
    context: GithubLinkContext,
    line: int | None,
) -> str:
    """Resolve the GitHub source URL for a validated repository path target."""
    resolved_object = _resolve_repo_object(context.repo_root, source_path_text)
    if resolved_object is None:
        line_info = f":{line}" if line is not None else ""
        raise SphinxError(
            "[github-links] "
            f"Unable to resolve local source path '{source_path_text}' "
            f"from marker '{marker_text.strip()}' "
            f"in {context.docname}{line_info}. "
            "Expected an existing repository file or directory identified by path."
        )

    object_kind, object_path = resolved_object
    if context.release.is_unstable:
        base_ref = context.release.commit_hash or "main"
    else:
        base_ref = context.release.tag_name

    if object_kind == "file":
        return f"{context.repo_url}/blob/{base_ref}/{object_path}"
    return f"{context.repo_url}/tree/{base_ref}/{object_path}"


def _resolve_link(
    target_text: str,
    label_text: str,
    *,
    context: GithubLinkContext,
    line: int | None,
) -> tuple[str, str] | None:
    """Resolve a markdown link target handled by this extension.

    None is returned if the MARKER does not match target_text.
    """
    # Decode marker syntax and classify the semantic target in one step.
    target = _classify_target(target_text, label_text, context.project_name)
    if target is None:
        return None
    kind, resolved_target_text = target

    # Build the final URL directly from the classified target kind.
    if kind == "issue":
        return f"{context.repo_url}/issues/{resolved_target_text}", kind
    if kind == "specific-version":
        return f"{context.repo_url}/releases/tag/{resolved_target_text}", kind
    if kind == "current-version":
        return _current_version_url(context), kind
    if kind == "project-root":
        return context.repo_url, kind
    if kind == "source":
        return (
            _resolve_source_url(
                resolved_target_text,
                target_text,
                context,
                line,
            ),
            kind,
        )

    # The target classifier currently emits the above kinds only.
    # Keep an explicit error so mismatches fail loudly during development.
    raise SphinxError(
        "[github-links] "
        f"Internal error: unsupported target kind '{kind}' "
        f"for marker '{target_text.strip()}' in {context.docname}."
    )


# ---------------------------------------------------------------------------
# Decorating Links
# ---------------------------------------------------------------------------


def _is_code_render_kind(kind: str) -> bool:
    """Return whether the rendered label should use a code-style appearance."""
    return kind in {"source", "specific-version", "current-version"}


def _decorate_reference(
    reference_node: nodes.reference,
    label_text: str,
    kind: str,
) -> None:
    """Apply consistent APPXC-specific styling and icon decoration."""
    # Compute the displayed label and accumulated CSS classes first.
    display_text = label_text
    classes: list[str] = [
        str(css_class) for css_class in reference_node.get("classes", [])
    ]
    if "appxc-gh-link" not in classes:
        classes.append("appxc-gh-link")
    if _is_code_render_kind(kind):
        classes.append("appxc-gh-link-code")
    else:
        classes.append("appxc-gh-link-textual")
    reference_node["classes"] = classes

    # Replace children so the rendered structure is fully controlled.
    reference_node.children = []
    if _is_code_render_kind(kind):
        reference_node += nodes.literal(
            display_text,
            display_text,
            classes=["appxc-gh-link-text"],
        )
    else:
        reference_node += nodes.Text(display_text)

    # Append the GitHub icon in a dedicated wrapper for styling hooks.
    icon_tail = nodes.inline("", "", classes=["appxc-gh-link-tail"])
    icon_tail += nodes.Text("\u00a0")
    icon = nodes.inline(
        "",
        "",
        classes=["appxc-gh-link-icon", "fa-brands", "fa-github"],
    )
    icon["aria-hidden"] = "true"
    icon_tail += icon
    reference_node += icon_tail


# ---------------------------------------------------------------------------
# Main Entry Point
# ---------------------------------------------------------------------------
# After the hookup with sphinx, the function below is the main entry point, iterating
# over all relevant nodes and (1) resolving the link before (2) decorating it.


def _resolve_doctree_link_nodes(
    doctree: nodes.document,
    *,
    context: GithubLinkContext,
) -> None:
    """Resolve and decorate all GitHub-link capable nodes in the doctree."""

    def _try_resolve(node: nodes.Node, target_text: str) -> tuple[str, str, str] | None:
        """Resolve target_text; return (label_text, resolved_url, kind) or None."""
        label_text = node.astext()
        resolved_link = _resolve_link(
            target_text,
            label_text,
            context=context,
            line=node.line,
        )
        if resolved_link is None:
            return None
        resolved_url, kind = resolved_link
        return label_text, resolved_url, kind

    # Handle MyST pending references before they are resolved by other Sphinx stages.
    # Resolved references replace the pending node with a concrete reference node.
    for pending_xref_node in list(doctree.findall(addnodes.pending_xref)):
        target_text = pending_xref_node.get("reftarget")
        if not isinstance(target_text, str):
            continue
        resolved = _try_resolve(pending_xref_node, target_text)
        if resolved is None:
            continue
        label_text, resolved_url, kind = resolved
        reference_node = nodes.reference("", "", refuri=resolved_url)
        _decorate_reference(reference_node, label_text, kind)
        pending_xref_node.replace_self(reference_node)

    # Handle plain reference nodes that already carry a concrete ``refuri``.
    # Resolved references update the existing node in place.
    for reference_node in doctree.findall(nodes.reference):
        target_text = reference_node.get("refuri")
        if not isinstance(target_text, str):
            continue
        resolved = _try_resolve(reference_node, target_text)
        if resolved is None:
            continue
        label_text, resolved_url, kind = resolved
        reference_node["refuri"] = resolved_url
        _decorate_reference(reference_node, label_text, kind)


# ---------------------------------------------------------------------------
# Hookup with sphinx
# ---------------------------------------------------------------------------


def _validated_repo_root_from_confdir(confdir_text: str) -> Path:
    """Resolve and validate the repository root derived from ``conf.py``."""
    confdir = Path(confdir_text).resolve()
    repo_root = confdir.parent
    if not repo_root.is_dir():
        raise SphinxError(
            "[github-links] "
            f"Derived repository root '{repo_root}' from confdir '{confdir}' "
            "is not an existing directory."
        )
    return repo_root


def _resolve_doctree_links(
    app: Sphinx,
    doctree: nodes.document,
    docname: str | None = None,
) -> None:
    """Main entry after Sphinx hookup: collect inputs, then resolve+decorate nodes."""
    # Merge both hookup paths: resolve docname from the hook arg or from source path.
    if docname is None:
        source_path = doctree.get("source")
        if isinstance(source_path, str):
            resolved_docname = app.env.path2doc(source_path)
            docname = resolved_docname if resolved_docname is not None else "<unknown>"
        else:
            docname = "<unknown>"

    # Build shared resolution input once per doctree processing run.
    repo_root = _validated_repo_root_from_confdir(app.confdir)
    context = GithubLinkContext(
        repo_url=app.config.github_links_repo_url.rstrip("/"),
        release=_release_context(app.config.release),
        project_name=app.config.project,
        repo_root=repo_root,
        docname=docname,
    )

    _resolve_doctree_link_nodes(
        doctree,
        context=context,
    )


def _resolve_doctree_links_on_resolved(
    app: Sphinx,
    doctree: nodes.document,
    docname: str,
) -> None:
    """Handle ``doctree-resolved`` by delegating into the shared main entry."""
    _resolve_doctree_links(app, doctree, docname)


def setup(app: Sphinx) -> dict[str, bool]:
    """Register configuration values and doctree hooks for GitHub link rewriting."""
    app.add_config_value("github_links_repo_url", "", "env", [str])
    app.connect("doctree-read", _resolve_doctree_links)
    app.connect("doctree-resolved", _resolve_doctree_links_on_resolved)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
