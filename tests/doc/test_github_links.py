# Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)
# SPDX-License-Identifier: 0BSD
import importlib.util
import sys
from pathlib import Path

import pytest
from sphinx.errors import SphinxError


def _load_github_links_module():
    module_path = (
        Path(__file__).resolve().parents[2] / "doc" / "_ext" / "github_links.py"
    )
    module_name = "appxc_doc_github_links"
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    assert spec is not None
    assert spec.loader is not None

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


github_links = _load_github_links_module()


def _make_context(
    release_name: str,
    *,
    repo_root: Path = Path("."),
    docname: str = "dev/references/deployment",
):
    return github_links.GithubLinkContext(
        repo_url="https://github.com/alexander-nbg/appxc",
        release=github_links._release_context(release_name),
        project_name="APPXC",
        repo_root=repo_root,
        docname=docname,
    )


def test_release_context_collects_derived_attributes():
    release = github_links._release_context("0.1.2.dev5+gabc1234")

    assert release.full_name == "0.1.2.dev5+gabc1234"
    assert release.tag_name == "0.1.2.dev5"
    assert release.base_version == "0.1.2"
    assert release.is_dev is True
    assert release.is_local is True
    assert release.is_unstable is True
    assert release.commit_hash == "abc1234"


def test_version_policy_for_normal_release():
    context = _make_context("0.1.2")
    assert (
        github_links._current_version_url(context)
        == "https://github.com/alexander-nbg/appxc/releases/tag/0.1.2"
    )


def test_version_policy_for_dev_release():
    context = _make_context("0.1.2.dev5")
    assert (
        github_links._current_version_url(context)
        == "https://github.com/alexander-nbg/appxc/tree/main"
    )


def test_version_policy_prefers_git_commit_for_unstable_release():
    context = _make_context("0.1.2.dev5+gabc1234")
    assert (
        github_links._current_version_url(context)
        == "https://github.com/alexander-nbg/appxc/tree/abc1234"
    )


def test_resolve_link_builds_supported_non_source_targets():
    context = _make_context("0.2.0+gabc1234")

    assert github_links._resolve_link(
        "gh:#12",
        "ignored",
        context=context,
        line=10,
    ) == ("https://github.com/alexander-nbg/appxc/issues/12", "issue")
    assert github_links._resolve_link(
        "gh:0.0.2",
        "ignored",
        context=context,
        line=11,
    ) == (
        "https://github.com/alexander-nbg/appxc/releases/tag/0.0.2",
        "specific-version",
    )
    assert github_links._resolve_link(
        "gh:gh:version",
        "ignored",
        context=context,
        line=12,
    ) == (
        "https://github.com/alexander-nbg/appxc/tree/abc1234",
        "current-version",
    )
    assert github_links._resolve_link(
        "gh:APPXC",
        "ignored",
        context=context,
        line=13,
    ) == ("https://github.com/alexander-nbg/appxc", "project-root")


def test_classify_target_for_primary_marker_issue_and_version():
    assert github_links._classify_target("gh", "#12", "APPXC") == ("issue", "12")
    assert github_links._classify_target("gh", "gh:version", "APPXC") == (
        "current-version",
        "",
    )
    assert github_links._classify_target("gh", "0.0.2", "APPXC") == (
        "specific-version",
        "0.0.2",
    )
    assert github_links._classify_target("gh", "v0.0.2", "APPXC") == (
        "specific-version",
        "v0.0.2",
    )
    assert github_links._classify_target(
        "gh",
        "doc/dev/concepts/doc_github_links.md",
        "APPXC",
    ) == (
        "source",
        "doc/dev/concepts/doc_github_links.md",
    )


def test_classify_target_rejects_empty_value():
    assert github_links._classify_target("gh", "", "APPXC") is None


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Issue #42", "Issue #42"),
        ("`Issue #42`", "`Issue #42`"),
        ("0.0.2.dev4", "0.0.2.dev4"),
        ("v1.2.3.dev5", "v1.2.3.dev5"),
    ],
)
def test_classify_target_leaves_removed_shorthand_as_source(
    text: str,
    expected: str,
):
    assert github_links._classify_target("gh", text, "APPXC") == ("source", expected)


def test_classify_target_supports_project_name():
    assert github_links._classify_target("gh", "APPXC", "APPXC") == (
        "project-root",
        "",
    )


def test_classify_target_respects_non_marker_links():
    assert (
        github_links._classify_target("https://example.org", "label", "APPXC") is None
    )


def test_resolve_repo_object_supports_directory(tmp_path: Path):
    (tmp_path / "doc" / "dev").mkdir(parents=True)
    assert github_links._resolve_repo_object(tmp_path, "doc/dev") == (
        "dir",
        "doc/dev",
    )


def test_resolve_link_supports_marker_override_for_issue_and_version(tmp_path: Path):
    context = _make_context("0.2.0", repo_root=tmp_path)

    assert github_links._resolve_link(
        "gh:#42",
        "issue",
        context=context,
        line=29,
    ) == ("https://github.com/alexander-nbg/appxc/issues/42", "issue")
    assert github_links._resolve_link(
        "gh:v1.2.3",
        "some version",
        context=context,
        line=29,
    ) == (
        "https://github.com/alexander-nbg/appxc/releases/tag/v1.2.3",
        "specific-version",
    )


def test_resolve_link_raises_human_readable_error_for_missing_source(tmp_path: Path):
    context = _make_context("0.2.0", repo_root=tmp_path)

    with pytest.raises(SphinxError, match="Unable to resolve local source path"):
        github_links._resolve_link(
            "gh",
            "does-not-exist.py",
            context=context,
            line=29,
        )


def test_resolve_link_supports_filename_plus_path_marker(tmp_path: Path):
    context = _make_context(
        "0.2.0",
        repo_root=tmp_path,
        docname="doc/dev/concepts/doc_github_links",
    )
    repo_root = tmp_path
    (repo_root / "doc" / "dev" / "concepts").mkdir(parents=True)
    (repo_root / "doc" / "dev" / "concepts" / "doc_github_links.md").write_text(
        "test",
        encoding="utf-8",
    )

    assert github_links._resolve_link(
        "gh:path:doc/dev/concepts",
        "doc_github_links.md",
        context=context,
        line=50,
    ) == (
        "https://github.com/alexander-nbg/appxc/blob/0.2.0/"
        "doc/dev/concepts/doc_github_links.md",
        "source",
    )


@pytest.mark.parametrize(
    ("input_text", "expected"),
    [
        ("src\\requirements.txt", "src/requirements.txt"),
        ("/src/requirements.txt", "src/requirements.txt"),
        ("src/../pyproject.toml", "pyproject.toml"),
    ],
)
def test_resolve_repo_object_normalizes_repo_relative_path(
    tmp_path: Path,
    input_text: str,
    expected: str,
):
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "requirements.txt").write_text("x", encoding="utf-8")
    (tmp_path / "pyproject.toml").write_text("x", encoding="utf-8")

    assert github_links._resolve_repo_object(tmp_path, input_text) == ("file", expected)


def test_resolve_repo_object_exact_existing_file(tmp_path: Path):
    (tmp_path / "src").mkdir()
    existing_file = tmp_path / "src" / "a.py"
    existing_file.write_text("print('x')", encoding="utf-8")

    assert github_links._resolve_repo_object(tmp_path, "src/a.py") == (
        "file",
        "src/a.py",
    )


def test_resolve_repo_object_basename_only_returns_none(tmp_path: Path):
    (tmp_path / "a").mkdir()
    existing_file = tmp_path / "a" / "target.py"
    existing_file.write_text("print('x')", encoding="utf-8")

    assert github_links._resolve_repo_object(tmp_path, "target.py") is None


def test_resolve_repo_object_missing_returns_none(tmp_path: Path):
    assert github_links._resolve_repo_object(tmp_path, "missing.py") is None
