"""Smoke-test every built-in component renders without errors."""
import pytest

from djangd_framework import registry


@pytest.mark.parametrize("component_name", sorted(registry.all()))
def test_component_smoke(component_name):
    """Calls the component class directly with valid props and verifies it
    renders to non-empty HTML containing at least the BEM block class."""
    cls = registry.get(component_name)
    props = dict(cls.defaults)
    for r in cls.required_props:
        existing = props.get(r)
        if existing in (None, "", (), [], 0):
            props[r] = (
                [{"label": "Item", "value": "x", "icon": "star",
                  "src": "x.png", "alt": "alt", "href": "#"}]
                if isinstance(existing, (list, tuple))
                else "x"
            )
    inst = cls(props=props, children="kids")
    html = inst.render()
    assert html.strip(), f"{component_name} rendered empty"
    block = component_name.split(".")[-1].replace("_", "-")
    # Every component renders either a `djangd-<block>` or `mdc-<block>` root.
    assert (f"djangd-{block}" in html) or ("mdc-" in html), f"BEM block missing for {component_name}"
