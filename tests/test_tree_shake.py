"""Tests for the DJANGD_FRAMEWORK settings-based component filter and the
``djangd_build_css`` management command's component selection logic."""
from __future__ import annotations

import importlib

import pytest
from django.test import override_settings

from djangd_framework.registry import registry


def _reload_components() -> None:
    """Re-import the components package to re-apply the settings filter.

    The filter runs at import time (so AppConfig.ready can do its
    ``from . import components`` with the user's settings already loaded).
    Tests need to swap settings on a fresh registry, so we clear builtins,
    reload, and let registration + filter happen again.
    """
    registry.clear(source="builtin")
    import djangd_framework.components as _components

    importlib.reload(_components)


@pytest.fixture(autouse=True)
def _restore_registry():
    """Make sure each test starts from (and leaves behind) the full registry."""
    _reload_components()
    yield
    _reload_components()


def test_no_settings_keeps_every_builtin():
    names = set(registry.all())
    # A representative sample — every group should be represented.
    assert "button" in names
    assert "card" in names
    assert "alert" in names
    assert "modal" in names
    assert "carousel" in names
    assert len(names) >= 70


def test_include_components_whitelist():
    with override_settings(
        DJANGD_FRAMEWORK={"INCLUDE_COMPONENTS": ["button", "card"]}
    ):
        _reload_components()
        names = set(registry.all())
        assert names == {"button", "card"}


def test_include_groups_whitelist():
    with override_settings(DJANGD_FRAMEWORK={"INCLUDE_GROUPS": ["feedback"]}):
        _reload_components()
        names = set(registry.all())
        # Every kept component must be in the feedback group.
        for n in names:
            assert registry.get(n).group == "feedback"
        # And it isn't empty.
        assert {"alert", "snackbar", "dialog"} <= names


def test_exclude_components():
    with override_settings(
        DJANGD_FRAMEWORK={"EXCLUDE_COMPONENTS": ["carousel", "command"]}
    ):
        _reload_components()
        names = set(registry.all())
        assert "carousel" not in names
        assert "command" not in names
        # Other components remain.
        assert "button" in names


def test_exclude_groups():
    with override_settings(DJANGD_FRAMEWORK={"EXCLUDE_GROUPS": ["overlays"]}):
        _reload_components()
        names = set(registry.all())
        assert "modal" not in names
        assert "popover" not in names
        assert "sheet" not in names
        assert "button" in names


def test_include_and_exclude_combine():
    """An exclude beats an include — useful for opting out of a single
    component in an otherwise whole-group include."""
    with override_settings(
        DJANGD_FRAMEWORK={
            "INCLUDE_GROUPS": ["inputs"],
            "EXCLUDE_COMPONENTS": ["transfer_list"],
        }
    ):
        _reload_components()
        names = set(registry.all())
        assert "button" in names
        assert "transfer_list" not in names
        # And nothing from outside the inputs group leaked in.
        for n in names:
            assert registry.get(n).group == "inputs"


def test_group_metadata_present():
    """Every built-in component declares a group and at least one SCSS
    partial — the CSS subset build relies on this."""
    for name in registry.all():
        cls = registry.get(name)
        group = cls.group
        assert group in {
            "inputs",
            "surfaces",
            "navigation",
            "data",
            "feedback",
            "overlays",
            "layout",
            "utility",
            "misc",
        }, f"{name} has unknown group {group!r}"
        # Utility components (icon, visually_hidden) don't need a partial.
        if group != "utility":
            assert cls.scss_partials, f"{name} has no SCSS partials declared"


def test_build_css_dry_run_reflects_filter():
    from io import StringIO
    from django.core.management import call_command

    with override_settings(
        DJANGD_FRAMEWORK={"INCLUDE_COMPONENTS": ["button", "card", "alert"]}
    ):
        _reload_components()
        out = StringIO()
        call_command("djangd_build_css", "--dry-run", stdout=out)
        text = out.getvalue()
        # Components listed
        assert "button (inputs)" in text
        assert "card (surfaces)" in text
        assert "alert (feedback)" in text
        # Partials listed for those three only
        assert "components/_button.scss" in text
        assert "components/_card.scss" in text
        assert "components/_feedback.scss" in text
        # And nothing from filtered-out partials
        assert "components/_carousel.scss" not in text
        assert "components/_layout-extras.scss" not in text
